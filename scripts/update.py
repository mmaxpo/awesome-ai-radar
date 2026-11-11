"""Read repos.yml, fetch details for each repo from GitHub, and write:
  - README.md            overview + "what's new"
  - repos/<owner>__<name>.md   a detail sheet for every repo
  - repos.csv            all repos in one table (GitHub shows it as a searchable sheet)
"""
import csv
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SHEETS = ROOT / "repos"
NEW_DAYS = 7  # anything pushed/released within this many days counts as "new"
STATUS_ORDER = [
    ("using", "🛠 Using"),
    ("study", "📚 To study"),
    ("later", "⏳ Maybe later"),
    ("done", "✅ Done"),
]
TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ---------- GitHub API ----------

def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read()
            return json.loads(body) if body.strip() else None
    except urllib.error.HTTPError as e:
        if e.code in (404, 409, 451):  # missing, empty repo, blocked
            return None
        raise
    except json.JSONDecodeError:
        return None


def parse_time(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def clean(s, limit=None):
    s = (s or "").replace("|", "/").replace("\r", "")
    return s[:limit] + "…" if limit and len(s) > limit else s


def fetch(entry):
    name = str(entry["repo"]).strip().strip("/")
    if "github.com/" in name:
        name = name.split("github.com/")[1].strip("/")
    info = api(f"/repos/{name}")
    if info is None:
        return {**entry, "repo": name, "missing": True}

    releases = [r for r in (api(f"/repos/{name}/releases?per_page=5") or []) if not r.get("draft")]
    stable = [r for r in releases if not r.get("prerelease")]
    latest = (stable or releases or [None])[0]
    commits = api(f"/repos/{name}/commits?per_page=10") or []
    languages = api(f"/repos/{name}/languages") or {}
    contributors = api(f"/repos/{name}/contributors?per_page=5") or []
    lic = info.get("license") or {}

    return {
        **entry,
        "repo": name,
        "missing": False,
        "description": clean(info.get("description")),
        "homepage": info.get("homepage") or "",
        "topics": info.get("topics") or [],
        "stars": info.get("stargazers_count", 0),
        "forks": info.get("forks_count", 0),
        "open_issues": info.get("open_issues_count", 0),
        "language": info.get("language") or "",
        "languages": languages,
        "license": lic.get("spdx_id") if lic.get("spdx_id") not in (None, "NOASSERTION") else (lic.get("name") or ""),
        "archived": info.get("archived", False),
        "fork_of": (info.get("parent") or {}).get("full_name", ""),
        "default_branch": info.get("default_branch", ""),
        "size_mb": round(info.get("size", 0) / 1024, 1),
        "created": parse_time(info.get("created_at")),
        "pushed": parse_time(info.get("pushed_at")),
        "release_tag": latest.get("tag_name") if latest else None,
        "release_url": latest.get("html_url") if latest else None,
        "release_date": parse_time(latest.get("published_at")) if latest else None,
        "releases": [{
            "tag": r.get("tag_name"),
            "name": r.get("name") or "",
            "url": r.get("html_url"),
            "date": parse_time(r.get("published_at")),
            "pre": r.get("prerelease", False),
            "body": r.get("body") or "",
        } for r in releases],
        "commits": [{
            "msg": clean(c["commit"]["message"].splitlines()[0] if c["commit"]["message"] else "", 100),
            "date": parse_time(c["commit"]["author"]["date"]) if c["commit"].get("author") else None,
            "author": (c.get("author") or {}).get("login") or (c["commit"].get("author") or {}).get("name", ""),
            "url": c.get("html_url"),
        } for c in commits if c.get("commit")],
        "contributors": [(c.get("login"), c.get("contributions", 0)) for c in contributors
                         if isinstance(c, dict) and c.get("login")],
    }


# ---------- formatting helpers ----------

def ago(dt, now):
    if not dt:
        return "—"
    days = (now - dt).days
    if days <= 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 30:
        return f"{days}d ago"
    if days < 365:
        return f"{days // 30}mo ago"
    return f"{days // 365}y ago"


def fmt_num(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def day(dt):
    return f"{dt:%Y-%m-%d}" if dt else "—"


def sheet_path(repo):
    return f"repos/{repo.replace('/', '__')}.md"


def is_new(it, key, now):
    d = it.get(key)
    return d is not None and (now - d).days < NEW_DAYS


def lang_bar(languages):
    total = sum(languages.values())
    if not total:
        return "—"
    parts = sorted(languages.items(), key=lambda kv: -kv[1])
    shown = [f"{k} {v * 100 / total:.0f}%" for k, v in parts[:5] if v * 100 / total >= 1]
    return " · ".join(shown) or "—"


def release_notes(body, max_lines=6):
    lines = [l.rstrip() for l in body.replace("\r", "").splitlines() if l.strip()]
    lines = [l for l in lines if not l.lstrip().startswith("<!--")]
    lines = [("**" + l.lstrip("# ").strip() + "**") if l.lstrip().startswith("#") else l for l in lines]
    out = lines[:max_lines]
    if len(lines) > max_lines:
        out.append("…")
    return "\n".join("> " + l for l in out) if out else "> _No notes._"


# ---------- detail sheet per repo ----------

def render_sheet(it, now):
    r = it["repo"]
    gh = f"https://github.com/{r}"
    L = [f"# {r}", "", "[← Back to radar](../README.md) · [Open on GitHub ↗]({})".format(gh), ""]
    if it["missing"]:
        L += ["⚠️ **This repo wasn't found** — it may have been renamed, made private or deleted.", ""]
    elif it["description"]:
        L += [f"> {it['description']}", ""]

    # my notes
    L += ["## 📝 My notes", "",
          "| | |", "|---|---|",
          f"| **Status** | {it.get('status') or '—'} |",
          f"| **Project** | {it.get('project') or '—'} |",
          f"| **Why I saved it** | {clean(str(it.get('why') or '—'))} |"]
    if it.get("added"):
        L.append(f"| **Added** | {it['added']} |")
    L.append("")
    if it.get("notes"):
        L += [str(it["notes"]).strip(), ""]
    if it["missing"]:
        return "\n".join(L)

    badges = []
    if it["archived"]:
        badges.append("🗄 **Archived** — no longer maintained")
    if is_new(it, "pushed", now) or is_new(it, "release_date", now):
        badges.append(f"🆕 **Active this week**")
    if badges:
        L += [" · ".join(badges), ""]

    # facts
    topics = " ".join(f"`{t}`" for t in it["topics"]) or "—"
    L += ["## 📊 At a glance", "",
          "| | |", "|---|---|",
          f"| ⭐ **Stars** | {fmt_num(it['stars'])} |",
          f"| 🍴 **Forks** | {fmt_num(it['forks'])} |",
          f"| 🐞 **Open issues + PRs** | [{fmt_num(it['open_issues'])}]({gh}/issues) |",
          f"| 💻 **Languages** | {lang_bar(it['languages'])} |",
          f"| 📜 **License** | {it['license'] or '—'} |",
          f"| 🏷 **Topics** | {topics} |",
          f"| 🕒 **Last activity** | {day(it['pushed'])} ({ago(it['pushed'], now)}) |",
          f"| 📅 **Created** | {day(it['created'])} |",
          f"| 📦 **Latest release** | " + (f"[{it['release_tag']}]({it['release_url']}) — {day(it['release_date'])}" if it["release_tag"] else "—") + " |",
          f"| 🌿 **Default branch** | `{it['default_branch']}` |",
          f"| 💾 **Size** | {it['size_mb']} MB |"]
    if it["homepage"]:
        L.append(f"| 🌐 **Website** | {it['homepage']} |")
    if it["fork_of"]:
        L.append(f"| 🔀 **Fork of** | [{it['fork_of']}](https://github.com/{it['fork_of']}) |")
    L.append("")

    # releases
    L += ["## 📦 Recent releases", ""]
    if it["releases"]:
        for rel in it["releases"]:
            pre = " _(pre-release)_" if rel["pre"] else ""
            title = f" — {clean(rel['name'], 80)}" if rel["name"] and rel["name"] != rel["tag"] else ""
            L += [f"### [{rel['tag']}]({rel['url']}){title}{pre}",
                  f"<sub>{day(rel['date'])} · {ago(rel['date'], now)}</sub>", "",
                  release_notes(rel["body"]), ""]
    else:
        L += ["_No releases — this project doesn't publish versions; follow the commits below._", ""]

    # commits
    L += ["## 🔨 Latest commits", "", "| Date | Change | By |", "|---|---|---|"]
    for c in it["commits"]:
        L.append(f"| {day(c['date'])} | [{c['msg']}]({c['url']}) | {c['author']} |")
    if not it["commits"]:
        L.append("| — | _No commits found_ | |")
    L += ["", f"[See all commits ↗]({gh}/commits)", ""]

    # contributors
    if it["contributors"]:
        L += ["## 👥 Top contributors", "",
              " · ".join(f"[{u}](https://github.com/{u}) ({n})" for u, n in it["contributors"]), ""]

    L += ["## ⬇️ Get it", "", "```bash", f"git clone https://github.com/{r}.git", "```", ""]
    return "\n".join(L)


# ---------- README overview ----------

def render_readme(items, now):
    L = [
        "# 📡 My Repo Radar",
        "",
        "Repos I'm following. Edit [`repos.yml`](repos.yml) to add or remove one;",
        "this page refreshes automatically every day. Click a repo name for its full sheet,",
        "or open [`repos.csv`](repos.csv) to see everything in one sortable table.",
        "",
        f"_Last updated: {now:%Y-%m-%d %H:%M} UTC · {len(items)} repos_",
        "",
    ]

    fresh = [it for it in items if not it["missing"]
             and (is_new(it, "release_date", now) or is_new(it, "pushed", now))]
    fresh.sort(key=lambda it: max(d for d in (it.get("release_date"), it.get("pushed")) if d), reverse=True)

    L += [f"## 🔥 What's new (last {NEW_DAYS} days)", ""]
    for it in fresh:
        r = it["repo"]
        link = f"**[{r}]({sheet_path(r)})**"
        if is_new(it, "release_date", now):
            L.append(f"- {link} — new release [{it['release_tag']}]({it['release_url']}) "
                     f"({ago(it['release_date'], now)})")
        else:
            msg = it["commits"][0]["msg"] if it["commits"] else ""
            L.append(f"- {link} — new commits ({ago(it['pushed'], now)})" + (f": _{msg}_" if msg else ""))
    if not fresh:
        L.append("_Nothing new this week._")
    L.append("")

    known = {s for s, _ in STATUS_ORDER}
    for status, title in list(STATUS_ORDER) + [("other", "📁 Other")]:
        group = [it for it in items
                 if (it.get("status") or "other") == status
                 or (status == "other" and (it.get("status") or "other") not in known)]
        if not group:
            continue
        group.sort(key=lambda it: it.get("pushed") or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
        L += [f"## {title} ({len(group)})", "",
              "| Repo | Why I saved it | Project | ⭐ | Last activity | Latest release |",
              "|---|---|---|---|---|---|"]
        for it in group:
            r = it["repo"]
            why = clean(str(it.get("why") or ""))
            project = it.get("project") or ""
            if it["missing"]:
                L.append(f"| [`{r}`]({sheet_path(r)}) ⚠️ not found | {why} | {project} | | | |")
                continue
            flag = " 🆕" if is_new(it, "pushed", now) or is_new(it, "release_date", now) else ""
            flag += " 🗄" if it["archived"] else ""
            desc = f"<br><sub>{clean(it['description'], 120)}</sub>" if it["description"] else ""
            rel = (f"[{it['release_tag']}]({it['release_url']}) · {ago(it['release_date'], now)}"
                   if it["release_tag"] else "—")
            L.append(f"| [**{r}**]({sheet_path(r)}){flag}{desc} | {why} | {project} "
                     f"| {fmt_num(it['stars'])} | {ago(it['pushed'], now)} | {rel} |")
        L.append("")
    L += ["---", "🆕 active in the last 7 days · 🗄 archived · ⚠️ repo not found", ""]
    return "\n".join(L)


# ---------- CSV ----------

def write_csv(items, path):
    cols = ["repo", "url", "status", "project", "why", "description", "language", "stars", "forks",
            "open_issues", "license", "topics", "last_activity", "latest_release", "release_date",
            "created", "archived"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for it in items:
            m = it["missing"]
            w.writerow([
                it["repo"], f"https://github.com/{it['repo']}", it.get("status") or "",
                it.get("project") or "", it.get("why") or "",
                "" if m else it["description"], "" if m else it["language"],
                "" if m else it["stars"], "" if m else it["forks"], "" if m else it["open_issues"],
                "" if m else it["license"], "" if m else " ".join(it["topics"]),
                "" if m else day(it["pushed"]), "" if m else (it["release_tag"] or ""),
                "" if m else day(it["release_date"]), "" if m else day(it["created"]),
                "NOT FOUND" if m else ("yes" if it["archived"] else "no"),
            ])


def main():
    entries = yaml.safe_load((ROOT / "repos.yml").read_text()) or []
    items = []
    for e in entries:
        if not isinstance(e, dict) or not e.get("repo"):
            continue
        print(f"Checking {e['repo']}…", file=sys.stderr)
        items.append(fetch(e))
    now = datetime.now(timezone.utc)

    SHEETS.mkdir(exist_ok=True)
    for old in SHEETS.glob("*.md"):  # remove sheets of repos you deleted from the list
        old.unlink()
    for it in items:
        (ROOT / sheet_path(it["repo"])).write_text(render_sheet(it, now), encoding="utf-8")

    (ROOT / "README.md").write_text(render_readme(items, now), encoding="utf-8")
    write_csv(items, ROOT / "repos.csv")
    print(f"Updated README, repos.csv and {len(items)} repo sheets.", file=sys.stderr)


if __name__ == "__main__":
    main()
