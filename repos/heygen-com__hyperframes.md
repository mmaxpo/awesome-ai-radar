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
| ⭐ **Stars** | 86.3k |
| 🍴 **Forks** | 8.0k |
| 🐞 **Open issues + PRs** | [294](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.66](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.66) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 534.1 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.66](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.66)
<sub>2026-11-18 · today</sub>

> **HyperFrames v0.9.66**
> Released on 2026-11-18.
> Studio's sealed preview now takes property edits, crops, resizes and plays slideshow scenes. A preview no longer sits in Buffering when a clip stops downloading, and the player can carry your own branding.
> **Features**
> - **Player:** Add customizable branding to the preview player ([a9b4745f1](https://github.com/heygen-com/hyperframes/commit/a9b4745f1f9773cc0dcd1f6d81b942ce97335f87), [#7718](https://github.com/heygen-com/hyperframes/pull/7718)).
> **Fixes**
> …

### [v0.9.65](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.65)
<sub>2026-11-18 · today</sub>

> **HyperFrames v0.9.65**
> Released on 2026-11-17.
> Studio's sealed preview now draws motion paths, reads keyframes and keeps a moved layer in place when you add a keyframe. Studio's error and analytics events no longer carry your error text, file paths or selectors.
> **Features**
> - **Studio Server:** Let a host count the requests the API refuses with 403 ([078e54d00](https://github.com/heygen-com/hyperframes/commit/078e54d0089f57c9513dbcb5d07ea092f7be907b), [#8049](https://github.com/heygen-com/hyperframes/pull/8049)).
> **Fixes**
> …

### [v0.9.64](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.64)
<sub>2026-11-17 · today</sub>

> **HyperFrames v0.9.64**
> Released on 2026-11-17.
> Hover and thumbnail captures no longer wait on a 4K clip's preview copy. In a sealed preview, scrubbing plays the music track and timeline rows know their element. `hyperframes check` finds text over a face. Studio's proxy refuses requests with no same-site signal. A stable release now needs a second maintainer besides its approver.
> **Features**
> - **CLI:** `check` finds text over a face, `measure` cuts the names of resumed takes, and `measure` reports hands ([820d63d7f](https://github.com/heygen-com/hyperframes/commit/820d63d7f9e2a5fafc0a0230e8b4c8dc5447d995), [#8074](https://github.com/heygen-com/hyperframes/pull/8074)).
> **Fixes**
> …

### [v0.9.63](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.63)
<sub>2026-11-17 · today</sub>

> **HyperFrames v0.9.63**
> Released on 2026-11-17.
> Studio's sealed preview shows audio meters and audio groups, a layer reorder is one undo step again, and text films start sooner. No HyperFrames server serves a project file as a service worker's script. This release also carries every change listed for 0.9.62. That version never reached npm: the merge queue landed it in one push with another PR, and the publish read only the push's last commit. Since #8077 a release publishes from its own commit in the push.
> **Features**
> - **Core:** The preview can stream an element's geometry to the editor every frame ([f9c5ed07b](https://github.com/heygen-com/hyperframes/commit/f9c5ed07bfc287b4097676b6c06e46b8f652e6c8), [#8052](https://github.com/heygen-com/hyperframes/pull/8052)).
> **Performance**
> …

### [v0.9.61](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.61)
<sub>2026-11-17 · yesterday</sub>

> **HyperFrames v0.9.61**
> Released on 2026-11-17.
> Received projects and the files they reach stay inside their own folder across render, preview and Studio, and a sealed preview reloads in place in a fraction of a second. This release also carries every change listed for 0.9.60. That version never reached npm: its publish was refused because it ran from the release PR's merge ref, and since #8020 a stable release publishes from the push to `main` that merges it.
> **Features**
> - **Engine:** Render telemetry says why a page cannot reuse still frames ([c8df284b2](https://github.com/heygen-com/hyperframes/commit/c8df284b2ed15ae0ade05bf90e95192d05f3d1c6), [#7993](https://github.com/heygen-com/hyperframes/pull/7993)).
> - **Studio:** An element's source-parsed animations are part of Studio's API ([efc91fc87](https://github.com/heygen-com/hyperframes/commit/efc91fc877d89d8057611dd87c81220be46df9a2), [#8061](https://github.com/heygen-com/hyperframes/pull/8061)).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [perf(core): count an svg id scope's renames once, not on every styles…](https://github.com/heygen-com/hyperframes/commit/67410727e63cd0de3e4013d1de2dd997790a7866) | miguel-heygen |
| 2026-11-18 | [fix(cli): the very-many-files received-render test stops timing out o…](https://github.com/heygen-com/hyperframes/commit/3db2da06c9eae7ecccb74c4e777739a2677d7aa9) | miguel-heygen |
| 2026-11-18 | [fix(studio-server): an inserted scene names its file from the project…](https://github.com/heygen-com/hyperframes/commit/f38e1e6defe59c97d2acec2595bafe34ac97fc9c) | miguel-heygen |
| 2026-11-18 | [fix(studio): refused group, freeze frame and animation saves keep the…](https://github.com/heygen-com/hyperframes/commit/2efb55ecb5e5f5df02192b1de53facbb26cd90e5) | miguel-heygen |
| 2026-11-18 | [fix(producer): fetch each remote script and stylesheet once, a few at…](https://github.com/heygen-com/hyperframes/commit/4bdf9181b4069fbe6ea2a230ad7eb695948057c8) | miguel-heygen |
| 2026-11-18 | [fix(studio): a 3D slider drag previews live in a sealed preview (#8148)](https://github.com/heygen-com/hyperframes/commit/75992d82adf5d33aa874809a406b819e540c3348) | miguel-heygen |
| 2026-11-18 | [chore: release v0.9.66 (#8172)](https://github.com/heygen-com/hyperframes/commit/1a82f6e9d65a2e50502cc411711b6a28481738c0) | miguel-heygen |
| 2026-11-18 | [chore(aws-lambda): give the packed size budget its usual 5% headroom …](https://github.com/heygen-com/hyperframes/commit/c696c0e1573d45111f117e365b9095d157638a53) | jrusso1020 |
| 2026-11-18 | [test(studio): edit accuracy waits for Studio to report the film loade…](https://github.com/heygen-com/hyperframes/commit/b90b8d1bb308f19ab82b7eac73a5fadaac88bf49) | miguel-heygen |
| 2026-11-18 | [revert(producer): a render that fails on a missing file stops naming …](https://github.com/heygen-com/hyperframes/commit/94d06663b114de340cb74f4368936f43810c2850) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
