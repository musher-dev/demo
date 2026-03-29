"""Example: Use the demo-starter bundle's skills with Claude via the Python SDK.

This example shows how to:
1. Pull the bundle and extract a skill's content
2. Use that skill as a system prompt with the Anthropic SDK
3. Run a code review using the code-reviewer agent spec

Prerequisites:
    pip install musher anthropic
    export MUSHER_API_KEY="mush_..."
    export ANTHROPIC_API_KEY="sk-ant-..."
"""

import anthropic
import musher

# Pull the demo-starter bundle
bundle = musher.pull("musher-dev/demo-starter:1.0.0")

# ── Example 1: Use a skill as a system prompt ────────────────────────────────

skill = bundle.skill("write-commit-message")
assert skill is not None, "Skill 'write-commit-message' not found in bundle"

client = anthropic.Anthropic()

# The skill's SKILL.md content contains the full instructions for the model
skill_instructions = skill.text()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=512,
    system=skill_instructions,
    messages=[
        {
            "role": "user",
            "content": (
                "I added input validation to the user registration endpoint. "
                "It now rejects emails longer than 254 characters and passwords "
                "shorter than 8 characters, returning a 422 with field-level errors."
            ),
        }
    ],
)

print("── Commit Message ───────────────────────────────")
print(response.content[0].text)
print()

# ── Example 2: Use the code-reviewer agent spec ───────────────────────────────

agent = bundle.agent("code-reviewer")
assert agent is not None, "Agent 'code-reviewer' not found in bundle"

agent_spec = agent.text()

sample_code = '''
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query).fetchone()
'''

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system=agent_spec,
    messages=[
        {
            "role": "user",
            "content": f"Please review this Python function:\n\n```python{sample_code}```",
        }
    ],
)

print("── Code Review ──────────────────────────────────")
print(response.content[0].text)
