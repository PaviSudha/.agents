# Chart Generation for Review Papers

This skill provides instructions for recommending the right chart type and turning raw CSV data into publication-ready figures using Python (Matplotlib and Seaborn). It incorporates the visual logic of modern interactive charting libraries (like AntV G2), the Elsevier Researcher Academy page "Data visualization and choosing the right plot" (<https://researcheracademy.elsevier.com/writing-research/fundamentals-manuscript-preparation/data-visualization-choosing-right-plot>), the Elsevier figure-design webinar `ELS_webinar slides figure design.pdf`, and strict journal formatting rules into static, high-resolution outputs required for LaTeX manuscripts.

## 0. Elsevier Figure-Design Gate Before Plotting

Before suggesting a chart type or writing Python, produce a short figure specification. If the user has not supplied enough information, infer conservatively from the CSV and ask only for missing details that materially change the figure.

```text
Figure message: [one sentence; what the reader must learn]
Audience: [specialist / broad review reader / reviewer / practitioner]
Figure class: [illustrative / characterization / application / synthesis]
Data source: [CSV columns and any filters]
Design language: [what color, marker shape, size, line style, and annotations mean]
Manuscript placement: [yes/no; if yes, no internal figure heading]
Caption claim: [one sentence the caption should support]
```

Reject or redesign any chart that fails this gate:

- **No clear message:** Do not generate a chart that merely displays available columns. Define the claim first.
- **Wrong audience level:** Use more labels and direct annotations for broad review readers; allow denser domain notation only for specialists.
- **No added insight:** In review papers, avoid recreating a standard bar graph from one prior paper. Prefer synthesis across multiple papers, replotting, or a new comparison that the reader could not get from one source.
- **Poor information density:** Remove decorative elements, redundant series, and categories that do not support the message. Group long tails as "Other" only when that does not hide a substantive category.
- **Weak information flow:** Arrange categories, panels, and annotations so the eye moves in the order of the argument: left-to-right, top-to-bottom, chronological, ranked, or grouped by theme.
- **Scientific rigor risk:** Check zero baselines for bars, defined uncertainty, honest scales, visible denominators/sample sizes, and correct units before styling.
- **Missing design language:** Every color, marker, line style, fill, or dashed threshold must mean something and stay consistent across all charts in the paper.
- **Duplicate heading:** For manuscript figures, do not place a chart title, headline, or subtitle inside the image. The manuscript caption supplies the figure title.

## 1. Chart Suggestion Protocol

Use this protocol when the user asks "which chart should I use?", provides a CSV/schema, or asks for chart ideas.

### Step 1: Inspect the Data Shape

Classify every relevant column before suggesting a plot:

| Column type | Examples | Chart implication |
|---|---|---|
| Nominal category | method family, asset class, journal | Compare counts/proportions with bars, dot plots, heatmaps |
| Ordered category | low/moderate/high rigor, quartile, rating | Preserve order with ordered bars, lollipop/dot plots, heatmaps |
| Time or sequence | year, month, stage, screening step | Use lines, step charts, area charts, slope charts, or flow diagrams |
| Continuous numeric | return, risk, accuracy, sample size | Use histograms, density, box/violin, scatter, or error bars |
| Binary/multi-label | uses transaction cost, reports benchmark | Use heatmaps, feature maps, stacked bars only if readable |
| Text/long labels | paper title, algorithm name | Prefer horizontal bars, grouped tables, or annotated dot plots |

### Step 2: Identify the Visual Question

Choose the chart from the question, not from the software menu:

| Visual question | Best first choice | Good alternatives | Avoid |
|---|---|---|---|
| Which categories are most common? | Ranked horizontal bar | Lollipop/dot plot, Pareto bar | Pie/donut with many categories, unsorted bars |
| How does a value change over time? | Line chart | Area chart, step chart, small multiples | Bar chart for long continuous trends |
| How do two numeric variables relate? | Scatter plot | Bubble plot, faceted scatter, regression overlay if justified | Dual-axis chart, grouped bars |
| What is the distribution of a numeric variable? | Histogram | Box plot, violin plot, strip/swarm plot | Mean-only bar chart |
| How do groups differ in distribution? | Box/violin + points | Small-multiple histograms, ridgeline plot | Bar chart hiding spread/outliers |
| How do parts contribute to a whole? | 100% stacked bar for few ordered groups | Donut only for 2-4 clear parts | Pie/donut with many or similar slices |
| Which papers have which features? | Feature heatmap | Binary matrix table, grouped dot matrix | Stacked bars when paper-level detail matters |
| How do methods compare against a threshold? | Dot/bar plot with dashed threshold | Bullet chart, slope chart | Unlabeled reference lines |
| How does screening/filtering progress? | Flow/funnel chart | PRISMA diagram, Sankey if flows branch | Pie chart of stages |
| What new synthesis emerges across papers? | Synthesis scatter or bubble plot | Taxonomy heatmap, threshold dot plot | Reproducing a single paper's chart |

### Step 3: Produce a Ranked Recommendation

When suggesting a chart, return this compact structure:

```text
Recommended chart: [chart type]
Why: [data types + visual question + paper message]
Use when: [conditions where this chart works]
Avoid if: [conditions that make it misleading]
Alternative: [second-best chart and why]
Rejected charts: [1-3 tempting but weaker options]
Caption angle: [claim the figure should support]
```

Example:

```text
Recommended chart: Ranked horizontal bar chart.
Why: The data are categorical method families with paper counts, and the message is dominance/concentration across methods.
Use when: Categories are discrete and labels are long.
Avoid if: You need to show change over time or paper-level co-occurrence.
Alternative: Dot plot if the journal layout is narrow or values are close.
Rejected charts: Donut chart because exact comparison is harder; line chart because categories are not continuous.
Caption angle: DRL portfolio studies are concentrated in a small number of algorithm families.
```

### Step 4: Apply Chart Suggestion Guardrails

- Recommend the simplest chart that answers the question.
- Prefer position on a common scale over angle, area, volume, or color intensity for precise comparisons.
- Prefer bars/dots for categorical counts, lines for continuous time, scatterplots for numeric relationships, and histograms/box plots for distributions.
- Avoid mean-only bars for continuous measurements unless the raw distribution is irrelevant and uncertainty is shown.
- Avoid dual y-axes unless the two scales are clearly related and no simpler faceted chart works.
- Avoid pie/donut charts except for a small number of parts where approximate composition is the message.
- Avoid bubble charts unless the third variable is essential and a size legend is included.
- Use small multiples when comparing the same relationship across groups.
- Use heatmaps for dense categorical matrices, but include readable labels and explain the color scale.
- If the user's requested chart is weak, say so briefly and offer the better chart.

## 2. Selecting the Best Chart Type Based on Data

Before writing code, analyze the primary data relationship and insight you wish to convey. Use the following taxonomy to choose the correct chart:

### A. Comparison (Discrete Categories)
Used to compare values across distinct, discrete categories or against specific targets.
*   **Column / Bar Chart:** Best for comparing data classified into discrete groups (e.g., Publication counts by Author). Horizontal bars are ideal for long text labels or multi-label categorical data. Elsevier stresses that Bar charts should strictly be used for discrete, not continuous, comparisons.
*   **Radar (Spider) Chart:** Used to compare multiple data series relative to a central point.
*   **Bullet Chart:** Highlights a primary measure and compares it against a target value.

### B. Trend & Change Over Time (Continuous Data)
Used to visualize how metrics evolve over a continuous or ordinal period.
*   **Line Chart:** The primary choice for visualizing continuous trends across time (e.g., Yearly Publication Trend). 
*   **Area Chart:** Similar to line charts but shades the area beneath the line to emphasize the volume or magnitude of change over time.

### C. Part-to-Whole
Used to show how individual components contribute to a total value.
*   **Donut / Pie Chart:** Displays the contribution of parts to a whole set (best for categorical proportions with few categories, like Asset Class Distribution).
*   **Stacked Column / Bar Chart:** Shows the contribution of individual "stacks" that make up a total column.
*   **Stacked Area Chart:** Shows the relationship of parts to a whole as they change over time.

### D. Distribution & Weightage
Used to highlight the volume, density, or relative importance of data points.
*   **Bubble / Packed Bubble Chart:** Adds a third dimension (size) to highlight weightage/magnitude. Elsevier recommends Bubble charts specifically for visualizing multi-dimensional data clearly.
*   **Histogram / Ordered Column Chart:** Best for showing the distribution of continuous variables or ordinal categorical data (e.g., Evaluation Rigor Score: Low -> Moderate -> High).

### E. Relationship & Flow
Used to show connections between variables or the progression of a process.
*   **Scatter Plot:** Specifically used for identifying relationships and correlations between two numerical variables to support scientific integrity.
*   **Combination Chart:** Combines bar and line charts to show relationships between mixed types of data series.
*   **Funnel Chart:** Represents the progressive flow or reduction across different phases.

### F. Review Synthesis and Replotting
Used when a review paper combines results, methods, or metadata across many publications.
*   **Synthesis Scatter Plot:** Use when two reported metrics can create a new figure of merit (e.g., performance vs. cost, accuracy vs. sample size). Each point should represent one paper, experiment, or model result.
*   **Threshold Bar / Dot Plot:** Use when categories must be compared against important practical or methodological thresholds. Use dashed reference lines and label the threshold in the caption.
*   **Taxonomy Heatmap:** Use when mapping papers against methods, datasets, asset classes, constraints, or evaluation criteria. Keep the matrix readable and explain all abbreviations.
*   **Bubble Plot:** Use when three dimensions matter, such as method class, publication year, and sample size/citation count. Make bubble area perceptually reasonable and include a size legend.

Review-paper chart rule: if the chart is derived from multiple papers, make the unit of analysis explicit (`paper`, `model`, `experiment`, `dataset`, or `metric observation`) and include that unit in the caption.

---

## 3. Elsevier Academic Standard Principles

Strictly follow these principles for scientific figures:

- **Message and Audience:** Every figure must convey a clear message. Do not include unnecessary or decorative information.
- **Scientific Rigor:**
  - Bar chart axes MUST start at zero. Never truncate axes to exaggerate differences.
  - Avoid 3D effects on plots; they distort perception.
  - Include error bars, confidence intervals, ranges, or sample sizes when the data support them; explain them in the caption or note.
  - Do not use smoothing, interpolation, jitter, log scales, or normalized values unless the choice is stated and justified.
- **Information Density & Flow:**
  - Avoid overcrowding. Remove chart junk.
  - Ensure logical reading order (e.g., left-to-right, top-to-bottom).
  - Sort bars and categories by the argument, not by spreadsheet order: descending rank, chronology, theory group, or ordered scale.
- **Avoid "Frankenfigures" and Frankenpanels:**
  - Use consistent panel labels (e.g., (A), (B), (C)) in the upper left of each panel.
  - Ensure uniform fonts, styles, and background across all panels.
  - Align the tops and sides of all panels perfectly.
  - Spell out any acronyms used in the figure.
  - Do not mix unrelated chart types in one figure unless the panel sequence tells a clear story.
- **Color Consistency:**
  - Use a consistent design language. The same color must represent the same category across *all* figures in the paper.
  - Use muted, non-saturated colors. Avoid pure primary colors.
  - Do not encode meaning by color alone; add direct labels, marker shape, line style, hatch, or text annotation.
- **Caption Readiness:**
  - The chart must be understandable from the figure and caption without the reader searching the body text.
  - The caption should state the data scope, unit of analysis, design language, and main takeaway.
- **Manuscript Heading Rule:**
  - Manuscript figures must not include internal chart headings such as `ax.set_title()` or `plt.suptitle()`.
  - Put the figure number, title, and interpretive claim in the caption below the figure.
  - Keep only necessary in-figure text: axis labels with units, tick labels, direct data labels, panel labels `(A)`, `(B)`, legends, and short annotations for thresholds or outliers.
  - Use an internal title only when the user explicitly asks for a standalone slide, dashboard, poster, or exploratory image.

---

## 4. Aesthetics & Design Language

To ensure the figures look modern, clean, and mimic web-based interactive charts (like AntV G2), strictly adhere to these Matplotlib/Seaborn aesthetic rules:

- **Theme & Background:**
  - For Bar/Line Charts: Use `whitegrid` with a light grey facecolor.
    `sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#F9F9F9", "grid.color": "#E0E0E0"})`
  - For Pie/Donut Charts: Use `white` theme with pure white facecolor.
    `sns.set_theme(style="white", rc={"axes.facecolor": "#FFFFFF"})`

- **Fonts & Typography:**
  - Use `serif` fonts (Times New Roman) to match the LaTeX manuscript.
  - Do not use in-plot headings for manuscript figures. The caption handles the title and interpretation.
  - Use panel labels `(A)`, `(B)`, `(C)` for multi-panel figures, not separate panel titles unless the panel cannot be understood otherwise.
  - Set specific sizes for axes labels (12), ticks (11), legends (10-11), and annotations (9-10).

- **Clean Borders (Spines):**
  - Always remove the top and right spines to reduce chart junk.
    `'axes.spines.top': False, 'axes.spines.right': False`

- **Color Palettes:**
  - Use muted, professional Seaborn palettes (`muted`, `pastel`, `mako`, `flare`, `viridis`, `Set2`, `deep`).
  - Add dark borders to bars (`edgecolor='black', linewidth=0.8`).
  - Reserve saturated or dark accent colors for the focal category only.
  - Reuse the same palette mapping across all generated charts. If `DRL` is blue in Chart 1, it must remain blue in Chart 4.

- **Data Labels:**
  - Label the end of bars with exact values when there are few enough bars to remain legible.
  - Prefer direct labels over legends for short line charts and small category sets.
  - Use annotations to explain thresholds, peaks, outliers, or category groupings; do not narrate the whole result inside the plot.

- **Axes Control:**
  - If plotting counts (number of papers, years), use `MaxNLocator(integer=True)` to prevent fractional ticks (e.g., 2020.5).
  - Use axis labels with units, not vague labels (`Count of papers`, `Sharpe ratio`, `Publication year`).
  - Rotate labels only as a last resort. Prefer horizontal bars for long category names.
  - Use dashed reference lines only for meaningful benchmarks or thresholds, and label them.

### Design Language Template

Every generated chart should have a design-language note in code comments and a caption-ready sentence:

```python
# Design language:
# - color: method family
# - marker shape: data source type
# - marker size: sample size
# - dashed line: minimum acceptable evaluation horizon
```

Caption sentence:

```text
Colors denote method families, marker shapes denote data-source types, and the dashed vertical line marks the minimum evaluation horizon used as a robustness threshold.
```

### Multi-Panel Chart Rules

Use multi-panel figures only when the panels build one argument. Before coding, define each panel role:

```text
(A) Field growth over time
(B) Distribution of method families
(C) Relationship between evaluation horizon and reported performance
```

Rules:

- Keep all panel fonts, axis-label sizes, color mappings, grid styles, and backgrounds identical.
- Place panel labels `(A)`, `(B)`, `(C)` consistently at the upper-left.
- Align axes where comparisons depend on scale.
- Do not include a panel because the data exists; include it only if it advances the figure message.

---

## 5. Python Matplotlib Templates

### 5.1. Standard Setup Boilerplate

Always begin your script with this configuration:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.ticker import MaxNLocator

os.makedirs('figures', exist_ok=True)

# Modern, clean aesthetics
sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#F9F9F9", "grid.color": "#E0E0E0"})
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'axes.labelsize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False
})

