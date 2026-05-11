# Review Paper Flow — Journal-Standard Structure

Derived from published exemplars:
- Salo et al. (2024) *European Journal of Operational Research* — narrative review
- Zhao et al. (2025) *Expert Systems with Applications* — systematic review (PRISMA)

---

## THE CORE PRINCIPLE

A journal review is not an annotated bibliography. It is a **structured argument** that answers:
> *Why does this review need to exist? What does it show that no single prior paper or prior review has shown?*

Every section must serve that argument. If a section can be removed without weakening the paper's claim, it should be restructured or cut.

---

## FULL PAPER ARCHITECTURE

```
Title
Abstract  (150–250 words)
1. Introduction
2. Methodology / Review Protocol
3. [First Major Theme]  ← answers RQ1
   3.1 Sub-theme A
   3.2 Sub-theme B
4. [Second Major Theme] ← answers RQ2
   4.1 ...
N.   Discussion / Implications
N+1. Conclusion
References
Appendix (if needed — abbreviation tables, supplementary data)
```

---

## SECTION-BY-SECTION WRITING GUIDE

---

### ABSTRACT (150–250 words)

**Purpose:** Get the paper accepted for full review. Editors read the abstract first.

**Required sentences — in this order:**

1. **Motivation sentence** — What problem or gap drives this review?
   > "Consumer upgrading and growing investment demand have brought portfolio management to the forefront."

2. **Gap sentence** — What is missing from existing knowledge?
   > "Existing portfolio literature reviews mainly focus on a single perspective, neglecting the comprehensive exploration of multiple perspectives and disciplines."

3. **Method sentence** — What did you do, with what sample?
   > "Based on the PRISMA method, 224 academic articles published between 2019 and 2024 were analyzed."

4. **Findings sentences (2–3)** — Concrete results, not vague summaries.
   > "First, enhancements to the M–V model focus on risk measurement, realistic constraints, risk attitude, and multi-stage portfolios. Second, AI in portfolio management is primarily applied in stock market forecasting, sentiment analysis, and model solving."

5. **Implication sentence** — Who benefits and how?
   > "This study lays a theoretical foundation for advancing portfolio optimization and provides valuable insights for investment practice."

**Keywords:** 4–6 terms. Include: (a) the domain noun, (b) the method, (c) at least one key sub-theme.
Example: `Portfolio | Artificial intelligence | Literature review | Stock market forecasting`

**Common abstract mistakes:**
- Saying "we review the literature on X" without stating what the review finds
- Vague findings: "results show that AI is important" → must name which AI methods and for what
- No method: never omit sample size and period

---

### 1. INTRODUCTION

**Length:** 800–1,500 words. Do not exceed 2 pages.

**Required components in sequence:**

**1.1 Opening hook (1 paragraph)**
Start with the real-world or scholarly importance of the topic. Not a history lesson — the *current moment*. Why does this topic matter *now*?

**1.2 Prior review landscape (1–2 paragraphs + Table 1)**
Summarize what previous reviews have done. This is where you place **Table 1: Comparison with existing literature** — showing prior reviews' sample size, period, databases, content focus, and findings. The last row of this table is always "This review."

Explicitly name what each prior review missed:
> "Mandal & Thakur (2024) focus on higher-order moments… Migliavacca et al. (2023) emphasize portfolio diversification… However, none provide a comprehensive multi-perspective analysis integrating theory and AI methodology."

**1.3 Research Questions (RQs)**
State them explicitly, numbered:
> "The following research questions (RQs) guided our literature review:
> RQ1: How has existing research improved classical portfolio theory (M–V)?
> RQ2: What are the emerging portfolio theories?
> RQ3: How are AI algorithms applied to portfolios?"

**Rule:** Every RQ must be answered by a named section in the paper. If a section doesn't answer an RQ, it shouldn't be a major section.

