"""Example: Use the demo-starter bundle's skills with Claude via the Python SDK.

This example shows how to:
1. Pull the bundle and extract a skill's content
2. Use that skill as a system prompt with the Anthropic SDK
3. Run a code review using the code-reviewer agent spec

Prerequisites:
    pip install musher-sdk anthropic
    export MUSHER_API_KEY="mush_..."
    export ANTHROPIC_API_KEY="sk-ant-..."
"""

import anthropic
import musher

# Pull the demo-starter bundle
bundle = musher.pull("musher-examples/demo-starter:1.0.0")

# ── Example 1: Use a skill as a system prompt ────────────────────────────────

skill = bundle.skill("writing-commit-messages")

client = anthropic.Anthropic()

# The skill's SKILL.md content contains the full instructions for the model
skill_instructions = skill.skill_md().text()

response = client.messages.create(
    model="claude-sonnet-4-6",
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

agent = bundle.agent_spec("code-reviewer")

# The agent spec is JSON — parse it to build a system prompt from its fields
agent_config = agent.parse_json()
system_prompt = (
    f"You are a {agent_config['name']}. {agent_config['description']}\n\n"
    "Analyze code for correctness, security vulnerabilities, and best practices. "
    "For each finding, assign a severity (CRITICAL, MAJOR, MINOR, NIT) and explain "
    "the issue with a suggested fix. End with an overall verdict: Approve, "
    "Approve with suggestions, or Request changes."
)

sample_code = '''
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query).fetchone()
'''

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": f"Please review this Python function:\n\n```python{sample_code}```",
        }
    ],
)

print("── Code Review ──────────────────────────────────")
print(response.content[0].text)
