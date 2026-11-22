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
| ⭐ **Stars** | 169.4k |
| 🍴 **Forks** | 35.3k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/huggingface/transformers/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `nlp` `natural-language-processing` `pytorch` `pytorch-transformers` `transformer` `model-hub` `pretrained-models` `speech-recognition` `hacktoberfest` `python` `machine-learning` `deep-learning` `audio` `deepseek` `gemma` `glm` `llm` `qwen` `vlm` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2018-10-29 |
| 📦 **Latest release** | [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 563.9 MB |
| 🌐 **Website** | https://huggingface.co/transformers |

## 📦 Recent releases

### [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — Release v5.24.0
<sub>2026-11-21 · yesterday</sub>

> **Release v5.24.0**
> **New Model additions**
> **Inkling 2 Mini**
> <img width="80%" alt="image" src="https://github.com/user-attachments/assets/beefb5e0-39a9-4205-ab07-0ee707af95f2" />
> Inkling 2 Mini is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs. It is a smaller sibling of Inkling 2 Small, added in v5.23.0. It has 24 decoder layers instead of 48, and compensates with a looping mechanism in which layers 6 to 17 run three times. A learned message-passing mechanism mixes the residuals of the previous pass into the attention and mixture-of-experts inputs of each loop layer. The decoder has a hidden size of 2304 and routes each token to 8 of 128 experts. The image encoder, tokenizer and processor are the same as Inkling 2 Small's.
> A research checkpoint ([TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)) has the same architecture but supports a variable number of loop passes. Fewer passes are faster, and more passes improve quality. Both checkpoints contain NVFP4 and MXFP8 quantized layers, which are dequantized at load time.
> …

### [v5.23.0](https://github.com/huggingface/transformers/releases/tag/v5.23.0) — Release v5.23.0
<sub>2026-11-13 · 8d ago</sub>

> **Release v5.23.0**
> **New Model additions**
> **Inkling2**
> <img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/9115e142-1be3-4f79-a51d-ea0e5c25b152" />
> Inkling 2 Small is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs, and it is intended for use in English and other languages and across multiple coding languages. Its language backbone has 48 mixture-of-experts decoder layers, each routing tokens to 8 of 384 experts, for 594B total and 17B active parameters. It keeps the Inkling decoder (learned relative attention, short causal convolutions, mixture-of-experts layers) and adds block attention residuals, gated attention with a learned sink, and dynamic key/value convolutions. Images are encoded by a Perception Encoder-based vision transformer and projected into the language model embeddings, one embedding per 40x40 pixel patch.
> **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2) | [Blog Post](https://thinkingmachines.ai/news/inkling-2-small/)
> …

### [v5.22.2](https://github.com/huggingface/transformers/releases/tag/v5.22.2) — Patch release v5.22.2
<sub>2026-11-06 · 15d ago</sub>

> **Patch release v5.22.2**
> Some in between patch for security and distributed fixes. See the included commits :hugs:
> - [Distributed] Set device_id only for NCCL (#50281) by @michaelbenayoun  and @3outeille
> - Harden our Jinja sandboxing (#50431) by @Rocketknight1
> **Full Changelog**: https://github.com/huggingface/transformers/compare/v5.22.1...v5.22.2

### [v5.22.1](https://github.com/huggingface/transformers/releases/tag/v5.22.1) — Patch release v5.22.1
<sub>2026-10-30 · 23d ago</sub>

> **Patch release v5.22.1**
> We just had to fix the documentation!
> ** [Fix] Remove WIP doc for Ml4 (https://github.com/huggingface/transformers/pull/50124) from @remi-or

### [v5.22.0](https://github.com/huggingface/transformers/releases/tag/v5.22.0) — v5.22.0: Mistral Large 4 (Le Chonk)
<sub>2026-10-29 · 23d ago</sub>

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
| 2026-11-21 | [Restore CUDA expectation for DeepseekV2 test_batch_fa2 (#51068)](https://github.com/huggingface/transformers/commit/2f1bc5e321b9a736200a590d6e7743ccdeb60772) | ydshieh |
| 2026-11-21 | [Add Inkling2 Mini (#51050)](https://github.com/huggingface/transformers/commit/046bdb8cc2cee29d233964bb77fe6fd37cfe4aa3) | guarin |
| 2026-11-20 | [Fix Intel CPU Dockerfile: pin kernels via transformers[kernels] and d…](https://github.com/huggingface/transformers/commit/4d9ef623e3b0a1fb6c12891a907e0e50d41f0af8) | jiqing-feng |
| 2026-11-20 | [Skip flaky Kosmos2 `test_generate_from_multimodal_encoder_outputs` (#…](https://github.com/huggingface/transformers/commit/8d7668dd7d5f945e34aa0f5d9f163bc5f955e163) | ydshieh |
| 2026-11-20 | [Save dequantized models without the quantizer's weight conversions (#…](https://github.com/huggingface/transformers/commit/106b40c7c2e6705680897271d06d774675c8cdb8) | qgallouedec |
| 2026-11-20 | [[CB] Scale the per-token memory estimate by the TP size (#48566)](https://github.com/huggingface/transformers/commit/d0da3b84c6b5851e7506fcde99d33e7fa793e1f7) | qgallouedec |
| 2026-11-20 | [Fix OmniASR CTC blank token ID (#51040)](https://github.com/huggingface/transformers/commit/1cfb1e8e4cb6945a84078c60a92a26bc35f80bd1) | taking-lying-flat |
| 2026-11-20 | [Fix flaky DeepseekV32 / Whisper / HiggsAudioV2 CUDA graph capture fai…](https://github.com/huggingface/transformers/commit/dd623c8cf785bec63a9b1a396b846b5d121f2ace) | ydshieh |
| 2026-11-20 | [[docs] Fix the custom ResNet example in the customizing models guide …](https://github.com/huggingface/transformers/commit/c0ae6dd7e68a8e8d7ad3a7fd8c8ac7fc9171d91e) | AlexxRussell |
| 2026-11-20 | [Keep the cache under activation checkpointing when gradients are off …](https://github.com/huggingface/transformers/commit/f2c9ee2401bce932d38d48eafde581a65af7fcc9) | qgallouedec |

[See all commits ↗](https://github.com/huggingface/transformers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/huggingface/transformers.git
```
