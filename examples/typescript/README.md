# TypeScript Examples

These examples show how to use the [Musher TypeScript SDK](https://github.com/musher-dev/typescript-sdk) with the `repo-documentation-governance` bundle.

## Prerequisites

```bash
npm install
```

### API Keys

| Variable | Where to get it | Used by |
|----------|----------------|---------|
| `MUSHER_API_KEY` | Sign up at [hub.musher.dev](https://hub.musher.dev), then **Settings > API Keys** | All examples |

```bash
export MUSHER_API_KEY="mush_..."
```

To use your own published bundle:

```bash
export MUSHER_BUNDLE_REF="your-namespace/repo-documentation-governance:1.0.0"
```

## Examples

| File | What it demonstrates |
|------|----------------------|
| `01-pull-bundle.ts` | Pull a bundle and inspect its multi-file skills, agents, and companion files |
| `02-install-skills.ts` | Install skills (SKILL.md + companion files) into `.claude/skills/` |
| `03-use-with-claude.ts` | Agent SDK demo (stub — see Python example for the full demo) |

## Running

```bash
npm run pull-bundle
npm run install-skills
```

The Agent SDK demo is available in the Python examples at `../python/repo_docs_audit.py`.
