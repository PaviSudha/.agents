---
name: codespeak-workflow
description: Spec-driven development workflow inspired by CodeSpeak. Use when the user asks you to "build", "implement", or "update" a feature based on a .cs.md spec file, or when they want to maintain a project solely through markdown specifications rather than writing raw code.
---

# CodeSpeak Workflow

This skill transforms the agent into a Spec-Driven Development engine. In this workflow, the user maintains small, plain-text Markdown specifications (`.cs.md` files) as the source of truth, and the agent acts as the compiler—generating, updating, and maintaining the underlying source code to perfectly match the specifications.

## Core Philosophy

- **Specs are the Source of Truth:** Code should always be a reflection of the `.cs.md` file. 
- **No Direct Code Edits (Ideally):** If the user wants a logic change, they should modify the Spec, and ask you to "rebuild" the code. If the user asks you to change the code directly during this workflow, politely remind them to update the Spec first to ensure the documentation doesn't drift from reality.

## Workflow Execution Steps

When triggered by a user request to "build" a spec (e.g., "Build the auth module based on `auth.cs.md`"):

1. **Read the Spec:** 
   Use `view_file` to carefully read the target `.cs.md` file. Pay close attention to:
   - Required inputs and outputs
   - Edge cases and error handling requirements
   - Output structure or formatting rules

2. **Understand the Context:**
   If the spec is meant to integrate with an existing project, use `list_dir` and `view_file` to inspect the surrounding files to ensure your generated code uses the correct imports and project architecture.

3. **Generate/Update the Code:**
   - Follow strict testing and validation before you generate the implementation.
   - For new files: Use `write_to_file` to create the implementation strictly adhering to the Spec.
   - For existing files: Use `multi_replace_file_content` to surgically update the implementation to match the new version of the Spec.

4. **Verify Constraints:**
   Before returning control to the user, ensure you did not hallucinate features. The code must be a 1:1 translation of the specification.

## Prompting the User
If the user gives you a very vague instruction without a Spec file while this skill is active, remind them:
*"Please create a `.cs.md` file outlining the exact requirements, inputs, and edge cases, and I will build the implementation for you."*
