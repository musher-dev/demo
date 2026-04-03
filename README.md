# Musher Demo

A showcase repository for the [Musher](https://hub.musher.dev) platform. It contains a ready-to-publish bundle with practical skills and agents, plus Python and TypeScript SDK examples that consume those same assets — demonstrating the full end-to-end value proposition.

## Start Here

Install the [Musher CLI](https://github.com/musher-dev/musher-cli):

```bash
curl -fsSL https://get.musher.dev | sh
```

## What's Inside

```
demo/
├── bundle/                   Musher bundle (skills + agents)
│   ├── musher.yaml           Bundle manifest
│   ├── skills/
│   │   ├── summarizing-changes/        Summarize git history and diffs
│   │   └── writing-commit-messages/    Generate Conventional Commits messages
│   └── agents/
│       └── code-reviewer.md  Specialist read-only code-review agent
└── examples/                 SDK usage examples
    ├── python/               Python SDK (pull, install skills, use with Claude)
    └── typescript/           TypeScript SDK (pull, install skills, use with Claude)
```

## The Bundle

The `musher-examples/demo-starter` bundle ships two skills and one agent that solve everyday developer workflow problems.

| Asset | Type | What it does |
|-------|------|--------------|
| `summarizing-changes` | Skill | Summarize git history, staged diffs, or PR changes into themed summaries |
| `writing-commit-messages` | Skill | Generate Conventional Commits–compliant messages from staged diffs |
| `code-reviewer` | Agent | Read-only specialist that reviews code with severity-graded findings |

### Use with a CLI harness

Install via the [Musher CLI](https://github.com/musher-dev/musher-cli) into any project:

```bash
# Install and add to your project
musher bundle pull musher-examples/demo-starter

# Or run ephemerally
musher bundle load musher-examples/demo-starter
```

Then invoke from Claude Code, Codex, or any supported harness:

```
Summarize the changes since the last release
Write a commit message for my staged changes
Use the code-reviewer agent to review the auth module
```

## SDK Examples

The `examples/` directory shows how to consume the same bundle assets programmatically.

Both SDKs need a `MUSHER_API_KEY` — sign up at [hub.musher.dev](https://hub.musher.dev) and generate one under **Settings > API Keys**. Examples that call the Anthropic API also need an `ANTHROPIC_API_KEY` from [console.anthropic.com](https://console.anthropic.com/).

> **Note — local source vs. published names:**
> The `bundle/` directory contains the *source* files for this bundle. Asset names in the
> source manifest (`musher.yaml`) may differ from names in the published bundle on
> [hub.musher.dev](https://hub.musher.dev). The SDK examples reference the **published**
> names (e.g. `summarizing-changes` rather than the source name `summarize-changes`).

### Python

```bash
cd examples/python
pip install -r requirements.txt
export MUSHER_API_KEY="mush_..."
python 01_pull_bundle.py        # Inspect bundle contents
python 02_install_skills.py     # Install skills into a Claude Code project
python 03_use_with_claude.py    # Use skills as system prompts with Anthropic API
```

### TypeScript

```bash
cd examples/typescript
npm install
export MUSHER_API_KEY="mush_..."
npm run pull-bundle             # Inspect bundle contents
npm run install-skills          # Install skills into a Claude Code project
npm run use-with-claude         # Use skills as system prompts with Anthropic SDK
```

## Related Repositories

| Repo | Description |
|------|-------------|
| [musher-dev/musher-cli](https://github.com/musher-dev/musher-cli) | Musher CLI — install, run, author, and publish bundles |
| [musher-dev/python-sdk](https://github.com/musher-dev/python-sdk) | Python SDK for the Musher platform |
| [musher-dev/typescript-sdk](https://github.com/musher-dev/typescript-sdk) | TypeScript SDK for the Musher platform |
| [musher-dev/specs](https://github.com/musher-dev/specs) | Bundle definition schemas and specifications |
| [musher-dev/bundles](https://github.com/musher-dev/bundles) | Community bundle collection |

## Dev Container

This repo includes a batteries-included dev container with Node, Python, Go, Claude CLI, Codex CLI, and all the tooling needed to work on the bundle and examples. See [CONFIGURATION.md](CONFIGURATION.md) for full details.
