# Figure Formatting — Journal-Standard Academic Figures

Sources:
- Salo et al. (2024) *European Journal of Operational Research* — narrative review exemplar
- Zhao et al. (2025) *Expert Systems with Applications* — systematic review exemplar
- Chin, Dursch & Pavlovich (2020) Elsevier Researcher Academy Webinar — *How to Design Effective Figures for Scientific Articles* (Cell Press / Trends journals)

---

## PART 1: FOUNDATIONS — WHY FIGURES MATTER

### How Readers Actually Read Papers

Readers do NOT read papers linearly. The typical reading order is:

```
1 → Title
2 → Abstract
3 → Introduction
4 → Conclusion
5 → FIGURES  ←── Figures seen here, before the body text
6 → Results and Discussion
```

**Critical implication:** Figures create the first impression of your results. A reader may decide whether to read a paper deeply based solely on figure quality. Figures must communicate the core message independently — before the reader has read the methods or results sections.

> "In an era of information overload, first impressions are critical!" — Chin et al. (2020)

### Two Questions to Answer Before Drawing Anything

1. **What is the message?** — What single thing must this figure communicate? If you cannot state it in one sentence, the figure is not ready to be designed.

2. **Who is the audience?** — A specialist sub-field reader vs. a broad journal readership vs. a reviewer vs. a practitioner. The audience determines how much labeling, legend, and explanation is needed.

> "Two key considerations when designing a scientific figure: (1) identify the message and (2) consider the audience." — Chin et al. (2020)

---

## PART 2: FOUR GENERAL DESIGN CONSIDERATIONS

Evaluate every figure against all four before submission.

### 2.1 Information Density

**Too much information is as bad as too little.**

Signs of an over-dense figure:
- Multiple crossing y-axes with overlapping labels
- 10+ data series with no visual hierarchy or focal point
- Panels A–H with inconsistent scales and styles jammed together
- Text labels overlapping data points
- No clear place for the eye to rest

Signs of an under-dense figure:
- A single bar chart that could be stated in one sentence of text
- A schematic that repeats exactly what the text already said
- A 2×2 grid of identical-looking panels with no synthesis

**Fix:** Ask "What would I lose if I removed this element?" If the answer is "nothing essential," remove it. Figures should highlight, not catalogue.

### 2.2 Information Flow

The reader's eye must travel through the figure in a logical order that matches the story.

**Good flow:**
- Left-to-right or top-to-bottom for sequential processes
- Arrows guide the eye explicitly when sequence is non-obvious
- The most important element placed where the eye naturally lands first (upper-left in Western conventions)
- Multi-panel figures use alphabetical labels (A, B, C…) in reading order
- Color draws the eye — use it to direct attention, not to decorate

**Bad flow signs:**
- No logical arrangement to panels — the reader cannot determine which to look at first
- Important result hidden in a lower-right corner panel
- Arrows pointing in confusing or contradictory directions

### 2.3 Scientific Rigor

The figure must accurately represent the data.

- Bar chart axes start at zero — never truncate to exaggerate differences
- Error bars always shown and defined (SD, SEM, 95% CI) in the caption
- Statistical significance markers (*, **, ***) defined and correctly applied
- Color scales must not distort perceived magnitude
- No selective cropping that removes contradictory evidence
- Microscopy/image scale bars present and accurate

### 2.4 Figure Aesthetics

Aesthetics serve communication, not decoration.

**Do:**
- Use a consistent color palette (the "design language") across all figures in the paper
- Choose muted, non-saturated colors — they print well and are accessible
- Use the same font family and minimum size throughout all figures
- Align panels precisely (tops, sides, baselines)
- Use white space deliberately — cramped figures look unprofessional

**Don't:**
- Use unusual or decorative fonts
- Use heavily saturated primary colors (they bleed in print and clash)
- Mix 2D and 3D elements in the same figure
- Add 3D effects to bar charts — they distort perception
- Use grey panel backgrounds — they add ink without information

---

## PART 3: THREE CLASSES OF SCIENTIFIC FIGURES

Every figure belongs to one class. Identify the class first — it determines design priorities.

### Class 1: Illustrative Figures — "This is our plan"

**Purpose:** High-level context before the data. Gives readers the conceptual framework for understanding the experimental design, synthesis route, workflow, or theoretical model.

**Sub-types:**
- **Schematic:** Simplified cartoon of a real system, reaction, or process
- **Experimental design:** Timeline, groups, interventions, measurements
- **Synthetic/process diagram:** Step-by-step transformation of materials, concepts, or decisions

