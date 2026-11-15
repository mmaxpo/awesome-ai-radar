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
| ⭐ **Stars** | 84.5k |
| 🍴 **Forks** | 7.8k |
| 🐞 **Open issues + PRs** | [298](https://github.com/heygen-com/hyperframes/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 9% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `animation` `ffmpeg` `framework` `gsap` `html` `mcp` `puppeteer` `rendering` `typescript` `ai-agents` `claude-code` `html-to-video` `motion-graphics` `video-editor` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-03-10 |
| 📦 **Latest release** | [v0.9.52](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.52) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 528.0 MB |
| 🌐 **Website** | https://hyperframes.heygen.com |

## 📦 Recent releases

### [v0.9.52](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.52)
<sub>2026-11-15 · today</sub>

> **HyperFrames v0.9.52**
> Released on 2026-11-15.
> In Studio menus, the highlighted row now follows the menu's rounded corner. The shared menu row style is exported so other apps can match it.
> **Fixes**
> - **Studio:** Menu row highlight follows the menu's corner ([b5f5ab36a](https://github.com/heygen-com/hyperframes/commit/b5f5ab36a1f4b626da9de40adf7e40257967997c), [#7791](https://github.com/heygen-com/hyperframes/pull/7791)).
> **Full changelog**
> …

### [v0.9.51](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.51)
<sub>2026-11-15 · today</sub>

> **HyperFrames v0.9.51**
> Released on 2026-11-15.
> Render services can name extra networks their renders must treat as non-public, and mapped or NAT64 addresses are judged by the IPv4 address they carry. Website capture keeps Chrome's sandbox where the host supports it, and helper programs start only from trusted folders.
> **Features**
> - **Engine:** Operators can add networks the render must treat as non-public ([b54f2079e](https://github.com/heygen-com/hyperframes/commit/b54f2079ed715e69b10c6be54909030f64827a7a), [#7790](https://github.com/heygen-com/hyperframes/pull/7790)).
> **Fixes**
> …

### [v0.9.50](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.50)
<sub>2026-11-15 · today</sub>

> **HyperFrames v0.9.50**
> Released on 2026-11-15.
> Renders now read only the media and files that belong to them, including every playlist a playlist names. Lambda renders reach only public addresses by default, like the other cloud render paths, and lint rules check large files faster.
> **Fixes**
> - **AWS Lambda:** Lambda renders reach only public addresses unless the function opts out ([e8a59bf17](https://github.com/heygen-com/hyperframes/commit/e8a59bf1774f9880109bb7a426c55825725feb74), [#7780](https://github.com/heygen-com/hyperframes/pull/7780)).
> - **Engine:** Media playlists are checked through every list they name ([f4b6aad33](https://github.com/heygen-com/hyperframes/commit/f4b6aad33251715e803e3bb84c24a0b446a5e956), [#7778](https://github.com/heygen-com/hyperframes/pull/7778)).
> …

### [v0.9.49](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.49)
<sub>2026-11-14 · today</sub>

> **HyperFrames v0.9.49**
> Released on 2026-11-14.
> Compiling a render now downloads composition scripts through the same downloader as other assets. Renders also log what kind of address the network limit refused.
> **Features**
> - **Engine:** Renders log the class of every address the proxy refuses ([89bca002e](https://github.com/heygen-com/hyperframes/commit/89bca002ef7720e94a71ef57e2a8d1624b3cb424), [#7762](https://github.com/heygen-com/hyperframes/pull/7762)).
> **Fixes**
> …

### [v0.9.48](https://github.com/heygen-com/hyperframes/releases/tag/v0.9.48)
<sub>2026-11-14 · today</sub>

> **HyperFrames v0.9.48**
> Released on 2026-11-14.
> Press ? in Studio to see every keyboard shortcut. A render service that limits the render page's network now applies the same limit to the whole render browser.
> **Features**
> - **Studio:** Press ? to open the keyboard shortcuts panel ([a03e85f43](https://github.com/heygen-com/hyperframes/commit/a03e85f43a7d2febaf801c5b96277671bd48f70d), [#7478](https://github.com/heygen-com/hyperframes/pull/7478)).
> **Fixes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [fix(cli): cloud render no longer refuses a file only an unused page n…](https://github.com/heygen-com/hyperframes/commit/45cc331e54b28040694a47e540ddc2d100cacdf3) | miguel-heygen |
| 2026-11-15 | [fix(core): pages with many CJK characters fetch fonts in several requ…](https://github.com/heygen-com/hyperframes/commit/6a8f4b5b46762e6b1631e02d6d77b29b950c88ee) | miguel-heygen |
| 2026-11-15 | [feat(cli): uploads list every file they carry from outside the projec…](https://github.com/heygen-com/hyperframes/commit/e426ce4eb44517db3f65105f1e05cb7b762cd950) | michaelwang11394 |
| 2026-11-15 | [perf(lint): scan CSS url references in linear time (#7829)](https://github.com/heygen-com/hyperframes/commit/bcf3d177d3476a1696b034544f5cfcf68404663b) | michaelwang11394 |
| 2026-11-15 | [fix(cli): hyperframes audio never looks up media on another computer'…](https://github.com/heygen-com/hyperframes/commit/eaf33bc658fbd2612753a48574fed6f9e376a511) | michaelwang11394 |
| 2026-11-15 | [fix(cli): uploads leave out outside scripts; .ts counts as video only…](https://github.com/heygen-com/hyperframes/commit/04202e8a4c2e7f334636bf1e3b07dd38c77e5b43) | michaelwang11394 |
| 2026-11-15 | [fix(cli): play and present check the Host like preview; local render …](https://github.com/heygen-com/hyperframes/commit/ac02474105bc6d2893a0ef1a79526f2952645aca) | michaelwang11394 |
| 2026-11-15 | [fix(cli): add lists files from a received config's registry as receiv…](https://github.com/heygen-com/hyperframes/commit/6a7b4df7c8bb04944b14820570b2dd7a32e76dc7) | michaelwang11394 |
| 2026-11-15 | [fix: Studio media routes refuse cross-site load, CLI escapes terminal…](https://github.com/heygen-com/hyperframes/commit/c4d60c347f324eb58dacfccee866a0b9bba7fe61) | michaelwang11394 |
| 2026-11-15 | [fix(cli): discover mounted scenes inside templates (#7822)](https://github.com/heygen-com/hyperframes/commit/a75e61f31c76d79016894e849799bdc456ac0b54) | weiweiwu007 |

[See all commits ↗](https://github.com/heygen-com/hyperframes/commits)

## ⬇️ Get it

```bash
git clone https://github.com/heygen-com/hyperframes.git
```
