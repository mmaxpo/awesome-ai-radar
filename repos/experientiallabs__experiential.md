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
| ⭐ **Stars** | 19.6k |
| 🍴 **Forks** | 333 |
| 🐞 **Open issues + PRs** | [191](https://github.com/experientiallabs/experiential/issues) |
| 💻 **Languages** | Python 86% · Rust 12% · TypeScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-26 (yesterday) |
| 📅 **Created** | 2026-06-24 |
| 📦 **Latest release** | [v0.7.263](https://github.com/experientiallabs/experiential/releases/tag/v0.7.263) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 115.3 MB |
| 🌐 **Website** | https://experientiallabs.ai |

## 📦 Recent releases

### [v0.7.263](https://github.com/experientiallabs/experiential/releases/tag/v0.7.263) — Experiential 0.7.263
<sub>2026-11-25 · yesterday</sub>

> Google Antigravity plan serving through Cloud Code Assist (#1440); native 0.3.207.

### [preview-input-outcomes-598b261b3b](https://github.com/experientiallabs/experiential/releases/tag/preview-input-outcomes-598b261b3b) — Input outcome test build (598b261b3b) _(pre-release)_
<sub>2026-11-21 · 6d ago</sub>

> Test build for #1432 at `598b261b3b6a2c2a8a74f89170394646d69b63e7`.
> The wheel contains that commit's source. Only the package metadata version was changed to `0.7.262rc1432` in the exported build tree so an installed test build is easy to identify. It uses the published `exp-gateway-native==0.3.205` wheel.
> This is an unmerged testing artifact, not a stable release or a PyPI publication. The attached manifest and SHA256SUMS identify its source and bytes. Runtime validation is still in progress.

### [v0.7.261](https://github.com/experientiallabs/experiential/releases/tag/v0.7.261) — Experiential 0.7.261
<sub>2026-11-21 · 6d ago</sub>

> Experiential 0.7.261 (exp-gateway-native 0.3.205).
> - /v1/images token answers now settle on their image-output subset (`output_tokens_details.image_tokens`) and their cache reads (`input_tokens_details.cached_tokens`), each clamped to its total and unknown without a breakdown. A GPT image lane with an image-output rate previously billed text output at the image rate (gpt-image-1.5: about 29% over passthrough on a live request).
> - route_images tests moved to route_images_tests.rs (file-length rule).
> - Six dated dependency-audit ignores (tornado via the capture extra, transformers via the sft extra) extended to 2026-11-28 while their upstream pins block the fix.
> `SNAPSHOT_SCHEMA_VERSION` stays 5; digest derivation is unchanged.
> Release PR: https://github.com/experientiallabs/experiential/pull/1431

### [v0.7.260](https://github.com/experientiallabs/experiential/releases/tag/v0.7.260)
<sub>2026-11-20 · 6d ago</sub>

> Experiential 0.7.260 (exp-gateway-native 0.3.204).
> - #1429: Claude plan rungs lead the system prompt with Claude Code's billing-header block unless it already does, so every harness (OpenCode, Pi, Hermes, Codex, Copilot, Cursor, Cline) can use an org's Claude plans; real Claude Code passes through unchanged and API-key and house rungs are untouched.
> - #1426: route a Gemini continuation to its signature's issuer; a repeatedly broken tool call answers 400 (native change, released here as 0.3.204).
> SNAPSHOT_SCHEMA_VERSION unchanged.

### [v0.7.258](https://github.com/experientiallabs/experiential/releases/tag/v0.7.258) — Experiential 0.7.258
<sub>2026-11-20 · 6d ago</sub>

> Experiential 0.7.258 (exp-gateway-native 0.3.203).
> - Reverts #1409 (request-linked input-check outcomes through accounting). The platform reverted its integration (platform#3177), so this release ships without that engine path. #1409's test-only fix stays.
> - #1424: redial a malformed Gemini function call with VALIDATED calling.
> - Carried from 0.7.257: image edits on GPT image (OpenAI, Azure) and xAI Grok Imagine rungs (#1422), and Gemini output blocks via OpenRouter filed as refusals (#1419).
> `SNAPSHOT_SCHEMA_VERSION` stays 5; digest derivation is unchanged.
> Release PR: https://github.com/experientiallabs/experiential/pull/1425

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [OpenRouter reported cost for passthrough billing; release 0.7.264 (na…](https://github.com/experientiallabs/experiential/commit/66b7b18ed23891ac14ecd9403ef261c3c9551653) | SilenNaihin |
| 2026-11-25 | [release: 0.7.263 (native 0.3.207) (#1442)](https://github.com/experientiallabs/experiential/commit/96469b1b405691cebb1c4fa2ca193cc0d7b4432c) | SilenNaihin |
| 2026-11-25 | [gateway: serve Gemini models on Google Antigravity plans through Clou…](https://github.com/experientiallabs/experiential/commit/123d9e6dda17acebaddfbf8b832cfb0c0f188dc1) | SilenNaihin |
| 2026-11-25 | [exp-code: read-only tools for the organization's Experiential data (#…](https://github.com/experientiallabs/experiential/commit/ca12a1093ec817436e154e08b4f180e5abdc52dc) | SilenNaihin |
| 2026-11-25 | [gateway: hold video job submit and poll to the public-only destinatio…](https://github.com/experientiallabs/experiential/commit/1efb21a5e4c0b038d0d25b5e70c5062a537d4408) | SilenNaihin |
| 2026-11-24 | [Honor vLLM sampling controls without priority scheduling (#1439)](https://github.com/experientiallabs/experiential/commit/3b07385de6d484b24a8764a98b34a91d3b99cddd) | kfallah |
| 2026-11-24 | [exp-code: Experiential identity in the terminal UI, prompt and help; …](https://github.com/experientiallabs/experiential/commit/af2551d0c4b7f78ab608fc4a59cd91fa73dc65ea) | SilenNaihin |
| 2026-11-21 | [gateway: settle image answers on their image-output and cache-read su…](https://github.com/experientiallabs/experiential/commit/02fcce0d8410726f7af53ade5f8a66ed43ca966d) | SilenNaihin |
| 2026-11-20 | [release: 0.7.260 (native 0.3.204) (#1430)](https://github.com/experientiallabs/experiential/commit/d6206e2578853aa8556a76a05671c950589c79bb) | SilenNaihin |
| 2026-11-20 | [gateway: route a Gemini continuation to its signature's issuer; a rep…](https://github.com/experientiallabs/experiential/commit/b6aa56087c39f0062422f4b8a814516e8a93008d) | SilenNaihin |

[See all commits ↗](https://github.com/experientiallabs/experiential/commits)

## ⬇️ Get it

```bash
git clone https://github.com/experientiallabs/experiential.git
```