**1.4 Contributions (numbered list)**
State 3–5 contributions. Be specific:
> "Our research has four contributions. First, by adhering to the research logic of 'literature review – current analysis – future prospects,' we systematically review existing findings. Second, exploring research hotspots provides theoretical references. Third, a comparative analysis of methods propels advancement of the field. Fourth, by aligning with global financial markets, we provide new ideas for portfolio research."

**1.5 Paper roadmap (1 paragraph)**
The last paragraph of the introduction always maps the paper:
> "The remainder of the paper is structured as follows. Section 2 provides the review methodology. Section 3 reviews improvements in portfolio theory… Section 5 discusses implications and future research. Section 6 summarizes findings."

---

### 2. METHODOLOGY / REVIEW PROTOCOL

**Two variants — choose based on your review type:**

#### 2A. Systematic Review (PRISMA)

**Required elements:**

**(i) Framework statement**
> "To ensure depth, rigor, and replicability, we followed the Preferred Reporting Items for Systematic Review and Meta-Analysis (PRISMA) framework."

**(ii) Figure 1: PRISMA Flowchart**
Always placed here. Shows exact n at each stage:
- Identification: total records from database
- Screening: records after title/abstract/keyword filter
- Eligibility: full-text records assessed
- Included: final sample (+ snowballing additions)

**(iii) Eligibility criteria — as two explicit lists:**

*Inclusion criteria:*
- Articles in journals meeting ranking thresholds (state them: UTD24, FT50, JCR Q1, ABS3+)
- Articles related to [topic]
- Articles involving [method]
- Empirical validation on real data
- Published in [language] between [years]

*Exclusion criteria:*
- Low-impact journals
- News, reports, biographies, conference papers, in-press
- Non-empirical articles (theoretical, conceptual, review papers)
- Articles not related to the research scope

**(iv) Search strings — show verbatim:**
> `"portfolio" OR "multi-objective" OR "machine learning" OR "artificial intelligence" OR "stock return"`

**(v) Sample description → Table 2**
After the flowchart, describe the final sample with a bibliometric table showing:
- Panel A: Top journals by paper count
- Panel B: Top journals by citation count
- Temporal trend: papers per year to show field growth

#### 2B. Narrative / Scope-Defined Review

When not using PRISMA, the methodology section must still justify:
- Why certain papers are included/excluded (explicit scope statement)
- Time period covered and why
- Databases or sources consulted
- Whether coverage is comprehensive or representative
- Any deliberate exclusions (e.g., "we purposely abstained from covering ML techniques for portfolio optimization, as these are covered in recent reviews such as Gunjan and Bhattacharyya (2023)")

---

### 3–N. THEMATIC REVIEW SECTIONS

**One major section = one research question.**

**Structure within each major section:**

**Opening paragraph (required)**
Every major section (e.g., Section 3, Section 4) opens with a paragraph that:
- Names what this section covers
- Explains why it matters
- Previews the sub-sections
- References the organizing figure if one exists

> "Despite its many shortcomings, the importance of the M–V theory in finance cannot be overstated. Researchers have made refinements and improvements in four directions. Fig. 2 illustrates the primary directions of these advancements."

**Sub-section structure (3.1, 3.1.1, etc.)**

Each sub-section follows: **Define → Formalize → Cite examples → Note limitations**

*Define:* What is this concept/method?
> "Semi-variance (SV). Unlike variance and standard deviation, SV only considers volatility below the average return or some target return, thus better reflecting investors' concerns about losses."

*Formalize (if applicable):* Give the mathematical expression with equation number:
> "The SV of ξ is defined as Eq. (1): SV(ξ) = E[(ξ − E(ξ))⁻]"

*Cite examples:* Name 2–4 papers that use/develop this approach, with brief descriptions of what each contributes.

*Note limitations:* Always end a sub-concept with its known shortcomings.
> "SV, LPM, and MASD exhibit good capability in gauging downside risk. However, the calculations are more sensitive to the distribution of return."

**Closing synthesis paragraph (required)**
Each major section ends with a paragraph synthesizing across sub-sections: what patterns emerge, what tensions exist, what remains unresolved.

