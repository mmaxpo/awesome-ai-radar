# e2e-inc/e2e

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/e2e-inc/e2e)

> Next generation e2e testing framework for web and mobile apps.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | End-to-end testing for agent-written code |
| **Added** | 2026-11-14 |

↪️ **Moved** — was `tester-army/e2e` · 🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 14.0k |
| 🍴 **Forks** | 772 |
| 🐞 **Open issues + PRs** | [119](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 99% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 119.1 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5)
<sub>2026-11-13 · 5d ago</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1715](https://github.com/e2e-inc/e2e/pull/1715) [`be460ec`](https://github.com/e2e-inc/e2e/commit/be460ecd91f4790884a36127310aab0d33853903) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Redact project tool results and errors before the model or AI trace recorder reads them, and redact and bound skip reasons before reporting. Avoid repeated scanning of malformed stack frames and trailing slashes in provider API endpoints. Keep ACP forwarding errors out of HTTP responses while preserving the cause in the runner's redacted failure output.

### [@e2e-dev/smol@0.1.3](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/smol%400.1.3)
<sub>2026-11-13 · 5d ago</sub>

> **Patch Changes**
> - [#1609](https://github.com/e2e-inc/e2e/pull/1609) [`34a260c`](https://github.com/e2e-inc/e2e/commit/34a260cc59d7ebd1d414fd2716f955bd2a51795f) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Bump playwright-core to 1.65.0 and commander to 15.1.0. `fill` no longer rejects malformed date, time, color, and range values, and actions wait for an element to leave an `inert` subtree. Smol sandboxes use the Playwright 1.65.0 image.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/limrun@0.2.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/limrun%400.2.5)
<sub>2026-11-13 · 5d ago</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1663](https://github.com/e2e-inc/e2e/pull/1663) [`322f00e`](https://github.com/e2e-inc/e2e/commit/322f00e55d8b2c8f834c150d5d239873bdad1daa) Thanks [@KrzysztofMoch](https://github.com/KrzysztofMoch)! - A Limrun device lease no longer names an agent-device `session` in its client configuration, which `@e2e-dev/mobile` rejected with `ENGINE_FAILURE` ("returned a lease without an id and a daemon baseUrl or JSON client configuration") before any test or session could start. The provider still allocates and renews the lease under its own session.

### [@e2e-dev/lightpanda@0.0.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/lightpanda%400.0.2)
<sub>2026-11-13 · 5d ago</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/kernel@0.2.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/kernel%400.2.2)
<sub>2026-11-13 · 5d ago</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [feat(test)!: set fixtures up on demand, once per worker, and in befor…](https://github.com/e2e-inc/e2e/commit/847a09e6dbd39e09c8941ddcc903003c61412d81) | KrzysztofMoch |
| 2026-11-18 | [feat: add a dot reporter (#1911)](https://github.com/e2e-inc/e2e/commit/902f044b49d1ca90bf12af80ccb53f5277305f9f) | FaZeDrug |
| 2026-11-18 | [feat(html-reporter): filter a run's results by target (#1793)](https://github.com/e2e-inc/e2e/commit/f5cda163137b298bfef82bd25281d7e872d47f46) | DeryFerd |
| 2026-11-18 | [docs: make translations best effort (#1930)](https://github.com/e2e-inc/e2e/commit/f74dd548fa100219cefe0cf468b33d66b3e68cbf) | kacperkapusciak |
| 2026-11-18 | [docs: show how to connect e2e mcp to OpenCode (#1926)](https://github.com/e2e-inc/e2e/commit/6fbcb66f02ea1783345696c99d8baba9f9c708f6) | KrzysztofMoch |
| 2026-11-18 | [feat(lightpanda): load linked stylesheets by default (#1923)](https://github.com/e2e-inc/e2e/commit/bc41a25c7d7e6d6f62c5b78b516c0a1f71c2b45c) | cdebled |
| 2026-11-18 | [fix(cache): read CJK counts followed by を, が, 이 or 를 as counts (#1917)](https://github.com/e2e-inc/e2e/commit/6a1cb9af45e1b12f6b28070aab7f094dfc8a3c9f) | Toraastrta |
| 2026-11-18 | [docs(examples): list the Lightpanda partner example (#1856)](https://github.com/e2e-inc/e2e/commit/a8b5371642bbdc3f6331cbb85bb61df31200ac9e) | cdebled |
| 2026-11-18 | [fix(examples): give the MAUI example's first iOS assertion 10 seconds…](https://github.com/e2e-inc/e2e/commit/f0d34fe249682cd9591b6b347c55addd49796348) | kacperkapusciak |
| 2026-11-18 | [docs(examples): list a form test with one agent step on OpenRouter (#…](https://github.com/e2e-inc/e2e/commit/d9891ead1dffd6eb4bbe79e897d4a91714e101d1) | jxnxts |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