**Design priority: Clarity above all.**
> "There is no such thing as being too clear!" — Chin et al. (2020)

**Design rules:**
- Use a consistent design language: assign one color per concept/component and maintain it throughout
- Simplify ruthlessly — preserve the main idea, remove detail that is not part of the argument
- Label every component (never assume the reader will infer from context)
- Arrows indicate direction of transformation or causality, not mere connection
- Each step in a process must be visually distinguishable from the others

**Caption:** Describe what the figure represents AND state the design language.
> "Fig. 1. Schematic of the proposed multi-stage portfolio selection framework. Stage 1 (blue) = initial screening; Stage 2 (orange) = optimization; Stage 3 (green) = sensitivity analysis and validation."

### Class 2: Characterization Figures — "This is what we made"

**Purpose:** In-depth evidence that the system/model works as described. Tends to be data-heavy.

**Common types in OR/management review papers:**
- Bibliometric trend charts (papers per year, citation growth curves)
- Keyword co-occurrence or co-citation network maps
- Performance comparison heatmaps across methods and datasets

**Design priority: Scientific rigor above all.**

**Design rule — necessary vs. nice-to-have:**
> "Be critical about what is necessary vs. nice to have." — Chin et al. (2020)

The average number of data items and panels per figure has doubled in two decades. More panels ≠ stronger evidence. Each panel must serve a distinct evidential purpose. If two panels show the same thing in different formats, cut one.

**Panel labeling:**
- Label with capital letters in parentheses: (A), (B), (C) — placed upper-left corner of each panel
- Never duplicate a label (two panels labeled C), skip a label (no D), or mix styles (A) vs. a)
- Every axis, curve, and data series labeled within each panel

### Class 3: Applications Figures — "This is what it does"

**Purpose:** Proof of concept. Demonstrates that the proposed method outperforms alternatives or achieves real-world relevance.

**Design priority: Clear comparison.**

**Two key questions:**
1. **Qualitative or quantitative?** Qualitative figures show existence of an effect. Quantitative figures demonstrate magnitude with error bars and significance tests. Prefer quantitative.
2. **What is the benchmark?** Always compare to a baseline, prior method, or established standard. A result without a reference point is characterization, not application.

**The main takeaway must be visually obvious within 3 seconds.** Use color, size, or bold to direct attention to the key comparison. If the reader must study the figure for 30 seconds to see the result, the design has failed.

---

## PART 4: THE FRANKENFIGURE — THE MOST COMMON FIGURE ERROR

A Frankenfigure is assembled from pieces of other papers without coherent design. It is the most common reason figures are criticized in peer review and the most common mistake in review papers.

### Frankenfigure Diagnostic Checklist

If any of these are true, your figure is a Frankenfigure:

