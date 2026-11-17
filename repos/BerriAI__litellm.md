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
| ⭐ **Stars** | 63.4k |
| 🍴 **Forks** | 13.4k |
| 🐞 **Open issues + PRs** | [5.2k](https://github.com/BerriAI/litellm/issues) |
| 💻 **Languages** | Python 83% · TypeScript 10% · Rust 5% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.108.10](https://github.com/BerriAI/litellm/releases/tag/v1.108.10) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2950.9 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.108.10](https://github.com/BerriAI/litellm/releases/tag/v1.108.10)
<sub>2026-11-16 · today</sub>

> **Verify Docker Image Signature**
> ```bash
> cosign verify \
>   --certificate-identity https://github.com/BerriAI/project-releaser/.github/workflows/release.yml@refs/heads/main \
>   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
>   ghcr.io/berriai/litellm:v1.108.10
> …

### [v1.111.0-dev.3](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.3) _(pre-release)_
<sub>2026-11-15 · 2d ago</sub>

> > [!WARNING]
> > **This release was only partly published. Use [v1.111.0-dev.4](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.4) instead.**
> > It is built from the same commit and fixes the publishing problems below.
> > [!IMPORTANT]
> > **Signing has moved to keyless cosign.** This is the first release signed with Sigstore keyless signing (GitHub OIDC) instead of the `cosign.pub` key.
> > `cosign verify --key ...` does not work for this release or later ones. Use the command below. Earlier releases still verify with the key.
> …

### [v1.111.0-dev.4](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.4) _(pre-release)_
<sub>2026-11-15 · 2d ago</sub>

> > [!IMPORTANT]
> > **Signing has moved to keyless cosign.** Since v1.111.0-dev.3, releases are signed with Sigstore keyless signing (GitHub OIDC) instead of the `cosign.pub` key.
> > `cosign verify --key ...` does not work for this release. Use the command below. Earlier releases still verify with the key.
> **Verify this release**
> ```bash
> cosign verify \
> …

### [v1.110.0-rc.3](https://github.com/BerriAI/litellm/releases/tag/v1.110.0-rc.3) _(pre-release)_
<sub>2026-11-15 · 2d ago</sub>

> **Verify this release**
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
>   ghcr.io/berriai/litellm:v1.110.0-rc.3
> ```
> …

### [v1.107.0-rc.4](https://github.com/BerriAI/litellm/releases/tag/v1.107.0-rc.4) _(pre-release)_
<sub>2026-11-14 · 2d ago</sub>

> **Verify this release**
> This release candidate is built from [`a1a541b`](https://github.com/BerriAI/litellm/commit/a1a541bfb1295d44bcb3b9ab882ba8f8b1c2dfa5), the reviewed merge of #51771 into `rc/1.107.0`. It is published as `1.107.0rc4` on PyPI and `v1.107.0-rc.4` on Docker
> After the Oct 21 incident (#47826) we replaced the cosign key that signs our Docker images. These images are signed with the new key from [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065)
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [feat(litellm): add Vispark provider with Vision Small/Medium/Large (#…](https://github.com/BerriAI/litellm/commit/0cc072c999514faefd891efcd1a8b406e5350f04) | vansh-one |
| 2026-11-17 | [refactor: reuse the shared session id reader and drop fresh restating…](https://github.com/BerriAI/litellm/commit/78d0a25fcd8ebdfc8854f0a801cea9858b30e49e) | mateo-berri |
| 2026-11-17 | [feat(cost-map): price Claude on Bedrock Mantle under bedrock_mantle/ …](https://github.com/BerriAI/litellm/commit/42f901ad6597d19b1661883bb53037bbc9d85bf4) | devin-ai-integration[bot] |
| 2026-11-17 | [test(cost): mark the cost tracking cases the reconciliation automatio…](https://github.com/BerriAI/litellm/commit/fd12cba0b2b9c195fd600a1695c2e4e5ab3ad8fe) | kerry-berri |
| 2026-11-17 | [feat(callbacks-parallel-request-limiter): port parallel request limit…](https://github.com/BerriAI/litellm/commit/f5e911afd0e38a5509bcfbea1e9b1d26760ff52b) | narmstrong-berri |
| 2026-11-17 | [fix(rust): read a dict subclass by its items when converting Python i…](https://github.com/BerriAI/litellm/commit/ae92c4750772bb954b5543b59af5431d76b56b58) | mika-lt |
| 2026-11-17 | [feat(proxy): opt-in prefix block hashes in spend logs for workload re…](https://github.com/BerriAI/litellm/commit/4b12a4051e6cae2bde998aa3c54babc29c3e60d2) | mateo-berri |
| 2026-11-17 | [fix(gemini): keep thought signatures for proxy model names without ge…](https://github.com/BerriAI/litellm/commit/da296ee4bfa706e2924ef4294d5b3d9802a2aa38) | ryan-crabbe-berri |
| 2026-11-17 | [fix: keep LiteLLM-internal params out of provider request bodies (#46…](https://github.com/BerriAI/litellm/commit/98e83feeb7e0e0bb57f6b04dfc412c85404dbfdd) | fangkangmi |
| 2026-11-17 | [refactor(ui): build the dashboard and chat shells on the shadcn Sideb…](https://github.com/BerriAI/litellm/commit/9e94c716f8a0e83cd08db299721669593adac0ce) | yuneng-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
