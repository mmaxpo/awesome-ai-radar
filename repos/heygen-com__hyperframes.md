# heygen-com/hyperframes

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/heygen-com/hyperframes)

> Open-source AI video editor: edit your own footage, or create and remake any video with Claude Code, Codex or the free Studio app. Write HTML, render MP4. By HeyGen.

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
| ⭐ **Stars** | 90.6k |
| 🍴 **Forks** | 8.4k |
| 🐞 **Open issues + PRs** | [318](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` `agent-skills` `ai-video` `ai-video-editor` `remotion-alternative` `video-editing` `video-generation` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.99](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.99) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 546.2 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.99](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.99)
<sub>2026-11-26 · today</sub>

> **HyperFrames v0.9.99**
> Released on 2026-11-26.
> Sealed previews now keep up with drags, presses and deletes like open ones, and Escape cancels a held drag. Fonts in dot-prefixed folders load in previews, renders and shares, and jumping while playing keeps the synced sound.
> **Fixes**
> - **Producer:** A frame coverage abort names the clip's source and window ([971499e9d](https://github.com/heygen-com/hyperframes/commit/971499e9d5e43e3915467f671e89a68e0f553be6), [#8828](https://github.com/heygen-com/hyperframes/pull/8828)).
> - **Studio:** A sealed move that rewrites no script rebinds in place instead of reloading the film ([274bc21ef](https://github.com/heygen-com/hyperframes/commit/274bc21efc7e74b8f9d77207e4644f5d6563478d), [#8814](https://github.com/heygen-com/hyperframes/pull/8814)).
> …

### [v0.9.98](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.98)
<sub>2026-11-26 · today</sub>

> **HyperFrames v0.9.98**
> Released on 2026-11-26.
> A project whose .hyperframes folder is deleted while it is open keeps recording edits again. A failed video extraction now shows FFmpeg's own reason, and a failed audio step or a cancel stops a sequential capture at once. A preview closed while it was reloading no longer holds up the next project's preview.
> **Fixes**
> - **Studio:** A closed preview never starts a reload it cannot show ([72a6e7bc7](https://github.com/heygen-com/hyperframes/commit/72a6e7bc7ddf3b4be3dd560d038284a5e96e60b8), [#8811](https://github.com/heygen-com/hyperframes/pull/8811)).
> - **Studio Server:** A history says at once that a folder whose id is gone was replaced ([7fcc0443f](https://github.com/heygen-com/hyperframes/commit/7fcc0443f1917d106c08e6bb2ce4090c355e1967), [#8891](https://github.com/heygen-com/hyperframes/pull/8891)).
> …

### [v0.9.97](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.97)
<sub>2026-11-26 · today</sub>

> **HyperFrames v0.9.97**
> Released on 2026-11-26.
> A sealed film's clip keeps its own effects and automation, and sealed previews show the text caret at screen size. Transcript-cut reads its parts back in the format it wrote, and a project's history does its folder work off Studio's main thread.
> **Features**
> - **CLI:** A start and end render that part of the film in any format, frame rate or HDR ([31dc4b80f](https://github.com/heygen-com/hyperframes/commit/31dc4b80f0eb5baa83292d780ea2d682e3eb698e), [#8878](https://github.com/heygen-com/hyperframes/pull/8878)).
> **Fixes**
> …

### [v0.9.96](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.96)
<sub>2026-11-25 · today</sub>

> **HyperFrames v0.9.96**
> Released on 2026-11-25.
> A sealed player plays its film's audio in Safari, and a drag right after a reload moves the element on screen. A page can no longer grow a render's script record or log without end, and lint reports a file it cannot parse instead of failing the run.
> **Features**
> - **Player:** A sealed player plays its film's audio from decoded buffers in Safari ([dd4f20d1b5](https://github.com/heygen-com/hyperframes/commit/dd4f20d1b5dc615bef9825ff9ac73041d7fd6f63), [#8636](https://github.com/heygen-com/hyperframes/pull/8636)).
> **Fixes**
> …

### [v0.9.95](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.95)
<sub>2026-11-25 · today</sub>

> **HyperFrames v0.9.95**
> Released on 2026-11-25.
> Studio opens a project without waiting on a slow drive, and a sealed preview keeps its timeline and selection box after a reload. Edits are written only to the file Studio mounted and only to HTML, and a file's markup can no longer steer them.
> **Features**
> - **Studio:** A sealed preview reports the shown display of every element a selector matches ([8008dc89f0](https://github.com/heygen-com/hyperframes/commit/8008dc89f078d748067b6e03524936b42c2defb3), [#8757](https://github.com/heygen-com/hyperframes/pull/8757)).
> **Fixes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [test(studio): the edit accuracy bench measures a sealed preview in it…](https://github.com/heygen-com/hyperframes/commit/7c217d9fdf3e32c628953f7325ddd90e0ff94392) | miguel-heygen |
| 2026-11-26 | [feat(studio): export shownPreviewFrame so hosts read the promoted pre…](https://github.com/heygen-com/hyperframes/commit/3152860f0810dde65f38750b26bd3e4fe737b60d) | miguel-heygen |
| 2026-11-26 | [fix(studio): the selection handles move with the box and the layer wh…](https://github.com/heygen-com/hyperframes/commit/fe711f7b43e4763d4cff8517c6aedf7d33529d30) | miguel-heygen |
| 2026-11-26 | [test(studio): the moved-project history test no longer fails at rando…](https://github.com/heygen-com/hyperframes/commit/36325eb49b2ff99d46c951b9ee06ca75b4f37841) | miguel-heygen |
| 2026-11-26 | [chore: release v0.9.99 (#8915)](https://github.com/heygen-com/hyperframes/commit/19238d88c8750149d303bbe821de2c4370dc0e28) | miguel-heygen |
| 2026-11-26 | [fix(producer): a frame coverage abort names the clip's source and win…](https://github.com/heygen-com/hyperframes/commit/971499e9d5e43e3915467f671e89a68e0f553be6) | miguel-heygen |
| 2026-11-26 | [fix(studio): a sealed move that rewrites no script rebinds in place i…](https://github.com/heygen-com/hyperframes/commit/274bc21efc7e74b8f9d77207e4644f5d6563478d) | miguel-heygen |
| 2026-11-26 | [fix(studio): a held canvas drag cancels on Escape or when the tab is …](https://github.com/heygen-com/hyperframes/commit/024d0637da09afc4823f64ddecb7a4f66bc47194) | miguel-heygen |
| 2026-11-26 | [fix(studio): a deleted clip's selection outline leaves with the clip …](https://github.com/heygen-com/hyperframes/commit/7d716974f469c39b731acdde5fac308fbbf0f7b4) | miguel-heygen |
| 2026-11-26 | [fix: load referenced dot-prefixed fonts in preview and rendering (#8905)](https://github.com/heygen-com/hyperframes/commit/3069ec8419b75eee06eeda6a0240705dc2cbf18a) | terencecho |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
