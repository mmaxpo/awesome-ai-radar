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
| ⭐ **Stars** | 63.8k |
| 🍴 **Forks** | 13.5k |
| 🐞 **Open issues + PRs** | [5.5k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 82% · TypeScript 10% · Rust 6% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.110.3](https://github.com/BerriAI/litellm/releases/tag/v1.110.3) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3157.1 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.110.3](https://github.com/BerriAI/litellm/releases/tag/v1.110.3)
<sub>2026-11-24 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.110.3
> …

### [v1.109.4](https://github.com/BerriAI/litellm/releases/tag/v1.109.4)
<sub>2026-11-24 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.109.4
> …

### [v1.108.16](https://github.com/BerriAI/litellm/releases/tag/v1.108.16)
<sub>2026-11-23 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.108.16
> …

### [v1.108.15](https://github.com/BerriAI/litellm/releases/tag/v1.108.15) — 1.108.15 (LTS)
<sub>2026-11-21 · 2d ago</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.112.0-dev.2](https://github.com/BerriAI/litellm/releases/tag/v1.112.0-dev.2) _(pre-release)_
<sub>2026-11-21 · 2d ago</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.112.0-dev.2
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [feat(proxy): skip blocked deployments in background health checks (#5…](https://github.com/BerriAI/litellm/commit/273cc395aeb773d28986579b86a73a34d7180edc) | AaronHowell |
| 2026-11-24 | [fix(scim): stop SCIM user writes from overwriting teams a concurrent …](https://github.com/BerriAI/litellm/commit/eedbdcc0f967009128f4fb23f124984d8c06bf8a) | jesus-berri |
| 2026-11-24 | [fix(openai): drop or refuse an o-series reasoning_effort level the mo…](https://github.com/BerriAI/litellm/commit/9a384a563a8600b65bda905c25c7c017c63e652a) | quietjules |
| 2026-11-24 | [chore(types): type optional_params and litellm_params as dict[str, ob…](https://github.com/BerriAI/litellm/commit/de342db9b65cf7984e0786e6c9926edc4d7974ae) | mateo-berri |
| 2026-11-24 | [fix(batches): keep the endpoint a batch was created for on retrieve, …](https://github.com/BerriAI/litellm/commit/85ba26ff5f0a566026c5cd172341c6c64322e16e) | paveln83 |
| 2026-11-24 | [fix(guardrails): scan refusal text in output guardrails on chat and r…](https://github.com/BerriAI/litellm/commit/25b010e8e1c94bff3db85e2bbc11a551ba73ff29) | quietjules |
| 2026-11-24 | [fix(realtime): enforce TPM limits during realtime sessions (#53689)](https://github.com/BerriAI/litellm/commit/440572c451c7d25d5233814eb0c40e01e221fd16) | owen-hj |
| 2026-11-24 | [fix(vertex_ai): answer 400 for gemini embedding video_metadata that s…](https://github.com/BerriAI/litellm/commit/731dce9083cb6f0e8c8f7fafa5f161f5dcb09510) | linhqm |
| 2026-11-24 | [refactor(types): replace Unknown with proven types in 86 files (#53803)](https://github.com/BerriAI/litellm/commit/957433607ab8475d65e7bebd0175646806350483) | mateo-berri |
| 2026-11-24 | [fix(bedrock): keep shared $defs in Claude tool schemas and bound inli…](https://github.com/BerriAI/litellm/commit/b484c877e1f232240ca2576c5e9e14c1bcedb483) | paveln83 |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