PALETTE = {
    # Fill this once per paper and reuse across every chart.
    # Example:
    # 'Deep reinforcement learning': '#4C78A8',
    # 'Classical reinforcement learning': '#F58518',
    # 'Hybrid / ensemble': '#54A24B',
}
```

### 5.2. Horizontal Bar Chart (Multi-label Data)

```python
def generate_chart():
    df = pd.read_csv('data/Data.csv')
    
    # Process multi-label strings if needed (e.g., "A, B, C")
    series = df['column'].astype(str).str.split(',').explode().str.strip()
    series = series[(series != '') & (series != 'Unclassified')]
    
    df_agg = series.value_counts().reset_index()
    df_agg.columns = ['Category', 'Count']
    df_agg = df_agg.head(10) # Keep top N for readability
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.barplot(
        data=df_agg, y='Category', x='Count', hue='Category',
        palette="viridis", ax=ax, legend=False, edgecolor='black', linewidth=0.8
    )
    
    # No in-plot title for manuscript figures; use the figure caption instead.
    ax.set_xlabel('Count of papers')
    ax.set_ylabel('')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    # Add values to bars
    for p in ax.patches:
        width = p.get_width()
        if pd.notnull(width) and width > 0:
            ax.text(width + 0.5, p.get_y() + p.get_height() / 2, f'{int(width)}', 
                    ha="left", va="center", fontsize=10, color='black')
                    
    fig.tight_layout()
    fig.savefig('figures/chart_name.pdf')
    fig.savefig('figures/chart_name.png')
    plt.close(fig)
