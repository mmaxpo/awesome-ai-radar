# experientiallabs/experiential

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/experientiallabs/experiential)

> Experiential is the open source, zero markup gateway for BYOK, self-hosted and 1000+ marketplace models. It learns from your traffic to cut costs, recommend better models, and train a specialized model you own.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Gateway and router for agent workflows |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 17.6k |
| 🍴 **Forks** | 313 |
| 🐞 **Open issues + PRs** | [179](https://github.com/experientiallabs/experiential/issues) |
| 💻 **Languages** | Python 87% · Rust 12% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-06-24 |
| 📦 **Latest release** | [exp-code-v0.1.8](https://github.com/experientiallabs/experiential/releases/tag/exp-code-v0.1.8) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 114.0 MB |
| 🌐 **Website** | https://experientiallabs.ai |

## 📦 Recent releases

### [exp-code-v0.1.8](https://github.com/experientiallabs/experiential/releases/tag/exp-code-v0.1.8) — exp-code 0.1.8
<sub>2026-11-17 · today</sub>

> exp-code 0.1.8: the open-source coding and cowork agent (agent/). The sandbox runner is attached as one self-contained file with its sha256.

### [v0.7.250](https://github.com/experientiallabs/experiential/releases/tag/v0.7.250)
<sub>2026-11-17 · yesterday</sub>

> Parallel input moderation accepts an explicit additional wait from 0 to 5000 ms. The default remains 250 ms, and the independent classifier timeout still bounds the entire check. The existing shared request budget, native deadline enforcement and settlement behavior remain unchanged.
> Includes exp-gateway-native 0.3.193 and the previously merged warm-cache throttle fix: long Retry-After values can advance to a failover route.
> Validation: all required checks pass, including 15,785 tests across the non-live suite shards and native wheel import checks on Linux, macOS and Windows.

### [gitlab-archive/package-edge-preview-engine-bfa38ffd9e5c](https://github.com/experientiallabs/experiential/releases/tag/gitlab-archive/package-edge-preview-engine-bfa38ffd9e5c) — GitLab archive: edge-preview-engine bfa38ffd9e5cd8bd6ed26bacc161963d51bd9c98 _(pre-release)_
<sub>2026-11-17 · yesterday</sub>

> Archived from the GitLab generic package registry before the GitLab project was retired.
> Package `edge-preview-engine`, version `bfa38ffd9e5cd8bd6ed26bacc161963d51bd9c98` (created 2026-10-25). Files verified against GitLab sha256.

### [v0.7.246](https://github.com/experientiallabs/experiential/releases/tag/v0.7.246) — experiential 0.7.246
<sub>2026-11-15 · 2d ago</sub>

> Ships #1365: gateway exits for five stuck states. These are the guardrail pool worker leak on cancel, the alias reload backoff, health registry pruning, closing requests left open by a crash during failover, and a follow-up crash reconcile pass for exclusive owners. Python only; exp-gateway-native stays 0.3.190.

### [exp-code-v0.1.7](https://github.com/experientiallabs/experiential/releases/tag/exp-code-v0.1.7) — exp-code 0.1.7
<sub>2026-11-13 · 4d ago</sub>

> exp-code 0.1.7: the open-source coding and cowork agent (agent/). The sandbox runner is attached as one self-contained file with its sha256.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Recover sessions after rejected image inputs (#1406)](https://github.com/experientiallabs/experiential/commit/a27bcd6a566f705e33610167a027a94930ea1ae4) | kfallah |
| 2026-11-18 | [release: 0.7.253 (native 0.3.196) (#1408)](https://github.com/experientiallabs/experiential/commit/3f204599ac7519bf0ada1bf7771bf767bef5cdbd) | SilenNaihin |
| 2026-11-18 | [gateway: a malformed streamed tool call is retried once before the ca…](https://github.com/experientiallabs/experiential/commit/3f8890c96b40fb9b25cad049b68a89f7607a7a11) | SilenNaihin |
| 2026-11-17 | [release: 0.7.252 (native 0.3.195) (#1405)](https://github.com/experientiallabs/experiential/commit/413e234a39542d0ad2a0b4f4756fc72f7837fba9) | SilenNaihin |
| 2026-11-17 | [gateway: a provider content-filter refusal fails over once to another…](https://github.com/experientiallabs/experiential/commit/e980c7ae4c7d835fd4ec263525126dccff057c58) | SilenNaihin |
| 2026-11-17 | [gateway: a dial with nowhere to fail over to waits to the budget, not…](https://github.com/experientiallabs/experiential/commit/89eec06915a695aa98e88f0f3e1305dae2396165) | SilenNaihin |
| 2026-11-17 | [exp-code 0.1.8: a conversation's standing instructions in the system …](https://github.com/experientiallabs/experiential/commit/4c23b4971c806016dce0ae045ab60e0a14e724e0) | SilenNaihin |
| 2026-11-17 | [release: 0.7.251 (native 0.3.194) (#1399)](https://github.com/experientiallabs/experiential/commit/d74ab1bd5c661246d9954f72e9550de7e28d552b) | SilenNaihin |
| 2026-11-17 | [gateway: accept Responses max_tool_calls (forward native, enforce gat…](https://github.com/experientiallabs/experiential/commit/9fcebeb0a6253c15fefea65d04e96fb14b2c33e2) | SilenNaihin |
| 2026-11-17 | [gateway: keep attempts for the next rung when one rung's connections …](https://github.com/experientiallabs/experiential/commit/70dfaf7b7cdf9589382cd1ee763a8449112ee6f3) | SilenNaihin |

[See all commits ↗](https://github.com/experientiallabs/experiential/commits)

## ⬇️ Get it

```bash
git clone https://github.com/experientiallabs/experiential.git
```
