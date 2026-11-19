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
| ⭐ **Stars** | 17.8k |
| 🍴 **Forks** | 316 |
| 🐞 **Open issues + PRs** | [179](https://github.com/experientiallabs/experiential/issues) |
| 💻 **Languages** | Python 87% · Rust 12% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-06-24 |
| 📦 **Latest release** | [v0.7.256](https://github.com/experientiallabs/experiential/releases/tag/v0.7.256) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 114.6 MB |
| 🌐 **Website** | https://experientiallabs.ai |

## 📦 Recent releases

### [v0.7.256](https://github.com/experientiallabs/experiential/releases/tag/v0.7.256) — Experiential 0.7.256
<sub>2026-11-19 · today</sub>

> Experiential 0.7.256 adds optional, content-free evidence for online input checks to existing terminal ledger writes. A host can distinguish completed checks from timeouts and classifier errors using authenticated request identity, policy revision, outcome and a bounded input-window digest.
> Collection is opt-in for supporting ledger writers. Terminal retries preserve the frozen evidence, and accepted requests that fail before accounting registration retain their check outcomes. This adds no classifier requests, recovery workers, policy deadlines or admission decisions.
> The release retains `exp-gateway-native==0.3.201`, published with 0.7.255.
> Changes: https://github.com/experientiallabs/experiential/pull/1409

### [exp-code-v0.1.8](https://github.com/experientiallabs/experiential/releases/tag/exp-code-v0.1.8) — exp-code 0.1.8
<sub>2026-11-17 · yesterday</sub>

> exp-code 0.1.8: the open-source coding and cowork agent (agent/). The sandbox runner is attached as one self-contained file with its sha256.

### [v0.7.250](https://github.com/experientiallabs/experiential/releases/tag/v0.7.250)
<sub>2026-11-17 · 2d ago</sub>

> Parallel input moderation accepts an explicit additional wait from 0 to 5000 ms. The default remains 250 ms, and the independent classifier timeout still bounds the entire check. The existing shared request budget, native deadline enforcement and settlement behavior remain unchanged.
> Includes exp-gateway-native 0.3.193 and the previously merged warm-cache throttle fix: long Retry-After values can advance to a failover route.
> Validation: all required checks pass, including 15,785 tests across the non-live suite shards and native wheel import checks on Linux, macOS and Windows.

### [gitlab-archive/package-edge-preview-engine-bfa38ffd9e5c](https://github.com/experientiallabs/experiential/releases/tag/gitlab-archive/package-edge-preview-engine-bfa38ffd9e5c) — GitLab archive: edge-preview-engine bfa38ffd9e5cd8bd6ed26bacc161963d51bd9c98 _(pre-release)_
<sub>2026-11-17 · 2d ago</sub>

> Archived from the GitLab generic package registry before the GitLab project was retired.
> Package `edge-preview-engine`, version `bfa38ffd9e5cd8bd6ed26bacc161963d51bd9c98` (created 2026-10-25). Files verified against GitLab sha256.

### [v0.7.246](https://github.com/experientiallabs/experiential/releases/tag/v0.7.246) — experiential 0.7.246
<sub>2026-11-15 · 3d ago</sub>

> Ships #1365: gateway exits for five stuck states. These are the guardrail pool worker leak on cancel, the alias reload backoff, health registry pruning, closing requests left open by a crash during failover, and a follow-up crash reconcile pass for exclusive owners. Python only; exp-gateway-native stays 0.3.190.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [gateway: file a Gemini output block relayed by OpenRouter as a refusa…](https://github.com/experientiallabs/experiential/commit/e177a06daf09a7e3216f229e453024b243504cc0) | SilenNaihin |
| 2026-11-19 | [Persist request-linked input-check outcomes through accounting (#1409)](https://github.com/experientiallabs/experiential/commit/c4a22749f1a28f0c132917a89e250d5163431c35) | kfallah |
| 2026-11-19 | [release: 0.7.255 (native 0.3.201) (#1418)](https://github.com/experientiallabs/experiential/commit/5d26abc13b8b6a4303d3e0570e9245ec710aacc0) | SilenNaihin |
| 2026-11-19 | [gateway: repair a Gemini thought signature another Google backend min…](https://github.com/experientiallabs/experiential/commit/a91f60b1dd4f469d6010a92e5b82c695609155c0) | SilenNaihin |
| 2026-11-18 | [gateway: clearer copy and leniency for coding-agent request shapes (#…](https://github.com/experientiallabs/experiential/commit/d96443ab593cd6f2086c7abd7476b18cc75f08bd) | SilenNaihin |
| 2026-11-18 | [gateway: word a context overflow as Anthropic's "prompt is too long" …](https://github.com/experientiallabs/experiential/commit/983eeb3402b4312725ed93cf8bbd3730de1721ec) | SilenNaihin |
| 2026-11-18 | [gateway: retry malformed DSML tool-call markup once, like a malformed…](https://github.com/experientiallabs/experiential/commit/02191ac8fe8a142390fe8c142983fbeea6f23f17) | SilenNaihin |
| 2026-11-18 | [gateway: strip refused encrypted function output parts on replay, nam…](https://github.com/experientiallabs/experiential/commit/b404266270ba44565f5d1933d2934c703af53e97) | SilenNaihin |
| 2026-11-18 | [release: 0.7.254 (native 0.3.197) (#1411)](https://github.com/experientiallabs/experiential/commit/63d94d649ee6d2adab9d81f055307f3c97895e94) | SilenNaihin |
| 2026-11-18 | [gateway: file an end-user policy block as a refusal, not provider_aut…](https://github.com/experientiallabs/experiential/commit/9641f8fcf6fe2b763c1fe631212cc3d0bca1847e) | SilenNaihin |

[See all commits ↗](https://github.com/experientiallabs/experiential/commits)

## ⬇️ Get it

```bash
git clone https://github.com/experientiallabs/experiential.git
```
