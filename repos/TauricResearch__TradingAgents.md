# TauricResearch/TradingAgents

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/TauricResearch/TradingAgents)

> TradingAgents: Multi-Agents LLM Financial Trading Framework

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Multi-agent LLM trading framework (analyst, risk, trader roles) |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 123.4k |
| 🍴 **Forks** | 23.6k |
| 🐞 **Open issues + PRs** | [158](https://github.com/TauricResearch/TradingAgents/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `finance` `llm` `multiagent` `trading` |
| 🕒 **Last activity** | 2026-11-17 (4d ago) |
| 📅 **Created** | 2024-12-28 |
| 📦 **Latest release** | [v0.7.1](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.7.1) — 2026-10-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 6.6 MB |
| 🌐 **Website** | https://tauric.ai |

## 📦 Recent releases

### [v0.7.1](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.7.1) — TradingAgents v0.7.1
<sub>2026-10-27 · 25d ago</sub>

> Decisions are scored only on final closes and settle across long market holidays, a model's unpadded date no longer reads filings made after the run date, and fixes to portfolios, prices, SEC statements, reports, Azure and Claude settings.
> **Upgrading from 0.7.0**
> - Docker images no longer include `.env.enterprise`. For Azure OpenAI in Docker, put its keys in `.env`.
> **Fixed**
> - A date a model passes without zero padding, such as `2024-7-5`, is read as that date. It could compare as later than a filing made after the run date, and SEC EDGAR then served that filing. (#1488)
> - A decision is no longer scored on the bar of a session still trading, and one made before a market closure longer than a week, such as a national holiday, settles once trading resumes instead of staying pending. (#1548, #1539)
> …

### [v0.7.0](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.7.0) — TradingAgents v0.7.0
<sub>2026-10-16 · 1mo ago</sub>

> Runs on your ChatGPT plan, backtests scored from the first close after each decision, a note at start-up when a newer release is out, and a wheel attached to each GitHub release.
> **Added**
> - **Your ChatGPT plan.** The `chatgpt` provider runs TradingAgents on a ChatGPT Plus or Pro plan instead of an API key, through OpenAI's sign-in for open-source apps. Choose "Subscription" in the CLI's provider menu; for unattended runs, Docker and Python (`llm_provider="chatgpt"`), sign in once with `tradingagents login chatgpt`. `tradingagents logout chatgpt` revokes the sign-in. The CLI lists the plan's models, and reasoning effort applies as it does for OpenAI. (#1194, #1475)
> - **What's new at start-up.** The interactive CLI mentions a newer release, with the command that upgrades this install when it can tell how TradingAgents was installed, and notices from Tauric Research for the running version. It checks at most once a day in the background, so a run never waits on it; runs without a terminal never check, and `TRADINGAGENTS_NO_UPDATE_CHECK=1` turns it off.
> - **Release downloads.** Each GitHub release carries the source archive and a wheel, so a version installs with `pip install` from its release page without cloning.
> **Upgrading from 0.6.0**
> …

### [v0.6.0](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.6.0) — TradingAgents v0.6.0
<sub>2026-10-03 · 1mo ago</sub>

> HTML reports, a provider per model tier, past decisions settled for every ticker while the analysts work, and company news read while Yahoo's news feed is down.
> **Added**
> - **HTML report.** A saved report also includes `complete_report.html`, the report as one page with its sections listed beside the text, that reads well in a browser, on a phone and in print. Answering the save question at the prompt also asks about the page and can open it in your browser; `--no-html` or `save_reports(..., html=False)` skips it. The page is self-contained: it loads nothing and runs nothing. (#1419)
> - **A provider per model tier.** The quick and deep models can run on different providers, for example the managers on Claude while the analysts run on OpenAI: set `deep_think_provider` or `quick_think_provider` (`TRADINGAGENTS_DEEP_THINK_PROVIDER`, `TRADINGAGENTS_QUICK_THINK_PROVIDER`) with the tier's model. The report header names each tier's provider. (#1440)
> - **Past decisions settle alongside the analysts.** While a run's analysts work, every logged decision whose holding period has passed is settled, for any ticker, not only the one being analyzed. If settling fails, the run goes on and the report header says so. (#1428, #1445)
> - **Crypto on Reddit.** For a crypto ticker the Sentiment Analyst reads r/CryptoCurrency and r/CryptoMarkets, plus r/Bitcoin, r/ethereum or r/solana for those coins, instead of the stock subreddits. (#1461)
> …

### [v0.5.2](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.5.2) — TradingAgents v0.5.2
<sub>2026-09-29 · 1mo ago</sub>

> Parallel analysts, unattended CLI runs, reports that record what produced them,
> and past runs served only what was known on their date.
> **Added**
> - **Parallel analysts.** The selected analysts run at the same time, so the analyst phase takes about as long as the slowest one; the CLI shows each analyst's progress and time as it finishes, and the debate starts when all reports are in. (#1255, #433)
> - **Unattended CLI runs.** Flags answer the per-run questions, and `TRADINGAGENTS_*` variables the rest, so a scheduled job or script asks nothing: `tradingagents --ticker NVDA --date 2026-09-26 --analysts market,news --save --no-show`. Without a terminal, a missing answer stops the run before it starts and names what to set. (#1127, #1133)
> - **Reports record what produced them.** Each report opens with the analysis date, version, provider, models, analysts, rounds and data vendors; the state log keeps them as `run_settings`. (#752, #1197)
> …

### [v0.5.1](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.5.1) — TradingAgents v0.5.1
<sub>2026-09-24 · 1mo ago</sub>

> A package layout organised by what each module holds, social posts screened by
> TypeSafe's Jev when a key is set, GPT-6 Sol and Luna as the default models, and
> fixes to run isolation, SEC EDGAR statements and historical runs.
> **Upgrading from 0.5.0**
> Some modules moved, and the old import paths are gone. Update imports as follows:
> - `tradingagents.dataflows.interface` is `tradingagents.dataflows.router`, and `dataflows.symbol_utils` is `dataflows.symbols`. `dataflows.utils` is gone: `get_current_date` is in `dataflows.date_window`, `safe_ticker_component` in `dataflows.symbols`.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-04 | [announce Trading-R1 official release](https://github.com/TauricResearch/TradingAgents/commit/9fa1196fffbcfd9de5146d2dd2869df84ab99838) | Tauric-Research |
| 2026-10-27 | [Merge pull request #1613 from TauricResearch/v0.7.1](https://github.com/TauricResearch/TradingAgents/commit/c4544913a14ed3df5f1ed7b9e8483270ce20682a) | Yijia-Xiao |
| 2026-10-27 | [release: 0.7.1](https://github.com/TauricResearch/TradingAgents/commit/3e44faafa042daf953f6ec2422ae36bb1fd4f50f) | Yijia-Xiao |
| 2026-10-27 | [fix(tools): accept only the statement frequencies the vendors serve (…](https://github.com/TauricResearch/TradingAgents/commit/bf7f4b55a300ede4a8106022044cc473fcbe85af) | Yijia-Xiao |
| 2026-10-27 | [test: fix tests that failed on Windows and macOS (#1506, #1485, #1541)](https://github.com/TauricResearch/TradingAgents/commit/d46c052278646836ded214b693f15081fceed8ad) | Yijia-Xiao |
| 2026-10-27 | [build(docker): keep every .env file out of the image](https://github.com/TauricResearch/TradingAgents/commit/ec4e2c8e5adc9de0757ccc14e1bedc1c405d835f) | Yijia-Xiao |
| 2026-10-27 | [fix(cli): check a ticker with the data layer's own rule (#1604)](https://github.com/TauricResearch/TradingAgents/commit/a334a1f878f4d744c34230e216e613955762e26b) | Yijia-Xiao |
| 2026-10-27 | [fix(llm): read a dated Claude snapshot's version without its date (#1…](https://github.com/TauricResearch/TradingAgents/commit/ae0424745ef8684bbe9db91a01effb84d40c8223) | Yijia-Xiao |
| 2026-10-27 | [fix(llm): pass the output-token cap and a configured endpoint to Azur…](https://github.com/TauricResearch/TradingAgents/commit/347974a000b66d9fe463c4d17b8f6e08dbdcce9a) | Yijia-Xiao |
| 2026-10-27 | [fix(polymarket): keep a long shot's odds from printing as 0% or 100% …](https://github.com/TauricResearch/TradingAgents/commit/b78f136ba3c9e7205fbbd79c7f337a4cac21ce25) | Yijia-Xiao |

[See all commits ↗](https://github.com/TauricResearch/TradingAgents/commits)

## ⬇️ Get it

```bash
git clone https://github.com/TauricResearch/TradingAgents.git
```
