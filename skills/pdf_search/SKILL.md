---
name: pdf_search
description: "Instructions for searching text within PDF files using ripgrep-all (rga)"
---

# PDF Content Search Skill

This skill allows you to search for specific text, citations, or keywords inside PDF files located in a directory.

## 📂 Primary Paper Directories

Always search in these three directories for backing research:

1.  `/home/kar/Syncthing/reff/papers current used`
2.  `/home/kar/Syncthing/reff/imgAndImgs`
3.  `/home/kar/Syncthing/papers with keys`

**⚠️ IMPORTANT PATH NOTE:** These paths may contain spaces. **ALWAYS** quote your paths in commands.
Example: `rga "query" "/home/kar/Syncthing/reff/papers current used"`

## 🔑 Citation Rule: Filename = BibKey

For all papers in the directories above:

- The **Filename** (without extension) is **EXACTLY** the **BibTeX Key** in `references.bib`.
- **Example:** If you find a match in `mohamed2024realtime.pdf`, the citation key is `\cite{mohamed2024realtime}`.
- **Action:** You generally DO NOT need to check `references.bib` for the key. Trust the filename.

## 🛠️ Available Tools (Choose the Right One)

| Tool | Speed | Best For |
|------|-------|----------|
| `rga` | **0.008s** | Keyword search with page numbers — fastest |
| `pdftotext` | 0.013s/page | Reading full pages, extracting sections |
| `pdftotext + grep` | 0.07s | Search with line numbers across full text |
| `pdfinfo` | **0.009s** | Quick metadata: page count, author, date |

### When to use which:
- **"Find where X is mentioned"** → Use `rga` (fastest)
- **"Read page 7 of this paper"** → Use `pdftotext -f 7 -l 7`
- **"Extract the full paper as text"** → Use `pdftotext paper.pdf /tmp/output.txt`
- **"How many pages is this paper?"** → Use `pdfinfo`

## 🔍 Search Workflow

**MANDATORY STRATEGY: Wide First -> Narrow Second**

Do **NOT** start by guessing a specific PDF. Search all directories first.

### Step 1: Broad Search (Wide Net)

```bash
rga -i "search phrase" "/home/kar/Syncthing/reff/papers current used" | head -n 20
```

### Step 2: Analyze & Select

Identify which papers contain the most relevant matches.

### Step 3: Narrow Focus (Deep Dive)

```bash
rga -i "specific detail" "/home/kar/Syncthing/reff/papers current used/author2023topic.pdf"
```

### Step 4: Read Full Context (NEW — use pdftotext)

When you need to **read an entire section** (not just search), extract the specific page:

```bash
# Read page 7 of a paper
pdftotext -f 7 -l 7 "paper.pdf" -

# Read pages 3 to 5
pdftotext -f 3 -l 5 "paper.pdf" -

# Extract full paper to file for repeated use
pdftotext "paper.pdf" /tmp/paper_full.txt
```

## 🚀 Advanced Techniques

### 1. Context Awareness (Surrounding lines)

```bash
rga -i -C 3 "fps" "/home/kar/Syncthing/reff/papers current used"
```

### 2. Smart "OR" Search (Regex)

```bash
rga -i "(fps|real-time|speed)" "/home/kar/Syncthing/reff/papers current used"
```

### 3. "AND" Logic (Co-occurrence)

```bash
rga -l -i "capacity" "/home/kar/Syncthing/reff/papers current used" | xargs rga -l -i "robustness"
```

### 4. Count Matches Per File (Ranking papers by relevance)

```bash
rga -i -c "steganography" "/home/kar/Syncthing/reff/papers current used" | sort -t: -k2 -nr | head -10
```

### 5. Quick Paper Info

```bash
pdfinfo "paper.pdf"
# Output: Pages, Author, Creation Date, File Size
```

### 6. Extract Text with Layout Preservation

```bash
# Preserve column layout (useful for two-column papers)
pdftotext -layout "paper.pdf" -
```

## Common Usage Examples

```bash
# Basic keyword search
rga -i "real-time efficiency" "/home/kar/Syncthing/reff/papers current used"

# Search for metrics
rga -i "fps" "/home/kar/Syncthing/reff/papers current used"
rga -i "file size" "/home/kar/Syncthing/reff/imgAndImgs"

# Read a specific page
pdftotext -f 3 -l 3 "/home/kar/Syncthing/reff/papers current used/smith2024.pdf" -

# Get paper metadata
pdfinfo "/home/kar/Syncthing/reff/papers current used/smith2024.pdf"
```

## 📑 Paper Structure Navigation

### Extract Section Headers (Table of Contents)

Instantly see the structure of any paper:

```bash
pdftotext "paper.pdf" - | grep -n "^[0-9]\."
```

Example output:
```
59:1. Introduction
100:2. Statistical modeling framework
390:3. The payload allocation game
565:4. Proof of Theorem 1
```

Use the line numbers to jump to specific sections by estimating the page.

### Extract References / Bibliography

```bash
pdftotext "paper.pdf" - | grep -n "^\[" | head -20
```

This lists all `[1] Author...` style references with line numbers.

### Find Figure and Table Captions

```bash
pdftotext "paper.pdf" - | grep -n -i "^Figure\|^Table"
```

Example output:
```
986:Figure 1: The payoff surface...
1100:Figure 2: Difference between predicted theoretical NE...
1163:Figure 3: PE of predicted theoretical NE...
```

## ⚡ Decision Flowchart: Which Tool to Use

```
What do you need?
│
├── "Find where X is mentioned" ──────► rga -i "X" paper.pdf
│
├── "Read a full section/page" ───────► pdftotext -f PAGE -l PAGE paper.pdf -
│
├── "How many pages / who wrote it" ──► pdfinfo paper.pdf
│
├── "List section headers" ───────────► pdftotext paper.pdf - | grep -n "^[0-9]\."
│
├── "Find all figures/tables" ────────► pdftotext paper.pdf - | grep -n -i "^Figure\|^Table"
│
├── "List all references" ────────────► pdftotext paper.pdf - | grep -n "^\["
│
├── "Rank papers by relevance" ───────► rga -i -c "topic" dir/ | sort -t: -k2 -nr
│
└── "Find papers with BOTH X and Y" ──► rga -l -i "X" dir/ | xargs rga -l -i "Y"
```

