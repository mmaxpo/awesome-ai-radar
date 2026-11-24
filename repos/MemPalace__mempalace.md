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
| ⭐ **Stars** | 60.7k |
| 🍴 **Forks** | 7.7k |
| 🐞 **Open issues + PRs** | [841](https://github.com/MemPalace/mempalace/issues) |
| 💻 **Languages** | Python 94% · JavaScript 2% · Shell 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `chromadb` `llm` `mcp` `memory` `python` |
| 🕒 **Last activity** | 2026-11-23 (yesterday) |
| 📅 **Created** | 2026-04-05 |
| 📦 **Latest release** | [v3.12.0](https://github.com/MemPalace/mempalace/releases/tag/v3.12.0) — 2026-11-12 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 33.5 MB |
| 🌐 **Website** | http://mempalaceofficial.com/ |

## 📦 Recent releases

### [v3.12.0](https://github.com/MemPalace/mempalace/releases/tag/v3.12.0) — v3.12.0 — verbatim mining, recoverable writes
<sub>2026-11-12 · 12d ago</sub>

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
<sub>2026-08-23 · 3mo ago</sub>

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
| 2026-11-23 | [Merge pull request #2533 from ariannamethod/fix/convo-source-snapshot](https://github.com/MemPalace/mempalace/commit/dfa318af2d41ad6c64fc3b08c28d16410c9b634b) | igorls |
| 2026-11-23 | [Merge pull request #2436 from BuboTheWise/fix/2413-process-scoped-wri…](https://github.com/MemPalace/mempalace/commit/988bb9a4c783333550f1c3717c44e08af13ed7c3) | igorls |
| 2026-11-23 | [Merge pull request #2507 from potterdigital/docs/macos-launchagent-pr…](https://github.com/MemPalace/mempalace/commit/f4b7fdea773e9a6fe2268a373344c9ea43166608) | igorls |
| 2026-11-23 | [Merge pull request #3048 from jayzhou2309/fix/sqlite-exact-bulk-paren…](https://github.com/MemPalace/mempalace/commit/81b8153ebbe135917402097d0c9fadea669fd7b3) | igorls |
| 2026-11-23 | [Merge pull request #3006 from MemPalace/dependabot/github_actions/act…](https://github.com/MemPalace/mempalace/commit/8eb77266b89be832b57581dbc5745dbe88125483) | igorls |
| 2026-11-23 | [Merge pull request #3005 from MemPalace/dependabot/github_actions/doc…](https://github.com/MemPalace/mempalace/commit/16d13e4aec31de01ba072ef37f84217d1e264a3e) | igorls |
| 2026-11-22 | [fix(sqlite_exact): join parent-key lookups with UNION ALL](https://github.com/MemPalace/mempalace/commit/d4a0bf808615e183aa7e26f337c3ec613c36f0b0) | jayzhou2309 |
| 2026-11-22 | [fix(kg): harden KnowledgeGraph for multi-process SQLite access (#948)](https://github.com/MemPalace/mempalace/commit/b2ef8fed22f53b48acbda1ffebac040cb8a22f69) | felipecpaiva |
| 2026-11-21 | [fix(test): update test for per-request lease lifecycle — address igor…](https://github.com/MemPalace/mempalace/commit/e739519191d46c0e3e74064dce6c39ff3f064fb6) | BuboTheWise |
| 2026-11-20 | [fix(convos): bound source reads and preserve other wings during remine](https://github.com/MemPalace/mempalace/commit/daef478210496a4f1438db1f49e90ad4900ca43c) | ariannamethod |

[See all commits ↗](https://github.com/MemPalace/mempalace/commits)

## ⬇️ Get it

```bash
git clone https://github.com/MemPalace/mempalace.git
```
