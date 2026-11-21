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
| ⭐ **Stars** | 14.8k |
| 🍴 **Forks** | 800 |
| 🐞 **Open issues + PRs** | [113](https://github.com/google/ax/issues) |
| 💻 **Languages** | Go 92% · Shell 7% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-03-30 |
| 📦 **Latest release** | [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1) — 2026-09-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 45.5 MB |
| 🌐 **Website** | https://agentexecutor.io |

## 📦 Recent releases

### [v0.4.0-rc.1](https://github.com/google/ax/releases/tag/v0.4.0-rc.1) _(pre-release)_
<sub>2026-11-20 · today</sub>

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
| 2026-11-21 | [hack: use the ax-runner image in the local install smoke test](https://github.com/google/ax/commit/0b44e971e802554e000bb7ca047bc9cef87b6691) | aojea |
| 2026-11-21 | [docs: add local development, prebuilt runners, and gateway to the roa…](https://github.com/google/ax/commit/bdb9fc1b0aab45103a49f7f29799c2da248dfa17) | rakyll |
| 2026-11-21 | [install: serve localhost registry images to the local cluster](https://github.com/google/ax/commit/7d3ba984e48b22cc402a1c7acc81eb59355a5ca7) | aojea |
| 2026-11-20 | [all: rename ax-task-runner to ax-runner (#677)](https://github.com/google/ax/commit/fb9b82966008af784b39309c13c3f9a5309b0f52) | rakyll |
| 2026-11-20 | [hack/hero-demo: redirect stdin from /dev/null in wait_for_file (#673)](https://github.com/google/ax/commit/2aa2c93433192ca959bd32033ee7c4875ca4ff9d) | mayawang |
| 2026-11-20 | [api, server: require Task spec.profile to name an image; drop the def…](https://github.com/google/ax/commit/465cbebbd29240800f5b1c2841790de916bcae5c) | rakyll |
| 2026-11-20 | [hack/hero-demo: follow tasks to completion in Steps 3, 4 and 5 (#671)](https://github.com/google/ax/commit/2701b10b459e6fe69ae3e4e0a1422641f349e229) | yongruilin |
| 2026-11-20 | [docs: add AX Studio to the README and the local installer guide (#668)](https://github.com/google/ax/commit/44ecc7963a5d458a14a071332e1d48693795e439) | YoyinZyc |
| 2026-11-20 | [fix(controller): let a task recreated under the same name start (#667)](https://github.com/google/ax/commit/c640e62cb8dc04b9cf769e173dea99a53bd20107) | yongruilin |
| 2026-11-20 | [fix(promote): handle a finished task and a workspace's setup gateway …](https://github.com/google/ax/commit/de7de9052233b67da83bf1df282ccd6b6f9dc356) | yongruilin |

[See all commits ↗](https://github.com/google/ax/commits)

## ⬇️ Get it

```bash
git clone https://github.com/google/ax.git
```
