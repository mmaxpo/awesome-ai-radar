# cheaper-inference/OmniRoute

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/cheaper-inference/OmniRoute)

> Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Free AI gateway: one endpoint for many providers |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 90.0k |
| 🍴 **Forks** | 14.0k |
| 🐞 **Open issues + PRs** | [861](https://github.com/cheaper-inference/OmniRoute/issues) |
| 💻 **Languages** | TypeScript 93% · JavaScript 6% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `a2a` `ai-agents` `ai-gateway` `anthropic` `claude` `claude-code` `cline` `codex` `copilot` `cursor` `deepseek` `free-ai` `gemini` `llm-gateway` `mcp` `openai` `openai-proxy` `qwen` `token-saver` `kimi` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v3.8.54](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.54) — 2026-11-17 |
| 🌿 **Default branch** | `release/v3.8.55` |
| 💾 **Size** | 3711.7 MB |
| 🌐 **Website** | https://omniroute.online |

## 📦 Recent releases

### [v3.8.54](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.54)
<sub>2026-11-17 · 7d ago</sub>

> **OmniRoute v3.8.54**
> - **Providers:** official "Sign in with ChatGPT" provider (`chatgpt`, PKCE + live model discovery); MiniMax Code (managed gateway + dashboard device-code sign-in); RenderHour (images, video, speech); MegaBrain (dual auth); EmpirioLabs, ParalonCloud, deAPI, Replicate chat, Cerebrium, Hetzner Inference and Grokified; native `opencode-server` executor; Microsoft 365 Copilot work/school sign-in; GitHub Copilot embeddings; Gemini Lyria 3 music models; custom JSON API provider nodes (request template + response path).
> - **Routing and combos:** endpoint-specific combo routes (chat, search/fetch, embeddings, rerank, images, video, music, OCR, audio) with capability-aware search/fetch combos; new `jev` and `expiry-first` strategies; preferred and reserve accounts for Auto combos; opt-in preferred-account response-start failover; opt-in deadline-failure sub-budget that ends a combo with a clean 504.
> - **Search:** Keenable web search and fetch provider (keyless by default) and `codex-search` through connected Codex accounts.
> - **API keys and usage:** `/v1/me/status` reports today's/this week's usage and every per-key limit; `/v1/me/sessions` self-service session listing; rolling 5-hour USD budget per key; reusable key policy templates; `POST /api/keys/import`; usage attributed to coding-agent sessions and projects; provider-reported cache-read and 5-minute/1-hour cache-write tiers carried through analytics.
> - **Agentic pipelines and streaming:** repeated-tool-round and consecutive-failure detection across native protocols; opt-in context compaction with per-model budgets; `STREAM_READINESS_TIMEOUT` now says which failure shape occurred; large request bodies to `api.anthropic.com` are gzip-compressed like Claude Code.
> …

### [v3.8.53](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.53)
<sub>2026-11-06 · 18d ago</sub>

