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
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.108.19](https://github.com/BerriAI/litellm/releases/tag/v1.108.19) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3197.3 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.108.19](https://github.com/BerriAI/litellm/releases/tag/v1.108.19) — 1.108.19 (LTS)
<sub>2026-11-26 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.113.0-dev.1](https://github.com/BerriAI/litellm/releases/tag/v1.113.0-dev.1) _(pre-release)_
<sub>2026-11-26 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.113.0-dev.1
> …

### [v1.108.18](https://github.com/BerriAI/litellm/releases/tag/v1.108.18) — 1.108.18 (LTS)
<sub>2026-11-26 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.109.5](https://github.com/BerriAI/litellm/releases/tag/v1.109.5)
<sub>2026-11-25 · 2d ago</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.109.5
> …

### [v1.110.4](https://github.com/BerriAI/litellm/releases/tag/v1.110.4)
<sub>2026-11-25 · 2d ago</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.110.4
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [perf(mcp): skip unchanged scheduled catalog rebuilds (#54514)](https://github.com/BerriAI/litellm/commit/f7113621311aed10b6245b344b5143a0382d0c3b) | mrinal-berri |
| 2026-11-27 | [feat(auth-store): read the user a sign-in resolves to without linking…](https://github.com/BerriAI/litellm/commit/4f4ab97bebbdc2ecf06ba012e2aedd64565f69e5) | yujonglee-berri |
| 2026-11-27 | [refactor(gateway): move prompt_estimate out of host, since it answers…](https://github.com/BerriAI/litellm/commit/920df7b4d37987ec16d9d913d9ba93d3541c84a8) | yujonglee-berri |
| 2026-11-27 | [refactor(gateway): prepare the auth host to read rows beside the key …](https://github.com/BerriAI/litellm/commit/ef7ba56688808e4f9c3e6a7f080729ab5cbfb184) | yujonglee-berri |
| 2026-11-27 | [fix(auth): read a JWT team list claim sent as text as one team (#54841)](https://github.com/BerriAI/litellm/commit/de1b77b2072471b739d9689324a05849307adebf) | yujonglee-berri |
| 2026-11-27 | [feat(rust): insert a team for team_id_upsert in auth-store (#54828)](https://github.com/BerriAI/litellm/commit/39f7f6a2d9d58327b15699f5d84663ea970f0948) | yujonglee-berri |
| 2026-11-27 | [feat(rust): port the team_id_upsert team insert to repositories (#54846)](https://github.com/BerriAI/litellm/commit/ba90a4ab5eb3fb2444eea75d23edb78daa79f497) | yujonglee-berri |
| 2026-11-27 | [feat(rust): add and remove a team member in auth-store (#54825)](https://github.com/BerriAI/litellm/commit/ed1c23bbbcb2c236f6b07673428dcfa98c6bdd98) | yujonglee-berri |
| 2026-11-27 | [feat(rust): port the team member removal and the default team join to…](https://github.com/BerriAI/litellm/commit/b9a8575df91318331cd99a5bd36302644206c9df) | yujonglee-berri |
| 2026-11-27 | [feat(rust): write a user's sign-in insert, email backfill and role in…](https://github.com/BerriAI/litellm/commit/aa65fa5deb2df488d8ab7b7563e50bdf04d879fd) | yujonglee-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
