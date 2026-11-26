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
| ⭐ **Stars** | 39.7k |
| 🍴 **Forks** | 3.7k |
| 🐞 **Open issues + PRs** | [20](https://github.com/The-Vibe-Company/quivr/issues) |
| 💻 **Languages** | Go 55% · Python 27% · TypeScript 7% · MDX 6% · JavaScript 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `llm` `api` `chatbot` `chatgpt` `database` `docker` `frontend` `openai` `postgresql` `privacy` `security` `typescript` `html` `javascript` `react` `rag` `vector` `groq` `framework` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2023-05-12 |
| 📦 **Latest release** | [v2.0.3](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.3) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 172.9 MB |
| 🌐 **Website** | https://www.thevibecompany.co/en/portfolio/quivr |

## 📦 Recent releases

### [v2.0.3](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.3)
<sub>2026-11-16 · 9d ago</sub>

> **Quivr 2.0.3**
> 2.0.3 is a security and fix release. It changes no API, no configuration and no stored data. Upgrade any 2.0.x installation to it.
> **Security fixes**
> - **Go 1.27.4** builds every Quivr binary and image (GO-2026-6859, in `net/http`).
> - **PostgreSQL 17.12** replaces 17.11 in the database image. It ships zlib 1.4 (CVE-2026-4738). This is a PostgreSQL minor release: the data on disk stays as it is.
> - **SeaweedFS**, which stores original files, gets zlib 1.4 (CVE-2026-4738) and brotli v1.2.7 (GO-2026-6888).
> …

### [v2.0.2](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.2)
<sub>2026-10-30 · 27d ago</sub>

> **Quivr 2.0.2**
> 2.0.2 moves the search database to Weaviate 1.39.14. It changes no API, no configuration and no stored data. Upgrade any 2.0.x installation to it.
> **What Weaviate 1.39.14 fixes for Quivr**
> - **Filtered searches no longer fail at random.** Quivr filters every vector and hybrid search to the scope of the request. Weaviate's default filtering strategy could crash such a search on a node of the vector graph with more links than expected, and the search then returned an error.
> - **Security:** CVE-2026-63209, in the compression library.
> - **Less memory.**
> …

### [v2.0.1](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.1)
<sub>2026-10-30 · 27d ago</sub>

> **Quivr 2.0.1**
> 2.0.1 is a security release. It changes no API, no configuration and no stored data. Upgrade any 2.0.0 installation to it.
> **Security fixes**
> - **Weaviate 1.39.13** replaces 1.39.10 as the search database. It rejects TLS certificate chains built on the eight leaked eMudhra intermediate certificates (CVE-2026-111943). Weaviate uses TLS for backups, OIDC and model modules.
> - **Python 3.12.16** replaces 3.12.15 in the core, plugin and CPU embedding images (CVE-2026-115557).
> - **`libbrotli1` 1.0.9-2+deb12u1** is now in the TEI embedding image (CVE-2026-111497).
> …

### [v2.0.0](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.0) — Quivr 2.0.0
<sub>2026-10-29 · 27d ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [ci: share verified image scan inputs and stop PR cache exports (#4024)](https://github.com/The-Vibe-Company/quivr/commit/38f027907a4bdb0a43b3f99811dc58ff585c1c5a) | StanGirard |
| 2026-11-26 | [feat(config): inject secrets outside runtime JSON (#4007)](https://github.com/The-Vibe-Company/quivr/commit/14518f3b41ba41ed99953c3d3adccd7c88ac28d0) | StanGirard |
| 2026-11-26 | [perf(storage): pack normalized text per version (#4022)](https://github.com/The-Vibe-Company/quivr/commit/edb55dbd46e9e071657198c9660485bbb8228710) | StanGirard |
| 2026-11-26 | [feat(bench): add reproducible cold/warm search and ingestion perf har…](https://github.com/The-Vibe-Company/quivr/commit/4af59a46b6fa9e25a00f0523f26ddf9aa5d6a914) | StanGirard |
| 2026-11-26 | [perf(hydration): add bounded content-addressed text blob LRU cache an…](https://github.com/The-Vibe-Company/quivr/commit/7aea34c336352afdb4b1b425a14a045f18e2ca68) | StanGirard |
| 2026-11-26 | [build(plugins): bundle first-party Go plugins into stripped multi-cal…](https://github.com/The-Vibe-Company/quivr/commit/b891901ebfc7db04cd1eeeeb497cb9bcb617b09d) | StanGirard |
| 2026-11-26 | [perf(devx): cache local Go plugin binaries and add fast dev profile (…](https://github.com/The-Vibe-Company/quivr/commit/4a12148ad365bf71f927f975233c826a0785236a) | StanGirard |
| 2026-11-26 | [feat(retrieval): add AIMD search admission limiter and graceful deep-…](https://github.com/The-Vibe-Company/quivr/commit/44f359d593aa70cbc447757182e6ffeaed1bd2d0) | StanGirard |
| 2026-11-26 | [perf(query-encoder): replace PyTorch FP32 CPU encoder with quantized …](https://github.com/The-Vibe-Company/quivr/commit/e9eaf43c89f547d4afac241efade2328beef8888) | StanGirard |
| 2026-11-26 | [perf(retrieval): coalesce and cache query encodings (#4018)](https://github.com/The-Vibe-Company/quivr/commit/2661a93eb630f7a5aff783e280e89661f3ec0be1) | StanGirard |

[See all commits ↗](https://github.com/The-Vibe-Company/quivr/commits)

## ⬇️ Get it

```bash
git clone https://github.com/The-Vibe-Company/quivr.git
```
