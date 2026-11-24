# google/ax

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/google/ax)

> Agent Executor (AX) is Google's open agentic orchestration runtime

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔁 Durable workflows & orchestration |
| **Project** | — |
| **Why it's worth a look** | Kubernetes-style infrastructure for AI agents |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 14.9k |
| 🍴 **Forks** | 805 |
| 🐞 **Open issues + PRs** | [126](https://github.com/google/ax/issues) |
| 💻 **Languages** | Go 91% · Shell 8% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-03-30 |
| 📦 **Latest release** | [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1) — 2026-09-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 45.9 MB |
| 🌐 **Website** | https://agentexecutor.io |

## 📦 Recent releases

### [v0.4.0-rc.1](https://github.com/google/ax/releases/tag/v0.4.0-rc.1) _(pre-release)_
<sub>2026-11-20 · 3d ago</sub>

> **Install**
> Requires [Agent Substrate](https://github.com/agent-substrate/substrate) `v1.0.0`; see [docs/installation.md](https://github.com/google/ax/blob/v0.4.0-rc.1/docs/installation.md).
> ```sh
> kubectl create namespace ax-system --dry-run=client -o yaml | kubectl apply -f -
> kubectl -n ax-system create secret generic ax-postgres --from-literal=password="$(openssl rand -hex 24)"
> kubectl apply -f https://github.com/google/ax/releases/download/v0.4.0-rc.1/postgres.yaml
> …

### [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1)
<sub>2026-09-25 · 2mo ago</sub>

> _No notes._

### [v0.3.0](https://github.com/google/ax/releases/tag/v0.3.0)
<sub>2026-09-20 · 2mo ago</sub>

> _No notes._

### [v0.2.3](https://github.com/google/ax/releases/tag/v0.2.3)
<sub>2026-08-13 · 3mo ago</sub>

> _No notes._

### [v0.2.2](https://github.com/google/ax/releases/tag/v0.2.2)
<sub>2026-07-23 · 4mo ago</sub>

> _No notes._

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [hack/hero-demo: detect task completion inside the sandbox (#738)](https://github.com/google/ax/commit/3779eeba5e470022b62b9a1f05b9198150a0053e) | rakyll |
| 2026-11-24 | [fix(server): return store errors on suspend and resume (#736)](https://github.com/google/ax/commit/c3e77d3989e4cee254a8bf819e17430bda34d926) | yongruilin |
| 2026-11-24 | [api: align TaskState with Substrate ActorState (#731)](https://github.com/google/ax/commit/33b93cfd3ecea324b252c99dc87fba50bb510402) | rakyll |
| 2026-11-24 | [docs: explain how AX relates to Agent Substrate (#732)](https://github.com/google/ax/commit/4fcd5a9d00e8895ba7c3411ed974d65ba837a4cd) | rakyll |
| 2026-11-23 | [install: default server image on releases, pin Studio, and simplify q…](https://github.com/google/ax/commit/765e3432313e2e28f97188ebbe7f8e10eb531c34) | mayawang |
| 2026-11-23 | [runner: rename the default launcher from ax-harness to ax-launcher (#…](https://github.com/google/ax/commit/0a329c8d270b93190d2f1b472dac225cde249ee7) | yongruilin |
| 2026-11-23 | [all: drop .gemini/skills and the CLAUDE.md/GEMINI.md claim (#733)](https://github.com/google/ax/commit/6e3eed3b1db76cd86c28ec84f4697e3fb4574ba3) | rakyll |
| 2026-11-23 | [controller: rename TaskReconciler to TaskManager (#730)](https://github.com/google/ax/commit/84bc16a64f305cd8463fa588d1d7bdba82d260ca) | rakyll |
| 2026-11-23 | [fix(runner): set the default environment at startup, not in runTask (…](https://github.com/google/ax/commit/a966be1a412961f0459f647d3c6f5f2dbe71e210) | yongruilin |
| 2026-11-23 | [store, server: delete TaskApplier (#719)](https://github.com/google/ax/commit/5b04a095c3bb2dad4f2c544e9d2832ef6beb89a6) | rakyll |

[See all commits ↗](https://github.com/google/ax/commits)

## ⬇️ Get it

```bash
git clone https://github.com/google/ax.git
```
