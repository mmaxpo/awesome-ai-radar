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
| 💻 **Languages** | Python 84% · TypeScript 10% · Rust 5% |
| 📜 **License** | Other |
| 🏷 **Topics** | `anthropic` `langchain` `llm` `llmops` `openai` `ai-gateway` `azure-openai` `bedrock` `gateway` `openai-proxy` `vertex-ai` `llm-gateway` `litellm` `mcp-gateway` `rust` `rust-ai` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2023-07-27 |
| 📦 **Latest release** | [v1.108.9](https://github.com/BerriAI/litellm/releases/tag/v1.108.9) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2936.1 MB |
| 🌐 **Website** | https://docs.litellm.ai/docs/ |

## 📦 Recent releases

### [v1.111.0-dev.3](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.3) _(pre-release)_
<sub>2026-11-15 · yesterday</sub>

> > [!WARNING]
> > **This release was only partly published. Use [v1.111.0-dev.4](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.4) instead.**
> > It is built from the same commit and fixes the publishing problems below.
> > [!IMPORTANT]
> > **Signing has moved to keyless cosign.** This is the first release signed with Sigstore keyless signing (GitHub OIDC) instead of the `cosign.pub` key.
> > `cosign verify --key ...` does not work for this release or later ones. Use the command below. Earlier releases still verify with the key.
> …

### [v1.111.0-dev.4](https://github.com/BerriAI/litellm/releases/tag/v1.111.0-dev.4) _(pre-release)_
<sub>2026-11-15 · yesterday</sub>

> > [!IMPORTANT]
> > **Signing has moved to keyless cosign.** Since v1.111.0-dev.3, releases are signed with Sigstore keyless signing (GitHub OIDC) instead of the `cosign.pub` key.
> > `cosign verify --key ...` does not work for this release. Use the command below. Earlier releases still verify with the key.
> **Verify this release**
> ```bash
> cosign verify \
> …

### [v1.110.0-rc.3](https://github.com/BerriAI/litellm/releases/tag/v1.110.0-rc.3) _(pre-release)_
<sub>2026-11-15 · yesterday</sub>

> **Verify Docker Image Signature**
> All LiteLLM Docker images are signed with [cosign](https://docs.sigstore.dev/cosign/overview/). This release is signed with the key introduced in [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065).
> **Verify using the pinned commit hash (recommended):**
> A commit hash is cryptographically immutable, so this is the strongest way to ensure you are using the published signing key:
> ```bash
> cosign verify \
> …

### [v1.107.0-rc.4](https://github.com/BerriAI/litellm/releases/tag/v1.107.0-rc.4) _(pre-release)_
<sub>2026-11-14 · yesterday</sub>

> **Verify this release**
> This release candidate is built from [`a1a541b`](https://github.com/BerriAI/litellm/commit/a1a541bfb1295d44bcb3b9ab882ba8f8b1c2dfa5), the reviewed merge of #51771 into `rc/1.107.0`. It is published as `1.107.0rc4` on PyPI and `v1.107.0-rc.4` on Docker
> After the Oct 21 incident (#47826) we replaced the cosign key that signs our Docker images. These images are signed with the new key from [commit `e82a3c6`](https://github.com/BerriAI/litellm/commit/e82a3c646908ba0a6ee0beddc4310d7a6cac4065)
> ```bash
> cosign verify \
>   --key https://raw.githubusercontent.com/BerriAI/litellm/e82a3c646908ba0a6ee0beddc4310d7a6cac4065/cosign.pub \
> …

### [v1.108.9](https://github.com/BerriAI/litellm/releases/tag/v1.108.9)
<sub>2026-11-14 · yesterday</sub>

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
| 2026-11-16 | [chore(cost-map): add fal_ai seedance 2.5 flash rows, copilot deprecat…](https://github.com/BerriAI/litellm/commit/9a1e3bde9453f9b1316790fc51e6c098d9447d7b) | devin-ai-integration[bot] |
| 2026-11-16 | [fix(proxy): stop returning stack traces in health check errors](https://github.com/BerriAI/litellm/commit/5c540976f603ff8bed19ebf846a0604a942d64ac) | ojensen-berri |
| 2026-11-16 | [fix(decisions): answer 400 naming extra_headers when it is not an obj…](https://github.com/BerriAI/litellm/commit/f517a821b320ede3882b44353cb40510d8357473) | paveln83 |
| 2026-11-16 | [refactor(auth): plan the authentication path in Rust (#51605)](https://github.com/BerriAI/litellm/commit/76e45df333c0b021b56ad119c3f3d4a40deedadf) | yujonglee-berri |
| 2026-11-16 | [refactor(auth): decide route rules in Rust (#51531)](https://github.com/BerriAI/litellm/commit/4aa00352bbf9878d781eeb4e4535204f9f92568b) | yujonglee-berri |
| 2026-11-16 | [feat(fnmatch): add a crate for Python's fnmatchcase glob dialect (#51…](https://github.com/BerriAI/litellm/commit/ad18efa84b369a71aba2bbd346d5b6eb2474923c) | yujonglee-berri |
| 2026-11-16 | [refactor(proxy): keep the detached stream failure hook state on the l…](https://github.com/BerriAI/litellm/commit/2f448a9ee896d6d3ccb2899be0532bb031d49d95) | narmstrong-berri |
| 2026-11-16 | [fix(messages): clamp bedrock effort before the drop_params effort gat…](https://github.com/BerriAI/litellm/commit/d034fb681ca296a0f082a224043eda62a2ce82d4) | narmstrong-berri |
| 2026-11-16 | [fix(proxy)!: match the sign-in email fallback to the right user (#51897)](https://github.com/BerriAI/litellm/commit/58d86c21488653dee1d4844e5d27e0789c0d9148) | shrey-berri |
| 2026-11-16 | [fix(proxy): stop team model writes from pulling in proxy-level settin…](https://github.com/BerriAI/litellm/commit/609acd5d9ccf54caf2061c883ea923347fd05b9b) | shrey-berri |

[See all commits ↗](https://github.com/BerriAI/litellm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BerriAI/litellm.git
```
