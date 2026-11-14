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
GONE_DAYS = 730   # archived, or no activity for this long -> moved to "Discontinued & archived"
GONE_TITLE = "🪦 Discontinued & archived"
CATEGORIES = {  # key used in repos.yml -> heading shown on the page (order = page order)
    "agents": "🤖 Agent frameworks & multi-agent",
    "coding": "💻 Coding agents & dev tools",
    "workflows": "🔁 Durable workflows & orchestration",
    "skills": "🪄 Agent skills & guidance",
    "rag": "🧠 RAG, memory & chat with your data",
    "documents": "📄 Documents, OCR & web data",
    "models": "🖥 Models, local inference & gateways",
    "ml": "📈 Classic ML, data science & vision",
    "science": "🧬 AI for science",
    "sdk": "🔌 MCP & SDKs",
    "security": "🛡 Security & OSINT",
    "builders": "🧩 Low-code builders & chat UIs",
    "prompting": "✍️ Prompting & LLM programming",
    "imagegen": "🖼 Image & video generation",
    "design": "🎨 Design & creative",
    "python": "🐍 Python & backend tooling",
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


# ---------- GitHub GraphQL (fast path: one request per batch of repos) ----------

GQL_BATCH = 15
API_STATS = {"graphql": 0, "rest_fallback": 0, "cost": 0}
REPO_FIELDS = """
  nameWithOwner description homepageUrl stargazerCount forkCount isArchived createdAt pushedAt diskUsage
  parent { nameWithOwner }
  licenseInfo { spdxId name }
  primaryLanguage { name }
  repositoryTopics(first: 20) { nodes { topic { name } } }
  languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } }
  issues(states: OPEN) { totalCount }
  pullRequests(states: OPEN) { totalCount }
  releases(first: 5, orderBy: {field: CREATED_AT, direction: DESC}) {
    nodes { tagName name url publishedAt isPrerelease isDraft description }
  }
  defaultBranchRef { name target { ... on Commit {
    history(first: 10) { nodes { messageHeadline committedDate url author { name user { login } } } }
  } } }
"""


def gql(query):
    req = urllib.request.Request("https://api.github.com/graphql",
                                 data=json.dumps({"query": query}).encode(), method="POST")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.load(r)
    API_STATS["graphql"] += 1
    API_STATS["cost"] += ((out.get("data") or {}).get("rateLimit") or {}).get("cost", 0)
    return out


def entry_name(entry, key="repo"):
    name = str(entry[key]).strip().strip("/")
    if "github.com/" in name:
        name = name.split("github.com/")[1].strip("/")
    return name


def node_to_item(entry, requested, n):
    full = n.get("nameWithOwner") or requested
    rels = [r for r in ((n.get("releases") or {}).get("nodes") or []) if r and not r.get("isDraft")]
    stable = [r for r in rels if not r.get("isPrerelease")]
    latest = (stable or rels or [None])[0]
    lic = n.get("licenseInfo") or {}
    branch = n.get("defaultBranchRef") or {}
    hist = (((branch.get("target") or {}).get("history")) or {}).get("nodes") or []
    return {
        **entry,
        "repo": full,
        "moved_from": requested if full.lower() != requested.lower() else "",
        "missing": False,
        "description": clean(n.get("description")),
        "homepage": n.get("homepageUrl") or "",
        "topics": [t["topic"]["name"] for t in ((n.get("repositoryTopics") or {}).get("nodes") or [])],
        "stars": n.get("stargazerCount", 0),
        "forks": n.get("forkCount", 0),
        "open_issues": ((n.get("issues") or {}).get("totalCount", 0)
                        + (n.get("pullRequests") or {}).get("totalCount", 0)),
        "language": (n.get("primaryLanguage") or {}).get("name", ""),
        "languages": {e["node"]["name"]: e["size"] for e in ((n.get("languages") or {}).get("edges") or [])},
        "license": (lic.get("spdxId") if lic.get("spdxId") not in (None, "NOASSERTION") else (lic.get("name") or "")),
        "archived": n.get("isArchived", False),
        "fork_of": (n.get("parent") or {}).get("nameWithOwner", ""),
        "default_branch": branch.get("name", ""),
        "size_mb": round((n.get("diskUsage") or 0) / 1024, 1),
        "created": parse_time(n.get("createdAt")),
        "pushed": parse_time(n.get("pushedAt")),
        "release_tag": latest.get("tagName") if latest else None,
        "release_url": latest.get("url") if latest else None,
        "release_date": parse_time(latest.get("publishedAt")) if latest else None,
        "releases": [{"tag": r.get("tagName"), "name": r.get("name") or "", "url": r.get("url"),
                      "date": parse_time(r.get("publishedAt")), "pre": r.get("isPrerelease", False),
                      "body": r.get("description") or ""} for r in rels],
        "commits": [{"msg": clean(c.get("messageHeadline"), 100), "date": parse_time(c.get("committedDate")),
                     "author": ((c.get("author") or {}).get("user") or {}).get("login")
                               or (c.get("author") or {}).get("name", ""),
                     "url": c.get("url")} for c in hist if c],
        "contributors": [],
    }


def fetch_repos(entries):
    """Fetch many repos; GraphQL in batches when a token is available, REST otherwise or on failure."""
    if not TOKEN:
        return [fetch(e) for e in entries]
    out = []
    for i in range(0, len(entries), GQL_BATCH):
        batch = entries[i:i + GQL_BATCH]
        names = [entry_name(e) for e in batch]
        parts = []
        for k, name in enumerate(names):
            owner, _, repo = name.partition("/")
            parts.append(f"r{k}: repository(owner: {json.dumps(owner)}, name: {json.dumps(repo)}) {{{REPO_FIELDS}}}")
        query = "query {\n" + "\n".join(parts) + "\nrateLimit { cost remaining }\n}"
        try:
            res = gql(query)
            data = res.get("data") or {}
            not_found = {str(e.get("path", [""])[0]) for e in (res.get("errors") or [])
                         if e.get("type") == "NOT_FOUND"}
        except Exception as ex:  # whole batch failed -> REST for this batch
            print(f"GraphQL batch failed ({ex}); using REST for {len(batch)} repos", file=sys.stderr)
            data, not_found = None, set()
        for k, (e, name) in enumerate(zip(batch, names)):
            node = data.get(f"r{k}") if data is not None else None
            if node:
                out.append(node_to_item(e, name, node))
            elif data is not None and f"r{k}" in not_found:
                out.append({**e, "repo": name, "missing": True})
            else:
                API_STATS["rest_fallback"] += 1
                out.append(fetch(e))
        print(f"Checked {min(i + GQL_BATCH, len(entries))}/{len(entries)} repos", file=sys.stderr)
    return out


def fetch_orgs(entries):
    if not TOKEN or not entries:
        return [fetch_org(e) for e in entries]
    names = [entry_name(e, "org") for e in entries]
    parts = [f"""o{k}: repositoryOwner(login: {json.dumps(n)}) {{
      login __typename
      ... on Organization {{ name description }}
      ... on User {{ name bio }}
      repositories(first: 30, privacy: PUBLIC, isFork: false, orderBy: {{field: PUSHED_AT, direction: DESC}}) {{
        totalCount nodes {{ nameWithOwner stargazerCount pushedAt description isArchived }}
      }}
    }}""" for k, n in enumerate(names)]
    try:
        data = gql("query {\n" + "\n".join(parts) + "\nrateLimit { cost remaining }\n}").get("data") or {}
    except Exception as ex:
        print(f"GraphQL orgs failed ({ex}); using REST", file=sys.stderr)
        return [fetch_org(e) for e in entries]
    out = []
    for k, (e, n) in enumerate(zip(entries, names)):
        o = data.get(f"o{k}")
        if not o:
            out.append({**e, "org": n, "missing": True})
            continue
        repos = [r for r in o["repositories"]["nodes"] if r and not r.get("isArchived")]
        top = sorted(repos, key=lambda r: -r.get("stargazerCount", 0))[:6]
        out.append({**e, "org": o["login"], "missing": False,
                    "display": o.get("name") or o["login"],
                    "description": clean(o.get("description") or o.get("bio") or ""),
                    "public_repos": o["repositories"]["totalCount"],
                    "top": [(r["nameWithOwner"], r.get("stargazerCount", 0), parse_time(r.get("pushedAt")),
                             clean(r.get("description"), 90)) for r in top]})
    return out


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


def gone_reason(it, now):
    """Why a repo counts as discontinued, or "" if it's alive."""
    if str(it.get("status") or "").lower() in ("deprecated", "discontinued"):
        return "marked deprecated"
    if it.get("missing"):
        return ""
    if it.get("archived"):
        return "archived by its owner"
    d = it.get("pushed")
    if d is not None and (now - d).days > GONE_DAYS:
        return f"no activity since {d:%b %Y}"
    return ""


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
    L = [f"# {r}", "", "[← Back to the radar](../README.md) · [Open on GitHub ↗]({})".format(gh), ""]
    if it["missing"]:
        L += ["⚠️ **This repo wasn't found** — it may have been renamed, made private or deleted.", ""]
    elif it["description"]:
        L += [f"> {it['description']}", ""]

    # my notes
    L += ["## 📝 Notes", "",
          "| | |", "|---|---|",
          f"| **Status** | {it.get('status') or '—'} |",
          f"| **Category** | {cat_title(it.get('category'))} |",
          f"| **Project** | {it.get('project') or '—'} |",
          f"| **Why it's worth a look** | {clean(str(it.get('why') or '—'))} |"]
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
    if is_stale(it, now) and not gone_reason(it, now):
        badges.append(f"💤 **Quiet** — no activity for {ago(it['pushed'], now).replace(' ago', '')}")
    reason = gone_reason(it, now)
    if reason:
        badges.append(f"🪦 **Discontinued** — {reason}")
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

def render_readme(items, orgs, links, now):
    slug = os.environ.get("GITHUB_REPOSITORY", "mmaxpo/awesome-ai-radar")
    n_active = sum(1 for it in items if not it["missing"]
                   and (is_new(it, "release_date", now) or is_new(it, "pushed", now)))
    n_rel = sum(1 for it in items if not it["missing"] and is_new(it, "release_date", now))
    n_cats = len({cat_title(it.get("category")) for it in items})
    badge = lambda label, msg, color: (f"![{label}](https://img.shields.io/badge/"
                                       f"{label.replace('-', '--').replace(' ', '_')}-"
                                       f"{str(msg).replace('-', '--').replace(' ', '_')}-{color})")
    L = [
        "# 📡 Awesome AI Radar",
        "",
        "![Awesome AI Radar](.github/banner.png)",
        "",
        "> A curated list of the best open-source AI repos — **that updates itself every day.**",
        "",
        " ".join([badge("repos", len(items), "blue"), badge("active this week", n_active, "brightgreen"),
                  badge("updated", f"{now:%Y-%m-%d}", "orange"), badge("license", "MIT", "lightgrey"),
                  f"[![suggest a repo](https://img.shields.io/badge/suggest-a_repo-purple)]"
                  f"(https://github.com/{slug}/issues/new?template=suggest-repo.yml)"]),
        "",
        "Most awesome lists go stale: dead projects sit next to great ones and you can't tell them apart.",
        "This list is checked by a GitHub Action **every day**, so you always see:",
        "",
        "- 🔥 **What shipped this week** — new releases and active projects",
        "- 💤 🗄 **What went quiet** — repos with no activity for months, or archived",
        "- 📄 **A detail sheet for every repo** — stars, languages, license, latest releases, recent commits",
        "- 📊 **The whole list as a table** — [`repos.csv`](repos.csv), sortable and searchable",
        "",
        f"**{len(items)} repos · {n_cats} categories · {n_rel} new releases this week** · "
        f"_last checked {now:%Y-%m-%d %H:%M} UTC_",
        "",
        "**Jump to:** [🔥 What's new](#-whats-new-last-7-days) · [🗂 Categories](#-categories) · "
        "[📰 Weekly digests](weekly/) · [➕ Suggest a repo](#-suggest-a-repo) · "
        "[🛠 Make your own radar](#-make-your-own-radar-in-1-minute)",
        "",
    ]

    # what's new
    fresh = [it for it in items if not it["missing"]
             and (is_new(it, "release_date", now) or is_new(it, "pushed", now))]
    releases = [it for it in fresh if is_new(it, "release_date", now)]
    commits_only = [it for it in fresh if not is_new(it, "release_date", now)]
    releases.sort(key=lambda it: it["release_date"], reverse=True)
    commits_only.sort(key=lambda it: it["pushed"], reverse=True)

    year, week, _ = now.isocalendar()
    L += [f"## 🔥 What's new (last {NEW_DAYS} days)", "",
          f"_📰 Readable summary: [this week's digest](weekly/{year}-W{week:02d}.md) · [all weeks](weekly/)_", ""]
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
    gone = [it for it in items if gone_reason(it, now)]
    for it in items:
        if not gone_reason(it, now):
            groups.setdefault(cat_title(it.get("category")), []).append(it)
    order = [t for t in CATEGORIES.values() if t in groups]
    order += sorted(t for t in groups if t not in order and t != "📁 Uncategorized")
    if "📁 Uncategorized" in groups:
        order.append("📁 Uncategorized")

    L += ["## 🗂 Categories", ""]
    L += [" · ".join(f"[{t}](#{cat_anchor(t)}) ({len(groups[t])})" for t in order)]
    if links:
        L[-1] += f" · [📎 More resources](#{cat_anchor('📎 More resources')}) ({len(links)})"
    if gone:
        L[-1] += f" · [{GONE_TITLE}](#{cat_anchor(GONE_TITLE)}) ({len(gone)})"
    if orgs:
        L[-1] += f" · [🏢 Organizations](#{cat_anchor('🏢 Organizations')}) ({len(orgs)})"
    L.append("")

    for title in order:
        group = sorted(groups[title], key=lambda it: (it["missing"], -(it.get("stars") or 0)))
        L += [f"## {title}", "",
              "| Repo | Why it's worth a look | ⭐ | Last activity | Latest release |",
              "|---|---|---|---|---|"]
        for it in group:
            r = it["repo"]
            why = clean(str(it.get("why") or ""))
            status = STATUS_ICON.get((it.get("status") or "").lower(), it.get("status") or "")
            if it.get("project"):
                why += f" <sub>· {clean(str(it['project']))}</sub>"
            if it["missing"]:
                L.append(f"| [`{r}`]({sheet_path(r)}) ⚠️ not found | {why} | | | |")
                continue
            flag = " 🆕" if is_new(it, "pushed", now) or is_new(it, "release_date", now) else ""
            flag += " 🗄" if it["archived"] else (" 💤" if is_stale(it, now) else "")
            flag += " ↪️" if it.get("moved_from") else ""
            desc = f"<br><sub>{clean(it['description'], 110)}</sub>" if it["description"] else ""
            rel = (f"[{it['release_tag']}]({it['release_url']}) · {ago(it['release_date'], now)}"
                   if it["release_tag"] else "—")
            L.append(f"| [**{r}**]({sheet_path(r)}){flag}{desc} | {why} "
                     f"| {fmt_num(it['stars'])} | {ago(it['pushed'], now)} | {rel} |")
        L.append("")

    if gone:
        L += [f"## {GONE_TITLE}", "",
              "Archived, or no activity for over two years. Still useful to read and learn from — "
              "but think twice before building on them.", "",
              "| Repo | Why it was on the list | Category | ⭐ | Status |", "|---|---|---|---|---|"]
        for it in sorted(gone, key=lambda it: -(it.get("stars") or 0)):
            r = it["repo"]
            L.append(f"| [**{r}**]({sheet_path(r)}) | {clean(str(it.get('why') or ''))} "
                     f"| {cat_title(it.get('category'))} | {fmt_num(it.get('stars') or 0)} | {gone_reason(it, now)} |")
        L.append("")

    if links:
        types = [("paper", "📄 Papers"), ("course", "🎓 Courses"), ("article", "📝 Articles & explainers"),
                 ("model", "🤗 Models & datasets"), ("person", "👤 People worth following"),
                 ("tool", "🌐 Tools & sites"), ("crypto", "🪙 Crypto & trading")]
        alias_t = {"dataset": "model", "api": "tool", "site": "tool", "docs": "article", "video": "course"}
        for x in links:
            x["type"] = alias_t.get(str(x.get("type") or "").lower(), x.get("type"))
        known_t = {k for k, _ in types}
        L += ["## 📎 More resources", "",
              "Papers, courses, models and sites that aren't GitHub repos (so they're not tracked for updates).", ""]
        for key, title in types + [("other", "🔗 Other")]:
            group = [x for x in links if (str(x.get("type") or "other").lower() if str(x.get("type") or "other").lower() in known_t else "other") == key]
            if not group:
                continue
            L += [f"**{title}**", ""]
            for x in group:
                t = clean(str(x.get("title") or x["link"]))
                why = f" — {clean(str(x['why']))}" if x.get("why") else ""
                L.append(f"- [{t}]({x['link']}){why}")
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

    L += ["## ➕ Suggest a repo", "",
          "Know a great open-source AI repo that's missing? "
          f"[**Suggest it here**](https://github.com/{slug}/issues/new?template=suggest-repo.yml) — "
          "it takes 30 seconds. Approved suggestions are added automatically.", "",
          "## 🛠 Make your own radar in 1 minute", "",
          "Want to track *your own* list of repos the same way?", "",
          f"1. Click **[Use this template](https://github.com/{slug}/generate)** to copy this repo to your account.",
          "2. Edit [`repos.yml`](repos.yml) — keep the repos you care about, add your own.",
          "3. Go to **Actions → Update Repo Radar → Run workflow**. Done — it refreshes itself daily.", "",
          "Each entry is just a few lines:", "",
          "```yaml", "- repo: owner/name", "  why: why it's worth following", "  category: agents",
          "  status: study        # study | using | later | done", "```", "",
          "<details><summary><b>How it works</b></summary>", "",
          "A small Python script ([`scripts/update.py`](scripts/update.py)) reads `repos.yml`, asks the "
          "GitHub API about each repo, and rewrites this README, the per-repo sheets in [`repos/`](repos/), "
          "[`repos.csv`](repos.csv) and the [weekly digest](weekly/). A GitHub Action runs it every day "
          "and whenever the list changes. No servers, no cost.", "",
          "</details>", "",
          "---",
          "If this list saves you time, a ⭐ helps others find it.", "",
          f"🆕 active in the last {NEW_DAYS} days · 💤 quiet for over {STALE_DAYS // 30} months · "
          "🗄 archived · ↪️ moved/renamed · ⚠️ not found", ""]
    return "\n".join(L)


# ---------- weekly digest ----------

def first_note(body):
    """One readable line from release notes: skip headings, boilerplate and links."""
    import re
    in_code = False
    for line in (body or "").replace("\r", "").splitlines():
        t = line.strip()
        if t.startswith("```"):
            in_code = not in_code
            continue
        if in_code or t.endswith("\\") or t.startswith(("$ ", ">")):
            continue
        t = re.sub(r"<[^>]*>?", "", t).strip()                  # HTML tags (and broken ones)
        if not t or t.startswith(("#", "<", "|", "!", "**Full Changelog", "Full Changelog")):
            continue
        if re.match(r"^\W*(what'?s changed|changes|changelog|highlights|new contributors)\W*$", t, re.I):
            continue
        t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)        # [text](link) -> text
        t = re.sub(r"https?://\S+", "", t)
        t = re.sub(r"^[-*+]\s*|\s*by @\S+.*$|\s*in #\d+.*$", "", t)  # bullets, "by @x in #12"
        t = t.replace("**", "").replace("`", "").strip(" :-*_")
        if len(t) > 8:
            return clean(t, 120)
    return ""


