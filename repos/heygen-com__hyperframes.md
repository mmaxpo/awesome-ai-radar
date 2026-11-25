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
| ⭐ **Stars** | 90.0k |
| 🍴 **Forks** | 8.4k |
| 🐞 **Open issues + PRs** | [332](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` `agent-skills` `ai-video` `ai-video-editor` `remotion-alternative` `video-editing` `video-generation` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.94](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.94) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 545.6 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.94](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.94)
<sub>2026-11-25 · today</sub>

> **HyperFrames v0.9.94**
> Released on 2026-11-25.
> You can render one part of a film in a single pass, in any format and frame rate, with HDR video and shader transitions. Project files, media paths and captured videos stay inside the project, and code that reads media input options by position works again.
> **Features**
> - **Studio Server:** The render route renders a part of the film when asked for a start and end ([d2d527952](https://github.com/heygen-com/hyperframes/commit/d2d527952b7f551185d460f1c1b1e194971727c1), [#8787](https://github.com/heygen-com/hyperframes/pull/8787)).
> - **Producer:** Render a part of the film with HDR video or shader transitions ([66aba4c7a](https://github.com/heygen-com/hyperframes/commit/66aba4c7a0b7475d964d22ae2491d22d7e89fb48), [#8802](https://github.com/heygen-com/hyperframes/pull/8802)).
> …

### [v0.9.93](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.93)
<sub>2026-11-25 · today</sub>

> **HyperFrames v0.9.93**
> Released on 2026-11-25.
> Telemetry turns off the same way everywhere with DO_NOT_TRACK or HYPERFRAMES_NO_TELEMETRY, and a cached whisper model is used only when its checksum matches. Media commands and playlists read only local, self-contained inputs, and auto GPU mode picks software rendering when it is faster.
> **Fixes**
> - **Studio:** Words selected in a sealed text edit show the formatting toolbar, as unsealed ([d4edc6d14f](https://github.com/heygen-com/hyperframes/commit/d4edc6d14faa62a7d9c6b3adb4aeb8b868ba6648), [#8777](https://github.com/heygen-com/hyperframes/pull/8777)).
> - **CLI:** A cached whisper model is used only once its sha256 matches its pin ([5c4f5febbc](https://github.com/heygen-com/hyperframes/commit/5c4f5febbcd7e4493542d2d7465c0ff46af4b807), [#8762](https://github.com/heygen-com/hyperframes/pull/8762)).
> …

### [v0.9.92](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.92)
<sub>2026-11-25 · today</sub>

> **HyperFrames v0.9.92**
> Released on 2026-11-24.
> A Studio rename now names the files it left on the old path, and sealed previews save moves and resizes like unsealed ones. Renders no longer stop on a URL Node cannot parse, and local media, LUT paths and pasted edits stay where they belong.
> **Features**
> - **Core:** A sealed preview answers a text toolbar's authored styles and fonts ([36d576395](https://github.com/heygen-com/hyperframes/commit/36d57639584d0534c32e816c87d9baf2a1683fd0), [#8761](https://github.com/heygen-com/hyperframes/pull/8761)).
> - **Studio:** Long audio keeps its fx and beats, read from the server, no page OOM ([630409ca1](https://github.com/heygen-com/hyperframes/commit/630409ca19e13bf3400d1d2180bc8c14932970b7), [#8622](https://github.com/heygen-com/hyperframes/pull/8622)).
> …

### [v0.9.91](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.91)
<sub>2026-11-24 · today</sub>

> **HyperFrames v0.9.91**
> Released on 2026-11-24.
> Local voice and tts now speak a narration line as written. Tts replaces a link at its output name with the audio file. Capture keeps an SVG link attribute only under its plain or xlink name.
> **Fixes**
> - **CLI:** Tts replaces a link at its output name with the audio file ([45846f1e6d](https://github.com/heygen-com/hyperframes/commit/45846f1e6d5609462d29652315d0d4254fe92c24), [#8707](https://github.com/heygen-com/hyperframes/pull/8707)).
> - **CLI:** Speak a narration line as written in local voice and tts ([99ccd54c63](https://github.com/heygen-com/hyperframes/commit/99ccd54c6369cfd5aab43e83a1dfd441e5fdf791), [#8706](https://github.com/heygen-com/hyperframes/pull/8706)).
> …

### [v0.9.90](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.90)
<sub>2026-11-24 · yesterday</sub>

> **HyperFrames v0.9.90**
> Released on 2026-11-24.
> A project page opened straight from a link now runs apart from Studio. Sealed previews show off-canvas indicators and keep a motion path on its layer. Capture saves an inline SVG as a file only when it is a plain image.
> **Fixes**
> - **CLI:** Media-use resolve reads each asset as one local self-contained container ([7975ecc423](https://github.com/heygen-com/hyperframes/commit/7975ecc423a0670a510fedd7d722146a370a0186), [#8713](https://github.com/heygen-com/hyperframes/pull/8713)).
> - **Media Use:** The skill's media probe opens files only as self-contained containers ([7a7471e7cf](https://github.com/heygen-com/hyperframes/commit/7a7471e7cf93ee44cbe79cbc9cc9156e6544028e), [#8710](https://github.com/heygen-com/hyperframes/pull/8710)).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [fix(core): strip file marks inside templates and refuse markup a brow…](https://github.com/heygen-com/hyperframes/commit/81869faaa769c3a1f720ac6adcf59d3201a58046) | miguel-heygen |
| 2026-11-25 | [fix(studio): an edit goes to the file a host was mounted from, never …](https://github.com/heygen-com/hyperframes/commit/9dc416ad50f958a9fa5454b14bbebb1094911a0e) | miguel-heygen |
| 2026-11-25 | [fix(studio-server): element and animation edits take an HTML file onl…](https://github.com/heygen-com/hyperframes/commit/92d0210a174390913958dde9ab50242a75065fc2) | jrusso1020 |
| 2026-11-25 | [fix(media-use): a music job puts its track at the name only when comp…](https://github.com/heygen-com/hyperframes/commit/5dd0ee9eff5b9656a84f6617b2cf65a93181448e) | jrusso1020 |
| 2026-11-25 | [test(studio): the edit bench reads a nudge burst's box once a sealed …](https://github.com/heygen-com/hyperframes/commit/b79fd6ae2ad9cb0452c103ff9bb8a36fdc139787) | miguel-heygen |
| 2026-11-25 | [feat(studio): a sealed preview reports the shown display of every ele…](https://github.com/heygen-com/hyperframes/commit/8008dc89f078d748067b6e03524936b42c2defb3) | miguel-heygen |
| 2026-11-25 | [test(engine): the cut audio link test cuts the read under load too (#…](https://github.com/heygen-com/hyperframes/commit/6f997837c0eae19d26946ebe8bdc96ebce3c5764) | miguel-heygen |
| 2026-11-25 | [fix(studio): a file is a composition only when a browser would build …](https://github.com/heygen-com/hyperframes/commit/d494f25c7b3048de45c38767503d94ebe34d2970) | jrusso1020 |
| 2026-11-25 | [fix(media-use): audio scripts replace the file at a name and leave a …](https://github.com/heygen-com/hyperframes/commit/4c0d6148a317bab266aec23168a48273e33989b8) | jrusso1020 |
| 2026-11-25 | [fix(studio-server): opening a project no longer waits on its drive to…](https://github.com/heygen-com/hyperframes/commit/7359dc95e4dd495b06a601e7d98db21078b8e811) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
