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
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2018-10-29 |
| 📦 **Latest release** | [v5.24.1](https://github.com/huggingface/transformers/releases/tag/v5.24.1) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 568.5 MB |
| 🌐 **Website** | https://huggingface.co/transformers |

## 📦 Recent releases

### [v5.24.1](https://github.com/huggingface/transformers/releases/tag/v5.24.1) — Patch release v5.24.1
<sub>2026-11-24 · 2d ago</sub>

> **Patch release v5.24.1**
> A patch to fix a bunch of stuff for vLLM, a few distributed issues, and some model fixes (llama4, dory); see the full list
> **vLLM related**
> - Fix backward compatibility of the cache rename for remote code (#51085) by @hmellor
> - Restore modeling_attn_mask_utils for remote code (one-off to unblock vLLM) (#51124) by @hmellor
> - Expose past_key_values in MBartDecoderLayer.forward signature for remote code (#51177) by @hmellor
> …

### [v5.24.0](https://github.com/huggingface/transformers/releases/tag/v5.24.0) — Release v5.24.0
<sub>2026-11-21 · 6d ago</sub>

> **Release v5.24.0**
> **New Model additions**
> **Inkling 2 Mini**
> <img width="80%" alt="image" src="https://github.com/user-attachments/assets/beefb5e0-39a9-4205-ab07-0ee707af95f2" />
> Inkling 2 Mini is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs. It is a smaller sibling of Inkling 2 Small, added in v5.23.0. It has 24 decoder layers instead of 48, and compensates with a looping mechanism in which layers 6 to 17 run three times. A learned message-passing mechanism mixes the residuals of the previous pass into the attention and mixture-of-experts inputs of each loop layer. The decoder has a hidden size of 2304 and routes each token to 8 of 128 experts. The image encoder, tokenizer and processor are the same as Inkling 2 Small's.
> A research checkpoint ([TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)) has the same architecture but supports a variable number of loop passes. Fewer passes are faster, and more passes improve quality. Both checkpoints contain NVFP4 and MXFP8 quantized layers, which are dequantized at load time.
> …

### [v5.23.0](https://github.com/huggingface/transformers/releases/tag/v5.23.0) — Release v5.23.0
<sub>2026-11-13 · 14d ago</sub>

> **Release v5.23.0**
> **New Model additions**
> **Inkling2**
> <img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/9115e142-1be3-4f79-a51d-ea0e5c25b152" />
> Inkling 2 Small is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs, and it is intended for use in English and other languages and across multiple coding languages. Its language backbone has 48 mixture-of-experts decoder layers, each routing tokens to 8 of 384 experts, for 594B total and 17B active parameters. It keeps the Inkling decoder (learned relative attention, short causal convolutions, mixture-of-experts layers) and adds block attention residuals, gated attention with a learned sink, and dynamic key/value convolutions. Images are encoded by a Perception Encoder-based vision transformer and projected into the language model embeddings, one embedding per 40x40 pixel patch.
> **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2) | [Blog Post](https://thinkingmachines.ai/news/inkling-2-small/)
> …

### [v5.22.2](https://github.com/huggingface/transformers/releases/tag/v5.22.2) — Patch release v5.22.2
<sub>2026-11-06 · 20d ago</sub>

> **Patch release v5.22.2**
> Some in between patch for security and distributed fixes. See the included commits :hugs:
> - [Distributed] Set device_id only for NCCL (#50281) by @michaelbenayoun  and @3outeille
> - Harden our Jinja sandboxing (#50431) by @Rocketknight1
> **Full Changelog**: https://github.com/huggingface/transformers/compare/v5.22.1...v5.22.2

### [v5.22.1](https://github.com/huggingface/transformers/releases/tag/v5.22.1) — Patch release v5.22.1
<sub>2026-10-30 · 28d ago</sub>

> **Patch release v5.22.1**
> We just had to fix the documentation!
> ** [Fix] Remove WIP doc for Ml4 (https://github.com/huggingface/transformers/pull/50124) from @remi-or

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [[serve] Refactor server and engine architecture (#50927)](https://github.com/huggingface/transformers/commit/f6b7cbef762d0b5997a2dcab0a6ea33f28f68753) | SunMarc |
| 2026-11-27 | [add or update xpu expectations for 4 models tests (#51363)](https://github.com/huggingface/transformers/commit/1c9278519d5e6fcc1d13044bed63e4ab3448be28) | kaixuanliu |
| 2026-11-27 | [Fix Qwen3-VL video expansion keeping the chat template's outer vision…](https://github.com/huggingface/transformers/commit/a779a0d3598a868cc3f67e4f4794bfc39b109767) | Abhijeet-Saich |
| 2026-11-27 | [Fix CamemBERTv2 WordPiece tokenizer auto-dispatch (#51188)](https://github.com/huggingface/transformers/commit/d5a6bfe462882c221ac35a06b920bd14530233a0) | WissamAntoun |
| 2026-11-27 | [fix some numeric issue for CB on XPU test cases (#51168)](https://github.com/huggingface/transformers/commit/04925af08a729b479998d6ad57886a748d51d878) | kaixuanliu |
| 2026-11-27 | [fix failed test cases for apertus1p5 (#51285)](https://github.com/huggingface/transformers/commit/ce66e565061a9cd8441f34c2cd922f56dff1f22d) | kaixuanliu |
| 2026-11-27 | [Accept remote-code sub-processors that ignore `return_unused_kwargs` …](https://github.com/huggingface/transformers/commit/9acc6335d881fd46c5c4827c47d2d72e4c4b51c5) | ydshieh |
| 2026-11-27 | [Add `_merge_and_standardize_kwargs` to image and video processors (#5…](https://github.com/huggingface/transformers/commit/5c9ca18ef807755d892671727ba9b55d2a757a9d) | hmellor |
| 2026-11-27 | [Fix Gemma 4 dropping `audio_outputs`, which made `audio_hidden_states…](https://github.com/huggingface/transformers/commit/44ee1da4158b5cdb5f836d2ddc489d191bf7d49c) | XiaoyuanWang111 |
| 2026-11-27 | [Post the model integration contracts gate on the PR (#51311)](https://github.com/huggingface/transformers/commit/adcc6878bd98d31ffe85f44b75ee1529a8f56259) | tarekziade |

[See all commits ↗](https://github.com/huggingface/transformers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/huggingface/transformers.git
```
