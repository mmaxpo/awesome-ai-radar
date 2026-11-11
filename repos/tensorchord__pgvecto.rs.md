# tensorchord/pgvecto.rs

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/tensorchord/pgvecto.rs)

> Scalable, Low-latency and Hybrid-enabled Vector Search in Postgres. Revolutionize Vector Search, not Database.

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why I saved it** | Vector search extension for Postgres |
| **Added** | 2026-11-11 |

💤 **Quiet** — no activity for 1y

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 2.2k |
| 🍴 **Forks** | 87 |
| 🐞 **Open issues + PRs** | [77](https://github.com/tensorchord/pgvecto.rs/issues) |
| 💻 **Languages** | Rust 82% · PLpgSQL 13% · Shell 3% · Dockerfile 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `chatgpt` `faiss` `gpt` `hacktoberfest` `llm` `nearest-neighbor-search` `postgres` `rust` `vector` `vector-database` |
| 🕒 **Last activity** | 2025-02-26 (1y ago) |
| 📅 **Created** | 2023-04-15 |
| 📦 **Latest release** | [v0.4.0](https://github.com/tensorchord/pgvecto.rs/releases/tag/v0.4.0) — 2024-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3.3 MB |
| 🌐 **Website** | https://docs.vectorchord.ai/getting-started/overview.html |

## 📦 Recent releases

### [v0.4.0](https://github.com/tensorchord/pgvecto.rs/releases/tag/v0.4.0)
<sub>2024-11-21 · 1y ago</sub>

> **What's Changed**
> * feat: increment build by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/508
> * test: fix flaky test in bvector.slt by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/512
> * fix: ivfflat options of pgvector compatibility by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/514
> * fix: fix elkan k means termination condition by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/515
> * ci: skip zomible process in crash test by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/516
> …

### [v0.4.0-alpha.2](https://github.com/tensorchord/pgvecto.rs/releases/tag/v0.4.0-alpha.2) _(pre-release)_
<sub>2024-09-23 · 2y ago</sub>

> **What's Changed**
> * refactor: rework quantization abstraction by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/591
> * feat: add metrics dot and cos by @cutecutecat in https://github.com/tensorchord/pgvecto.rs/pull/566
> * refactor: rabitq by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/593
> * docs: delete sparse vector search comparison in readme by @JinweiOS in https://github.com/tensorchord/pgvecto.rs/pull/595
> * refactor: use transposed centroids in PQ preprocess by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/594
> …

### [v0.4.0-alpha.1](https://github.com/tensorchord/pgvecto.rs/releases/tag/v0.4.0-alpha.1) _(pre-release)_
<sub>2024-09-05 · 2y ago</sub>

> _No notes._

### [v0.3.0](https://github.com/tensorchord/pgvecto.rs/releases/tag/v0.3.0)
<sub>2024-06-20 · 2y ago</sub>

> _No notes._

### [v0.3.0-alpha.2](https://github.com/tensorchord/pgvecto.rs/releases/tag/v0.3.0-alpha.2) _(pre-release)_
<sub>2024-06-01 · 2y ago</sub>

> **What's Changed**
> * fix: disable UNLOGGED vector indexes by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/443
> * fix: invalid check for bvector with 64 dims by @silver-ymz in https://github.com/tensorchord/pgvecto.rs/pull/444
> * fix: take `MyDatabaseId` into handle to resolve conflicts of OIDs in multidatabases by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/445
> * feat: add optimizing_threads to function by @cutecutecat in https://github.com/tensorchord/pgvecto.rs/pull/375
> * chore: add another implementation of multiversion by @usamoi in https://github.com/tensorchord/pgvecto.rs/pull/446
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2025-02-26 | [docs: update to ghcr in README (#642)](https://github.com/tensorchord/pgvecto.rs/commit/2b290b34e8ba69104ea2f800fa53328c6ed6c236) | kemingy |
| 2025-02-24 | [docs: add 'migrate to vectorchord' in readme (#640)](https://github.com/tensorchord/pgvecto.rs/commit/ca3e144d03fd9746e6f8aa22e74cf7901b47675e) | kemingy |
| 2025-02-24 | [chore: fix ghcr release (#639)](https://github.com/tensorchord/pgvecto.rs/commit/8ebab135a19bb3bb462973e9ffb5fb31564ef79a) | kemingy |
| 2025-02-24 | [chore: run rust test on ubuntu 22.04 (#638)](https://github.com/tensorchord/pgvecto.rs/commit/490fd2396d66cd9fcedac6a7904c54040bd982d8) | kemingy |
| 2025-02-24 | [feat: push docker image also to Github registry (#605)](https://github.com/tensorchord/pgvecto.rs/commit/0dccfb49d014e8979bd0b0e07a8b1738349ed6e9) | tobiasdiez |
| 2025-01-17 | [docs: fix discord and x badge (#632)](https://github.com/tensorchord/pgvecto.rs/commit/eb9fbaee145a6e772147ccd54c563eb73465646d) | kemingy |
| 2025-01-01 | [chore: Fix links (#627)](https://github.com/tensorchord/pgvecto.rs/commit/ae115754d96b670359aac5e82954256fe7089711) | gaocegege |
| 2024-11-21 | [fix: confict typmod for _vectors_cast_array_to_vecf32 (#617)](https://github.com/tensorchord/pgvecto.rs/commit/06e1c76898717e54a09ae2ae11247fc57c235f42) | cutecutecat |
| 2024-11-20 | [release: v0.4.0 (#615)](https://github.com/tensorchord/pgvecto.rs/commit/21656e4912c18980eb16176e8f754e68f0663cd9) | cutecutecat |
| 2024-11-20 | [Release enterprise ci (#613)](https://github.com/tensorchord/pgvecto.rs/commit/93e5cf4eb13d317111744a45969ac393a797447f) | xieydd |

[See all commits ↗](https://github.com/tensorchord/pgvecto.rs/commits)

## 👥 Top contributors

[usamoi](https://github.com/usamoi) (156) · [kemingy](https://github.com/kemingy) (36) · [VoVAllen](https://github.com/VoVAllen) (23) · [cutecutecat](https://github.com/cutecutecat) (23) · [silver-ymz](https://github.com/silver-ymz) (21)

## ⬇️ Get it

```bash
git clone https://github.com/tensorchord/pgvecto.rs.git
```
