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
| 🐞 **Open issues + PRs** | [291](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.77](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.77) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 537.4 MB |
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
| 2026-11-21 | [fix(studio-server): the preview file check resolves links on volumes …](https://github.com/heygen-com/hyperframes/commit/40cc86252d80ebc0daaf3db373b13d339f8c13f8) | miguel-heygen |
| 2026-11-21 | [fix(cli): print capture setup commands on their own lines (#8374)](https://github.com/heygen-com/hyperframes/commit/281f1a2a48137925d114dbd8b55e03d152bdf83d) | jrusso1020 |
| 2026-11-21 | [fix(studio-server): an agent step waits for history's first copies, s…](https://github.com/heygen-com/hyperframes/commit/fbbf5ee67e86e41e10536e5088baaf886330a60c) | miguel-heygen |
| 2026-11-21 | [fix(studio-server): history refusals carry a closed reason, so caller…](https://github.com/heygen-com/hyperframes/commit/d5881e8aa67f796f851ae15a75702294ef53cc9f) | miguel-heygen |
| 2026-11-21 | [fix(studio-server): a timed-out history save says it may still land, …](https://github.com/heygen-com/hyperframes/commit/6b74cfa9f5bbf01ebb0fe30420c0dab6c71f4f84) | miguel-heygen |
| 2026-11-21 | [feat(engine): a late image's load time is logged when it arrives (#8372)](https://github.com/heygen-com/hyperframes/commit/e65b11e5c2be2c73d3ab0ea5628c51ec13f68a21) | miguel-heygen |
| 2026-11-21 | [fix(cli): read --json before the command name the same as after it (#…](https://github.com/heygen-com/hyperframes/commit/9a618b798fcb6bb262d3709bc1de6edf2fff974b) | jrusso1020 |
| 2026-11-21 | [fix(cli): a catalog gap report hands back a line only when every shel…](https://github.com/heygen-com/hyperframes/commit/4145572625110706fdbc269adaca70ee5de531e8) | miguel-heygen |
| 2026-11-21 | [fix(cli): show control characters as text in capture, figma, usage an…](https://github.com/heygen-com/hyperframes/commit/7fcc4909b442ba79918ae69d8a67416820d730f9) | jrusso1020 |
| 2026-11-21 | [fix(studio): adding or removing a text field keeps the spaces between…](https://github.com/heygen-com/hyperframes/commit/e8f52dc866221ff8ffad06ce4c198d0d969aaa05) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
