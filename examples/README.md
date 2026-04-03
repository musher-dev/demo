# Examples

SDK usage examples demonstrating the full Musher lifecycle: author → publish → consume with Claude Agent SDK.

See [Python README](python/README.md) and [TypeScript README](typescript/README.md) for language-specific setup.

## Structure

```
examples/
├── python/
│   ├── repo_docs_audit.py               Pull, install, and run Agent SDK in one script
│   ├── fixtures/under_documented_repo/   Intentionally under-documented fixture project
│   └── requirements.txt
└── typescript/
    ├── 01-pull-bundle.ts                 Pull and inspect a bundle
    ├── 02-install-skills.ts              Install skills into a Claude Code project
    └── 03-use-with-claude.ts             Agent SDK demo (stub — see Python)
```

## Quick Start

**Python**
```bash
cd python
pip install -r requirements.txt
export MUSHER_API_KEY="mush_..."
export ANTHROPIC_API_KEY="sk-ant-..."
python repo_docs_audit.py
```

**TypeScript**
```bash
cd typescript
npm install
export MUSHER_API_KEY="mush_..."
npm run pull-bundle
npm run install-skills
```

## What These Examples Show

1. **Pull a bundle** — Fetch the bundle from the registry and inspect its multi-file skills and agent specs
2. **Install skills** — Copy skills (SKILL.md + companion files) into `.claude/skills/` for SDK discovery
3. **Run with Agent SDK** — Claude discovers and invokes installed skills, constrained by hooks, producing structured JSON output
