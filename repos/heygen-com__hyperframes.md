# heygen-com/hyperframes

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/heygen-com/hyperframes)

> Write HTML. Render video. Built for agents.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖼 Image & video generation |
| **Project** | — |
| **Why it's worth a look** | HeyGen's framework: write HTML, render video — built for AI agents |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 84.1k |
| 🍴 **Forks** | 7.8k |
| 🐞 **Open issues + PRs** | [275](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.45](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.45) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 527.0 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.45](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.45)
<sub>2026-11-14 · today</sub>

> **HyperFrames v0.9.45**
> Released on 2026-11-14.
> A preview of 4K takes uses far less memory at full quality. Each 4K clip now plays a copy at the size the preview shows it, so long edits of 4K footage no longer run out of memory. Exports still use the original files.
> **Fixes**
> - **Core:** At full quality a 4K clip plays a copy at the size the preview shows it ([2f0ade181](https://github.com/heygen-com/hyperframes/commit/2f0ade181585323ebb2b53a2e15d68098655c90e), [#7723](https://github.com/heygen-com/hyperframes/pull/7723)).
> **Full changelog**
> …

### [v0.9.44](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.44)
<sub>2026-11-14 · today</sub>

> **HyperFrames v0.9.44**
> Released on 2026-11-14.
> Check now warns when text leaves the safe areas of a 9:16 social video. Previews free a clip's decoder once the playhead leaves it, and a cancelled audio fade no longer crashes the page. Set HYPERFRAMES_OWNER to tell which run started a leftover browser.
> **Features**
> - **CLI:** Name a caller's owner id on the browsers and warm check it starts ([798c241e4d0cf](https://github.com/heygen-com/hyperframes/commit/798c241e4d0cf18fc328d90c41823a766a9d8d8e), [#7687](https://github.com/heygen-com/hyperframes/pull/7687)).
> - **CLI:** Check warns when text leaves the 9:16 social safe areas ([45882027bd284](https://github.com/heygen-com/hyperframes/commit/45882027bd284a8fbd96ffe854184104304c224f), [#7680](https://github.com/heygen-com/hyperframes/pull/7680)).
> …

### [v0.9.43](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.43)
<sub>2026-11-13 · today</sub>

> **HyperFrames v0.9.43**
> Released on 2026-11-13.
> Renders on Windows no longer show coloured fringes around text, and previews open no audio device until a clip with sound plays. That second change ends long freezes on Windows. Drag and resize on an opaque preview now start from one read.
> **Features**
> - **Studio:** Drag and resize on an opaque preview start from one gesture-start read ([6bdf9291647f3](https://github.com/heygen-com/hyperframes/commit/6bdf9291647f3739e7d74fc34d304e46ba7141b7), [#7657](https://github.com/heygen-com/hyperframes/pull/7657)).
> **Fixes**
> …

### [v0.9.42](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.42)
<sub>2026-11-13 · today</sub>

> **HyperFrames v0.9.42**
> Released on 2026-11-13.
> Studio now says why a file cannot be saved when another program holds it open or it is read-only. Dragging and resizing a layer draw live over an opaque preview, local renders bring in only media, font, CSS and JS files from outside the project, and preparing fonts for large pages is faster.
> **Features**
> - **Studio:** Drag and resize draw live on an opaque preview over its channel ([87c4a07dc99a9](https://github.com/heygen-com/hyperframes/commit/87c4a07dc99a91e185c02a53090bdf941ff32db2), [#7646](https://github.com/heygen-com/hyperframes/pull/7646)).
> - **Studio:** Layers panel and marquee read an opaque preview over its channel ([be67089a80b59](https://github.com/heygen-com/hyperframes/commit/be67089a80b59be945d84e09d400a4ece254daef), [#7639](https://github.com/heygen-com/hyperframes/pull/7639)).
> …

### [v0.9.41](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.41)
<sub>2026-11-13 · yesterday</sub>

> **HyperFrames v0.9.41**
> Released on 2026-11-13.
> Fast capture works again on Chrome 157 and newer, which fixes Windows exports that failed at drawElementImage. Local renders keep Chrome's sandbox on where the host supports it and launch Chrome with only the environment it needs and explain a failed launch with the environment it had, cloud render --json lists the files an upload leaves out, publish copies only media, font, CSS and JS files from outside the project and leaves out the rest that came in with an import, a video variable given as a link now plays its sound once, media ids that differ only by case get separate folders so a render no longer fails with a missing file, and the Studio timeline and overlays read an opaque preview over its channel.
> **Features**
> - **CLI:** Cloud render --json lists the files an upload leaves out ([2591abfbf](https://github.com/heygen-com/hyperframes/commit/2591abfbf014c2f70fdc48ac315fd8acbd704e3d), [#7631](https://github.com/heygen-com/hyperframes/pull/7631)).
> - **Studio:** Read overlay geometry from an opaque preview over its channel ([faff4e16a](https://github.com/heygen-com/hyperframes/commit/faff4e16a8719c63234ac7a02fc3006ddf3cc375), [#7628](https://github.com/heygen-com/hyperframes/pull/7628)).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [fix(engine): an unrecognised capture failure is unknown, not the auth…](https://github.com/heygen-com/hyperframes/commit/ff9c3b7619c6c46c3145b287914cd09b377174f9) | miguel-heygen |
| 2026-11-14 | [chore: release v0.9.45 (#7729)](https://github.com/heygen-com/hyperframes/commit/fe8d93056cbec121367fc6cfd2dbcab0bc7f17ee) | miguel-heygen |
| 2026-11-14 | [fix(core): at full quality a 4K clip plays a copy at the size the pre…](https://github.com/heygen-com/hyperframes/commit/2f0ade181585323ebb2b53a2e15d68098655c90e) | miguel-heygen |
| 2026-11-14 | [chore: release v0.9.44 (#7708)](https://github.com/heygen-com/hyperframes/commit/58ef24c6d88634ff42f60b0435f3685ccfa2d459) | miguel-heygen |
| 2026-11-14 | [fix(cli): parse capture and grade-compare --timeout as a duration (#7…](https://github.com/heygen-com/hyperframes/commit/50c21c355aa2e2b5b5e8f203d4c38ce0bde6e6a3) | shurtado24 |
| 2026-11-14 | [docs(cli): list --format and the 24-worker cap in docs rendering (#7716)](https://github.com/heygen-com/hyperframes/commit/3e69d0dff038e4b72bef0fa9395649a68c26eeed) | shurtado24 |
| 2026-11-14 | [feat(studio): toasts show as a centred pill that rises in (#7714)](https://github.com/heygen-com/hyperframes/commit/690b07e4552fceacfc1d75af61d9ae1e1e6677d8) | miguel-heygen |
| 2026-11-14 | [fix(lint): say the audio overlap warning is about a shared Studio lan…](https://github.com/heygen-com/hyperframes/commit/3ce9ebeaf168a6d142fc259298214f9d35195a70) | wonjangcloud9 |
| 2026-11-14 | [fix(cli): quote the project name in init's printed `cd` commands (#7608)](https://github.com/heygen-com/hyperframes/commit/213f7c538305dc5773576eb92f45bc31f86a4ae6) | wonjangcloud9 |
| 2026-11-14 | [fix(cli): the render header names the quality preset and CRF it encod…](https://github.com/heygen-com/hyperframes/commit/2f31cc14b16b497641979e597637343e55302067) | wonjangcloud9 |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
