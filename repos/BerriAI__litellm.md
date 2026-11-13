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
| 🍴 **Forks** | 13.3k |
| 🐞 **Open issues + PRs** | [5.2k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 84% · TypeScript 10% · Rust 4% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.108.7](https://github.com/BerriAI/litellm/releases/tag/v1.108.7) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2892.8 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.111.0-dev.1](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.1) _(pre-release)_
<sub>2026-11-13 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.108.7](https://github.com/BerriAI/litellm/releases/tag/v1.108.7) — 1.108.7 (LTS)
<sub>2026-11-12 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
> …

### [v1.109.1](https://github.com/BerriAI/litellm/releases/tag/v1.109.1)
<sub>2026-11-12 · yesterday</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.110.0-rc.2](https://github.com/BerriAI/litellm/releases/tag/v1.110.0-rc.2) _(pre-release)_
<sub>2026-11-12 · yesterday</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.106.9](https://github.com/BerriAI/litellm/releases/tag/v1.106.9)
<sub>2026-11-12 · yesterday</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [fix(cost-map): mark together_ai/elorian-labs/glimpse-1.0 as supportin…](https://github.com/BerriAI/litellm/commit/6a1f81b9f8bd365718e781c50141fd3164721dbb) | devin-ai-integration[bot] |
| 2026-11-13 | [fix(proxy): preserve team aliases in Responses WebSockets (#51380)](https://github.com/BerriAI/litellm/commit/6abacd329b70dc668f69c705eb7118fbd639cd96) | brianhong-dev |
| 2026-11-13 | [fix(deps): bump soupsieve past GHSA-4j63-6c4x-wfg4 and GHSA-mmhr-3c5m…](https://github.com/BerriAI/litellm/commit/76794359cc2d8e4bf0b90cd550b4a94b16f72a59) | devin-ai-integration[bot] |
| 2026-11-13 | [fix(databricks): record the November 19 retirement and successor for …](https://github.com/BerriAI/litellm/commit/dc65705eb3d79478d03b5c1fadd6d11be3052b9d) | devin-ai-integration[bot] |
| 2026-11-13 | [fix(interactions): bind Deep Research agents and record their costs (…](https://github.com/BerriAI/litellm/commit/563dfd50757bb5332fe42c69d8518a6511c67ad7) | joshua-berri |
| 2026-11-13 | [fix(interactions): route Vertex lifecycle calls through the selected …](https://github.com/BerriAI/litellm/commit/ac5fd9e0d048e2f86a20d5a7b4ad422f379eff5b) | joshua-berri |
| 2026-11-13 | [fix(router): keep pinned deployment ids to the caller's access groups…](https://github.com/BerriAI/litellm/commit/c5843a812490a6de6834c2a39a429d77846175b1) | joshua-berri |
| 2026-11-13 | [fix(proxy): import soundfile lazily in the transcribe logging handler…](https://github.com/BerriAI/litellm/commit/257418cbd8cb45ad63f8e39a167a8fb42f5ced60) | joshua-berri |
| 2026-11-13 | [fix(utils): register ollama deployment prices from the built-in catal…](https://github.com/BerriAI/litellm/commit/4dad0bc513b75029e2a274143536bf50a7e56a4d) | devin-ai-integration[bot] |
| 2026-11-13 | [fix(openai): record the successor for the gpt-4o-mini audio and realt…](https://github.com/BerriAI/litellm/commit/32cb45a3d8875321efd8adab9ddccb5ff41d8d9a) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
