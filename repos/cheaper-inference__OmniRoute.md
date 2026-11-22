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
| ⭐ **Stars** | 89.5k |
| 🍴 **Forks** | 13.8k |
| 🐞 **Open issues + PRs** | [810](https://github.com/cheaper-inference/OmniRoute/issues) |
| 💻 **Languages** | TypeScript 93% · JavaScript 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `a2a` `ai-agents` `ai-gateway` `anthropic` `claude` `claude-code` `cline` `codex` `copilot` `cursor` `deepseek` `free-ai` `gemini` `llm-gateway` `mcp` `openai` `openai-proxy` `qwen` `token-saver` `kimi` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v3.8.54](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.54) — 2026-11-17 |
| 🌿 **Default branch** | `release/v3.8.55` |
| 💾 **Size** | 3699.1 MB |
| 🌐 **Website** | https://omniroute.online |

## 📦 Recent releases

### [v3.8.54](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.54)
<sub>2026-11-17 · 4d ago</sub>

> **OmniRoute v3.8.54**
> - **Providers:** official "Sign in with ChatGPT" provider (`chatgpt`, PKCE + live model discovery); MiniMax Code (managed gateway + dashboard device-code sign-in); RenderHour (images, video, speech); MegaBrain (dual auth); EmpirioLabs, ParalonCloud, deAPI, Replicate chat, Cerebrium, Hetzner Inference and Grokified; native `opencode-server` executor; Microsoft 365 Copilot work/school sign-in; GitHub Copilot embeddings; Gemini Lyria 3 music models; custom JSON API provider nodes (request template + response path).
> - **Routing and combos:** endpoint-specific combo routes (chat, search/fetch, embeddings, rerank, images, video, music, OCR, audio) with capability-aware search/fetch combos; new `jev` and `expiry-first` strategies; preferred and reserve accounts for Auto combos; opt-in preferred-account response-start failover; opt-in deadline-failure sub-budget that ends a combo with a clean 504.
> - **Search:** Keenable web search and fetch provider (keyless by default) and `codex-search` through connected Codex accounts.
> - **API keys and usage:** `/v1/me/status` reports today's/this week's usage and every per-key limit; `/v1/me/sessions` self-service session listing; rolling 5-hour USD budget per key; reusable key policy templates; `POST /api/keys/import`; usage attributed to coding-agent sessions and projects; provider-reported cache-read and 5-minute/1-hour cache-write tiers carried through analytics.
> - **Agentic pipelines and streaming:** repeated-tool-round and consecutive-failure detection across native protocols; opt-in context compaction with per-model budgets; `STREAM_READINESS_TIMEOUT` now says which failure shape occurred; large request bodies to `api.anthropic.com` are gzip-compressed like Claude Code.
> …

### [v3.8.53](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.53)
<sub>2026-11-06 · 16d ago</sub>

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
| 2026-11-21 | [Merge pull request #20961 from cheaper-inference/fix/restore-preferre…](https://github.com/cheaper-inference/OmniRoute/commit/5ffa68e835442a12ed1204a2eebf4076c298aecb) | diegosouzapw |
| 2026-11-21 | [Merge pull request #20370 from maxmad64bis/fix/plugin-model-row-fidelity](https://github.com/cheaper-inference/OmniRoute/commit/65ff1f94940f82214eab6c1b129579df102420b7) | diegosouzapw |
| 2026-11-21 | [Merge pull request #20958 from cheaper-inference/fix/merge-train-h-20…](https://github.com/cheaper-inference/OmniRoute/commit/5b6c0af52deb06d6f278adad542f988f58afc9e4) | diegosouzapw |
| 2026-11-21 | [Merge branch 'release/v3.8.55' into fix/plugin-model-row-fidelity](https://github.com/cheaper-inference/OmniRoute/commit/3ab4719c0769040016b50e1f8a419eb192508d64) | diegosouzapw |
| 2026-11-21 | [Merge pull request #20947 from cheaper-inference/fix/merge-train-g-20…](https://github.com/cheaper-inference/OmniRoute/commit/4265bb2ad5477450a07d3a43ea33a62c6c874878) | diegosouzapw |
| 2026-11-21 | [chore(changelog): name the fragment after #20961](https://github.com/cheaper-inference/OmniRoute/commit/7b7b61c6e771a17a35bdc829dbaa624404dadd76) | diegosouzapw |
| 2026-11-21 | [Merge branch 'release/v3.8.55' into fix/restore-preferred-failover-wi…](https://github.com/cheaper-inference/OmniRoute/commit/a86811d79e3ebb90f41e707dc04c44815b680a8c) | diegosouzapw |
| 2026-11-21 | [Merge pull request #20108 from b84330808/fix/usage-guard-once-per-req…](https://github.com/cheaper-inference/OmniRoute/commit/934d6afee6eb3b260a91fbe5dec7d152e58bdabb) | diegosouzapw |
| 2026-11-21 | [fix(sse): restore the preferred-account failover wiring in chat.ts](https://github.com/cheaper-inference/OmniRoute/commit/7477ae6c6bad26a983773392b371dd8791f46149) | diegosouzapw |
| 2026-11-21 | [Merge pull request #19735 from serenity-X/pr/perf/or9r-b-call-log-ove…](https://github.com/cheaper-inference/OmniRoute/commit/eaf57c1cc11aaea9b6cee6de04308fdfc9d2fffb) | diegosouzapw |

[See all commits ↗](https://github.com/cheaper-inference/OmniRoute/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cheaper-inference/OmniRoute.git
```