> **OmniRoute v3.8.53**
> **1,189 documented changes** from 1,162 commits in the cycle, with **222 people** contributing. Thank you all.
> 📄 **Complete release notes** (every entry, full description and credit): attached below as `CHANGELOG-v3.8.53.md`, and in [`CHANGELOG.md` → `[3.8.53]`](https://github.com/cheaper-inference/OmniRoute/blob/main/CHANGELOG.md).
> ⚠️ Known at release time: `providers.apiRegionLabel` (fi, ko, pl, pt, pt-BR, zh-CN, zh-TW) and `providers.apiRegionInternational` (fi) show their English text until they are retranslated in v3.8.54.
> **📊 Release by the numbers**
> | | |
> …

### [v3.8.52](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.52)
<sub>2026-10-19 · 1mo ago</sub>

> **OmniRoute v3.8.52**
> **1,442 documented changes** — 135 features, 1,112 fixes and 195 maintenance entries from 1,386 commits in the cycle, with **306 external contributors**. Thank you all.
> 📄 **Complete release notes** (every entry, full description and credit): attached below as `CHANGELOG-v3.8.52.md`, and in [`CHANGELOG.md` → `[3.8.52]`](https://github.com/diegosouzapw/OmniRoute/blob/v3.8.52/CHANGELOG.md).
> ⚠️ Known at release time: the i18n mirrors of `docs/reference/ENVIRONMENT.md`, `docs/architecture/RESILIENCE_GUIDE.md` and `docs/security/GUARDRAILS.md` (and 11 more sources) lag the English text; the re-translation wave lands in the next cycle (#15306).
> **📊 Release by the numbers**
> | | |
> …

### [v3.8.51](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.51)
<sub>2026-09-30 · 1mo ago</sub>

> **OmniRoute v3.8.51**
> **2,022 documented changes** — 235 features, 1,454 fixes and 333 maintenance entries from 1,973 commits in the cycle, with **301 external contributors**. Thank you all.
> 📄 **Complete release notes** (every entry, full description and credit): attached below as `CHANGELOG-v3.8.51.md`, and in [`CHANGELOG.md` → `[3.8.51]`](https://github.com/diegosouzapw/OmniRoute/blob/main/CHANGELOG.md). GitHub caps a release body at 125,000 characters, so the 1,454 fixes and 333 maintenance entries live there in full.
> **📊 Release by the numbers**
> | | |
> | --- | ---: |
> …

### [v3.8.50](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.50)
<sub>2026-08-26 · 2mo ago</sub>

> **📊 Release by the numbers**
> | | |
> | --- | ---: |
> | 👥 People who contributed | **248** |
> | 📝 Commits in the cycle | **1,714** |
> | 🔀 Pull requests referenced | **1,666** |
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Merge pull request #21090 from cheaper-inference/feat/opencode-zen-go…](https://github.com/cheaper-inference/OmniRoute/commit/264eb34420498d976ebeb4c607531a8209893346) | diegosouzapw |
| 2026-11-24 | [Merge pull request #21082 from cheaper-inference/fix/kilo-paid-model-…](https://github.com/cheaper-inference/OmniRoute/commit/af292fe49fd207de99c2c73d9454a777ac51d0e2) | diegosouzapw |
| 2026-11-24 | [Merge pull request #21081 from cheaper-inference/fix/rtk-preserve-err…](https://github.com/cheaper-inference/OmniRoute/commit/7cdf9a4d4ea5f0caee7ad08a217a0bb43917a664) | diegosouzapw |
| 2026-11-24 | [Merge pull request #21080 from cheaper-inference/fix/cline-daily-free…](https://github.com/cheaper-inference/OmniRoute/commit/b65b8a728ccc8b97cfe5d61509c047635fd92aea) | diegosouzapw |
| 2026-11-24 | [fix(db): run the migration-numbering gate in the pre-commit hook when…](https://github.com/cheaper-inference/OmniRoute/commit/eff2a475edf1d282db4b2ac485c9098df2de96de) | diegosouzapw |
| 2026-11-24 | [Merge pull request #20891 from cheaper-inference/fix/salvage-20106-v3855](https://github.com/cheaper-inference/OmniRoute/commit/817ebfb2c0934a9769b01fe9beffc6b4387fd357) | diegosouzapw |
| 2026-11-24 | [Merge pull request #20216 from KiaroSama/fix/pr-comparison-base-20261114](https://github.com/cheaper-inference/OmniRoute/commit/b47ecc93c8101d5fcc9188cde7e2a3b84c0eca1b) | diegosouzapw |
| 2026-11-24 | [Merge pull request #20539 from cheaper-inference/feat/ui-kit-0-43-ado…](https://github.com/cheaper-inference/OmniRoute/commit/3648db7a48138c87fbeda683260f1a69c96fd4aa) | diegosouzapw |
| 2026-11-24 | [Merge pull request #21145 from cheaper-inference/fix/release-v3.8.55-…](https://github.com/cheaper-inference/OmniRoute/commit/9a663869b73399e47d0d2a93f21a2fbdf48ffb37) | diegosouzapw |
| 2026-11-24 | [test(quota): read the reset hint's wait instead of matching one shape](https://github.com/cheaper-inference/OmniRoute/commit/c5a324e5ca15abe01db9a62f7f391a4886efe951) | diegosouzapw |

[See all commits ↗](https://github.com/cheaper-inference/OmniRoute/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cheaper-inference/OmniRoute.git
```
