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
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.108.14](https://github.com/BerriAI/litellm/releases/tag/v1.108.14) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3087.9 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.108.14](https://github.com/BerriAI/litellm/releases/tag/v1.108.14) — 1.108.14 (LTS)
<sub>2026-11-20 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.106.12](https://github.com/BerriAI/litellm/releases/tag/v1.106.12)
<sub>2026-11-20 · yesterday</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.106.12
> …

### [v1.111.0-rc.3](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-rc.3) _(pre-release)_
<sub>2026-11-20 · yesterday</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.111.0-rc.3
> …

### [v1.109.3](https://github.com/BerriAI/litellm/releases/tag/v1.109.3)
<sub>2026-11-20 · yesterday</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.109.3
> …

### [v1.108.13](https://github.com/BerriAI/litellm/releases/tag/v1.108.13) — 1.108.13 (LTS)
<sub>2026-11-20 · yesterday</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [refactor(auth-store): shape the cached virtual key in Rust and load i…](https://github.com/BerriAI/litellm/commit/590f5b8992bb54459ddfdce3a45f1030e55a8f83) | yujonglee-berri |
| 2026-11-21 | [refactor(auth_cache_invalidation): move the invalidation channel to t…](https://github.com/BerriAI/litellm/commit/6245f94734938b0cfc25d208064a01806518040d) | yujonglee-berri |
| 2026-11-21 | [refactor(auth_cache): type auth cache keys and keep the cache always …](https://github.com/BerriAI/litellm/commit/e8ae52cd618843cd2cf63b410751c434b8df083f) | yujonglee-berri |
| 2026-11-21 | [feat(gateway): serve inference through router-core with the host glue…](https://github.com/BerriAI/litellm/commit/897fb204f6ab44fc412453c36fc4c3caeca49467) | yujonglee-berri |
| 2026-11-21 | [test: isolate guardrail opt-out from AWS signing executor timing (#53…](https://github.com/BerriAI/litellm/commit/bc2b1d771f3e78c034c52157fdefabbcdc44fab8) | devin-ai-integration[bot] |
| 2026-11-21 | [test(spend): assert ledger callback counts apart from wire command or…](https://github.com/BerriAI/litellm/commit/e6f9598da099ec31e3be25fe2b8926249ee94c01) | devin-ai-integration[bot] |
| 2026-11-21 | [test(files): measure only upload path allocations in the large upload…](https://github.com/BerriAI/litellm/commit/c7f05822a3b9fa57d50c2b88a627be1d4d2ee9b7) | devin-ai-integration[bot] |
| 2026-11-21 | [feat(provider)!: add ResetData and stop sending OPENAI_API_KEY to key…](https://github.com/BerriAI/litellm/commit/ac7674625ceed298d6c411cc964f23aded63989d) | TheRealKraken |
| 2026-11-21 | [refactor(messages): write anthropic-family configs as anthropic plus …](https://github.com/BerriAI/litellm/commit/f428dedb315c380f193c1b5901075768b9a2bcf6) | narmstrong-berri |
| 2026-11-21 | [refactor(messages): split the messages config into four parts and bui…](https://github.com/BerriAI/litellm/commit/f72825cb6ed68ecdd27c3babaf18065b4acc4249) | narmstrong-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
