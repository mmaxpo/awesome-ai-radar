# microsoft/playwright-python

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/microsoft/playwright-python)

> Python version of the Playwright testing and automation library.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | Browser automation for Python (scraping, testing, agents) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 15.1k |
| 🍴 **Forks** | 1.3k |
| 🐞 **Open issues + PRs** | [0](https://github.com/microsoft/playwright-python/issues) |
| 💻 **Languages** | Python 92% · HTML 4% · JavaScript 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `playwright` `chromium` `firefox` `webkit` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2020-07-01 |
| 📦 **Latest release** | [v1.65.2](https://github.com/microsoft/playwright-python/releases/tag/v1.65.2) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 16.0 MB |
| 🌐 **Website** | https://playwright.dev/python/ |

## 📦 Recent releases

### [v1.65.2](https://github.com/microsoft/playwright-python/releases/tag/v1.65.2)
<sub>2026-11-14 · today</sub>

> **Highlights**
> https://github.com/microsoft/playwright/pull/44098 - browser(chromium): roll to r1255, v159.0.8154.6
> **Browser Versions**
> - Chromium 159.0.8154.6

### [v1.65.1](https://github.com/microsoft/playwright-python/releases/tag/v1.65.1)
<sub>2026-11-11 · 2d ago</sub>

> **Highlights**
> https://github.com/microsoft/playwright-python/pull/3337 - chore: roll Node.js to 26.13.1
> https://github.com/microsoft/playwright-python/pull/3331 - devops(docker): install libatomic1 for the Node.js binary of the driver
> https://github.com/microsoft/playwright-python/pull/3336 - fix(docker): upgrade base image packages during the build
> The bundled Node.js 26.13.1 is a [security release](https://github.com/nodejs/node/releases/tag/v26.13.1) with fixes in `tls`, `http`, `https` and `http2`. The driver uses Node.js for its own network connections, for example `connect_over_cdp` to a `wss://` endpoint.
> The Docker images now include `libatomic1`, which the Node.js binary of the driver needs, and the latest security updates of the Ubuntu packages.
> …

### [v1.65.0](https://github.com/microsoft/playwright-python/releases/tag/v1.65.0)
<sub>2026-11-09 · 4d ago</sub>

> **🧾 Locator code in Python**
> A locator from [locator.normalize()](https://playwright.dev/python/docs/api/class-locator#locator-normalize) now converts to a string as Python code. Use it with [page.get_by_ref()](https://playwright.dev/python/docs/api/class-page#page-get-by-ref) to turn an element that an agent picks from a [page.aria_snapshot()](https://playwright.dev/python/docs/api/class-page#page-aria-snapshot) in the `"ai"` mode into code for your test:
> ```python
> normalized = page.get_by_ref("e2").normalize()
> print(str(normalized))
> **get_by_role("button", name="Submit")**
> …

### [v1.64.1](https://github.com/microsoft/playwright-python/releases/tag/v1.64.1)
<sub>2026-10-22 · 23d ago</sub>

> **Highlights**
> https://github.com/microsoft/playwright-python/pull/3283 - chore: roll Node.js to 24.22.1
> The bundled Node.js 24.22.1 is a security release that distrusts the compromised eMudhra intermediate CAs. The driver uses Node's CA store for its own TLS connections, for example `connect_over_cdp` to a `wss://` endpoint.
> **Browser Versions**
> - Chromium 156.0.8078.4
> - Mozilla Firefox 157.0
> …

### [v1.64.0](https://github.com/microsoft/playwright-python/releases/tag/v1.64.0)
<sub>2026-10-13 · 1mo ago</sub>

> **🧰 WebMCP**
> New [page.webmcp](https://playwright.dev/python/docs/api/class-page#page-webmcp) and [frame.webmcp](https://playwright.dev/python/docs/api/class-frame#frame-webmcp) give access to the tools that a page registers through
> the experimental [WebMCP](https://webmachinelearning.github.io/webmcp/) browser API, so you can test them like
> any other part of your app:
> ```python
> browser = chromium.launch(args=["--enable-features=WebMCP"])
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [devops(release): prepare a patch release with a workflow (#3347)](https://github.com/microsoft/playwright-python/commit/86a5f5a81010b1dbd155263e99782442b61d0cb2) | pavelfeldman |
| 2026-11-13 | [fix(handlers): support immutable and built-in callbacks (#3344)](https://github.com/microsoft/playwright-python/commit/dbf7807fe7c26201a8ac7feb795e793325892693) | microsoft-playwright-automation[bot] |
| 2026-11-13 | [chore: roll Playwright to 1.66.0-next (8534271f04) (#3342)](https://github.com/microsoft/playwright-python/commit/88eafe1b2b004c2f489d04d8d9cfdcd66f6c2cf2) | microsoft-playwright-automation[bot] |
| 2026-11-13 | [devops(roll): roll a release branch with the roll workflow (#3339)](https://github.com/microsoft/playwright-python/commit/f68f05ce17d548e6cc21e3cdc592c5b6cb489d20) | pavelfeldman |
| 2026-11-12 | [build(deps): bump types-pyyaml from 6.0.12.20260906 to 6.0.12.2026110…](https://github.com/microsoft/playwright-python/commit/b36f716b50808af0ef031fda06546f97b407ddcc) | dependabot[bot] |
| 2026-11-12 | [chore: roll Playwright to 1.66.0-next (3b438229c6) (#3334)](https://github.com/microsoft/playwright-python/commit/273ab97d953e0f24f9e52d574f481a35aca313e9) | microsoft-playwright-automation[bot] |
| 2026-11-11 | [chore: roll Node.js to 26.13.1 (#3337)](https://github.com/microsoft/playwright-python/commit/6f724516c648edda6bf55ba9a9fa2e8143faec52) | pavelfeldman |
| 2026-11-11 | [fix(docker): upgrade base image packages during the build (#3336)](https://github.com/microsoft/playwright-python/commit/3b1f408208b970a3c108ee47f57c9b57f9b2bbe5) | yury-s |
| 2026-11-10 | [devops(docker): publish stable images from the tip of a release branc…](https://github.com/microsoft/playwright-python/commit/89436fb88df74b0f1c5ef4b9df3a113d409bf3cd) | yury-s |
| 2026-11-10 | [chore(bots): name the agent workflows agent-*, and start tasks by han…](https://github.com/microsoft/playwright-python/commit/63cdffb905cbd09c1b73ae2cde51f8dd353bccd8) | pavelfeldman |

[See all commits ↗](https://github.com/microsoft/playwright-python/commits)

## ⬇️ Get it

```bash
git clone https://github.com/microsoft/playwright-python.git
```
