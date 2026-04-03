# Configuration Guide

**Philosophy: One need, one place.** Every configuration concern maps to exactly one canonical location.

## Decision Tree

```
Where does my configuration go?

Language runtime or system package?
  → devcontainer.json → features block

CLI tool installed via curl/npm?
  → scripts/lib/base-setup.sh (add a function, call from post-create.sh)

VS Code editor behavior or extension?
  → devcontainer.json → customizations.vscode block

Shell aliases, oh-my-zsh plugins, or shell functions?
  → config/shell/ directory

One-time setup step?
  → scripts/post-create.sh

Runs on every container start?
  → scripts/startup.sh
```

## Quick Reference

| Category | Need | Canonical Location |
|---|---|---|
| **Runtimes** | Language runtimes (Node, Python) | `devcontainer.json` → `features` |
| | Package managers (uv) | `devcontainer.json` → `features` |
| | CLI tools (Claude) | `scripts/lib/base-setup.sh` |
| **Editor** | VS Code settings | `devcontainer.json` → `customizations.vscode.settings` |
| | VS Code extensions | `devcontainer.json` → `customizations.vscode.extensions` |
| **Shell** | Shell aliases, functions | `.devcontainer/config/shell/` |
| | Git config | Host `.gitconfig` (auto-forwarded) |
| **Environment** | Runtime behavior vars | `devcontainer.json` → `containerEnv` |
| | PATH extensions | `devcontainer.json` → `remoteEnv` |
| | Secrets (API keys) | Host env forwarded via `remoteEnv` — never committed |
| **Lifecycle** | One-time container setup | `scripts/post-create.sh` → `lib/base-setup.sh` |
| | Every-start tasks | `scripts/startup.sh` |
| **AI Tools** | Claude CLI installation | `lib/base-setup.sh` |
| | Claude config persistence | `devcontainer.json` → `mounts` (named volume) |

---

## Shell Customization

| Pattern | Tracked | Purpose |
|---|---|---|
| `*.shared.sh` | Yes | Team defaults — aliases, functions |
| `*.local.sh` | No (gitignored) | Personal overrides |

Shared files are sourced first, then local files.

---

## Environment Variables

| Scope | Location | When to Use |
|---|---|---|
| **Container-wide** | `devcontainer.json` → `containerEnv` | Runtime behavior (`PYTHONUNBUFFERED`, etc.) |
| **Remote/IDE** | `devcontainer.json` → `remoteEnv` | PATH extensions, forwarded host secrets |

Never commit secrets. Forward them from your host:

```jsonc
"remoteEnv": {
  "MY_API_KEY": "${localEnv:MY_API_KEY}"
}
```

---

## Lifecycle

| Hook | Runs | Use For |
|---|---|---|
| `postCreateCommand` | Once, on container creation | Tool installation, permissions |
| `postStartCommand` | Every container start | Service startup |

### Script Layers

```
post-create.sh              ← Entry point (repo-specific customization)
  └── lib/base-setup.sh     ← Reusable orchestrator (Claude CLI, config dirs)
        └── lib/common.sh   ← Shared utilities (log, retry, has_cmd)
```

---

## Directory Map

```
.devcontainer/
  devcontainer.json           Runtimes, extensions, settings, mounts
  .env.example                Environment template (copy to .env)
  .env                        Local overrides (gitignored)
  config/
    shell/
      aliases.shared.sh       Team-default shell aliases
  scripts/
    post-create.sh            One-time setup entry point
    startup.sh                Every-start launcher
    lib/
      base-setup.sh           Reusable tool installer
      common.sh               Shared utilities
      motd.sh                 Message of the day
```
