# matplotlib/mplfinance

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/matplotlib/mplfinance)

> Financial Markets Data Visualization using Matplotlib

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | Candlestick and financial charts with matplotlib |
| **Added** | 2026-11-11 |

💤 **Quiet** — no activity for 2y

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 4.5k |
| 🍴 **Forks** | 680 |
| 🐞 **Open issues + PRs** | [178](https://github.com/matplotlib/mplfinance/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ohlc-plot` `finance` `matplotlib` `ohlc` `ohlcv` `ohlc-chart` `candlestick-chart` `candlestick` `mplfinance` `trading-days` `ohlc-data` `intraday-data` `market-data` `candlestickchart` |
| 🕒 **Last activity** | 2024-08-08 (2y ago) |
| 📅 **Created** | 2019-12-05 |
| 📦 **Latest release** | [v0.12.10b0](https://github.com/matplotlib/mplfinance/releases/tag/v0.12.10b0) — 2023-08-02 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 85.3 MB |
| 🌐 **Website** | https://pypi.org/project/mplfinance/ |

## 📦 Recent releases

### [v0.12.10b0](https://github.com/matplotlib/mplfinance/releases/tag/v0.12.10b0)
<sub>2023-08-02 · 3y ago</sub>

> **What's Changed**
> * markersize validator extended by @ugorsahin in https://github.com/matplotlib/mplfinance/pull/580
> * add ticks_issue_573.ipynb by @DanielGoldfarb in https://github.com/matplotlib/mplfinance/pull/589
> * saving a few examples and experiments into the repository by @DanielGoldfarb in https://github.com/matplotlib/mplfinance/pull/599
> * Ploting Example Added With Data by @DrChandrakant in https://github.com/matplotlib/mplfinance/pull/612
>   - [**Many thanks to @DrChandrakant for adding many new plotting examples - click here.**](https://github.com/matplotlib/mplfinance/tree/master/examples/indicators)
> …

### [v0.12.9b7](https://github.com/matplotlib/mplfinance/releases/tag/v0.12.9b7) — Point and Figure rewrite
<sub>2022-12-08 · 3y ago</sub>

> - Rewrite Point and Figure code to fix problems noted in #568
> - also includes assorted changes to fix various deprecation warnings that otherwise appeared when mplfinance ran with newer versions of matplotlib and pandas.
> **What's Changed**
> * Fix a few deprecation warnings by @DanielGoldfarb in https://github.com/matplotlib/mplfinance/pull/571
> * Rewrite (fix/correct) Point and Figure algorithm by @DanielGoldfarb in https://github.com/matplotlib/mplfinance/pull/575
> **Full Changelog**: https://github.com/matplotlib/mplfinance/compare/v0.12.9b5...v0.12.9b7

### [v0.12.9b5](https://github.com/matplotlib/mplfinance/releases/tag/v0.12.9b5) — Hacktoberfest
<sub>2022-11-01 · 4y ago</sub>

> **What's Changed**
> * Change maximum panels to 32 in docs & examples, in regards to completion of #377 by @Animeshz in https://github.com/matplotlib/mplfinance/pull/555
> * mpf now accepts alpha parameter as list for [hvat]lines so it is possible to set a different alpha for each line.
>   - also import pyplot as plt to resolve unresolved reference error
>   - by @nijek in https://github.com/matplotlib/mplfinance/pull/558
> * Script additions for 'ema' plotting by @andrewrgarcia in https://github.com/matplotlib/mplfinance/pull/563
> …

### [v0.12.9b1](https://github.com/matplotlib/mplfinance/releases/tag/v0.12.9b1)
<sub>2022-05-25 · 4y ago</sub>

> **What's Changed (PR https://github.com/matplotlib/mplfinance/pull/530)**
> - Handle OHLC and Volume on same panel, by ...
>   - placing Volume on the panel's secondary axes
>   - using Axes.zorder to make sure OHLC is draw on top of volume
> - Also add the following kwargs to `mpf.plot()`:
>   - `volume_alpha` to set alpha of volume bars
> …

### [v0.12.9b0](https://github.com/matplotlib/mplfinance/releases/tag/v0.12.9b0)
<sub>2022-05-10 · 4y ago</sub>

> **What's Changed**
> * tweak multicursor, and add ginput example by @DanielGoldfarb in https://github.com/matplotlib/mplfinance/pull/501
> * Removing a TODO comment in `plotting.py` by @anbarief in https://github.com/matplotlib/mplfinance/pull/504
> * Removed `if (plottype not in _valid_types_all) ... ` and also `num_panels = config['num_panels']` by @anbarief in https://github.com/matplotlib/mplfinance/pull/507
> * allow a list to be passed as `mpl_base_style` kwarg  by @donbing in https://github.com/matplotlib/mplfinance/pull/516
> * Assorted cleanup and minor fixes. by @DanielGoldfarb in https://github.com/matplotlib/mplfinance/pull/526
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2024-04-02 | [Merge pull request #666 from DanielGoldfarb/master](https://github.com/matplotlib/mplfinance/commit/493811dac9a203de7ec148fb95504e7d3f400ba5) | DanielGoldfarb |
| 2024-04-02 | [re-generate price-movement_plots notebook](https://github.com/matplotlib/mplfinance/commit/c9270db4fd0fda7b2c718621df01a5e398f04068) | DanielGoldfarb |
| 2024-02-08 | [Update CONTRIBUTING.md](https://github.com/matplotlib/mplfinance/commit/9e40c7dff3d8ccf1b7c3a98dcca22433f4870c8c) | DanielGoldfarb |
| 2024-02-08 | [Update CONTRIBUTING.md](https://github.com/matplotlib/mplfinance/commit/ba35f04b1cfb757c444872a1d851d1269b8c712c) | DanielGoldfarb |
| 2023-08-02 | [Merge remote-tracking branch 'upstream/master'](https://github.com/matplotlib/mplfinance/commit/fb96216100bb89e9e371e5946971714833510627) | DanielGoldfarb |
| 2023-08-01 | [Merge pull request #605 from alexpvpmindustry/master](https://github.com/matplotlib/mplfinance/commit/50d7eb3ec29f0ca46e24d44ee573a2a9039ca9e3) | DanielGoldfarb |
| 2023-08-01 | [Merge branch 'master' into master](https://github.com/matplotlib/mplfinance/commit/cbda0af616e759a4ec8db2e0679ef7e31c57e603) | DanielGoldfarb |
| 2023-08-01 | [bump version; labels significant](https://github.com/matplotlib/mplfinance/commit/46c1dca6375ffc7274c427f53adcb45ebc9c9a73) | DanielGoldfarb |
| 2023-08-01 | [example of multiple labels in a single addplot](https://github.com/matplotlib/mplfinance/commit/5c22c44af38a6e066bfa80e179ded6aa8fb6ba82) | DanielGoldfarb |
| 2023-08-01 | [Merge branch 'master' into master](https://github.com/matplotlib/mplfinance/commit/16eaf85ee77afb11e57b9ab1efef503737a86aab) | DanielGoldfarb |

[See all commits ↗](https://github.com/matplotlib/mplfinance/commits)

## ⬇️ Get it

```bash
git clone https://github.com/matplotlib/mplfinance.git
```
