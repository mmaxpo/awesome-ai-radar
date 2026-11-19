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
| ⭐ **Stars** | 86.8k |
| 🍴 **Forks** | 8.1k |
| 🐞 **Open issues + PRs** | [299](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.70](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.70) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 534.5 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.70](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.70)
<sub>2026-11-19 · today</sub>

> **HyperFrames v0.9.70**
> Released on 2026-11-19.
> Projects with many SVG references or large sets of variables compile faster, and files whose path holds a tab join again. A provider key in your own project's .env file is used again, as the docs describe.
> **Fixes**
> - **Media Use:** Recipe, prefs and SFX lines show control characters as escapes ([36b60d18b4](https://github.com/heygen-com/hyperframes/commit/36b60d18b488999a36748693ef04fc3516e40aa4), [#8202](https://github.com/heygen-com/hyperframes/pull/8202)).
> - **Render:** Keep segment checkpoints in the local cache ([e5283f63b9](https://github.com/heygen-com/hyperframes/commit/e5283f63b90dfe1bd4da45391dcd6969d3475462), [#8137](https://github.com/heygen-com/hyperframes/pull/8137)).
> …

### [v0.9.69](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.69)
<sub>2026-11-18 · today</sub>

> **HyperFrames v0.9.69**
> Released on 2026-11-18.
> Image captioning in `capture` can now use a short-lived Vertex access token instead of a service-account key file. In Studio, a script edit in a sealed preview re-runs in place, without reloading the page.
> **Features**
> - **Capture:** Accept a short-lived Vertex access token for image captioning ([e0470b0add](https://github.com/heygen-com/hyperframes/commit/e0470b0add0569e158b0b07109155a9c760a72e3), [#8215](https://github.com/heygen-com/hyperframes/pull/8215)).
> **Fixes**
> …

### [v0.9.68](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.68)
<sub>2026-11-18 · today</sub>

> **HyperFrames v0.9.68**
> Released on 2026-11-18.
> A render whose page Chrome closed while opening now reopens it, or says why it can't. Sealed previews keep an unsized video's own size and show animated values, and renders can send all their traffic through one outbound proxy.
> **Features**
> - **Engine:** Renders send page traffic through the egress proxy in HYPERFRAMES_CAPTURE_PROXY ([a2830467e](https://github.com/heygen-com/hyperframes/commit/a2830467e4d106d5058de89bb0d2c20d83d2cc4e), [#8196](https://github.com/heygen-com/hyperframes/pull/8196)).
> **Fixes**
> …

### [v0.8.190-hdr.2](https://github.com/heygen-com/hyperframes/releases/tag/v0.8.190-hdr.2) _(pre-release)_
<sub>2026-11-18 · today</sub>

> **What's Changed**
> **Other Changes**
> * fix(cli): isolate the skills freshness check on the hdr prerelease by @terencecho in https://github.com/heygen-com/hyperframes/pull/8199
> **Full Changelog**: https://github.com/heygen-com/hyperframes/compare/v0.8.190-hdr.1...v0.8.190-hdr.2

### [v0.9.28-alpha.4](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.28-alpha.4) _(pre-release)_
<sub>2026-11-18 · today</sub>

> **What's Changed**
> **Other Changes**
> * fix(cli): isolate the skills freshness check on the alpha prerelease by @terencecho in https://github.com/heygen-com/hyperframes/pull/8197
> **Full Changelog**: https://github.com/heygen-com/hyperframes/compare/v0.9.28-alpha.3...v0.9.28-alpha.4

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [fix(producer): cap compile-time remote downloads, give them one deadl…](https://github.com/heygen-com/hyperframes/commit/77ea9d80cfc8b347ccca966487a8ff902ce28320) | miguel-heygen |
| 2026-11-19 | [fix: stop crashing on SVG elements named template (#8241)](https://github.com/heygen-com/hyperframes/commit/d106f9c8c7eacce9ae30275f9e78d715dd269e10) | miguel-heygen |
| 2026-11-19 | [fix(core): read selector aliases only from what the compiler wrote (#…](https://github.com/heygen-com/hyperframes/commit/def770ed9886171789f420d9cd3fcd79eaace91b) | miguel-heygen |
| 2026-11-19 | [fix(core): page runtimes carry no wide characters, so pages stay one …](https://github.com/heygen-com/hyperframes/commit/01a5e948beb984e0ea19f8939d4a5ae2b242f117) | miguel-heygen |
| 2026-11-19 | [fix(media-use): re-freezing a recipe archives only under an integer v…](https://github.com/heygen-com/hyperframes/commit/e383abf475b6ebd5072d6aa1cb380bc7d984c629) | WaterrrForever |
| 2026-11-19 | [chore: release v0.9.70 (#8234)](https://github.com/heygen-com/hyperframes/commit/592a9feff9aacce8c25246b04aa4fda54bea294d) | miguel-heygen |
| 2026-11-19 | [fix(media-use): recipe, prefs and SFX lines show control characters a…](https://github.com/heygen-com/hyperframes/commit/36b60d18b488999a36748693ef04fc3516e40aa4) | WaterrrForever |
| 2026-11-19 | [fix(render): keep segment checkpoints in the local cache (#8137)](https://github.com/heygen-com/hyperframes/commit/e5283f63b90dfe1bd4da45391dcd6969d3475462) | terencecho |
| 2026-11-19 | [fix(skills): raise the launcher minimum to 0.9.68 (#8232)](https://github.com/heygen-com/hyperframes/commit/a4995e9e6f3856292bf957e5b376600a634b918c) | terencecho |
| 2026-11-19 | [perf(core): rewrite svg attribute selectors in linear time over many …](https://github.com/heygen-com/hyperframes/commit/c672ef0e5d03a9f7410db7352172bd8fc75ddde6) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
