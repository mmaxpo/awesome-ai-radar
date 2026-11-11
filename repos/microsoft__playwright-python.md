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
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2020-07-01 |
| 📦 **Latest release** | [v1.65.0](https://github.com/microsoft/playwright-python/releases/tag/v1.65.0) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 15.8 MB |
| 🌐 **Website** | https://playwright.dev/python/ |

## 📦 Recent releases

### [v1.65.0](https://github.com/microsoft/playwright-python/releases/tag/v1.65.0)
<sub>2026-11-09 · yesterday</sub>

> **🧾 Locator code in Python**
> A locator from [locator.normalize()](https://playwright.dev/python/docs/api/class-locator#locator-normalize) now converts to a string as Python code. Use it with [page.get_by_ref()](https://playwright.dev/python/docs/api/class-page#page-get-by-ref) to turn an element that an agent picks from a [page.aria_snapshot()](https://playwright.dev/python/docs/api/class-page#page-aria-snapshot) in the `"ai"` mode into code for your test:
> ```python
> normalized = page.get_by_ref("e2").normalize()
> print(str(normalized))
> **get_by_role("button", name="Submit")**
> …

### [v1.64.1](https://github.com/microsoft/playwright-python/releases/tag/v1.64.1)
<sub>2026-10-22 · 19d ago</sub>

> **Highlights**
> https://github.com/microsoft/playwright-python/pull/3283 - chore: roll Node.js to 24.22.1
> The bundled Node.js 24.22.1 is a security release that distrusts the compromised eMudhra intermediate CAs. The driver uses Node's CA store for its own TLS connections, for example `connect_over_cdp` to a `wss://` endpoint.
> **Browser Versions**
> - Chromium 156.0.8078.4
> - Mozilla Firefox 157.0
> …

### [v1.64.0](https://github.com/microsoft/playwright-python/releases/tag/v1.64.0)
<sub>2026-10-13 · 28d ago</sub>

> **🧰 WebMCP**
> New [page.webmcp](https://playwright.dev/python/docs/api/class-page#page-webmcp) and [frame.webmcp](https://playwright.dev/python/docs/api/class-frame#frame-webmcp) give access to the tools that a page registers through
> the experimental [WebMCP](https://webmachinelearning.github.io/webmcp/) browser API, so you can test them like
> any other part of your app:
> ```python
> browser = chromium.launch(args=["--enable-features=WebMCP"])
> …

### [v1.63.0](https://github.com/microsoft/playwright-python/releases/tag/v1.63.0)
<sub>2026-09-15 · 1mo ago</sub>

> **🪟 Locate across frames**
> [page.frame_locator()](https://playwright.dev/python/docs/api/class-page#page-frame-locator) and [frame.frame_locator()](https://playwright.dev/python/docs/api/class-frame#frame-frame-locator) called without a selector search in any frame of the
> subtree, so you no longer need to locate the iframe first:
> ```python
> **Finds the button in any frame on the page.**
> page.frame_locator().get_by_role("button").click()
> …

### [v1.62.0](https://github.com/microsoft/playwright-python/releases/tag/v1.62.0)
<sub>2026-07-31 · 3mo ago</sub>

> **🖼️ WebP screenshots**
> [page.screenshot()](<https://playwright.dev/python/docs/api/class-page#page-screenshot>) and [locator.screenshot()](<https://playwright.dev/python/docs/api/class-locator#locator-screenshot>) can now capture screenshots in the WebP format. Playwright infers the format from a `.webp` file extension, or you can set the `type` explicitly. Quality `100` (the default) is lossless, while lower values use lossy compression:
> ```python
> page.screenshot(path="homepage.webp", quality=50)
> ```
> **New APIs**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-10 | [devops(docker): publish stable images from the tip of a release branc…](https://github.com/microsoft/playwright-python/commit/89436fb88df74b0f1c5ef4b9df3a113d409bf3cd) | yury-s |
| 2026-11-10 | [chore(bots): name the agent workflows agent-*, and start tasks by han…](https://github.com/microsoft/playwright-python/commit/63cdffb905cbd09c1b73ae2cde51f8dd353bccd8) | pavelfeldman |
| 2026-11-10 | [devops(docker): install libatomic1 for the Node.js binary of the driv…](https://github.com/microsoft/playwright-python/commit/02e247e3fe492566110e94cbb972f09b69b0952e) | dgozman |
| 2026-11-10 | [chore(bots): hand triage, review, tasks and rolls to the Playwright b…](https://github.com/microsoft/playwright-python/commit/6b42560a3b5849dc98a47e77ff0536b81c45b53d) | pavelfeldman |
| 2026-11-09 | [chore: roll Playwright to 1.65.0 (a1f35e1955) (#3327)](https://github.com/microsoft/playwright-python/commit/18175f80c7ede1073f91e2df37587500a5f902c7) | microsoft-playwright-automation[bot] |
| 2026-11-05 | [devops: wait 7 days before Dependabot proposes pip updates (#3325)](https://github.com/microsoft/playwright-python/commit/6bd6aaa2073695da7320277862ceede0b9756621) | pavelfeldman |
| 2026-11-05 | [devops(bots): pin the shared actions to a commit SHA (#3319)](https://github.com/microsoft/playwright-python/commit/1e2746c96817d63c3136f21ac02be44d558c5c63) | pavelfeldman |
| 2026-11-04 | [fix(deps): remove unused pyee runtime dependency (#3316)](https://github.com/microsoft/playwright-python/commit/015115d530c5ce36edfbea3b2e1a156379509d45) | microsoft-playwright-automation[bot] |
| 2026-11-04 | [chore: roll Playwright to 1.66.0-next (0ea3691032) (#3318)](https://github.com/microsoft/playwright-python/commit/df2bf0bf04d75dc0cd4d2e0ec4f5ab728545a8d8) | microsoft-playwright-automation[bot] |
| 2026-11-03 | [devops(roll): open the pull request with publish-calls (#3317)](https://github.com/microsoft/playwright-python/commit/989329c642af4336c5958dee92a061e546392084) | pavelfeldman |

[See all commits ↗](https://github.com/microsoft/playwright-python/commits)

## ⬇️ Get it

```bash
git clone https://github.com/microsoft/playwright-python.git
```
