# Python Example

This example shows how to use the [Musher Python SDK](https://github.com/musher-dev/python-sdk) and the Claude Agent SDK to consume a Musher bundle end-to-end.

## Prerequisites

- Python 3.13+

```bash
pip install -r requirements.txt
```

### API Keys

| Variable | Where to get it | Used by |
|----------|----------------|---------|
| `MUSHER_API_KEY` | Sign up at [hub.musher.dev](https://hub.musher.dev), then **Settings > API Keys** | Bundle pull & install |
| `ANTHROPIC_API_KEY` | Create at [console.anthropic.com](https://console.anthropic.com/) under **API Keys** | Agent SDK run |

```bash
export MUSHER_API_KEY="mush_..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

### Bundle Source

By default the script pulls `musher-examples/repo-documentation-governance:1.0.0`. To use your own published bundle:

```bash
export MUSHER_BUNDLE_REF="your-namespace/repo-documentation-governance:1.0.0"
```

## Running

```bash
python repo_docs_audit.py
```

The script does everything in one run:

1. **Pulls** the bundle from the Musher registry and prints its multi-file skills
2. **Installs** skills (SKILL.md + rubrics, templates, checklists) into `.claude/skills/`
3. **Runs** the Claude Agent SDK — it discovers the installed skills, audits a fixture repo, scaffolds missing docs, and returns a structured JSON report

## Output

- `out/repo_docs_report.json` — Structured report (score, gaps, files created, recommendations)
- `out/tool_calls.jsonl` — Log of every tool call the agent made

## What to Look For

- Skills are loaded from `.claude/skills/` — including companion files (rubrics, templates)
- Claude invokes them autonomously through the `Skill` tool
- Hooks constrain where the agent can write (fixture repo only)
- The final result is JSON you could feed into CI, a dashboard, or another service
