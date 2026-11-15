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
| ⭐ **Stars** | 63.3k |
| 🍴 **Forks** | 13.3k |
| 🐞 **Open issues + PRs** | [5.2k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 84% · TypeScript 10% · Rust 4% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.108.9](https://github.com/BerriAI/litellm/releases/tag/v1.108.9) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2927.9 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.111.0-dev.3](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.3) _(pre-release)_
<sub>2026-11-15 · today</sub>

> > [!WARNING]
> > **This release was only partly published. Use [v1.111.0-dev.4](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.4) instead.**
> > It is built from the same commit and fixes the publishing problems below.
> > [!IMPORTANT]
> > **Signing has moved to keyless cosign.** This is the first release signed with Sigstore keyless signing (GitHub OIDC) instead of the `cosign.pub` key.
> > `cosign verify --key ...` does not work for this release or later ones. Use the command below. Earlier releases still verify with the key.
> …

### [v1.111.0-dev.4](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.4) _(pre-release)_
<sub>2026-11-15 · today</sub>

> > [!IMPORTANT]
> > **Signing has moved to keyless cosign.** Since v1.111.0-dev.3, releases are signed with Sigstore keyless signing (GitHub OIDC) instead of the `cosign.pub` key.
> > `cosign verify --key ...` does not work for this release. Use the command below. Earlier releases still verify with the key.
> **Verify this release**
> ```bash
> cosign verify \
> …

### [v1.110.0-rc.3](https://github.com/BerriAI/litellm/releases/tag/v1.110.0-rc.3) _(pre-release)_
<sub>2026-11-15 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.107.0-rc.4](https://github.com/BerriAI/litellm/releases/tag/v1.107.0-rc.4) _(pre-release)_
<sub>2026-11-14 · today</sub>

> **Verify this release**
> This release candidate is built from [`a1a541b`](https://github.com/BerriAI/litellm/commit/a1a541bfb1295d44bcb3b9ab882ba8f8b1c2dfa5), the reviewed merge of #51771 into `rc/1.107.0`. It is published as `1.107.0rc4` on PyPI and `v1.107.0-rc.4` on Docker
> After the Oct 21 incident (#47826) we replaced the cosign key that signs our Docker images. These images are signed with the new key from [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065)
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
> …

### [v1.108.9](https://github.com/BerriAI/litellm/releases/tag/v1.108.9)
<sub>2026-11-14 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [perf(auth): read token model fields from the class instead of depreca…](https://github.com/BerriAI/litellm/commit/09ce4f50ed1298882747c6e279ea6760f1527384) | narmstrong-berri |
| 2026-11-15 | [perf(caching): format dual cache debug logs lazily (#51902)](https://github.com/BerriAI/litellm/commit/9e3a82ff03702e36e2d9e88a3b93648e6f20b787) | narmstrong-berri |
| 2026-11-15 | [perf(streaming): extract usage once per chunk when assembling stream …](https://github.com/BerriAI/litellm/commit/98c86f6e7c8e31ee66b6b68b1522941975e4cc2b) | narmstrong-berri |
| 2026-11-15 | [perf(host-python): settle ready async values inline instead of spawni…](https://github.com/BerriAI/litellm/commit/d76a7d76c4ce99bdc13c3ca68eefa53438000f22) | narmstrong-berri |
| 2026-11-15 | [refactor(s3-log): move the rust-backed s3 logger from s3_v3 to s3_v2 …](https://github.com/BerriAI/litellm/commit/3bcd77954e37ace5dd7999aaa342b41c844dac72) | narmstrong-berri |
| 2026-11-15 | [test(integration): record a stack when an owned proxy crashes (#51922)](https://github.com/BerriAI/litellm/commit/b90ac69841ed0d5afac6f0cbf790f0dcc02bbbd3) | devin-ai-integration[bot] |
| 2026-11-15 | [test(e2e): drop two batch waits that never finish in time (#51882)](https://github.com/BerriAI/litellm/commit/91fc6c20714af4a0773f8eeefaab3c57c57dfb10) | yuneng-berri |
| 2026-11-15 | [feat(customers): search customer members by ID or alias in the Member…](https://github.com/BerriAI/litellm/commit/26807a99254580b06fd91231428412460f9ecfb6) | kenneth-berri |
| 2026-11-15 | [feat(customers): move existing members between teams (#51913)](https://github.com/BerriAI/litellm/commit/00313c9e5b33715e97fbaeaa2a32571be0876536) | moe-berri |
| 2026-11-15 | [feat(ui): reuse usage spend design for customer teams and members (#5…](https://github.com/BerriAI/litellm/commit/c3b929d2031a642f4cc17f9888f4aeeea2a6df90) | tin-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
