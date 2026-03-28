# TypeScript Examples

These examples show how to use the Musher TypeScript SDK with the `musher-dev/demo-starter` bundle.

## Prerequisites

```bash
npm install
export MUSHER_API_KEY="mush_..."        # From https://hub.musher.dev
export ANTHROPIC_API_KEY="sk-ant-..."  # Only needed for example 02
```

## Examples

| File | What it demonstrates |
|------|----------------------|
| `01-pull-bundle.ts` | Pull a bundle and inspect its skills, agents, and files |
| `02-use-with-claude.ts` | Use bundle skills as system prompts with the Anthropic SDK |

## Running

```bash
npm run pull-bundle
npm run use-with-claude
```
