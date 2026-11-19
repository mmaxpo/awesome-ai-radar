# firecrawl/firecrawl

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/firecrawl/firecrawl)

> Knowledge infrastructure to make your agents smarter. Search, scrape and 550+ data providers through one API.

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
| ⭐ **Stars** | 203.7k |
| 🍴 **Forks** | 10.7k |
| 🐞 **Open issues + PRs** | [833](https://github.com/firecrawl/firecrawl/issues) |
| 💻 **Languages** | TypeScript 73% · Python 10% · Rust 5% · Java 3% · PHP 2% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai` `crawler` `markdown` `scraper` `html-to-markdown` `llm` `scraping` `web-crawler` `ai-scraping` `webscraping` `web-scraping` `web-data` `web-data-extraction` `ai-agents` `data-extraction` `ai-crawler` `ai-search` `web-scraper` `web-search` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2024-04-15 |
| 📦 **Latest release** | [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0) — 2026-06-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 188.0 MB |
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
| 2026-11-18 | [fix(branding): don't cut surrogate pairs when the branding script tru…](https://github.com/firecrawl/firecrawl/commit/1510bc4fff9c7014f6fa5be0f821ece168a69d13) | abimaelmartell |
| 2026-11-18 | [fix(branding): read the brand name from either end of the page title …](https://github.com/firecrawl/firecrawl/commit/e22933303269cb724cd3cd0ab3a98d9886919225) | abimaelmartell |
| 2026-11-18 | [chore(python-sdk): release 4.58.0 (#5835)](https://github.com/firecrawl/firecrawl/commit/24002c681a9b827b953ac6c4a4729c6ea9783648) | KrisOei |
| 2026-11-18 | [feat(search): per-team overrides for the Research Index daily limit (…](https://github.com/firecrawl/firecrawl/commit/20dfb471c61d8f6751fb6d08ed29cb26e21d738b) | KrisOei |
| 2026-11-18 | [feat(api): gzip research responses (#5849)](https://github.com/firecrawl/firecrawl/commit/158050d0bcdef9dab97f0ea7a830c0b5f9e081ca) | KrisOei |
| 2026-11-18 | [fix(security): drop rand 0.7.3 by moving kuchikiki to 0.8.9-speedread…](https://github.com/firecrawl/firecrawl/commit/7c16513e6ada9df5d9a6cfa6a1a1cfda3c841f9d) | mogery |
| 2026-11-18 | [fix(security): move zip to 9.5.1 through anydoc 0.2.5 (#5851)](https://github.com/firecrawl/firecrawl/commit/31a321ca5e0009b2cf9b9446f9b2e8b5ed9a31bf) | mogery |
| 2026-11-18 | [chore(js-sdk): release 4.55.0](https://github.com/firecrawl/firecrawl/commit/b7776ccb842b7e8aeb1be908b4d4d2936bec2ba2) | KrisOei |
| 2026-11-18 | [fix(webhook): publish zero data retention webhooks to a dedicated exp…](https://github.com/firecrawl/firecrawl/commit/88611467f2d22d25d7b56f8bf27476362d9af892) | rahul-firecrawl |
| 2026-11-18 | [feat(api): bill the fresh feed per returned record (#5848)](https://github.com/firecrawl/firecrawl/commit/caae4319794ac3b345a6d927a9327cb9d5c345f8) | KrisOei |

[See all commits ↗](https://github.com/firecrawl/firecrawl/commits)

## ⬇️ Get it

```bash
git clone https://github.com/firecrawl/firecrawl.git
```