def write_weekly(items, now):
    from datetime import date, timedelta
    year, week, _ = now.isocalendar()
    monday = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    sunday = monday + timedelta(days=6)
    since = lambda d: d is not None and d >= monday
    folder = ROOT / "weekly"
    folder.mkdir(exist_ok=True)

    live = [it for it in items if not it["missing"]]
    rel = [it for it in live if since(it.get("release_date"))]
    added = [it for it in items if isinstance(it.get("added"), date) and it["added"] >= monday.date()]
    busy = sorted([it for it in live if since(it.get("pushed")) and it not in rel],
                  key=lambda it: -(it.get("stars") or 0))[:12]

    title = f"This week in AI repos — {monday:%b %-d} – {sunday:%b %-d, %Y}"
    L = [f"# 📰 {title}", "",
         f"_Week {week} of {year} · from [Awesome AI Radar](../README.md) · "
         f"updated daily, final on Sunday · last update {now:%Y-%m-%d %H:%M} UTC_", "",
         f"**{len(rel)} new releases · {len(busy)} other busy repos"
         + (f" · {len(added)} added to the radar" if added else "") + "**", ""]

    L += [f"## 📦 New releases", ""]
    if rel:
        by_cat = {}
        for it in sorted(rel, key=lambda it: -(it.get("stars") or 0)):
            by_cat.setdefault(cat_title(it.get("category")), []).append(it)
        order = [t for t in CATEGORIES.values() if t in by_cat] + sorted(t for t in by_cat if t not in CATEGORIES.values())
        for t in order:
            L += [f"**{t}**", ""]
            for it in by_cat[t]:
                r = it["repo"]
                note = first_note(it["releases"][0]["body"]) if it["releases"] else ""
                L.append(f"- **[{r}](https://github.com/{r})** [{it['release_tag']}]({it['release_url']})"
                         f" · ⭐ {fmt_num(it['stars'])}" + (f" — {note}" if note else ""))
            L.append("")
    else:
        L += ["_No releases yet this week._", ""]

    if busy:
        L += ["## 🔨 Busy without a release", ""]
        for it in busy:
            r = it["repo"]
            msg = it["commits"][0]["msg"] if it["commits"] else ""
            L.append(f"- **[{r}](https://github.com/{r})** · ⭐ {fmt_num(it['stars'])}" + (f" — _{msg}_" if msg else ""))
        L.append("")

    if added:
        L += ["## ➕ New on the radar", ""]
        for it in added[:20]:
            r = it["repo"]
            L.append(f"- **[{r}](https://github.com/{r})** — {clean(str(it.get('why') or ''))}")
        if len(added) > 20:
            L.append(f"- …and {len(added) - 20} more — see the [full list](../README.md#-categories)")
        L.append("")

    (folder / f"{year}-W{week:02d}.md").write_text("\n".join(L), encoding="utf-8")

    # index of all weeks
    weeks = sorted((p.stem for p in folder.glob("*-W*.md")), reverse=True)
    idx = ["# 📰 Weekly digests", "",
           "What shipped each week across the repos on [Awesome AI Radar](../README.md).", ""]
    idx += [f"- [{w}]({w}.md)" + (" — this week" if w == f"{year}-W{week:02d}" else "") for w in weeks]
    (folder / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")


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
            elif gone_reason(it, now):
                health = "discontinued"
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
    entries = [e for e in entries if isinstance(e, dict)]
    repo_entries = [e for e in entries if e.get("repo")]
    org_entries = [e for e in entries if e.get("org")]
    links = [e for e in entries if e.get("link")]

    orgs = fetch_orgs(org_entries)
    items, seen = [], set()
    for it in fetch_repos(repo_entries):
        if it["repo"].lower() in seen:  # duplicate (or two names for a moved repo)
            continue
        seen.add(it["repo"].lower())
        items.append(it)
    print(f"API use: {API_STATS['graphql']} GraphQL requests (cost {API_STATS['cost']}), "
          f"{API_STATS['rest_fallback']} repos via REST fallback", file=sys.stderr)
    now = datetime.now(timezone.utc)

    SHEETS.mkdir(exist_ok=True)
    for old in SHEETS.glob("*.md"):  # remove sheets of repos you deleted from the list
        old.unlink()
    for it in items:
        (ROOT / sheet_path(it["repo"])).write_text(render_sheet(it, now), encoding="utf-8")

    (ROOT / "README.md").write_text(render_readme(items, orgs, links, now), encoding="utf-8")
    write_csv(items, ROOT / "repos.csv", now)
    write_weekly(items, now)
    print(f"Updated README, repos.csv and {len(items)} repo sheets.", file=sys.stderr)


if __name__ == "__main__":
    main()