- [ ] No logical story to the panel arrangement
- [ ] Acronyms inside the figure that are never explained
- [ ] Duplicated panel labels (two panels labeled C) or missing labels (no D)
- [ ] Inconsistent panel label styles mixing (A) and a) and A:
- [ ] Unlabeled plots, axes, or chemical structures
- [ ] Inconsistent row/column layout (panels of wildly different sizes)
- [ ] Inconsistent level of detail across panels
- [ ] Font styles, sizes, or backgrounds vary between panels
- [ ] Inconsistent panel framing (some have borders, others don't)
- [ ] Text labels illegible at expected print size
- [ ] No new insight beyond what the original studies already published

### How to Fix a Frankenfigure

| Problem | Fix |
|---|---|
| Random panel arrangement | Rearrange to tell a story: illustrative → characterization → application |
| Unexplained acronyms | Spell out all acronyms — even if the original article did not |
| Inconsistent/duplicated panel labels | Remove original labels; create your own consistent (A), (B), (C) set |
| Unlabeled plots or structures | Add your own axis labels and component labels from scratch |
| Inconsistent panel sizes or framing | Align all panel edges; use same frame style for every panel |
| Too much detail everywhere | Select only what serves the argument; remove decorative detail |
| Illegible text | Recreate all labels at ≥ 8pt at final print size |
| No purpose beyond reproduction | Define the insight the combination of panels creates that no single paper provided |

> "Have a purpose for including these images rather than simply reproducing them for the sake of showing a picture." — Chin et al. (2020)

---

## PART 5: WHEN TO REPRODUCE IMAGES FROM OTHER PAPERS

Reproducing figures from prior publications requires both justification and copyright permission.

### Justified Reasons to Reproduce

**Reason 1:** To show what a device, experimental platform, or system actually looks like — when physical appearance is itself informative and cannot be approximated by a schematic.

**Reason 2:** When the result being discussed is itself an image — e.g., microscopy, brain scans, satellite images, visualizations where the image IS the data finding.

**Reason 3 (the best reason):** When combining images from many publications gives readers new insight that no individual paper provides — the review figure synthesizes across the literature.

### How to Reproduce Responsibly

- Obtain permission from the copyright holder (journal + authors) — required for most Elsevier and Cell Press journals
- Cite explicitly in the caption: "(Adapted from Smith et al., 2020, with permission)"
- Remove original panel labels; create your own consistent labeling system
- Add your own scale bars, axis labels, and annotations
- The reproduction must make an argument the original did not make

### What You Must Never Reproduce

- Any standard data plot (bar graph, line chart, spectrum, Kaplan-Meier curve) — replot the data yourself
- An image included just to "show an example" with no analytical purpose
- Multiple figures from the same paper arranged without new synthesis

---

## PART 6: DATA COLLECTION AND REPLOTTING

**The most powerful figures in review papers create a new visualization that no single paper provides — by synthesizing data across multiple publications.**

### Three Replotting Approaches

**Approach A: Comparative landscape**
Collect the same metric (accuracy, Sharpe ratio, F1 score) from multiple papers. Plot all results together on shared axes. Each data point = one published result from one paper.

*Design language:* Color-code by category (e.g., ML methods blue, DL methods red, heuristic methods green). Use consistent marker shapes for subcategories. Include reference numbers [1], [2]… tied to the reference list.

**Approach B: New figure of merit**
Identify two metrics commonly reported in the field that have never been plotted against each other. Plotting them creates a new perspective on the relative strengths of different approaches.

*Design language:* Each plotted point = one paper's result. Ellipses or convex hulls group related techniques. Diagonal lines show iso-performance thresholds. Caption explains what each visual element means.

> "Feature width and delivery rate are commonly reported in this field; this figure plots them against each other to invent a new figure of merit." — Chin et al. (2020)

**Approach C: Full-field taxonomy map**
Show the landscape of a field by organizing all relevant publications along meaningful axes: chronological, methodological, application domain, performance tier.

### Design Language Rules for Replotted Figures

Every replotted review figure must define and state its design language:

- **Color** = one categorical variable (method class, year bracket, domain)
- **Shape** = a second categorical variable if needed
- **Size** = a quantitative variable if needed (e.g., sample size, number of citations)
- **Dashed reference lines** = important benchmark values or performance thresholds

State the design language in the caption:
> "Colors represent distinct method classes: blue = machine learning, red = deep learning, green = heuristic algorithms. Dashed vertical lines mark published performance thresholds for real-world deployment."

---

## PART 7: SCHEMATIC ILLUSTRATIONS — DESIGN LANGUAGE IN DEPTH

A schematic preserves the main idea of a real process, system, or concept in simplified visual form — it is not a photograph and not a data chart.

### Five Rules for Effective Schematics

**Rule 1: One color = one meaning, always**
Assign color meanings before drawing. Apply without exception throughout the figure and across all figures in the paper.
> "Oil phase shown in beige; Biological material in purple; Aqueous phase in blue." — Chin et al. (2020)

**Rule 2: Same entity always looks the same across panels**
If a component appears in panels A, C, and E, it must have identical shape, color, and size in all three. Readers build understanding by recognizing visual patterns.
> "Cell types are the same shape and color across all developmental stages." — Chin et al. (2020)

**Rule 3: Use visual surprise deliberately**
Graphical elements in unexpected locations draw attention. An arrow in an unusual direction, a component breaking out of a grid — these highlight a key result or exception. Use once per figure; never gratuitously.
> "Graphical elements in 'unexpected' locations draw attention to that part of the process." — Chin et al. (2020)

**Rule 4: End parallel comparisons with the same image**
When comparing multiple techniques or pathways that converge on the same outcome, end each pathway with the identical final image. This visually reinforces convergence.
> "Each technique ends with the same image." — Chin et al. (2020)

**Rule 5: Use text to label, not to narrate**
Text inside a schematic should name components and indicate direction. The narrative belongs in the caption and body text. If a schematic requires paragraph-length text inside it to be understood, it is not a schematic — it is a slide deck.

---

## PART 8: UNIVERSAL FIGURE RULES (ALL TYPES)

1. **Caption below** — always. (Tables: caption above. Figures: caption below.)
   Format: `Fig. N. [Title or bold opening phrase.] [Descriptive sentences explaining how to read it.]`

2. **Number sequentially:** Fig. 1, Fig. 2, Fig. 3… Never restart. Never label subfigures as separate figures — panels within a figure are labeled (A), (B), (C) not Fig. 1a, Fig. 1b.

3. **Reference in text before the figure appears:**
   - Integrative: "The search process is detailed in Fig. 1."
   - Parenthetical: "(see Fig. 2)"
   - Interpretive: "Fig. 2 illustrates the four primary directions of M–V model improvement."

4. **Self-contained caption:** A reader seeing only the figure + caption must understand what was measured/shown, how to read the design language, and what the key finding is — without any body text.

5. **Resolution:** ≥ 300 DPI for photographs/halftones; ≥ 600 DPI for line art (flowcharts, schematics). Submit as TIFF, EPS, or PDF vector where possible.

6. **Font size:** All text in figures ≥ 8pt at final print size (~8 cm single-column width, ~17 cm full-page width).

7. **No color-only encoding:** Every color distinction must be supported by a shape, pattern, or label — for colorblind readers and B&W printing.

8. **Consistent design language across ALL figures in the paper:** Same color for the same concept in Fig. 1, Fig. 2, and Fig. 3. Same font. Same line weight. Same box style.

9. **No saturated colors; no unusual fonts:** Use muted professional palettes. Stick to the manuscript's body font family inside figures.

---

## PART 9: REVIEW PAPER FIGURE TYPES — QUICK REFERENCE

| Figure Type | Used In | Design Priority | Caption Length |
|---|---|---|---|
| PRISMA flowchart | Section 2, Methodology | Completeness: exact n at every stage | Short: "Fig. 1. Search process." |
| Framework diagram | Opening of major sections | Clarity of sub-theme organization | Two sentences: what it is + how to read it |
| Process/conceptual diagram | Any section | Logical flow, consistent arrow types | Enough to describe each step |
| Data replot / synthesis chart | Results / Thematic sections | New insight, clear design language | State design language in caption |
| Schematic illustration | Introduction / Section openings | Consistent design language, no narration inside | State design language + what is shown |

---

## PART 10: WHAT ALL GOOD FIGURES HAVE IN COMMON

From Chin et al. (2020) — the synthesis principles that separate good figures from the rest:

- **Add insight** beyond just reporting results from other articles — much like the review article itself should
- **Judiciously reproduce** images from prior publications only when the image itself is part of the research finding
- **Never simply reproduce** raw data plots (bar graphs, spectra, survival curves) — replot or redesign them
- **Use consistent colors and symbols** throughout each figure — and across all figures in the same paper
- **Take inspiration** from real systems to create simplified visualizations of the most important ideas
- **Avoid saturated colors** and unusual fonts
- **Use text to label the images**, not to tell the story — the story belongs in the caption and body

---

## PART 11: FINAL SUBMISSION CHECKLIST

**Message and audience:**
- [ ] The figure's message can be stated in one sentence
- [ ] Design is calibrated to the target journal's readership level

**Four design considerations:**
- [ ] Information density is appropriate (not overloaded; not trivially sparse)
- [ ] Information flows in a logical, readable direction
- [ ] All data is accurately represented (axes, error bars, significance markers)
- [ ] Aesthetics serve communication — no decorative elements

**Class-specific checks:**
- [ ] *Illustrative:* Design language defined; all components labeled; story clear without caption
- [ ] *Characterization:* All axes labeled with units; statistical markers defined; scale bars present
- [ ] *Applications:* Benchmark shown; key result visually obvious within 3 seconds

**Frankenfigure check:**
- [ ] Panels tell a logical story in their arrangement
- [ ] All panel labels consistent (A, B, C…) and non-duplicated
- [ ] All acronyms spelled out inside the figure
- [ ] All text legible at ≥ 8pt at final print size
- [ ] Consistent fonts, colors, framing across all panels

**Universal technical checks:**
- [ ] Caption is below the figure
- [ ] Caption is self-contained
- [ ] Figure referenced in text before it appears
- [ ] Resolution ≥ 300 DPI (600 for line art)
- [ ] File format meets journal requirements
- [ ] No information encoded by color alone

**Figure count by paper type:**

| Paper type | Typical count | Notes |
|---|---|---|
| Narrative review | 0–2 | Only where structure is genuinely clarified |
| Systematic review (PRISMA) | 2–5 | PRISMA required; 1–2 framework diagrams typical |
| Bibliometric review | 3–8 | Trend charts, keyword maps, co-citation networks |
| Meta-analysis | 2–6 | Forest plots and funnel plots required |

**Too many:** If every section has a figure, reconsider — some belong as tables or prose.
**Too few:** A systematic review without a PRISMA flowchart is typically rejected outright.
