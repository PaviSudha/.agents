---
name: pdf-struct-analyzer
description: Converts PDF files to Markdown and extracts a hierarchical tree structure to aid in structural analysis and identifying misalignment.
---

# PDF Structure Analyzer

This skill helps you understand the deep structure of a PDF document by converting it to Markdown and parsing its headings into a visual tree. This is useful for:
1. Identifying missing or misaligned sections after conversion.
2. Quickly navigating long documents.
3. Analyzing the hierarchical organization of technical papers.

## Workflow

1.  **Analyze Structure**: Run the provided analysis script on a target PDF.
2.  **Inspect Tree**: Review the generated tree structure (nodes and leaves).
3.  **Cross-Reference**: Compare the tree with the original PDF to find inconsistencies.

## Scripts

### `scripts/analyze_pdf_structure.py`

This script automates the PDF-to-MD conversion and tree generation.

**Usage**:
```bash
python .agents/skills/pdf-struct-analyzer/scripts/analyze_pdf_structure.py path/to/document.pdf
```

**What it does**:
- Converts the PDF to `.md` using `markitdown`.
- Extracts Markdown headers (`#`, `##`, etc.).
- Extracts numbered sections (e.g., `1`, `1.1`, `1.1.1`).
- Identifies key sub-nodes like "Datasets:", "Implementation Details:", etc.
- Filters out bibliography/reference lists to keep the tree clean.
- Outputs a visual tree representation.

## Tips for Misalignment Analysis

- **Check for Gaps**: If the tree jumps from `1.1` to `1.3`, a section was likely missed or incorrectly parsed.
- **Check for Noise**: If random text appears as a node (e.g., page numbers or running headers), the alignment is likely off.
- **Table Data**: Remember that `markitdown` may lose table structure; use the `pdf_search` skill if the tree shows a table but the Markdown content is empty.
