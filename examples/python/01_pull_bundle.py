"""Example: Pull the demo-starter bundle and inspect its contents."""

import musher

# Credentials are auto-discovered from the MUSHER_API_KEY environment variable,
# the OS keyring, or a credential file (~/.config/mush/credentials.yaml).
# To set credentials explicitly: musher.configure(token="mush_...")

bundle = musher.pull("musher-dev/demo-starter:1.0.0")

print(f"Bundle: {bundle.manifest.name} v{bundle.manifest.version}")
print(f"Description: {bundle.manifest.description}")
print()

# List all files in the bundle
print(f"Files ({len(list(bundle.files()))}):")
for fh in bundle.files():
    print(f"  {fh.logical_path}  ({fh.media_type or 'unknown'})")
print()

# List available skills
print(f"Skills ({len(bundle.skills())}):")
for skill in bundle.skills():
    print(f"  {skill.name}")
    # Read the SKILL.md content
    content = skill.text()
    # Extract the description from the frontmatter (first 120 chars of body)
    lines = content.splitlines()
    for line in lines:
        if line.startswith("description:"):
            desc = line.replace("description:", "").strip()
            print(f"    → {desc[:100]}...")
            break
print()

# List available agents
print(f"Agents ({len(bundle.agents())}):")
for agent in bundle.agents():
    print(f"  {agent.name}")
print()

# Access a specific skill by name
skill = bundle.skill("summarize-changes")
if skill:
    print(f"Skill content preview ({skill.name}):")
    print(skill.text()[:300])
    print("...")
