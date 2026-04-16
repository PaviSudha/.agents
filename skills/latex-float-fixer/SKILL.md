---
name: latex-float-fixer
description: Fixes LaTeX image, table, and algorithm placement (float drifting), especially in single-column double-spaced academic templates like SPIE or Elsevier. Use this skill whenever the user complains about figures/tables dropping to the end of the document, sections printing out of order, or LaTeX failing with "Float too large" or "TeX capacity exceeded" errors because of huge tables.
---

# LaTeX Float Fixer Skill

This skill provides a systematic approach to fixing LaTeX float (figure, table, algorithm) drifting and alignment issues. Single-column, double-spaced academic templates (like the SPIE `spieman` class) naturally push large floats far from their text references, eventually causing them to pile up at the end of the document or crash the compiler.

When instructed to fix LaTeX layout or float alignment, execute the following phased heuristic approach exactly. Do not use generic tools like `sed` in bash; use your proper `replace_file_content` tools to make changes.

## Phase 1: Remove Hard Breaks
Poor layout often comes from manually inserted `\clearpage` commands that force massive white-space gaps in single-column text.
- **Action**: Search for and delete arbitrary `\clearpage` commands inserted inside the main text flow (exclude ones before references or major section breaks at the very end).

## Phase 2: Relax Constraints (General Flow)
Authors often use `[ht]` constraints universally. These are highly restrictive and force LaTeX to accumulate floats if it cannot fit them perfectly "here" or "top".
- **Action**: Change restrictive float parameters like `[ht]`, `[h]`, or `[b]` to the universally flexible `[htbp]` on standard figures and tables. This allows LaTeX to generate dedicated float pages `[p]` if an element spans too much vertical height.

## Phase 3: Strict Inline Locking (Precision Placement)
When the user requests that a specific small image, algorithm, or table appear **exactly** after a specific paragraph, do not rely on natural floating.
- **Prerequisite**: Ensure `\usepackage{float}` is included in the preamble.
- **Action**: Change the placement specifier from `[htbp]` to exactly `[H]` directly on that float environment. This forces LaTeX to render it as an inline minipage, physically locking it between the surrounding text lines.
- **CRITICAL WARNING**: **NEVER** use `[H]` on massive tables (like `tabular*` bounding boxes spanning more than 60% of a page height or `longtable` entities). Applying `[H]` to massive tables will trap the LaTeX compiler in infinite loops, crashing with a `! TeX capacity exceeded` fatal error. If you crash the compiler, immediately revert to `[htbp]`.

## Phase 4: Systematic Section Anchoring (The Ultimate Fix)
To permanently prevent any tables or figures from drifting out of their respective sub-sections without crashing the compiler layout engine, use strategic barriers.
- **Prerequisite**: Ensure `\usepackage{placeins}` is included in the preamble.
- **Action**: Insert the `\FloatBarrier` command exactly preceding the `\section` or `\subsection` commands.
- **Result**: This forces LaTeX to flush (print) all pending floats immediately before the new section starts. This guarantees that `Table X` referenced in `Section Y` will absolutely render at the bottom of the `Section Y` text block, strictly before `Section Z` begins. 

### Summary Flowchart
1. User: "Fix float drifting / Section order is totally wrong!"
2. Remove random `\clearpage` commands.
3. Loosen standard floats to `[htbp]`.
4. Add `\usepackage{placeins}` and add `\FloatBarrier` right before `\section` and `\subsection` commands to establish bounds.
5. If user needs *pixel-perfect inline ordering* for a small block, use `float` package and `[H]`. 
6. Rebuild using `pdflatex` to test logic.
