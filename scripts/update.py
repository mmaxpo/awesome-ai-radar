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
STALE_DAYS = 180  # no activity for this long -> marked 💤
CATEGORIES = {  # key used in repos.yml -> heading shown on the page (order = page order)
    "agents": "🤖 Agent frameworks & multi-agent",
    "coding": "💻 Coding agents & dev tools",
    "workflows": "🔁 Durable workflows & orchestration",
    "rag": "🧠 RAG, memory & chat with your data",
    "documents": "📄 Documents, OCR & web data",
    "models": "🖥 Models, local inference & gateways",
    "sdk": "🔌 MCP & SDKs",
    "builders": "🧩 Low-code builders & chat UIs",
    "prompting": "✍️ Prompting & LLM programming",
    "imagegen": "🖼 Image & video generation",
    "design": "🎨 Design & creative",
    "persian": "🇮🇷 Persian NLP",
    "learning": "📚 Awesome lists & learning",
    "apps": "🛠 Apps & other",
}
STATUS_ICON = {"using": "🛠 using", "study": "📚 study", "later": "⏳ later", "done": "✅ done"}
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
    moved_from = ""
    if info.get("full_name") and info["full_name"].lower() != name.lower():
        moved_from, name = name, info["full_name"]

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
        "moved_from": moved_from,
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


