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
| ⭐ **Stars** | 200.8k |
| 🍴 **Forks** | 10.6k |
| 🐞 **Open issues + PRs** | [790](https://github.com/firecrawl/firecrawl/issues) |
| 💻 **Languages** | TypeScript 73% · Python 12% · Rust 3% · Java 3% · PHP 2% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-crawler` `ai-scraping` `ai-search` `crawler` `data-extraction` `html-to-markdown` `llm` `markdown` `scraper` `scraping` `web-crawler` `web-data` `web-data-extraction` `web-scraper` `web-scraping` `web-search` `webscraping` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2024-04-15 |
| 📦 **Latest release** | [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0) — 2026-06-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 186.5 MB |
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
<sub>2026-05-15 · 5mo ago</sub>

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
| 2026-11-11 | [fix(api): accept World ID's advertised Orb acr values (#5678)](https://github.com/firecrawl/firecrawl/commit/32fa6f6273daecc9675d41dc2dab44c61e8cc500) | erikengervall |
| 2026-11-10 | [feat(api): serve government web searches through the Government Index (#5672)](https://github.com/firecrawl/firecrawl/commit/346045851ba7ce96771a313f1f591a201065476f) | netankit |
| 2026-11-10 | [test(api): stop v1 snips at the v1 sunset and check the 410 (#5675)](https://github.com/firecrawl/firecrawl/commit/5c57e8765e6c5af6fe71a9f88265e8137ad94b47) | mogery |
| 2026-11-10 | [feat(api): sunset /extract on 2026-12-10 and point it at its migration guide (#5607)](https://github.com/firecrawl/firecrawl/commit/394aba10e8b09b97d3f84d279b391b3b77549658) | mogery |
| 2026-11-10 | [feat(api): sunset deep-research and llmstxt, with surface keys and migration links (#5606)](https://github.com/firecrawl/firecrawl/commit/603d3ec4a7f7ef7e0b1c3e5c8ec5a514bca8e1b7) | mogery |
| 2026-11-10 | [feat(api): deprecation notices on every v1 route (#5604)](https://github.com/firecrawl/firecrawl/commit/52ecbfc0766bd5cce928aef1ce278b1b27f7d504) | mogery |
| 2026-11-10 | [feat(api): point v0 deprecation notices at the v0 migration guide (#5623)](https://github.com/firecrawl/firecrawl/commit/a9ca1a386b8ae1858646fc453b3c3bb897ff9ab1) | mogery |
| 2026-11-10 | [feat(api): pass team_id to fire-engine chrome-cdp scrapes (#5670)](https://github.com/firecrawl/firecrawl/commit/3cfb9b54d069302aaf58f61bbdb0345b2224db8a) | rowinsg |
| 2026-11-10 | [perf(alexandria): fewer round trips around a provider call (#5662)](https://github.com/firecrawl/firecrawl/commit/df271b3d76e9bb08f61b1ff6552585578f029176) | KrisOei |
| 2026-11-09 | [fix(alexandria): retry provider pre-checks once when the connection drops (#5658)](https://github.com/firecrawl/firecrawl/commit/c8a5b7a1d53748975b524f5392c5e0b93e5410e5) | KrisOei |

[See all commits ↗](https://github.com/firecrawl/firecrawl/commits)

## 👥 Top contributors

[nickscamara](https://github.com/nickscamara) (1906) · [mogery](https://github.com/mogery) (1797) · [rafaelsideguide](https://github.com/rafaelsideguide) (597) · [abimaelmartell](https://github.com/abimaelmartell) (365) · [developersdigest](https://github.com/developersdigest) (257)

## ⬇️ Get it

```bash
git clone https://github.com/firecrawl/firecrawl.git
```
