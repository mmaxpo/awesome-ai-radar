# hiyouga/LlamaFactory

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/hiyouga/LlamaFactory)

> Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Unified fine-tuning for 100+ LLMs & VLMs |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 76.2k |
| 🍴 **Forks** | 9.4k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/hiyouga/LlamaFactory/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `fine-tuning` `llama` `llm` `peft` `transformers` `rlhf` `qlora` `quantization` `qwen` `instruction-tuning` `gpt` `lora` `large-language-models` `agent` `ai` `moe` `llama3` `deepseek` `gemma` `nlp` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-05-28 |
| 📦 **Latest release** | [v0.9.5](https://github.com/hiyouga/LlamaFactory/releases/tag/v0.9.5) — 2026-05-30 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 14.0 MB |
| 🌐 **Website** | https://llamafactory.readthedocs.io |

## 📦 Recent releases

### [v0.9.5](https://github.com/hiyouga/LlamaFactory/releases/tag/v0.9.5) — v0.9.5: Qwen3.5/3.6, Gemma 4, Transformers v5
<sub>2026-05-30 · 5mo ago</sub>

> Added primary support for Qwen3.5/Qwen3.6/Gemma4 models and compatibility with Transformers v5.
> **What's Changed**
> * [misc] set dev version by @hiyouga in https://github.com/hiyouga/LlamaFactory/pull/9703
> * fix(fp8): add Transformer Engine backend support by @sbhavani in https://github.com/hiyouga/LlamaFactory/pull/9705
> * [misc] Compatible with an empty architectures field in config.json by @tangefly in https://github.com/hiyouga/LlamaFactory/pull/9709
> * [model] support Youtu-LLM-2B by @isLinXu in https://github.com/hiyouga/LlamaFactory/pull/9707
> …

### [v0.9.4](https://github.com/hiyouga/LlamaFactory/releases/tag/v0.9.4) — v0.9.4: Goodbye 2025
<sub>2025-12-31 · 10mo ago</sub>

> **Farewell to 2025. Thank you to all contributors and supporters. We will continue to deliver an easy and efficient LLM fine-tuning framework to the community in 2026. Stay tuned.**
> **Breaking**
> - Repository name updated: LLaMA-Factory → **LlamaFactory**
> - Python 3.9–3.10 have been deprecated; LlamaFactory now requires **Python 3.11–3.13**
> - Migrated from pip to **[uv](https://github.com/astral-sh/uv)**; use `uv pip install llamafactory`
> - The official LlamaFactory **blog** is now live: https://blog.llamafactory.net/en/
> …

### [v0.9.3](https://github.com/hiyouga/LlamaFactory/releases/tag/v0.9.3) — v0.9.3: Llama4, Gemma3, Qwen3, InternVL3, Qwen2.5-Omni
<sub>2025-06-16 · 1y ago</sub>

> **We will attend the **AWS Summit Shanghai 2025** on June 20th! See you in Shanghai 👋**
> - Event info: https://aws.amazon.com/cn/events/summits/shanghai/
> **New features**
> - 🔥 InternVL2.5/InternVL3 model by @Kuangdd01 in #7258
> - 🔥 Qwen2.5-Omni model by @Kuangdd01 in #7537
> - 🔥 Llama 4 and Gemma 3 multimodal model by @hiyouga in #7273 and #7611
> …

### [v0.9.2](https://github.com/hiyouga/LlamaFactory/releases/tag/v0.9.2) — v0.9.2: MiniCPM-o, SwanLab, APOLLO
<sub>2025-03-11 · 1y ago</sub>

> **We will attend the **vLLM Beijing Meetup** on Mar 16th! See you in Beijing 👋**
> - Event info: https://mp.weixin.qq.com/s/viPRDlhnzS3qO9-96fMeeA
> **New features**
> - 🔥 **[APOLLO optimizer](https://arxiv.org/abs/2412.05270)** by @zhuhanqing in #6617
> - 🔥 **[SwanLab](https://github.com/SwanHubX/SwanLab)** experiment tracker by @Zeyi-Lin in #6401
> - 🔥 **[Ray Trainer](https://docs.ray.io/en/latest/train/train.html)** by @erictang000 in #6542
> …

### [v0.9.1](https://github.com/hiyouga/LlamaFactory/releases/tag/v0.9.1) — v0.9.1: Many Vision Models, Qwen2.5 Coder, Gradient Fix
<sub>2024-11-24 · 1y ago</sub>

> **New features**
> - 🔥Support **Llama-3.2** and **Llama-3.2-Vision** by @marko1616 in #5547 and #5555
> - 🔥Support **LLaVA-NeXT**, **LLaVA-NeXT-Video** and **Video-LLaVA** by @BUAADreamer in #5574
> - 🔥Support **Pixtral** model by @Kuangdd01 in #5581
> - Support EXAONE3.0 by @shing100 in #5585
> - Support Index-series models by @Cuiyn in #5910
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [[docs] Add InCoder and IQuest models to the README tables (#11008)](https://github.com/hiyouga/LlamaFactory/commit/42acf37f59b0af71480647e47e228ca4228cb43b) | CSJianYang |
| 2026-11-19 | [[docs] Add GitCode badge to README (#11000)](https://github.com/hiyouga/LlamaFactory/commit/b4e4d3fcb2a5a13ce6b9431d395e3939f84b8ec1) | hiyouga |
| 2026-11-18 | [[model] Add GS1 decision model training with native two-stage recipe …](https://github.com/hiyouga/LlamaFactory/commit/57712ad19597cf75114c4c907e5189df5107f6bd) | jacklanda |
| 2026-11-17 | [[deps] upgrade transformers to 5.17.0 (#10869)](https://github.com/hiyouga/LlamaFactory/commit/885a4ca65cebf17a92e869af13c2ce42caca314a) | chinyixiang |
| 2026-11-17 | [[docs] add Qwen3.8 to the supported models table (#10992)](https://github.com/hiyouga/LlamaFactory/commit/5cbf775b4e22c791d9026a9682634378bbf1aabd) | Manfredss |
| 2026-11-16 | [[ci] Trigger CI workflows on requirements/*.txt changes (#10989)](https://github.com/hiyouga/LlamaFactory/commit/8869783bb72fffd44524042fbb716980bd89fd85) | hiyouga |
| 2026-11-16 | [[v1] Adapt to FSDPTurbo GDN API (#10985)](https://github.com/hiyouga/LlamaFactory/commit/fc4f229430a2bb30cfbf47dd0ce3f37429821804) | hazelduan |
| 2026-11-16 | [[v1] Fix FSDPTurbo expert ownership, CP gradients, and plan compatibi…](https://github.com/hiyouga/LlamaFactory/commit/faee7b999862e7abed1e0922ea818d5684762981) | hazelduan |
| 2026-11-13 | [[deps] upgrade vllm to 0.28.0 (#10857)](https://github.com/hiyouga/LlamaFactory/commit/5f1f6ad537e69216e0604671223cc1eeecbb7ba6) | chinyixiang |
| 2026-11-12 | [fix model type cast (#10971)](https://github.com/hiyouga/LlamaFactory/commit/6d1059c727450a4f58e56ad204d01a71abad7781) | codemayq |

[See all commits ↗](https://github.com/hiyouga/LlamaFactory/commits)

## ⬇️ Get it

```bash
git clone https://github.com/hiyouga/LlamaFactory.git
```
