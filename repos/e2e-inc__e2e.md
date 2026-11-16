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
| 🍴 **Forks** | 751 |
| 🐞 **Open issues + PRs** | [115](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 98% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 110.8 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1715](https://github.com/e2e-inc/e2e/pull/1715) [`be460ec`](https://github.com/e2e-inc/e2e/commit/be460ecd91f4790884a36127310aab0d33853903) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Redact project tool results and errors before the model or AI trace recorder reads them, and redact and bound skip reasons before reporting. Avoid repeated scanning of malformed stack frames and trailing slashes in provider API endpoints. Keep ACP forwarding errors out of HTTP responses while preserving the cause in the runner's redacted failure output.

### [@e2e-dev/smol@0.1.3](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/smol%400.1.3)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - [#1609](https://github.com/e2e-inc/e2e/pull/1609) [`34a260c`](https://github.com/e2e-inc/e2e/commit/34a260cc59d7ebd1d414fd2716f955bd2a51795f) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Bump playwright-core to 1.65.0 and commander to 15.1.0. `fill` no longer rejects malformed date, time, color, and range values, and actions wait for an element to leave an `inert` subtree. Smol sandboxes use the Playwright 1.65.0 image.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/limrun@0.2.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/limrun%400.2.5)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1663](https://github.com/e2e-inc/e2e/pull/1663) [`322f00e`](https://github.com/e2e-inc/e2e/commit/322f00e55d8b2c8f834c150d5d239873bdad1daa) Thanks [@KrzysztofMoch](https://github.com/KrzysztofMoch)! - A Limrun device lease no longer names an agent-device `session` in its client configuration, which `@e2e-dev/mobile` rejected with `ENGINE_FAILURE` ("returned a lease without an id and a daemon baseUrl or JSON client configuration") before any test or session could start. The provider still allocates and renews the lease under its own session.

### [@e2e-dev/lightpanda@0.0.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/lightpanda%400.0.2)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/kernel@0.2.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/kernel%400.2.2)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [docs(readme): point Discord links to e2e.com/discord (#1840)](https://github.com/e2e-inc/e2e/commit/1f12af8574e4954bf4475973692cc3e21a009161) | kacperkapusciak |
| 2026-11-16 | [fix(plugin): point Codex terms link to the e2e license (#1842)](https://github.com/e2e-inc/e2e/commit/ed4ab954f8e62f6c697e9dd724b6774c004f560d) | KrzysztofMoch |
| 2026-11-16 | [chore(examples): upgrade examples to e2e 0.23.1 (#1838)](https://github.com/e2e-inc/e2e/commit/bb1fc00aaf340141f3dd97b06a1af985dd4100b7) | kacperkapusciak |
| 2026-11-16 | [fix(html-reporter): round durations before choosing the unit (#1829)](https://github.com/e2e-inc/e2e/commit/3fac999c460bc2dfc1268aba9316e3f67ca9ad4f) | Wali05 |
| 2026-11-16 | [docs(examples): list the experimental remote MCP over HTTP example (#…](https://github.com/e2e-inc/e2e/commit/9d4aaf0c07da15701cd6ed6d3c7b087a84bf5565) | jxnxts |
| 2026-11-16 | [fix(web,mobile): load the main entry without e2e installed (#1828)](https://github.com/e2e-inc/e2e/commit/40cb356a1ead2b09f195d91a47db62b5029315d3) | kdy1 |
| 2026-11-16 | [fix(ci): repair agent-device nightly setup and summary (#1832)](https://github.com/e2e-inc/e2e/commit/a6d125539456596e4518ee4da257b9a866feaadf) | thymikee |
| 2026-11-16 | [test(acp): wait for the cancel ack before tearing down the step direc…](https://github.com/e2e-inc/e2e/commit/902de2263e7d7ef25ce0c95dbdf73e937ec65731) | okwasniewski |
| 2026-11-16 | [feat(core): add launch, SessionState, and createAgent to @e2e-dev/cor…](https://github.com/e2e-inc/e2e/commit/dbe3dc54a9123b10e535441f785de2e81a202798) | kdy1 |
| 2026-11-16 | [perf(report): avoid copying accumulated Markdown file results (#1814)](https://github.com/e2e-inc/e2e/commit/5c7e18f922abb4830b9309498d89b088c040a268) | jxnxts |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
