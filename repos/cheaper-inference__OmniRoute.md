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
| ⭐ **Stars** | 90.3k |
| 🍴 **Forks** | 14.0k |
| 🐞 **Open issues + PRs** | [876](https://github.com/cheaper-inference/OmniRoute/issues) |
| 💻 **Languages** | TypeScript 92% · JavaScript 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `a2a` `ai-agents` `ai-gateway` `anthropic` `claude` `claude-code` `cline` `codex` `copilot` `cursor` `deepseek` `free-ai` `gemini` `llm-gateway` `mcp` `openai` `openai-proxy` `qwen` `token-saver` `kimi` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v3.8.54](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.54) — 2026-11-17 |
| 🌿 **Default branch** | `release/v3.8.55` |
| 💾 **Size** | 3780.9 MB |
| 🌐 **Website** | https://omniroute.online |

## 📦 Recent releases

### [v3.8.54](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.54)
<sub>2026-11-17 · 8d ago</sub>

> **OmniRoute v3.8.54**
> - **Providers:** official "Sign in with ChatGPT" provider (`chatgpt`, PKCE + live model discovery); MiniMax Code (managed gateway + dashboard device-code sign-in); RenderHour (images, video, speech); MegaBrain (dual auth); EmpirioLabs, ParalonCloud, deAPI, Replicate chat, Cerebrium, Hetzner Inference and Grokified; native `opencode-server` executor; Microsoft 365 Copilot work/school sign-in; GitHub Copilot embeddings; Gemini Lyria 3 music models; custom JSON API provider nodes (request template + response path).
> - **Routing and combos:** endpoint-specific combo routes (chat, search/fetch, embeddings, rerank, images, video, music, OCR, audio) with capability-aware search/fetch combos; new `jev` and `expiry-first` strategies; preferred and reserve accounts for Auto combos; opt-in preferred-account response-start failover; opt-in deadline-failure sub-budget that ends a combo with a clean 504.
> - **Search:** Keenable web search and fetch provider (keyless by default) and `codex-search` through connected Codex accounts.
> - **API keys and usage:** `/v1/me/status` reports today's/this week's usage and every per-key limit; `/v1/me/sessions` self-service session listing; rolling 5-hour USD budget per key; reusable key policy templates; `POST /api/keys/import`; usage attributed to coding-agent sessions and projects; provider-reported cache-read and 5-minute/1-hour cache-write tiers carried through analytics.
> - **Agentic pipelines and streaming:** repeated-tool-round and consecutive-failure detection across native protocols; opt-in context compaction with per-model budgets; `STREAM_READINESS_TIMEOUT` now says which failure shape occurred; large request bodies to `api.anthropic.com` are gzip-compressed like Claude Code.
> …

### [v3.8.53](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.53)
<sub>2026-11-06 · 19d ago</sub>

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
<sub>2026-08-26 · 3mo ago</sub>

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
| 2026-11-25 | [Merge pull request #21204 from cheaper-inference/fix/release-v3.8.55-…](https://github.com/cheaper-inference/OmniRoute/commit/e6476f01a9fd0a76df12326cc742aeef00ffa63a) | diegosouzapw |
| 2026-11-25 | [fix(docker): drop all capabilities and forbid privilege gains in comp…](https://github.com/cheaper-inference/OmniRoute/commit/38f8e51e261a7593d10a525612a92198a224d9b8) | diegosouzapw |
| 2026-11-25 | [fix(docker): give the Bun web image the full Playwright installer (#2…](https://github.com/cheaper-inference/OmniRoute/commit/f639a2c887973663ef4b264e88d853f3c8923b09) | diegosouzapw |
| 2026-11-25 | [build(docker): run the Node images on Wolfi instead of Debian (#21177)](https://github.com/cheaper-inference/OmniRoute/commit/81668e27470846dda762d5b2eae51c0f4b7e0d38) | diegosouzapw |
| 2026-11-25 | [Merge pull request #21180 from cheaper-inference/fix/kea-9516-reserve…](https://github.com/cheaper-inference/OmniRoute/commit/8e8b8377b916b92f3f05277a64fff654ec147000) | diegosouzapw |
| 2026-11-25 | [Merge remote-tracking branch 'origin/release/v3.8.55' into fix/kea-95…](https://github.com/cheaper-inference/OmniRoute/commit/964e60c0d78930c0b7e490dbdf960617f3360a9e) | diegosouzapw |
| 2026-11-25 | [Merge pull request #21147 from cheaper-inference/fix/injection-guard-…](https://github.com/cheaper-inference/OmniRoute/commit/b4ff3daa62a5a707c4ca92ad17052898ee7b5db1) | diegosouzapw |
| 2026-11-25 | [Merge pull request #21176 from cheaper-inference/fix/stream-retained-…](https://github.com/cheaper-inference/OmniRoute/commit/badd29369f314e0fa57a87fc0f4851babd6b14f9) | diegosouzapw |
| 2026-11-25 | [Merge pull request #21152 from cheaper-inference/fix/stream-semantic-…](https://github.com/cheaper-inference/OmniRoute/commit/0b7113e66fd34c6fafdb9183ba477bdb50689a43) | diegosouzapw |
| 2026-11-25 | [Merge remote-tracking branch 'origin/release/v3.8.55' into fix/kea-95…](https://github.com/cheaper-inference/OmniRoute/commit/b4498dfd50e9c2d71edb787fcb4c3378a0154bf6) | diegosouzapw |

[See all commits ↗](https://github.com/cheaper-inference/OmniRoute/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cheaper-inference/OmniRoute.git
```
