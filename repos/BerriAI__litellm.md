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
| ⭐ **Stars** | 63.9k |
| 🍴 **Forks** | 13.6k |
| 🐞 **Open issues + PRs** | [5.5k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 82% · TypeScript 10% · Rust 7% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.109.5](https://github.com/BerriAI/litellm/releases/tag/v1.109.5) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3173.8 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.109.5](https://github.com/BerriAI/litellm/releases/tag/v1.109.5)
<sub>2026-11-25 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.109.5
> …

### [v1.110.4](https://github.com/BerriAI/litellm/releases/tag/v1.110.4)
<sub>2026-11-25 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.110.4
> …

### [v1.111.0](https://github.com/BerriAI/litellm/releases/tag/v1.111.0)
<sub>2026-11-25 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.111.0
> …

### [v1.108.17](https://github.com/BerriAI/litellm/releases/tag/v1.108.17) — 1.108.17 (LTS)
<sub>2026-11-24 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.112.0-rc.1](https://github.com/BerriAI/litellm/releases/tag/v1.112.0-rc.1) _(pre-release)_
<sub>2026-11-24 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.112.0-rc.1
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [fix(responses): reject an unresolvable previous_response_id on the ch…](https://github.com/BerriAI/litellm/commit/d941699343bdc61682b59cc9346b9e1fd8341194) | edvinsq |
| 2026-11-25 | [test(budgets): give the held-back stream cancel test a fallback so th…](https://github.com/BerriAI/litellm/commit/519d84423e27aa0520b2948c65ca444cbadc313f) | kerry-berri |
| 2026-11-25 | [fix(guardrails): check one-object parts and tool turns on generateCon…](https://github.com/BerriAI/litellm/commit/bc4ca0b218ff6af1595ae105298f979d20062fd2) | zoveki |
| 2026-11-25 | [refactor(gateway-auth-core): keep the model access denial in error.rs…](https://github.com/BerriAI/litellm/commit/6f34f0cf25d58015a62a7b74ed557294ed57b923) | yujonglee-berri |
| 2026-11-25 | [fix(router): send /v1/messages message_start live during thinking whe…](https://github.com/BerriAI/litellm/commit/34dea88f048b7106df3e16d513c9a616953aee28) | ellisc42 |
| 2026-11-25 | [fix(llms): send later system messages as user turns for models declar…](https://github.com/BerriAI/litellm/commit/801976e7077c3fd85a92d2b457a4be7d96761635) | quietjules |
| 2026-11-25 | [test(responses-bridge): cover multi-turn GPT-6.2 prompt caching on Op…](https://github.com/BerriAI/litellm/commit/d91a02dfb3471e683078338102633403ceee74d3) | paveln83 |
| 2026-11-25 | [fix(guardrails): classify only the frames each read completes in Pres…](https://github.com/BerriAI/litellm/commit/2c4d2344660564b1e256acd6b8dc0c1c1620361c) | izzybn |
| 2026-11-25 | [fix(router): with pre-call checks on, retry a context window error on…](https://github.com/BerriAI/litellm/commit/9add785f1a9c13d8ae60980610868253c86cc0df) | martenj4 |
| 2026-11-25 | [fix(rust-config): apply require_key_mcp_access_defined from the store…](https://github.com/BerriAI/litellm/commit/df9d7606c3b01faf975e06d00138c5521bb77775) | kerry-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