**Section-level headings — formatting rules:**
- Major sections: `3. Review from Framework Perspective: Enhancements of Portfolio Theories`
- Sub-sections: `3.1 Improvement of Mean-Variance Model`
- Sub-sub-sections: `3.1.1 Risk Measurement`
- Do not go deeper than three levels (X.X.X)

---

### N. DISCUSSION / IMPLICATIONS

**Length:** 600–1,000 words + Table (Future Research).

**Required components:**

**N.1 Implications for researchers**
What gaps did the review identify? What methodological opportunities exist? Be specific:
> "For risk measurement, researchers can enhance assessment by refining estimation methods for VaR and CVaR, incorporating higher-order moments, and improving Copula models."

**N.2 Implications for practitioners**
What can investors, managers, or policymakers take from this? Do not repeat the researcher implications — these must be practically oriented:
> "For investors, this paper provides essential guidance for more precise risk assessment. It recommends effective tools for processing extensive data, identifying market patterns, and optimizing investment decisions."

**N.3 Future Research Agenda — Table (required)**
Always present as a structured table with columns:
`Categories | Research Direction | Research Recommendations (numbered)`

Group recommendations into 3–4 categories (e.g., Theoretical, Methodological, Applied, Emerging Topics). Number individual recommendations within each cell (1. 2. 3.).

**N.4 Limitations**
One sub-section addressing validity threats honestly:
- Database coverage (e.g., "only Web of Science core collection")
- Language bias ("only English-language articles")
- Scope exclusions ("energy and environment field excluded")
- Temporal boundary ("articles before June 2024")

Do not minimize limitations — reviewers check this section carefully.

---

### N+1. CONCLUSION

**Length:** 300–500 words. No new content introduced here.

**Required components in sequence:**

1. **Restate the purpose** (1 sentence): What did this review set out to do?

2. **Summarize findings** as numbered/lettered points matching the RQs:
   > "The key findings are as follows: (i) enhancements to the M–V model focus on risk measurement, realistic constraints, risk attitude, and multi-stage portfolios. (ii) AI application areas are mainly stock market forecasting, sentiment analysis, and model solving."

3. **Field-level statement** (1–2 sentences): What does this mean for the field as a whole?

4. **Forward-looking close** (1 sentence): End with aspiration, not summary.
   > "We hope that the findings of this study inspire researchers to develop novel ideas for optimizing MPT."

**What NOT to include in the conclusion:**
- New citations not in the body
- New findings or interpretations
- Repetition of the introduction's motivation paragraph

---

## SECTION LENGTH GUIDE

| Section | Typical length |
|---|---|
| Abstract | 150–250 words |
| Introduction | 800–1,500 words |
| Methodology | 400–800 words |
| Each thematic section (major) | 1,500–3,000 words |
| Discussion | 600–1,000 words + table |
| Conclusion | 300–500 words |
| **Total paper** | **6,000–12,000 words** |

---

## TRANSITION LANGUAGE BANK

**Between sections:**
> "Having established the methodological framework, the following sections review the literature across [N] themes."
> "Building on the theoretical improvements discussed in Section 3, Section 4 examines the role of AI methods."

**Between sub-sections:**
> "Beyond [sub-theme A], a related strand of research has focused on [sub-theme B]."
> "While the above approaches share [X], they differ in [Y]."

**Introducing limitations of reviewed work:**
> "However, this approach has several limitations."
> "Notwithstanding these contributions, [gap] remains unaddressed."
> "While [method] is computationally attractive, it assumes [restrictive assumption]."

---

## NARRATIVE VS. SYSTEMATIC — QUICK COMPARISON

| Feature | Narrative Review | Systematic Review (PRISMA) |
|---|---|---|
| Search documented? | No | Yes — exact strings, databases, n |
| Inclusion criteria explicit? | Partially | Fully (inclusion + exclusion lists) |
| PRISMA flowchart | No | Required |
| Reproducible? | No | Yes |
| Best for | Conceptual/historical synthesis | Empirical evidence mapping |
| Exemplar | Salo et al. (2024) EJOR | Zhao et al. (2025) ESWA |
