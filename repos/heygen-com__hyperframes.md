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
| ⭐ **Stars** | 87.7k |
| 🍴 **Forks** | 8.2k |
| 🐞 **Open issues + PRs** | [290](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.77](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.77) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 536.8 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.77](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.77)
<sub>2026-11-21 · today</sub>

> **HyperFrames v0.9.77**
> Released on 2026-11-21.
> CLI messages now show control characters as plain text. An undo in Studio never deletes a file another page still uses, and big root previews no longer hold up other requests.
> **Features**
> - **Studio Server:** A host can name paths its project history never records ([9bea44695](https://github.com/heygen-com/hyperframes/commit/9bea44695b6c36f9eb89542fdeca556750dcc797), [#8224](https://github.com/heygen-com/hyperframes/pull/8224)).
> **Fixes**
> …

### [v0.9.75](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.75)
<sub>2026-11-21 · today</sub>

> **HyperFrames v0.9.75**
> Released on 2026-11-21.
> Seeking a film with many videos no longer hangs Safari. Opening and pruning history no longer stalls on a slow project folder, and CLI writes never follow a link already in a project.
> **Fixes**
> - **CLI:** Writes into a project folder never follow a link already there ([4a50fb279](https://github.com/heygen-com/hyperframes/commit/4a50fb2798186e3292144f4cee78071cbca7172b), [#8334](https://github.com/heygen-com/hyperframes/pull/8334)).
> - **Studio Server:** History reads a project's folder off the thread when opening and pruning ([63d1bb559](https://github.com/heygen-com/hyperframes/commit/63d1bb5596d0a307b3efa4290a7a3cf3848e090e), [#8340](https://github.com/heygen-com/hyperframes/pull/8340)).
> …

### [v0.9.74](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.74)
<sub>2026-11-21 · today</sub>

> **HyperFrames v0.9.74**
> Released on 2026-11-21.
> Films whose later scene sets an !important background on an id no longer render blank. Clips dropped on a sealed preview show on the timeline, and a package that fails to publish is tried again.
> **Features**
> - **Core:** A sealed preview's frame runs an in-place text editing session for Studio ([9848647b9](https://github.com/heygen-com/hyperframes/commit/9848647b962bf889ec8baac832f2b1ee3daf7c9e), [#8181](https://github.com/heygen-com/hyperframes/pull/8181)).
> **Fixes**
> …

### [v0.9.73](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.73)
<sub>2026-11-20 · today</sub>

> **HyperFrames v0.9.73**
> Released on 2026-11-20.
> Preview copies of long clips with sound finish again, so their footage no longer shows black. Saving history on a drive that stops answering no longer freezes the app, and sealed films show when their timeline arrives late.
> **Fixes**
> - **Studio:** Paste refuses an element with an event handler or a script link ([7b2c6dc1a](https://github.com/heygen-com/hyperframes/commit/7b2c6dc1ad7aaf49d72d023d0e6b0d3f537143a9), [#8298](https://github.com/heygen-com/hyperframes/pull/8298)).
> - **Studio:** The first edit of a film without ids no longer reloads the preview ([99fcdfb5c](https://github.com/heygen-com/hyperframes/commit/99fcdfb5c1de5d17bd1e848e9ae5d7b4450ff7c8), [#8274](https://github.com/heygen-com/hyperframes/pull/8274)).
> …

### [v0.9.72](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.72)
<sub>2026-11-20 · yesterday</sub>

> **HyperFrames v0.9.72**
> Released on 2026-11-20.
> Renders limited by a CPU quota, such as a Kubernetes CPU limit, get their workers back, so long renders run at full speed again. Sealed previews restack layers from the layers panel and the timeline, and their videos keep colour grading and audio effects.
> **Fixes**
> - **Engine:** Renders under a CPU quota get their workers back ([db5950c00](https://github.com/heygen-com/hyperframes/commit/db5950c0049cd38b4fa73712121556c763621211), [#8262](https://github.com/heygen-com/hyperframes/pull/8262)).
> - **Studio:** Dragging a layer in a sealed preview's layers panel restacks it ([9c3bfe150](https://github.com/heygen-com/hyperframes/commit/9c3bfe150eada7728d1d99f4b957aeba863cb081), [#8209](https://github.com/heygen-com/hyperframes/pull/8209)).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [fix(cli): show control characters as text in capture, figma, usage an…](https://github.com/heygen-com/hyperframes/commit/7fcc4909b442ba79918ae69d8a67416820d730f9) | jrusso1020 |
| 2026-11-21 | [fix(studio): adding or removing a text field keeps the spaces between…](https://github.com/heygen-com/hyperframes/commit/e8f52dc866221ff8ffad06ce4c198d0d969aaa05) | miguel-heygen |
| 2026-11-21 | [fix(cli): a received-files write waits out a held lock instead of fai…](https://github.com/heygen-com/hyperframes/commit/f74e1545c06e32b5f0c0722b4a46b7e628d04a31) | miguel-heygen |
| 2026-11-21 | [test(studio): the marquee-past-the-cap check waits as long as the fra…](https://github.com/heygen-com/hyperframes/commit/b0d9f3615984e6e88c2d6b4dae862fbde2004da1) | miguel-heygen |
| 2026-11-21 | [fix(cli): a stop reads the process tree from /proc on Linux, so load …](https://github.com/heygen-com/hyperframes/commit/a2df08e49ebb2b2d285c0e8a7c173f953b032a9d) | miguel-heygen |
| 2026-11-21 | [fix(engine): a capture proxy shared by many browsers no longer drops …](https://github.com/heygen-com/hyperframes/commit/5e16c18b1d239f7e1225f59be5c44614a6d9d784) | miguel-heygen |
| 2026-11-21 | [fix(cli): show control characters as text in init, skills and render …](https://github.com/heygen-com/hyperframes/commit/8bc73a0bd34313790bdbf6be43cf67f311800711) | jrusso1020 |
| 2026-11-21 | [test(studio-server): a held-file edit is checked for blocking waits, …](https://github.com/heygen-com/hyperframes/commit/29a5003eebdd1a1a01e4d1a4e3f375da93b078ab) | miguel-heygen |
| 2026-11-21 | [fix(cli): show control characters as text in more commands' printed l…](https://github.com/heygen-com/hyperframes/commit/7a1163fc98149719c636a170aad6c99e2d68a291) | jrusso1020 |
| 2026-11-21 | [fix(studio-server): a preview file request no longer waits on a silen…](https://github.com/heygen-com/hyperframes/commit/7cb605c787f4e85f66a2a46df60f8fdbe13faad6) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
