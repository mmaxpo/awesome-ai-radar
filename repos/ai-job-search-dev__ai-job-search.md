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
| ⭐ **Stars** | 72.9k |
| 🍴 **Forks** | 23.4k |
| 🐞 **Open issues + PRs** | [49](https://github.com/ai-job-search-dev/ai-job-search/issues) |
| 💻 **Languages** | Python 99% · TeX 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `ai-agents` `career` `claude-code` `cover-letter` `cv` `interview-preparation` `job-application` `job-hunting` `job-search` `latex` `resume` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-03-18 |
| 📦 **Latest release** | [v2.0.0](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v2.0.0) — 2026-11-16 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 5.8 MB |

## 📦 Recent releases

### [v2.0.0](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v2.0.0)
<sub>2026-11-16 · 5d ago</sub>

> **What's Changed**
> * fix(scrape): send one plain term per CLI call and make portals state their query syntax (#536) by @ai-tvang in https://github.com/ai-job-search-dev/ai-job-search/pull/653
> * fix(rank): report a non-object seen_jobs.json entry instead of a traceback by @rudycelekli in https://github.com/ai-job-search-dev/ai-job-search/pull/636
> * fix(salary): split combined name-and-city workbook columns by @mvanhorn in https://github.com/ai-job-search-dev/ai-job-search/pull/660
> * fix(fetch-page): decode standard zlib-wrapped HTTP deflate by @rudycelekli in https://github.com/ai-job-search-dev/ai-job-search/pull/711
> * fix(add-portal): keep generated tests offline in CI by @rudycelekli in https://github.com/ai-job-search-dev/ai-job-search/pull/714
> …

### [v1.7.5](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.5)
<sub>2026-11-09 · 12d ago</sub>

> **What's Changed**
> * fix(job-key): fold Latin letters without an NFKD decomposition and add --audit --migrate by @ai-tvang in https://github.com/ai-job-search-dev/ai-job-search/pull/637
> * fix(notion-sync): re-key a row matched by URL when its Key has drifted by @ai-tvang in https://github.com/ai-job-search-dev/ai-job-search/pull/761
> * fix(install): find bun at standard install locations when PATH misses it (fixes #707) by @ahmed-husssain in https://github.com/ai-job-search-dev/ai-job-search/pull/762
> * fix(fetch-page): pass --compressed only when curl supports it (fixes #705) by @ahmed-husssain in https://github.com/ai-job-search-dev/ai-job-search/pull/759
> * fix(scrape): force UTF-8 output in scrape_state.py by @harshajv7981 in https://github.com/ai-job-search-dev/ai-job-search/pull/744
> …

### [v1.7.4](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.4)
<sub>2026-11-02 · 19d ago</sub>

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

### [v1.7.2](https://github.com/ai-job-search-dev/ai-job-search/releases/tag/v1.7.2) — v1.7.2 - Measured PDFs, CLIs that stop trusting the digits, tools that survive n…
<sub>2026-09-29 · 1mo ago</sub>

> A patch release with one theme: **the checks the workflow documented now actually run, and the tools stop breaking on anything that is not ASCII.** Compiled PDFs get measured instead of eyeballed, the portal CLIs stop trusting the digits in a URL, and every Python tool survives a Cyrillic posting or a Turkish robots.txt on Windows. Thirty-two entries, twenty-four of them fixes, most reported and fixed by contributors within days of each other.
> **Highlights**
> **`/apply` measures the PDF instead of looking at it (#378, #476, #458, #498, #465)**
> `tools/verify_layout.py` measures what Step 5b previously only eyeballed: per-page text extent, bottom whitespace, the largest internal gap, footer collisions, and an entry header stranded at a page break. It exists for a failure every other check missed: a moderncv `\cventry` is unbreakable, so an entry that does not fit jumps to the next page and leaves a hole while the document still compiles, still has the right page count, and still passes `verify_pdf.py`. Step 5b now also runs the page-count check it had been claiming Step 5d ran (nothing in the workflow passed `--pages` at all). `verify_pdf.py --contains` sees through LaTeX's typographic substitutions, so `--contains "Master's degree"` and `--contains "2016-2024"` no longer report a keyword missing from a document that plainly contains it, and the new `--ascii-dates` flag reads the raw text layer for the one thing the fold must not hide: a year joined to an en-dash, which a real Workday import dropped together with the date. Poppler stays optional; a missing or xpdf `pdftotext` degrades to a `skipped:` exit 2 that now names both causes.
> **Portal CLIs stop trusting the digits (#448, #500, #435, #460, #504, #505)**
> `jobindex-search detail` fetched any URL verbatim and, when the path did not match, returned a well-formed fake posting built from whatever page came back. `linkedin-search detail` took the first six-plus-digit segment from any URL, so a Greenhouse or Lever apply link fetched whichever LinkedIn posting carried that number, with exit 0. Both now parse the host for real and exit 1 with the `BAD_ID` contract before any request, matching the rest of the CLIs. `jobnet-search detail` no longer reports an externally hosted ad as not found, `jobdanmark-search detail` backs off on 429/5xx like every other portal, and `freehire-search` decodes HTML entities in titles and keeps the salary period, so a yearly figure no longer reads as monthly.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [feat(setup): recommend a minimal TeX install instead of texlive-full …](https://github.com/ai-job-search-dev/ai-job-search/commit/b3ea106cac34b783ae4d5708a9e6d97f6660d084) | jakob1379 |
| 2026-11-19 | [fix(posting-guard): detect CSS invisibility tricks in inline styles (…](https://github.com/ai-job-search-dev/ai-job-search/commit/d2afe00bfc9b7be8ffc2ee41acc22570970b76d4) | ahmed-husssain |
| 2026-11-18 | [fix(posting-guard): refuse input with no text to evaluate and exit 1 …](https://github.com/ai-job-search-dev/ai-job-search/commit/7b1cd4495967cfa4a781b8f5913f4c806c4c1f82) | ahmed-husssain |
| 2026-11-18 | [ci: check PR titles against Conventional Commits with commitizen (#863)](https://github.com/ai-job-search-dev/ai-job-search/commit/ee13aa4f0e5c02e2e4c16bc8ea8f159ab614fa15) | jakob1379 |
| 2026-11-17 | [ci: add a stable CLI checks result job for required checks (#856)](https://github.com/ai-job-search-dev/ai-job-search/commit/f0195d1864549ea0f58e00e527398a8905f3d5d9) | jakob1379 |
| 2026-11-16 | [feat!: move the portal skills to community-portals (#829)](https://github.com/ai-job-search-dev/ai-job-search/commit/745e6770dbcfb524ee245c89be0ff8df95924919) | jakob1379 |
| 2026-11-12 | [fix(scrape): deduplicate candidates on the canonical key so store nev…](https://github.com/ai-job-search-dev/ai-job-search/commit/0d0d1a907a21454affa1b694acc4e2c5008a0d21) | ayobamiseun |
| 2026-11-12 | [fix(upskill): leave jobs /rank vetoed on location or language out of …](https://github.com/ai-job-search-dev/ai-job-search/commit/8fc6d7c860b0ffff3fdb744e007ca255c02c8385) | TheMattHub |
| 2026-11-12 | [fix(cover-letter): load Raleway's bold face in the bullet-list font w…](https://github.com/ai-job-search-dev/ai-job-search/commit/8e814e57ac487d5f15675bb13ed07f95c9765c4a) | TheMattHub |
| 2026-11-12 | [fix(guards): check command and agent files in subfolders too (#735)](https://github.com/ai-job-search-dev/ai-job-search/commit/e686ff24f634bbf40cb4c21e38d61d734f90ac26) | ayobamiseun |

[See all commits ↗](https://github.com/ai-job-search-dev/ai-job-search/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ai-job-search-dev/ai-job-search.git
```
