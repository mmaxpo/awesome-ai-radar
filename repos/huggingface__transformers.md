# huggingface/transformers

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/huggingface/transformers)

> 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | The model-definition library behind most open models |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 169.2k |
| 🍴 **Forks** | 35.3k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/huggingface/transformers/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `nlp` `natural-language-processing` `pytorch` `pytorch-transformers` `transformer` `model-hub` `pretrained-models` `speech-recognition` `hacktoberfest` `python` `machine-learning` `deep-learning` `audio` `deepseek` `gemma` `glm` `llm` `qwen` `vlm` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2018-10-29 |
| 📦 **Latest release** | [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 564.2 MB |
| 🌐 **Website** | https://huggingface.co/transformers |

## 📦 Recent releases

### [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — Release v5.24.0
<sub>2026-11-21 · 3d ago</sub>

> **Release v5.24.0**
> **New Model additions**
> **Inkling 2 Mini**
> <img width="80%" alt="image" src="https://github.com/user-attachments/assets/beefb5e0-39a9-4205-ab07-0ee707af95f2" />
> Inkling 2 Mini is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs. It is a smaller sibling of Inkling 2 Small, added in v5.23.0. It has 24 decoder layers instead of 48, and compensates with a looping mechanism in which layers 6 to 17 run three times. A learned message-passing mechanism mixes the residuals of the previous pass into the attention and mixture-of-experts inputs of each loop layer. The decoder has a hidden size of 2304 and routes each token to 8 of 128 experts. The image encoder, tokenizer and processor are the same as Inkling 2 Small's.
> A research checkpoint ([TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)) has the same architecture but supports a variable number of loop passes. Fewer passes are faster, and more passes improve quality. Both checkpoints contain NVFP4 and MXFP8 quantized layers, which are dequantized at load time.
> …

### [v5.23.0](https://github.com/huggingface/transformers/releases/tag/v5.23.0) — Release v5.23.0
<sub>2026-11-13 · 11d ago</sub>

> **Release v5.23.0**
> **New Model additions**
> **Inkling2**
> <img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/9115e142-1be3-4f79-a51d-ea0e5c25b152" />
> Inkling 2 Small is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs, and it is intended for use in English and other languages and across multiple coding languages. Its language backbone has 48 mixture-of-experts decoder layers, each routing tokens to 8 of 384 experts, for 594B total and 17B active parameters. It keeps the Inkling decoder (learned relative attention, short causal convolutions, mixture-of-experts layers) and adds block attention residuals, gated attention with a learned sink, and dynamic key/value convolutions. Images are encoded by a Perception Encoder-based vision transformer and projected into the language model embeddings, one embedding per 40x40 pixel patch.
> **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2) | [Blog Post](https://thinkingmachines.ai/news/inkling-2-small/)
> …

### [v5.22.2](https://github.com/huggingface/transformers/releases/tag/v5.22.2) — Patch release v5.22.2
<sub>2026-11-06 · 18d ago</sub>

> **Patch release v5.22.2**
> Some in between patch for security and distributed fixes. See the included commits :hugs:
> - [Distributed] Set device_id only for NCCL (#50281) by @michaelbenayoun  and @3outeille
> - Harden our Jinja sandboxing (#50431) by @Rocketknight1
> **Full Changelog**: https://github.com/huggingface/transformers/compare/v5.22.1...v5.22.2

### [v5.22.1](https://github.com/huggingface/transformers/releases/tag/v5.22.1) — Patch release v5.22.1
<sub>2026-10-30 · 25d ago</sub>

> **Patch release v5.22.1**
> We just had to fix the documentation!
> ** [Fix] Remove WIP doc for Ml4 (https://github.com/huggingface/transformers/pull/50124) from @remi-or

### [v5.22.0](https://github.com/huggingface/transformers/releases/tag/v5.22.0) — v5.22.0: Mistral Large 4 (Le Chonk)
<sub>2026-10-29 · 26d ago</sub>

> **New Models**
> **Mistral Large 4 (Le Chonk)**
> <img width="1329" height="780" alt="image" src="https://github.com/user-attachments/assets/1cff9ca7-19e3-4622-8db6-fb1cfa842579" />
> Mistral Large 4 is Mistral's largest and most capable model to date: a 1 trillion-parameter natively multimodal Mixture-of-Experts model with 49 billion active parameters per token (52 billion including embeddings and output layers), trained from scratch on 3,800 NVIDIA Grace Blackwell GPUs in Mistral's own datacenters in Europe.
> Mistral Large 4 unifies instruction following, reasoning, coding, and agentic workflows in a single set of weights. While a generalist model, it shows especially good performance on workloads such as cybersecurity, finance, and law, and it surpasses frontier closed models on visual grounding. It is natively fluent in 160+ languages, including every official language of the European Union.
> **Key Features**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [feat: add rocm entries to hub kernels mapping (#50980)](https://github.com/huggingface/transformers/commit/9ffd1f50a1fe13183d435ff60cb4b92777cc417e) | drbh |
| 2026-11-24 | [Pad text and audio features on their own sides when batching multimod…](https://github.com/huggingface/transformers/commit/840bc92650ad5b8d8a83f2c64c5b3782e05ce4f7) | Enricoftw |
| 2026-11-24 | [[vLLM CI] Add more language / multimodal pooling models vs transforme…](https://github.com/huggingface/transformers/commit/b308e3d194858a276c0481fabfd72e4380534e8c) | ydshieh |
| 2026-11-24 | [Fix strided checkpoint reads on PyTorch 2.9 (#51042)](https://github.com/huggingface/transformers/commit/af80f69cb0cf321dffc1cdb8379f3a58a883295b) | satsuki2486441738 |
| 2026-11-24 | [Fix Llama4 forward crash on missing image_outputs (#51144)](https://github.com/huggingface/transformers/commit/ab19734bb45071c74b6d9dd7a5906dd68b366ae7) | kylesayrs |
| 2026-11-24 | [Fix TIPSv2 bfloat16 forward: text pooling returned float32 (#50175)](https://github.com/huggingface/transformers/commit/b0f4265020c209826afb7dca2c95c8077433b90f) | tarekziade |
| 2026-11-24 | [Expose `past_key_values` in `MBartDecoderLayer.forward` signature for…](https://github.com/huggingface/transformers/commit/8f548bbfaed26adb72d88b897d9c3e60cc4a075b) | hmellor |
| 2026-11-24 | [Move YaRN `mscale` helpers into `modeling_rope_utils` (#51175)](https://github.com/huggingface/transformers/commit/ae61745a79914d83b8e600cea57341af82f19eb2) | ArthurZucker |
| 2026-11-24 | [[PR1] [Modular Clean-Up] Remove No-op Overrides (#50317)](https://github.com/huggingface/transformers/commit/fe4a46771d2d38ffb047a2cab797d3848303cd4c) | itazap |
| 2026-11-24 | [Add kolibri 1.1 (#51176)](https://github.com/huggingface/transformers/commit/e75335fb29c266b36b22bf32f250bfca1f2165f3) | Cyrilvallez |

[See all commits ↗](https://github.com/huggingface/transformers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/huggingface/transformers.git
```
