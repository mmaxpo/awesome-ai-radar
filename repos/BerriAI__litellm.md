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
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.106.10](https://github.com/BerriAI/litellm/releases/tag/v1.106.10) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2916.2 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.106.10](https://github.com/BerriAI/litellm/releases/tag/v1.106.10)
<sub>2026-11-14 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
>   ghcr.io/berriai/litellm:v1.106.10
> ```
> …

### [v1.108.8](https://github.com/BerriAI/litellm/releases/tag/v1.108.8) — 1.108.8 (LTS)
<sub>2026-11-13 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
> …

### [v1.111.0-dev.2](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.2) _(pre-release)_
<sub>2026-11-13 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.111.0-dev.1](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.1) _(pre-release)_
<sub>2026-11-13 · yesterday</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.108.7](https://github.com/BerriAI/litellm/releases/tag/v1.108.7) — 1.108.7 (LTS)
<sub>2026-11-12 · yesterday</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [feat(custom_llm): let custom providers serve native generateContent (…](https://github.com/BerriAI/litellm/commit/d81c55f4cc86d0303dd89ebb7dba0a745ce425b4) | mika-lt |
| 2026-11-14 | [fix(azure): send no api-version on Foundry project /openai/v1 Respons…](https://github.com/BerriAI/litellm/commit/6fc368a15c7a54f63d9265f6f4d3d91333b641c3) | tavren27 |
| 2026-11-14 | [fix(responses): send cache_control as a prompt_cache_breakpoint on th…](https://github.com/BerriAI/litellm/commit/3ad164382b1c4bf72c37fda0b2468a62168b365b) | paveln83 |
| 2026-11-14 | [fix(proxy): retrieve and delete a managed file when the request also …](https://github.com/BerriAI/litellm/commit/7d4c0ab91a8437d84b9f33383f094462a4b69f09) | paveln83 |
| 2026-11-14 | [fix(responses): accept a string or tuple allowed_openai_params on Res…](https://github.com/BerriAI/litellm/commit/4e29aea11c8eb5fadd96c78de2bd9d10b0381727) | tavren27 |
| 2026-11-14 | [fix(cohere): honor COHERE_API_BASE for embeddings (#50249)](https://github.com/BerriAI/litellm/commit/ad24ca9f3150eafda6da55b62e814aec02775063) | zhengqiuyang |
| 2026-11-14 | [refactor: clear fresh debt in customer hierarchy and v2 callback modu…](https://github.com/BerriAI/litellm/commit/1a8ed2723753db46d1adb64690ce337ad89508ca) | mateo-berri |
| 2026-11-14 | [fix(proxy): honor cancel_on_disconnect on the rerank endpoints (#51252)](https://github.com/BerriAI/litellm/commit/3988ce286501b8d584218e4f5fe8d329a0f5d9b1) | jesus-berri |
| 2026-11-14 | [feat(mistral): add native upstream token counting support (#50652) (#…](https://github.com/BerriAI/litellm/commit/35b9df1f4040ba17af06b936cb65026fb1f90ff6) | yogeshwaran10 |
| 2026-11-14 | [fix(vertex_ai): reuse one Google token across RAG Engine searches and…](https://github.com/BerriAI/litellm/commit/9ba216d521cb992fab16209315f2e1eb69cf6077) | quietjules |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
