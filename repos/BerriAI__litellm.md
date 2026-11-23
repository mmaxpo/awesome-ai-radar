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
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.108.15](https://github.com/BerriAI/litellm/releases/tag/v1.108.15) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3119.2 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.108.15](https://github.com/BerriAI/litellm/releases/tag/v1.108.15) — 1.108.15 (LTS)
<sub>2026-11-21 · yesterday</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.112.0-dev.2](https://github.com/BerriAI/litellm/releases/tag/v1.112.0-dev.2) _(pre-release)_
<sub>2026-11-21 · yesterday</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.112.0-dev.2
> …

### [v1.108.14](https://github.com/BerriAI/litellm/releases/tag/v1.108.14) — 1.108.14 (LTS)
<sub>2026-11-20 · 2d ago</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.106.12](https://github.com/BerriAI/litellm/releases/tag/v1.106.12)
<sub>2026-11-20 · 3d ago</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.106.12
> …

### [v1.111.0-rc.3](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-rc.3) _(pre-release)_
<sub>2026-11-20 · 3d ago</sub>

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
| 2026-11-23 | [refactor(cost-map): fetch through a Source trait and RemoteSource (#5…](https://github.com/BerriAI/litellm/commit/3e27fc2a88d2545a706fb9cc1a85ea99e474f18c) | yujonglee-berri |
| 2026-11-23 | [fix(guardrails)!: mask PII in Presidio tool calls and refuse streams …](https://github.com/BerriAI/litellm/commit/fdf3bab02f77b5bb28e6b4f0a062f4557d71d8ef) | izzybn |
| 2026-11-23 | [fix(redaction): scrub authorization_token values by their key name (#…](https://github.com/BerriAI/litellm/commit/f409bfd8025f1da52cf7342e98175b14c0a025aa) | yujonglee-berri |
| 2026-11-23 | [refactor(tracing): drop the unused sink_layer and the log macro re-ex…](https://github.com/BerriAI/litellm/commit/f5343c14faa2336ea3a800abb45f5afad762a1e8) | yujonglee-berri |
| 2026-11-23 | [refactor(rust_bridge): send every Rust log line through one subscribe…](https://github.com/BerriAI/litellm/commit/baf0e74f56b1278ee42a751bcaf000a8c9a62a4a) | yujonglee-berri |
| 2026-11-23 | [fix(logging): print a Rust log line's fields in plain Python logs (#5…](https://github.com/BerriAI/litellm/commit/0ad8c0908b7042e9913fd467c60a1bb721961c66) | yujonglee-berri |
| 2026-11-23 | [fix(gateway): scrub secrets from the gateway's log lines (#53714)](https://github.com/BerriAI/litellm/commit/a4c9c56c981e7bb76832020e1ff32cc0d1b3df6f) | yujonglee-berri |
| 2026-11-23 | [refactor(rust_bridge): pick the Python logger for a Rust target in on…](https://github.com/BerriAI/litellm/commit/4cdb1842064d1fbe17a46b05ec6012b21361452f) | yujonglee-berri |
| 2026-11-23 | [refactor(redaction): move the secret redactors out of the tracing cra…](https://github.com/BerriAI/litellm/commit/4681fd912fb9d780b5a1288aaeea159cab2a4277) | yujonglee-berri |
| 2026-11-23 | [fix(rust_bridge): send warnings from unscoped native threads to the p…](https://github.com/BerriAI/litellm/commit/9f5f234499d03910222ee4e665ba513477fb25cb) | yujonglee-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
