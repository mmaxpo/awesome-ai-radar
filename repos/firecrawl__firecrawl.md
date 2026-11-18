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
| ⭐ **Stars** | 202.8k |
| 🍴 **Forks** | 10.6k |
| 🐞 **Open issues + PRs** | [817](https://github.com/firecrawl/firecrawl/issues) |
| 💻 **Languages** | TypeScript 73% · Python 10% · Rust 5% · Java 3% · PHP 2% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai` `crawler` `markdown` `scraper` `html-to-markdown` `llm` `scraping` `web-crawler` `ai-scraping` `webscraping` `web-scraping` `web-data` `web-data-extraction` `ai-agents` `data-extraction` `ai-crawler` `ai-search` `web-scraper` `web-search` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2024-04-15 |
| 📦 **Latest release** | [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0) — 2026-06-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 188.1 MB |
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
| 2026-11-18 | [feat(api): send library commands down the catalogue-read path (#5832)](https://github.com/firecrawl/firecrawl/commit/25c130276117f3d6fe5e142147cc2414d6dee609) | capy-ai[bot] |
| 2026-11-18 | [Remove the support docs search method from the Elixir SDK and OpenAPI…](https://github.com/firecrawl/firecrawl/commit/0e535bc534e7050a9da1e5e70dd5f1a0a4e42eac) | mogery |
| 2026-11-18 | [feat(api): serve Alexandria provider calls from /v2/alexandria (#5826)](https://github.com/firecrawl/firecrawl/commit/9dc8170a0e9bd81e3d8e8d354d7258dd96ae3b3c) | developersdigest |
| 2026-11-17 | [feat(api): short redirect links for session downloads (#5828)](https://github.com/firecrawl/firecrawl/commit/0a585939b2d0ff9bbc4e8b1d2a41e4d8f9c74f1b) | tomsideguide |
| 2026-11-17 | [refactor(api): trim session file routes and share the storage client …](https://github.com/firecrawl/firecrawl/commit/e35d5e340c56dbcabf36350805a91d7ffc3681c6) | tomsideguide |
| 2026-11-17 | [feat(api): session, file and download link routes for the hosted MCP …](https://github.com/firecrawl/firecrawl/commit/b1a4d7521d0234bab45793fc72a587a45aec0684) | Ben2W |
| 2026-11-17 | [test(api): remove the v0 e2e snips (#5825)](https://github.com/firecrawl/firecrawl/commit/dc55805c2ebdfe389943d4c4bed86629423ac8d9) | mogery |
| 2026-11-17 | [README: update positioning to Firecrawl Alexandria (550+ providers) (…](https://github.com/firecrawl/firecrawl/commit/8ae5bed1d7ef3de532a29a981298da795361d115) | lauracodesatwork |
| 2026-11-17 | [refactor(api): move admin controllers out of controllers/v0 (#5615)](https://github.com/firecrawl/firecrawl/commit/b666afbab019df1a57328b9bc8db25d2c40552fe) | mogery |
| 2026-11-17 | [feat(api): authenticate to OpenAI with workload identity federation (…](https://github.com/firecrawl/firecrawl/commit/d69aa23c2008c35ffa929b92951bb60e16e403c3) | tomsideguide |

[See all commits ↗](https://github.com/firecrawl/firecrawl/commits)

## ⬇️ Get it

```bash
git clone https://github.com/firecrawl/firecrawl.git
```
