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
| ⭐ **Stars** | 85.0k |
| 🍴 **Forks** | 7.9k |
| 🐞 **Open issues + PRs** | [291](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.56](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.56) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 529.4 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.56](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.56)
<sub>2026-11-16 · today</sub>

> **HyperFrames v0.9.56**
> Released on 2026-11-16.
> Studio's preview and the local servers now act only for their own pages. The CLI keeps its cache, history and restores inside the project. The arm64 Lambda image ships only the reviewed ffmpeg build, and large previews build faster.
> **Fixes**
> - **Studio Server:** The composition file servers no longer serve credential or tool-state files ([014326b40](https://github.com/heygen-com/hyperframes/commit/014326b40bf22bebb77a5cf08a50d5b0968c112e), [#7889](https://github.com/heygen-com/hyperframes/pull/7889)).
> - **Studio Server:** Lint and probe run only for requests from Studio's own pages ([bbac8900e](https://github.com/heygen-com/hyperframes/commit/bbac8900ea9201dca8aacdd17387e3275a9e6d84), [#7894](https://github.com/heygen-com/hyperframes/pull/7894)).
> …

### [v0.9.55](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.55)
<sub>2026-11-15 · today</sub>

> **HyperFrames v0.9.55**
> Released on 2026-11-15.
> A sealed Studio preview now plays a video's proxy copy and reloads under one current frame token. Cloud render sends one zip when it fits and uploads only the largest media. The file servers check the Host they are asked under, and publish and cloud render staging skip other computers' network shares.
> **Fixes**
> - **Studio Server:** Sub-composition head and root tag scans take linear time ([ceb969dba](https://github.com/heygen-com/hyperframes/commit/ceb969dbacff281ec1fdddf9fe22c0fcd34fb663), [#7866](https://github.com/heygen-com/hyperframes/pull/7866)).
> - **CLI:** The engine and CLI share one trusted PATH rule, and a skipped project copy says why ([e2430edec](https://github.com/heygen-com/hyperframes/commit/e2430edecf5492a02a363eaa5c30ad2708af5aee), [#7801](https://github.com/heygen-com/hyperframes/pull/7801)).
> …

### [v0.9.54](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.54)
<sub>2026-11-15 · today</sub>

> **HyperFrames v0.9.54**
> Released on 2026-11-15.
> Studio hosts can now run the preview on its own sealed origin with the sandboxOrigin option or VITE_STUDIO_OPAQUE_PREVIEW_ENABLED, off by default. When sealed, the preview's images, media, fetched files, console errors panel and GSAP keyframe and 3D previews keep working. Render, capture and bundling also leave out the app's own .hyperframes records.
> **Features**
> - **Studio:** Hosts can share the preview's editing-port client ([3a4f57252](https://github.com/heygen-com/hyperframes/commit/3a4f57252377051f6602bd0149e84f8ead0845b2), [#7811](https://github.com/heygen-com/hyperframes/pull/7811)).
> - **Studio:** Hosts can seal the preview frames NLEPreview draws ([a73ecff2b](https://github.com/heygen-com/hyperframes/commit/a73ecff2bef2168c47625e781bc1de13c7ca23ce), [#7817](https://github.com/heygen-com/hyperframes/pull/7817)).
> …

### [v0.9.53](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.53)
<sub>2026-11-15 · today</sub>

> **HyperFrames v0.9.53**
> Released on 2026-11-15.
> Pages with many Chinese, Japanese or Korean characters now load their fonts in a few small requests, so they render instead of timing out. Cloud render no longer refuses a file that only an unused page names, and uploads now list every file they carry from outside the project.
> **Features**
> - **CLI:** Uploads list every file they carry from outside the project ([e426ce4eb](https://github.com/heygen-com/hyperframes/commit/e426ce4eb44517db3f65105f1e05cb7b762cd950), [#7831](https://github.com/heygen-com/hyperframes/pull/7831)).
> **Fixes**
> …

### [v0.9.52](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.52)
<sub>2026-11-15 · yesterday</sub>

> **HyperFrames v0.9.52**
> Released on 2026-11-15.
> In Studio menus, the highlighted row now follows the menu's rounded corner. The shared menu row style is exported so other apps can match it.
> **Fixes**
> - **Studio:** Menu row highlight follows the menu's corner ([b5f5ab36a](https://github.com/heygen-com/hyperframes/commit/b5f5ab36a1f4b626da9de40adf7e40257967997c), [#7791](https://github.com/heygen-com/hyperframes/pull/7791)).
> **Full changelog**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [ci(skills): read the ClawHub token from the main-only clawhub environ…](https://github.com/heygen-com/hyperframes/commit/5d5e2c062a4876e590f8d5a9fe59833d7b1e3684) | miguel-heygen |
| 2026-11-16 | [fix(cli): check and info never probe a composition's remote media URL…](https://github.com/heygen-com/hyperframes/commit/78648113dbdac0f5daae75fed820509860267b41) | michaelwang11394 |
| 2026-11-16 | [fix(cli): open starts the desktop app in the home folder, not the fol…](https://github.com/heygen-com/hyperframes/commit/a2e7306b2fa1ca55a360d7d22b8dbb1ef2bc1f8d) | miguel-heygen |
| 2026-11-16 | [fix(cli): studio thumbnails and Ctrl-C cleanup under a restricted pag…](https://github.com/heygen-com/hyperframes/commit/707e20f185f3c7fa67b8aa527ea0f0aecbfec0b6) | jrusso1020 |
| 2026-11-16 | [fix(studio-server): a host that built a page on the build worker can …](https://github.com/heygen-com/hyperframes/commit/e8f1fff5fdf330d2fd634f7abe117ee6ba17f63e) | miguel-heygen |
| 2026-11-16 | [test(studio-server): give tests the CLI's 20 s ceiling so a busy CI r…](https://github.com/heygen-com/hyperframes/commit/8ec98be29a64e88239a0c05f7e5d09f36e181493) | miguel-heygen |
| 2026-11-16 | [fix(cli): commands that open a composition honor PRODUCER_RESTRICT_PA…](https://github.com/heygen-com/hyperframes/commit/49e9424baa74cf27aa91981ed0da3349e6371ab4) | jrusso1020 |
| 2026-11-16 | [fix(engine,producer,cli): media inputs refuse formats that open other…](https://github.com/heygen-com/hyperframes/commit/ead110aab9e4b43befdbe21001deac168c09e04b) | vanceingalls |
| 2026-11-16 | [feat(studio): a sealed preview frame forwards Studio's playback keys …](https://github.com/heygen-com/hyperframes/commit/b741ecf1320ebad92f3a74b1e87a50a326c84db4) | miguel-heygen |
| 2026-11-16 | [fix(engine): check the resolved address of a restricted download unde…](https://github.com/heygen-com/hyperframes/commit/04b690361a294678cd9f7514432702031e6a854f) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
