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
| 🍴 **Forks** | 810 |
| 🐞 **Open issues + PRs** | [82](https://github.com/google/ax/issues) |
| 💻 **Languages** | Go 90% · Shell 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-03-30 |
| 📦 **Latest release** | [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1) — 2026-09-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 46.1 MB |
| 🌐 **Website** | https://agentexecutor.io |

## 📦 Recent releases

### [v0.4.0-rc.2](https://github.com/google/ax/releases/tag/v0.4.0-rc.2) _(pre-release)_
<sub>2026-11-25 · today</sub>

> **Install**
> Requires [Agent Substrate](https://github.com/agent-substrate/substrate) `v1.0.0`; see [docs/installation.md](https://github.com/google/ax/blob/v0.4.0-rc.2/docs/installation.md).
> ```sh
> kubectl create namespace ax-system --dry-run=client -o yaml | kubectl apply -f -
> kubectl -n ax-system create secret generic ax-postgres --from-literal=password="$(openssl rand -hex 24)"
> kubectl apply -f https://github.com/google/ax/releases/download/v0.4.0-rc.2/postgres.yaml
> …

### [v0.4.0-rc.1](https://github.com/google/ax/releases/tag/v0.4.0-rc.1) _(pre-release)_
<sub>2026-11-20 · 5d ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [docs: simplify the Start AX section of the README (#787)](https://github.com/google/ax/commit/0484e74dedd591862c3d8be87a32f1b411c6c6d4) | rakyll |
| 2026-11-26 | [runner: set AX_WORKSPACE to the workspace path (#786)](https://github.com/google/ax/commit/cd6ca7c1ff9e5e6df572423d38e88204a7bd9a1d) | yongruilin |
| 2026-11-26 | [server, controller: stop reporting failures as Ready conditions (#785)](https://github.com/google/ax/commit/550f8fed985b0c5eaa221af8f572caa01ec735ea) | yongruilin |
| 2026-11-25 | [skills: remove sync-contract (#783)](https://github.com/google/ax/commit/184bb791887a9718bf6f233d396654661826a90e) | rakyll |
| 2026-11-25 | [docs: simplify the Prebuilt agent images section; add a Tour header (…](https://github.com/google/ax/commit/743d7ed81108f67b38b983b41273c7ea1b6ebf9f) | rakyll |
| 2026-11-25 | [controller: return transient Substrate errors without a condition (#779)](https://github.com/google/ax/commit/393f0bcd6c9b062605bd94ff5a2b03cca8296458) | yongruilin |
| 2026-11-25 | [install: resolve everything from AX_VERSION; simplify the local insta…](https://github.com/google/ax/commit/2263beef77b9fe29da6964bca45ca2b2ae05430e) | rakyll |
| 2026-11-25 | [api: validate resource names with k8s declarative validation (#762)](https://github.com/google/ax/commit/40cfb18e2b3be7c977ee8d0f7189384d3d6a1cbe) | yongruilin |
| 2026-11-25 | [docs: link prebuilt agent images and bump hero demo to v0.0.0-rc.4 (#…](https://github.com/google/ax/commit/8c367577b2deb4674b8a4f5fa14d16a35036326c) | mayawang |
| 2026-11-25 | [docs: drop the Anthropic Model example; only the google provider is s…](https://github.com/google/ax/commit/3f2678e8496c9919897f8ad997bdab001213ad13) | rakyll |

[See all commits ↗](https://github.com/google/ax/commits)

## ⬇️ Get it

```bash
git clone https://github.com/google/ax.git
```
