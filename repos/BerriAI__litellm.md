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
| ⭐ **Stars** | 63.6k |
| 🍴 **Forks** | 13.4k |
| 🐞 **Open issues + PRs** | [5.3k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 83% · TypeScript 10% · Rust 6% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.106.12](https://github.com/BerriAI/litellm/releases/tag/v1.106.12) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3055.2 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.106.12](https://github.com/BerriAI/litellm/releases/tag/v1.106.12)
<sub>2026-11-20 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.106.12
> …

### [v1.111.0-rc.3](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-rc.3) _(pre-release)_
<sub>2026-11-20 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.111.0-rc.3
> …

### [v1.109.3](https://github.com/BerriAI/litellm/releases/tag/v1.109.3)
<sub>2026-11-20 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.109.3
> …

### [v1.108.13](https://github.com/BerriAI/litellm/releases/tag/v1.108.13) — 1.108.13 (LTS)
<sub>2026-11-20 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.110.2](https://github.com/BerriAI/litellm/releases/tag/v1.110.2)
<sub>2026-11-20 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.110.2
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [fix(proxy): bill a forwarded-credential clone's final timed-out attem…](https://github.com/BerriAI/litellm/commit/dccecb97aed70c35be758e69fdebbbfdf9fb6e4d) | kerry-berri |
| 2026-11-20 | [fix(customer-portal): simplify budget navigation (#53066)](https://github.com/BerriAI/litellm/commit/f9b908a185fddcc8f88fb0bd5a78d004a38fad70) | tin-berri |
| 2026-11-20 | [feat(proxy): cache per-app customer authentication records (#53056)](https://github.com/BerriAI/litellm/commit/78ddb5e4de1928233e5438817732993adf0b31b6) | tin-berri |
| 2026-11-20 | [feat(customer-portal): share budget editors and app model access (#52…](https://github.com/BerriAI/litellm/commit/53adbf6f6af0fea9d1dc4e43829247988744cdb0) | tin-berri |
| 2026-11-20 | [feat(auth_cache): name each auth cache object with a typed key (#52831)](https://github.com/BerriAI/litellm/commit/b64f11c7889452d2979d546b9fdd997a2b631b56) | yujonglee-berri |
| 2026-11-20 | [refactor(proxy): move non-auth writers out of the auth cache (#51599)](https://github.com/BerriAI/litellm/commit/464420355bfd78b93cf431a7bb6c7c523073bcca) | yujonglee-berri |
| 2026-11-20 | [refactor(auth): name the keyspace in the JWT cache host calls (#52830)](https://github.com/BerriAI/litellm/commit/88a4161e40100f92cbc4a1a072eb42171cfe3a2f) | yujonglee-berri |
| 2026-11-20 | [refactor(redis): move per-request miss, settlement and shutdown-drain…](https://github.com/BerriAI/litellm/commit/4616174c4531f5c5c2b1c3eeb25acde36ea2b544) | yujonglee-berri |
| 2026-11-20 | [feat(budgets): support custom additional spend windows (#52976)](https://github.com/BerriAI/litellm/commit/b608fa878fbf741199afd2445f602f08f6266173) | tin-berri |
| 2026-11-20 | [chore: drop narration comments added in the last day (#53053)](https://github.com/BerriAI/litellm/commit/1ff622c3cdc7b9583edbe6f86204719ba0459908) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
