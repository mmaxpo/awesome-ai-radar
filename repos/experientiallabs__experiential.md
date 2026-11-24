# experientiallabs/experiential

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/experientiallabs/experiential)

> Experiential is the open source, zero markup gateway for BYOK, self-hosted and 1000+ marketplace models. It learns from your traffic to cut costs, recommend better models, and train a specialized model you own.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Gateway and router for agent workflows |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 18.8k |
| 🍴 **Forks** | 325 |
| 🐞 **Open issues + PRs** | [186](https://github.com/experientiallabs/experiential/issues) |
| 💻 **Languages** | Python 87% · Rust 12% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-06-24 |
| 📦 **Latest release** | [v0.7.261](https://github.com/experientiallabs/experiential/releases/tag/v0.7.261) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 116.3 MB |
| 🌐 **Website** | https://experientiallabs.ai |

## 📦 Recent releases

### [preview-input-outcomes-598b261b3b](https://github.com/experientiallabs/experiential/releases/tag/preview-input-outcomes-598b261b3b) — Input outcome test build (598b261b3b) _(pre-release)_
<sub>2026-11-21 · 3d ago</sub>

> Test build for #1432 at `598b261b3b6a2c2a8a74f89170394646d69b63e7`.
> The wheel contains that commit's source. Only the package metadata version was changed to `0.7.262rc1432` in the exported build tree so an installed test build is easy to identify. It uses the published `exp-gateway-native==0.3.205` wheel.
> This is an unmerged testing artifact, not a stable release or a PyPI publication. The attached manifest and SHA256SUMS identify its source and bytes. Runtime validation is still in progress.

### [v0.7.261](https://github.com/experientiallabs/experiential/releases/tag/v0.7.261) — Experiential 0.7.261
<sub>2026-11-21 · 3d ago</sub>

> Experiential 0.7.261 (exp-gateway-native 0.3.205).
> - /v1/images token answers now settle on their image-output subset (`output_tokens_details.image_tokens`) and their cache reads (`input_tokens_details.cached_tokens`), each clamped to its total and unknown without a breakdown. A GPT image lane with an image-output rate previously billed text output at the image rate (gpt-image-1.5: about 29% over passthrough on a live request).
> - route_images tests moved to route_images_tests.rs (file-length rule).
> - Six dated dependency-audit ignores (tornado via the capture extra, transformers via the sft extra) extended to 2026-11-28 while their upstream pins block the fix.
> `SNAPSHOT_SCHEMA_VERSION` stays 5; digest derivation is unchanged.
> Release PR: https://github.com/experientiallabs/experiential/pull/1431

### [v0.7.260](https://github.com/experientiallabs/experiential/releases/tag/v0.7.260)
<sub>2026-11-20 · 3d ago</sub>

> Experiential 0.7.260 (exp-gateway-native 0.3.204).
> - #1429: Claude plan rungs lead the system prompt with Claude Code's billing-header block unless it already does, so every harness (OpenCode, Pi, Hermes, Codex, Copilot, Cursor, Cline) can use an org's Claude plans; real Claude Code passes through unchanged and API-key and house rungs are untouched.
> - #1426: route a Gemini continuation to its signature's issuer; a repeatedly broken tool call answers 400 (native change, released here as 0.3.204).
> SNAPSHOT_SCHEMA_VERSION unchanged.

### [v0.7.258](https://github.com/experientiallabs/experiential/releases/tag/v0.7.258) — Experiential 0.7.258
<sub>2026-11-20 · 3d ago</sub>

> Experiential 0.7.258 (exp-gateway-native 0.3.203).
> - Reverts #1409 (request-linked input-check outcomes through accounting). The platform reverted its integration (platform#3177), so this release ships without that engine path. #1409's test-only fix stays.
> - #1424: redial a malformed Gemini function call with VALIDATED calling.
> - Carried from 0.7.257: image edits on GPT image (OpenAI, Azure) and xAI Grok Imagine rungs (#1422), and Gemini output blocks via OpenRouter filed as refusals (#1419).
> `SNAPSHOT_SCHEMA_VERSION` stays 5; digest derivation is unchanged.
> Release PR: https://github.com/experientiallabs/experiential/pull/1425

### [v0.7.257](https://github.com/experientiallabs/experiential/releases/tag/v0.7.257) — Experiential 0.7.257
<sub>2026-11-20 · 4d ago</sub>

> Experiential 0.7.257 (exp-gateway-native 0.3.202) adds image edits on GPT image models (OpenAI, Azure OpenAI Image API wire) and xAI Grok Imagine models through `POST /v1/images/edits`, with fail-closed billing:
> - GPT image edits are token-billed with a new image-input price leg: `image_input_nano_usd_per_million_tokens` on the price cards and `image_input_tokens` (the image subset of input) on usage. A token-priced edit rung needs that rate.
> - xAI edits are billed per image: `GatewayUnitPrices.input_rates` prices consumed source images, the `"edit"` variant prices returned images, and settled units carry `input_quantity_milli`.
> It also files a Gemini output block relayed by OpenRouter as a refusal (#1419).
> `SNAPSHOT_SCHEMA_VERSION` stays 5; the new fields are excluded from identity while unset.
> Changes: https://github.com/experientiallabs/experiential/pull/1422, https://github.com/experientiallabs/experiential/pull/1419, release https://github.com/experientiallabs/experiential/pull/1423

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [gateway: settle image answers on their image-output and cache-read su…](https://github.com/experientiallabs/experiential/commit/02fcce0d8410726f7af53ade5f8a66ed43ca966d) | SilenNaihin |
| 2026-11-20 | [release: 0.7.260 (native 0.3.204) (#1430)](https://github.com/experientiallabs/experiential/commit/d6206e2578853aa8556a76a05671c950589c79bb) | SilenNaihin |
| 2026-11-20 | [gateway: route a Gemini continuation to its signature's issuer; a rep…](https://github.com/experientiallabs/experiential/commit/b6aa56087c39f0062422f4b8a814516e8a93008d) | SilenNaihin |
| 2026-11-20 | [Claude plan rungs: lead the system prompt with Claude Code's billing-…](https://github.com/experientiallabs/experiential/commit/26e5c68490ee1e17649a24bbbd4c22a35b8299fc) | SilenNaihin |
| 2026-11-20 | [gateway: Gemini 4 Neon, Hydrogen and Carbon thinking levels (#1428)](https://github.com/experientiallabs/experiential/commit/786e84fd3bd4f8a4f111bd6b6843ddd6fe0ae64b) | SilenNaihin |
| 2026-11-20 | [release: 0.7.258 (native 0.3.203), reverting #1409's engine change (#…](https://github.com/experientiallabs/experiential/commit/67a0e57f82a7de4f464e1f164ebca0afc8d67101) | SilenNaihin |
| 2026-11-20 | [count_tokens: ignore Chat-only reasoning_effort, verbosity and servic…](https://github.com/experientiallabs/experiential/commit/dc80ed72609809d5dfdeaa00ecaae8ec46c2b2d7) | SilenNaihin |
| 2026-11-20 | [gateway: redial a malformed Gemini function call with VALIDATED calli…](https://github.com/experientiallabs/experiential/commit/7dcd533e1c3eb1fc0e681bdf884602f86be525c8) | SilenNaihin |
| 2026-11-20 | [release: 0.7.257 (native 0.3.202) (#1423)](https://github.com/experientiallabs/experiential/commit/ecf0a10c9e514121d29713e5f82cae6bc3655caa) | SilenNaihin |
| 2026-11-20 | [gateway: image edits on GPT image (OpenAI, Azure) and xAI Grok Imagin…](https://github.com/experientiallabs/experiential/commit/f752bcfaa0cfc90aae118a6dc4f903a468964511) | SilenNaihin |

[See all commits ↗](https://github.com/experientiallabs/experiential/commits)

## ⬇️ Get it

```bash
git clone https://github.com/experientiallabs/experiential.git
```
