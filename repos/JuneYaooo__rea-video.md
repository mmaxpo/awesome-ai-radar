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
| ⭐ **Stars** | 11.6k |
| 🍴 **Forks** | 1.7k |
| 🐞 **Open issues + PRs** | [6](https://github.com/JuneYaooo/rea-video/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering` `remotion` `reverse-engineering` `short-video` `shot-detection` `subtitles` `video-analysis` `video-breakdown` `video-editing` `video-generation` `vlm` `videomd` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-10-29 |
| 📦 **Latest release** | [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 72.9 MB |
| 🌐 **Website** | https://www.reavideo.ai/ |

## 📦 Recent releases

### [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0)
<sub>2026-11-11 · 9d ago</sub>

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
| 2026-11-21 | [Make reports easier to read](https://github.com/JuneYaooo/rea-video/commit/86486c6e104b917fb4b6a2d6501134686c05b219) | JuneYaooo |
| 2026-11-21 | [Refresh report layout](https://github.com/JuneYaooo/rea-video/commit/612b3ef523c868d4c7cd5741ce29ba159f7582cb) | JuneYaooo |
| 2026-11-21 | [Keep pitch frames steady and clarify Windows setup](https://github.com/JuneYaooo/rea-video/commit/2901858590cd919aeb48a9d0ab8b34463ea1b51a) | JuneYaooo |
| 2026-11-21 | [Fix pitch analysis past the end of audio](https://github.com/JuneYaooo/rea-video/commit/3d9a740b7b5d449b3cba7af16a0125ee38276163) | zitihc |
| 2026-11-21 | [fmt_time: carry rounded-up seconds into the minutes](https://github.com/JuneYaooo/rea-video/commit/8fae330148b6ea4a8ee76db88e425462fb1a2616) | nurlanmnn |
| 2026-11-21 | [docs(setup): say which Python the Windows install uses](https://github.com/JuneYaooo/rea-video/commit/27cc34c0d7cad1285807f32fd0cc6c177ce6a8b1) | xdAsaah |
| 2026-11-21 | [Handle image paths and Windows setup](https://github.com/JuneYaooo/rea-video/commit/4d98dd8dd1838edfa58037cf4df9d1cccc245da7) | JuneYaooo |
| 2026-11-21 | [Report a missing ffmpeg when probe runs, not a missing file](https://github.com/JuneYaooo/rea-video/commit/73541597454c29281103e03029ba7bdb439875b7) | xdAsaah |
| 2026-11-21 | [Tell Windows users how to install ffmpeg and Python, and how to link …](https://github.com/JuneYaooo/rea-video/commit/1526ca3b3c9c166f16a6425f34667981d7041725) | xdAsaah |
| 2026-11-21 | [Find browsers in the 64-bit and per-user Windows install locations](https://github.com/JuneYaooo/rea-video/commit/6eb1e1779e57426a3ccf3b2e4cd8d992ce8180b5) | xdAsaah |

[See all commits ↗](https://github.com/JuneYaooo/rea-video/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuneYaooo/rea-video.git
```
