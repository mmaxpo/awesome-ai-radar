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
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.106.10](https://github.com/BerriAI/litellm/releases/tag/v1.106.10) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2921.2 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.106.10](https://github.com/BerriAI/litellm/releases/tag/v1.106.10)
<sub>2026-11-14 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
>   ghcr.io/berriai/litellm:v1.106.10
> ```
> …

### [v1.108.8](https://github.com/BerriAI/litellm/releases/tag/v1.108.8) — 1.108.8 (LTS)
<sub>2026-11-13 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
> …

### [v1.111.0-dev.2](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.2) _(pre-release)_
<sub>2026-11-13 · today</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.111.0-dev.1](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.1) _(pre-release)_
<sub>2026-11-13 · yesterday</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.108.7](https://github.com/BerriAI/litellm/releases/tag/v1.108.7) — 1.108.7 (LTS)
<sub>2026-11-12 · yesterday</sub>

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
| 2026-11-14 | [fix(aiohttp): reset the upstream connection when a stream closes earl…](https://github.com/BerriAI/litellm/commit/ec48e2491c5132951cd2710671506019ce93f0a0) | princejain756 |
| 2026-11-14 | [fix(scim): skip groups with no team so a PATCH or PUT still deactivat…](https://github.com/BerriAI/litellm/commit/cad4570bbe49d0f3be013d07abd403dd21621b3b) | mika-lt |
| 2026-11-14 | [fix(gateway)!: apply a deployment's Messages params and fill model ca…](https://github.com/BerriAI/litellm/commit/8140fdf54f31a417d8cb186f2074df62a3cf490c) | norkelbyte |
| 2026-11-14 | [fix(together_ai): stop listing retired Together ids (#51827)](https://github.com/BerriAI/litellm/commit/1f6e401a681163bf7039948a4713921dc18955ec) | mika-lt |
| 2026-11-14 | [feat(github_copilot): support GitHub App authentication with PEM uplo…](https://github.com/BerriAI/litellm/commit/9d827093c5cd220be65c8f2e3bd3979e5ede9062) | giladk1221 |
| 2026-11-14 | [test(e2e): move audio, realtime, and Langfuse tests off model ids wit…](https://github.com/BerriAI/litellm/commit/05518975a559f1b3d40a12a254a9aba3f4e49a61) | paveln83 |
| 2026-11-14 | [feat(decisions): support Vercel AI Gateway decision models (#50642)](https://github.com/BerriAI/litellm/commit/fd6c00200c52e079ea010c3752ad241eb5ac45e5) | mishdotdev |
| 2026-11-14 | [fix(proxy): run baggage tag mappings and budget checks on /queue/chat…](https://github.com/BerriAI/litellm/commit/ac1cc5111cb26700710a4aafaef18df897634e16) | norkelbyte |
| 2026-11-14 | [fix(proxy): count the request's tool_choice on the token count routes…](https://github.com/BerriAI/litellm/commit/27c796c412eed2f7336dccb46a58247463b7c498) | tavren27 |
| 2026-11-14 | [fix(openrouter): suppress empty post-finish choice before usage trail…](https://github.com/BerriAI/litellm/commit/8b28818fa22a4a915f974ba6096f3cb9474061f4) | VISHNU0906 |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
