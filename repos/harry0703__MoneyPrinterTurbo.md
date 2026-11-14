# harry0703/MoneyPrinterTurbo

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/harry0703/MoneyPrinterTurbo)

> 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖼 Image & video generation |
| **Project** | — |
| **Why it's worth a look** | Generates short-form videos with AI from a topic |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 143.5k |
| 🍴 **Forks** | 23.0k |
| 🐞 **Open issues + PRs** | [86](https://github.com/harry0703/MoneyPrinterTurbo/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `python` `tiktok` `ai-video-generator` `content-creation` `ffmpeg` `instagram-reels` `llm` `short-video` `subtitles` `text-to-speech` `video-automation` `video-workflow` `workflow-automation` `youtube-shorts` |
| 🕒 **Last activity** | 2026-11-13 (yesterday) |
| 📅 **Created** | 2024-03-11 |
| 📦 **Latest release** | [v1.3.10](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.10) — 2026-11-07 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 528.8 MB |

## 📦 Recent releases

### [v1.3.10](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.10)
<sub>2026-11-07 · 7d ago</sub>

> [English](#en-v1.3.10) | [中文](#cn-v1.3.10)
> <h2 id="en-v1.3.10">Highlights</h2>
> - Added **OpenAI Codex subscription access** with device-code sign-in and dynamic model selection, plus a separate **ChatGPT Native OAuth** provider. Native OAuth availability depends on account eligibility; existing Codex sign-in remains independent.
> - Added **Codex image generation** as a material source. Text and image generation can share the application's Codex login, and generated images support the existing static and slow zoom effects.
> - Added **Infistar and Jalapeno Cloud** for LLM and video generation, alongside **Runcrate, CloudGPU, and cheapaimodel** LLM providers.
> - Improved **long-running video generation feedback** with generation stages, elapsed time, and polling status. Task tracking survives page refreshes and temporary query failures, with protection against duplicate submissions.
> …

### [v1.3.9](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.9)
<sub>2026-10-21 · 24d ago</sub>

> [English](#en-v1.3.9) | [中文](#cn-v1.3.9)
> <h2 id="en-v1.3.9">Highlights</h2>
> - Added official **`mpt` pip packaging**. Start the WebUI with `mpt webui` or generate videos with `mpt cli`.
> - Added **static and slow zoom image effects** for local and AI-generated images. Slow zoom remains the default.
> - Added Kimi Code subscription access with browser authorization, alongside improvements to the sign-in dialog, status updates, and cancellation.
> - Added an optional **local SDXL image server** for the OpenAI-compatible image material workflow, with idle GPU offloading.
> …

### [v1.3.8](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.8)
<sub>2026-10-03 · 1mo ago</sub>

> [English](#en-v1.3.8) | [中文](#cn-v1.3.8)
> <h2 id="en-v1.3.8">Highlights</h2>
> - Added continuous progress reporting during stock footage downloads, clip processing, and final rendering, with task logs from background helper threads visible in the WebUI.
> - Added configurable stock material and clip rendering concurrency. Stock material concurrency applies to Pexels, Pixabay, and Coverr; both settings default to **1 (serial processing)**.
> - Added VoxCPM reference-audio voice cloning and optional delivery conditioning to carry over pacing and emotion, with local Whisper transcription for editable reference transcripts.
> - Added Fluxion AI, Cheaper Inference, Requesty, FutureInfra, Y-API, and iFlytek Spark (Astron MaaS) LLM providers.
> …

### [v1.3.7](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.7)
<sub>2026-09-13 · 2mo ago</sub>

> [English](#en-v1.3.7) | [中文](#cn-v1.3.7)
> <h2 id="en-v1.3.7">Highlights</h2>
> - Added word-by-word subtitles and a pop-up spring animation, with independent controls for display mode and animation in the WebUI.
> - Added preset background music selection with in-browser audio preview, so you can listen before generating a video.
> - Added native pauses to scripts with Azure TTS V1 (Edge TTS): use `[pause: 2s]` or `[停顿: 2s]` to insert silence while keeping narration and subtitles aligned.
> - Added Kokoro and VoxCPM TTS providers. Kokoro supports a self-hosted OpenAI-compatible service and automatically loads the server's voice list.
> …

### [v1.3.6](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.6)
<sub>2026-09-02 · 2mo ago</sub>

> [English](#en-v1.3.6) | [中文](#cn-v1.3.6)
> <h2 id="en-v1.3.6">Highlights</h2>
> - Added native Volcano Engine Ark Seedance video generation for generating source clips directly from script segments.
> - Added OFox multi-model text-to-video support, allowing Seedance, Wan, and other models to share one API key.
> - Added Metaso MiniMax H3 text-to-video support with `768P`/`2K` output, 4–15 second clips, and `9:16`, `16:9`, and `1:1` aspect ratios.
> - Added an OpenAI-compatible text-to-image material source for cloud relays and local gateways.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [docs: update packaging examples to current release](https://github.com/harry0703/MoneyPrinterTurbo/commit/ce289ffb61a118779c56d6b4a34181905dbed2b9) | dajiaohuang |
| 2026-11-13 | [docs: clarify Docker setup order (#1801)](https://github.com/harry0703/MoneyPrinterTurbo/commit/f7f4aeff368bd2d5c97ee3c397e1b67aaaa62f79) | dajiaohuang |
| 2026-11-13 | [docs: update MangoDisk promotion in readmes](https://github.com/harry0703/MoneyPrinterTurbo/commit/f6eb73ef6b674283d2d4ccd5cb10ad67cf6575a1) | harry0703 |
| 2026-11-13 | [perf(material): download Pixabay's 1080p file instead of the 4K one w…](https://github.com/harry0703/MoneyPrinterTurbo/commit/16986d0118cbdaa284ff7ce03a87734ffd837ee9) | tanishqbaweja |
| 2026-11-13 | [fix(subtitle): keep Mr. Smith, Dr. Walker and Mt. Everest in one subt…](https://github.com/harry0703/MoneyPrinterTurbo/commit/6a9a0cbe1659ea261afa34a6e85b597042d0d720) | tanishqbaweja |
| 2026-11-13 | [fix(api): give /videos requests without voice_name the default voice …](https://github.com/harry0703/MoneyPrinterTurbo/commit/c2868a6774f5d824bff910e34342883f6eb5a973) | tanishqbaweja |
| 2026-11-13 | [fix(webui): read the voice sample in the voice's language, so English…](https://github.com/harry0703/MoneyPrinterTurbo/commit/a06a43dd6ce9de6263620d3795506f387c5ca2d2) | tanishqbaweja |
| 2026-11-12 | [fix(material): at clip speeds above 1x, download enough stock videos …](https://github.com/harry0703/MoneyPrinterTurbo/commit/82216ccbad2ff20d9c51a0cd8472e6ee6cda3f45) | tanishqbaweja |
| 2026-11-12 | [chore: update project resources](https://github.com/harry0703/MoneyPrinterTurbo/commit/782cf3ae8cf829d95023d8bcb2ff5545d11ec858) | harry0703 |
| 2026-11-12 | [fix(webui): show 1.00 MB instead of 1024 KB just below a unit boundary](https://github.com/harry0703/MoneyPrinterTurbo/commit/dd096584f1642f3d52b8b2aa7c39df84bb2066bf) | kevin9327 |

[See all commits ↗](https://github.com/harry0703/MoneyPrinterTurbo/commits)

## ⬇️ Get it

```bash
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
```
