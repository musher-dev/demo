/**
 * Use the demo-starter bundle's skills with Claude via the Anthropic SDK.
 *
 * This example shows how to:
 * 1. Pull the bundle and extract a skill's content
 * 2. Use that skill as a system prompt with the Anthropic SDK
 * 3. Run a structured code review using the code-reviewer agent spec
 *
 * Prerequisites:
 *   export MUSHER_API_KEY="mush_..."
 *   export ANTHROPIC_API_KEY="sk-ant-..."
 *
 * Run:
 *   npx tsx 03-use-with-claude.ts
 */

import Anthropic from "@anthropic-ai/sdk";
import { pull } from "@musher-dev/musher-sdk";

const client = new Anthropic();
const bundle = await pull("musher-examples/demo-starter:1.0.0");

// ── Example 1: Use a skill as a system prompt ────────────────────────────────

const commitSkill = bundle.skill("writing-commit-messages");
if (!commitSkill) throw new Error("Skill 'writing-commit-messages' not found");

const commitResponse = await client.messages.create({
	model: "claude-sonnet-4-6",
	max_tokens: 512,
	system: commitSkill.definition()!.text(),
	messages: [
		{
			role: "user",
			content:
				"I added input validation to the user registration endpoint. " +
				"It now rejects emails longer than 254 characters and passwords " +
				"shorter than 8 characters, returning a 422 with field-level errors.",
		},
	],
});

console.log("── Commit Message ───────────────────────────────");
console.log(
	commitResponse.content[0].type === "text" ? commitResponse.content[0].text : "",
);
console.log();

// ── Example 2: Use the code-reviewer agent spec ───────────────────────────────

const reviewerAgent = bundle.agentSpec("code-reviewer");
if (!reviewerAgent) throw new Error("Agent spec 'code-reviewer' not found");

const sampleCode = `
function getUser(userId) {
  const query = \`SELECT * FROM users WHERE id = \${userId}\`;
  return db.execute(query).then(r => r.rows[0]);
}
`;

const reviewResponse = await client.messages.create({
	model: "claude-sonnet-4-6",
	max_tokens: 1024,
	system: reviewerAgent.content(),
	messages: [
		{
			role: "user",
			content: `Please review this JavaScript function:\n\n\`\`\`javascript${sampleCode}\`\`\``,
		},
	],
});

console.log("── Code Review ──────────────────────────────────");
console.log(
	reviewResponse.content[0].type === "text" ? reviewResponse.content[0].text : "",
);
