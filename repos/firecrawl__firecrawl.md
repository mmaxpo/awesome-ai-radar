# firecrawl/firecrawl

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/firecrawl/firecrawl)

> Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥

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
| ⭐ **Stars** | 201.4k |
| 🍴 **Forks** | 10.6k |
| 🐞 **Open issues + PRs** | [797](https://github.com/firecrawl/firecrawl/issues) |
| 💻 **Languages** | TypeScript 72% · Python 11% · Rust 5% · Java 3% · PHP 2% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai` `crawler` `markdown` `scraper` `html-to-markdown` `llm` `scraping` `web-crawler` `ai-scraping` `webscraping` `web-scraping` `web-data` `web-data-extraction` `ai-agents` `data-extraction` `ai-crawler` `ai-search` `web-scraper` `web-search` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2024-04-15 |
| 📦 **Latest release** | [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0) — 2026-06-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 186.6 MB |
| 🌐 **Website** | https://firecrawl.dev |

## 📦 Recent releases

### [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0) — Firecrawl v2.11.0
<sub>2026-06-19 · 4mo ago</sub>

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
| 2026-11-13 | [Forward zero data retention to Exchange from the exchange proxy (#5736)](https://github.com/firecrawl/firecrawl/commit/eaa56e8803b8d15336503d2c26fccb0ca6b99d18) | developersdigest |
| 2026-11-12 | [feat(api): give the keyless provider-tools 403 a signup link (#5734)](https://github.com/firecrawl/firecrawl/commit/ab3acea889c724e8d7ebc48839e74cb16d8ca7a1) | nickscamara |
| 2026-11-12 | [feat(api): hosted bash for agents at /v2/bash (experiment, off by def…](https://github.com/firecrawl/firecrawl/commit/793fd57f133b71426bb6ce65641428c28b883e36) | Ben2W |
| 2026-11-12 | [chore(api): remove extraction provider (#5730)](https://github.com/firecrawl/firecrawl/commit/ace3c58bc88f0fccdabc8ec6483f8c935eaa6a9c) | abimaelmartell |
| 2026-11-12 | [perf(api): compress exchange route responses (#5729)](https://github.com/firecrawl/firecrawl/commit/755ff8cb00f691b9a7ccf4673e4aa15ee8f1e19f) | KrisOei |
| 2026-11-12 | [test(api): stop extract snips at the extract sunset and check the 410…](https://github.com/firecrawl/firecrawl/commit/902a083b95329d2f892e1dc2f76877363504e07b) | mogery |
| 2026-11-12 | [fix(api): keep page engines when stealth proxy is unavailable (#5713)](https://github.com/firecrawl/firecrawl/commit/b3868a988173f2eacf1ba9286e566757038ca71b) | abimaelmartell |
| 2026-11-12 | [docs(readme): mention Alexandria and note it runs on Firecrawl Cloud …](https://github.com/firecrawl/firecrawl/commit/0b64de1d651bd8e15e01a0a2f085e7b5edc9bce3) | claude[bot] |
| 2026-11-12 | [test(api): stop deep research and llms.txt snips at their sunset and …](https://github.com/firecrawl/firecrawl/commit/4c4275fa8a2cac3307ac6279b3fe8aa59e4345b8) | mogery |
| 2026-11-12 | [feat(sdks): pass gov search sources and type the gov result group (#5…](https://github.com/firecrawl/firecrawl/commit/1fcb57c3e324345d5fd342388d653951deb89220) | erikengervall |

[See all commits ↗](https://github.com/firecrawl/firecrawl/commits)

## ⬇️ Get it

```bash
git clone https://github.com/firecrawl/firecrawl.git
```
