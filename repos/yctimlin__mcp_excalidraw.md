# yctimlin/mcp_excalidraw

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/yctimlin/mcp_excalidraw)

> MCP server and Claude Code skill for Excalidraw — programmatic canvas toolkit to create, edit, and export diagrams via AI agents with real-time canvas sync.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔌 MCP & SDKs |
| **Project** | — |
| **Why it's worth a look** | Excalidraw MCP server: agents draw diagrams |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 2.6k |
| 🍴 **Forks** | 298 |
| 🐞 **Open issues + PRs** | [39](https://github.com/yctimlin/mcp_excalidraw/issues) |
| 💻 **Languages** | TypeScript 73% · JavaScript 26% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-10 (4d ago) |
| 📅 **Created** | 2025-03-16 |
| 📦 **Latest release** | [v2.2.0](https://github.com/yctimlin/mcp_excalidraw/releases/tag/v2.2.0) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3.6 MB |
| 🌐 **Website** | https://mcp-excalidraw-landing.vercel.app/ |

## 📦 Recent releases

### [v2.2.0](https://github.com/yctimlin/mcp_excalidraw/releases/tag/v2.2.0)
<sub>2026-11-10 · 4d ago</sub>

> **Features**
> - **Act on the selection:** `get_selection` (MCP) and `selection` (CLI) return the IDs selected in the most recently active canvas tab. (#149, thanks @Totopo27; requested in #147 by @fgeierst)
> - **Editable PNGs:** export a PNG with the scene embedded (`--embed-scene` / `embedScene: true`, PNG only, off by default) and import or `render` it later. One `.excalidraw.png` file is both the README preview and the editable source. (#132, thanks @FortniteGamer747)
> - **Durable canvas (opt-in):** set `EXCALIDRAW_DATA_DIR` to keep elements, image files and named snapshots across canvas restarts. Each change is saved to disk before it is acknowledged, and one process owns the directory at a time. Unset, nothing changes. (#130, thanks @IndelibleVivi; #133)
> - **Self-hosted share links:** `share` / `export_to_excalidraw_url` can upload to your own Excalidraw instance via `EXCALIDRAW_SHARE_UPLOAD_URL` and `EXCALIDRAW_SHARE_BASE_URL`. Defaults still go to excalidraw.com. (#138, thanks @j2ali)
> **Fixes**
> …

### [v2.1.2](https://github.com/yctimlin/mcp_excalidraw/releases/tag/v2.1.2)
<sub>2026-10-04 · 1mo ago</sub>

> **Fixes**
> - **Snapshot restore and import are atomic:** a rejected restore or replace-import no longer wipes the canvas. Native frames now restore, import, export and can be created through the CLI and MCP. (#101, thanks @sanjayy0612; #120)
> - **One label per shape:** updating or renaming a labelled shape while a canvas tab is open no longer stacks duplicate labels. (#121, thanks @sdrshn-nmbr)
> - **Dropped images survive reload:** the tab uploads image files on sync (only new ones), so they persist and appear in exports and headless screenshots. (#122, thanks @appdesigngeeks)
> - **No more clipped text:** the canvas tab loads Excalidraw's fonts before sizing text, so labels and text fit their boxes. (#123, #124)
> Also: the README was audited end to end against the code (headless screenshots, network use, environment variables, frames, tests).
> …

### [v2.1.1](https://github.com/yctimlin/mcp_excalidraw/releases/tag/v2.1.1)
<sub>2026-10-04 · 1mo ago</sub>

> **Fixes**
> - **Exports always load:** valid order keys, so saved scenes with more than about 45 labelled shapes no longer fail with `invalid order key`. Free text exports left/top aligned, like the canvas. (#115, thanks @fernandovmacedo)
> - **No more drift on sync:** center- and right-aligned text, labels on arrows, and arrows no longer move or shrink each time an open canvas tab syncs. Text `x`/`y` is always the top-left corner. (#116, thanks @hidinginabunker)
> - **Canvas library:** installs from libraries.excalidraw.com work, the library persists across reloads, and labels re-wrap when their shape is resized through the API. (#113, thanks @lukemariano)
> ```
> npx -y mcp-excalidraw-server@2.1.1
> …

### [v2.1.0](https://github.com/yctimlin/mcp_excalidraw/releases/tag/v2.1.0) — v2.1.0 — Headless Rendering
<sub>2026-10-03 · 1mo ago</sub>

> **What's Changed**
> * Dev by @yctimlin in https://github.com/yctimlin/mcp_excalidraw/pull/11
> * Support windows by @PhantomPayne in https://github.com/yctimlin/mcp_excalidraw/pull/13
> * Fix MCP delete/update methods and add frontend sync functionality by @Songmengdi in https://github.com/yctimlin/mcp_excalidraw/pull/19
> * Dev by @yctimlin in https://github.com/yctimlin/mcp_excalidraw/pull/21
> * docs: set figure aligned by @ctchen222 in https://github.com/yctimlin/mcp_excalidraw/pull/25
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-10 | [chore: release 2.2.0 (#151)](https://github.com/yctimlin/mcp_excalidraw/commit/81720ac819d2325177cd6137c6ad41d52d0f5374) | yctimlin |
| 2026-11-10 | [feat: expose current canvas selection via MCP get_selection and CLI (…](https://github.com/yctimlin/mcp_excalidraw/commit/678b5cac0edd8a9c061580db77a5f793d5c1be97) | Totopo27 |
| 2026-10-30 | [fix(mcp): resolve symlinks and restrict file types for MCP file tools…](https://github.com/yctimlin/mcp_excalidraw/commit/66b768b47914987bb77a49e1fd1922e7f6deb0fe) | yctimlin |
| 2026-10-30 | [docs: clarify MCP transport and remote canvas setup (#144)](https://github.com/yctimlin/mcp_excalidraw/commit/a0d01f294e5969a6c347dbaed45f80f2533ee14a) | IndelibleVivi |
| 2026-10-30 | [fix: keep dark theme after copy link, copy as SVG and wrap in frame (…](https://github.com/yctimlin/mcp_excalidraw/commit/ce5c6bbaa3e59bc769f4a9764e65fea3a7d25a83) | tomerSP |
| 2026-10-30 | [fix: resolve ?element= links after the server scene loads (#141)](https://github.com/yctimlin/mcp_excalidraw/commit/f4c4196ef711192b3688efdba74e5d5f106e7462) | tomerSP |
| 2026-10-30 | [fix: stop idle autosync loop after a single click (#142)](https://github.com/yctimlin/mcp_excalidraw/commit/d5a24a14153f04adc55d118d43f55f5a27e6ecdc) | tomerSP |
| 2026-10-22 | [feat: configurable share target for self-hosted Excalidraw (#138)](https://github.com/yctimlin/mcp_excalidraw/commit/774a70c1b3f0c7b9901fbbbf66b432d1a8dbbfe7) | j2ali |
| 2026-10-22 | [docs: clarify snapshot persistence defaults (#140)](https://github.com/yctimlin/mcp_excalidraw/commit/3e984241fb7c20530d08c0f1a2458483d6f5c7ab) | IndelibleVivi |
| 2026-10-09 | [perf(docker): shrink MCP and canvas images by ~70-80% (#112)](https://github.com/yctimlin/mcp_excalidraw/commit/8084a1c8b410d625fcfd59d5cffb32f3a86a2a6f) | hermes-carpet |

[See all commits ↗](https://github.com/yctimlin/mcp_excalidraw/commits)

## ⬇️ Get it

```bash
git clone https://github.com/yctimlin/mcp_excalidraw.git
```
