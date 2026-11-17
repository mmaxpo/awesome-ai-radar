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
| ⭐ **Stars** | 10.1k |
| 🍴 **Forks** | 1.5k |
| 🐞 **Open issues + PRs** | [5](https://github.com/JuneYaooo/rea-video/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering` `remotion` `reverse-engineering` `short-video` `shot-detection` `subtitles` `video-analysis` `video-breakdown` `video-editing` `video-generation` `vlm` `videomd` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-10-29 |
| 📦 **Latest release** | [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 153.6 MB |
| 🌐 **Website** | https://www.reavideo.ai/ |

## 📦 Recent releases

### [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0)
<sub>2026-11-11 · 5d ago</sub>

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
| 2026-11-17 | [Keep the install handoff to ChatCut](https://github.com/JuneYaooo/rea-video/commit/94625f2cc6ad738fb4fd2c2126fbc857428c8782) | JuneYaooo |
| 2026-11-17 | [Note ChatCut also edits live-action footage](https://github.com/JuneYaooo/rea-video/commit/2cf82874641315d26e8b01df3bf805f0cb165c67) | JuneYaooo |
| 2026-11-17 | [Merge pull request #51 from NicolaSanmu/chatcut-continue-install](https://github.com/JuneYaooo/rea-video/commit/a274f48ac8911c415c46c21f7b78026e1638f0ef) | JuneYaooo |
| 2026-11-17 | [Hand off to each remake tool once the user picks one](https://github.com/JuneYaooo/rea-video/commit/cb37fc2a0fdd384b3c072d8984b4a0cd97b73d9c) | JuneYaooo |
| 2026-11-17 | [Merge pull request #50 from cpbackend/fix/windows-proxy-for-model-dow…](https://github.com/JuneYaooo/rea-video/commit/a4faff3f8183f9922383cab94f3dcaf2f12a3dbb) | JuneYaooo |
| 2026-11-17 | [Keep system proxy when no proxy env is set](https://github.com/JuneYaooo/rea-video/commit/23834983ad19bf4617e1df5f834b6b17fef73cdc) | JuneYaooo |
| 2026-11-17 | [remake-tools：改推荐收尾措辞；装好后给用户一段提示，在新对话里接着复刻](https://github.com/JuneYaooo/rea-video/commit/d9394c066eb2eb214eab7bb327a375f4429779b4) | NicolaSanmu |
| 2026-11-17 | [remake-tools：用户回「继续」时由 Agent 装好 ChatCut 接着复刻](https://github.com/JuneYaooo/rea-video/commit/f72ce05f8e760cff4974e5cd5c83b2d0b253bef2) | NicolaSanmu |
| 2026-11-17 | [fix: use the Windows registry proxy for model downloads when only NO_…](https://github.com/JuneYaooo/rea-video/commit/521c3bcc18dd5441f66ea08d2867a432b72748b9) | cpbackend |
| 2026-11-16 | [Write spec transition ids in VIDEO.md shots](https://github.com/JuneYaooo/rea-video/commit/07dd587119e884f7c50fbfae92e47840de86bea5) | JuneYaooo |

[See all commits ↗](https://github.com/JuneYaooo/rea-video/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuneYaooo/rea-video.git
```
