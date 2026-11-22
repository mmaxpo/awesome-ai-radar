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
| ⭐ **Stars** | 63.7k |
| 🍴 **Forks** | 13.5k |
| 🐞 **Open issues + PRs** | [5.4k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 82% · TypeScript 10% · Rust 6% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.108.15](https://github.com/BerriAI/litellm/releases/tag/v1.108.15) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3104.0 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.108.15](https://github.com/BerriAI/litellm/releases/tag/v1.108.15) — 1.108.15 (LTS)
<sub>2026-11-21 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.112.0-dev.2](https://github.com/BerriAI/litellm/releases/tag/v1.112.0-dev.2) _(pre-release)_
<sub>2026-11-21 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.112.0-dev.2
> …

### [v1.108.14](https://github.com/BerriAI/litellm/releases/tag/v1.108.14) — 1.108.14 (LTS)
<sub>2026-11-20 · yesterday</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.106.12](https://github.com/BerriAI/litellm/releases/tag/v1.106.12)
<sub>2026-11-20 · 2d ago</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.106.12
> …

### [v1.111.0-rc.3](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-rc.3) _(pre-release)_
<sub>2026-11-20 · 2d ago</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.111.0-rc.3
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [feat(proxy)!: carry unused budget into the next period with a cap (#5…](https://github.com/BerriAI/litellm/commit/90dce4b93bd2b090621a6b9083311294d3358bc6) | shivamrawat1 |
| 2026-11-22 | [refactor: drop slop comments and string getattr from fresh code (#53552)](https://github.com/BerriAI/litellm/commit/6df435f81c1703f1c6c61a2b4f4f1aaf54a31c0c) | devin-ai-integration[bot] |
| 2026-11-22 | [feat(realtime): bill translation WebRTC calls by the time the call ra…](https://github.com/BerriAI/litellm/commit/aa166f1b9abff926711255be8e85b85d18c88f5a) | moe-berri |
| 2026-11-22 | [fix(models): declare GPT-Live and translation endpoints (#53277)](https://github.com/BerriAI/litellm/commit/18fe30f31d0b94683efa3b494e8da920f6b02f47) | moe-berri |
| 2026-11-22 | [test(e2e): expect the Models refresh action in the page header above …](https://github.com/BerriAI/litellm/commit/39d797be54d828926218298a6741db9918e055a7) | kerry-berri |
| 2026-11-22 | [fix(models): accept the Live sessions route in the Rust catalog (#53279)](https://github.com/BerriAI/litellm/commit/935177e7baf0bf240e2f41d069b682c24aa62a82) | moe-berri |
| 2026-11-22 | [test(e2e): match the renamed Virtual Key and Admin labels in UI specs…](https://github.com/BerriAI/litellm/commit/20a9c0c6a558240519c19675b7c5dbff38cd5bb7) | kerry-berri |
| 2026-11-22 | [test(e2e): expect the Admin Settings heading on the admin page (#53545)](https://github.com/BerriAI/litellm/commit/2e2bd37853238a50cad8c48efe38bf481f61e1c3) | kerry-berri |
| 2026-11-22 | [test(e2e): match the Skills Hub search placeholder (#53544)](https://github.com/BerriAI/litellm/commit/2abb952dd0043759febd2374f8b870cab98880a0) | kerry-berri |
| 2026-11-22 | [test(e2e): expect only key-creating teams in the Create Key team drop…](https://github.com/BerriAI/litellm/commit/3938707deb5259b9d3860b02c0bcdfa0e28a563f) | kerry-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
