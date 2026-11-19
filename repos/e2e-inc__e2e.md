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
| 🍴 **Forks** | 777 |
| 🐞 **Open issues + PRs** | [128](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 99% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 120.3 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5)
<sub>2026-11-13 · 6d ago</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1715](https://github.com/e2e-inc/e2e/pull/1715) [`be460ec`](https://github.com/e2e-inc/e2e/commit/be460ecd91f4790884a36127310aab0d33853903) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Redact project tool results and errors before the model or AI trace recorder reads them, and redact and bound skip reasons before reporting. Avoid repeated scanning of malformed stack frames and trailing slashes in provider API endpoints. Keep ACP forwarding errors out of HTTP responses while preserving the cause in the runner's redacted failure output.

### [@e2e-dev/smol@0.1.3](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/smol%400.1.3)
<sub>2026-11-13 · 6d ago</sub>

> **Patch Changes**
> - [#1609](https://github.com/e2e-inc/e2e/pull/1609) [`34a260c`](https://github.com/e2e-inc/e2e/commit/34a260cc59d7ebd1d414fd2716f955bd2a51795f) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Bump playwright-core to 1.65.0 and commander to 15.1.0. `fill` no longer rejects malformed date, time, color, and range values, and actions wait for an element to leave an `inert` subtree. Smol sandboxes use the Playwright 1.65.0 image.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/limrun@0.2.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/limrun%400.2.5)
<sub>2026-11-13 · 6d ago</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1663](https://github.com/e2e-inc/e2e/pull/1663) [`322f00e`](https://github.com/e2e-inc/e2e/commit/322f00e55d8b2c8f834c150d5d239873bdad1daa) Thanks [@KrzysztofMoch](https://github.com/KrzysztofMoch)! - A Limrun device lease no longer names an agent-device `session` in its client configuration, which `@e2e-dev/mobile` rejected with `ENGINE_FAILURE` ("returned a lease without an id and a daemon baseUrl or JSON client configuration") before any test or session could start. The provider still allocates and renews the lease under its own session.

### [@e2e-dev/lightpanda@0.0.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/lightpanda%400.0.2)
<sub>2026-11-13 · 6d ago</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/kernel@0.2.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/kernel%400.2.2)
<sub>2026-11-13 · 6d ago</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [chore(skills): hide vendored skills on skills.sh and group the public…](https://github.com/e2e-inc/e2e/commit/624636d05d6c205d8d136c99567783f5c1833a52) | KrzysztofMoch |
| 2026-11-19 | [feat(mcp)!: remove the run_tests tool (#1967)](https://github.com/e2e-inc/e2e/commit/0e9d58ec98dd4522929766c533f8078239fa72f9) | okwasniewski |
| 2026-11-19 | [feat(cli): pause at screen.pause() under --watch (#1905)](https://github.com/e2e-inc/e2e/commit/34322c54165a214d8c65d8a10e09b788b7cbc382) | satya164 |
| 2026-11-19 | [chore: move the conduct and contributor emails to e2e.com (#1965)](https://github.com/e2e-inc/e2e/commit/60d29cfe4c9d88b00659e0d0e00b8973d61e7391) | szymonrybczak |
| 2026-11-19 | [fix(oauth): send the e2e User-Agent on sign-in and token requests (#1…](https://github.com/e2e-inc/e2e/commit/34b52baa0d0595827a18158d788ab9b73b791019) | Jaaneek |
| 2026-11-19 | [feat: add screen.pause() (#1904)](https://github.com/e2e-inc/e2e/commit/4893d1dd7574a6661363bc43e33b335f40be667c) | satya164 |
| 2026-11-19 | [fix(cache): read a clock time written as 5:42pm as volatile (#1955)](https://github.com/e2e-inc/e2e/commit/f3cd0321048ee73aae6464599473cb62b130341a) | JaynouOliver |
| 2026-11-19 | [refactor(run): generalize the --step hold path (#1901)](https://github.com/e2e-inc/e2e/commit/759d1fc260e5c5f6fc7a7eff01d482c12849904b) | satya164 |
| 2026-11-19 | [docs(examples): list a local Moli sign-in example (#1944)](https://github.com/e2e-inc/e2e/commit/ae36939a85a7537655b3032a40fecd704e2a9c56) | ldm0 |
| 2026-11-19 | [docs(es): translate the getting-started and platform pages (#1932)](https://github.com/e2e-inc/e2e/commit/aa5190bcd8b5f9b067509e177613aa77c928a261) | kblok |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
