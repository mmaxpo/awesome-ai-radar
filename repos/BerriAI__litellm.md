# BerriAI/litellm

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/BerriAI/litellm)

> The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM]

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | One API / proxy for 100+ LLM providers |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 63.2k |
| 🍴 **Forks** | 13.2k |
| 🐞 **Open issues + PRs** | [5.2k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 84% · TypeScript 10% · Rust 4% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.109.1](https://github.com/BerriAI/litellm/releases/tag/v1.109.1) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2873.2 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.109.1](https://github.com/BerriAI/litellm/releases/tag/v1.109.1)
<sub>2026-11-12 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.110.0-rc.2](https://github.com/BerriAI/litellm/releases/tag/v1.110.0-rc.2) _(pre-release)_
<sub>2026-11-12 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.106.9](https://github.com/BerriAI/litellm/releases/tag/v1.106.9)
<sub>2026-11-12 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.108.6](https://github.com/BerriAI/litellm/releases/tag/v1.108.6)
<sub>2026-11-12 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.106.8](https://github.com/BerriAI/litellm/releases/tag/v1.106.8)
<sub>2026-11-11 · yesterday</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
>   ghcr.io/berriai/litellm:v1.106.8
> ```
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [feat(dynamic_rate_limiter_v3): steer flexible teams to a permitted al…](https://github.com/BerriAI/litellm/commit/52d1c4cd80162fbf03d7f92def0cb1631f1edfd4) | kerry-berri |
| 2026-11-12 | [ci: stop PR runs from thrashing the Actions cache and stop smoke comp…](https://github.com/BerriAI/litellm/commit/1677c2250e24697a904dd1750815f574af8040f4) | yuneng-berri |
| 2026-11-12 | [fix(gemini): add batch and priority image output token prices to gemi…](https://github.com/BerriAI/litellm/commit/db8ad3b13e7320bf835205cae58be5a58e0ff366) | devin-ai-integration[bot] |
| 2026-11-12 | [feat(rate-limit): team_model_limit_max_borrow_multiple caps how far a…](https://github.com/BerriAI/litellm/commit/ece1484bc7428da8f66683d4897c9c1d7d504e19) | kerry-berri |
| 2026-11-12 | [test(providers): expect Rust routing for idle Messages streams (#51364)](https://github.com/BerriAI/litellm/commit/3d389262a4fc5c07e487c50a8bacdf73e077b83b) | devin-ai-integration[bot] |
| 2026-11-12 | [fix(anthropic): close strict JSON schemas on the Messages to Response…](https://github.com/BerriAI/litellm/commit/4cd8f9174dda26c9af10832b8c9663dac4062ebf) | kenneth-berri |
| 2026-11-12 | [fix(fal_ai): give MiniMax H3 Max video endpoints their own resolution…](https://github.com/BerriAI/litellm/commit/7c7e02b06fa9fbf74d1e3c5064e5921e62aeb51a) | kerry-berri |
| 2026-11-12 | [feat(rate-limit): team_model_limit_borrows_idle_capacity_from_other_t…](https://github.com/BerriAI/litellm/commit/19ffe3a5f24594bb5c71a512e14ee8fad50d6c58) | kerry-berri |
| 2026-11-12 | [fix(alerts): stop detecting traffic drops (#51338)](https://github.com/BerriAI/litellm/commit/6a98d0926117478a4ab937f1bad46a120cd4832a) | moe-berri |
| 2026-11-12 | [ci: fail when the repo root grows past 15 entries (#51007)](https://github.com/BerriAI/litellm/commit/61944def17ec3a188d4ab2f730077a7949b812fc) | yassin-berriai |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
