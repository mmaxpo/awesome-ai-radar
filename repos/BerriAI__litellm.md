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
| ⭐ **Stars** | 63.1k |
| 🍴 **Forks** | 13.2k |
| 🐞 **Open issues + PRs** | [5.1k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 84% · TypeScript 10% · Rust 4% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.106.8](https://github.com/BerriAI/litellm/releases/tag/v1.106.8) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2860.4 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.106.8](https://github.com/BerriAI/litellm/releases/tag/v1.106.8)
<sub>2026-11-11 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
>   ghcr.io/berriai/litellm:v1.106.8
> ```
> …

### [v1.110.0-rc.1](https://github.com/BerriAI/litellm/releases/tag/v1.110.0-rc.1) _(pre-release)_
<sub>2026-11-11 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.103.11](https://github.com/BerriAI/litellm/releases/tag/v1.103.11)
<sub>2026-11-10 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
>   ghcr.io/berriai/litellm:v1.103.11
> ```
> …

### [v1.104.9](https://github.com/BerriAI/litellm/releases/tag/v1.104.9)
<sub>2026-11-10 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
>   ghcr.io/berriai/litellm:v1.104.9
> ```
> …

### [v1.108.5](https://github.com/BerriAI/litellm/releases/tag/v1.108.5) — 1.108.5 (LTS)
<sub>2026-11-10 · today</sub>

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
| 2026-11-11 | [fix(router): preserve held tiers for OpenCode subagent results (#51176)](https://github.com/BerriAI/litellm/commit/0a4ccf95544127d7b1e9b9121ee0c41deec4f0c9) | joshua-berri |
| 2026-11-11 | [chore(cost-map): rolling registry PR, fal_ai rows, databricks gemini-…](https://github.com/BerriAI/litellm/commit/1d97931c84703453368852d786a33bda644524e7) | devin-ai-integration[bot] |
| 2026-11-11 | [docs(security): updated mailinglist and vdp in security.md (#51199)](https://github.com/BerriAI/litellm/commit/25b1de636985aaa483ccd679ce0963f5cc30ae46) | ojensen-berri |
| 2026-11-11 | [fix(vertex): drop floor-only retirement dates, veo 3.1 successor and …](https://github.com/BerriAI/litellm/commit/8b8ec4e3a64facae7af657ab06bc214dd5bf9060) | devin-ai-integration[bot] |
| 2026-11-11 | [fix(tls)!: exclude RSA key exchange and ChaCha20 from the outbound ci…](https://github.com/BerriAI/litellm/commit/eba880e108109fec9a9a131c6e26c71b9c2b5828) | yucheng-berri |
| 2026-11-11 | [fix(proxy): add tzdata to the proxy extra so a legacy TZ doesn't stop…](https://github.com/BerriAI/litellm/commit/3616014548d40020f508566620c5cd8745721f3c) | satwik-bankapur |
| 2026-11-11 | [fix(spend): keep free response reads and cancels off the creation spe…](https://github.com/BerriAI/litellm/commit/c2afb07f93b47e982ae57724bbf94100c1aefd4e) | devin-ai-integration[bot] |
| 2026-11-11 | [fix(gemini): batch and flex tier fields the -latest alias rows were m…](https://github.com/BerriAI/litellm/commit/606490a52dbafa822a24f943d0f8a14a1bc29940) | devin-ai-integration[bot] |
| 2026-11-11 | [test(spend): expect token billing for Vertex image edits (#51148)](https://github.com/BerriAI/litellm/commit/525df3f9a113d750e49e1ec865104c5c5d40bc67) | devin-ai-integration[bot] |
| 2026-11-11 | [test(providers): preserve unspecified Gemini image output modality (#…](https://github.com/BerriAI/litellm/commit/97f07af044c854d861347181c7a118f9dd78e285) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
