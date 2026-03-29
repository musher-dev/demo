# Python Examples

These examples show how to use the Musher Python SDK with the `musher-dev/demo-starter` bundle.

## Prerequisites

```bash
pip install musher anthropic
export MUSHER_API_KEY="mush_..."        # From https://hub.musher.dev
export ANTHROPIC_API_KEY="sk-ant-..."  # Only needed for example 03
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
