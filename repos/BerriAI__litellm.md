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
| ⭐ **Stars** | 64.0k |
| 🍴 **Forks** | 13.6k |
| 🐞 **Open issues + PRs** | [5.6k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 82% · TypeScript 10% · Rust 7% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.109.5](https://github.com/BerriAI/litellm/releases/tag/v1.109.5) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3185.3 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.109.5](https://github.com/BerriAI/litellm/releases/tag/v1.109.5)
<sub>2026-11-25 · yesterday</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.109.5
> …

### [v1.110.4](https://github.com/BerriAI/litellm/releases/tag/v1.110.4)
<sub>2026-11-25 · yesterday</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.110.4
> …

### [v1.111.0](https://github.com/BerriAI/litellm/releases/tag/v1.111.0)
<sub>2026-11-25 · yesterday</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.111.0
> …

### [v1.108.17](https://github.com/BerriAI/litellm/releases/tag/v1.108.17) — 1.108.17 (LTS)
<sub>2026-11-24 · yesterday</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.112.0-rc.1](https://github.com/BerriAI/litellm/releases/tag/v1.112.0-rc.1) _(pre-release)_
<sub>2026-11-24 · yesterday</sub>

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
| 2026-11-26 | [Type the kwargs reads in the Prometheus logger (#54711)](https://github.com/BerriAI/litellm/commit/52f22bbc17f53a84736fc19b4d63852988f55d3f) | mateo-berri |
| 2026-11-26 | [fix(cost-map): give the lowercase together_ai Inkling row the same 20…](https://github.com/BerriAI/litellm/commit/82af66e3403be291b71b8a58fa790f1754443992) | kerry-berri |
| 2026-11-26 | [test(logging): make the SDK key identity test read only its own call'…](https://github.com/BerriAI/litellm/commit/1d4edf17ea0c4f2ee5a156f8f54fd77479e9e211) | mateo-berri |
| 2026-11-26 | [refactor(gateway-auth-core): move the key model access check into aut…](https://github.com/BerriAI/litellm/commit/68669b0dd938a7c29a9d028d072c7a51e1ff0184) | yujonglee-berri |
| 2026-11-26 | [refactor(types): type the kwargs views of embedding, transcription an…](https://github.com/BerriAI/litellm/commit/6470964faa935ea849538e6d36b9da44c7ff902f) | mateo-berri |
| 2026-11-26 | [feat(auth-store): read a user in the shape the auth cache holds it (#…](https://github.com/BerriAI/litellm/commit/fcb456ba3b6bed163c8ec44d7b13058989401577) | yujonglee-berri |
| 2026-11-26 | [feat(auth-store): read an organization in the shape the auth cache ho…](https://github.com/BerriAI/litellm/commit/d8691dba03413ea307a7bd950176deedee2ce8f2) | yujonglee-berri |
| 2026-11-26 | [fix(auth-cache): take only the key roles and regions UserAPIKeyAuth t…](https://github.com/BerriAI/litellm/commit/22eb9581cbf8678bd463b4b35f1206d425f05355) | yujonglee-berri |
| 2026-11-26 | [feat(auth-store): read an end user in the shape the auth cache holds …](https://github.com/BerriAI/litellm/commit/a44f977d2bf0d4acee111f848a5911f627ec629f) | yujonglee-berri |
| 2026-11-26 | [refactor(repositories): read an object permission row as one type (#5…](https://github.com/BerriAI/litellm/commit/799c38859a06c57c71a9c237ef70224a31a88921) | yujonglee-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
