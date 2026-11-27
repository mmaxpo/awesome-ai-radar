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
| ⭐ **Stars** | 91.3k |
| 🍴 **Forks** | 8.5k |
| 🐞 **Open issues + PRs** | [324](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` `agent-skills` `ai-video` `ai-video-editor` `remotion-alternative` `video-editing` `video-generation` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.102](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.102) — 2026-11-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 548.4 MB |
| 🌐 **Website** | https://hyperframes.studio |

## 📦 Recent releases

### [v0.9.102](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.102)
<sub>2026-11-27 · today</sub>

> **HyperFrames v0.9.102**
> Released on 2026-11-27.
> Studio stays responsive when a preview asks for paused frames or the disk holding a history lock stops answering. The CLI reports EPIPE crashes from browser pipes, and core starts safely when the page has no body yet.
> **Fixes**
> - **CLI:** Report non-stdio EPIPE crashes and guard launched browser pipes ([bd477dc45](https://github.com/heygen-com/hyperframes/commit/bd477dc45215c70d98879bb5f3cb9f170184e7e9), [#8949](https://github.com/heygen-com/hyperframes/pull/8949)).
> - **Studio Server:** A history lock on a disk that stops answering no longer freezes the app ([281db3bd6](https://github.com/heygen-com/hyperframes/commit/281db3bd6dfd0cb914f44c3bcfd6f752c86d9c4f), [#8948](https://github.com/heygen-com/hyperframes/pull/8948)).
> …

### [v0.9.101](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.101)
<sub>2026-11-26 · today</sub>

> **HyperFrames v0.9.101**
> Released on 2026-11-26.
> Studio's crop frame, rotate handle and group outlines now move with the selection, and hosts can measure the preview stage. Renders read the right CPU quota and probe inline audio correctly.
> **Features**
> - **Core:** Measure preview stage layout and styles over the editing port ([f00e93479](https://github.com/heygen-com/hyperframes/commit/f00e93479546eca4c7d841859174fe32d53b2564), [#8937](https://github.com/heygen-com/hyperframes/pull/8937)).
> **Fixes**
> …

### [v0.9.100](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.100)
<sub>2026-11-26 · today</sub>

> **HyperFrames v0.9.100**
> Released on 2026-11-26.
> Sealed group moves, resizes and rotations now update the preview right away, and selection outlines and handles stay lined up while dragging. Studio also stays responsive on oversized preview replies and logs whether a failed preview reload came from the project or Studio.
> **Features**
> - **Studio:** Export shownPreviewFrame so hosts read the promoted preview frame ([3152860f0](https://github.com/heygen-com/hyperframes/commit/3152860f0810dde65f38750b26bd3e4fe737b60d), [#8917](https://github.com/heygen-com/hyperframes/pull/8917)).
> **Fixes**
> …

### [v0.9.99](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.99)
<sub>2026-11-26 · yesterday</sub>

> **HyperFrames v0.9.99**
> Released on 2026-11-26.
> Sealed previews now keep up with drags, presses and deletes like open ones, and Escape cancels a held drag. Fonts in dot-prefixed folders load in previews, renders and shares, and jumping while playing keeps the synced sound.
> **Fixes**
> - **Producer:** A frame coverage abort names the clip's source and window ([971499e9d](https://github.com/heygen-com/hyperframes/commit/971499e9d5e43e3915467f671e89a68e0f553be6), [#8828](https://github.com/heygen-com/hyperframes/pull/8828)).
> - **Studio:** A sealed move that rewrites no script rebinds in place instead of reloading the film ([274bc21ef](https://github.com/heygen-com/hyperframes/commit/274bc21efc7e74b8f9d77207e4644f5d6563478d), [#8814](https://github.com/heygen-com/hyperframes/pull/8814)).
> …

### [v0.9.98](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.98)
<sub>2026-11-26 · yesterday</sub>

> **HyperFrames v0.9.98**
> Released on 2026-11-26.
> A project whose .hyperframes folder is deleted while it is open keeps recording edits again. A failed video extraction now shows FFmpeg's own reason, and a failed audio step or a cancel stops a sequential capture at once. A preview closed while it was reloading no longer holds up the next project's preview.
> **Fixes**
> - **Studio:** A closed preview never starts a reload it cannot show ([72a6e7bc7](https://github.com/heygen-com/hyperframes/commit/72a6e7bc7ddf3b4be3dd560d038284a5e96e60b8), [#8811](https://github.com/heygen-com/hyperframes/pull/8811)).
> - **Studio Server:** A history says at once that a folder whose id is gone was replaced ([7fcc0443f](https://github.com/heygen-com/hyperframes/commit/7fcc0443f1917d106c08e6bb2ce4090c355e1967), [#8891](https://github.com/heygen-com/hyperframes/pull/8891)).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [fix(studio-server): cached waveform and preview reads never hold the …](https://github.com/heygen-com/hyperframes/commit/32ec0b9835fddf4a58ac3d754cf27284dd784374) | miguel-heygen |
| 2026-11-27 | [fix(studio): a sealed canvas drag keeps its drop when the keyboard mo…](https://github.com/heygen-com/hyperframes/commit/b4f47cec1f0fc6ac1dff91de597423b7edc460c5) | miguel-heygen |
| 2026-11-27 | [feat(core): a frame-presented wait can be asked to run longer, up to …](https://github.com/heygen-com/hyperframes/commit/4c92e37a708662240c1a96d53d0565332a1aea8d) | miguel-heygen |
| 2026-11-27 | [feat(parsers): export the size the renderer compiles a composition at…](https://github.com/heygen-com/hyperframes/commit/a7cca1a2e47e7275de366623508e1cb075fa717f) | miguel-heygen |
| 2026-11-27 | [test(cli): the skills git-folder test runs git without the lookup's 4…](https://github.com/heygen-com/hyperframes/commit/32274984f8e189ae471f1c962650ed910fb29933) | miguel-heygen |
| 2026-11-27 | [fix(core): the preview runtime's editing port ignores later changes t…](https://github.com/heygen-com/hyperframes/commit/23f665d0a2dd62dbd00a8e8eb51cd7d8e74a8279) | miguel-heygen |
| 2026-11-27 | [fix(studio): sealed previews start loading as fast as open ones (#8972)](https://github.com/heygen-com/hyperframes/commit/407c0efb7dd82dfff8e5ad7dcf1404fa643ff9fb) | miguel-heygen |
| 2026-11-27 | [fix(studio): a timeline clip loads media only from its own project's …](https://github.com/heygen-com/hyperframes/commit/413d37badb84f29db4a463800753c3d703c9eb21) | miguel-heygen |
| 2026-11-27 | [fix(parsers): css parsing ignores source-map comments in the styleshe…](https://github.com/heygen-com/hyperframes/commit/626644b2da0ed86fe542264f3757e994ddf0fb11) | miguel-heygen |
| 2026-11-27 | [docs: redirect renamed catalog items and moved guides to their curren…](https://github.com/heygen-com/hyperframes/commit/1cb750bbae3ab2aaecc19f300d8cc2a55adab08b) | ukimsanov |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
