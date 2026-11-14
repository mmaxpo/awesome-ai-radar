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
| ⭐ **Stars** | 13.9k |
| 🍴 **Forks** | 741 |
| 🐞 **Open issues + PRs** | [108](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 98% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 111.0 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5)
<sub>2026-11-13 · yesterday</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1715](https://github.com/e2e-inc/e2e/pull/1715) [`be460ec`](https://github.com/e2e-inc/e2e/commit/be460ecd91f4790884a36127310aab0d33853903) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Redact project tool results and errors before the model or AI trace recorder reads them, and redact and bound skip reasons before reporting. Avoid repeated scanning of malformed stack frames and trailing slashes in provider API endpoints. Keep ACP forwarding errors out of HTTP responses while preserving the cause in the runner's redacted failure output.

### [@e2e-dev/smol@0.1.3](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/smol%400.1.3)
<sub>2026-11-13 · yesterday</sub>

> **Patch Changes**
> - [#1609](https://github.com/e2e-inc/e2e/pull/1609) [`34a260c`](https://github.com/e2e-inc/e2e/commit/34a260cc59d7ebd1d414fd2716f955bd2a51795f) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Bump playwright-core to 1.65.0 and commander to 15.1.0. `fill` no longer rejects malformed date, time, color, and range values, and actions wait for an element to leave an `inert` subtree. Smol sandboxes use the Playwright 1.65.0 image.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/limrun@0.2.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/limrun%400.2.5)
<sub>2026-11-13 · yesterday</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1663](https://github.com/e2e-inc/e2e/pull/1663) [`322f00e`](https://github.com/e2e-inc/e2e/commit/322f00e55d8b2c8f834c150d5d239873bdad1daa) Thanks [@KrzysztofMoch](https://github.com/KrzysztofMoch)! - A Limrun device lease no longer names an agent-device `session` in its client configuration, which `@e2e-dev/mobile` rejected with `ENGINE_FAILURE` ("returned a lease without an id and a daemon baseUrl or JSON client configuration") before any test or session could start. The provider still allocates and renews the lease under its own session.

### [@e2e-dev/lightpanda@0.0.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/lightpanda%400.0.2)
<sub>2026-11-13 · yesterday</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/kernel@0.2.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/kernel%400.2.2)
<sub>2026-11-13 · yesterday</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [refactor(scripts): share the docs page walker across the checks (#1796)](https://github.com/e2e-inc/e2e/commit/f41edce99dbfe47a143b3fe4f799d3c3994d8a67) | DeryFerd |
| 2026-11-14 | [test(explore): pin the finding fields the schema test left unbounded …](https://github.com/e2e-inc/e2e/commit/020c57d6cb4525742e2dadbeeae8a9bd84bc1c28) | DeryFerd |
| 2026-11-14 | [test(run): run two serial groups through the scheduler at once (#1790)](https://github.com/e2e-inc/e2e/commit/d9c581fefcd9dceeac795ff7c178280da80e8fe6) | DeryFerd |
| 2026-11-14 | [fix(mobile): keep userinfo out of openLink and openApp step labels (#…](https://github.com/e2e-inc/e2e/commit/74435e23b68a103ce21f25947c3b7a8a4015cb2a) | karolkulesza |
| 2026-11-14 | [fix(mobile): refuse an unknown snapshot or videoTouches value in mobi…](https://github.com/e2e-inc/e2e/commit/dd39974acedee5b68042dd219f99249f781dfaf0) | karolkulesza |
| 2026-11-14 | [docs(web): clarify media emulation tab scope (#1772)](https://github.com/e2e-inc/e2e/commit/b56e8ed52539eab09a08af7b76ef34d0328936ea) | nguyenvanhieu1710 |
| 2026-11-14 | [chore(deps): bump workspace deps to latest, playwright-core to 1.65.1…](https://github.com/e2e-inc/e2e/commit/ceaea64ceead09d0a0f8cb5b384ef0d9ffac23a1) | okwasniewski |
| 2026-11-14 | [fix(acp): cancel the wait for the previous agent turn when the step e…](https://github.com/e2e-inc/e2e/commit/f64e7dba8d617a8804cba96cd8c885658db8aca5) | jxnxts |
| 2026-11-13 | [docs(mobile): say which device runs when no device is named (#1728)](https://github.com/e2e-inc/e2e/commit/e167149af1d390492af09e5fe28bb64072e9df64) | karolkulesza |
| 2026-11-13 | [docs(screen): say what doubleTapAt does on a device (#1733)](https://github.com/e2e-inc/e2e/commit/800a93e62a331c11f47dccdc8eac99124ebd36d2) | karolkulesza |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
