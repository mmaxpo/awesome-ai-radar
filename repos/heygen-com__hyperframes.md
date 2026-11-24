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
| ⭐ **Stars** | 89.4k |
| 🍴 **Forks** | 8.3k |
| 🐞 **Open issues + PRs** | [324](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` `agent-skills` `ai-video` `ai-video-editor` `remotion-alternative` `video-editing` `video-generation` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.90](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.90) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 542.4 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.90](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.90)
<sub>2026-11-24 · today</sub>

> **HyperFrames v0.9.90**
> Released on 2026-11-24.
> A project page opened straight from a link now runs apart from Studio. Sealed previews show off-canvas indicators and keep a motion path on its layer. Capture saves an inline SVG as a file only when it is a plain image.
> **Fixes**
> - **CLI:** Media-use resolve reads each asset as one local self-contained container ([7975ecc423](https://github.com/heygen-com/hyperframes/commit/7975ecc423a0670a510fedd7d722146a370a0186), [#8713](https://github.com/heygen-com/hyperframes/pull/8713)).
> - **Media Use:** The skill's media probe opens files only as self-contained containers ([7a7471e7cf](https://github.com/heygen-com/hyperframes/commit/7a7471e7cf93ee44cbe79cbc9cc9156e6544028e), [#8710](https://github.com/heygen-com/hyperframes/pull/8710)).
> …

### [v0.9.89](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.89)
<sub>2026-11-24 · today</sub>

> **HyperFrames v0.9.89**
> Released on 2026-11-24.
> A Studio capture shows a 4K clip from the server's frame, and deleting a clip no longer re-renders every player. File, media and backup reads touch only the one path they were given.
> **Fixes**
> - **Media Use:** Carve decodes only media files inside the composition's folder ([aefca2baff](https://github.com/heygen-com/hyperframes/commit/aefca2baff396213711b59fcce5ec357896529c6), [#8649](https://github.com/heygen-com/hyperframes/pull/8649)).
> - **Player:** A sealed player plays media from hosts without CORS and names a missing runtime ([1c20a107a6](https://github.com/heygen-com/hyperframes/commit/1c20a107a6d671b69e13d0b31402f35f10c8e5ea), [#8142](https://github.com/heygen-com/hyperframes/pull/8142)).
> …

### [v0.9.88](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.88)
<sub>2026-11-24 · today</sub>

> **HyperFrames v0.9.88**
> Released on 2026-11-24.
> A cloud render no longer stops a chunk as stalled while its video frames are still extracting. The 4K clip on screen plays its own file while its lighter preview copy is made, instead of showing a still.
> **Fixes**
> - **Producer:** A cloud chunk is not stopped as stalled while its video frames are still extracting ([8cdf5b22dc](https://github.com/heygen-com/hyperframes/commit/8cdf5b22dc2edf6766d2cd8c17e3b8d35883cdfa), [#8632](https://github.com/heygen-com/hyperframes/pull/8632)).
> - **Player:** A film ready before load no longer times the frame's next own document from it ([779bed5c0a](https://github.com/heygen-com/hyperframes/commit/779bed5c0a6da3c7364d441f8945c2d8a54a8cbe), [#8634](https://github.com/heygen-com/hyperframes/pull/8634))
> …

### [v0.9.87](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.87)
<sub>2026-11-24 · today</sub>

> **HyperFrames v0.9.87**
> Released on 2026-11-23.
> An edit's preview shows the change again within about a second, not after a five-second wait. Looped audio stays in sync in Safari, and a render's compile now stops at a deadline.
> **Features**
> - **Studio:** Apps embedding Studio can style a sealed pick as Studio's panel does ([8376f32e0c](https://github.com/heygen-com/hyperframes/commit/8376f32e0c8586c2055bc704724fa390beef54eb), [#8614](https://github.com/heygen-com/hyperframes/pull/8614)).
> **Fixes**
> …

### [v0.9.86](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.86)
<sub>2026-11-23 · yesterday</sub>

> **HyperFrames v0.9.86**
> Released on 2026-11-23.
> A save during an import keeps its own undo step, and full-size stills count their real memory, so the cache frees them. Text on a sealed preview can now be edited in place, and sealed recordings move the layer live.
> **Features**
> - **Studio:** Edit text in place on a sealed preview's canvas ([8d2783561](https://github.com/heygen-com/hyperframes/commit/8d2783561f4eb3038a2b6305cc9f160651834a12), [#8183](https://github.com/heygen-com/hyperframes/pull/8183)).
> **Fixes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [chore: release v0.9.91 (#8718)](https://github.com/heygen-com/hyperframes/commit/08431260d936ba5001bb7d13be21397a1ef6ffd2) | jrusso1020 |
| 2026-11-24 | [fix(cli): tts replaces a link at its output name with the audio file …](https://github.com/heygen-com/hyperframes/commit/45846f1e6d5609462d29652315d0d4254fe92c24) | jrusso1020 |
| 2026-11-24 | [fix(registry): inline the warm-grain starter's grain texture (#8712)](https://github.com/heygen-com/hyperframes/commit/93309f35cda894adab3e13ba66b1cd2e81618569) | jrusso1020 |
| 2026-11-24 | [fix(docs): copied catalog wiring reads back as the values shown (#8715)](https://github.com/heygen-com/hyperframes/commit/716a89e571e2e8f94ecc84934741b02dd1592a66) | jrusso1020 |
| 2026-11-24 | [fix(cli): speak a narration line as written in local voice and tts (#…](https://github.com/heygen-com/hyperframes/commit/99ccd54c6369cfd5aab43e83a1dfd441e5fdf791) | jrusso1020 |
| 2026-11-24 | [fix(studio-server): preview head scripts land in the head when an att…](https://github.com/heygen-com/hyperframes/commit/07e03e8fed3846ccbf0d79f9ec0b145b3e308fae) | jrusso1020 |
| 2026-11-24 | [fix(cli): capture keeps an SVG link attribute only under its plain or…](https://github.com/heygen-com/hyperframes/commit/42ad487987b7e7f61b10fda341338f2caa10020f) | jrusso1020 |
| 2026-11-24 | [chore: release v0.9.90 (#8709)](https://github.com/heygen-com/hyperframes/commit/8eeeabf8a6c293c96e69444dd92de9b8b6c8c945) | jrusso1020 |
| 2026-11-24 | [fix(cli): media-use resolve reads each asset as one local self-contai…](https://github.com/heygen-com/hyperframes/commit/7975ecc423a0670a510fedd7d722146a370a0186) | michaelwang11394 |
| 2026-11-24 | [fix(media-use): the skill's media probe opens files only as self-cont…](https://github.com/heygen-com/hyperframes/commit/7a7471e7cf93ee44cbe79cbc9cc9156e6544028e) | michaelwang11394 |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
