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
| ⭐ **Stars** | 169.3k |
| 🍴 **Forks** | 35.3k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/huggingface/transformers/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `nlp` `natural-language-processing` `pytorch` `pytorch-transformers` `transformer` `model-hub` `pretrained-models` `speech-recognition` `hacktoberfest` `python` `machine-learning` `deep-learning` `audio` `deepseek` `gemma` `glm` `llm` `qwen` `vlm` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2018-10-29 |
| 📦 **Latest release** | [v5.24.1](https://github.com/huggingface/transformers/releases/tag/v5.24.1) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 570.2 MB |
| 🌐 **Website** | https://huggingface.co/transformers |

## 📦 Recent releases

### [v5.24.1](https://github.com/huggingface/transformers/releases/tag/v5.24.1) — Patch release v5.24.1
<sub>2026-11-24 · today</sub>

> **Patch release v5.24.1**
> A patch to fix a bunch of stuff for vLLM, a few distributed issues, and some model fixes (llama4, dory); see the full list
> **vLLM related**
> - Fix backward compatibility of the cache rename for remote code (#51085) by @hmellor
> - Restore modeling_attn_mask_utils for remote code (one-off to unblock vLLM) (#51124) by @hmellor
> - Expose past_key_values in MBartDecoderLayer.forward signature for remote code (#51177) by @hmellor
> …

### [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — Release v5.24.0
<sub>2026-11-21 · 4d ago</sub>

> **Release v5.24.0**
> **New Model additions**
> **Inkling 2 Mini**
> <img width="80%" alt="image" src="https://github.com/user-attachments/assets/beefb5e0-39a9-4205-ab07-0ee707af95f2" />
> Inkling 2 Mini is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs. It is a smaller sibling of Inkling 2 Small, added in v5.23.0. It has 24 decoder layers instead of 48, and compensates with a looping mechanism in which layers 6 to 17 run three times. A learned message-passing mechanism mixes the residuals of the previous pass into the attention and mixture-of-experts inputs of each loop layer. The decoder has a hidden size of 2304 and routes each token to 8 of 128 experts. The image encoder, tokenizer and processor are the same as Inkling 2 Small's.
> A research checkpoint ([TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)) has the same architecture but supports a variable number of loop passes. Fewer passes are faster, and more passes improve quality. Both checkpoints contain NVFP4 and MXFP8 quantized layers, which are dequantized at load time.
> …

### [v5.23.0](https://github.com/huggingface/transformers/releases/tag/v5.23.0) — Release v5.23.0
<sub>2026-11-13 · 12d ago</sub>

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
<sub>2026-10-30 · 26d ago</sub>

> **Patch release v5.22.1**
> We just had to fix the documentation!
> ** [Fix] Remove WIP doc for Ml4 (https://github.com/huggingface/transformers/pull/50124) from @remi-or

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [[tests] Fix SpeechT5 coverage and TPU device selection (#51171)](https://github.com/huggingface/transformers/commit/1d8544b25c6780d85c6538636a6ca15aeabbcb7e) | tengomucho |
| 2026-11-25 | [[vLLM CI] Fix the KV cache memory check failures (page cache eviction…](https://github.com/huggingface/transformers/commit/85d7be82fa26e16a0c87c35dc3c48175149a9e8a) | ydshieh |
| 2026-11-25 | [Key the doc build concurrency group on the pull request number (#48707)](https://github.com/huggingface/transformers/commit/c9b611dc3eead5b0b50eced6b3d068040687fba8) | albertvillanova |
| 2026-11-25 | [The shared test resets the seed before eager and compiled runs, then …](https://github.com/huggingface/transformers/commit/0cc3b774e0d02595f1f0ee7cbe7a4444003e34d2) | sywangyi |
| 2026-11-25 | [Fix line breaks in the Megatron-BERT download commands (#51209)](https://github.com/huggingface/transformers/commit/8ce044a54857ae3957b052a1e092d8dea961370e) | JuanFKurucz |
| 2026-11-25 | [[docs] Fix the `images=` and `audio=` pipeline calls in the pipeline …](https://github.com/huggingface/transformers/commit/598021f5684f0e5f9e66433d9c700666f83b86a3) | AlexxRussell |
| 2026-11-25 | [Pre-fetch the `hf-internal-testing/test-videos` assets for CI (#51150)](https://github.com/huggingface/transformers/commit/292aead50f7659f5412e6966a9627d6d04ded6ce) | ydshieh |
| 2026-11-25 | [Update dev version (#51225)](https://github.com/huggingface/transformers/commit/3370f9427c2b948073ee17596970c0df19812af7) | albertvillanova |
| 2026-11-25 | [🚨 [PR2] [Modular Cleanup] *Norm canonicals and renaming (#50523)](https://github.com/huggingface/transformers/commit/3a96649547593bacad4b65d43442ccdf15d0ae0f) | itazap |
| 2026-11-25 | [Add `_get_num_multimodal_tokens` to more image/video processors (#50671)](https://github.com/huggingface/transformers/commit/9d5d0ee866d70b30fe187aab1bcf2aed398e9ecc) | hmellor |

[See all commits ↗](https://github.com/huggingface/transformers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/huggingface/transformers.git
```