```

### 5.3. Donut Chart (Proportions)

Use donut charts sparingly. Prefer a ranked bar chart when categories are numerous, percentages are close, or exact comparison matters.

```python
def generate_chart():
    df = pd.read_csv('data/Data.csv')
    df_agg = df['category'].value_counts().reset_index()
    df_agg.columns = ['Category', 'Count']
    
    # Override theme for Pie/Donut
    sns.set_theme(style="white", rc={"axes.facecolor": "#FFFFFF"})
    
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = sns.color_palette("muted")[0:len(df_agg)]
    
    # wedgeprops=dict(width=0.4) creates the donut hole
    wedges, texts, autotexts = ax.pie(
        df_agg['Count'], labels=df_agg['Category'], autopct='%1.1f%%',
        colors=colors, startangle=90, pctdistance=0.85,
        wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2)
    )
    
    plt.setp(autotexts, size=10, weight="bold", color="white")
    plt.setp(texts, size=12)
    
    # No in-plot title for manuscript figures; use the figure caption instead.
    
    fig.tight_layout()
    fig.savefig('figures/chart_name.pdf')
    fig.savefig('figures/chart_name.png')
    plt.close(fig)
```

### 5.4. Synthesis Scatter Plot With Thresholds

Use this when the review combines comparable metrics from multiple papers and the chart creates a new comparison.

```python
def generate_chart():
    df = pd.read_csv('data/synthesis_metrics.csv')
    required = {'paper', 'method_family', 'x_metric', 'y_metric'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f'Missing required columns: {sorted(missing)}')

    fig, ax = plt.subplots(figsize=(8.5, 5.8))
    sns.scatterplot(
        data=df,
        x='x_metric',
        y='y_metric',
        hue='method_family',
        style='method_family',
        s=80,
        palette='Set2',
        edgecolor='black',
        linewidth=0.6,
        ax=ax,
    )

    # Design language:
    # - color and marker shape: method family
    # - dashed lines: application or robustness thresholds
    ax.axvline(12, color='#555555', linestyle='--', linewidth=1.0)
    ax.text(12, ax.get_ylim()[1], '12-month threshold', va='top', ha='left', fontsize=9)

    # No in-plot title for manuscript figures; use the figure caption instead.
    ax.set_xlabel('Evaluation horizon (months)')
    ax.set_ylabel('Reported performance metric')
    ax.legend(title='Method family', frameon=False, bbox_to_anchor=(1.02, 1), loc='upper left')

    fig.tight_layout()
    fig.savefig('figures/synthesis_scatter.pdf')
    fig.savefig('figures/synthesis_scatter.png')
    plt.close(fig)
```

### 5.5. Caption Template for Generated Charts

Write a caption immediately after generating the chart:

```text
Fig. N. [Specific chart title]. The figure summarizes [data scope and unit of analysis]. [Design language sentence: what colors, markers, sizes, or dashed lines mean]. [Main takeaway sentence].
```

Do not duplicate the caption title inside the figure image.

Example:

```text
Fig. 4. Evaluation horizon and reported performance across reviewed DRL portfolio studies. Each point represents one model result extracted from the review dataset; colors and marker shapes denote method families, and the dashed vertical line marks a 12-month evaluation threshold. Longer evaluation horizons remain concentrated in a small subset of method families, indicating uneven robustness evidence across the literature.
```

## 6. Execution & Export

- Save all charts in the `figures/` directory.
- Always save in both `.pdf` (for LaTeX vector scaling) and `.png` formats.
- If using categorical ordered data, explicitly set the category order in Pandas before plotting.
- Save or print the figure specification with the script so future edits preserve the intended message and design language.
- Inspect the exported figure for legibility at expected journal size: about 8 cm wide for single-column and 17 cm wide for full-width figures.
- Before finalizing, check that every acronym, symbol, color, marker, threshold, and abbreviation is either directly labeled or explained in the caption.
