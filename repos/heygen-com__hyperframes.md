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
| ⭐ **Stars** | 88.7k |
| 🍴 **Forks** | 8.3k |
| 🐞 **Open issues + PRs** | [310](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` `agent-skills` `ai-video` `ai-video-editor` `remotion-alternative` `video-editing` `video-generation` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.86](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.86) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 541.3 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.86](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.86)
<sub>2026-11-23 · today</sub>

> **HyperFrames v0.9.86**
> Released on 2026-11-23.
> A save during an import keeps its own undo step, and full-size stills count their real memory, so the cache frees them. Text on a sealed preview can now be edited in place, and sealed recordings move the layer live.
> **Features**
> - **Studio:** Edit text in place on a sealed preview's canvas ([8d2783561](https://github.com/heygen-com/hyperframes/commit/8d2783561f4eb3038a2b6305cc9f160651834a12), [#8183](https://github.com/heygen-com/hyperframes/pull/8183)).
> **Fixes**
> …

### [v0.9.85](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.85)
<sub>2026-11-23 · today</sub>

> **HyperFrames v0.9.85**
> Released on 2026-11-23.
> Apps that embed Studio can now read a sealed preview's page markup. Undo keeps a save made during an import, sealed resizes keep the dragged corner under the pointer, and the skills ask before usage notes or destroy.
> **Features**
> - **Studio:** Apps embedding Studio can read a sealed preview's page markup ([3134c5f1b](https://github.com/heygen-com/hyperframes/commit/3134c5f1b88295d7b6507228a4c2ddeb3298c846), [#8564](https://github.com/heygen-com/hyperframes/pull/8564)).
> **Fixes**
> …

### [v0.9.84](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.84)
<sub>2026-11-23 · today</sub>

> **HyperFrames v0.9.84**
> Released on 2026-11-23.
> A new blank project opens on an empty timeline again. Leftover render folders are cleaned up reliably on macOS and Windows, and capture finishes on a small host with no GPU.
> **Fixes**
> - **Lint:** A page with thousands of scripts and tags lints in seconds ([148f9deb7](https://github.com/heygen-com/hyperframes/commit/148f9deb771f1c47f834f609e9cc667ab15f36c5), [#8551](https://github.com/heygen-com/hyperframes/pull/8551)).
> - **CLI:** Keep objects sliding offscreen in one shot ([b734a4114](https://github.com/heygen-com/hyperframes/commit/b734a411420e7d5e738d6a07b6a5ac097f40ee74), [#8552](https://github.com/heygen-com/hyperframes/pull/8552)).
> …

### [v0.9.83](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.83)
<sub>2026-11-22 · today</sub>

> **HyperFrames v0.9.83**
> Released on 2026-11-22.
> Compiling a page with thousands of clips or style rules stays fast. The notes also list a fix that shipped in v0.9.82: a sandboxed app reads project history again.
> **Fixes**
> - **Studio Server:** A sandboxed history read no longer fails with EPERM while the app holds it, shipped in v0.9.82 ([02450e3e2](https://github.com/heygen-com/hyperframes/commit/02450e3e2e9f9792589399d3a10b7a4ae34f6f2e), [#8529](https://github.com/heygen-com/hyperframes/pull/8529))
> **Performance**
> …

### [v0.9.82](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.82)
<sub>2026-11-22 · today</sub>

> **HyperFrames v0.9.82**
> Released on 2026-11-22.
> A preview loads GSAP's motion path plugin from the page's own GSAP folder or the host's copy, so it works with no network. Sealed previews get more fixes, from sound and the keyboard to moves inside nested compositions.
> **Fixes**
> - **Producer:** A render serves every GSAP the CLI ships, and its own when the CDN is blocked ([8c9c94572](https://github.com/heygen-com/hyperframes/commit/8c9c94572a148c62675a4e181cec1e3480e75bc4), [#8349](https://github.com/heygen-com/hyperframes/pull/8349)).
> - **Core:** The motion path plugin loads from beside the page's own GSAP, never a CDN it did not name ([80f45de33](https://github.com/heygen-com/hyperframes/commit/80f45de33da92c8f765fd184a0ac4cb8e2ade261), [#8523](https://github.com/heygen-com/hyperframes/pull/8523)).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(studio): a ProRes clip's preview copy is no longer starved by thu…](https://github.com/heygen-com/hyperframes/commit/bebfdd13e909b9aea05f3b7d1319f579cb28f2b2) | miguel-heygen |
| 2026-11-23 | [fix(core): a sealed recording starts on a composition without GSAP (#…](https://github.com/heygen-com/hyperframes/commit/bc33d032e55b387580fa7b383cf9cce139701e8b) | miguel-heygen |
| 2026-11-23 | [chore: release v0.9.86 (#8595)](https://github.com/heygen-com/hyperframes/commit/574b5e3d3bbf526809d268a6728f9c5ce52e18bb) | miguel-heygen |
| 2026-11-23 | [feat(studio): edit text in place on a sealed preview's canvas (#8183)](https://github.com/heygen-com/hyperframes/commit/8d2783561f4eb3038a2b6305cc9f160651834a12) | miguel-heygen |
| 2026-11-23 | [fix(studio): a sealed gesture recording moves the layer live in the p…](https://github.com/heygen-com/hyperframes/commit/c0753d2ad6beb46ab097b9a598d9408f8070c113) | miguel-heygen |
| 2026-11-23 | [fix(lint): read each linked file once and stop at one page's size lim…](https://github.com/heygen-com/hyperframes/commit/70d547cace34c0107c4519f6e8d3df82cae828ac) | miguel-heygen |
| 2026-11-23 | [fix(studio): a cancelled media read is not retried or logged as a fai…](https://github.com/heygen-com/hyperframes/commit/112e52c3c5bfd6e41f7616e7ddd0616684bcc146) | miguel-heygen |
| 2026-11-23 | [fix(studio-server): a save asked to be recorded keeps its own undo st…](https://github.com/heygen-com/hyperframes/commit/5409387218cc0e695552f8a5dccac93484dc32c0) | miguel-heygen |
| 2026-11-23 | [Revert "test(studio): measure a sealed press by the element until the…](https://github.com/heygen-com/hyperframes/commit/ceaba36390d54e4459153b58f875bcb5a555955b) | miguel-heygen |
| 2026-11-23 | [test(cli): describe the team descriptor in prose, not as a citation (…](https://github.com/heygen-com/hyperframes/commit/c451acae33789969c2f0e19774ea9df07a7100bc) | WaterrrForever |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
