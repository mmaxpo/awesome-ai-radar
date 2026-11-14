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
| ⭐ **Stars** | 84.2k |
| 🍴 **Forks** | 7.8k |
| 🐞 **Open issues + PRs** | [284](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.46](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.46) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 527.3 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.46](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.46)
<sub>2026-11-14 · today</sub>

> **HyperFrames v0.9.46**
> Released on 2026-11-14.
> Editing a project file that is read-only is now refused, and the file stays as it was. A capture failure the engine does not recognise is now reported as unknown, not blamed on the project.
> **Fixes**
> - **Studio Server:** An edit to a read-only project file is refused and leaves it unchanged ([b5e9bc689](https://github.com/heygen-com/hyperframes/commit/b5e9bc6893a7a5b4ab306151c362f46b1b24e4e1), [#7731](https://github.com/heygen-com/hyperframes/pull/7731)).
> - **Engine:** An unrecognised capture failure is unknown, not the author's fault ([ff9c3b761](https://github.com/heygen-com/hyperframes/commit/ff9c3b7619c6c46c3145b287914cd09b377174f9), [#7730](https://github.com/heygen-com/hyperframes/pull/7730)).
> …

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [fix(scripts): the comment check names a git too old for check-attr --…](https://github.com/heygen-com/hyperframes/commit/8e0f196a8b151f02adbf2f2a96e13f9d6b9f2908) | miguel-heygen |
| 2026-11-14 | [fix(engine): hold the render page to the asset download address rules…](https://github.com/heygen-com/hyperframes/commit/29533f631fdfd3b5bd733319de49d2a97c1fbf3f) | miguel-heygen |
| 2026-11-14 | [fix(producer): a clip whose file name has a space or accent is mixed …](https://github.com/heygen-com/hyperframes/commit/a3fa250b25c7c42dedaf4b19b5df65d80260cc65) | miguel-heygen |
| 2026-11-14 | [fix(studio-server): save an edit Windows briefly holds without freezi…](https://github.com/heygen-com/hyperframes/commit/a92498b9033a069418940fe54360e172968381e4) | miguel-heygen |
| 2026-11-14 | [fix(cli): an unknown flag's error leaves out hidden rename shims (#7746)](https://github.com/heygen-com/hyperframes/commit/cb52dcf646b8c0a413ce80c99fb6719ad452a2c1) | miguel-heygen |
| 2026-11-14 | [fix: check, render and downloads work on a drive without hard links (…](https://github.com/heygen-com/hyperframes/commit/b746a0ee1389895b861b7177e226df3622d09bd4) | miguel-heygen |
| 2026-11-14 | [fix(studio): HEVC with long-term reference pictures keeps its pixel a…](https://github.com/heygen-com/hyperframes/commit/b7238744624b49fc2a54cb7cd5c9c73b6004f92e) | miguel-heygen |
| 2026-11-14 | [fix(cli): check still reports a film's other GL driver notes (#7745)](https://github.com/heygen-com/hyperframes/commit/d26ec25385630f2427079c65bb300f0e12f26661) | miguel-heygen |
| 2026-11-14 | [fix(cli): an unknown flag lists the command's real flags (#7740)](https://github.com/heygen-com/hyperframes/commit/88beb282f26cd9c8eaa6381e477336e1a3971d65) | miguel-heygen |
| 2026-11-14 | [fix(registry): caption-highlight clears a short word's highlight when…](https://github.com/heygen-com/hyperframes/commit/e21e64f6ab51f9024f9c0fe0d1acb39553887c99) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
