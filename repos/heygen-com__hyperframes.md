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
| ⭐ **Stars** | 82.7k |
| 🍴 **Forks** | 7.6k |
| 🐞 **Open issues + PRs** | [237](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.33](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.33) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 525.5 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.33](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.33)
<sub>2026-11-11 · today</sub>

> **HyperFrames v0.9.33**
> Released on 2026-11-11.
> Clips that start partway into a voice recording now keep their sound to the end, even when the WAV file misreports its own byte rate. Variable-bound media also renders at the right length and loudness.
> **Fixes**
> - **Engine:** A clip that starts partway into a WAV whose header gives the wrong byte rate now plays the right sound to its end, instead of going quiet early or staying silent ([7ae1ae649](https://github.com/heygen-com/hyperframes/commit/7ae1ae64942f036a18c546bef024121d8df76ef2), [#7541](https://github.com/heygen-com/hyperframes/pull/7541)).
> - **Share:** When you reach the hourly limit on review versions, the message now explains that limit ([8a15d9fee](https://github.com/heygen-com/hyperframes/commit/8a15d9feedc62dc9695246dceda9271a6d0a08e9), [#7539](https://github.com/heygen-com/hyperframes/pull/7539)).
> …

### [v0.9.32](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.32)
<sub>2026-11-11 · today</sub>

> **HyperFrames v0.9.32**
> Released on 2026-11-11.
> Long films that are slow to open now render instead of failing before their first frame. The CLI, Studio and the renderer also stop a project folder from choosing what they run or serve.
> **Features**
> - SDR MP4 renders can keep full colour detail with `--chroma-subsampling 444`, for masters that will be re-encoded; the default is unchanged ([1a9fb8acb](https://github.com/heygen-com/hyperframes/commit/1a9fb8acb65d044e1732381fad953b69c3604648), [#5820](https://github.com/heygen-com/hyperframes/pull/5820)).
> - **Producer:** The render stream's complete event names the producer version that rendered it ([7afa05a78](https://github.com/heygen-com/hyperframes/commit/7afa05a782c452ca76af22bdde12d4cddaf64c60), [#7515](https://github.com/heygen-com/hyperframes/pull/7515)).
> …

### [v0.9.28-alpha.3](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.28-alpha.3) _(pre-release)_
<sub>2026-11-10 · today</sub>

> **Full Changelog**: https://github.com/heygen-com/hyperframes/compare/v0.9.28-alpha.2...v0.9.28-alpha.3

### [v0.9.31](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.31)
<sub>2026-11-10 · today</sub>

> **HyperFrames v0.9.31**
> Released on 2026-11-10.
> In Safari, long videos no longer load the whole file at once, and playing clips keep their source. The Studio dev server now checks the Host on its API routes, so a tunnel or remote setup may need one setting.
> **Fixes**
> - **Core:** In Safari, a small video file keeps its preload, and a clip that is playing keeps its source ([cda84222a](https://github.com/heygen-com/hyperframes/commit/cda84222aa12716f2ceb92b45629487be81a0601), [#7498](https://github.com/heygen-com/hyperframes/pull/7498)).
> - **Studio:** The Studio dev server now checks the Host header on its API routes too, as the preview server does since 0.9.30. A tunnel, Codespaces or remote dev host that worked before can now get a 403: name the host in `HYPERFRAMES_PREVIEW_ALLOWED_HOSTS` (comma separated), which now also reaches the dev server's own allowed hosts ([b0835262a](https://github.com/heygen-com/hyperframes/commit/b0835262ae5179f27d95ac2d140298f83fbf2fd1), [#7493](https://github.com/heygen-com/hyperframes/pull/7493)).
> …

### [v0.9.28-alpha.2](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.28-alpha.2) _(pre-release)_
<sub>2026-11-10 · today</sub>

> **Full Changelog**: https://github.com/heygen-com/hyperframes/compare/v0.9.28-alpha.1...v0.9.28-alpha.2

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [fix(studio-server): load fonts and modules only in the Studio's own p…](https://github.com/heygen-com/hyperframes/commit/ffb13c3b62a1b8ed98fdcd835f15412d0a7ca7e6) | jrusso1020 |
| 2026-11-11 | [fix(skills): plugin launcher and media helpers run the pinned CLI, no…](https://github.com/heygen-com/hyperframes/commit/a8fe3a5b6844c9f1ae1a4473793eeb11dfcec627) | jrusso1020 |
| 2026-11-11 | [fix(cli): preview uses the bundled Studio unless local Studio mode is…](https://github.com/heygen-com/hyperframes/commit/668983e1a63efb7618049c73cf9dcad2a5977a4e) | jrusso1020 |
| 2026-11-11 | [fix: take helper programs only from install locations, never the proj…](https://github.com/heygen-com/hyperframes/commit/84799bdc59b18f6a3df6595d8a8d1ec03dfde673) | jrusso1020 |
| 2026-11-11 | [feat(producer): fail a render whose variables the page does not decla…](https://github.com/heygen-com/hyperframes/commit/f312fca7e2098524af07055bdf6c20a3706d6f89) | miguel-heygen |
| 2026-11-11 | [fix(cli): refuse more coding-agent instruction files in registry inst…](https://github.com/heygen-com/hyperframes/commit/9bab57ab48db70f3aee3376f6bb86af5f7c50583) | jrusso1020 |
| 2026-11-11 | [fix(core): fall back to a direct write when link() is denied with EAC…](https://github.com/heygen-com/hyperframes/commit/f36463e292f4487daef522ec9b19c2dacceb6adb) | miguel-heygen |
| 2026-11-11 | [fix(cli,studio-server): limit registry installs and Studio file write…](https://github.com/heygen-com/hyperframes/commit/b96c82b785ab8fbd9c030c093de9c39e5dc39342) | jrusso1020 |
| 2026-11-11 | [fix(studio-server): run thumbnail captures in an opaque origin (#7528)](https://github.com/heygen-com/hyperframes/commit/80cda85d761128e121a1cef0f1378ad342472411) | jrusso1020 |
| 2026-11-11 | [test(engine): the URL-read concurrency test passes on machines with 3…](https://github.com/heygen-com/hyperframes/commit/3ad7611f9fd36c1cef589c59b116ad7043c3b041) | miguel-heygen |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
