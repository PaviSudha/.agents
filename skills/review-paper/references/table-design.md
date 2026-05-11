# Table Design — Journal-Standard Academic Tables

Derived from published exemplars:
- Salo et al. (2024) *European Journal of Operational Research*
- Zhao et al. (2025) *Expert Systems with Applications*
- Elsevier Author Services, "How to Use Tables and Figures effectively in Research Papers" (<https://scientific-publishing.webshop.elsevier.com/manuscript-preparation/use-tables-and-figures-effectively-research-papers/>)
- Fonnes and Rosenberg (2025) *Journal of Surgical Research*, "Researcher's Guide for the Preparation of Tables" (`1-s2.0-S0022480425001556-main.pdf`)

---

## STEP 0: ELSEVIER TABLE-DISPLAY GATE

Before generating, redesigning, or formatting a table, produce a short table specification. If information is missing, infer conservatively and ask only for details that materially affect the table.

```text
Table message: [one sentence; what the reader should learn]
Table purpose: [describe / compare / map features / report outcomes / support future agenda]
Manuscript placement: [Introduction / Methodology / Results / Discussion / Appendix]
Data scope: [sample, period, source, inclusion rule]
Display choice: [table / figure / prose / appendix]
Redundancy risk: [what prose or figure might duplicate this table]
Structure: [single table / panels / grouped rows / sub-columns]
Data-ink plan: [what is essential data vs. nonessential formatting]
Caption claim: [specific caption title above the table]
Note needs: [abbreviations, symbols, scope caveats, statistical notes]
Journal constraints: [target journal rules if known]
```

Reject or redesign any table that fails this gate:

- **Not self-explanatory:** A reader should understand the table's purpose, scope, variables, abbreviations, and symbols without reading several surrounding paragraphs.
- **Redundant with prose or figure:** Do not repeat exact values in text and table unless a few values are being highlighted. Let the text interpret; let the table document.
- **Inconsistent with manuscript text:** Counts, percentages, labels, row names, and definitions must match the text, figures, and supplementary material.
- **Vague caption:** The caption above the table must state what is being compared or summarized and in what context.
- **Poor relevance:** Remove columns, rows, precision, and notes that do not support the table message.
- **Cluttered layout:** If a table is dense, combine repeated structures, split into panels, group categories, or move full detail to an appendix.
- **Missing journal fit:** Follow the target journal's table numbering, caption, footnote, file-format, and supplementary-table instructions when known.
- **Excess non-data-ink:** Remove visible grids, vertical rules, decorative shading, unnecessary boldface, repeated symbols, and over-precise decimals unless the journal explicitly requires them.

## ELSEVIER MANUSCRIPT PRINCIPLES FOR TABLES

- Use tables as concise display items that complement the research text.
- Expect readers, reviewers, and editors to scan tables before reading the full manuscript; make tables organized and self-contained.
- Combine repetitive tables when they share the same structure or message.
- Divide large data into categories, panels, columns, or sub-columns so the table has visible structure.
- Keep only relevant data and preserve enough spacing; a crowded table is a design failure, not a sign of rigor.
- Use informative captions above the table, clear column heads, appropriate labels, and notes that define abbreviations and symbols.
- Ensure all values in the table match values mentioned in the manuscript body.
- If the same message is clearer as a figure, recommend a figure instead of forcing a table.
- Treat table preparation as five steps: define purpose, apply a universal low-noise layout, select variables according to table role, simplify by categorizing/standardizing/reducing, and make numbers/decimals readable.

## TABLE PREPARATION MODEL FROM `1-s2.0-S0022480425001556-main.pdf`

Use this model when transforming extracted data into a manuscript table:

1. **Purpose first:** Decide what the table does for the reader. Purpose controls which rows, columns, precision, labels, and notes are worth keeping.
2. **Universal layout:** Keep the data visually dominant by minimizing non-data-ink. Use a few horizontal rules, clear white space, and consistent typography.
3. **Table role:** Select data according to whether the table is Table 1/descriptive, an outcome/results table, a feature map, or a supplement.
4. **Simplify:** Categorize related variables, standardize terms and units, and reduce sparse or nonessential variables.
5. **Readable numbers:** Use only meaningful decimals and report proportions in a way that preserves denominators.

### Gestalt-Informed Layout Rules

- **Figure-ground:** Make data stand out from the background; avoid heavy grids and decorative shading.
- **Closure:** Use only enough horizontal rules to mark the table boundary and header/body separation.
- **Proximity:** Use spacing and grouped columns/sub-columns to show related variables.
- **Good continuation:** Keep vertical alignment clean so readers can follow each column from header to data.
- **Similarity:** Use consistent font style, size, symbols, decimal precision, and group labels.
- **Symmetry:** Avoid sparse rows/columns and irregular gaps; group rare categories as `Other` when that better supports readability, then explain the grouping in the note.

### Universal Layout Defaults

- Use top rule, header rule, and bottom rule as the default; avoid vertical rules and full grids.
- Avoid row shading by default; if a very large table needs row guidance, use it cautiously and only when it improves readability.
- Use bold text only for header rows or essential hierarchy, not for entire rows.
- Use real table structure for subcategories, such as split cells, grouped rows, or sub-columns. Do not create indentation with spaces.
- Align text left and numbers right; consider right-aligning the rightmost column to create a clean visual edge.
- Prefer white space over borders for grouping.
- Keep symbols such as `%`, units, and currencies in headers where possible instead of repeating them in every cell.
- Use descriptive group names consistently across text, tables, and figures; avoid opaque labels such as Group A/B unless the manuscript defines them immediately.

---

## STEP 1: DIAGNOSE WHAT THE USER HAS GIVEN YOU

When a user provides raw data, a list, or an informal table, **do not immediately format it**. First diagnose:

### Diagnostic Questions (answer these before designing)

1. **What is the purpose of this table?**
   - Comparing this paper to prior papers → Type A (Literature Comparison)
   - Describing the sample/dataset → Type B (Bibliometric/Descriptive)
   - Showing which papers include which features → Type C (Feature Mapping)
   - Comparing methods/models across studies → Type D (Method Comparison)
   - Listing future research directions → Type E (Research Agenda)
   - Showing numerical results/performance → Type F (Results/Performance)

2. **How many rows and columns?**
   - ≤ 5 columns: standard single table
   - 6–9 columns: consider splitting into panels (Panel A / Panel B) or rotating to landscape
   - ≥ 10 columns: almost certainly needs splitting or a different representation
   - Very wide tables: avoid landscape in the main manuscript when possible; split, summarize, or move extraction-level detail to supplement

3. **What is the data type?**
   - Binary presence/absence → use √ / × symbols
   - Categorical labels → text cells, left-aligned
   - Numerical values → right-aligned, consistent decimal places
   - Long text entries → consider abbreviating with a note key
   - Proportions → report numerator/denominator or make the denominator explicit in the table/note

4. **What is the relationship being shown?**
   - Ranking → sort the rows by the ranking criterion
   - Categories → group rows by category with merged left column
   - Chronological → sort by year
   - Frequency → sort descending by count

5. **Is a table the right display item?**
   - Exact lookup or many dimensions → table
   - Trend, distribution, relationship, or visual pattern → figure
   - One or two key values only → prose
   - Long audit trail or exhaustive extraction → appendix/supplementary table

6. **Will the manuscript repeat the same values?**
   - If yes, keep the detailed values in the table and rewrite the prose as interpretation.
   - If no, make sure the table is referenced before it appears and the surrounding paragraph explains its purpose.

7. **Is this Table 1 or an outcome table?**
   - Table 1 / descriptive: show sample or included-study characteristics.
   - Table 2+ / outcomes: group by primary endpoints, secondary endpoints, analysis type, or outcome domain.
   - Literature reviews: choose between one row per included study and a summary table; use a summary table when one-row-per-study becomes long and hard to scan.

8. **Can the data be simplified without hiding the message?**
   - Categorize related variables.
   - Standardize units, terminology, spelling, and group labels.
   - Reduce sparse or nonessential variables; place exhaustive extraction in supplementary material.
   - Reduce decimals to the meaningful precision needed for the table's purpose.

---

## STEP 2: CLASSIFY AND RECOMMEND

After diagnosing, tell the user:
- Which table type fits their data
- Whether a table is better than a figure, prose, or appendix
- How many columns to use
- How to sort/group rows
- Whether to split into panels
- What redundant rows/columns should be removed
- What abbreviation notes are needed
- What manuscript sentence should introduce the table

---

## ANATOMY OF EVERY JOURNAL TABLE

```
Table N
Caption — one specific sentence above the table
──────────────────────────────────────────────────────
Col Header 1    Col Header 2    Col Header 3    Col 4
──────────────────────────────────────────────────────
Row 1 label     data            data            data
Row 2 label     data            data            data
[Category row — bold/italic if grouping rows]
Row 3 label     data            data            data
──────────────────────────────────────────────────────
Note: Abbreviations spelled out. Symbol key. Any
      important qualifier about the data.
```

**Ironclad rules for every table:**
- Caption **above**, Note **below**
- Horizontal rules **only** — top rule, header rule, bottom rule. Zero vertical lines
- Number sequentially: Table 1, Table 2 … (not "Table A", "Table I")
- Reference in text **before** the table appears: "Table 2 provides…" or "(see Table 2)"
- Every abbreviation in the table must be spelled out in the Note
- Consistent alignment: text → left; numbers → right; headers → center or left
- Use enough spacing and concise cell text so the table remains readable at journal page width
- Do not use a table as a dumping ground; move extraction-level detail to supplementary material
- Minimize non-data-ink: avoid visible grids, vertical rules, decorative shading, repeated symbols, and unnecessary boldface
- Use real structural grouping instead of manual spaces or fake indentation
- Put units and repeated symbols in headers whenever possible

---

## THE SIX TABLE TYPES — FULL DESIGN GUIDE

---

### TYPE A: Literature Comparison Table
*Used in: Introduction*
*Purpose: Show the gap this paper fills relative to prior reviews*

**Column structure (standard 6-column):**

| Literature | Sample Size | Period | Databases | Research Content | Findings |
|---|---|---|---|---|---|

**Design rules:**
- Each row = one prior review paper
- **Last row always = "This review"** — clearly distinguishing what is new
- Research Content column: use sub-columns or checkmarks if comparing across themes
  - Sub-column example: Portfolio Theory | Application of AI | Stock Market Forecasting | Model Solving | Other Areas
  - Use √ for covered, × for not covered, £ for partially covered
- Findings column: 1–2 sentence summary, not a full paragraph
- Sort rows chronologically (oldest first) so the reader sees evolution
- Caption: "Table 1. Comparison of this study with existing [field] review literature."

**Before / After Example:**

*User provides (raw):*
```
Kehinde 2023 - 220 papers - 2001-2021 - Scopus - AI in stock forecasting - ML shifting to DL
Kumbure 2022 - 138 papers - 2000-2019 - Multiple - ML for stock prediction - ANN most common
This review - 227 papers - 2019-2024 - WoS - Portfolio theory + AI - M-V improvements + AI methods
```

*Table-designed output:*

**Table 1.** Comparison of this study with existing literature on portfolio and stock prediction reviews.

| Literature | Sample Size | Period | Database | Research Content | Key Findings |
|---|---|---|---|---|---|
| Kehinde et al. (2023) | 220 | 2001–2021 | Scopus | AI: stock forecasting | Technology gradually shifting from ML to DL and hybrid models |
| Kumbure et al. (2022) | 138 | 2000–2019 | Scopus, IEEE, WoS, ScienceDirect | ML: stock prediction | ANN most common; S&P 500 most studied index |
| **This review** | **227** | **2019–2024** | **Web of Science** | **M–V improvements + AI methods** | **(i) M–V enhancements on risk, constraints, attitude, dynamics; (ii) MLP, LSTM, GA most used AI methods** |

*Note:* WoS = Web of Science; ML = Machine Learning; DL = Deep Learning; ANN = Artificial Neural Network; M–V = Mean–Variance; MLP = Multi-Layer Perceptron; LSTM = Long Short-Term Memory; GA = Genetic Algorithm.

---

### TYPE B: Bibliometric / Descriptive Table
*Used in: Methodology section*
*Purpose: Characterize the literature sample — which journals, how many papers, how many citations*

**Best presented as a two-panel table:**

**Panel A:** Publication source (journals with ≥ threshold papers)
Columns: `Rank | Name of Journal | Papers`
Sort: descending by paper count

**Panel B:** Citation impact (journals with ≥ threshold citations)
Columns: `Rank | Name of Journal | Citations`
Sort: descending by citation count

**Design rules:**
- Rank column: integer, right-aligned
- Journal names: full name (not abbreviated), title case
- Numbers: right-aligned, no decimal places for counts
- Note below Panel B: define what period the citations cover, and explain any cutoffs
  > "Note: Panel A shows journals with three or more publications (JCR Q1; ABS3+) for 2019–2024; Panel B illustrates journals with more than 20 citations over the period."
- Caption: "Table 2. Descriptive analysis of the reviewed literature."

**When to split into more panels:**
- If also showing temporal distribution (papers per year) → Panel C
- If showing field/topic distribution → Panel D

**Literature-review Table 1 choice:**
- Use **one row per included study** when the sample is small and the reader needs study-level lookup.
- Use a **summary descriptive table** when many studies are included; summarize publication period, study design, region/market, sample-size bands, data source, or asset class.
- If one-row-per-study detail is still necessary, move the exhaustive version to the appendix/supplement and keep the main text table summarized.
- For literature reviews, Table 1 usually belongs in the methodology/sample-description section, not deep in the thematic results.

---

### TYPE C: Feature Mapping / Constraint Table
*Used in: Thematic sections*
*Purpose: Show which papers incorporate which features, constraints, or characteristics*

**Column structure:**
- First column: Literature (Author, Year) — left-aligned
- Remaining columns: Feature names — centered headers, short (1–3 words)
- Cells: √ (present), £ or × (absent), ~ (partially)

**Design rules:**
- Feature columns should be ≤ 8 (beyond that, split into two tables)
- Sort rows chronologically or by sub-theme grouping
- Bold the feature name in header if it's the "most important" feature
- Note below: define all symbols
  > "Note: √ indicates the feature is incorporated; £ indicates the feature is not incorporated; × indicates explicitly excluded."
- Caption: "Table 3. Summary of [constraint/feature] in existing [topic] literature."

#### Spec-Driven Review Taxonomy Variant

Use this variant when the project contains a table-specification document and a CSV coding file, for example a review taxonomy table such as state representation, action space, reward pillars, Markovian validity, or evaluation rigor.

**Design gate additions:**
- Read the relevant table section in the specification file before designing the table.
- Treat the specification's `Purpose`, `Column`, and `Source fields` as the canonical schema unless the user asks to revise them.
- Preserve the table's role: a feature-mapping table should show how studies map to features, not only aggregate counts.
- If reducing rows for the main manuscript, state whether the table is `complete`, `representative`, or `supplementary`.

**Citation and study identification:**
- In LaTeX manuscripts, use `\cite{bibkey}` in the study/reference column when the user wants citable studies.
- Verify cited bibkeys exist in the `.bib` file before finalizing.
- Do not use raw citekeys alone in the manuscript table unless the user asks for an extraction-table style.

**Representative-row rule:**
- Do not silently reduce a complete corpus table to a small sample.
- If the corpus is too large for the main manuscript, choose representative rows by an explicit rule, such as coverage across years, coverage across taxonomy categories, inclusion of rare/advanced features, or one example per major sub-theme.
- Add a note such as:
  > "Note: This table reports representative studies selected to illustrate the main [taxonomy] patterns in the [N]-paper corpus. The complete paper-level coding is provided in [file/supplement]."
- If the selection rule would affect interpretation materially, explain it before editing or ask the user to choose between a complete appendix table and a representative main-text table.

**Column naming and audit columns:**
- Convert internal coding labels into reader-facing labels. Example: `price_return_features` → `Price/return`; `macroeconomic_sentiment_features` → `Macro/sentiment`.
- Keep audit columns only when they add interpretive value beyond raw feature flags.
- Name audit columns precisely and define them in the note. Example: use `Temporal/hidden-state handling` instead of `Partial-observability treatment` when the column records windows, recurrence, attention, graph context, sentiment/macro context, or regime variables.
- Remove columns that only repeat the note, prose, or another column; preserve the audit meaning elsewhere if needed.

**Wide-table LaTeX pattern:**
- For wide manuscript tables, prefer `tabularx` with compact headers and, when necessary, `sidewaystable`.
- Use symbol columns for binary fields and short controlled vocabulary for categorical fields.
- Keep complete extraction-level detail in supplementary material rather than shrinking the font until the table becomes unreadable.

#### Evidence-Map Taxonomy Variant for Coded CSVs

Use this variant when a review table is built from a coded CSV with many studies and repeated categories, and the main manuscript needs to distinguish design patterns rather than list every paper. Typical inputs include:
- A table-specification file with `Purpose`, `Column`, and `Source fields`.
- A CSV with `BibKey`/`CiteKey`, year/title, one or more taxonomy classes, and audit fields such as mechanism, frequency, cost, constraint, reward/penalty terms, limitation, evaluation, or relevance.
- A manuscript requirement to cite studies with `\cite{...}` while keeping the table compact.
- A separate planned figure/chart for counts, so the table should not duplicate count columns.

**When to choose this pattern:**
- Use it for main-text review synthesis when the CSV has too many rows for a readable one-study-per-row table.
- Use it when the spec asks the table to distinguish mechanism/design/relevance, not just show presence/absence.
- Do not use it when the user needs an audit trail, exact extraction lookup, or every study row; move that version to an appendix/supplement.
- If the user says a proposed table feels vague, formulaic, or copied from a previous table pattern, pause LaTeX editing and return to diagnosis. Present alternative structures for approval before rewriting the manuscript.

**Design method:**
1. Inspect the CSV distribution first: taxonomy classes, missingness, cost/frequency/constraint fields, and repeated patterns.
2. Identify 5--8 row groups that cover the breadth of the taxonomy, including rare or ambiguous patterns.
3. Build columns from the table's review questions, not generic labels. Convert each proposed column into a question the reader needs answered, then make the heading name the answer type.
   - What is being classified?
   - What does the study use, output, optimize, constrain, assume, evaluate, or report?
   - How does that element map to the review construct or domain object?
   - Where in the workflow does it enter: input, model, action, reward, training, evaluation, deployment, limitation?
   - Which constraints, risks, costs, assumptions, data sources, or validation choices affect interpretation?
   - What status should the review assign: core design, supporting component, screening/pre-processing step, evaluation caveat, not reported, or not applicable?
4. Use compact controlled phrases in cells. Prefer `Target weights`, `Projection layer`, `Daily; NR`, `Reward/wealth update`, `Selection-to-weight rule required` over full sentences.
5. Support each row with multiple representative citations when available. Cite enough papers to show that the row is a real pattern, not a single anecdote; one citation is acceptable only for a rare pattern.
6. Verify all cited bibkeys in the `.bib` file before finalizing.
7. Add a note explaining that rows group coded patterns and that the full paper-level extraction is in the CSV/supplement.

**General column-precision rule:**
- Preserve the spec's core dimensions, but rename columns so they state the role of the evidence in this table.
- Avoid bare headings that could apply to any table, such as `Type`, `Object`, `Mechanism`, `Role`, `Status`, `Details`, `Notes`, or `Relevance`, unless they are qualified by a domain noun and the table note defines the meaning.
- Prefer headings in the form `[domain construct] + [evidence role]`, for example `Input information channel`, `Temporal encoding`, `Reward objective`, `Penalty terms`, `Constraint implementation`, `Evaluation protocol`, `Validation weakness`, `Data-source role`, `Algorithm suitability`, `Portfolio-control status`, or `Clinical endpoint`.
- If a heading cannot be paraphrased as a clear reader question, redesign it. Example: `Mechanism` is weak; `Rebalancing rule / interval`, `Feature aggregation method`, `Reward-to-objective mapping`, or `Validation protocol` is stronger.
- Do not automatically remove `Notes`, `Limitations`, `Year`, `Paper`, or `Title` fields when they appear in a CSV/spec. Treat them as candidate columns in the grill session. Recommend keeping, excluding, merging, or moving them to note/prose/appendix from CSV evidence, then ask user approval.
- Keep row labels and cell values short. If a cell becomes a sentence, split the concept into a better column, create a controlled vocabulary, or move the explanation to surrounding prose.
- Do not reuse the same column template across adjacent taxonomy tables unless the underlying CSV fields and table purpose are genuinely the same. For example, an action-space table may need output/mapping/rebalancing columns, while an algorithm table may need observed algorithm variants, observed action-space deployment, asset/evaluation evidence, and representative studies.

**Rejected-design recovery workflow:**
1. Restate the table purpose from the specification.
2. List the strongest and weakest evidence fields in the CSV.
3. Explain why the current headings fail: too generic, not supported by CSV fields, too inferential, too paragraph-like, or too similar to another table.
4. Offer 1--3 replacement structures. For each, give concrete column names, one sample row, and the tradeoff.
5. Ask one approval question before editing LaTeX. Use a grill-style question if the user requested it.

**CSV table-design consultation gate:**
Use this gate when the user asks for suggestions before editing, wants to choose columns, rejects a table, or invokes `grill-me`. Do file-based analysis first, then ask only unresolved questions. Ask one question at a time and include a recommended answer.

**Mandatory CSV-first approval sequence:**
1. Analyze the CSV and table specification before asking design questions. Do not analyze existing manuscript tables to choose the design, columns, representation, or layout for the new CSV table.
2. Summarize the evidence driving the design: row count, cite-key availability, dominant categories, rare categories, missingness/noisy fields, repeated text fields, and fields that duplicate planned figures from the spec.
3. Open a decision ledger with four gates: `Design`, `Columns`, `Representation`, and `Layout`.
4. Recommend the best representation and columns from that evidence; provide alternatives only when there is a meaningful tradeoff.
5. Use grill-style approval questions to confirm the design type, row unit/scope, included columns, excluded columns, selected-column representation, citation strategy, and layout.
6. Update LaTeX only after all four gates are approved or already clearly specified by the user. Inspect the manuscript only after approval, and only for insertion/replacement location, labels, cross-references, and compilation.

Every grill question must be based on CSV/spec analysis. Include the relevant field name, pattern, count, missingness issue, or sample value that motivates the recommendation. Do not ask broad preference questions before inspecting the data, and do not copy the design pattern of an existing manuscript table unless the CSV/spec independently justify it.

Use this approval order unless the user's answer requires revisiting an earlier decision:

| Gate | What must be approved | Evidence basis |
|---|---|---|
| Design | table purpose, row unit, complete vs representative/supplementary, grouping strategy | row count, repeated categories, spec purpose |
| Columns | included and excluded columns | source fields, missingness, cardinality, redundancy with planned figures, width risk |
| Representation | display form for each selected column | value length, cardinality, consistency, citation need, interpretive risk |
| Layout | physical table layout | number of columns/rows, cell length, journal width, landscape/panel need |

Ask one question per gate or unresolved sub-choice. If the user rejects the recommendation, revise that gate from the CSV evidence before moving forward.

1. **Purpose choice:** Is the table meant to document extraction, synthesize design patterns, compare methods, audit reporting gaps, or support a figure?
   - Recommended default: use synthesis/evidence-map tables in the main manuscript and move extraction-level lookup to CSV/supplement when there are many studies.
2. **Row-unit choice:** Should each row be a study, taxonomy class, deployment pattern, design decision, evidence gap, or panel group?
   - Recommended default: use grouped rows for main-text taxonomy tables; use study rows only for small or appendix tables.
3. **Scope choice:** Should the table be complete, representative, or supplementary?
   - Recommended default: representative main-text table with a note naming the complete CSV/supplement when the corpus is too large.
4. **Column inclusion/exclusion choice:** Which spec dimensions must remain, which CSV fields are too noisy/sparse, and which fields duplicate planned figures or another approved column?
   - Recommended default: keep only CSV-supported columns that answer the review question. Treat `Year`, `Paper`, `Title`, `Limitations`, and `Notes` as candidate columns rather than automatic exclusions; recommend include/exclude/merge/move based on CSV evidence and ask user approval. Remove separate count columns only when a chart will report counts and the user approves.
5. **Column naming choice:** Do headings name the evidence precisely, or are they generic placeholders?
   - Recommended default: replace vague headings with domain-specific evidence roles, such as `Action-output design`, `Evaluation evidence`, `Constraint implementation`, `Temporal encoding`, or `Reporting gap`.
6. **Citation choice:** Should rows use single citations, multi-citations, or exhaustive study citations?
   - Recommended default: use verified multi-citations for grouped rows to show the pattern is backed by several studies; avoid unreadable citation cells and point to the full CSV for exhaustive coverage.
7. **Layout choice:** Should the table be a single table, panelled table, combined panel table, landscape table, or appendix table?
   - Recommended default: prefer a single grouped table or combined panel table at manuscript width; use panels for readability; use landscape only when the table cannot be made readable otherwise.
8. **Cell-style choice:** Are cells compact labels or paragraph-like explanations?
   - Recommended default: use controlled phrases; if a cell becomes a sentence, split the concept into a better column or move the explanation to prose.

**Selected-column representation grill:**
After the candidate columns are selected, decide how each column will be represented before editing LaTeX. Do not ask the user about every obvious column; ask only where representation affects readability, interpretation, or manuscript quality.

For each important selected column, record:
- `Source field(s)`: exact CSV/spec fields supporting the column.
- `Reader question`: what the column helps the reader decide.
- `Display form`: raw category, controlled vocabulary, checkmark/symbol, grouped phrase, merged column, split sub-column, multi-citation cell, table note, prose, figure, appendix, or omitted.
- `Compression rule`: how long values become concise table cells.
- `Citation rule`: no citation, one representative citation, multi-citation, or complete citation list.
- `Excluded detail`: where omitted information goes, such as surrounding prose, a chart, appendix, or CSV supplement.

Use this decision pattern:

| Candidate column | Source field(s) | Recommended representation | Why | User choice needed? |
|---|---|---|---|---|
| [column name] | [CSV/spec fields] | [display form + compression rule] | [readability/evidence reason] | [yes/no] |

Ask grill-style questions when the representation is not obvious:
- "For this selected column, the key choice is display form. Recommended: controlled vocabulary instead of raw CSV text, because the raw values are long and inconsistent. Should I use controlled phrases?"
- "For citations, recommended: multi-citations per grouped row, because it strengthens review evidence without listing every study. Should I use multi-cites here?"
- "For this noisy field, recommended: do not make it a column; summarize it in the note/prose. Should I exclude it from the table?"
- "For this selected column, recommended: merge it with `[related column]`, because both answer the same reader question and separate columns will widen the table. Should I merge them?"
- "For this selected column, recommended: split it into `[sub-column A]` and `[sub-column B]`, because one heading would hide two different review dimensions. Should I split it?"

**Grill-style approval prompts for table work:**
- "Design gate: the CSV has [N] rows and `[field]` repeats into [K] main patterns, so recommended design is [grouped evidence map / feature matrix / complete extraction]. Should I approve this design?"
- "Column gate: `[field]` has [missingness/cardinality] and duplicates [planned chart/approved column], so recommended action is [include/exclude/merge/split]. Should I approve this column choice?"
- "Column gate: `[Year/Paper/Title/Limitations/Notes field]` is present in the CSV. Recommended action is [include/exclude/merge/move to note or prose] because [CSV-based reason]. Should I approve this column choice?"
- "Representation gate: `[field]` values are [long/inconsistent/sparse], so recommended display is [controlled vocabulary / symbols / grouped phrases / note / appendix]. Should I approve this representation?"
- "Layout gate: the approved columns create [N] visible columns, so recommended layout is [single grouped table / panel table / combined panel table / landscape / appendix]. Should I approve this layout?"
- "The CSV has [N] rows and repeated values in `[field]`, so the key unresolved design choice is row unit. Recommended: grouped evidence-map rows rather than one row per study. Should I proceed with that?"
- "`[count field]` duplicates the planned chart, while `[citekey field]` supports citations. Recommended: exclude count columns from this table and use multi-citations as evidence support. Should I proceed?"
- "`[title/paper field]` is high-cardinality in the CSV. Recommended: [include it / exclude it / move it to appendix / replace it with a `Studies` citation column] because [CSV-based reason]. Should I approve this column choice?"
- "The current headings do not map cleanly to `[CSV fields]` or the spec purpose. Recommended: replace them with CSV-supported, review-question headings. Should I update the LaTeX with this structure?"

**Reusable heading examples by review-table type:**
- State/input tables: `Information channel`, `Temporal encoding`, `Context signal`, `State-construction role`, `Hidden-state handling`.
- Action/control tables: `Action-output design`, `Domain mapping`, `Execution rule / interval`, `Feasibility or risk constraint`, `Control status`.
- Reward/objective tables: `Objective encoded`, `Risk term`, `Cost/penalty term`, `Training signal`, `Portfolio-objective alignment`.
- Algorithm tables: `Algorithm family`, `Observed algorithm variants`, `Observed action-space deployment`, `Asset-class evidence`, `Evaluation evidence`, `Portfolio decision represented`.
- Evaluation tables: `Backtest protocol`, `Benchmark type`, `Cost/slippage treatment`, `Statistical test`, `Reproducibility gap`.
- Data/source tables: `Market/asset scope`, `Data frequency`, `Alternative-data role`, `Pre-processing dependency`, `Generalizability concern`.

**Action-space-specific example, not a general rule:**
- `Action-output design` instead of a bare `Action object`
- `Portfolio mapping` instead of a bare `Portfolio role`
- `Rebalancing rule / interval` instead of a bare `Mechanism`
- `Feasibility or risk constraint` instead of generic `Constraint handling`
- `Cost integration` instead of `Transaction cost during action`
- `Portfolio-control status` instead of generic `Relevance`

**Template for mechanism/design evidence maps:**

| Taxonomy class | Design/output pattern | Domain mapping | Execution / timing | Constraint or audit dimension | Cost / penalty treatment | Review status | Representative studies |
|---|---|---|---|---|---|---|---|
| [coded class] | [short design phrase] | [how output becomes domain object] | [rule; interval; NR if absent] | [constraints/risk/audit terms] | [cost/penalty status] | [taxonomy implication] | `\cite{key1,key2,key3}` |

**Action-space example:**

For a DRL portfolio-optimization action-space CSV, use columns such as:
`Action-space class | Action-output design | Portfolio mapping | Rebalancing rule / interval | Feasibility or risk constraint | Cost integration | Portfolio-control status | Studies`.

Good row style:
`Continuous | Weight-vector allocation | Target weights or weight changes | Direct allocation or update from previous weights; daily, intraday, or NR | Budget; simplex; variance; turnover | Reward or wealth update | Direct allocation control | \cite{...}`

Bad row style:
`Continuous | Portfolio weights or allocation vector | Direct allocation or adjustment from previous weights; frequency may be daily, intraday, or unreported | Often includes turnover and transaction-cost terms; feasibility must be explicit | Core portfolio-control formulation because the action directly determines allocation | \cite{...}`

**Anti-patterns:**
- Do not use separate count columns in this table when the same counts will be shown in a figure.
- Do not over-cite every paper in a row if the citation cell becomes unreadable; choose representative, verified, coverage-rich citations and point to the complete CSV.
- Do not invent mechanistic detail that is not supported by the CSV/spec. If a mechanism is inferred from title or context, keep the wording cautious or mark it as not reported.
- Do not retain paragraph-like cells; the surrounding manuscript prose should interpret the table.
- If the user is dissatisfied with the table design, stop editing and present 1--2 alternative structures for approval before updating LaTeX.

**Before / After Example:**

*User provides (raw):*
```
Gupta 2021: no transaction costs, has bounds, has no short selling, no liquidity, has cardinality
Jalota 2023: no transaction costs, has bounds, has no short selling, has liquidity, has cardinality
Gong 2022: has transaction costs, has bounds, has no short selling, no liquidity, has cardinality
```

*Table-designed output:*

**Table 3.** Summary of portfolio constraints in existing multi-period fuzzy portfolio literature.

| Literature | Transaction Costs | Bounds | No Short Selling | Liquidity | Cardinality |
|---|:---:|:---:|:---:|:---:|:---:|
| Gupta et al. (2021) | £ | √ | √ | £ | √ |
| Jalota et al. (2023) | £ | √ | √ | √ | √ |
| Gong et al. (2022) | √ | √ | √ | × | √ |

*Note:* √ = incorporated; £ = not incorporated; × = explicitly excluded. Cardinality constraint limits the number of assets in the portfolio.

---

### TYPE D: Method Comparison Table
*Used in: Results, Applications, or AI methods sections*
*Purpose: Systematic comparison of approaches, models, or algorithms across studies*

**Column structure varies by sub-field. Typical patterns:**

*For financial portfolio methods:*
`Author | Objectives (beyond return) | Model Type | Other Features`

*For AI/ML method comparison:*
`Literature | Subject/Dataset | ML Methods | DL Methods | Heuristic Methods | Purpose`

**Design rules:**
- Group rows by sub-theme if comparing across categories (use merged left column or bold category rows)
- For binary method presence: use √ / £ grid (as in Zhao et al. Table 4)
- For complex method names: abbreviate in the table, spell out in the Note
- "Other Features" or equivalent catch-all column goes last
- Caption should name the comparison being made specifically:
  > "Table 2. A representative list of comparative studies on financial portfolio optimization."
  > "Table 4. Comparison of the literature on portfolio strategies based on AI."

**Column width guidance:**
- Author column: narrow (15% width)
- Method columns in a presence/absence grid: equal width, narrow
- Description/findings columns: wide (25–35% width)

---

### TYPE E: Future Research Agenda Table
*Used in: Discussion section*
*Purpose: Structured, actionable research directions*

**Three-column format (required):**

| Categories | Research Direction | Research Recommendations |
|---|---|---|

**Design rules:**
- Categories: 3–5 broad groupings (e.g., Theoretical, Methodological, Applied, Emerging)
- Merge the Categories cell vertically across all rows belonging to that category
- Research Direction: a 2–4 word label (e.g., "Portfolio Optimization", "Behavioral Finance", "Applications of AI")
- Research Recommendations: numbered list within the cell (1. 2. 3. …), specific and actionable — not vague
- Recommendations should be verb-led: "Develop…", "Apply…", "Incorporate…", "Explore…"
- Note at bottom: "These research directions are not mutually exclusive; many can be combined."
- Caption: "Table 5. Future research directions."

**Bad recommendation (too vague):** "Study AI more"
**Good recommendation:** "Apply transfer learning in financial market prediction to improve adaptability across different market regimes."

---

### TYPE F: Results / Performance Table
*Used in: Empirical sections or application comparisons*
*Purpose: Present quantitative results (metrics, scores, statistics)*

**Column structure:**
`Method/Model | Dataset | Metric 1 | Metric 2 | Metric 3 | Notes`

**Design rules:**
- Numerical values: consistent decimal places (e.g., all 4 dp for returns, 2 dp for ratios)
- Bold the best value in each column: **0.1823**
- Underline the second-best if useful: <u>0.1756</u>
- Percentage values: include % symbol in header, not each cell: `Return (%)`
- Statistical significance: mark with superscripts (*, **, ***) defined in Note
- If multiple time periods: use horizontal dividers between periods, not separate tables
- Caption: include the dataset and metric names
  > "Table 4. Out-of-sample performance comparison across models on S&P 500 (2015–2023)."

**Numeric readability rules:**
- Use decimals only when they change interpretation. Whole-number ages/counts are usually easier to read than unnecessary calculated decimals.
- Use the same decimal precision down a column.
- For percentages/proportions, include the denominator either in the table cell, header, or note so readers can back-calculate.
- For very small p-values, use a consistent convention such as `<0.001`; avoid overloading descriptive tables with inferential statistics unless the table purpose requires them.
- For Table 1/descriptive tables, avoid standard error and confidence intervals when the goal is sample description rather than population inference.
- Place exact/high-precision values in supplementary material when the main table needs readability but downstream reuse needs full precision.

---

## TABLE FORMATTING: DOS AND DON'TS

| ✅ DO | ❌ DON'T |
|---|---|
| Caption above: "**Table 1.** Comparison of…" | Caption below the table |
| Horizontal rules only (3 total: top, header, bottom) | Vertical lines or grid lines |
| Spell out every abbreviation in the Note | Leave acronyms undefined |
| Reference table in text before it appears | Have tables that are never cited in the text |
| Sort rows by a logical criterion (date, rank, category) | Leave rows in arbitrary order |
| Align: text left, numbers right, headers center | Mix alignment within a column |
| Bold "This review" row in Type A tables | Let the author's own row blend in |
| Note begins: "Note:" (italic or plain, journal-specific) | Omit the Note when abbreviations are used |
| Use consistent symbols: √/£ throughout | Mix √/Y or ×/£ in same table |
| Merge cells for repeated category labels | Repeat the same category label in every row |
| Combine repetitive tables with the same structure | Create several near-duplicate tables |
| Split dense content into panels or sub-columns | Force 10+ unrelated columns into one table |
| Let prose interpret the table's pattern | Repeat every table value in the prose |
| Keep table values consistent with manuscript text | Let counts/percentages drift across text, tables, and figures |
| Move exhaustive extraction to appendix/supplement | Overload the main manuscript table |
| Minimize non-data-ink with sparse horizontal rules and white space | Use full grids, vertical rules, decorative shading, or bold everywhere |
| Put repeated symbols/units in column headers | Repeat `%`, `$`, units, or symbols in every cell |
| Use real grouped rows/sub-columns | Fake indentation with spaces |
| Use meaningful decimal precision | Report long decimals because software produced them |
| Choose one-row-per-study only when it remains readable | Make a long Table 1 when a summary table would communicate better |

---

## DECIDING THE RIGHT NUMBER OF COLUMNS

| Columns | Action |
|---|---|
| 3–5 | Single table, portrait orientation |
| 6–8 | Consider splitting into panels or using landscape |
| 9+ | Must split — either two tables or collapse columns by merging related ones |
| Binary grid ≥ 8 features | Split into two Type C tables by feature group |

---

## CAPTION WRITING GUIDE

**Formula:** `Table [N]. [Specific description of what the table shows and in what context.]`

The caption is the table's manuscript title. It should be concise, informative, and specific enough that a reader can understand the table's purpose before reading the cells.

**Specific = good:**
> "Table 1. Comparison of this study with existing portfolio optimization review literature."
> "Table 3. Summary of portfolio constraints incorporated in multi-period fuzzy selection models (2019–2024)."
> "Table 4. Out-of-sample Sharpe ratio and maximum drawdown across six portfolio models on S&P 500."

**Vague = bad:**
> "Table 1. Literature comparison." ← What literature? Compared on what?
> "Table 3. Constraints." ← Which constraints? In what context?
> "Table 4. Results." ← Results of what?

---

## NOTE WRITING GUIDE

**Standard Note format:**
> *Note:* [Abbreviation 1] = [full form]; [Abbreviation 2] = [full form]. [Symbol key if applicable.] [Any important qualifier about data or scope.]

**Example from Zhao et al.:**
> *Note:* Panel A shows journals with three or more publications (JCR = Q1; ABS3 and above rankings) for the period 2019–2024; Panel B illustrates the journals with more than 20 citations over the period.

**Example from Salo et al.:**
> CP: compromise programming; DP: dynamic programming; GP: goal programming; MCDA: multicriteria decision analysis; MILP: mixed-integer non-linear programming; MO: multiobjective optimization; MOEA: multiobjective evolutionary algorithm; MV: mean–variance; RO: robust optimization.

---

## TEXT AROUND THE TABLE

Before the table, write one purpose sentence:

```text
Table N summarizes [scope] to show [comparison/pattern/gap].
```

After the table, interpret only the main pattern:

```text
The table indicates that [main finding], while [secondary contrast] remains limited.
```

Do not narrate every row or repeat all numeric values. If a value is important enough to repeat in prose, explain why it matters.

---

## WHEN USER GIVES RAW DATA — TRANSFORMATION WORKFLOW

**Step 1: Identify the table type** (see Diagnostic Questions above)
**Step 2: Decide whether the display should be a table, figure, prose, or appendix**
**Step 3: State the table purpose** — the purpose controls columns, rows, precision, and notes
**Step 4: Determine columns** — consolidate redundant ones, split overloaded ones
**Step 5: Determine row order** — chronological, ranked, grouped, frequency-sorted, or importance-ordered
**Step 6: Simplify content** — categorize, standardize units/terms, reduce sparse variables, move exhaustive detail to supplement
**Step 7: Combine repetitive tables or split dense data into panels/categories**
**Step 8: Write the caption** — specific, above the table
**Step 9: Format cells** — align, abbreviate long text carefully, apply symbols, preserve spacing, minimize non-data-ink
**Step 10: Write the Note** — spell out abbreviations, define symbols, state scope caveats and denominators
**Step 11: State where in the paper this table belongs and how the text should introduce it**

Always explain to the user *why* you made each design choice, so they can adjust.
