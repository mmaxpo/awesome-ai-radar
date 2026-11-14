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
| ⭐ **Stars** | 71.7k |
| 🍴 **Forks** | 23.1k |
| 🐞 **Open issues + PRs** | [49](https://github.com/ai-job-search-dev/ai-job-search/issues) |
| 💻 **Languages** | Python 66% · TypeScript 33% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `ai-agents` `career` `claude-code` `cover-letter` `cv` `interview-preparation` `job-application` `job-hunting` `job-search` `latex` `resume` |
| 🕒 **Last activity** | 2026-11-12 (yesterday) |
| 📅 **Created** | 2026-03-18 |
| 📦 **Latest release** | [v1.7.5](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.5) — 2026-11-09 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 5.6 MB |

## 📦 Recent releases

### [v1.7.5](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.5)
<sub>2026-11-09 · 5d ago</sub>

> **What's Changed**
> * fix(job-key): fold Latin letters without an NFKD decomposition and add --audit --migrate by @ai-tvang in https://github.com/ai-job-search-dev/ai-job-search/pull/637
> * fix(notion-sync): re-key a row matched by URL when its Key has drifted by @ai-tvang in https://github.com/ai-job-search-dev/ai-job-search/pull/761
> * fix(install): find bun at standard install locations when PATH misses it (fixes #707) by @ahmed-husssain in https://github.com/ai-job-search-dev/ai-job-search/pull/762
> * fix(fetch-page): pass --compressed only when curl supports it (fixes #705) by @ahmed-husssain in https://github.com/ai-job-search-dev/ai-job-search/pull/759
> * fix(scrape): force UTF-8 output in scrape_state.py by @harshajv7981 in https://github.com/ai-job-search-dev/ai-job-search/pull/744
> …

### [v1.7.4](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.4)
<sub>2026-11-02 · 12d ago</sub>

> **What's Changed**
> * fix(freehire-search): reject detail URLs on other hosts instead of asking the API for their last segment (#622) by @ayobamiseun in https://github.com/ai-job-search-dev/ai-job-search/pull/623
> * fix(freehire-search): reject --description-format on detail instead of ignoring it by @rudycelekli in https://github.com/ai-job-search-dev/ai-job-search/pull/648
> * freehire-search: honor Retry-After on 429/503 by @strelov1 in https://github.com/ai-job-search-dev/ai-job-search/pull/632
> * freehire-search: us is a country, not a region by @strelov1 in https://github.com/ai-job-search-dev/ai-job-search/pull/630
> * fix(freehire-search): say what --region is, and warn when it matches a thin bucket by @GOPNIK64 in https://github.com/ai-job-search-dev/ai-job-search/pull/651
> …

### [v1.7.3](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.3) — v1.7.3 - Least privilege, postings checked before use, and fifty-eight fixes
<sub>2026-10-19 · 26d ago</sub>

> A patch release in two halves. **The security model now does what the docs said it did:** skills and agents get only the tools they need, the permission file ships rules that hold even in bypass mode, and every job posting is checked for hidden instructions before anything reads it. **And contributors closed fifty-eight bugs in two weeks**, most of them found by running the real tools against real data. Seventy-one entries.
> **Highlights**
> **Least-privilege skills, agents and permissions (#642, #654)**
> A public review by an AI agent read the shipped configuration and concluded that local use was unsafe as configured. It had a point. The job-application skill's frontmatter granted bare `Bash`, `Edit` and `Write`. The scraper pre-approved `bun run` on any CLI path. And the `/apply` reviewer and the `/rank` scorers ran as general-purpose agents with every tool while they held untrusted posting text. Now:
> - **Skill frontmatter grants nothing beyond what `settings.json` already allows.** The security guard checks every skill and command frontmatter against an exact allowlist, and a portal skill may grant only its own CLI.
> - **`settings.json` ships `deny` rules that hold in every permission mode.** They block uploads via `curl`/`wget`, `scp`, `ssh`, `nc`, and reads of `.env` and credential folders. `ask` rules cover edits to the permission files themselves and `git push`.
> …

### [v1.7.2](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.2) — v1.7.2 - Measured PDFs, CLIs that stop trusting the digits, tools that survive n…
<sub>2026-09-29 · 1mo ago</sub>

> A patch release with one theme: **the checks the workflow documented now actually run, and the tools stop breaking on anything that is not ASCII.** Compiled PDFs get measured instead of eyeballed, the portal CLIs stop trusting the digits in a URL, and every Python tool survives a Cyrillic posting or a Turkish robots.txt on Windows. Thirty-two entries, twenty-four of them fixes, most reported and fixed by contributors within days of each other.
> **Highlights**
> **`/apply` measures the PDF instead of looking at it (#378, #476, #458, #498, #465)**
> `tools/verify_layout.py` measures what Step 5b previously only eyeballed: per-page text extent, bottom whitespace, the largest internal gap, footer collisions, and an entry header stranded at a page break. It exists for a failure every other check missed: a moderncv `\cventry` is unbreakable, so an entry that does not fit jumps to the next page and leaves a hole while the document still compiles, still has the right page count, and still passes `verify_pdf.py`. Step 5b now also runs the page-count check it had been claiming Step 5d ran (nothing in the workflow passed `--pages` at all). `verify_pdf.py --contains` sees through LaTeX's typographic substitutions, so `--contains "Master's degree"` and `--contains "2016-2024"` no longer report a keyword missing from a document that plainly contains it, and the new `--ascii-dates` flag reads the raw text layer for the one thing the fold must not hide: a year joined to an en-dash, which a real Workday import dropped together with the date. Poppler stays optional; a missing or xpdf `pdftotext` degrades to a `skipped:` exit 2 that now names both causes.
> **Portal CLIs stop trusting the digits (#448, #500, #435, #460, #504, #505)**
> `jobindex-search detail` fetched any URL verbatim and, when the path did not match, returned a well-formed fake posting built from whatever page came back. `linkedin-search detail` took the first six-plus-digit segment from any URL, so a Greenhouse or Lever apply link fetched whichever LinkedIn posting carried that number, with exit 0. Both now parse the host for real and exit 1 with the `BAD_ID` contract before any request, matching the rest of the CLIs. `jobnet-search detail` no longer reports an externally hosted ad as not found, `jobdanmark-search detail` backs off on 429/5xx like every other portal, and `freehire-search` decodes HTML entities in titles and keeps the salary period, so a yearly figure no longer reads as monthly.
> …

### [v1.7.1](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.1) — v1.7.1 - Cheaper ranking, portals that fail loudly, forks that stop fighting CI
<sub>2026-09-06 · 2mo ago</sub>

> A patch release with one theme: **the workflow stops paying for work it does not need and stops hiding work it failed to do.** `/rank` no longer drags your whole job history through the conversation on every run, the portal CLIs now refuse bad input instead of silently returning the wrong thing, and forks get a clean CI and a complete `/setup`. Seventeen entries, fourteen of them fixes, most of them reported and fixed by contributors within a day of each other.
> **Highlights**
> **`/rank` is bounded and keeps its state on disk (#395, #424, #425, #390)**
> A bare `/rank` used to score the entire backlog in one go and read the whole of `seen_jobs.json` into the conversation twice per run - a cost that grew for the life of a workspace and was paid regardless of batch size (one reporter measured a 188 KB state file). `--limit <N>` now bounds each run to ten jobs by default, independently of `--top`, and reports what it deferred. `tools/rank_state.py` owns the state traffic: `candidates` selects and projects only the fields a scoring agent needs, `sweep` runs the expiry pass on disk, and `apply` writes results back atomically. Scoring policy is unchanged, and every existing write-back rule (legacy `location` migration, null deadlines never erasing a stored one, verbatim strengths and gaps) is pinned by tests. `/rank` also now flags postings whose stored `posted_date` is more than 30 days old.
> **Portal CLIs fail loudly instead of lying (#426, #429, #371, #416, #418, #421)**
> The sharpest fix of the release: the unknown-flag guard in the four bunli-based CLIs only inspected `--long` flags, so an undefined short flag was silently discarded and the search ran unfiltered - `search -q "sygeplejerske"` on jobnet returned 18,210 ads with exit 0 where the correct flag returns 669. Both dash forms are now checked. The `detail` commands of jobbank, jobdanmark and jobnet accept full posting URLs as the contract always said they should, `linkedin-search` rejects fractional numeric flags instead of truncating them, and a one-CLI-at-a-time audit closed three crashes where a single null field from a portal API killed the whole run (a jobbank feed date, a jobnet publication date, a jobdanmark autocomplete item).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [fix(scrape): deduplicate candidates on the canonical key so store nev…](https://github.com/ai-job-search-dev/ai-job-search/commit/0d0d1a907a21454affa1b694acc4e2c5008a0d21) | ayobamiseun |
| 2026-11-12 | [fix(upskill): leave jobs /rank vetoed on location or language out of …](https://github.com/ai-job-search-dev/ai-job-search/commit/8fc6d7c860b0ffff3fdb744e007ca255c02c8385) | TheMattHub |
| 2026-11-12 | [fix(cover-letter): load Raleway's bold face in the bullet-list font w…](https://github.com/ai-job-search-dev/ai-job-search/commit/8e814e57ac487d5f15675bb13ed07f95c9765c4a) | TheMattHub |
| 2026-11-12 | [fix(guards): check command and agent files in subfolders too (#735)](https://github.com/ai-job-search-dev/ai-job-search/commit/e686ff24f634bbf40cb4c21e38d61d734f90ac26) | ayobamiseun |
| 2026-11-12 | [fix(scrape): accept company: null as the portal contract allows (#738)](https://github.com/ai-job-search-dev/ai-job-search/commit/317ec994eafc11b11893af1e000e2ddcd12dfff1) | ayobamiseun |
| 2026-11-12 | [fix(rank): hand the posting-scorer each job's key so it can return it…](https://github.com/ai-job-search-dev/ai-job-search/commit/281f9ef0e0daf06d58b250b666c9cf7a5e3532b9) | ayobamiseun |
| 2026-11-12 | [fix(fetch): compare --out against the repo by identity, not spelling …](https://github.com/ai-job-search-dev/ai-job-search/commit/7a082b212aef4159a22144d01998dd37b9912af0) | ayobamiseun |
| 2026-11-12 | [fix(posting-guard): refuse --out inside the repository (#732)](https://github.com/ai-job-search-dev/ai-job-search/commit/790692f63a60abf01aadc6be0a7c351a0cb5ff3f) | ayobamiseun |
| 2026-11-11 | [docs(setup): give the private-repository path real commands in the qu…](https://github.com/ai-job-search-dev/ai-job-search/commit/a2e81c4fa65ccaf22d6163d5a946ff77ecea6348) | Yusuprozimemet |
| 2026-11-11 | [docs(readme): list job_key, page_decode, rank_state, scrape_state and…](https://github.com/ai-job-search-dev/ai-job-search/commit/9a3c852f1079ee6c846c18edcc400bf851eefd92) | ayobamiseun |

[See all commits ↗](https://github.com/ai-job-search-dev/ai-job-search/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ai-job-search-dev/ai-job-search.git
```
