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
| ⭐ **Stars** | 10.9k |
| 🍴 **Forks** | 1.6k |
| 🐞 **Open issues + PRs** | [5](https://github.com/JuneYaooo/rea-video/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering` `remotion` `reverse-engineering` `short-video` `shot-detection` `subtitles` `video-analysis` `video-breakdown` `video-editing` `video-generation` `vlm` `videomd` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-10-29 |
| 📦 **Latest release** | [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 79.3 MB |
| 🌐 **Website** | https://www.reavideo.ai/ |

## 📦 Recent releases

### [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0)
<sub>2026-11-11 · 7d ago</sub>

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
| 2026-11-19 | [Keep frame select expressions shallow](https://github.com/JuneYaooo/rea-video/commit/cf12cc73353635dc859cd7fb8a0c471c03ab150d) | JuneYaooo |
| 2026-11-19 | [Update 3D-Speaker CAM++ checksum after sherpa-onnx re-export](https://github.com/JuneYaooo/rea-video/commit/cd2ca431bdf236d6123f320170bd0d762c2e384d) | BitmanAlan |
| 2026-11-19 | [Update ChatCut entry](https://github.com/JuneYaooo/rea-video/commit/ac470773188574833b839be17abee6162201ddf9) | JuneYaooo |
| 2026-11-19 | [Label sponsored tool in skill replies](https://github.com/JuneYaooo/rea-video/commit/7b411d5f18f5ba051465270ac0d7aad49e486d72) | JuneYaooo |
| 2026-11-18 | [Add token notice to READMEs](https://github.com/JuneYaooo/rea-video/commit/538eb3a757db94826cb90c4297279e50c5dd0f83) | JuneYaooo |
| 2026-11-18 | [Move flow diagrams under docs/flow](https://github.com/JuneYaooo/rea-video/commit/e2acf601d212c63f9662cca58177588c2ba26006) | JuneYaooo |
| 2026-11-18 | [Size model threads to the machine](https://github.com/JuneYaooo/rea-video/commit/2651186b98f2e7f8cab5f1fe8e680d410913b7a3) | JuneYaooo |
| 2026-11-18 | [Decode once for samples, sheets and stills; fewer model threads](https://github.com/JuneYaooo/rea-video/commit/2478ce5778b540bbe2b3595feb84b11552fe6936) | JuneYaooo |
| 2026-11-18 | [Time generated clips to the original's moves](https://github.com/JuneYaooo/rea-video/commit/16e683ebba2f708d98134fe198c256b7ef97df8e) | JuneYaooo |
| 2026-11-18 | [Point remakes at frame numbers](https://github.com/JuneYaooo/rea-video/commit/5c072a60dafbaaf8a4cfd254704f3cb8ecdf2699) | JuneYaooo |

[See all commits ↗](https://github.com/JuneYaooo/rea-video/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuneYaooo/rea-video.git
```
