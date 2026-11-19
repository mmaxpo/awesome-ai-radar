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
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.106.11](https://github.com/BerriAI/litellm/releases/tag/v1.106.11) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3014.8 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.106.11](https://github.com/BerriAI/litellm/releases/tag/v1.106.11)
<sub>2026-11-19 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.106.11
> …

### [v1.108.12](https://github.com/BerriAI/litellm/releases/tag/v1.108.12) — 1.108.12 (LTS)
<sub>2026-11-19 · today</sub>

> > [!TIP]
> > The `lts` image tag always points to the latest LTS release. Pull `ghcr.io/berriai/litellm:lts` to stay on the newest LTS patch
> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
> …

### [v1.110.1](https://github.com/BerriAI/litellm/releases/tag/v1.110.1)
<sub>2026-11-19 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.110.1
> …

### [v1.109.2](https://github.com/BerriAI/litellm/releases/tag/v1.109.2)
<sub>2026-11-19 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.109.2
> …

### [v1.111.0-rc.2](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-rc.2) _(pre-release)_
<sub>2026-11-19 · today</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.111.0-rc.2
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [refactor(router-types): move RoutingStrategy and RoutingGroupSpec out…](https://github.com/BerriAI/litellm/commit/f20296a77635b4014077968007603391afdf971f) | yujonglee-berri |
| 2026-11-19 | [refactor(framer): relay SSE blocks without dropping a byte (#52544)](https://github.com/BerriAI/litellm/commit/95806573ea0f2e0bef3ef3b4549dcb61e9249076) | yujonglee-berri |
| 2026-11-19 | [refactor(messages): name the Messages body fields once, on the reques…](https://github.com/BerriAI/litellm/commit/f3c642ea114d63d7b810389fe039b128c2b74af3) | yujonglee-berri |
| 2026-11-19 | [feat(config): read env-backed litellm_settings keys from LITELLM_<KEY…](https://github.com/BerriAI/litellm/commit/8be5a27ebc8fe8219520654b1f35b3bf49ba9e57) | yujonglee-berri |
| 2026-11-19 | [refactor: clean up fresh tech debt in routing, riva, least-busy, prox…](https://github.com/BerriAI/litellm/commit/030bfe25b2bdb5d661654e9292122a31f49d2e89) | mateo-berri |
| 2026-11-19 | [fix(proxy): send no body upstream on a pass-through GET or DELETE sen…](https://github.com/BerriAI/litellm/commit/252ead0cc7b287c28d842f8f79b6cb46bc5a091a) | quietjules |
| 2026-11-19 | [fix(guardrails): mask reasoning text on /v1/responses output (#52504)](https://github.com/BerriAI/litellm/commit/9eb867b5aadb87a6fca07ef8470eebe6c4659147) | quietjules |
| 2026-11-19 | [refactor: clean up fresh provider configuration tech debt (#52817)](https://github.com/BerriAI/litellm/commit/f041b70191850639c054a8e4edcae4e106e89622) | devin-ai-integration[bot] |
| 2026-11-19 | [test(azure): restore client session after extra headers test (#52815)](https://github.com/BerriAI/litellm/commit/62e265506dca7bc09aecb289368d1b2a0cd6f8a2) | devin-ai-integration[bot] |
| 2026-11-19 | [fix(cost-map): price together_ai/Qwen/Qwen4-Max at the promotional ra…](https://github.com/BerriAI/litellm/commit/2f29a55a5102fbf23e406d313ea4b91a7257e48f) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
