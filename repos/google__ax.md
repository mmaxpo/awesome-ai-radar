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
| 🍴 **Forks** | 802 |
| 🐞 **Open issues + PRs** | [128](https://github.com/google/ax/issues) |
| 💻 **Languages** | Go 91% · Shell 8% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-03-30 |
| 📦 **Latest release** | [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1) — 2026-09-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 45.5 MB |
| 🌐 **Website** | https://agentexecutor.io |

## 📦 Recent releases

### [v0.4.0-rc.1](https://github.com/google/ax/releases/tag/v0.4.0-rc.1) _(pre-release)_
<sub>2026-11-20 · 2d ago</sub>

> **Install**
> Requires [Agent Substrate](https://github.com/agent-substrate/substrate) `v1.0.0`; see [docs/installation.md](https://github.com/google/ax/blob/v0.4.0-rc.1/docs/installation.md).
> ```sh
> kubectl create namespace ax-system --dry-run=client -o yaml | kubectl apply -f -
> kubectl -n ax-system create secret generic ax-postgres --from-literal=password="$(openssl rand -hex 24)"
> kubectl apply -f https://github.com/google/ax/releases/download/v0.4.0-rc.1/postgres.yaml
> …

### [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1)
<sub>2026-09-25 · 1mo ago</sub>

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
| 2026-11-23 | [api: remove TaskResult, TaskStatusReason, and TaskStatusDetail (#707)](https://github.com/google/ax/commit/775f5ad60ad86ee0bc68266b6b10ed745230ac4f) | rakyll |
| 2026-11-23 | [examples: remove Claude Code example (#706)](https://github.com/google/ax/commit/d59f5888b3a65a1cf51096f4b6d009307d236608) | rakyll |
| 2026-11-23 | [all: remove dead code and rename guest.DialTarget to Dial (#705)](https://github.com/google/ax/commit/95f4932701a35efe50342928b02146329c87e7d8) | rakyll |
| 2026-11-23 | [store, server: remove unused SetTaskDeleteTime (#701)](https://github.com/google/ax/commit/0f7abc5888f90ed711ce04de6e12ae93e4aa5330) | rakyll |
| 2026-11-22 | [fix(controller): reach actors only through atenet-router (#700)](https://github.com/google/ax/commit/d5af95e1a5b588807da7286f8327333095357405) | yongruilin |
| 2026-11-22 | [all: push tasks to runners and remove the runner pull protocol (#688)](https://github.com/google/ax/commit/2ede873cb5a1a519c0b5adf2adc8e97fe80ca1d2) | rakyll |
| 2026-11-21 | [hack: use the ax-runner image in the local install smoke test](https://github.com/google/ax/commit/0b44e971e802554e000bb7ca047bc9cef87b6691) | aojea |
| 2026-11-21 | [docs: add local development, prebuilt runners, and gateway to the roa…](https://github.com/google/ax/commit/bdb9fc1b0aab45103a49f7f29799c2da248dfa17) | rakyll |
| 2026-11-21 | [install: serve localhost registry images to the local cluster](https://github.com/google/ax/commit/7d3ba984e48b22cc402a1c7acc81eb59355a5ca7) | aojea |
| 2026-11-20 | [all: rename ax-task-runner to ax-runner (#677)](https://github.com/google/ax/commit/fb9b82966008af784b39309c13c3f9a5309b0f52) | rakyll |

[See all commits ↗](https://github.com/google/ax/commits)

## ⬇️ Get it

```bash
git clone https://github.com/google/ax.git
```
