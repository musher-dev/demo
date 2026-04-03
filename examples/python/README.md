# Python Examples

These examples show how to use the [Musher Python SDK](https://github.com/musher-dev/python-sdk) with the `musher-examples/demo-starter` bundle.

## Prerequisites

- Python 3.13+

```bash
pip install musher-sdk anthropic
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
| `01_pull_bundle.py` | Pull a bundle and inspect its skills, agents, and files |
| `02_install_skills.py` | Install skills into a Claude Code project directory |
| `03_use_with_claude.py` | Use bundle skills as system prompts with the Anthropic API |

## Running

```bash
python 01_pull_bundle.py
python 02_install_skills.py
python 03_use_with_claude.py
```
