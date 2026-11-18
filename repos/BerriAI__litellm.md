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
| ⭐ **Stars** | 63.5k |
| 🍴 **Forks** | 13.4k |
| 🐞 **Open issues + PRs** | [5.3k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 83% · TypeScript 10% · Rust 5% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.110.0](https://github.com/BerriAI/litellm/releases/tag/v1.110.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2982.6 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.111.0-rc.1](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-rc.1) _(pre-release)_
<sub>2026-11-18 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.111.0-rc.1
> …

### [v1.110.0](https://github.com/BerriAI/litellm/releases/tag/v1.110.0)
<sub>2026-11-18 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.110.0
> …

### [v1.108.11](https://github.com/BerriAI/litellm/releases/tag/v1.108.11) — 1.108.11 (LTS)
<sub>2026-11-17 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.108.10](https://github.com/BerriAI/litellm/releases/tag/v1.108.10) — 1.108.10 (LTS)
<sub>2026-11-16 · yesterday</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.111.0-dev.3](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.3) _(pre-release)_
<sub>2026-11-15 · 3d ago</sub>

> > [!WARNING]
> > **This release was only partly published. Use [v1.111.0-dev.4](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.4) instead.**
> > It is built from the same commit and fixes the publishing problems below.
> > [!IMPORTANT]
> > **Signing has moved to keyless cosign.** This is the first release signed with Sigstore keyless signing (GitHub OIDC) instead of the `cosign.pub` key.
> > `cosign verify --key ...` does not work for this release or later ones. Use the command below. Earlier releases still verify with the key.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [feat(providers): add Sarvam Token Factory v2 models (#49792)](https://github.com/BerriAI/litellm/commit/c030ffb6b9c7a1b49072dceca1c2224cdfc21bcc) | vikashmaddi-sarvam |
| 2026-11-18 | [fix(proxy): resolve a team wildcard deployment for a wildcard key on …](https://github.com/BerriAI/litellm/commit/da8c02b9d5ac2956537ff3d6c1a84d415c51cb49) | tavren27 |
| 2026-11-18 | [refactor: clean up fresh tech debt from 2026-11-18 (#52491)](https://github.com/BerriAI/litellm/commit/90991cbd6302eeff5a2f81fbcecee87a52129758) | devin-ai-integration[bot] |
| 2026-11-18 | [chore(cost-map): add together_ai/Qwen/Qwen4-Max from the Together mod…](https://github.com/BerriAI/litellm/commit/910100c8b59e26d6905b350a706243847c6df037) | devin-ai-integration[bot] |
| 2026-11-18 | [docs(review): require the breaking-change marker only for evidenced b…](https://github.com/BerriAI/litellm/commit/4916d5636a18f3494e83866545d21a349b0556d4) | mateo-berri |
| 2026-11-18 | [test(auth): leave two Prisma connections for concurrent JWT registrat…](https://github.com/BerriAI/litellm/commit/907f91a4b65b204778097995ee810444fe02b1a1) | devin-ai-integration[bot] |
| 2026-11-18 | [feat(customer-portal): reuse budget groups for organizations (#52411)](https://github.com/BerriAI/litellm/commit/ee133621323bebf27e72695c0b9822d4e8343def) | tin-berri |
| 2026-11-18 | [fix(responses): preserve single-object input through the completion b…](https://github.com/BerriAI/litellm/commit/436f6d57a46cb289af058a6780b2b34e79f781d1) | devin-ai-integration[bot] |
| 2026-11-18 | [test(cost): add gemini-3.1-pro-preview flex tier cost tracking case (…](https://github.com/BerriAI/litellm/commit/214bbbcb24d85e009abe57d989b5a98e2107c1ad) | devin-ai-integration[bot] |
| 2026-11-18 | [test(management): size team delete lock probes for the Prisma pool sp…](https://github.com/BerriAI/litellm/commit/22ef72681fd8eca770d492fa743ffa60d18e2ff0) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
