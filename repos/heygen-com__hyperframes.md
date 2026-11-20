# heygen-com/hyperframes

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/heygen-com/hyperframes)

> AI video you can actually edit. HyperFrames is a free, open-source AI video editor. Describe any video and get a real project you can change down to the frame.

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
| ⭐ **Stars** | 87.3k |
| 🍴 **Forks** | 8.1k |
| 🐞 **Open issues + PRs** | [307](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.72](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.72) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 535.7 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.72](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.72)
<sub>2026-11-20 · today</sub>

> **HyperFrames v0.9.72**
> Released on 2026-11-20.
> Renders limited by a CPU quota, such as a Kubernetes CPU limit, get their workers back, so long renders run at full speed again. Sealed previews restack layers from the layers panel and the timeline, and their videos keep colour grading and audio effects.
> **Fixes**
> - **Engine:** Renders under a CPU quota get their workers back ([db5950c00](https://github.com/heygen-com/hyperframes/commit/db5950c0049cd38b4fa73712121556c763621211), [#8262](https://github.com/heygen-com/hyperframes/pull/8262)).
> - **Studio:** Dragging a layer in a sealed preview's layers panel restacks it ([9c3bfe150](https://github.com/heygen-com/hyperframes/commit/9c3bfe150eada7728d1d99f4b957aeba863cb081), [#8209](https://github.com/heygen-com/hyperframes/pull/8209)).
> …

### [v0.9.71](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.71)
<sub>2026-11-19 · today</sub>

> **HyperFrames v0.9.71**
> Released on 2026-11-19.
> Cancelling a render now stops its compile, and files a compile downloads have a size cap and one shared deadline. Renders read frames from MP4s whose seek index leaves out the first keyframe, and SVG-heavy compositions stay within the compile size limit.
> **Fixes**
> - **Engine:** Extract frames from MP4s whose seek index leaves out the first keyframe ([9813a6cbe](https://github.com/heygen-com/hyperframes/commit/9813a6cbef97fffda70f5a147b87747f7e35a77b), [#8252](https://github.com/heygen-com/hyperframes/pull/8252)).
> - **Media Use:** Duck, cut, transcribe, dither and audio scripts print control characters as escapes ([98f548447](https://github.com/heygen-com/hyperframes/commit/98f548447e44307d4c240cf100bfb15a5e362b2f), [#8235](https://github.com/heygen-com/hyperframes/pull/8235)).
> …

### [v0.9.70](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.70)
<sub>2026-11-19 · yesterday</sub>

> **HyperFrames v0.9.70**
> Released on 2026-11-19.
> Projects with many SVG references or large sets of variables compile faster, and files whose path holds a tab join again. A provider key in your own project's .env file is used again, as the docs describe.
> **Fixes**
> - **Media Use:** Recipe, prefs and SFX lines show control characters as escapes ([36b60d18b4](https://github.com/heygen-com/hyperframes/commit/36b60d18b488999a36748693ef04fc3516e40aa4), [#8202](https://github.com/heygen-com/hyperframes/pull/8202)).
> - **Render:** Keep segment checkpoints in the local cache ([e5283f63b9](https://github.com/heygen-com/hyperframes/commit/e5283f63b90dfe1bd4da45391dcd6969d3475462), [#8137](https://github.com/heygen-com/hyperframes/pull/8137)).
> …

### [v0.9.69](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.69)
<sub>2026-11-18 · yesterday</sub>

> **HyperFrames v0.9.69**
> Released on 2026-11-18.
> Image captioning in `capture` can now use a short-lived Vertex access token instead of a service-account key file. In Studio, a script edit in a sealed preview re-runs in place, without reloading the page.
> **Features**
> - **Capture:** Accept a short-lived Vertex access token for image captioning ([e0470b0add](https://github.com/heygen-com/hyperframes/commit/e0470b0add0569e158b0b07109155a9c760a72e3), [#8215](https://github.com/heygen-com/hyperframes/pull/8215)).
> **Fixes**
> …

### [v0.9.68](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.68)
<sub>2026-11-18 · yesterday</sub>

> **HyperFrames v0.9.68**
> Released on 2026-11-18.
> A render whose page Chrome closed while opening now reopens it, or says why it can't. Sealed previews keep an unsized video's own size and show animated values, and renders can send all their traffic through one outbound proxy.
> **Features**
> - **Engine:** Renders send page traffic through the egress proxy in HYPERFRAMES_CAPTURE_PROXY ([a2830467e](https://github.com/heygen-com/hyperframes/commit/a2830467e4d106d5058de89bb0d2c20d83d2cc4e), [#8196](https://github.com/heygen-com/hyperframes/pull/8196)).
> **Fixes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [fix(studio): a sealed move, resize or turn takes GSAP's route when GS…](https://github.com/heygen-com/hyperframes/commit/468ab907ee9836e076abdd7d0e0611c475dc1271) | miguel-heygen |
| 2026-11-20 | [fix(studio): a sealed resize, move or turn typed or made by the agent…](https://github.com/heygen-com/hyperframes/commit/89edb0af0059fc599ec7b17c1078ab49a46d9da2) | miguel-heygen |
| 2026-11-20 | [fix(studio): agent tools see the film in a sealed preview (#8281)](https://github.com/heygen-com/hyperframes/commit/c34df57abdb02b07916aa2a26c5c1be8dcd2ac64) | miguel-heygen |
| 2026-11-20 | [fix(studio): a sealed crop lands where it was dragged (#8279)](https://github.com/heygen-com/hyperframes/commit/a755e3f58588024cdbc3f698e3d7673a4760dbc2) | miguel-heygen |
| 2026-11-20 | [fix(core): a sub-composition's script re-run keeps the preview at its…](https://github.com/heygen-com/hyperframes/commit/33272097272eeda1b082879a2d79f38a9e47526b) | miguel-heygen |
| 2026-11-20 | [fix(core): a redo in a sealed preview puts Studio's edit marks back i…](https://github.com/heygen-com/hyperframes/commit/95a8a91b5ea28ec21ac638aa69cd43b3a8c46cea) | miguel-heygen |
| 2026-11-20 | [fix(core): split a rule's selector list once when rewriting svg id re…](https://github.com/heygen-com/hyperframes/commit/fbbbfe0587bb27f6738b7a697c11914caaa9a39c) | miguel-heygen |
| 2026-11-20 | [fix(studio-server): preview copies of long clips with sound finish ag…](https://github.com/heygen-com/hyperframes/commit/07928702f8b3e3f59c75594e759df84443896890) | miguel-heygen |
| 2026-11-20 | [fix(media-use): remove only the temp folders media-use made, and neve…](https://github.com/heygen-com/hyperframes/commit/e16c681dc07d360a9cf42e2ab77d827196a29883) | ukimsanov |
| 2026-11-20 | [fix(core): check svg id scopes against excluded roots in one ancestor…](https://github.com/heygen-com/hyperframes/commit/026bff07d60edecbbc33045490511d1d948e6950) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
