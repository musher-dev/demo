# Musher Demo

A showcase repository for the [Musher](https://hub.musher.dev) platform. It contains a ready-to-publish bundle with practical skills and agents, plus Python and TypeScript SDK examples that consume those same assets — demonstrating the full end-to-end value proposition.

## What's Inside

```
demo/
├── bundle/                   Musher bundle (skills + agents)
│   ├── musher.yaml           Bundle manifest
│   ├── skills/
│   │   ├── summarize-changes/     Summarize git history and diffs
│   │   └── write-commit-message/  Generate Conventional Commits messages
│   └── agents/
│       └── code-reviewer.md  Specialist read-only code-review agent
└── examples/                 SDK usage examples
    ├── python/               Python SDK (pull, install skills, use with Claude)
    └── typescript/           TypeScript SDK (pull, use with Claude)
```

## The Bundle

The `musher-dev/demo-starter` bundle ships two skills and one agent that solve everyday developer workflow problems.

| Asset | Type | What it does |
|-------|------|--------------|
| `summarize-changes` | Skill | Summarize git history, staged diffs, or PR changes into themed summaries |
| `write-commit-message` | Skill | Generate Conventional Commits–compliant messages from staged diffs |
| `code-reviewer` | Agent | Read-only specialist that reviews code with severity-graded findings |

### Use with a CLI harness

Install via the [Mush CLI](https://github.com/musher-dev/mush) into any project:

```bash
# Install and add to your project
mush bundle install musher-dev/demo-starter

# Or run ephemerally
mush bundle load musher-dev/demo-starter
```

Then invoke from Claude Code, Codex, or any supported harness:

```
Summarize the changes since the last release
Write a commit message for my staged changes
Use the code-reviewer agent to review the auth module
```

## SDK Examples

The `examples/` directory shows how to consume the same bundle assets programmatically.

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
npm run use-with-claude         # Use skills as system prompts with Anthropic SDK
```

## Related Repositories

| Repo | Description |
|------|-------------|
| [musher-dev/mush](https://github.com/musher-dev/mush) | Mush CLI — install and run bundles locally |
| [musher-dev/musher-cli](https://github.com/musher-dev/musher-cli) | CLI for publishing bundles to the registry |
| [musher-dev/python-sdk](https://github.com/musher-dev/python-sdk) | Python SDK for the Musher platform |
| [musher-dev/typescript-sdk](https://github.com/musher-dev/typescript-sdk) | TypeScript SDK for the Musher platform |
| [musher-dev/specs](https://github.com/musher-dev/specs) | Bundle definition schemas and specifications |
| [musher-dev/bundles](https://github.com/musher-dev/bundles) | Community bundle collection |

## Dev Container

This repo includes a batteries-included dev container with Node, Python, Go, Claude CLI, Codex CLI, and all the tooling needed to work on the bundle and examples. See [CONFIGURATION.md](CONFIGURATION.md) for full details.
