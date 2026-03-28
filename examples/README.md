# Examples

SDK usage examples that demonstrate the full Musher value proposition using the `musher-dev/demo-starter` bundle.

## Structure

```
examples/
├── python/          Python SDK examples
│   ├── 01_pull_bundle.py       Pull and inspect a bundle
│   ├── 02_install_skills.py    Install skills into a Claude Code project
│   └── 03_use_with_claude.py   Use skills as system prompts via Anthropic API
└── typescript/      TypeScript SDK examples
    ├── 01-pull-bundle.ts       Pull and inspect a bundle
    └── 02-use-with-claude.ts   Use skills as system prompts via Anthropic SDK
```

## Quick Start

**Python**
```bash
cd python
pip install -r requirements.txt
export MUSHER_API_KEY="mush_..."
python 01_pull_bundle.py
```

**TypeScript**
```bash
cd typescript
npm install
export MUSHER_API_KEY="mush_..."
npm run pull-bundle
```

## What These Examples Show

1. **Pull a bundle** — Fetch the `musher-dev/demo-starter` bundle from the registry and inspect its skills, agents, and raw files.
2. **Install skills** *(Python only)* — Copy skills into a Claude Code project directory so they are auto-discovered by the harness.
3. **Use with Claude** — Load a skill's instructions as a system prompt and call the Anthropic API directly, demonstrating programmatic use of bundle assets.
