# TauricResearch/TradingAgents

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/TauricResearch/TradingAgents)

> TradingAgents: Towards Agentic Finance Research

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
| ⭐ **Stars** | 123.9k |
| 🍴 **Forks** | 23.7k |
| 🐞 **Open issues + PRs** | [164](https://github.com/TauricResearch/TradingAgents/issues) |
| 💻 **Languages** | TypeScript 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `finance` `llm` `multiagent` `trading` |
| 🕒 **Last activity** | 2026-11-25 (2d ago) |
| 📅 **Created** | 2024-12-28 |
| 📦 **Latest release** | [v1.0.1](https://github.com/TauricResearch/TradingAgents/releases/tag/v1.0.1) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 11.2 MB |
| 🌐 **Website** | https://tauric.ai |

## 📦 Recent releases

### [v1.0.1](https://github.com/TauricResearch/TradingAgents/releases/tag/v1.0.1)
<sub>2026-11-25 · 2d ago</sub>

> **Fixed**
> - Plan mode: the PDF report shows the question you asked, with what you added while planning, instead of "Carry out the plan".
> - Reports: the report starts with the answer; progress notes written along the way are left out.
> - Price history: a one-year window that spans February 29 is no longer refused.
> - Correlation: returns over only three shared dates are refused instead of reported as a perfect +1 or -1; four dates are the minimum.
> - API keys: saving a key confirms it by the provider's name ("Stored the Tauric API key").
> …

### [v1.0.0](https://github.com/TauricResearch/TradingAgents/releases/tag/v1.0.0)
<sub>2026-11-24 · 3d ago</sub>

> - TradingAgents: Towards Agentic Finance Research.
> **Research**
> - Agents: Equity Research, Macro Strategy, Quant Research and Risk Analysis research in parallel and report back.
> - Skills: sixteen built-in research methods, from an earnings review to a DCF valuation.
> - Your own agents and skills, as Markdown files.
> - Plan mode: review and revise a research plan before it runs.
> …

### [v0.7.1](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.7.1) — TradingAgents v0.7.1
<sub>2026-10-27 · 1mo ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [release: TradingAgents 1.0.1](https://github.com/TauricResearch/TradingAgents/commit/121265d18d467ac717f7af99cb0d669c15d2e73c) | Yijia-Xiao |
| 2026-11-24 | [ci(npm): enable publishing for TradingAgents v1.0.0](https://github.com/TauricResearch/TradingAgents/commit/81501e0f108c9960f55f0f45b79cafa7857f2c0a) | Yijia-Xiao |
| 2026-11-24 | [release: TradingAgents 1.0.0](https://github.com/TauricResearch/TradingAgents/commit/da95d501c9363f0a58bb0ce5746a6d31cc15df2f) | Yijia-Xiao |
| 2026-11-04 | [announce Trading-R1 official release](https://github.com/TauricResearch/TradingAgents/commit/9fa1196fffbcfd9de5146d2dd2869df84ab99838) | Tauric-Research |
| 2026-10-27 | [Merge pull request #1613 from TauricResearch/v0.7.1](https://github.com/TauricResearch/TradingAgents/commit/c4544913a14ed3df5f1ed7b9e8483270ce20682a) | Yijia-Xiao |
| 2026-10-27 | [release: 0.7.1](https://github.com/TauricResearch/TradingAgents/commit/3e44faafa042daf953f6ec2422ae36bb1fd4f50f) | Yijia-Xiao |
| 2026-10-27 | [fix(tools): accept only the statement frequencies the vendors serve (…](https://github.com/TauricResearch/TradingAgents/commit/bf7f4b55a300ede4a8106022044cc473fcbe85af) | Yijia-Xiao |
| 2026-10-27 | [test: fix tests that failed on Windows and macOS (#1506, #1485, #1541)](https://github.com/TauricResearch/TradingAgents/commit/d46c052278646836ded214b693f15081fceed8ad) | Yijia-Xiao |
| 2026-10-27 | [build(docker): keep every .env file out of the image](https://github.com/TauricResearch/TradingAgents/commit/ec4e2c8e5adc9de0757ccc14e1bedc1c405d835f) | Yijia-Xiao |
| 2026-10-27 | [fix(cli): check a ticker with the data layer's own rule (#1604)](https://github.com/TauricResearch/TradingAgents/commit/a334a1f878f4d744c34230e216e613955762e26b) | Yijia-Xiao |

[See all commits ↗](https://github.com/TauricResearch/TradingAgents/commits)

## ⬇️ Get it

```bash
git clone https://github.com/TauricResearch/TradingAgents.git
```
