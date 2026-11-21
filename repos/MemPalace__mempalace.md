# MemPalace/mempalace

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/MemPalace/mempalace)

> The best-benchmarked open-source AI memory system. And it's free.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | TCOS |
| **Why it's worth a look** | Top-benchmarked open-source AI memory system |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 60.6k |
| 🍴 **Forks** | 7.7k |
| 🐞 **Open issues + PRs** | [838](https://github.com/MemPalace/mempalace/issues) |
| 💻 **Languages** | Python 94% · JavaScript 2% · Shell 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `chromadb` `llm` `mcp` `memory` `python` |
| 🕒 **Last activity** | 2026-11-20 (yesterday) |
| 📅 **Created** | 2026-04-05 |
| 📦 **Latest release** | [v3.12.0](https://github.com/MemPalace/mempalace/releases/tag/v3.12.0) — 2026-11-12 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 33.2 MB |
| 🌐 **Website** | http://mempalaceofficial.com/ |

## 📦 Recent releases

### [v3.12.0](https://github.com/MemPalace/mempalace/releases/tag/v3.12.0) — v3.12.0 — verbatim mining, recoverable writes
<sub>2026-11-12 · 9d ago</sub>

> MemPalace 3.12 keeps source text and bytes intact, makes interrupted re-mines recoverable, and cuts the work needed to maintain large palaces. Timestamps and project wings now follow the same rules across tools and hooks. Antigravity gains a visual Palace explorer, and the final release review fixes graph identity collisions, concurrent checkpoint duplicates, document filtering, and newest-first pagination.
> **Upgrade notes**
> - **Python 3.10 or newer is required.** Python 3.9 is no longer supported; native wheels use the Python 3.10+ ABI.
> - **The next mine re-reads each source it covers once.** Normalization version 3 picks up the parsing and byte-preservation fixes. Drawers whose text is unchanged reuse their stored vectors; unchanged files keep their closets and AAAK summaries. Sources no longer on disk keep their existing drawers. Back up a large palace before upgrading and allow time for this first pass. ([#2813](https://github.com/MemPalace/mempalace/pull/2813))
> - **Hallways migrate to SQLite on the first hallway write.** `hallways.json` is imported transactionally into `hallways.sqlite3` and retained under an `.imported-*` name. Upgrade every installation sharing the palace, since older versions keep writing the old JSON file. After a downgrade, rebuild derived hallways with `mempalace hallways --rebuild`. ([#2895](https://github.com/MemPalace/mempalace/pull/2895))
> - **New timestamps carry an explicit UTC offset.** Legacy naive timestamps are read as local time, as they were written; existing metadata is not rewritten. Date-only filters still mean local calendar dates. Project wings also use one slug rule across CLI, MCP, mining and hooks; filters continue finding stored legacy spellings. ([#2851](https://github.com/MemPalace/mempalace/pull/2851), [upgrade details](https://github.com/MemPalace/mempalace/blob/main/CHANGELOG.md#upgrade-notes))
> …

### [v3.11.0](https://github.com/MemPalace/mempalace/releases/tag/v3.11.0) — v3.11.0 — audit, repair and opt-in EmbeddingGemma 2
<sub>2026-10-14 · 1mo ago</sub>

> A palace can now be audited and repaired in guided steps, and EmbeddingGemma 2 arrives as an opt-in embedder with native image, audio and video search. Every palace records the embedding model that built it and refuses to open with a different one. Conversation mining stops discarding text, status, search, wake-up and hub mines stay responsive on large palaces, and a round of correctness fixes from the 3.11 review hardens metadata updates, recovery and HTTP validation.
> **Upgrade notes**
> - **The first conversation mine after upgrading re-mines each conversation file it covers, once.** The exchange chunker no longer discards text (#2591), so conversation drawers filed before 3.11 count as stale and are re-chunked and re-embedded from transcripts still on disk; transcripts no longer on disk keep their drawers. Project files are not re-mined. Expect roughly 40 minutes to 3 hours per million drawers, depending on hardware. On a large palace, back up first and run it in batches at a quiet time, for example `mempalace mine <dir> --mode convos --limit 200`; an interrupted run resumes where it stopped.
> - **A palace refuses to open with a different embedding model than the one that built it.** Search, mining and MCP writes stop with a message that names the fix: set `embedding_model` (`config.json` or `MEMPALACE_EMBEDDING_MODEL`) back to the model the palace was built with, or re-embed with `mempalace repair rebuild-index`. A palace with no recorded model opens with the configured one and a warning that names `mempalace palace set-embedder`. (#2694, #2717)
> - **`EntityRegistry.research()` and `confirm_research()` are removed.** They were an opt-in, off-by-default Wikipedia lookup that nothing in the CLI, MCP server, miners or hooks called. Existing `wiki_cache` entries in `entities.json` are still read by `lookup()`. (GHSA-mrj5)
> **EmbeddingGemma 2 and embedder identity**
> …

### [v3.10.0](https://github.com/MemPalace/mempalace/releases/tag/v3.10.0) — v3.10.0 — lighter ways in for agents
<sub>2026-09-16 · 2mo ago</sub>

> Agents get lighter ways in: a 3-tool MCP server with Palace Query Language, shared-brain rules for `host:harness:project` identities, and optional native exact-vector search. New installs follow XDG, and storage fixes close a silent write-loss path, a macOS integrity refusal and several hangs.
> **Upgrade notes**
> - **`mempalace rules` no longer accepts `--agent`.** Pass `--host`, `--harness` and `--project`, then re-render any installed shared-brain block. (#2508)
> - **`get_collection()` refuses names MemPalace never reads.** Any name other than the configured drawers collection or `mempalace_closets` raises `CollectionNameMismatchError`; maintenance scripts can pass `_skip_name_check=True`. (#2446)
> - **The MCP event listing returns the newest events first when no cursor is given.** `mempalace_event_list` and `palace_coordinate` now default to newest-first unless `since_event_id` or `order` is passed; `mempalace logstream list` and `Logstream.list_events()` still default to oldest-first. (#2497)
> - **New installs keep config and palace under `~/.config/mempalace`** (or `$XDG_CONFIG_HOME/mempalace`). Existing `~/.mempalace` installs are unchanged. (#148)
> …

### [v3.9.0](https://github.com/MemPalace/mempalace/releases/tag/v3.9.0) — v3.9.0 — one hub for every agent
<sub>2026-08-31 · 2mo ago</sub>

> **v3.9.0 — one hub for every agent**
> One hub now serves every agent. CLI search reuses the live palace index instead of loading another multi-gigabyte HNSW copy, concurrent searches stop blocking each other, and skill-first coordination plus opt-in release awareness make shared-brain fleets easier to operate safely.
> **Shared hub and search**
> - **`mempalace search` reuses a healthy live Hub.** On the reported 4.99-million-vector palace, two direct CLI searches held about 18.6 GB of private RSS. Forwardable searches now reuse the Hub collection while preserving filters, ranking, output, authentication, configuration negotiation, and safe fallback behavior. (#2379)
> - **Hub reads run concurrently.** Searches no longer serialize behind one exclusive HTTP dispatch lock; reads share a writer-preferring lock while mutations remain exclusive. (#2398)
> - **Search results are clearer and faster to enrich.** Public similarity is the raw vector score, closet boost remains in effective ranking, source lookups are indexed, and duplicate enriched passages are removed. (#2399, #2143)
> …

### [v3.8.0](https://github.com/MemPalace/mempalace/releases/tag/v3.8.0) — v3.8.0 — fast large palaces, lean MCP proxies, wakeable agents
<sub>2026-08-23 · 2mo ago</sub>

> **v3.8.0 — fast large palaces, lean MCP proxies, wakeable agents**
> Large palaces get fast and stay small in 3.8.0. Chroma metadata tools no longer cold-load HNSW, `sqlite_exact` stops scanning and hydrating the whole palace for common reads, long-running Chroma servers stop rebuilding their client on their own writes, and proxied MCP sessions no longer import a storage stack they never use. Agents also gain a persistent `logstream watch` primitive so coordination can wake a harness instead of relying on repeated five-minute waits.
> **Performance**
> - **Chroma metadata reads skip the vector index.** On a 1.7 GB / 165k-drawer palace, wing-scoped `list_drawers(limit=20)` fell from **2.31 s and 1148 MB peak RSS to 0.01 s and 86 MB**. `list_drawers` and tunnel reads now query Chroma's SQLite metadata directly, push filters into SQL, and hydrate only the requested previews. (#2314)
> - **`sqlite_exact` common reads no longer walk the whole palace.** On a live 167k-drawer / 166k-closet palace, `mempalace_status` fell from **6997 ms to 1045 ms** and warm `mempalace_search` from **6364 ms to 210–1600 ms**. Vector ranking is batched and cached, top-k documents are hydrated afterward, equality filters paginate in SQL, taxonomy results are cached, and `wing` / `room` / `hall` gain indexed generated columns without rewriting the 1.6 GB embedding table. (#2308, #2311, #2313)
> - **Long-running Chroma servers stay flat instead of reloading HNSW on their own writes.** Across eight searches, measured RSS changed from **951 MB → 3522 MB before** to **940 MB → 965 MB after**. Replaced clients are closed, while genuine external database changes still trigger a rebuild. (#2307)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [Merge pull request #3031 from MemPalace/chore/changelog-backfill-blas…](https://github.com/MemPalace/mempalace/commit/51717e00dd6e12ed2200552afb9504bb7c480955) | igorls |
| 2026-11-20 | [docs(changelog): backfill unreleased entries and fix the 3.12.0 date](https://github.com/MemPalace/mempalace/commit/b8e2a81f26fe65c2b4fe10419227873b1f9dd7c3) | igorls |
| 2026-11-20 | [fix(perf): cap BLAS threads in server entry points, not at import](https://github.com/MemPalace/mempalace/commit/c201f7091b1cefda77b25d46da058a4c4e6e803c) | igorls |
| 2026-11-19 | [Merge pull request #3032 from MemPalace/fix/ci-flakes-node-hooks-watc…](https://github.com/MemPalace/mempalace/commit/358e25cd1aa466252ac41c1284362318e9fc1c81) | igorls |
| 2026-11-19 | [Merge pull request #3016 from MemPalace/fix/remine-preserve-prior-text](https://github.com/MemPalace/mempalace/commit/24d3d9048e22b2b58b55b1a920e0bc9b9dd03457) | igorls |
| 2026-11-19 | [test(miner): synchronize the armed watchdog test with a handshake (#3…](https://github.com/MemPalace/mempalace/commit/f379ed49ee4d092f988d2a96fbdee57994786e01) | igorls |
| 2026-11-19 | [test(antigravity): start Node once per module for hook-common probes](https://github.com/MemPalace/mempalace/commit/f974e1b9c1807413c6c3e73b5b7c963f5695d35a) | igorls |
| 2026-11-19 | [docs(changelog): re-mine journal and owner-scoped prunes](https://github.com/MemPalace/mempalace/commit/8dc627de15fd98d84a092657a4b8c777036203d4) | igorls |
| 2026-11-19 | [test(mine): a journal failing on the second upsert batch loses nothing](https://github.com/MemPalace/mempalace/commit/700717cefb4ede2ec409cbbfaf953d4388ab9ec9) | igorls |
| 2026-11-19 | [fix(revisions): keep the palace directory 0700 when the journal creat…](https://github.com/MemPalace/mempalace/commit/2745bc796060d7da96316ba14b817580987961b5) | igorls |

[See all commits ↗](https://github.com/MemPalace/mempalace/commits)

## ⬇️ Get it

```bash
git clone https://github.com/MemPalace/mempalace.git
```
