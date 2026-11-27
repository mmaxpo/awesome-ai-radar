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
| ⭐ **Stars** | 90.7k |
| 🍴 **Forks** | 14.1k |
| 🐞 **Open issues + PRs** | [967](https://github.com/cheaper-inference/OmniRoute/issues) |
| 💻 **Languages** | TypeScript 92% · JavaScript 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `a2a` `ai-agents` `ai-gateway` `anthropic` `claude` `claude-code` `cline` `codex` `copilot` `cursor` `deepseek` `free-ai` `gemini` `llm-gateway` `mcp` `openai` `openai-proxy` `qwen` `token-saver` `kimi` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v3.8.54](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.54) — 2026-11-17 |
| 🌿 **Default branch** | `release/v3.8.55` |
| 💾 **Size** | 3833.5 MB |
| 🌐 **Website** | https://omniroute.online |

## 📦 Recent releases

### [v3.8.54](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.54)
<sub>2026-11-17 · 10d ago</sub>

> **OmniRoute v3.8.54**
> - **Providers:** official "Sign in with ChatGPT" provider (`chatgpt`, PKCE + live model discovery); MiniMax Code (managed gateway + dashboard device-code sign-in); RenderHour (images, video, speech); MegaBrain (dual auth); EmpirioLabs, ParalonCloud, deAPI, Replicate chat, Cerebrium, Hetzner Inference and Grokified; native `opencode-server` executor; Microsoft 365 Copilot work/school sign-in; GitHub Copilot embeddings; Gemini Lyria 3 music models; custom JSON API provider nodes (request template + response path).
> - **Routing and combos:** endpoint-specific combo routes (chat, search/fetch, embeddings, rerank, images, video, music, OCR, audio) with capability-aware search/fetch combos; new `jev` and `expiry-first` strategies; preferred and reserve accounts for Auto combos; opt-in preferred-account response-start failover; opt-in deadline-failure sub-budget that ends a combo with a clean 504.
> - **Search:** Keenable web search and fetch provider (keyless by default) and `codex-search` through connected Codex accounts.
> - **API keys and usage:** `/v1/me/status` reports today's/this week's usage and every per-key limit; `/v1/me/sessions` self-service session listing; rolling 5-hour USD budget per key; reusable key policy templates; `POST /api/keys/import`; usage attributed to coding-agent sessions and projects; provider-reported cache-read and 5-minute/1-hour cache-write tiers carried through analytics.
> - **Agentic pipelines and streaming:** repeated-tool-round and consecutive-failure detection across native protocols; opt-in context compaction with per-model budgets; `STREAM_READINESS_TIMEOUT` now says which failure shape occurred; large request bodies to `api.anthropic.com` are gzip-compressed like Claude Code.
> …

### [v3.8.53](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.53)
<sub>2026-11-06 · 21d ago</sub>

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
| 2026-11-27 | [Merge PR #21360: chore(quality): resync catalog drift probes with the…](https://github.com/cheaper-inference/OmniRoute/commit/44812b66fdff9e420d92aee4645a61546fe89f43) | diegosouzapw |
| 2026-11-27 | [Merge PR #21347: fix(sse): route advertised Claude effort variants th…](https://github.com/cheaper-inference/OmniRoute/commit/c71f0065a7efe9230ec23b96a12253b050c4d7ad) | diegosouzapw |
| 2026-11-27 | [Merge PR #21162: fix(dashboard): contain provider model card actions …](https://github.com/cheaper-inference/OmniRoute/commit/248da3e8ad15ac08464e690d8a315722920c34ac) | diegosouzapw |
| 2026-11-27 | [Merge PR #21111: fix(mcp): preserve bounded full CCR retrieval (@Kiar…](https://github.com/cheaper-inference/OmniRoute/commit/9f3fcade6586dc73bccc6e33bbf8092a3ef933d8) | diegosouzapw |
| 2026-11-27 | [Merge PR #20976: fix(images): forward OpenAI generation complexity, m…](https://github.com/cheaper-inference/OmniRoute/commit/f1c51d2051393182df042da68f2d0155f1617c74) | diegosouzapw |
| 2026-11-27 | [Merge PR #21337: fix(docker,build): enforce the frozen lockfile in Do…](https://github.com/cheaper-inference/OmniRoute/commit/943e080319ac78c399eb6ee12f1532533ed3cf95) | diegosouzapw |
| 2026-11-27 | [Merge PR #21359: test(ui): give the combo searchable-selector cases t…](https://github.com/cheaper-inference/OmniRoute/commit/c245b61a29b5ee49b8a7e2687543ae2784153f07) | diegosouzapw |
| 2026-11-27 | [Merge PR #21313: test(combo): prove the handoff summary stays inside …](https://github.com/cheaper-inference/OmniRoute/commit/459a0154190312147057b829d2b7d8c6ecc17326) | diegosouzapw |
| 2026-11-27 | [Merge PR #21306: feat(models): refresh the AI Horde image catalog in …](https://github.com/cheaper-inference/OmniRoute/commit/62dc783388d328682f00a482af818666e3342c84) | diegosouzapw |
| 2026-11-27 | [Merge PR #21295: chore(quality): sync the merge-gates template with t…](https://github.com/cheaper-inference/OmniRoute/commit/d3f06ea668109f8ac1feadfcae25f6ff9b873b5f) | diegosouzapw |

[See all commits ↗](https://github.com/cheaper-inference/OmniRoute/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cheaper-inference/OmniRoute.git
```
