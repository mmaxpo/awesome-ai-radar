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
| ⭐ **Stars** | 17.5k |
| 🍴 **Forks** | 313 |
| 🐞 **Open issues + PRs** | [179](https://github.com/experientiallabs/experiential/issues) |
| 💻 **Languages** | Python 87% · Rust 12% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-06-24 |
| 📦 **Latest release** | [v0.7.250](https://github.com/experientiallabs/experiential/releases/tag/v0.7.250) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 112.5 MB |
| 🌐 **Website** | https://experientiallabs.ai |

## 📦 Recent releases

### [v0.7.250](https://github.com/experientiallabs/experiential/releases/tag/v0.7.250)
<sub>2026-11-17 · today</sub>

> Parallel input moderation accepts an explicit additional wait from 0 to 5000 ms. The default remains 250 ms, and the independent classifier timeout still bounds the entire check. The existing shared request budget, native deadline enforcement and settlement behavior remain unchanged.
> Includes exp-gateway-native 0.3.193 and the previously merged warm-cache throttle fix: long Retry-After values can advance to a failover route.
> Validation: all required checks pass, including 15,785 tests across the non-live suite shards and native wheel import checks on Linux, macOS and Windows.

### [gitlab-archive/package-edge-preview-engine-bfa38ffd9e5c](https://github.com/experientiallabs/experiential/releases/tag/gitlab-archive/package-edge-preview-engine-bfa38ffd9e5c) — GitLab archive: edge-preview-engine bfa38ffd9e5cd8bd6ed26bacc161963d51bd9c98 _(pre-release)_
<sub>2026-11-17 · today</sub>

> Archived from the GitLab generic package registry before the GitLab project was retired.
> Package `edge-preview-engine`, version `bfa38ffd9e5cd8bd6ed26bacc161963d51bd9c98` (created 2026-10-25). Files verified against GitLab sha256.

### [v0.7.246](https://github.com/experientiallabs/experiential/releases/tag/v0.7.246) — experiential 0.7.246
<sub>2026-11-15 · yesterday</sub>

> Ships #1365: gateway exits for five stuck states. These are the guardrail pool worker leak on cancel, the alias reload backoff, health registry pruning, closing requests left open by a crash during failover, and a follow-up crash reconcile pass for exclusive owners. Python only; exp-gateway-native stays 0.3.190.

### [exp-code-v0.1.7](https://github.com/experientiallabs/experiential/releases/tag/exp-code-v0.1.7) — exp-code 0.1.7
<sub>2026-11-13 · 3d ago</sub>

> exp-code 0.1.7: the open-source coding and cowork agent (agent/). The sandbox runner is attached as one self-contained file with its sha256.

### [exp-code-v0.1.6](https://github.com/experientiallabs/experiential/releases/tag/exp-code-v0.1.6) — exp-code 0.1.6
<sub>2026-11-13 · 3d ago</sub>

> exp-code 0.1.6: the open-source coding and cowork agent (agent/). The sandbox runner is attached as one self-contained file with its sha256.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [release: 0.7.251 (native 0.3.194) (#1399)](https://github.com/experientiallabs/experiential/commit/d74ab1bd5c661246d9954f72e9550de7e28d552b) | SilenNaihin |
| 2026-11-17 | [gateway: accept Responses max_tool_calls (forward native, enforce gat…](https://github.com/experientiallabs/experiential/commit/9fcebeb0a6253c15fefea65d04e96fb14b2c33e2) | SilenNaihin |
| 2026-11-17 | [gateway: keep attempts for the next rung when one rung's connections …](https://github.com/experientiallabs/experiential/commit/70dfaf7b7cdf9589382cd1ee763a8449112ee6f3) | SilenNaihin |
| 2026-11-17 | [Allow configurable parallel moderation response waits (#1398)](https://github.com/experientiallabs/experiential/commit/7a2778c0e02abb3f7f51aadf24ebf3574cbd0bf6) | kfallah |
| 2026-11-17 | [Merge GitLab main into GitHub main for history parity (#1394)](https://github.com/experientiallabs/experiential/commit/e061382b0a83fb2b6845cd6df3038f3b4ecf6eb1) | SilenNaihin |
| 2026-11-17 | [gateway: a throttle waiting past the prompt cache fails over even whe…](https://github.com/experientiallabs/experiential/commit/61bceb6caa1d7dd8a74cfc9dbf4e856c17aa4fc8) | SilenNaihin |
| 2026-11-17 | [registry: scope the Azure Responses and Vertex Anthropic transports t…](https://github.com/experientiallabs/experiential/commit/6ee78cb32e1c1519abb85be17c5ec08af7d6ec23) | SilenNaihin |
| 2026-11-17 | [Merge GitLab main (e4ed8b946) into GitHub main for history parity](https://github.com/experientiallabs/experiential/commit/a6b23865b62e707b187eb45c65ee707e3ba051b5) | SilenNaihin |
| 2026-11-16 | [release: 0.7.249 (native 0.3.192) (#1384)](https://github.com/experientiallabs/experiential/commit/6c3570f1d1d42052b6f17fd65fd9d2c4f34734dc) | SilenNaihin |
| 2026-11-16 | [gateway: never end a request on a transport failure while another run…](https://github.com/experientiallabs/experiential/commit/c7b2a3474dd5cd37a11295c0c6dd68dd25d595ff) | SilenNaihin |

[See all commits ↗](https://github.com/experientiallabs/experiential/commits)

## ⬇️ Get it

```bash
git clone https://github.com/experientiallabs/experiential.git
```
