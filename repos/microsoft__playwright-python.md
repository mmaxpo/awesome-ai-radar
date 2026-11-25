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
| 🐞 **Open issues + PRs** | [2](https://github.com/microsoft/playwright-python/issues) |
| 💻 **Languages** | Python 92% · HTML 4% · JavaScript 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `playwright` `chromium` `firefox` `webkit` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2020-07-01 |
| 📦 **Latest release** | [v1.65.2](https://github.com/microsoft/playwright-python/releases/tag/v1.65.2) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 16.6 MB |
| 🌐 **Website** | https://playwright.dev/python/ |

## 📦 Recent releases

### [v1.65.2](https://github.com/microsoft/playwright-python/releases/tag/v1.65.2)
<sub>2026-11-14 · 11d ago</sub>

> **Highlights**
> https://github.com/microsoft/playwright/pull/44098 - browser(chromium): roll to r1255, v159.0.8154.6
> **Browser Versions**
> - Chromium 159.0.8154.6

### [v1.65.1](https://github.com/microsoft/playwright-python/releases/tag/v1.65.1)
<sub>2026-11-11 · 13d ago</sub>

> **Highlights**
> https://github.com/microsoft/playwright-python/pull/3337 - chore: roll Node.js to 26.13.1
> https://github.com/microsoft/playwright-python/pull/3331 - devops(docker): install libatomic1 for the Node.js binary of the driver
> https://github.com/microsoft/playwright-python/pull/3336 - fix(docker): upgrade base image packages during the build
> The bundled Node.js 26.13.1 is a [security release](https://github.com/nodejs/node/releases/tag/v26.13.1) with fixes in `tls`, `http`, `https` and `http2`. The driver uses Node.js for its own network connections, for example `connect_over_cdp` to a `wss://` endpoint.
> The Docker images now include `libatomic1`, which the Node.js binary of the driver needs, and the latest security updates of the Ubuntu packages.
> …

### [v1.65.0](https://github.com/microsoft/playwright-python/releases/tag/v1.65.0)
<sub>2026-11-09 · 15d ago</sub>

> **🧾 Locator code in Python**
> A locator from [locator.normalize()](https://playwright.dev/python/docs/api/class-locator#locator-normalize) now converts to a string as Python code. Use it with [page.get_by_ref()](https://playwright.dev/python/docs/api/class-page#page-get-by-ref) to turn an element that an agent picks from a [page.aria_snapshot()](https://playwright.dev/python/docs/api/class-page#page-aria-snapshot) in the `"ai"` mode into code for your test:
> ```python
> normalized = page.get_by_ref("e2").normalize()
> print(str(normalized))
> **get_by_role("button", name="Submit")**
> …

### [v1.64.1](https://github.com/microsoft/playwright-python/releases/tag/v1.64.1)
<sub>2026-10-22 · 1mo ago</sub>

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
| 2026-11-25 | [chore: roll Playwright to 1.66.0-next (b0e0b7b555) (#3373)](https://github.com/microsoft/playwright-python/commit/f31e7025d36bebc4b55c2e94f97f26ac92e13067) | microsoft-playwright-automation[bot] |
| 2026-11-24 | [fix(events): preserve pytest outcomes without closing the connection …](https://github.com/microsoft/playwright-python/commit/8b452510884008b70c099a32089d4501c90c721f) | microsoft-playwright-automation[bot] |
| 2026-11-23 | [chore: roll Playwright to 1.66.0-next (049226728d) (#3365)](https://github.com/microsoft/playwright-python/commit/c830b5f852afd4a0c036b69443544875c7249fa7) | microsoft-playwright-automation[bot] |
| 2026-11-20 | [chore: roll Playwright to 1.66.0-next (a018f24a4f) (#3359)](https://github.com/microsoft/playwright-python/commit/de03c865f5738c2291a6a58c8b5c20346d8e70f2) | microsoft-playwright-automation[bot] |
| 2026-11-20 | [docs: remove the mention of generateApiJson.js (#3358)](https://github.com/microsoft/playwright-python/commit/cdf38fca52c8ff0156a1b2ae40f76b5345224458) | yury-s |
| 2026-11-19 | [chore: roll Playwright to 1.66.0-next (1664ab2899) (#3357)](https://github.com/microsoft/playwright-python/commit/f5d8fecdaf13556fef738b155fd171a3bfc869e3) | microsoft-playwright-automation[bot] |
| 2026-11-19 | [build(deps): bump pytest-asyncio from 1.4.1 to 1.5.0 (#3356)](https://github.com/microsoft/playwright-python/commit/73e3a31c460622fefeb0f27246a85eb2754104ae) | dependabot[bot] |
| 2026-11-19 | [build(deps): bump types-pyyaml from 6.0.12.20261103 to 6.0.12.2026111…](https://github.com/microsoft/playwright-python/commit/cf56bf910ea3b5560ff1cf5ab0832ee325a7337c) | dependabot[bot] |
| 2026-11-18 | [chore: start the review bot on pull_request_target again (#3354)](https://github.com/microsoft/playwright-python/commit/613727245cbeed62c9b0fb27a84942abd276602f) | pavelfeldman |
| 2026-11-18 | [chore: roll Playwright to 1.66.0-next (8124fc3923) (#3353)](https://github.com/microsoft/playwright-python/commit/af8baa0ff17b494d934a992fdc7b399e696edea2) | microsoft-playwright-automation[bot] |

[See all commits ↗](https://github.com/microsoft/playwright-python/commits)

## ⬇️ Get it

```bash
git clone https://github.com/microsoft/playwright-python.git
```