def fetch_org(entry):
    name = str(entry["org"]).strip().strip("/")
    if "github.com/" in name:
        name = name.split("github.com/")[1].strip("/")
    info = api(f"/users/{name}")
    if info is None:
        return {**entry, "org": name, "missing": True}
    kind = "orgs" if info.get("type") == "Organization" else "users"
    repos = api(f"/{kind}/{name}/repos?sort=pushed&per_page=30") or []
    repos = [r for r in repos if not r.get("fork") and not r.get("archived")]
    top = sorted(repos, key=lambda r: -r.get("stargazers_count", 0))[:6]
    return {
        **entry, "org": info.get("login", name), "missing": False,
        "display": info.get("name") or info.get("login", name),
        "description": clean(info.get("bio") or info.get("description") or ""),
        "public_repos": info.get("public_repos", 0),
        "top": [(r["full_name"], r.get("stargazers_count", 0), parse_time(r.get("pushed_at")),
                 clean(r.get("description"), 90)) for r in top],
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


def cat_title(key):
    key = (key or "").strip()
    if not key:
        return "📁 Uncategorized"
    return CATEGORIES.get(key.lower(), key[:1].upper() + key[1:])


def cat_anchor(title):
    import re
    return re.sub(r"[^a-z0-9 _-]", "", title.lower()).replace(" ", "-")  # same rule GitHub uses


def is_stale(it, now):
    d = it.get("pushed")
    return d is not None and (now - d).days > STALE_DAYS


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
          f"| **Category** | {cat_title(it.get('category'))} |",
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
    if it.get("moved_from"):
        badges.append(f"↪️ **Moved** — was `{it['moved_from']}`")
    if is_stale(it, now) and not it["archived"]:
        badges.append(f"💤 **Quiet** — no activity for {ago(it['pushed'], now).replace(' ago', '')}")
    if it["archived"]:
        badges.append("🗄 **Archived** — no longer maintained")
    if is_new(it, "pushed", now) or is_new(it, "release_date", now):
        badges.append("🆕 **Active this week**")
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

def render_readme(items, orgs, now):
    L = [
        "# 📡 My Repo Radar",
        "",
        "Repos I'm following, grouped by topic. Edit [`repos.yml`](repos.yml) to add or remove one;",
        "this page refreshes automatically every day. Click a repo name for its full sheet,",
        "or open [`repos.csv`](repos.csv) to see everything in one sortable table.",
        "",
        f"_Last updated: {now:%Y-%m-%d %H:%M} UTC · {len(items)} repo{'s' if len(items) != 1 else ''}"
        + (f" · {len(orgs)} organization{'s' if len(orgs) != 1 else ''}" if orgs else "") + "_",
        "",
    ]

    # what's new
    fresh = [it for it in items if not it["missing"]
             and (is_new(it, "release_date", now) or is_new(it, "pushed", now))]
    releases = [it for it in fresh if is_new(it, "release_date", now)]
    commits_only = [it for it in fresh if not is_new(it, "release_date", now)]
    releases.sort(key=lambda it: it["release_date"], reverse=True)
    commits_only.sort(key=lambda it: it["pushed"], reverse=True)

    L += [f"## 🔥 What's new (last {NEW_DAYS} days)", ""]
    if releases:
        L += ["**📦 New releases**", ""]
        for it in releases:
            r = it["repo"]
            L.append(f"- **[{r}]({sheet_path(r)})** — [{it['release_tag']}]({it['release_url']}) "
                     f"({ago(it['release_date'], now)}) · {cat_title(it.get('category'))}")
        L.append("")
    if commits_only:
        L += [f"<details><summary><b>🔨 New commits only</b> ({len(commits_only)} repos)</summary>", ""]
        for it in commits_only:
            r = it["repo"]
            msg = it["commits"][0]["msg"] if it["commits"] else ""
            L.append(f"- **[{r}]({sheet_path(r)})** ({ago(it['pushed'], now)})" + (f": _{msg}_" if msg else ""))
        L += ["", "</details>", ""]
    if not fresh:
        L += ["_Nothing new this week._", ""]

    # group by category
    groups = {}
    for it in items:
        groups.setdefault(cat_title(it.get("category")), []).append(it)
    order = [t for t in CATEGORIES.values() if t in groups]
    order += sorted(t for t in groups if t not in order and t != "📁 Uncategorized")
    if "📁 Uncategorized" in groups:
        order.append("📁 Uncategorized")

    L += ["## 🗂 Categories", ""]
    L += [" · ".join(f"[{t}](#{cat_anchor(t)}) ({len(groups[t])})" for t in order)]
    if orgs:
        L[-1] += f" · [🏢 Organizations](#{cat_anchor('🏢 Organizations')}) ({len(orgs)})"
    L.append("")

    for title in order:
        group = sorted(groups[title], key=lambda it: (it["missing"], -(it.get("stars") or 0)))
        L += [f"## {title}", "",
              "| Repo | Why I saved it | Status | ⭐ | Last activity | Latest release |",
              "|---|---|---|---|---|---|"]
        for it in group:
            r = it["repo"]
            why = clean(str(it.get("why") or ""))
            status = STATUS_ICON.get((it.get("status") or "").lower(), it.get("status") or "")
            if it.get("project"):
                why += f" <sub>· {clean(str(it['project']))}</sub>"
            if it["missing"]:
                L.append(f"| [`{r}`]({sheet_path(r)}) ⚠️ not found | {why} | {status} | | | |")
                continue
            flag = " 🆕" if is_new(it, "pushed", now) or is_new(it, "release_date", now) else ""
            flag += " 🗄" if it["archived"] else (" 💤" if is_stale(it, now) else "")
            flag += " ↪️" if it.get("moved_from") else ""
            desc = f"<br><sub>{clean(it['description'], 110)}</sub>" if it["description"] else ""
            rel = (f"[{it['release_tag']}]({it['release_url']}) · {ago(it['release_date'], now)}"
                   if it["release_tag"] else "—")
            L.append(f"| [**{r}**]({sheet_path(r)}){flag}{desc} | {why} | {status} "
                     f"| {fmt_num(it['stars'])} | {ago(it['pushed'], now)} | {rel} |")
        L.append("")

    if orgs:
        L += ["## 🏢 Organizations", ""]
        for o in orgs:
            if o["missing"]:
                L += [f"### `{o['org']}` ⚠️ not found", ""]
                continue
            why = f" — {clean(str(o['why']))}" if o.get("why") else ""
            L += [f"### [{o['display']}](https://github.com/{o['org']}){why}",
                  f"<sub>{o['description'] or ''} · {o['public_repos']} public repos</sub>", "",
                  "| Top repo | ⭐ | Last activity |", "|---|---|---|"]
            for full, stars, pushed, desc in o["top"]:
                d = f"<br><sub>{desc}</sub>" if desc else ""
                L.append(f"| [{full}](https://github.com/{full}){d} | {fmt_num(stars)} | {ago(pushed, now)} |")
            L.append("")

    L += ["---",
          f"🆕 active in the last {NEW_DAYS} days · 💤 quiet for over {STALE_DAYS // 30} months · "
          "🗄 archived · ↪️ moved/renamed · ⚠️ not found", ""]
    return "\n".join(L)


# ---------- CSV ----------

def write_csv(items, path, now):
    cols = ["repo", "url", "category", "status", "project", "why", "description", "language", "stars",
            "forks", "open_issues", "license", "topics", "last_activity", "latest_release",
            "release_date", "created", "health"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        order = list(CATEGORIES.values())
        rank = lambda t: order.index(t) if t in order else len(order)
        for it in sorted(items, key=lambda it: (rank(cat_title(it.get("category"))),
                                                cat_title(it.get("category")), -(it.get("stars") or 0))):
            m = it["missing"]
            if m:
                health = "not found"
            elif it["archived"]:
                health = "archived"
            elif is_stale(it, now):
                health = "quiet"
            else:
                health = "active"
            w.writerow([
                it["repo"], f"https://github.com/{it['repo']}",
                cat_title(it.get("category")).split(" ", 1)[-1], it.get("status") or "",
                it.get("project") or "", it.get("why") or "",
                "" if m else it["description"], "" if m else it["language"],
                "" if m else it["stars"], "" if m else it["forks"], "" if m else it["open_issues"],
                "" if m else it["license"], "" if m else " ".join(it["topics"]),
                "" if m else day(it["pushed"]), "" if m else (it["release_tag"] or ""),
                "" if m else day(it["release_date"]), "" if m else day(it["created"]), health,
            ])


def main():
    entries = yaml.safe_load((ROOT / "repos.yml").read_text()) or []
    items, orgs, seen = [], [], set()
    for e in entries:
        if not isinstance(e, dict):
            continue
        if e.get("org"):
            print(f"Checking org {e['org']}…", file=sys.stderr)
            orgs.append(fetch_org(e))
            continue
        if not e.get("repo"):
            continue
        print(f"Checking {e['repo']}…", file=sys.stderr)
        it = fetch(e)
        if it["repo"].lower() in seen:  # duplicate (or two names for a moved repo)
            continue
        seen.add(it["repo"].lower())
        items.append(it)
    now = datetime.now(timezone.utc)

    SHEETS.mkdir(exist_ok=True)
    for old in SHEETS.glob("*.md"):  # remove sheets of repos you deleted from the list
        old.unlink()
    for it in items:
        (ROOT / sheet_path(it["repo"])).write_text(render_sheet(it, now), encoding="utf-8")

    (ROOT / "README.md").write_text(render_readme(items, orgs, now), encoding="utf-8")
    write_csv(items, ROOT / "repos.csv", now)
    print(f"Updated README, repos.csv and {len(items)} repo sheets.", file=sys.stderr)


if __name__ == "__main__":
    main()
