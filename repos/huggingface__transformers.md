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
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2018-10-29 |
| 📦 **Latest release** | [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 564.3 MB |
| 🌐 **Website** | https://huggingface.co/transformers |

## 📦 Recent releases

### [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — Release v5.24.0
<sub>2026-11-21 · 2d ago</sub>

> **Release v5.24.0**
> **New Model additions**
> **Inkling 2 Mini**
> <img width="80%" alt="image" src="https://github.com/user-attachments/assets/beefb5e0-39a9-4205-ab07-0ee707af95f2" />
> Inkling 2 Mini is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs. It is a smaller sibling of Inkling 2 Small, added in v5.23.0. It has 24 decoder layers instead of 48, and compensates with a looping mechanism in which layers 6 to 17 run three times. A learned message-passing mechanism mixes the residuals of the previous pass into the attention and mixture-of-experts inputs of each loop layer. The decoder has a hidden size of 2304 and routes each token to 8 of 128 experts. The image encoder, tokenizer and processor are the same as Inkling 2 Small's.
> A research checkpoint ([TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)) has the same architecture but supports a variable number of loop passes. Fewer passes are faster, and more passes improve quality. Both checkpoints contain NVFP4 and MXFP8 quantized layers, which are dequantized at load time.
> …

### [v5.23.0](https://github.com/huggingface/transformers/releases/tag/v5.23.0) — Release v5.23.0
<sub>2026-11-13 · 10d ago</sub>

> **Release v5.23.0**
> **New Model additions**
> **Inkling2**
> <img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/9115e142-1be3-4f79-a51d-ea0e5c25b152" />
> Inkling 2 Small is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs, and it is intended for use in English and other languages and across multiple coding languages. Its language backbone has 48 mixture-of-experts decoder layers, each routing tokens to 8 of 384 experts, for 594B total and 17B active parameters. It keeps the Inkling decoder (learned relative attention, short causal convolutions, mixture-of-experts layers) and adds block attention residuals, gated attention with a learned sink, and dynamic key/value convolutions. Images are encoded by a Perception Encoder-based vision transformer and projected into the language model embeddings, one embedding per 40x40 pixel patch.
> **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2) | [Blog Post](https://thinkingmachines.ai/news/inkling-2-small/)
> …

### [v5.22.2](https://github.com/huggingface/transformers/releases/tag/v5.22.2) — Patch release v5.22.2
<sub>2026-11-06 · 17d ago</sub>

> **Patch release v5.22.2**
> Some in between patch for security and distributed fixes. See the included commits :hugs:
> - [Distributed] Set device_id only for NCCL (#50281) by @michaelbenayoun  and @3outeille
> - Harden our Jinja sandboxing (#50431) by @Rocketknight1
> **Full Changelog**: https://github.com/huggingface/transformers/compare/v5.22.1...v5.22.2

### [v5.22.1](https://github.com/huggingface/transformers/releases/tag/v5.22.1) — Patch release v5.22.1
<sub>2026-10-30 · 24d ago</sub>

> **Patch release v5.22.1**
> We just had to fix the documentation!
> ** [Fix] Remove WIP doc for Ml4 (https://github.com/huggingface/transformers/pull/50124) from @remi-or

### [v5.22.0](https://github.com/huggingface/transformers/releases/tag/v5.22.0) — v5.22.0: Mistral Large 4 (Le Chonk)
<sub>2026-10-29 · 25d ago</sub>

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
| 2026-11-23 | [[OmniASR] Support a `padding_mask` kept on the CPU in the audio encod…](https://github.com/huggingface/transformers/commit/0d3998c0ae41a9cf9b853d93f2b22806c215f19e) | El-euchidali |
| 2026-11-23 | [[vLLM CI] Test vLLM features built on transformers tokenizers / proce…](https://github.com/huggingface/transformers/commit/bae9427f872e2a96e6ef612a99ff135a133f42e1) | ydshieh |
| 2026-11-23 | [Fix test_flash_attn_2_can_dispatch_composite_models for models that d…](https://github.com/huggingface/transformers/commit/5b6c887c3e75dce213631488353a73b5d67d373e) | Abdennacer-Badaoui |
| 2026-11-23 | [[Chat Parsing] Preserve explicit string arguments in typed json and p…](https://github.com/huggingface/transformers/commit/fcc89620113994456848b7f2a7a47230b187f569) | xgbtxy |
| 2026-11-23 | [[docs] Replace deprecated torch_dtype with dtype in doc examples (#51…](https://github.com/huggingface/transformers/commit/91c512bc655351d5a38fd355a923ae167518f6fb) | abhitorch81 |
| 2026-11-23 | [Fix batch-dependent text output in image-text-to-text and any-to-any …](https://github.com/huggingface/transformers/commit/a8041496678faf305f8d384f34fc3997c7edd04f) | Enricoftw |
| 2026-11-23 | [Add overridable Trainer.get_resumed_dataloader (#50248)](https://github.com/huggingface/transformers/commit/f6c0d55d3a61c2a1880a03a4042b9be5c8e7befa) | bruno-hays |
| 2026-11-23 | [:red-circle: fix(nemotron_h): honor configured Mamba time-step limits…](https://github.com/huggingface/transformers/commit/2f6f6912aff24e5d31b20a129a19b6c1819bca60) | yuhezhang-ai |
| 2026-11-23 | [Restore `modeling_attn_mask_utils` for remote code (one-off to unbloc…](https://github.com/huggingface/transformers/commit/4b401cf208f3a39a5d9cc2a93723ce8dc7049d6c) | hmellor |
| 2026-11-23 | [Refactor output tracing for `depth_anything` (#49947)](https://github.com/huggingface/transformers/commit/8516c7394b6b19e8e3abbf6dabb965eeb5439c02) | omkar-334 |

[See all commits ↗](https://github.com/huggingface/transformers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/huggingface/transformers.git
```
