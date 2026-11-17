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
| ⭐ **Stars** | 85.7k |
| 🍴 **Forks** | 7.9k |
| 🐞 **Open issues + PRs** | [295](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.61](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.61) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 531.9 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.61](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.61)
<sub>2026-11-17 · today</sub>

> **HyperFrames v0.9.61**
> Released on 2026-11-17.
> Received projects and the files they reach stay inside their own folder across render, preview and Studio, and a sealed preview reloads in place in a fraction of a second. This release also carries every change listed for 0.9.60. That version never reached npm: its publish was refused because it ran from the release PR's merge ref, and since #8020 a stable release publishes from the push to `main` that merges it.
> **Features**
> - **Engine:** Render telemetry says why a page cannot reuse still frames ([c8df284b2](https://github.com/heygen-com/hyperframes/commit/c8df284b2ed15ae0ade05bf90e95192d05f3d1c6), [#7993](https://github.com/heygen-com/hyperframes/pull/7993)).
> - **Studio:** An element's source-parsed animations are part of Studio's API ([efc91fc87](https://github.com/heygen-com/hyperframes/commit/efc91fc877d89d8057611dd87c81220be46df9a2), [#8061](https://github.com/heygen-com/hyperframes/pull/8061)).
> …

### [v0.9.59](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.59)
<sub>2026-11-17 · today</sub>

> **HyperFrames v0.9.59**
> Released on 2026-11-16.
> The preview player gets a fullscreen button, and a failed render now says why. Renders, Studio and the CLI keep to the project's own files and to public media hosts.
> **Features**
> - **CLI:** Diff --hide scores a project's layer by what it adds ([e6d5c699b](https://github.com/heygen-com/hyperframes/commit/e6d5c699b18d4f1c6cc9d22227b1f1c3e1fd43f3), [#7972](https://github.com/heygen-com/hyperframes/pull/7972)).
> - **Player:** Add a fullscreen button to the preview player ([5be6c1580](https://github.com/heygen-com/hyperframes/commit/5be6c1580f6e707966818ab15c349ea31814f69e), [#7726](https://github.com/heygen-com/hyperframes/pull/7726)).
> …

### [v0.9.58](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.58)
<sub>2026-11-16 · today</sub>

> **HyperFrames v0.9.58**
> Released on 2026-11-16.
> Studio exports a sealed preview's checked element reads and stand-ins, and renders, carve and the audio engine keep to the project's own files. This release also carries everything prepared as v0.9.57, which never reached npm.
> **Features**
> - **Studio:** A sealed preview frame forwards Studio's playback keys ([b741ecf13](https://github.com/heygen-com/hyperframes/commit/b741ecf1320ebad92f3a74b1e87a50a326c84db4), [#7844](https://github.com/heygen-com/hyperframes/pull/7844)).
> - **CLI:** Show and open the page to manage or cancel a paid plan ([b2e6076b7](https://github.com/heygen-com/hyperframes/commit/b2e6076b7e7f73debadd1ac91a5b64ea2c4d3ae0), [#7784](https://github.com/heygen-com/hyperframes/pull/7784)).
> …

### [v0.9.56](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.56)
<sub>2026-11-16 · yesterday</sub>

> **HyperFrames v0.9.56**
> Released on 2026-11-16.
> Studio's preview and the local servers now act only for their own pages. The CLI keeps its cache, history and restores inside the project. The arm64 Lambda image ships only the reviewed ffmpeg build, and large previews build faster.
> **Fixes**
> - **Studio Server:** The composition file servers no longer serve credential or tool-state files ([014326b40](https://github.com/heygen-com/hyperframes/commit/014326b40bf22bebb77a5cf08a50d5b0968c112e), [#7889](https://github.com/heygen-com/hyperframes/pull/7889)).
> - **Studio Server:** Lint and probe run only for requests from Studio's own pages ([bbac8900e](https://github.com/heygen-com/hyperframes/commit/bbac8900ea9201dca8aacdd17387e3275a9e6d84), [#7894](https://github.com/heygen-com/hyperframes/pull/7894)).
> …

### [v0.9.55](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.55)
<sub>2026-11-15 · yesterday</sub>

> **HyperFrames v0.9.55**
> Released on 2026-11-15.
> A sealed Studio preview now plays a video's proxy copy and reloads under one current frame token. Cloud render sends one zip when it fits and uploads only the largest media. The file servers check the Host they are asked under, and publish and cloud render staging skip other computers' network shares.
> **Fixes**
> - **Studio Server:** Sub-composition head and root tag scans take linear time ([ceb969dba](https://github.com/heygen-com/hyperframes/commit/ceb969dbacff281ec1fdddf9fe22c0fcd34fb663), [#7866](https://github.com/heygen-com/hyperframes/pull/7866)).
> - **CLI:** The engine and CLI share one trusted PATH rule, and a skipped project copy says why ([e2430edec](https://github.com/heygen-com/hyperframes/commit/e2430edecf5492a02a363eaa5c30ad2708af5aee), [#7801](https://github.com/heygen-com/hyperframes/pull/7801)).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix(studio): a layer reorder is one undo step again (#8072)](https://github.com/heygen-com/hyperframes/commit/df31ce2b15fd132432de6d39007ad345d5f5389e) | miguel-heygen |
| 2026-11-17 | [fix(studio): audio meters and audio groups work in a sealed preview (…](https://github.com/heygen-com/hyperframes/commit/93a4d29c032bec4726372e9db4a1ffff96462fac) | miguel-heygen |
| 2026-11-17 | [fix(studio): adding a track no longer remounts every clip on the time…](https://github.com/heygen-com/hyperframes/commit/b064e40e13810a73ddf27c4e467fd8a5ba33400d) | miguel-heygen |
| 2026-11-17 | [fix(studio-server): a project file is never served as a service worke…](https://github.com/heygen-com/hyperframes/commit/b4acc1a1da9b36e9e0e35e73e47697d6a59ed1ff) | miguel-heygen |
| 2026-11-17 | [feat(core): the preview can stream an element's geometry to the edito…](https://github.com/heygen-com/hyperframes/commit/f9c5ed07bfc287b4097676b6c06e46b8f652e6c8) | miguel-heygen |
| 2026-11-17 | [perf(engine): check still frames on several pages at once so text fil…](https://github.com/heygen-com/hyperframes/commit/8ec97da011f8746b6a82a03356ed3808aa7dfc6b) | miguel-heygen |
| 2026-11-17 | [fix(release): publish to npm with the job's OIDC token, not a stored …](https://github.com/heygen-com/hyperframes/commit/c106793f79f155626e7fba7602b22a769b0af4ba) | miguel-heygen |
| 2026-11-17 | [fix(core): a held video picture is drawn through a VideoFrame closed …](https://github.com/heygen-com/hyperframes/commit/43e5b7cecdd66d2df14cee219bb08db27da3d88f) | miguel-heygen |
| 2026-11-17 | [test(core): the reloaded-video playhead test builds a smaller film so…](https://github.com/heygen-com/hyperframes/commit/34f98e6a04e572296e314485d8e2f330edb0ca69) | miguel-heygen |
| 2026-11-17 | [fix(producer): leave outside links out of site listings by default an…](https://github.com/heygen-com/hyperframes/commit/fbb4838525313e4acb379963e7544fc621db781a) | jrusso1020 |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
