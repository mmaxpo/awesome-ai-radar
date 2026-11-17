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
| 🍴 **Forks** | 762 |
| 🐞 **Open issues + PRs** | [106](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 99% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 115.9 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/testmu@0.0.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.5)
<sub>2026-11-13 · 4d ago</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1715](https://github.com/e2e-inc/e2e/pull/1715) [`be460ec`](https://github.com/e2e-inc/e2e/commit/be460ecd91f4790884a36127310aab0d33853903) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Redact project tool results and errors before the model or AI trace recorder reads them, and redact and bound skip reasons before reporting. Avoid repeated scanning of malformed stack frames and trailing slashes in provider API endpoints. Keep ACP forwarding errors out of HTTP responses while preserving the cause in the runner's redacted failure output.

### [@e2e-dev/smol@0.1.3](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/smol%400.1.3)
<sub>2026-11-13 · 4d ago</sub>

> **Patch Changes**
> - [#1609](https://github.com/e2e-inc/e2e/pull/1609) [`34a260c`](https://github.com/e2e-inc/e2e/commit/34a260cc59d7ebd1d414fd2716f955bd2a51795f) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Bump playwright-core to 1.65.0 and commander to 15.1.0. `fill` no longer rejects malformed date, time, color, and range values, and actions wait for an element to leave an `inert` subtree. Smol sandboxes use the Playwright 1.65.0 image.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/limrun@0.2.5](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/limrun%400.2.5)
<sub>2026-11-13 · 4d ago</sub>

> **Patch Changes**
> - [#1735](https://github.com/e2e-inc/e2e/pull/1735) [`16ff228`](https://github.com/e2e-inc/e2e/commit/16ff228576b0c5959d96450a626faafd580bdc75) Thanks [@gronxb](https://github.com/gronxb)! - Update agent-device to 0.21.37. Without `device`, the iOS pool no longer picks a paired iPhone that is not connected: agent-device now lists a phone whose CoreDevice tunnel is unavailable as not booted. A `device` that names such a phone fails in `prepare` with "iOS device is not ready for automation", before any test runs, instead of at app launch. A test's own swipe and scroll now skip agent-device's post-gesture wait, which 0.21.36 ignored.
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.
> - [#1663](https://github.com/e2e-inc/e2e/pull/1663) [`322f00e`](https://github.com/e2e-inc/e2e/commit/322f00e55d8b2c8f834c150d5d239873bdad1daa) Thanks [@KrzysztofMoch](https://github.com/KrzysztofMoch)! - A Limrun device lease no longer names an agent-device `session` in its client configuration, which `@e2e-dev/mobile` rejected with `ENGINE_FAILURE` ("returned a lease without an id and a daemon baseUrl or JSON client configuration") before any test or session could start. The provider still allocates and renews the lease under its own session.

### [@e2e-dev/lightpanda@0.0.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/lightpanda%400.0.2)
<sub>2026-11-13 · 4d ago</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

### [@e2e-dev/kernel@0.2.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/kernel%400.2.2)
<sub>2026-11-13 · 4d ago</sub>

> **Patch Changes**
> - [#1672](https://github.com/e2e-inc/e2e/pull/1672) [`3735887`](https://github.com/e2e-inc/e2e/commit/373588756937562aa89c7dd7f7995ac6b16db972) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Move GitHub repository metadata and CLI links to e2e-inc/e2e after the organization rename. Register the MCP server as io.github.e2e-inc/e2e.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [chore: add glama.json to claim the Glama listing (#1879)](https://github.com/e2e-inc/e2e/commit/e693cdcf0baee66dead26fa2e51a6693266b4b8f) | KrzysztofMoch |
| 2026-11-17 | [docs(readme): describe the e2e MCP server (#1876)](https://github.com/e2e-inc/e2e/commit/32dc6b2611c3fba948998eb7ac5294e960216e50) | KrzysztofMoch |
| 2026-11-17 | [docs(examples): add the Ricochet community example (#1753)](https://github.com/e2e-inc/e2e/commit/368dc874009e07e2b4dd5c63cff17836d1ece61c) | forever8896 |
| 2026-11-17 | [fix(agent): strip unknown fields on no-input agent tools (#1835)](https://github.com/e2e-inc/e2e/commit/95c574adec0d6844bda5fa503d1fe1cd64041ac5) | mvanhorn |
| 2026-11-17 | [feat(test): add test.skipIf and test.runIf (#1870)](https://github.com/e2e-inc/e2e/commit/1d0271b3066681a0aeca283060d33562616ece8a) | samanyudas |
| 2026-11-17 | [feat(cli): ask for a GitHub star after init, upgrade, and update noti…](https://github.com/e2e-inc/e2e/commit/6c4eddd0f9a295dbd8d29a8c5b432bb156f9d05e) | okwasniewski |
| 2026-11-17 | [chore(deps): bump workspace deps to latest (#1871)](https://github.com/e2e-inc/e2e/commit/8af43f5075661ad61bcf36f246e1a269e8c1bb17) | okwasniewski |
| 2026-11-17 | [feat(expect): add toHaveRole locator matcher (#1857)](https://github.com/e2e-inc/e2e/commit/d4fb5ccd49a841afc9afc3c741cdb41990f38322) | Asheesh7298 |
| 2026-11-17 | [fix(report): keep \r\n line breaks in serialized errors and the JUnit…](https://github.com/e2e-inc/e2e/commit/aadf95506d05d2888db75792182b634912acbcef) | kdy1 |
| 2026-11-17 | [chore(mobile): bump agent-device to 0.21.38 (#1859)](https://github.com/e2e-inc/e2e/commit/e65091bbe10b00860ec6240336b57933a7ce65f7) | kdy1 |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
