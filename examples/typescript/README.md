# TypeScript Examples

These examples show how to use the [Musher TypeScript SDK](https://github.com/musher-dev/typescript-sdk) with the `musher-examples/demo-starter` bundle.

## Prerequisites

```bash
npm install
```

### API Keys

| Variable | Where to get it | Used by |
|----------|----------------|---------|
| `MUSHER_API_KEY` | Sign up at [hub.musher.dev](https://hub.musher.dev), then **Settings > API Keys** | All examples |
| `ANTHROPIC_API_KEY` | Create at [console.anthropic.com](https://console.anthropic.com/) under **API Keys** | Example 03 only |

```bash
export MUSHER_API_KEY="mush_..."
export ANTHROPIC_API_KEY="sk-ant-..."   # Only needed for example 03
```

## Examples

| File | What it demonstrates |
|------|----------------------|
| `01-pull-bundle.ts` | Pull a bundle and inspect its skills, agent specs, and files |
| `02-install-skills.ts` | Install skills into a Claude Code project directory |
| `03-use-with-claude.ts` | Use bundle skills as system prompts with the Anthropic SDK |

## Running

```bash
npm run pull-bundle
npm run install-skills
npm run use-with-claude
```
