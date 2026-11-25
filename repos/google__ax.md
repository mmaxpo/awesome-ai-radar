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
| 🍴 **Forks** | 807 |
| 🐞 **Open issues + PRs** | [118](https://github.com/google/ax/issues) |
| 💻 **Languages** | Go 90% · Shell 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-03-30 |
| 📦 **Latest release** | [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1) — 2026-09-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 45.9 MB |
| 🌐 **Website** | https://agentexecutor.io |

## 📦 Recent releases

### [v0.4.0-rc.1](https://github.com/google/ax/releases/tag/v0.4.0-rc.1) _(pre-release)_
<sub>2026-11-20 · 4d ago</sub>

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
| 2026-11-25 | [hack: add a basic tour of features (#753)](https://github.com/google/ax/commit/0bbe4f604a5f8756091ad94a65a596260238ad10) | rakyll |
| 2026-11-25 | [install: add a liveness probe to the Envoy sidecars of Substrate (#735)](https://github.com/google/ax/commit/b81b8c149cd67a8201d7e3da7006e10aa8384c83) | YoyinZyc |
| 2026-11-24 | [ax-server: take the router URL from --router-url, not ATENET_ROUTER_A…](https://github.com/google/ax/commit/d2e8a081cdc10ad56cff6e1285ab9af3bf5be870) | yongruilin |
| 2026-11-24 | [server: fix bugs and remove duplication from #749 (#750)](https://github.com/google/ax/commit/d47308bc5a8752e06b96f2315df7643a612d9c49) | rakyll |
| 2026-11-24 | [server: simplify CreateTask retries and model handlers (#748)](https://github.com/google/ax/commit/e97bf7ac8fa4398d8118743babc0d92f002e2325) | rakyll |
| 2026-11-24 | [api: drop data-plane fields from TaskStatus (#756)](https://github.com/google/ax/commit/39172e4811e630f380bc924170f11b3270adf9ba) | rakyll |
| 2026-11-24 | [hack/hero-demo: detect task completion inside the sandbox (#738)](https://github.com/google/ax/commit/3779eeba5e470022b62b9a1f05b9198150a0053e) | rakyll |
| 2026-11-24 | [fix(server): return store errors on suspend and resume (#736)](https://github.com/google/ax/commit/c3e77d3989e4cee254a8bf819e17430bda34d926) | yongruilin |
| 2026-11-24 | [api: align TaskState with Substrate ActorState (#731)](https://github.com/google/ax/commit/33b93cfd3ecea324b252c99dc87fba50bb510402) | rakyll |
| 2026-11-24 | [docs: explain how AX relates to Agent Substrate (#732)](https://github.com/google/ax/commit/4fcd5a9d00e8895ba7c3411ed974d65ba837a4cd) | rakyll |

[See all commits ↗](https://github.com/google/ax/commits)

## ⬇️ Get it

```bash
git clone https://github.com/google/ax.git
```
