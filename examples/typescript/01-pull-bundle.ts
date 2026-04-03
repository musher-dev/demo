/**
 * Pull the repo-documentation-governance bundle and inspect its contents.
 *
 * Prerequisites:
 *   export MUSHER_API_KEY="mush_..."
 *
 * To use your own published bundle, set:
 *   export MUSHER_BUNDLE_REF="your-namespace/repo-documentation-governance:1.0.0"
 *
 * Run:
 *   npx tsx 01-pull-bundle.ts
 */

import { pull } from "@musher-dev/musher-sdk";

const bundleRef =
	process.env.MUSHER_BUNDLE_REF ?? "musher-examples/repo-documentation-governance:1.0.0";

const bundle = await pull(bundleRef);

console.log(`Bundle: ${bundle.ref.toBaseRef()} v${bundle.version}`);
console.log();

// List all files — notice multi-file skills ship more than just SKILL.md
const files = bundle.files();
console.log(`Files (${files.length}):`);
for (const file of files) {
	console.log(`  ${file.logicalPath}  (${file.assetType}, ${file.sizeBytes} bytes)`);
}
console.log();

// List available skills
const skills = bundle.skills();
console.log(`Skills (${skills.length}):`);
for (const skill of skills) {
	console.log(`  ${skill.name}`);
}
console.log();

// List available agent specs
const agentSpecs = bundle.agentSpecs();
console.log(`Agent Specs (${agentSpecs.length}):`);
for (const agentSpec of agentSpecs) {
	console.log(`  ${agentSpec.name}`);
}
console.log();

// Access a specific skill by name
const skill = bundle.skill("auditing-repo-documentation");
if (skill) {
	const preview = skill.definition()!.text().slice(0, 300);
	console.log(`Skill content preview (${skill.name}):`);
	console.log(preview);
	console.log("...");
}
