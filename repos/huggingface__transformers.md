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
| 🐞 **Open issues + PRs** | [1.2k](https://github.com/huggingface/transformers/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `nlp` `natural-language-processing` `pytorch` `pytorch-transformers` `transformer` `model-hub` `pretrained-models` `speech-recognition` `hacktoberfest` `python` `machine-learning` `deep-learning` `audio` `deepseek` `gemma` `glm` `llm` `qwen` `vlm` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2018-10-29 |
| 📦 **Latest release** | [v5.24.1](https://github.com/huggingface/transformers/releases/tag/v5.24.1) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 566.8 MB |
| 🌐 **Website** | https://huggingface.co/transformers |

## 📦 Recent releases

### [v5.24.1](https://github.com/huggingface/transformers/releases/tag/v5.24.1) — Patch release v5.24.1
<sub>2026-11-24 · yesterday</sub>

> **Patch release v5.24.1**
> A patch to fix a bunch of stuff for vLLM, a few distributed issues, and some model fixes (llama4, dory); see the full list
> **vLLM related**
> - Fix backward compatibility of the cache rename for remote code (#51085) by @hmellor
> - Restore modeling_attn_mask_utils for remote code (one-off to unblock vLLM) (#51124) by @hmellor
> - Expose past_key_values in MBartDecoderLayer.forward signature for remote code (#51177) by @hmellor
> …

### [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — Release v5.24.0
<sub>2026-11-21 · 5d ago</sub>

> **Release v5.24.0**
> **New Model additions**
> **Inkling 2 Mini**
> <img width="80%" alt="image" src="https://github.com/user-attachments/assets/beefb5e0-39a9-4205-ab07-0ee707af95f2" />
> Inkling 2 Mini is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs. It is a smaller sibling of Inkling 2 Small, added in v5.23.0. It has 24 decoder layers instead of 48, and compensates with a looping mechanism in which layers 6 to 17 run three times. A learned message-passing mechanism mixes the residuals of the previous pass into the attention and mixture-of-experts inputs of each loop layer. The decoder has a hidden size of 2304 and routes each token to 8 of 128 experts. The image encoder, tokenizer and processor are the same as Inkling 2 Small's.
> A research checkpoint ([TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)) has the same architecture but supports a variable number of loop passes. Fewer passes are faster, and more passes improve quality. Both checkpoints contain NVFP4 and MXFP8 quantized layers, which are dequantized at load time.
> …

### [v5.23.0](https://github.com/huggingface/transformers/releases/tag/v5.23.0) — Release v5.23.0
<sub>2026-11-13 · 13d ago</sub>

> **Release v5.23.0**
> **New Model additions**
> **Inkling2**
> <img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/9115e142-1be3-4f79-a51d-ea0e5c25b152" />
> Inkling 2 Small is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs, and it is intended for use in English and other languages and across multiple coding languages. Its language backbone has 48 mixture-of-experts decoder layers, each routing tokens to 8 of 384 experts, for 594B total and 17B active parameters. It keeps the Inkling decoder (learned relative attention, short causal convolutions, mixture-of-experts layers) and adds block attention residuals, gated attention with a learned sink, and dynamic key/value convolutions. Images are encoded by a Perception Encoder-based vision transformer and projected into the language model embeddings, one embedding per 40x40 pixel patch.
> **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2) | [Blog Post](https://thinkingmachines.ai/news/inkling-2-small/)
> …

### [v5.22.2](https://github.com/huggingface/transformers/releases/tag/v5.22.2) — Patch release v5.22.2
<sub>2026-11-06 · 19d ago</sub>

> **Patch release v5.22.2**
> Some in between patch for security and distributed fixes. See the included commits :hugs:
> - [Distributed] Set device_id only for NCCL (#50281) by @michaelbenayoun  and @3outeille
> - Harden our Jinja sandboxing (#50431) by @Rocketknight1
> **Full Changelog**: https://github.com/huggingface/transformers/compare/v5.22.1...v5.22.2

### [v5.22.1](https://github.com/huggingface/transformers/releases/tag/v5.22.1) — Patch release v5.22.1
<sub>2026-10-30 · 27d ago</sub>

> **Patch release v5.22.1**
> We just had to fix the documentation!
> ** [Fix] Remove WIP doc for Ml4 (https://github.com/huggingface/transformers/pull/50124) from @remi-or

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Fix reloading a `SynthIDTextWatermarkingConfig` from `generation_conf…](https://github.com/huggingface/transformers/commit/ebf21a5acd6c49544ca035cef96e4c05a429211a) | SeanPeppers |
| 2026-11-26 | [Make root AGENTS.md a real file (#51324)](https://github.com/huggingface/transformers/commit/f879b5db43c9b4442b91d42e67285fa15261e806) | Rocketknight1 |
| 2026-11-26 | [Fix hybrid_sliding mapping in LAYER_PATTERN_TO_MASK_FUNCTION_MAPPING …](https://github.com/huggingface/transformers/commit/f7ba81261e1a9e29692f59e3bb0b39cfa0745e9a) | Nikhilodeon1 |
| 2026-11-26 | [fix multi GPU tests for pi05 (#51226)](https://github.com/huggingface/transformers/commit/664369a4fb1625537f1b0ca8581d2242a4d28f59) | molbap |
| 2026-11-26 | [[`Kernels`] Bump min version (#51258)](https://github.com/huggingface/transformers/commit/d4b94d3f58c736a673ece14a6b2df8d8f93f136d) | vasqu |
| 2026-11-26 | [Fix assisted decoding crash when the model returns no attentions (#51…](https://github.com/huggingface/transformers/commit/083a0adc621ae9f55c5b4ff09d445ba58679c487) | ranmori |
| 2026-11-26 | [Use the correct forward method in the chunk batching example (#51296)](https://github.com/huggingface/transformers/commit/a6c5e6f8e4a211cf829506b8afb3c90c73efb627) | ViktorBystrov72 |
| 2026-11-26 | [Fix Unigram tokenizers built from a bare `spiece.model` splitting tex…](https://github.com/huggingface/transformers/commit/9e5e84cc8985a4c2b1b5adc4facee92dbc25ec2f) | XiaoyuanWang111 |
| 2026-11-26 | [Count only embedding tokens in the remaining `_get_num_multimodal_tok…](https://github.com/huggingface/transformers/commit/708d41ca9421f1432ee81aef46a16542e58c3d21) | hmellor |
| 2026-11-26 | [Let an explicit `attn_implementation` override a serialized `_attn_im…](https://github.com/huggingface/transformers/commit/378f20a1fda66b9349731ee24844e1defd77e9dc) | lucamotz |

[See all commits ↗](https://github.com/huggingface/transformers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/huggingface/transformers.git
```
