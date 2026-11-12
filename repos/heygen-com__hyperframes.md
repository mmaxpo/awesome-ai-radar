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
| ⭐ **Stars** | 83.2k |
| 🍴 **Forks** | 7.7k |
| 🐞 **Open issues + PRs** | [246](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.38](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.38) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 526.0 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.38](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.38)
<sub>2026-11-12 · today</sub>

> **HyperFrames v0.9.38**
> Released on 2026-11-12.
> The Volume control in Studio now changes the whole clip, a paused video shows the same colors as the playing one on Mac, and edit history records which layer each edit touched. Publish also keeps Library files out for projects on cloud drives, and render servers only load assets from inside the project.
> **Features**
> - **Studio:** Record the layer name on each history entry's target ([4fad43db2](https://github.com/heygen-com/hyperframes/commit/4fad43db2010d61002cc9f9296f3c5f8bf2d4210), [#7586](https://github.com/heygen-com/hyperframes/pull/7586)).
> - **CLI:** Heygen generate defaults images to nano-banana-2.1 ([fc7cb1aad](https://github.com/heygen-com/hyperframes/commit/fc7cb1aad8d5f01361343d004de1ee7b8143ed20), [#7591](https://github.com/heygen-com/hyperframes/pull/7591)).
> …

### [v0.9.37](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.37)
<sub>2026-11-12 · today</sub>

> **HyperFrames v0.9.37**
> Released on 2026-11-12.
> Sharing refuses to build an archive when it can't read `.hyperframesignore`, so ignored files stay out. `templates pull` also refuses archives that hold links.
> **Fixes**
> - **CLI:** `hyperframes templates pull` refuses an archive that holds anything other than plain files and folders, such as a symlink, hard link or device entry. Nothing is unpacked, and no partial folder is left behind. A link inside a pulled template could otherwise let preview, render and publish reach files elsewhere on your machine ([ab66e5bd7](https://github.com/heygen-com/hyperframes/commit/ab66e5bd72ad16b36a37dd1ee50d23cc21b41bb0), [#7576](https://github.com/heygen-com/hyperframes/pull/7576)).
> - **Share:** `snapshotProject` and `snapshotFiles` throw `invalid_source_ignore` again when `.hyperframesignore` can't be read. In 0.9.35 they skipped the unreadable file, so an archive built from the snapshot could include files the ignore file meant to leave out. Hosts that use these functions only for change detection should pass `{ lenientIgnore: true }` to keep the 0.9.35 behavior. `projectFingerprint` already does ([35cf03cab](https://github.com/heygen-com/hyperframes/commit/35cf03cab9e75a4f21fc90cf0dac8a08310ab6ad), [#7573](https://github.com/heygen-com/hyperframes/pull/7573)).
> …

### [v0.9.36](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.36)
<sub>2026-11-12 · today</sub>

> **HyperFrames v0.9.36**
> Released on 2026-11-11.
> Motion blur previews more smoothly when you lower preview quality. Renders still draw full-quality blur.
> **Features**
> - **Core:** Lowering preview quality now makes motion blur lighter too. The preview draws 16 blur copies at 1/2 and 8 at 1/4 and below, instead of 32. Renders always draw 32. A host that lowers quality on choppy playback can now do so for a film slowed only by blur ([6cc734fd2](https://github.com/heygen-com/hyperframes/commit/6cc734fd24e25c09e28824b5543fa4f85612f02c), [#7547](https://github.com/heygen-com/hyperframes/pull/7547)).
> **Fixes**
> …

### [v0.9.35](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.35)
<sub>2026-11-11 · today</sub>

> **HyperFrames v0.9.35**
> Released on 2026-11-11.
> Private files like `.env` and git data stay out of preview bundles, and local sharing only answers your own machine. Sharing also keeps tracking changes when `.hyperframesignore` uses gitignore patterns.
> **Fixes**
> - **Security:** Preview bundles never include `.env` files or git data, even through a link. A render that names one of these files now stops with an error. Local sharing only answers this machine, so sharing from Studio in a container now gets a 403 ([a243169f8](https://github.com/heygen-com/hyperframes/commit/a243169f8a10fa26fe9e9d1d1623d68445e2a3c7), [#7563](https://github.com/heygen-com/hyperframes/pull/7563)).
> - **Security:** Helper programs are found by walking your trusted `PATH` folders directly. On Windows, the working folder is never searched ([9a048ac01](https://github.com/heygen-com/hyperframes/commit/9a048ac019e919f9e9c37b1b764172676434511e), [#7562](https://github.com/heygen-com/hyperframes/pull/7562)).
> …

### [v0.9.34](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.34)
<sub>2026-11-11 · today</sub>

> **HyperFrames v0.9.34**
> Released on 2026-11-11.
> HyperFrames now runs helper programs like FFmpeg only from where they are installed, never from a project folder. Renders can also refuse variables a page does not declare, when that check is turned on.
> **Features**
> - **Producer:** With strict variables turned on, a render fails when it is given a variable the page does not declare. It is off by default, so renders are unchanged ([f312fca7e](https://github.com/heygen-com/hyperframes/commit/f312fca7e2098524af07055bdf6c20a3706d6f89), [#7548](https://github.com/heygen-com/hyperframes/pull/7548)).
> **Fixes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [chore: release v0.9.39 (#7605)](https://github.com/heygen-com/hyperframes/commit/256675f92c44827ac3309cac615f46424dfca895) | miguel-heygen |
| 2026-11-12 | [feat(studio): show the move, resize and rotate readout as a chip unde…](https://github.com/heygen-com/hyperframes/commit/6e0e03f542beacf758d8abe86f8a448f59b2ef1e) | miguel-heygen |
| 2026-11-12 | [fix(ci): a release fails its checks when its notes miss a commit merg…](https://github.com/heygen-com/hyperframes/commit/5d2914f7ceb626e750b1f08feee7fa2bf628f025) | miguel-heygen |
| 2026-11-12 | [feat(studio): add a light @hyperframes/studio/keys subpath for key pa…](https://github.com/heygen-com/hyperframes/commit/234fb1aeef13f8d86b4f7f4cb1af624db3a81ec2) | miguel-heygen |
| 2026-11-12 | [feat(studio): picker styles and composition size read an opaque previ…](https://github.com/heygen-com/hyperframes/commit/01618d504aed5f8ac935394b67156a4c43baf5e7) | jrusso1020 |
| 2026-11-12 | [feat(studio): playback and timeline reads go over the preview's messa…](https://github.com/heygen-com/hyperframes/commit/940963afaa5f2c0bfae3444aa284f5437b75a2f7) | jrusso1020 |
| 2026-11-12 | [chore: release v0.9.38 (#7594)](https://github.com/heygen-com/hyperframes/commit/1ec03c4e190fb7262c8ad65884dfd576a81f1ebd) | miguel-heygen |
| 2026-11-12 | [fix(studio): a preview reload survives its pane unmounting mid-load (…](https://github.com/heygen-com/hyperframes/commit/5a3e46235fe1f749006af6bacae01c684f2866ca) | miguel-heygen |
| 2026-11-12 | [perf(lint): parse each style block once per lint instead of once per …](https://github.com/heygen-com/hyperframes/commit/32cacab74bb52076efb9e84258f382200b56b19e) | miguel-heygen |
| 2026-11-12 | [docs(skills): name the model next to each media-use image price (#7592)](https://github.com/heygen-com/hyperframes/commit/748bfe3b2beef424c289dd12cc146b8dfcfa019c) | jrusso1020 |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
