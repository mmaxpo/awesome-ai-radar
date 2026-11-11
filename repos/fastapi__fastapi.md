# fastapi/fastapi

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/fastapi/fastapi)

> FastAPI framework, high performance, easy to learn, fast to code, ready for production

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🐍 Python & backend tooling |
| **Project** | — |
| **Why it's worth a look** | Fast, typed Python web framework for APIs |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 104.6k |
| 🍴 **Forks** | 10.2k |
| 🐞 **Open issues + PRs** | [54](https://github.com/fastapi/fastapi/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `python` `json` `swagger-ui` `redoc` `starlette` `openapi` `api` `openapi3` `framework` `async` `asyncio` `uvicorn` `python3` `python-types` `pydantic` `json-schema` `fastapi` `swagger` `rest` `web` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2018-12-08 |
| 📦 **Latest release** | [0.162.4](https://github.com/fastapi/fastapi/releases/tag/0.162.4) — 2026-11-10 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 59.2 MB |
| 🌐 **Website** | https://fastapi.tiangolo.com/ |

## 📦 Recent releases

### [0.162.4](https://github.com/fastapi/fastapi/releases/tag/0.162.4)
<sub>2026-11-10 · today</sub>

> > FastAPI includes an official skill that helps coding agents use new features and recommended patterns for your installed version. Install it with `uvx library-skills` in your project. See [Develop with AI](https://fastapi.tiangolo.com/ai-development/).
> **Fixes**
> * 🐛 Require AnyIO 4.1.0 or newer at runtime. PR [#16730](https://github.com/fastapi/fastapi/pull/16730) by [@tiangolo](https://github.com/tiangolo).

### [0.162.3](https://github.com/fastapi/fastapi/releases/tag/0.162.3)
<sub>2026-11-10 · yesterday</sub>

> > FastAPI includes an official skill that helps coding agents use new features and recommended patterns for your installed version. Install it with `uvx library-skills` in your project. See [Develop with AI](https://fastapi.tiangolo.com/ai-development/).
> **Upgrades**
> * ⬆️ Add support for Python 3.15. PR [#16727](https://github.com/fastapi/fastapi/pull/16727) by [@tiangolo](https://github.com/tiangolo).
> * ⬆️ Update locked Pydantic to 2.14.3. PR [#16728](https://github.com/fastapi/fastapi/pull/16728) by [@tiangolo](https://github.com/tiangolo).
> * ⬆️ Upgrade `markdown-include-variants` to 0.0.10. PR [#16705](https://github.com/fastapi/fastapi/pull/16705) by [@tiangolo](https://github.com/tiangolo).
> **Docs**
> …

### [0.162.2](https://github.com/fastapi/fastapi/releases/tag/0.162.2)
<sub>2026-11-07 · 4d ago</sub>

> > FastAPI includes an official skill that helps coding agents use new features and recommended patterns for your installed version. Install it with `uvx library-skills` in your project. See [Develop with AI](https://fastapi.tiangolo.com/ai-development/).
> **Docs**
> * 📝 Add FastAPI Cloud guidance to the FastAPI skill. PR [#16697](https://github.com/fastapi/fastapi/pull/16697) by [@tiangolo](https://github.com/tiangolo).
> * 📝 Add guidance for developing FastAPI apps with AI. PR [#16695](https://github.com/fastapi/fastapi/pull/16695) by [@tiangolo](https://github.com/tiangolo).
> **Internal**
> * 🔧 Add an agent skills note to GitHub releases. PR [#16696](https://github.com/fastapi/fastapi/pull/16696) by [@tiangolo](https://github.com/tiangolo).

### [0.162.1](https://github.com/fastapi/fastapi/releases/tag/0.162.1)
<sub>2026-11-07 · 4d ago</sub>

> **Docs**
> * 📝 Add parameter model guidance to the FastAPI skill. PR [#16693](https://github.com/fastapi/fastapi/pull/16693) by [@tiangolo](https://github.com/tiangolo).
> **Translations**
> * 🌐 Update translations for zh-hant (update-outdated). PR [#16654](https://github.com/fastapi/fastapi/pull/16654) by [@pr-submit[bot]](https://github.com/apps/pr-submit).
> * 🌐 Update translations for uk (update-outdated). PR [#16655](https://github.com/fastapi/fastapi/pull/16655) by [@pr-submit[bot]](https://github.com/apps/pr-submit).
> * 🌐 Update translations for de (update-outdated). PR [#16652](https://github.com/fastapi/fastapi/pull/16652) by [@pr-submit[bot]](https://github.com/apps/pr-submit).
> …

### [0.162.0](https://github.com/fastapi/fastapi/releases/tag/0.162.0)
<sub>2026-10-23 · 18d ago</sub>

> Omitted `bool` and `bool | None` form fields now use their declared defaults or produce missing-field errors, consistent with other fields and Pydantic behavior. FastAPI no longer infers `False` for omitted booleans. This applies to individual form parameters, form models, and unions of form models.
> Omitted boolean model fields are excluded from `model_dump(exclude_unset=True)`, and their defaults no longer count as submitted fields during union selection. Default factories and `validate_default` follow the usual rules.
> For HTML checkboxes, declare a boolean with a default of `False`. See [Boolean Form Fields](https://fastapi.tiangolo.com/tutorial/request-forms/#boolean-form-fields).
> **Breaking Changes**
> * 🐛 Restore default handling for omitted boolean form fields. PR [#16605](https://github.com/fastapi/fastapi/pull/16605) by [@tiangolo](https://github.com/tiangolo).

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-10 | [📝 Update release notes](https://github.com/fastapi/fastapi/commit/e1144f6954eb8dd8c306f8dd2f5f0a14bbeb2cfd) | latest-changes[bot] |
| 2026-11-10 | [➖ Drop `pydantic-ai` dependency, use `pydantic-ai-slim[openai]` inste…](https://github.com/fastapi/fastapi/commit/1c78a216472a56a9346b78a795ce9024d8f2e0e4) | YuriiMotov |
| 2026-11-10 | [🔖 Release version 0.162.4 (#16731)](https://github.com/fastapi/fastapi/commit/e10178c18d8dc2dcc21a70e14152253abc4a4e2f) | pr-submit[bot] |
| 2026-11-10 | [📝 Update release notes](https://github.com/fastapi/fastapi/commit/af628068e772b05bb56bf050cc99f2817b9020f9) | latest-changes[bot] |
| 2026-11-10 | [🐛 Require AnyIO 4.1.0 or newer at runtime (#16730)](https://github.com/fastapi/fastapi/commit/0902e8b5599031cca795e43964922a07d7c6c9b2) | tiangolo |
| 2026-11-10 | [🔖 Release version 0.162.3 (#16729)](https://github.com/fastapi/fastapi/commit/84d5f8ea759355e26d5a36f9c5c5652df924328e) | tiangolo |
| 2026-11-10 | [📝 Update release notes](https://github.com/fastapi/fastapi/commit/6b131a6bba9c7ee54c6324a896d0e9b8ed31c01c) | latest-changes[bot] |
| 2026-11-10 | [⬆️ Add support for Python 3.15 (#16727)](https://github.com/fastapi/fastapi/commit/ed6f566fd9f6243b9ece9270b0183440e8c1965c) | tiangolo |
| 2026-11-10 | [📝 Update release notes](https://github.com/fastapi/fastapi/commit/5e24b3219a11cdf5c41179406eb358f6d1a19c1a) | latest-changes[bot] |
| 2026-11-10 | [⬆️ Update locked Pydantic to 2.14.3 (#16728)](https://github.com/fastapi/fastapi/commit/60acfa1b73dab918aeec21ca49815c42dbf53bc7) | tiangolo |

[See all commits ↗](https://github.com/fastapi/fastapi/commits)

## ⬇️ Get it

```bash
git clone https://github.com/fastapi/fastapi.git
```
