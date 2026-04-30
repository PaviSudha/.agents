---
name: update-paper-prompts
description: Synchronize and update research paper extraction prompts (prompt.md and supplemental_prompt.md). Use when adding metrics, changing classifications, or updating venue types to ensure consistency between initial and supplemental extraction passes.
---

# Update Paper Prompts

This skill ensures that extraction requirements for research papers are consistently applied across both the **Initial Pass** (`prompt.md`) and the **Supplemental Pass** (`supplemental_prompt.md`).

## Core Concepts

- **Initial Pass (`prompt.md`)**: Used for the first-time extraction of a paper. Contains the full 13-section JSON schema.
- **Supplemental Pass (`supplemental_prompt.md`)**: Used to "patch" existing records with new or missed metrics. Contains a subset of the JSON schema (usually the `supplemental_verification` block).

## Consistency Checklists

When updating a prompt, you MUST ensure:

### 1. Instruction Consistency
- Update the **Role** and **Task** descriptions in both files if the domain scope changes.
- Ensure "Supplemental Verification instructions" in `prompt.md` match the "Task" instructions in `supplemental_prompt.md`.

### 2. Schema Consistency
- Field names (keys) must be identical in both files.
- Options in `_options` keys must match exactly.
- Taxonomy (e.g., "GT + Blind") must be consistent.

### 3. JSON Validity
- Use `extract_papers.py` or a dedicated script to ensure the JSON blocks in the markdown files are parseable.

## Common Taxonomy Reference

Always use the established taxonomy for `paper_classification`:
- "GT + Blind"
- "GT + Blind + Steganalysis"
- "GT + Semi-blind"
- "GT + Semi-blind + Steganalysis"
- "GT + Non-blind"
- "GT + Non-blind + Steganalysis"
- "Other"

## Workflow

1. **Modify `prompt.md` first**: Add the new fields to the relevant section (usually `section_13_supplemental_verification`) and add corresponding instructions at the top.
2. **Sync to `supplemental_prompt.md`**: Copy the new JSON structure and specific task instructions to the supplemental file.
3. **Validate**: Ensure both files remain valid markdown with single, parseable JSON blocks.
