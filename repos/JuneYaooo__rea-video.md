# JuneYaooo/rea-video

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/JuneYaooo/rea-video)

> Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖼 Image & video generation |
| **Project** | — |
| **Why it's worth a look** | Reverse-engineer any video shot by shot |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 13.3k |
| 🍴 **Forks** | 1.9k |
| 🐞 **Open issues + PRs** | [8](https://github.com/JuneYaooo/rea-video/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering` `remotion` `reverse-engineering` `short-video` `shot-detection` `subtitles` `video-analysis` `video-breakdown` `video-editing` `video-generation` `vlm` `videomd` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-10-29 |
| 📦 **Latest release** | [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 73.9 MB |
| 🌐 **Website** | https://www.reavideo.ai/ |

## 📦 Recent releases

### [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0)
<sub>2026-11-11 · 13d ago</sub>

> **视频拆解标准包 Reel，报告重写，音效单独分离**
> 这一版定下了视频拆解的标准包格式：拆片包（Reel）。拆一条视频现在得到两样东西：给人看的报告（HTML / PDF），和给模型、下游项目读的拆片包。格式介绍和规范见 [docs/reel.md](https://github.com/JuneYaooo/rea-video/blob/v0.1.0/docs/reel.md)。
> **拆片包 Reel**
> - 四层逐级展开：卡片 → 概览和地图 → 时间线（一行一镜）→ 单镜文件，最后才是完整数据。一条 3 分钟口播读到概览约 2k token，完整数据约 19 万 token。
> - 每个文件开头写着自己的 token 数；看到的和推断的分开写，时间线里推断的键名带 `~`。
> - 字段有 JSON Schema（`rea_video/reel.schema.json`）。`rea-video reel out/ref --check` 检查一个目录是否合格，`reel.read()` 读出结构化数据。
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Add 3D motion forensics, capability-gated edit/frame routing, DP subc…](https://github.com/JuneYaooo/rea-video/commit/c11f1bd8fd3edd26a40e8f45be828be685417700) | JuneYaooo |
| 2026-11-25 | [Tighten report HTML rendering](https://github.com/JuneYaooo/rea-video/commit/8b40ef79beffa4d9a9a8c5e407c64ba11192063c) | JuneYaooo |
| 2026-11-25 | [Broaden code-render remake guidance](https://github.com/JuneYaooo/rea-video/commit/f8884a086caad66bea814456ff7fda248f05a011) | JuneYaooo |
| 2026-11-24 | [Fix ref-image guard on non-multiref models, English separators, and l…](https://github.com/JuneYaooo/rea-video/commit/fc69e194bdb4da91f72420c58debbc38eee647f5) | JuneYaooo |
| 2026-11-24 | [Tighten real-face check, dialogue quote escaping, and rewrite validation](https://github.com/JuneYaooo/rea-video/commit/5e6391f9a2d4ceda83e7dac25bd9675ce763eba9) | JuneYaooo |
| 2026-11-24 | [Tailor remake plans, prompt drafts, and API options to each video model](https://github.com/JuneYaooo/rea-video/commit/6c8dd9de06f89d658b26a9d0c52f55a4d775741d) | JuneYaooo |
| 2026-11-24 | [Read clip lengths more reliably](https://github.com/JuneYaooo/rea-video/commit/0449f76b151c70ead5a4bb3d08623ff283af3985) | JuneYaooo |
| 2026-11-24 | [Keep a dissolve's measured span when shots are rebuilt from the survey](https://github.com/JuneYaooo/rea-video/commit/4440430ee3bbb1b369a61f31bb664d2c57093f87) | HEOJUNFO |
| 2026-11-24 | [Tighten how survey cuts join a measured transition](https://github.com/JuneYaooo/rea-video/commit/763673b5e53101d29173981159b0e48e0a708ba5) | JuneYaooo |
| 2026-11-24 | [Keep a measured dissolve when the survey calls a cut inside it](https://github.com/JuneYaooo/rea-video/commit/de6b61802e8b6f289af493946b7083072466d63b) | HEOJUNFO |

[See all commits ↗](https://github.com/JuneYaooo/rea-video/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuneYaooo/rea-video.git
```
