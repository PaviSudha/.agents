---
name: latex_lint
description: Fast LaTeX diagnostics using chktex and lacheck for catching style and structural errors.
---

# LaTeX Lint Skill

Use this skill to catch LaTeX errors and style issues instantly after every edit, similar to how `pyright_lsp` works for Python.

**Performance:** Finds all issues in **0.06 seconds** with exact fix suggestions — compared to 6+ grep commands that miss critical bugs like mismatched `\begin/\end` pairs.

## Tools Used

| Tool | Purpose |
|------|---------|
| `chktex` | Style issues: wrong quotes, missing `~` before `\cite`, bad dashes, `...` vs `\ldots` |
| `lacheck` | Structural issues: unmatched `\begin/\end`, unclosed braces, double words |

## Usage

### Quick Check (Single File)

```bash
python /run/media/kar/Turbo/.agent/skills/latex_lint/scripts/latex_linter.py --file /path/to/file.tex
```

### Full Project Check

```bash
python /run/media/kar/Turbo/.agent/skills/latex_lint/scripts/latex_linter.py --dir /path/to/project/
```

### When to Run

- **After every major LaTeX edit** to catch broken environments, missing braces, or bad citations.
- **Before compiling** to avoid wasting time on failed builds.
- **When reviewing LaTeX files** to find style inconsistencies.

## What It Catches

### Style Errors (chktex)

| Warning Code | Issue | Fix |
|-------------|-------|-----|
| 11 | Wrong quotes `"text"` | Use ` ``text'' ` |
| 2 | Missing `~` before `\cite` or `\ref` | Write `~\cite{key}` |
| 11 | `...` used instead of `\ldots` | Replace with `\ldots` |
| 8 | Wrong dash length (`10-20`) | Use `10--20` for ranges, `---` for em dash |
| 12 | Intersentence spacing after period | Add `\ ` or `~` after abbreviations like `Dr.` |
| 1 | Command terminated with space | Use `{}` after command: `\LaTeX{}` |
| 36 | Mixed use of `\bfseries` and `\textbf` | Stick to one style |

### Structural Errors (lacheck)

| Issue | Example |
|-------|---------|
| Unmatched `\begin/\end` | `\begin{itemize}...\end{enumerate}` — wrong closing |
| Missing closing brace | `\textbf{text` — no `}` |
| Double words | `the the method` — repeated word |
| Dots not ellipsis | `results...` — should be `\ldots` |
| Missing `\ ` after period | `method. The` inside sentence |

### Things grep CANNOT catch (but this skill does)

- `\begin{itemize}` closed by `\end{enumerate}` — grep counts both as "2 and 2" and says OK
- Missing `~` before `\cite` — grep finds `\cite` lines but can't tell if `~` is present
- Wrong dash length — grep can't distinguish `10-20` (wrong) from `-1` (valid math)

## Suppressing False Positives

If chktex flags something intentional, suppress it for that line:

```latex
This is "intentional" % chktex 18
```

The number after `chktex` is the warning code from the table above.

## Best Practices

1. Fix **structural errors** (lacheck) first — these cause build failures.
2. Fix **style errors** (chktex) second — these affect quality.
3. Run this skill **before every `pdflatex` compilation** to save time.
4. When editing multiple `.tex` files, use `--dir` to sweep the entire project at once.
