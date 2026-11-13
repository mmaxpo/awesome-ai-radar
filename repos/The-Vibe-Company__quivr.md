# The-Vibe-Company/quivr

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/The-Vibe-Company/quivr)

> An open-source engine that turns continuous content streams into search and monitoring. Durable ingestion, hybrid search, alerts, and plugins for formats, models and business rules.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why it's worth a look** | Opinionated RAG 'second brain' building block |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 39.6k |
| 🍴 **Forks** | 3.7k |
| 🐞 **Open issues + PRs** | [16](https://github.com/The-Vibe-Company/quivr/issues) |
| 💻 **Languages** | Go 55% · Python 26% · TypeScript 7% · MDX 6% · JavaScript 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `llm` `api` `chatbot` `chatgpt` `database` `docker` `frontend` `openai` `postgresql` `privacy` `security` `typescript` `html` `javascript` `react` `rag` `vector` `groq` `framework` |
| 🕒 **Last activity** | 2026-11-09 (3d ago) |
| 📅 **Created** | 2023-05-12 |
| 📦 **Latest release** | [v2.0.2](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.2) — 2026-10-30 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 171.3 MB |
| 🌐 **Website** | https://www.thevibecompany.co/en/portfolio/quivr |

## 📦 Recent releases

### [v2.0.2](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.2)
<sub>2026-10-30 · 13d ago</sub>

> **Quivr 2.0.2**
> 2.0.2 moves the search database to Weaviate 1.39.14. It changes no API, no configuration and no stored data. Upgrade any 2.0.x installation to it.
> **What Weaviate 1.39.14 fixes for Quivr**
> - **Filtered searches no longer fail at random.** Quivr filters every vector and hybrid search to the scope of the request. Weaviate's default filtering strategy could crash such a search on a node of the vector graph with more links than expected, and the search then returned an error.
> - **Security:** CVE-2026-63209, in the compression library.
> - **Less memory.**
> …

### [v2.0.1](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.1)
<sub>2026-10-30 · 14d ago</sub>

> **Quivr 2.0.1**
> 2.0.1 is a security release. It changes no API, no configuration and no stored data. Upgrade any 2.0.0 installation to it.
> **Security fixes**
> - **Weaviate 1.39.13** replaces 1.39.10 as the search database. It rejects TLS certificate chains built on the eight leaked eMudhra intermediate certificates (CVE-2026-111943). Weaviate uses TLS for backups, OIDC and model modules.
> - **Python 3.12.16** replaces 3.12.15 in the core, plugin and CPU embedding images (CVE-2026-115557).
> - **`libbrotli1` 1.0.9-2+deb12u1** is now in the TEI embedding image (CVE-2026-111497).
> …

### [v2.0.0](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.0) — Quivr 2.0.0
<sub>2026-10-29 · 14d ago</sub>

> **Quivr 2.0.0**
> Quivr is an open-source engine for content that keeps arriving. Your application, or Quivr's sources (RSS, Microsoft 365 mailboxes, X lists), send it documents. Quivr keeps every version of each document and makes it searchable within seconds, by keywords, by meaning, or both. It also checks every new document against your saved alerts. Quivr has no user interface: your application talks to it over an HTTP API, and AI agents use it through `quivr mcp`.
> 2.0.0 is the first stable release of the rewritten Quivr. The alphas were for evaluation. From this release on, Quivr makes promises you can build on.
> **What 2.0 promises**
> - **A stable API.** The HTTP API keeps the `/v0` path for every 2.x release. A 2.x release only adds to it: new endpoints, optional fields, response fields and enum values. A change that could break a working client waits for the next major release.
> - **Upgrades that keep your data.** An upgrade from one 2.x release to another runs `quivr migrate`, then rolls the worker and the API, with your data in place.
> …

### [v2.0.0-alpha.7](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.0-alpha.7) _(pre-release)_
<sub>2026-10-14 · 1mo ago</sub>

> **[2.0.0-alpha.7](https://github.com/The-Vibe-Company/quivr/compare/v2.0.0-alpha.6...v2.0.0-alpha.7) (2026-10-13)**
> **⚠ BREAKING CHANGES**
> * **storage:** In-place upgrades from `2.0.0-alpha.6` and earlier are unsupported. Reset the installation, or export data using the old installation and re-import into a fresh one. The existing Commitizen  footer records this for release-please; CHANGELOG.md is untouched.
> * **queues:** In-place upgrades from 2.0.0-alpha.6 and older are unsupported. Reset the installation, or export the data and re-import it. Rebuild operations no longer report `indexed` or `vectors_reused`.
> **Features**
> * **admin:** say when no alert applies to a document ([#3872](https://github.com/The-Vibe-Company/quivr/issues/3872)) ([c67f4ac](https://github.com/The-Vibe-Company/quivr/commit/c67f4ac89b0705a576e3e406cf0818cb42a3378c))
> …

### [v2.0.0-alpha.6](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.0-alpha.6) _(pre-release)_
<sub>2026-10-08 · 1mo ago</sub>

> **[2.0.0-alpha.6](https://github.com/The-Vibe-Company/quivr/compare/v2.0.0-alpha.5...v2.0.0-alpha.6) (2026-10-08)**
> **Features**
> * **autoscaling:** scale bulk workers from queue backlog ([#3818](https://github.com/The-Vibe-Company/quivr/issues/3818)) ([b7267a7](https://github.com/The-Vibe-Company/quivr/commit/b7267a7f52d9c0c275372ddf87db299fd87a0dda))
> * **connectors:** pause and resume continuing imports ([#3844](https://github.com/The-Vibe-Company/quivr/issues/3844)) ([fa06fe4](https://github.com/The-Vibe-Company/quivr/commit/fa06fe4cf274a798147929733b6c5da26c0133b6))
> * **content:** count metadata values for facets ([#3789](https://github.com/The-Vibe-Company/quivr/issues/3789)) ([63d76a9](https://github.com/The-Vibe-Company/quivr/commit/63d76a953fb3e42beb6fb771e86eec0f0d0fa009))
> * **corpora:** add archive, restore and rename ([#3817](https://github.com/The-Vibe-Company/quivr/issues/3817)) ([939e273](https://github.com/The-Vibe-Company/quivr/commit/939e273e61a2bcd28fc809886b18d4c57542d5d8))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-02 | [test(demo): walk every main journey of the demo with TesterArmy e2e (…](https://github.com/The-Vibe-Company/quivr/commit/bb1b19ecf4094dbd1e309e521ce8b5fed4fb539f) | StanGirard |
| 2026-11-02 | [fix(demo): pin alerts to the plugin version the core serves (#3980)](https://github.com/The-Vibe-Company/quivr/commit/25e4edf083c0fcd115ee952a048444de646604fd) | StanGirard |
| 2026-10-30 | [chore(main): release 2.0.2 (#3977)](https://github.com/The-Vibe-Company/quivr/commit/0f9ce97492ebc2f577629bcc958f377e4f8673c0) | StanGirard |
| 2026-10-30 | [fix(deploy): pin Weaviate 1.39.14 for filtered-search panics and RQ m…](https://github.com/The-Vibe-Company/quivr/commit/90d7d88e3f4287a0fa648834dbc1546ae2569cd4) | StanGirard |
| 2026-10-30 | [chore(main): release 2.0.1 (#3975)](https://github.com/The-Vibe-Company/quivr/commit/5e2bdae4c6fc5f8d029501c0303c170590f1a639) | StanGirard |
| 2026-10-30 | [fix(deploy): pin Weaviate 1.39.13 for CVE-2026-111943 (#3973)](https://github.com/The-Vibe-Company/quivr/commit/191d35f195c087852b5387e0887def9b95435bb8) | StanGirard |
| 2026-10-30 | [fix(images): rebase on Python 3.12.16 and patch brotli in TEI (#3974)](https://github.com/The-Vibe-Company/quivr/commit/84e5c4ec5a45077952326d6387bf434d6dd175f9) | StanGirard |
| 2026-10-29 | [chore(main): release 2.0.0 (#3955)](https://github.com/The-Vibe-Company/quivr/commit/e91e3d6c30e554d015974bfa69926cee5001bca4) | StanGirard |
| 2026-10-29 | [fix(release): check out before downloading signed images in publish (…](https://github.com/The-Vibe-Company/quivr/commit/313f51e361b737f7986522493e26f0f1fa411ef7) | StanGirard |
| 2026-10-29 | [docs(readme): add the Ask DeepWiki badge (#3972)](https://github.com/The-Vibe-Company/quivr/commit/bfed77dbf70f34996391d74908e4d21bbc2689ea) | StanGirard |

[See all commits ↗](https://github.com/The-Vibe-Company/quivr/commits)

## ⬇️ Get it

```bash
git clone https://github.com/The-Vibe-Company/quivr.git
```
