# meta/prophet

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/meta/prophet)

> Tool for producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | Time-series forecasting (formerly the fbprophet package) |
| **Added** | 2026-11-11 |

↪️ **Moved** — was `facebook/prophet` · 🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 20.5k |
| 🍴 **Forks** | 4.6k |
| 🐞 **Open issues + PRs** | [468](https://github.com/meta/prophet/issues) |
| 💻 **Languages** | Python 66% · R 32% · Stan 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `forecasting` `r` `python` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2016-11-16 |
| 📦 **Latest release** | [v1.5.0](https://github.com/meta/prophet/releases/tag/v1.5.0) — 2026-10-05 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 67.2 MB |
| 🌐 **Website** | https://facebook.github.io/prophet |

## 📦 Recent releases

### [v1.5.0](https://github.com/meta/prophet/releases/tag/v1.5.0) — 1.5.0
<sub>2026-10-05 · 1mo ago</sub>

> **What's Changed**
> * fix: close cross-validation executor pools by @mameikagou in https://github.com/facebook/prophet/pull/2745
> * fix cross-validation with shared seasonality conditions by @Shubham-Padkonde in https://github.com/facebook/prophet/pull/2748
> * fix: avoid deprecated class-scoped fixture instance method by @RblxDev-ALS in https://github.com/facebook/prophet/pull/2746
> * fix: do not modify the metrics list passed to performance_metrics by @kwy404 in https://github.com/facebook/prophet/pull/2751
> * refactor: separate performance_metrics into metrics module to resolve circular import by @fabiooliveir in https://github.com/facebook/prophet/pull/2747
> …

### [v1.4.0-patched](https://github.com/meta/prophet/releases/tag/v1.4.0-patched) — v1.4.0 patched
<sub>2026-08-15 · 2mo ago</sub>

> Patched wheel build.

### [v1.4.0](https://github.com/meta/prophet/releases/tag/v1.4.0)
<sub>2026-08-01 · 3mo ago</sub>

> **What's Changed**
> * Drop support for Python <3.10 by @jorenham in https://github.com/facebook/prophet/pull/2716
> * full static typing support by @jorenham in https://github.com/facebook/prophet/pull/2720
> * Add optional regressor predictor models and propagate their uncertainty by @tcuongd with @Copilot in https://github.com/facebook/prophet/pull/2703
> **Full Changelog**: https://github.com/facebook/prophet/compare/v1.3.0...v1.4.0

### [v1.3.0](https://github.com/meta/prophet/releases/tag/v1.3.0)
<sub>2026-01-27 · 9mo ago</sub>

> **What's Changed**
> * minor: Support pandas 3.0 and numpy 2.4 by @tcuongd in https://github.com/facebook/prophet/pull/2715
> **Full Changelog**: https://github.com/facebook/prophet/compare/v1.2.2...v1.3.0

### [v1.2.2-patched](https://github.com/meta/prophet/releases/tag/v1.2.2-patched) — v1.2.2
<sub>2026-01-25 · 9mo ago</sub>

> **What's Changed**
> * R Package: Update C++ Version to Comply with CRAN Policy by @mitokic in https://github.com/facebook/prophet/pull/2707
> * chore: Add .tar.gz upload for R package to CI by @tcuongd in https://github.com/facebook/prophet/pull/2708
> * fix: max version on pandas by @tcuongd in https://github.com/facebook/prophet/pull/2711
> * fix: constrain numpy by @tcuongd in https://github.com/facebook/prophet/pull/2712
> * minor: Re-generated holidays.csv for R package.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-10-22 | [fix: reject NaN holiday windows instead of silently dropping the rang…](https://github.com/meta/prophet/commit/5cf15c0f6e5d5259d9dd8d511fb4e15a45884cdc) | NishchayMahor |
| 2026-10-21 | [refactor: compute component plot data in private helpers (#2756)](https://github.com/meta/prophet/commit/ad059eba8fc9f38e921b3e5e907bc83b27b44472) | Thanatos9404 |
| 2026-10-21 | [Fix Prophet init failure on Windows in UTF-8 mode (#2758) (#2759)](https://github.com/meta/prophet/commit/02bae83fce07702339c607dca62183f9143e92e2) | hippi345 |
| 2026-10-21 | [fix: do not modify the holidays dataframe passed to Prophet (#2757)](https://github.com/meta/prophet/commit/45dff6980efa81986cb476437390da6f3e692cec) | Thanatos9404 |
| 2026-10-13 | [fix: keep the scaling option when copying a model for cross-validatio…](https://github.com/meta/prophet/commit/0cf18fc38e002cbe7f2cf77a81120e6c26d5b73d) | kwy404 |
| 2026-10-05 | [Adding references to Helter Skelter project (#2750)](https://github.com/meta/prophet/commit/f931ceb204932e92371982eb3f1745ba3b6fe73a) | diegoruotolo |
| 2026-10-05 | [minor: 1.5.0 release (#2752)](https://github.com/meta/prophet/commit/f57c4e13a29d18f927f2516f04990a3540711694) | tcuongd |
| 2026-10-05 | [fix: keep MAP parameter shapes when the history is constant (#2749)](https://github.com/meta/prophet/commit/f98ff2167556248b50804fbe52adce74387618ca) | kwy404 |
| 2026-10-05 | [refactor: separate performance_metrics into metrics module to resolve…](https://github.com/meta/prophet/commit/a6b6ce40807a54e68ea7dc3ee820eee88ed668e6) | fabiooliveir |
| 2026-10-03 | [fix: do not modify the metrics list passed to performance_metrics (#2…](https://github.com/meta/prophet/commit/0e2adaf37f59f594e51fab673cd1c103632eb0a7) | kwy404 |

[See all commits ↗](https://github.com/meta/prophet/commits)

## ⬇️ Get it

```bash
git clone https://github.com/meta/prophet.git
```
