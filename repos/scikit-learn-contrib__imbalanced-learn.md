# scikit-learn-contrib/imbalanced-learn

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/scikit-learn-contrib/imbalanced-learn)

>  A Python Package to Tackle the Curse of Imbalanced Datasets in Machine Learning

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | Tools for imbalanced datasets (over/under-sampling) |
| **Added** | 2026-11-11 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 7.1k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [117](https://github.com/scikit-learn-contrib/imbalanced-learn/issues) |
| 💻 **Languages** | Python 98% · Shell 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `machine-learning` `python` `statistics` `data-science` `data-analysis` |
| 🕒 **Last activity** | 2026-06-29 (4mo ago) |
| 📅 **Created** | 2014-08-16 |
| 📦 **Latest release** | [0.14.2](https://github.com/scikit-learn-contrib/imbalanced-learn/releases/tag/0.14.2) — 2026-06-07 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 22.5 MB |
| 🌐 **Website** | https://imbalanced-learn.org |

## 📦 Recent releases

### [0.14.2](https://github.com/scikit-learn-contrib/imbalanced-learn/releases/tag/0.14.2) — Imbalanced-learn 0.14.2
<sub>2026-06-07 · 5mo ago</sub>

> **Changelog**
> **Maintenance**
> - Compatibility with scikit-learn 1.9 [#1178](https://github.com/scikit-learn-contrib/imbalanced-learn/pull/1178) by [Guillaume Lemaitre](https://github.com/glemaitre).
> **Bug fixes**
> - Raise an informative error in [SMOTENC](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTENC.html#imblearn.over_sampling.SMOTENC) when the provided categorical_encoder does not keep one column per category (e.g. OneHotEncoder(drop=...) or an encoder merging infrequent categories), instead of failing with an opaque zero-size array NumPy error. [#1035](https://github.com/scikit-learn-contrib/imbalanced-learn/issues/1035) by [Imran Ahamed](https://github.com/immu4989).

### [0.14.1](https://github.com/scikit-learn-contrib/imbalanced-learn/releases/tag/0.14.1) — Imbalanced-learn 0.14.1
<sub>2025-12-21 · 10mo ago</sub>

> **Changelog**
> **Maintenance**
> - Compatibility with scikit-learn 1.8 [#1158](https://github.com/scikit-learn-contrib/imbalanced-learn/pull/1158) by [Guillaume Lemaitre](https://github.com/glemaitre) and [stratakis](https://github.com/stratakis).

### [0.14.0](https://github.com/scikit-learn-contrib/imbalanced-learn/releases/tag/0.14.0) — Imbalanced-learn 0.14.0
<sub>2025-08-14 · 1y ago</sub>

> **Changelog**
> **Enhancements**
> - Add [InstanceHardnessCV](https://imbalanced-learn.org/stable/references/generated/imblearn.model_selection.InstanceHardnessCV.html#imblearn.model_selection.InstanceHardnessCV) to split data and ensure that samples are distributed in folds based on their instance hardness. [#1125](https://github.com/scikit-learn-contrib/imbalanced-learn/pull/1125) by [Frits Hermans](https://github.com/fritshermans).
> **Compatibility**
> - Compatibility with scikit-learn 1.7 [#1137](https://github.com/scikit-learn-contrib/imbalanced-learn/pull/1137), [#1145](https://github.com/scikit-learn-contrib/imbalanced-learn/pull/1145), [#1146](https://github.com/scikit-learn-contrib/imbalanced-learn/pull/1146) by [Guillaume Lemaitre](https://github.com/glemaitre).

### [0.13.0](https://github.com/scikit-learn-contrib/imbalanced-learn/releases/tag/0.13.0) — Imbalanced-learn 0.13.0
<sub>2024-12-20 · 1y ago</sub>

> **Changelog**
> **Bug fixes**
> - Fix `get_metadata_routing` in `Pipeline` such that one can use a sampler with metadata routing. #1115 by @glemaitre.
> **Compatibility**
> - Compatibility with scikit-learn 1.6. #1109 by @glemaitre.
> **Deprecations**
> …

### [0.12.4](https://github.com/scikit-learn-contrib/imbalanced-learn/releases/tag/0.12.4) — Imbalanced-learn 0.12.4
<sub>2024-10-04 · 2y ago</sub>

> **Changelog**
> **Compatibility**
> - Compatibility with NumPy 2.0+ [#1097](https://github.com/scikit-learn-contrib/imbalanced-learn/pull/1097) by [Guillaume Lemaitre](https://github.com/glemaitre).

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-06-07 | [docs: Update the changelog](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/8504e95f0160f61d1b617ca66f779646d2ee609e) | glemaitre |
| 2026-06-07 | [chore: Compatibility with scikit-learn 1.9.0 (#1178)](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/38a7e3e06baf6ca69df295295977f535d5aa65ca) | glemaitre |
| 2026-06-07 | [FIX SMOTENC: clear error for column-dropping categorical encoders (#1…](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/7f97dba29bec5f450079668f6cafc29efae29e2d) | immu4989 |
| 2026-04-09 | [chore: Compatibility scikit-learn 1.9.0 (#1169)](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/de97df0855f367116958c78d811ee55b4c9f9aeb) | glemaitre |
| 2025-12-24 | [Bump the actions group with 3 updates (#1159)](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/6cdb18e9b8fc74fbdd9686c8b79c647e2e621c13) | dependabot[bot] |
| 2025-12-21 | [DOC add co-author to changelog](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/b899e657277f9a9de98d7ccc21d7ee71b2e00690) | glemaitre |
| 2025-12-21 | [DOC add entry in changelog for 0.14.1](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/af2a6e02a5dce7b4b8c033e2c5b913b93944554f) | glemaitre |
| 2025-12-21 | [MAINT compatibility with sklearn 1.8 (#1158)](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/95c9d1a85d6ad115db325bec4fb99371f50989b3) | glemaitre |
| 2025-12-21 | [Bump the actions group across 1 directory with 3 updates (#1148)](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/3163a678cbb449e14cd4b59d2ae7d3e950c7ab52) | dependabot[bot] |
| 2025-08-14 | [DOC fix hyperlink changelog](https://github.com/scikit-learn-contrib/imbalanced-learn/commit/5a5f6d76a5f5f1f6f37b391d0322339e23ef7088) | glemaitre |

[See all commits ↗](https://github.com/scikit-learn-contrib/imbalanced-learn/commits)

## ⬇️ Get it

```bash
git clone https://github.com/scikit-learn-contrib/imbalanced-learn.git
```
