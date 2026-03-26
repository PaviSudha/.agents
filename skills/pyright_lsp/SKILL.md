---
name: pyright_lsp
description: High-speed Python code intelligence and diagnostics via Pyright.
---

# Pyright LSP Skill

Use this skill to accelerate Python development through fast diagnostics and code intelligence, mimicking an LSP (Language Server Protocol) experience.

## Capabilities

1.  **Passive Diagnostics**: Run Pyright after any major edit to catch type errors, undefined variables, and broken imports before they cause runtime failures.
2.  **Active Intelligence**: Query symbols, definitions, and type signatures across the workspace.

## Usage Instructions

### 1. Running Diagnostics

Use the `pyright_runner.py` script to get formatted diagnostics.

```bash
# Check the entire project
actenv && python .agent/skills/pyright_lsp/scripts/pyright_runner.py

# Check a specific file or directory
actenv && python .agent/skills/pyright_lsp/scripts/pyright_runner.py --path /absolute/path/to/file.py
```

### 2. Interpreting Results

The runner outputs errors and warnings in a concise format:
`[FILE] [LINE:COL] [LEVEL] [RULE] Message`

If you see errors after an edit, **fix them immediately** in the same turn to maintain a "self-correcting" workflow.

### 3. Symbol Search (Workspace)

To find where a symbol is defined or used across the workspace:

```bash
# List all occurrences of a symbol
grep_search --Query "symbol_name" --SearchPath "/absolute/path/to/project"
```
*(Note: Continue to use grep for searching while symbol index tools are developed.)*

## Best Practices

- Always run in the correct environment (ensure `actenv` has been called).
- Prefer `pyright_runner.py` over raw `pyright` as it filters noise and provides actionable paths.
- If Pyright reports a "missing import" for a newly installed package, ensure you've run `uv pip install`.
