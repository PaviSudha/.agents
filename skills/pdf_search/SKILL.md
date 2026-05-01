---
name: pdf_search
description: "High-precision PDF search and structural extraction using rga and poppler"
---

# PDF Content Search Skill

This skill provides a high-performance workflow for searching, navigating, and **accurately extracting** content from PDF files.

## 📂 Primary Paper Directories

Always search in these three directories for backing research:

1.  current directory
2.  `/home/kar/Syncthing/papers with keys`


**⚠️ IMPORTANT PATH NOTE:** These paths may contain spaces. **ALWAYS** quote your paths.

## 🔑 Citation Rule: Filename = BibKey

- The **Filename** (without extension) is **EXACTLY** the **BibTeX Key** in `references.bib`.
- **Action:** Trust the filename. You generally DO NOT need to check `references.bib`.
- **Example:** `mohamed2024realtime.pdf` -> `\cite{mohamed2024realtime}`.

## ⚡ Performance (Automatic Caching)

`rga` automatically caches extracted PDF text at `~/.cache/ripgrep-all/cache.sqlite3`.

| State | Time (234 PDFs) | Notes |
|-------|-----------------|-------|
| Cold cache | ~5s | First search after cache clear |
| Warm cache | **~0.2s** | All subsequent searches |
| Parallel xargs | ~0.3s | Slower than cached `rga` |

**Action:** Just use `rga` normally. The cache provides automatic **27x speedup** on repeated queries. No manual caching or parallelization needed.

## 🚀 High-Speed Search (rga)

Use `rga` for rapid discovery and identifying page numbers.

| Goal | Command |
|------|---------|
| **Broad Search** | `rga -i "search phrase" "/path/to/directory"` |
| **Rank Papers** | `rga -i -c "topic" dir/ \| sort -t: -k2 -nr` |
| **OR Search** | `rga -i -e "term1" -e "term2" "file.pdf"` |
| **AND Search** | `rga -l "term1" dir/ \| xargs -I {} rga -l "term2" "{}"` |
| **Batch Parallel** | `find dir/ -name "*.pdf" -print0 \| xargs -0 -P 4 -I {} rga -i "topic" "{}"` *Note: Slower than cached `rga` for repeated searches* |

## 🎯 Accurate Extraction (The Hybrid Workflow)

Raw extraction from `rga` or `pdftotext` often interleaves columns in two-column papers, making text unreadable. **Always use this hybrid approach for reading:**

### Step 1: Find the Page (rga)
```bash
rga -i "specific keyword" "paper.pdf"
# Note the Page Number (e.g., Page 3)
```

### Step 2: Extract with Layout (-layout)
Use `-layout` to preserve columns and read the text in its natural flow.
```bash
# Extract Page 3 with column preservation
pdftotext -layout -f 3 -l 3 "paper.pdf" -
```

## 📑 Structured Data Extraction

To extract specific sections like Tables, Figures, or References:

| Target | Pattern / Strategy |
|--------|--------------------|
| **Tables** | `rga -i -A 30 "Table [0-9VI]+" "file.pdf"` |
| **Figures** | `rga -i -A 5 "Figure [0-9]+" "file.pdf"` |
| **References** | `rga -i -A 100 "References" "file.pdf"` |
| **Sections** | `rga -i "^[0-9]\. [A-Z]" "file.pdf"` |

## ⚡ Power-User Techniques

### 1. High-Recall Research (Fuzzy-ish)
Search for multiple variations of a technical term in one go:
```bash
rga -i -e "bitrate" -e "bit-rate" -e "bps" "paper.pdf"
```

### 2. Contextual Deep Dive
When you find a hit, grab 5 lines of context before and after to understand the surrounding logic:
```bash
rga -i -C 5 "FPS" "paper.pdf"
```

### 3. Metadata Snippet
Quickly check the paper's scope and length:
```bash
pdfinfo "paper.pdf"
```

## 🛠️ Summary Task Map

```bash
# To identify papers for a topic
rga -l -i "steganography" "/home/kar/Syncthing/reff/papers current used"

# To read a specific section in a 2-column paper
rga -i "Introduction" "paper.pdf" # Find page
pdftotext -layout -f PAGE -l PAGE "paper.pdf" - # Read page
```
