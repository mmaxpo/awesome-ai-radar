# firecrawl/firecrawl

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/firecrawl/firecrawl)

> Knowledge infrastructure to make your agents smarter. Search, scrape and access 550+ data providers through one API.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | Turn websites into clean LLM-ready markdown/data |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 211.4k |
| 🍴 **Forks** | 11.1k |
| 🐞 **Open issues + PRs** | [933](https://github.com/firecrawl/firecrawl/issues) |
| 💻 **Languages** | TypeScript 54% · Python 18% · Rust 9% · Java 5% · PHP 4% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai` `crawler` `markdown` `scraper` `html-to-markdown` `llm` `scraping` `web-crawler` `ai-scraping` `webscraping` `web-scraping` `web-data` `web-data-extraction` `ai-agents` `data-extraction` `ai-crawler` `ai-search` `web-scraper` `web-search` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2024-04-15 |
| 📦 **Latest release** | [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0) — 2026-06-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 191.5 MB |
| 🌐 **Website** | https://firecrawl.dev |

## 📦 Recent releases

### [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0) — Firecrawl v2.11.0
<sub>2026-06-19 · 5mo ago</sub>

> **Firecrawl v2.11.0**
> **Improvements**
> - **Firecrawl Research Index** — Added a specialized index for agentic AI/ML research: search across 3M+ arXiv papers and the GitHub code behind them (issues, merged PRs, and READMEs, refreshed daily), fetch a paper's details or related work, and check claims against full text. It has state-of-the-art recall on arXivQA, outperforming the next best provider by 18% at comparable cost. Available via the API, SDKs, MCP, and CLI.
> - **Keyless access for core endpoints** — Use `/scrape`, `/search`, `/interact`, and `/parse` without an API key from official MCP, CLI, and SDK clients.
> - **Automatic PII redaction** — Added a `redactPII` option that strips personal and sensitive data like names, emails, phone numbers, addresses, and secrets out of scraped content before it's returned.
> - **`deterministicJson` format** — Added a format that returns structured JSON without running an LLM on every request. Firecrawl generates a reusable extractor for your schema and caches it per site, so repeat scrapes are cheaper and return consistent results.
> …

### [v2.10](https://github.com/firecrawl/firecrawl/releases/tag/v2.10) — Firecrawl v2.10
<sub>2026-05-15 · 6mo ago</sub>

> **Firecrawl v2.10**
> **Improvements**
> - **`/parse` endpoint** — Upload local files (PDF, DOCX, DOC, ODT, RTF, XLSX, XLS, HTML) up to 50 MB and get back clean, LLM-ready Markdown, JSON, or a summary. Tables and reading order are preserved, with full Zero Data Retention support for enterprise plans. Available in JS, Python, Go, Rust, Java, .NET, PHP, Ruby, and Elixir SDKs.
> - **Lockdown Mode** — Set `lockdown: true` on `/scrape` to serve results exclusively from Firecrawl's index with zero outbound requests and zero data retention by default. Gated outbound paths include HTTP fetches, robots.txt, audio downloads, and media. Available in every SDK, the CLI (`--lockdown`), and MCP.
> - **`question` format** — Pass a natural-language prompt to `/scrape` and get a grounded, hallucination-free answer back in `data.question`. Runs on a managed model chain with automatic fallback, prompt-injection isolation via XML tagging and zero-width-space escaping, and up to 100x fewer tokens per call.
> - **`highlights` format** — Returns the exact sentences, code blocks, and table rows on a page that match your query. Consecutive sentences re-join into paragraphs, code lines wrap in fenced blocks with their original language, and table rows rebuild into Markdown tables with headers — all from the source page, using up to 100x fewer tokens per call.
> …

### [v2.9.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.9.0)
<sub>2026-04-10 · 7mo ago</sub>

> **Firecrawl v2.9.0**
> **Improvements**
> - **Browser Interaction via `/interact` endpoint** — Scrape a page, then call `/interact` to take actions on it — click buttons, fill forms, navigate deeper, or extract dynamic content. Describe what you want in natural language via `prompt`, or write Playwright code (Node.js, Python) and Bash (`agent-browser`) for full control. Sessions persist across calls, with live view and interactive live view URLs for real-time browser streaming. Persistent profiles let you save and reuse browser state (cookies, localStorage) across scrapes. Available in JS, Python, Java, and Rust SDKs.
> - **`query` format** — Added `query` format to the `/scrape` endpoint — pass a natural-language prompt and get a direct answer back in `data.answer`.
> - **`audio` format** — Added `audio` format option to scrape responses, returning audio output as a field on the document.
> - **`onlyCleanContent` parameter** — Added `onlyCleanContent` parameter to the `/scrape` endpoint, which strips navigation, ads, cookie banners, and other non-semantic content from markdown output.
> …

### [v2.8.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.8.0)
<sub>2026-02-03 · 9mo ago</sub>

> **v2.8.0**
> **Firecrawl v2.8.0 is here!**
> Firecrawl v2.8.0 brings major improvements to agent workflows, developer tooling, and self-hosted deployments across the API and SDKs, including our new Skill.
> * Parallel Agents for running thousands of `/agent` queries simultaneously, powered by our new Spark 1 Fast model.
> * Firecrawl CLI with full support for scrape, search, crawl, and map commands.
> * Firecrawl Skill for enabling AI agents (Claude Code, Codex, OpenCode) to use Firecrawl autonomously.
> …

### [v2.7.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.7.0)
<sub>2025-12-05 · 11mo ago</sub>

> **Firecrawl v2.7.0 is here!**
> - ZDR Search support for enterprise customers.
> - Improved Branding Format with better detection.
> - Partner Integrations API now in closed beta.
> - Faster and more accurate screenshots.
> - Self-hosted improvements
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [fix(api): strip NUL characters from markdown and html (#6104)](https://github.com/firecrawl/firecrawl/commit/cb8e1c09106eaa600dafad67806fbde5e0a708a8) | Chadha93 |
| 2026-11-26 | [chore(api): drop the unread active_crawls and crawls_by_team_id sets …](https://github.com/firecrawl/firecrawl/commit/68291b7a8c27d60b848a58f26e271be808912735) | abimaelmartell |
| 2026-11-26 | [feat(api): dedicated crawl state Redis and loud handling of missing c…](https://github.com/firecrawl/firecrawl/commit/d355ef9020e34abe52948f8e99577bdaf4d290fc) | abimaelmartell |
| 2026-11-25 | [chore(sdks): update package descriptions (#6080)](https://github.com/firecrawl/firecrawl/commit/d7ae564d3c49df3be44d344956675c43947517fc) | capy-ai[bot] |
| 2026-11-25 | [test(api): remove obsolete __experimental_omceDomain scrape snip test…](https://github.com/firecrawl/firecrawl/commit/83ed15240edefc4df591b2b2c229a0e57040a574) | mogery |
| 2026-11-25 | [fix(api): guard raw PDF prefetch temp-file unlink (#6077)](https://github.com/firecrawl/firecrawl/commit/1b8a5ff0112175f29f1a43b2af9a6692c05b3fac) | mogery |
| 2026-11-25 | [feat(api): add optional expires_at to auth chunk type and key_expired…](https://github.com/firecrawl/firecrawl/commit/b6b4d03589b841ddf6f57d8dba8b8671115a070d) | micahstairs |
| 2026-11-25 | [chore(api): log webhook host and events instead of full config (#6066)](https://github.com/firecrawl/firecrawl/commit/98ae8c7578cccb021560eca6158ca347420810bc) | abimaelmartell |
| 2026-11-25 | [refactor(api): complete modular service architecture, env cleanup, an…](https://github.com/firecrawl/firecrawl/commit/edd2574beed4b92a12cd83198de6f9ac6f0030ae) | mogery |
| 2026-11-25 | [feat(api): let search providers declare enterprise retention mode sup…](https://github.com/firecrawl/firecrawl/commit/0519b26a2b73c13048c0d29bce12c0306f7601ec) | abimaelmartell |

[See all commits ↗](https://github.com/firecrawl/firecrawl/commits)

## ⬇️ Get it

```bash
git clone https://github.com/firecrawl/firecrawl.git
```
