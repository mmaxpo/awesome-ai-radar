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
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-05-12 |
| 📦 **Latest release** | [v2.1.1](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.1.1) — 2026-11-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 173.8 MB |
| 🌐 **Website** | https://www.thevibecompany.co/en/portfolio/quivr |

## 📦 Recent releases

### [v2.1.1](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.1.1)
<sub>2026-11-27 · today</sub>

> **[2.1.1](https://github.com/The-Vibe-Company/quivr/compare/v2.1.0...v2.1.1) (2026-11-27)**
> **Performance Improvements**
> * **postgres:** shard large hydration batches across pool connections ([#4034](https://github.com/The-Vibe-Company/quivr/issues/4034)) ([e9cbe98](https://github.com/The-Vibe-Company/quivr/commit/e9cbe98f36052a77679524819eefbac1c884b690))
> * **retrieval:** coalesce legacy multi-part hydration and back off failed coverage refreshes ([#4032](https://github.com/The-Vibe-Company/quivr/issues/4032)) ([1e5d28c](https://github.com/The-Vibe-Company/quivr/commit/1e5d28c054e615a787aa7d84c294c0622ed71064))

### [v2.1.0](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.1.0)
<sub>2026-11-26 · today</sub>

> **[2.1.0](https://github.com/The-Vibe-Company/quivr/compare/v2.0.3...v2.1.0) (2026-11-26)**
> **Features**
> * **api:** separate /v0/admin/* onto a dedicated internal admin listener ([#4011](https://github.com/The-Vibe-Company/quivr/issues/4011)) ([805021c](https://github.com/The-Vibe-Company/quivr/commit/805021cebeead309f5507d2d4c1d9c270f15cb63))
> * **audit:** record access refusals and filter by actor ([#4006](https://github.com/The-Vibe-Company/quivr/issues/4006)) ([290ba33](https://github.com/The-Vibe-Company/quivr/commit/290ba3314df1740cb084f186bdf3db9ec7873c19))
> * **bench:** add reproducible cold/warm search and ingestion perf harness ([#4012](https://github.com/The-Vibe-Company/quivr/issues/4012)) ([4af59a4](https://github.com/The-Vibe-Company/quivr/commit/4af59a46b6fa9e25a00f0523f26ddf9aa5d6a914))
> * **config:** inject secrets outside runtime JSON ([#4007](https://github.com/The-Vibe-Company/quivr/issues/4007)) ([14518f3](https://github.com/The-Vibe-Company/quivr/commit/14518f3b41ba41ed99953c3d3adccd7c88ac28d0))
> …

### [v2.0.3](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.3)
<sub>2026-11-16 · 10d ago</sub>

> **Quivr 2.0.3**
> 2.0.3 is a security and fix release. It changes no API, no configuration and no stored data. Upgrade any 2.0.x installation to it.
> **Security fixes**
> - **Go 1.27.4** builds every Quivr binary and image (GO-2026-6859, in `net/http`).
> - **PostgreSQL 17.12** replaces 17.11 in the database image. It ships zlib 1.4 (CVE-2026-4738). This is a PostgreSQL minor release: the data on disk stays as it is.
> - **SeaweedFS**, which stores original files, gets zlib 1.4 (CVE-2026-4738) and brotli v1.2.7 (GO-2026-6888).
> …

### [v2.0.2](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.2)
<sub>2026-10-30 · 28d ago</sub>

> **Quivr 2.0.2**
> 2.0.2 moves the search database to Weaviate 1.39.14. It changes no API, no configuration and no stored data. Upgrade any 2.0.x installation to it.
> **What Weaviate 1.39.14 fixes for Quivr**
> - **Filtered searches no longer fail at random.** Quivr filters every vector and hybrid search to the scope of the request. Weaviate's default filtering strategy could crash such a search on a node of the vector graph with more links than expected, and the search then returned an error.
> - **Security:** CVE-2026-63209, in the compression library.
> - **Less memory.**
> …

### [v2.0.1](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.1)
<sub>2026-10-30 · 28d ago</sub>

> **Quivr 2.0.1**
> 2.0.1 is a security release. It changes no API, no configuration and no stored data. Upgrade any 2.0.0 installation to it.
> **Security fixes**
> - **Weaviate 1.39.13** replaces 1.39.10 as the search database. It rejects TLS certificate chains built on the eight leaked eMudhra intermediate certificates (CVE-2026-111943). Weaviate uses TLS for backups, OIDC and model modules.
> - **Python 3.12.16** replaces 3.12.15 in the core, plugin and CPU embedding images (CVE-2026-115557).
> - **`libbrotli1` 1.0.9-2+deb12u1** is now in the TEI embedding image (CVE-2026-111497).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [feat(eval): support corpus reuse, corpus config, and multi-plugin ret…](https://github.com/The-Vibe-Company/quivr/commit/066e78df719f25b195ccd069c2d232e71c1e0659) | StanGirard |
| 2026-11-27 | [feat(plugins): add generic HTTP cross-encoder reranking retrieval plu…](https://github.com/The-Vibe-Company/quivr/commit/85a2f028a62357377c5c8d47c0488787bc8209c9) | StanGirard |
| 2026-11-27 | [feat(plugins): add retrieval plugin scaffold template (#4038)](https://github.com/The-Vibe-Company/quivr/commit/0371d46dbbbc99911ab78c7a672c2df55cb03635) | StanGirard |
| 2026-11-27 | [feat(eval): add TREC scoring and judgment diagnostics (#4036)](https://github.com/The-Vibe-Company/quivr/commit/0acaf492c1fe1dcffd69f01b8498e3101d7bce06) | StanGirard |
| 2026-11-27 | [chore(main): release 2.1.1 (#4033)](https://github.com/The-Vibe-Company/quivr/commit/64f5a9712da1371b1cd1443002b41be5b2e89d99) | StanGirard |
| 2026-11-27 | [ci(release): advance stable branch on verified stable releases (#4035)](https://github.com/The-Vibe-Company/quivr/commit/3153805eb07993f7a7cd708c24f6bf45a9506f49) | StanGirard |
| 2026-11-26 | [perf(postgres): shard large hydration batches across pool connections…](https://github.com/The-Vibe-Company/quivr/commit/e9cbe98f36052a77679524819eefbac1c884b690) | StanGirard |
| 2026-11-26 | [perf(retrieval): coalesce legacy multi-part hydration and back off fa…](https://github.com/The-Vibe-Company/quivr/commit/1e5d28c054e615a787aa7d84c294c0622ed71064) | StanGirard |
| 2026-11-26 | [chore(main): release 2.1.0 (#4023)](https://github.com/The-Vibe-Company/quivr/commit/44168d1ab925cfd0fa0a6a1c8d587568eec69015) | StanGirard |
| 2026-11-26 | [fix(deploy): count multi-tenant Weaviate objects in lifecycle and res…](https://github.com/The-Vibe-Company/quivr/commit/64e964f4040243a35e60ce1ff1aa77a8923fffe9) | StanGirard |

[See all commits ↗](https://github.com/The-Vibe-Company/quivr/commits)

## ⬇️ Get it

```bash
git clone https://github.com/The-Vibe-Company/quivr.git
```
