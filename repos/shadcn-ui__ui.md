# shadcn-ui/ui

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/shadcn-ui/ui)

> Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make your own.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🎨 Design & creative |
| **Project** | — |
| **Why it's worth a look** | shadcn/ui components, CLI, registry and MCP |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 128.2k |
| 🍴 **Forks** | 11.4k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/shadcn-ui/ui/issues) |
| 💻 **Languages** | TypeScript 86% · MDX 10% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `components` `nextjs` `radix-ui` `react` `tailwindcss` `ui` `shadcn` `base-ui` `laravel` `tanstack` `vite` `react-aria` `react-aria-components` `ai` `gen-ui` `generative-ai` `generative-ui` |
| 🕒 **Last activity** | 2026-11-13 (yesterday) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [shadcn@4.23.0](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.23.0) — 2026-10-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 73.6 MB |
| 🌐 **Website** | https://ui.shadcn.com |

## 📦 Recent releases

### [shadcn@4.23.0](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.23.0)
<sub>2026-10-27 · 18d ago</sub>

> **Minor Changes**
> - [#12296](https://github.com/shadcn-ui/ui/pull/12296) [`15f59b4`](https://github.com/shadcn-ui/ui/commit/15f59b41750542ef5d41ee34601a85a4e7c1be17) Thanks [@mattzcarey](https://github.com/mattzcarey)! - Upgrade the MCP server to MCP TypeScript SDK v2 (`@modelcontextprotocol/server`). `shadcn mcp` now serves MCP protocol 2026-07-28 as well as earlier versions. The `shadcn/mcp` export is now an `McpServer`, and a new `createServer()` export returns a fresh instance per connection. Code that called `server.setRequestHandler(...)` on the old `Server` export should use `server.registerTool(...)` or `server.server.setRequestHandler(...)` instead.

### [shadcn@4.22.2](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.22.2)
<sub>2026-10-27 · 18d ago</sub>

> **Patch Changes**
> - [#12479](https://github.com/shadcn-ui/ui/pull/12479) [`8f04138`](https://github.com/shadcn-ui/ui/commit/8f04138777c1b6996e709993362a7b0a12888ecf) Thanks [@dependabot](https://github.com/apps/dependabot)! - Update `undici` to 7.30.1.
> - Updated dependencies [[`8f04138`](https://github.com/shadcn-ui/ui/commit/8f04138777c1b6996e709993362a7b0a12888ecf)]:
>   - @shadcn/registry@0.2.1

### [@shadcn/registry@0.2.1](https://github.com/shadcn-ui/ui/releases/tag/%40shadcn/registry%400.2.1)
<sub>2026-10-27 · 18d ago</sub>

> **Patch Changes**
> - [#12479](https://github.com/shadcn-ui/ui/pull/12479) [`8f04138`](https://github.com/shadcn-ui/ui/commit/8f04138777c1b6996e709993362a7b0a12888ecf) Thanks [@dependabot](https://github.com/apps/dependabot)! - Update `undici` to 7.30.1.

### [shadcn@4.22.1](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.22.1)
<sub>2026-10-18 · 26d ago</sub>

> **Patch Changes**
> - [#12360](https://github.com/shadcn-ui/ui/pull/12360) [`4381eeb`](https://github.com/shadcn-ui/ui/commit/4381eeb3fe421af7d25b780f85ff9cbc8d50c51a) Thanks [@shadcn](https://github.com/shadcn)! - Fix `shadcn add --all` and the component picker to only include components available for the project's style.

### [shadcn@4.22.0](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.22.0)
<sub>2026-10-16 · 29d ago</sub>

> **Minor Changes**
> - [#12298](https://github.com/shadcn-ui/ui/pull/12298) [`954ce95`](https://github.com/shadcn-ui/ui/commit/954ce953412867a57b7e067c076fa7fd395ea115) Thanks [@shadcn](https://github.com/shadcn)! - Upgrade to Zod 4. `shadcn/schema` and `@shadcn/registry/schema` now export Zod 4 schemas, so passing them to Zod 3's `z` no longer typechecks. On Zod 3, use the exported types (`RegistryItem`, `RegistryItemFile`, `Config`) and the schema's own methods (`registryItemSchema.array()`) instead of `z.infer` and `z.array`. Zod errors expose `issues`, not `errors`. Validation messages now use Zod 4's wording.
> **Patch Changes**
> - Updated dependencies [[`954ce95`](https://github.com/shadcn-ui/ui/commit/954ce953412867a57b7e067c076fa7fd395ea115)]:
>   - @shadcn/registry@0.2.0

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [chore(deps): bump the deps group (#12691)](https://github.com/shadcn-ui/ui/commit/e62c9435fff729a175f38983dee73b2cb4f6a069) | dependabot[bot] |
| 2026-11-13 | [chore(deps): bump the deps group (#12689)](https://github.com/shadcn-ui/ui/commit/dc71abffb601162a12345dc0f363fb3b552349fd) | dependabot[bot] |
| 2026-11-13 | [chore(deps): bump the deps group in /templates/astro-app with 4 updat…](https://github.com/shadcn-ui/ui/commit/cb373dbe0de08c85783f78d4390b33032b523935) | dependabot[bot] |
| 2026-11-13 | [chore(deps-dev): bump the deps group (#12686)](https://github.com/shadcn-ui/ui/commit/f60ff2a02be0fd689fa70c247543aeaea32f18a5) | dependabot[bot] |
| 2026-11-13 | [chore(deps): bump the deps group (#12684)](https://github.com/shadcn-ui/ui/commit/06ce8b7c59a7263289ab111fd60133d1f33f4a65) | dependabot[bot] |
| 2026-11-13 | [chore(deps): bump the deps group (#12683)](https://github.com/shadcn-ui/ui/commit/ec8fb0859ce86b04f688c43bbcc03b38cd59c2fa) | dependabot[bot] |
| 2026-11-13 | [chore(deps): bump the deps group (#12682)](https://github.com/shadcn-ui/ui/commit/077fd2b4c35e172cbfc93218c682b07110e2feb5) | dependabot[bot] |
| 2026-11-13 | [chore(deps): bump the deps group in /templates/next-app with 2 update…](https://github.com/shadcn-ui/ui/commit/56f71cfab3064180f87896d4bb170050a0012440) | dependabot[bot] |
| 2026-11-11 | [feat(registry): add community registries (#12629)](https://github.com/shadcn-ui/ui/commit/dd41d19e2f80ff6891951f7ced74c2c9a650b065) | shadcn |
| 2026-11-08 | [chore(deps): bump the deps group in /templates/start-app with 2 updat…](https://github.com/shadcn-ui/ui/commit/8ab27715521cbd4f87ae6886cd989cbb678f6de7) | dependabot[bot] |

[See all commits ↗](https://github.com/shadcn-ui/ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/shadcn-ui/ui.git
```
