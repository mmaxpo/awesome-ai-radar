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
| ⭐ **Stars** | 208.6k |
| 🍴 **Forks** | 10.9k |
| 🐞 **Open issues + PRs** | [924](https://github.com/firecrawl/firecrawl/issues) |
| 💻 **Languages** | TypeScript 74% · Python 10% · Rust 5% · Java 3% · PHP 2% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai` `crawler` `markdown` `scraper` `html-to-markdown` `llm` `scraping` `web-crawler` `ai-scraping` `webscraping` `web-scraping` `web-data` `web-data-extraction` `ai-agents` `data-extraction` `ai-crawler` `ai-search` `web-scraper` `web-search` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2024-04-15 |
| 📦 **Latest release** | [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0) — 2026-06-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 189.1 MB |
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
| 2026-11-24 | [refactor(api): register scrape engines and feature priorities on the …](https://github.com/firecrawl/firecrawl/commit/bfaa238fee1770e011c863c3717fa4a0a3249c11) | mogery |
| 2026-11-24 | [refactor(api): declare worker and deterministic JSON env vars with de…](https://github.com/firecrawl/firecrawl/commit/708bea10df3b5f88dc0834c37f5ce5279c83e2d9) | mogery |
| 2026-11-24 | [fix(api): keep error-serde free of config, database, and Redis import…](https://github.com/firecrawl/firecrawl/commit/1ecd596e47e9a561dfbb127231b112aca6735cfe) | mogery |
| 2026-11-24 | [fix(api): stop persisting unused Slack incoming webhook URLs (#6022)](https://github.com/firecrawl/firecrawl/commit/7cd29a248cc575522c01facf46c394fba7cc46d3) | micahstairs |
| 2026-11-24 | [feat(api): return the job id in v2 error responses and read it in the…](https://github.com/firecrawl/firecrawl/commit/ac30b86df0afc77800148f0027f06bbf3926c302) | micahstairs |
| 2026-11-24 | [Skip blocklist hit logging for zero data retention requests (#6007)](https://github.com/firecrawl/firecrawl/commit/c13b60d96c2e0d586b9abacb7c20ee4f81d391dc) | rahul-firecrawl |
| 2026-11-24 | [feat(api): stream Marketplace listing files through to Exchange (#6013)](https://github.com/firecrawl/firecrawl/commit/4924105f57c105fa678706e05fa234d66b5b061e) | developersdigest |
| 2026-11-23 | [feat(api): replay an Alexandria response from a cache when the record…](https://github.com/firecrawl/firecrawl/commit/6648cfa9679ae2a87301bf06a2109a2aaac9c735) | abimaelmartell |
| 2026-11-23 | [feat(api): proxy provider onboarding routes to Exchange (#5999)](https://github.com/firecrawl/firecrawl/commit/8538d3a8d18b7d4d6849cd5b2245a7d4d21f25b2) | developersdigest |
| 2026-11-23 | [feat(fresh-feed): support multi-vertical routing and upstream selecti…](https://github.com/firecrawl/firecrawl/commit/6069c7b5fdf4f1dc248e50fd784eb908d027f555) | KrisOei |

[See all commits ↗](https://github.com/firecrawl/firecrawl/commits)

## ⬇️ Get it

```bash
git clone https://github.com/firecrawl/firecrawl.git
```
