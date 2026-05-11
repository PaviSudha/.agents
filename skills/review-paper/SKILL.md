---
name: review-paper
description: Use this skill when working on academic review papers, literature reviews, narrative reviews, systematic reviews, PRISMA-style reviews, or journal submissions. It supports review-paper structure and flow, research questions, abstract/introduction/methodology/discussion writing, EJOR/ESWA-style citation and reference formatting, journal-standard table design, CSV-to-table diagnosis, grill-style table design consultation, explicit user approval for design/column/representation/layout choices, table generation, raw-data-to-table transformation, academic figure and flowchart formatting, PRISMA flowcharts, figure captions, choosing the right plot, chart suggestions, and publication-ready chart generation from CSV data with Matplotlib or Seaborn.
---

# Review Paper

## Workflow

1. Identify the user task before writing or editing.
2. Load only the relevant reference file:
   - `references/review-flow.md` for review structure, research questions, PRISMA methodology, section writing, discussion, limitations, and conclusion.
   - `references/citation-practice.md` for in-text citations, reference-list formatting, author-year rules, DOI formatting, and citation consistency.
   - `references/table-design.md` for journal tables, raw-data-to-table transformations, captions, notes, sorting, grouping, and table type selection.
   - `references/figure-formatting.md` for academic figures, PRISMA flowcharts, captions, image reuse, framework diagrams, schematics, and submission checks.
   - `references/chart-generation.md` for chart suggestions, choosing the right plot from CSV/data schemas, and generating publication-ready PDF/PNG figures with Python, Matplotlib, and Seaborn.
3. Apply the selected guidance directly to the user's artifact or request.
4. Keep the paper internally consistent across structure, terminology, citations, table captions, figure captions, and visual design language.

When the user explicitly asks for design suggestions, rejects a proposed table, says column names are vague/repeated, or invokes `grill-me`, do not edit the manuscript first. Use the table-design consultation workflow below, ask only the design questions that cannot be answered from the files, and ask them one at a time with a recommended answer.

For CSV-to-table manuscript work, the required order is: analyze the CSV and table specification first, recommend the best table representation from that evidence, obtain user approval through grill-style questions, then update the LaTeX only after the table design, selected columns, column representation, citation strategy, and layout have been approved or are clearly implied by the user's instruction. Do not inspect existing manuscript tables to infer the design, columns, representation, or layout for a new CSV table; use the manuscript only after approval for insertion, replacement, numbering, cross-references, and compilation.

When the user asks to use this skill on a CSV table, treat the four table choices as required approval gates unless the user explicitly says to skip consultation:
- `Design`: table purpose, row unit, grouping strategy, complete vs representative vs supplementary.
- `Columns`: columns to include, columns to exclude, and why each choice follows from the CSV/spec.
- `Representation`: how each approved column is displayed, compressed, cited, merged/split, or moved to note/prose/figure/appendix.
- `Layout`: single table, grouped table, panel table, combined panel table, landscape, or appendix placement.

Treat `Year`, `Paper`, `Paper title`, `Title`, `Limitations`, and `Notes` fields as candidate columns during the `Columns` gate when they exist in the CSV/spec. Do not exclude them automatically because a table is grouped or compact. Recommend inclusion, exclusion, merging, or moving to prose/note/appendix from the CSV evidence, then ask for user approval in the grill session.

## Defaults

- Prefer numeric citation style (e.g., `\bibliographystyle{elsarticle-num}`) for operations research, management, finance, and AI review journals unless the user gives a different journal style.
- Use journal-standard academic tone: precise, specific, and evidence-linked.
- Treat a review paper as a structured argument, not a list of article summaries.
- For systematic reviews, require transparent search strings, databases, inclusion/exclusion criteria, screening counts, and a PRISMA flowchart.
- For manuscript figures and charts, do not place a title or heading inside the figure; use the manuscript caption for the figure title and keep the plot area to axis labels, panel labels, legends, and necessary annotations.
- For figures and charts, prioritize scientific rigor, readable hierarchy, muted colors, consistent fonts, and self-contained captions.
- For tables, use captions above, notes below, horizontal rules only, abbreviation definitions, logical row ordering, minimized non-data-ink, and enough spacing for manuscript readability.
- For manuscript tables, avoid duplicating prose or figures; the table should add concise structure, comparison, or lookup value that text alone does not provide.

## Chart Work

When generating charts from CSV files:

1. Start with the Elsevier figure-design gate in `references/chart-generation.md`: define the message, audience, figure class, data source, design language, and caption claim before plotting.
2. Inspect the schema and the intended comparison, trend, distribution, relationship, part-to-whole message, or review-synthesis/replotting opportunity.
3. Give a ranked chart suggestion using `references/chart-generation.md`: best chart, acceptable alternative, and charts to avoid for this data.
4. Write a reproducible Python script in the project without an internal chart title, save figures to `figures/`, and export both `.pdf` and `.png`.
5. Provide the manuscript-ready caption separately from the figure image and verify that categorical order, labels, legends, axes, and integer tick marks are correct.

## Table Work

When generating or redesigning tables:

