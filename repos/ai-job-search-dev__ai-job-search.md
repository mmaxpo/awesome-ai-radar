# ai-job-search-dev/ai-job-search

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/ai-job-search-dev/ai-job-search)

> The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛠 Apps & other |
| **Project** | — |
| **Why it's worth a look** | Local AI job-search framework on Claude Code: evaluate postings, tailor CVs, cover letters, interview prep |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 73.7k |
| 🍴 **Forks** | 23.5k |
| 🐞 **Open issues + PRs** | [35](https://github.com/ai-job-search-dev/ai-job-search/issues) |
| 💻 **Languages** | Python 99% · TeX 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `ai-agents` `career` `claude-code` `cover-letter` `cv` `interview-preparation` `job-application` `job-hunting` `job-search` `latex` `resume` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-03-18 |
| 📦 **Latest release** | [v2.1.0](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v2.1.0) — 2026-11-23 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 6.0 MB |

## 📦 Recent releases

### [v2.1.0](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v2.1.0)
<sub>2026-11-23 · 4d ago</sub>

> **What's Changed**
> * ci: add a stable CLI checks result job for required checks by @jakob1379 in https://github.com/ai-job-search-dev/ai-job-search/pull/856
> * ci: check PR titles against Conventional Commits with commitizen by @jakob1379 in https://github.com/ai-job-search-dev/ai-job-search/pull/863
> * fix(posting-guard): refuse empty input and exit 1 (fixes #798) by @ahmed-husssain in https://github.com/ai-job-search-dev/ai-job-search/pull/815
> * fix(posting-guard): detect CSS invisibility tricks in inline styles (#785) by @ahmed-husssain in https://github.com/ai-job-search-dev/ai-job-search/pull/834
> * feat(setup): recommend a minimal TeX install instead of texlive-full by @jakob1379 in https://github.com/ai-job-search-dev/ai-job-search/pull/873
> …

### [v2.0.0](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v2.0.0)
<sub>2026-11-16 · 11d ago</sub>

> **What's Changed**
> * fix(scrape): send one plain term per CLI call and make portals state their query syntax (#536) by @ai-tvang in https://github.com/ai-job-search-dev/ai-job-search/pull/653
> * fix(rank): report a non-object seen_jobs.json entry instead of a traceback by @rudycelekli in https://github.com/ai-job-search-dev/ai-job-search/pull/636
> * fix(salary): split combined name-and-city workbook columns by @mvanhorn in https://github.com/ai-job-search-dev/ai-job-search/pull/660
> * fix(fetch-page): decode standard zlib-wrapped HTTP deflate by @rudycelekli in https://github.com/ai-job-search-dev/ai-job-search/pull/711
> * fix(add-portal): keep generated tests offline in CI by @rudycelekli in https://github.com/ai-job-search-dev/ai-job-search/pull/714
> …

### [v1.7.5](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.5)
<sub>2026-11-09 · 18d ago</sub>

> **What's Changed**
> * fix(job-key): fold Latin letters without an NFKD decomposition and add --audit --migrate by @ai-tvang in https://github.com/ai-job-search-dev/ai-job-search/pull/637
> * fix(notion-sync): re-key a row matched by URL when its Key has drifted by @ai-tvang in https://github.com/ai-job-search-dev/ai-job-search/pull/761
> * fix(install): find bun at standard install locations when PATH misses it (fixes #707) by @ahmed-husssain in https://github.com/ai-job-search-dev/ai-job-search/pull/762
> * fix(fetch-page): pass --compressed only when curl supports it (fixes #705) by @ahmed-husssain in https://github.com/ai-job-search-dev/ai-job-search/pull/759
> * fix(scrape): force UTF-8 output in scrape_state.py by @harshajv7981 in https://github.com/ai-job-search-dev/ai-job-search/pull/744
> …

### [v1.7.4](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.4)
<sub>2026-11-02 · 25d ago</sub>

> **What's Changed**
> * fix(freehire-search): reject detail URLs on other hosts instead of asking the API for their last segment (#622) by @ayobamiseun in https://github.com/ai-job-search-dev/ai-job-search/pull/623
> * fix(freehire-search): reject --description-format on detail instead of ignoring it by @rudycelekli in https://github.com/ai-job-search-dev/ai-job-search/pull/648
> * freehire-search: honor Retry-After on 429/503 by @strelov1 in https://github.com/ai-job-search-dev/ai-job-search/pull/632
> * freehire-search: us is a country, not a region by @strelov1 in https://github.com/ai-job-search-dev/ai-job-search/pull/630
> * fix(freehire-search): say what --region is, and warn when it matches a thin bucket by @GOPNIK64 in https://github.com/ai-job-search-dev/ai-job-search/pull/651
> …

### [v1.7.3](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.3) — v1.7.3 - Least privilege, postings checked before use, and fifty-eight fixes
<sub>2026-10-19 · 1mo ago</sub>

> A patch release in two halves. **The security model now does what the docs said it did:** skills and agents get only the tools they need, the permission file ships rules that hold even in bypass mode, and every job posting is checked for hidden instructions before anything reads it. **And contributors closed fifty-eight bugs in two weeks**, most of them found by running the real tools against real data. Seventy-one entries.
> **Highlights**
> **Least-privilege skills, agents and permissions (#642, #654)**
> A public review by an AI agent read the shipped configuration and concluded that local use was unsafe as configured. It had a point. The job-application skill's frontmatter granted bare `Bash`, `Edit` and `Write`. The scraper pre-approved `bun run` on any CLI path. And the `/apply` reviewer and the `/rank` scorers ran as general-purpose agents with every tool while they held untrusted posting text. Now:
> - **Skill frontmatter grants nothing beyond what `settings.json` already allows.** The security guard checks every skill and command frontmatter against an exact allowlist, and a portal skill may grant only its own CLI.
> - **`settings.json` ships `deny` rules that hold in every permission mode.** They block uploads via `curl`/`wget`, `scp`, `ssh`, `nc`, and reads of `.env` and credential folders. `ask` rules cover edits to the permission files themselves and `git push`.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [docs(job-key): say that --migrate renames only company_title keys (#901)](https://github.com/ai-job-search-dev/ai-job-search/commit/9078cad68fb3847f41b9ee3657998a1ab555c1d1) | MadsLorentzen |
| 2026-11-27 | [ci: cancel a stale PR-title check when the title changes (#902)](https://github.com/ai-job-search-dev/ai-job-search/commit/a4c731907f74eb878ea8bf824a68d662d1672698) | jakob1379 |
| 2026-11-27 | [fix(guards): ask before writing files that pre-approved commands load…](https://github.com/ai-job-search-dev/ai-job-search/commit/95dd99c736a1da410ab92d6698d66ce10016b704) | MadsLorentzen |
| 2026-11-26 | [fix(guards): refuse a tracked settings.local.json and read .gitignore…](https://github.com/ai-job-search-dev/ai-job-search/commit/15436e4e150d74bdd95526fa59be36db201b8a90) | jakob1379 |
| 2026-11-26 | [fix(robots-check): check every hop's host before connecting and bound…](https://github.com/ai-job-search-dev/ai-job-search/commit/50defd097cc4339ee55ccfa44bac67c73e56b145) | jakob1379 |
| 2026-11-26 | [fix(tools): confine fetch_page and posting_guard file arguments to th…](https://github.com/ai-job-search-dev/ai-job-search/commit/f3ad83a3962c445099bb5632bc9aadf239dc0f52) | jakob1379 |
| 2026-11-25 | [feat(apply): flag posting phrases copied into the CV and cover letter…](https://github.com/ai-job-search-dev/ai-job-search/commit/965452f74749bd9b0bb4edd415d628a610946ec9) | TheMattHub |
| 2026-11-24 | [feat(html-report): render the dashboard from a script instead of hand…](https://github.com/ai-job-search-dev/ai-job-search/commit/4e021e52f7e3d4016e0c22fc416c814a3d44c5c9) | loxator |
| 2026-11-22 | [fix(robots): treat a comment-only robots.txt as allow-all (Greenhouse…](https://github.com/ai-job-search-dev/ai-job-search/commit/ab51f852316faca85fe6ce93cccd7ac58b9c20df) | MadsLorentzen |
| 2026-11-22 | [fix(posting-guard): stop reading window.ENV in a page script as a .en…](https://github.com/ai-job-search-dev/ai-job-search/commit/6ec7eead309013cebfa002fb2c3588d0bfb2090a) | MadsLorentzen |

[See all commits ↗](https://github.com/ai-job-search-dev/ai-job-search/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ai-job-search-dev/ai-job-search.git
```
