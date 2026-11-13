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
| ⭐ **Stars** | 83.7k |
| 🍴 **Forks** | 7.7k |
| 🐞 **Open issues + PRs** | [248](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.41](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.41) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 526.0 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.41](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.41)
<sub>2026-11-13 · today</sub>

> **HyperFrames v0.9.41**
> Released on 2026-11-13.
> Fast capture works again on Chrome 157 and newer, which fixes Windows exports that failed at drawElementImage. Local renders keep Chrome's sandbox on where the host supports it and launch Chrome with only the environment it needs and explain a failed launch with the environment it had, cloud render --json lists the files an upload leaves out, publish copies only media, font, CSS and JS files from outside the project and leaves out the rest that came in with an import, a video variable given as a link now plays its sound once, media ids that differ only by case get separate folders so a render no longer fails with a missing file, and the Studio timeline and overlays read an opaque preview over its channel.
> **Features**
> - **CLI:** Cloud render --json lists the files an upload leaves out ([2591abfbf](https://github.com/heygen-com/hyperframes/commit/2591abfbf014c2f70fdc48ac315fd8acbd704e3d), [#7631](https://github.com/heygen-com/hyperframes/pull/7631)).
> - **Studio:** Read overlay geometry from an opaque preview over its channel ([faff4e16a](https://github.com/heygen-com/hyperframes/commit/faff4e16a8719c63234ac7a02fc3006ddf3cc375), [#7628](https://github.com/heygen-com/hyperframes/pull/7628)).
> …

### [v0.9.40](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.40)
<sub>2026-11-12 · today</sub>

> **HyperFrames v0.9.40**
> Released on 2026-11-12.
> A local render now extracts each video at about the size it is shown, so a long export of 4K footage in a 1080p film no longer fills the disk. A frame's pixels no longer depend on the frames drawn before it, render work is sized to the CPUs the process may use, and check hears a WAV whose header misstates its byte rate.
> **Features**
> - **Core:** Runtime element handles for the editing channel ([e1ddb2e16](https://github.com/heygen-com/hyperframes/commit/e1ddb2e162388fcef4b6496ceb81d02fe22fe3d3), [#7603](https://github.com/heygen-com/hyperframes/pull/7603)).
> **Fixes**
> …

### [v0.9.39](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.39)
<sub>2026-11-12 · today</sub>

> **HyperFrames v0.9.39**
> Released on 2026-11-12.
> Studio shows the move, resize and rotate readout in a chip under the element. Desktop and other hosts can now import key parsing and defaults from a light @hyperframes/studio/keys path.
> **Features**
> - **Studio:** Show the move, resize and rotate readout as a chip under the element ([6e0e03f54](https://github.com/heygen-com/hyperframes/commit/6e0e03f542beacf758d8abe86f8a448f59b2ef1e), [#7588](https://github.com/heygen-com/hyperframes/pull/7588)).
> - **Studio:** Add a light @hyperframes/studio/keys subpath for key parsing and defaults ([234fb1aee](https://github.com/heygen-com/hyperframes/commit/234fb1aeef13f8d86b4f7f4cb1af624db3a81ec2), [#7600](https://github.com/heygen-com/hyperframes/pull/7600)).
> …

### [v0.9.38](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.38)
<sub>2026-11-12 · yesterday</sub>

> **HyperFrames v0.9.38**
> Released on 2026-11-12.
> The Volume control in Studio now changes the whole clip, a paused video shows the same colors as the playing one on Mac, and edit history records which layer each edit touched. Publish also keeps Library files out for projects on cloud drives, and render servers only load assets from inside the project.
> **Features**
> - **Studio:** Record the layer name on each history entry's target ([4fad43db2](https://github.com/heygen-com/hyperframes/commit/4fad43db2010d61002cc9f9296f3c5f8bf2d4210), [#7586](https://github.com/heygen-com/hyperframes/pull/7586)).
> - **CLI:** Heygen generate defaults images to nano-banana-2.1 ([fc7cb1aad](https://github.com/heygen-com/hyperframes/commit/fc7cb1aad8d5f01361343d004de1ee7b8143ed20), [#7591](https://github.com/heygen-com/hyperframes/pull/7591)).
> …

### [v0.9.37](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.37)
<sub>2026-11-12 · yesterday</sub>

> **HyperFrames v0.9.37**
> Released on 2026-11-12.
> Sharing refuses to build an archive when it can't read `.hyperframesignore`, so ignored files stay out. `templates pull` also refuses archives that hold links.
> **Fixes**
> - **CLI:** `hyperframes templates pull` refuses an archive that holds anything other than plain files and folders, such as a symlink, hard link or device entry. Nothing is unpacked, and no partial folder is left behind. A link inside a pulled template could otherwise let preview, render and publish reach files elsewhere on your machine ([ab66e5bd7](https://github.com/heygen-com/hyperframes/commit/ab66e5bd72ad16b36a37dd1ee50d23cc21b41bb0), [#7576](https://github.com/heygen-com/hyperframes/pull/7576)).
> - **Share:** `snapshotProject` and `snapshotFiles` throw `invalid_source_ignore` again when `.hyperframesignore` can't be read. In 0.9.35 they skipped the unreadable file, so an archive built from the snapshot could include files the ignore file meant to leave out. Hosts that use these functions only for change detection should pass `{ lenientIgnore: true }` to keep the 0.9.35 behavior. `projectFingerprint` already does ([35cf03cab](https://github.com/heygen-com/hyperframes/commit/35cf03cab9e75a4f21fc90cf0dac8a08310ab6ad), [#7573](https://github.com/heygen-com/hyperframes/pull/7573)).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [fix(studio): open the canvas context menu when a pointer move overtak…](https://github.com/heygen-com/hyperframes/commit/d208281091b1c00db1724a2ee3db0055955eb41b) | jrusso1020 |
| 2026-11-13 | [feat(studio): layers panel and marquee read an opaque preview over it…](https://github.com/heygen-com/hyperframes/commit/be67089a80b59be945d84e09d400a4ece254daef) | jrusso1020 |
| 2026-11-13 | [docs(adopters): add varg (#7640)](https://github.com/heygen-com/hyperframes/commit/ff687fed9900ed6a531057f2ebbed7ad43e801c6) | SecurityQQ |
| 2026-11-13 | [chore: release v0.9.41 (#7632)](https://github.com/heygen-com/hyperframes/commit/20084cbe67f37e2a9386402165f66233d2824baa) | miguel-heygen |
| 2026-11-13 | [feat(studio): canvas click, hover and timeline select read an opaque …](https://github.com/heygen-com/hyperframes/commit/7e04f3cce8a4d3e7c4e04590828104c37c2be8cb) | jrusso1020 |
| 2026-11-13 | [fix(cli): copy only media, font, CSS and JS files from outside the pr…](https://github.com/heygen-com/hyperframes/commit/89a7aa30042e34eb2643205e1dca6a18b642cf0e) | jrusso1020 |
| 2026-11-13 | [fix(engine): keep media ids that differ only by case in separate fold…](https://github.com/heygen-com/hyperframes/commit/b54e4981f2f710e928215e3138e1fa075b1d1108) | miguel-heygen |
| 2026-11-13 | [fix(producer): a video variable given as a link plays its sound once …](https://github.com/heygen-com/hyperframes/commit/2760fa11916d37a512044f6243fcbbaba43fad3a) | miguel-heygen |
| 2026-11-13 | [fix(engine): diagnose a failed Chrome launch with the env it had (#7634)](https://github.com/heygen-com/hyperframes/commit/9701f4bbf3d1ef41753dcf5613fead937e1edf2c) | jrusso1020 |
| 2026-11-13 | [feat(cli): cloud render --json lists the files an upload leaves out (…](https://github.com/heygen-com/hyperframes/commit/2591abfbf014c2f70fdc48ac315fd8acbd704e3d) | jrusso1020 |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