1. Start with the Elsevier table-display gate in `references/table-design.md`: define the table message, manuscript placement, data scope, table purpose, redundancy risk, journal constraints, and note/caption needs.
2. Diagnose whether the data should be a table, figure, prose summary, appendix table, or split/panel table.
3. Keep only relevant data, combine repetitive tables, split large information into clear categories or sub-columns, standardize units/terms/decimals, and preserve consistency with values cited in the manuscript text.
4. Generate a manuscript-ready table with caption above, note below, defined abbreviations/symbols, horizontal rules only, and logical row order.
5. State where the table belongs in the paper and what text should reference it.

When a project has a table specification file, such as `Review_Tables_and_Figures_Spec.md`, treat the specified columns, purpose, source fields, and manuscript placement as the starting schema. Do not silently replace a paper-level taxonomy table with a count-only summary; if summarizing or using representative rows, explain the selection rule and identify where the complete extraction table lives.

For review taxonomy tables from CSV data:

1. Inspect the CSV schema and the corresponding table specification before editing the manuscript.
2. Profile the CSV before proposing columns: row count, cite-key field, high-cardinality text fields, repeated categories, missingness, rare patterns, fields that directly support the table purpose, and fields that should move to prose, a figure, appendix, or note.
3. Use `\cite{bibkey}` in the study/reference column when the manuscript is LaTeX and the user wants citable studies; verify that cited bibkeys exist in the bibliography.
4. Decide whether the table is complete, representative, or supplementary. Complete paper-level tables are appropriate for small datasets or appendices; representative main-text tables must cover the taxonomy breadth and disclose the selection logic in the note.
5. Prefer precise, reader-facing column names over internal coding labels. Rename audit columns so their meaning is explicit, and define any non-obvious audit column in the table note.
6. If the table is wide, use compact labels, symbol columns, `tabularx`, panels, grouped rows, or `sidewaystable`; keep horizontal rules only and compile/check the LaTeX after editing.

For large coded CSV taxonomy tables where the manuscript needs synthesis rather than one row per paper, use the evidence-map taxonomy pattern in `references/table-design.md`. This is appropriate when the CSV has many studies, repeated categorical codes, cite keys, and review-spec dimensions such as inputs, methods, mechanisms, constraints, assumptions, evaluation, or relevance. Derive columns from the table's purpose and review questions, group rows by analytically meaningful design patterns, use short controlled-phrase cells, support each row with multi-citations, and disclose that the full extraction remains in the CSV/supplement.

### Table-design consultation with `grill-me`

Use this mode before editing when the user asks to choose a table design, when the CSV/spec allow several valid representations, or when prior table attempts were rejected.

1. Answer everything discoverable from the CSV and table specification first; inspect the bibliography only to verify citation feasibility. Do not inspect existing manuscript table content when deciding design, columns, representation, or layout. Grill questions must be grounded in CSV/spec analysis, not generic preference questions or patterns copied from another manuscript table.
2. Produce a short diagnosis: table purpose, data scope, row count, cite-key availability, repeated categories, missingness/noisy fields, strongest CSV evidence fields, weakest fields, likely redundancy with planned figures from the spec, and whether the table should be complete, representative, grouped, panelled, or supplementary.
3. Create a decision ledger with four sections: `Design`, `Columns`, `Representation`, and `Layout`. Mark each section as `pending`, `approved`, or `rejected` as the user responds.
4. Recommend the best design first, then optionally list 1--2 alternatives if there is a real tradeoff. For each structure, give:
   - table design type, such as complete extraction, grouped evidence map, feature matrix, comparative taxonomy, or panelled/combined panel table;
   - concrete column headings, avoiding vague labels such as `Object`, `Mechanism`, `Role`, `Status`, `Details`, or `Notes` unless qualified by a domain noun;
   - one sample row using compact controlled phrases, not paragraph cells;
   - inclusion/exclusion rationale for columns, especially count columns, year columns, paper/title columns, limitation columns, notes columns, and audit columns;
   - citation strategy, including whether to use multi-citations per row and whether all cited bibkeys can be verified.
5. For the selected columns, propose a representation plan before editing: source CSV field(s), table heading, display form, compression rule, citation rule, and where excluded detail will go. Display forms include raw category, controlled vocabulary, checkmark/symbol, grouped phrase, merged column, split sub-column, multi-citation cell, table note, prose, figure, appendix, or omission.
6. Ask one approval question at a time, following `grill-me`: state the decision category (`Design`, `Columns`, `Representation`, or `Layout`), cite the CSV/spec basis, give the recommended answer, and wait when the user needs to choose. Do not bundle several unresolved choices into one question.
7. After each user response, update the decision ledger and continue to the next unresolved gate. If the user says `no`, revise that gate from the CSV evidence before asking the next approval question.
8. After all four gates are approved, inspect the manuscript only for the mechanical LaTeX update, then update the table and compile or otherwise validate the artifact. If any gate remains pending or rejected, continue the grill-style consultation instead of editing LaTeX.

If the user rejects a table design, says the headings are vague, says it repeats a previous table pattern, or asks for suggestions before updating, stop editing the manuscript. Reinspect the CSV and specification, explain why the current table fails, propose replacement structures with concrete column names and sample rows, then ask for approval before changing LaTeX.

## Output Discipline

- State the design or writing choice briefly, then provide the improved text, table, figure plan, caption, or code.
- Ask only for missing information that changes the result materially, such as target journal, review type, data columns, or citation style.
- If the user gives a draft, revise it instead of returning generic advice.
