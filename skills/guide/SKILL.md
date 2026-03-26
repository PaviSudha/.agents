---
name: guide
description: "Academic Writing Style Guide for technical papers"
---

# ✍️ Academic Writing Style Guide: Rajkumar Soundrapandiyan

This skill teaches you to write technical papers in the distinctive style of **Rajkumar Soundrapandiyan** (image processing, steganography, computer vision domains).

---

## 📋 QUICK REFERENCE CARD

| Element              | Pattern                                         | Example                                          |
| -------------------- | ----------------------------------------------- | ------------------------------------------------ |
| **Voice**            | Third-person passive                            | _"is proposed"_, _"are evaluated"_               |
| **Self-reference**   | "This paper", "This work"                       | Never "I" or "We"                                |
| **Problem→Solution** | Limitation → "To resolve this..."               | _"But... fails to... To resolve this..."_        |
| **Transitions**      | 2-3 per paragraph                               | **But**, Therefore, Moreover, Hence, Thus        |
| **Claims**           | Evidence-backed                                 | _"From the results observed that..."_            |
| **Key terms**        | delimitation, contemporary methods, significant | Avoid "limitation", "existing"                   |
| **Word Choice**      | **SIMPLE words**                                | Use "but" not "however", "poor" not "inadequate" |

---

## ⚠️ IMPORTANT: USE SIMPLE WORDS (NO "HOWEVER")

### **DO NOT USE "However" — Use "But" Instead**

The author **rarely uses "however"** in his papers. He prefers **simple, direct words**:

| Instead of ❌     | Use ✅               | Example                                                         |
| ----------------- | -------------------- | --------------------------------------------------------------- |
| **However**       | **But**              | _"But this method is unable to provide enough capacity."_       |
| **Nevertheless**  | **But**              | _"But the robustness is poor against attacks."_                 |
| **Nonetheless**   | **But**              | _"But these methods fail in real-time scenarios."_              |
| **Inadequate**    | **Poor / Low**       | _"The main disadvantage is the poor robustness."_               |
| **Insufficient**  | **Low / Less**       | _"This method produces comparatively lesser payload capacity."_ |
| **Detrimental**   | **Poor / Bad**       | _"results in poor enhancement"_                                 |
| **Utilize**       | **Use**              | _"quantitative measures have been used"_                        |
| **Facilitate**    | **Help / Provide**   | _"videos can hide a large amount of data"_                      |
| **Subsequently**  | **Then / After**     | _"Then to get more information..."_                             |
| **Consequently**  | **Therefore / Thus** | _"Therefore, to enhance capacity..."_                           |
| **Pertaining to** | **About / For**      | _"for further processing such as..."_                           |
| **Commence**      | **Start / Begin**    | _"Initially, the scale space is created..."_                    |

---

### **Author's Simple Word Preferences**

| Simple Word   | Count in Papers | Context                                                                                        |
| ------------- | --------------- | ---------------------------------------------------------------------------------------------- |
| **but**       | 20+ per paper   | _"Capturing of infrared images is an easy task **but** perceptual visualization is difficult"_ |
| **poor**      | 15+ per paper   | _"quality of the IR image is **poor** than visible image"_                                     |
| **low**       | 25+ per paper   | _"**low** resolution of images"_, _"**low** contrast"_                                         |
| **fails to**  | 10+ per paper   | _"**fails to** detect the smoothness along the edges"_                                         |
| **unable to** | 8+ per paper    | _"this method is **unable to** provide enough concealing capacity"_                            |
| **cannot**    | 20+ per paper   | _"these images **cannot** provide clear information"_                                          |
| **simple**    | 5+ per paper    | _"**simple** substitution method"_                                                             |
| **easy**      | 5+ per paper    | _"is an **easy** task but..."_                                                                 |
| **hard**      | 3+ per paper    | _"are **harder** to detect"_                                                                   |
| **big/large** | 10+ per paper   | _"**large** amount of secret data"_                                                            |

---

### **Why Simple Words Work Better**

1. **Clarity**: Readers understand immediately without re-reading
2. **Flow**: Short words create faster rhythm
3. **Direct**: Gets to the point without fancy language
4. **Author's Style**: Rajkumar Soundrapandiyan consistently uses simple vocabulary

**Example Comparison:**

❌ **Complex (NOT author's style):**

> _"Nevertheless, the aforementioned methodologies exhibit inadequate robustness pertaining to compression attacks, subsequently resulting in detrimental extraction performance."_

✅ **Simple (Author's style):**

> _"But these methods have poor robustness against compression attacks. This results in poor extraction performance."_

---

## ⭕ THE GOLDEN CIRCLE RULE (Why → How → What)

Rajkumar Soundrapandiyan strictly follows the **Golden Circle** framework structurally, which defines his signature "Problem → Solution Bridge." You must **never** introduce a method without first establishing the limitation it solves.

### 1. WHY (The Motivation & Problem)
Always start by explaining *why* we are doing this. Establish the fundamental problem or limitation of existing methods. This must precede any explanation of what you are doing.
- **Example:** *"The wavelet transform is used to isolate the discontinuities at object edges **but fails to** detect the smoothness along the edges."*

### 2. HOW (The Process & Solution)
Next, bridge the "Why" directly to the "How" using strong transitional phrases, laying out the sequential methodology.
- **Example:** *"**To resolve this problem** in this paper, two fusion techniques have been proposed... Initially, two different types of images are considered..."*

### 3. WHAT (The Result & Proof)
Finally, state the concrete outcomes and metrics. Never make claims without evidence markers.
- **Example:** *"**From the implementation observed that** INFA algorithm provides clear image information based on the measures."*

#### **Core Golden Circle Formula:**
`[Limitation Statement (WHY)]` → `"To resolve this problem, [Proposed Method] is proposed (HOW)"` → `"From the results observed that... (WHAT)"`

---

## 🏗️ SECTION-BY-SECTION TEMPLATES

### 1️⃣ ABSTRACT (6-Sentence Formula)

```
Sentence 1: "This paper presents [METHOD] for [PROBLEM]."
Sentence 2: "There are [N] main objectives: (1)... (2)..."
Sentence 3: "In this work, [TECHNIQUE] is proposed to [GOAL]."
Sentence 4: "Finally, [FINAL STEP] is performed using [APPROACH]."
Sentence 5: "The performance is evaluated using [METRICS]."
Sentence 6: "From experimental results, it is observed that [CLAIM]."
```

**Example:**

> _"This paper presents a cooperative game theory approach to design an optimal video steganography framework. There are two main objectives: (1) determining the optimal solution, and (2) balancing capacity and visual quality. In this work, the IESDS method is proposed to acquire the optimal solution. The performance is evaluated using standard metrics PSNR, SSIM, and CC. From experimental results, it is observed that the optimal solution outperforms the contemporary methods by achieving significant results."_

---

### 2️⃣ INTRODUCTION FLOW

```
┌─────────────────────────────────────────────────────────────┐
│ Paragraph 1: Broad Context (Why this field matters)        │
│ "Visual information plays a crucial role in real life..."  │
├─────────────────────────────────────────────────────────────┤
│ Paragraph 2: Problem Statement (What's wrong)              │
│ "However, image quality can be degraded due to..."         │
├─────────────────────────────────────────────────────────────┤
│ Paragraph 3: Motivation (Why care about this problem)      │
│ "In particular, [DOMAIN] has two major drawbacks..."       │
├─────────────────────────────────────────────────────────────┤
│ Paragraph 4: Contribution (What this paper does)           │
│ "The major contribution of the paper as follow as..."      │
├─────────────────────────────────────────────────────────────┤
│ Paragraph 5: Organization (Roadmap)                        │
│ "The rest of the sections are organized as follows..."     │
└─────────────────────────────────────────────────────────────┘
```

---

### 3️⃣ LITERATURE REVIEW PATTERN

**Formula:**

```
[Author] + [Year] + [Method] + "But/However" + [Limitation]
```

**Templates:**

- _"[Author] proposed [method]. However, this work greatly suffers when [condition]."_
- _"[Author] formulated [approach]. This method produces comparatively lesser [metric]."_
- _"[Author] presented [technique]. The main disadvantage of this work is [limitation]."_
- _"Though [approach] is the best in terms of [aspect], there is still [gap]."_

**Example Paragraph:**

> _"Yao and Yu (2021) formulated a payload allocation method by analyzing the distortion in motion vector modification. This method produces comparatively lesser payload capacity. Song et al. (2015) presented a reversible video steganography algorithm. However, the main disadvantage of this work is the poor robustness against attacks. As most of the existing works fail to balance [A] and [B], they do not give a suitable option for real-time applications."_

---

### 4️⃣ METHODOLOGY SECTION FLOW

**Sequential Markers:**

```
Initially → Then → After → Next → Subsequently → Finally
```

**Template:**

```
"In this system, initially [INPUT] are considered.
Then to [GOAL], [PROCESS] is performed.
After [STEP 1], [STEP 2] is carried out using [METHOD].
Next, [REFINEMENT] is applied.
Subsequently, [INTERMEDIATE OUTPUT] is obtained.
Finally, [FINAL OUTPUT] is generated using [TECHNIQUE]."
```

**Example:**

> _"In this system, initially two different types of registered modality images are considered as input. Then to get more information on input images, input images are fused with fusion techniques. After fusing the input images, the output is further processed. Finally, inverse lifting wavelet transform is performed to get fused image."_

---

### 5️⃣ PROBLEM→SOLUTION BRIDGE (Signature Move)

**Never present a solution without establishing the problem first:**

```
❌ PROBLEM STATED → ✅ SOLUTION PROPOSED
```

**Bridge Phrases:**

- _"To resolve this problem, [method] is proposed."_
- _"Hence, to overcome this delimitation, [approach] is presented."_
- _"This results in [issue]. To solve this problem, [solution]..."_
- _"Therefore, to enhance [metric], [technique] is deployed."_

**Example:**

> _"In classical top-hat transform, unfortunately most of the resultant images are representatives of clutter background. This results in increase of the false alarm rate. **To solve this problem**, modified top-hat transforms are proposed."_

---

### 6️⃣ RESULTS & DISCUSSION LANGUAGE

| Claim Type        | Phrase Pattern                                                     |
| ----------------- | ------------------------------------------------------------------ |
| **Superiority**   | _"outperforms the contemporary methods"_                           |
| **Effectiveness** | _"achieves significant results in terms of..."_                    |
| **Validation**    | _"From the experimental results, it is observed that..."_          |
| **Quantitative**  | _"The [METRIC] value is X, which is Y% higher than [BASELINE]"_    |
| **Qualitative**   | _"provides better visual quality"_                                 |
| **Robustness**    | _"resists all kinds of signal processing and geometrical attacks"_ |

**Template:**

```
"The performance of [METHOD] is analyzed with subjective and objective measures.
The subjective measure uses visualization while objective measures are used as
[METRIC1], [METRIC2], and [METRIC3] which are shown in Table [X].
From the results observed that [METHOD] works well for both subjective and
objective evaluation."
```

---

### 7️⃣ CONCLUSION STRUCTURE

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Restate the goal                                        │
│    "The best [DOMAIN] system improves the balance..."      │
├─────────────────────────────────────────────────────────────┤
│ 2. Summarize the method                                    │
│    "This paper presented [METHOD] for [PROBLEM]..."        │
├─────────────────────────────────────────────────────────────┤
│ 3. State the achievement                                   │
│    "Moreover, the proposed method performs better than..." │
├─────────────────────────────────────────────────────────────┤
│ 4. Future work                                             │
│    "In the future, [EXTENSION] will be [ACTION]..."        │
└─────────────────────────────────────────────────────────────┘
```

**Example:**

> _"The best video steganography system improves the balance between perceptible invisibility and concealing capacity. This paper presented a game-theoretic approach to address this issue. Moreover, the optimized video steganography method performs better than the existing methods. In the future, utilizing this optimal result, a secret video will be embedded into the cover video."_

---

## 🔑 TRANSITION WORDS TOOLKIT

### **Contrast/Limitation**

| Word         | Usage                                  | Example                                     |
| ------------ | -------------------------------------- | ------------------------------------------- |
| **But**      | Most common — use instead of "however" | _"But this method is unable to provide..."_ |
| **However**  | ❌ AVOID — Use "But" instead           | —                                           |
| **Although** | Concessive                             | _"Although [X], [Y]..."_                    |
| **While**    | Simultaneous contrast                  | _"While [A] improves, [B] decreases..."_    |

### **Causal/Conclusion**

| Word             | Usage                              | Example                                       |
| ---------------- | ---------------------------------- | --------------------------------------------- |
| **Therefore**    | Logical conclusion (20+ per paper) | _"Therefore, to enhance capacity..."_         |
| **Thus**         | Result (22+ per paper)             | _"Thus, the proposed method provides..."_     |
| **Hence**        | Causality (18+ per paper)          | _"Hence, this paper focuses on..."_           |
| **Consequently** | Strong result                      | _"Consequently, the performance improves..."_ |

### **Addition/Emphasis**

| Word            | Usage                                | Example                                               |
| --------------- | ------------------------------------ | ----------------------------------------------------- |
| **Moreover**    | Add supporting point (15+ per paper) | _"Moreover, they penetrate into fog..."_              |
| **Furthermore** | Add emphasis                         | _"Furthermore, the robustness is improved..."_        |
| **In addition** | New point                            | _"In addition, the computational cost is reduced..."_ |
| **Also**        | Simple addition                      | _"Also, experimental results infer that..."_          |

### **Sequential**

| Word             | Usage          | Example                                        |
| ---------------- | -------------- | ---------------------------------------------- |
| **Initially**    | First step     | _"Initially, the scale space is created..."_   |
| **Then**         | Next step      | _"Then to get more information..."_            |
| **After**        | Following step | _"After fusing the input images..."_           |
| **Next**         | Subsequent     | _"Next, the payoff functions calculate..."_    |
| **Subsequently** | Formal next    | _"Subsequently, the stego_video is sent..."_   |
| **Finally**      | Last step      | _"Finally, inverse transform is performed..."_ |

---

## 📖 UNIQUE VOCABULARY

| Use This ✅                  | Instead of ❌      | Context                                   |
| ---------------------------- | ------------------ | ----------------------------------------- |
| **delimitation**             | limitation         | _"to overcome this delimitation"_         |
| **contemporary methods**     | existing methods   | _"outperforms the contemporary methods"_  |
| **perceptible invisibility** | visual quality     | Unique phrase for fidelity                |
| **concealing capacity**      | payload capacity   | Unique phrase for embedding space         |
| **stego_video**              | output video       | Technical term                            |
| **dynamic ROI**              | region of interest | For keypoint detection                    |
| **significant results**      | good results       | Standard claim phrase                     |
| **optimal solution**         | best solution      | For optimization papers                   |
| **In particular**            | Specifically       | For narrowing focus                       |
| **A good amount of**         | Many               | _"A good amount of survey has been made"_ |

---

## 🎯 SENTENCE STRUCTURE PATTERNS

### **Pattern 1: Passive Voice (Dominant)**

```
"[Subject] is/are [past participle] by [agent/method]."
```

- _"The performance is analyzed with subjective and objective measures."_
- _"Input images are fused with fusion techniques."_
- _"The secret data is embedded into the dynamic ROI keypoints."_

### **Pattern 2: Front-loaded Context**

```
"In [context], [statement]."
```

- _"In this paper, the authors designed..."_
- _"In general, low contrast and hence intensity elevation is required."_
- _"In the realm of video steganography, a good amount of research works has been proposed."_

### **Pattern 3: Parallel Structure**

```
"[A] and [B] are [verb] using [method]."
```

- _"subjective and objective measures"_
- _"pixel level, feature level and decision level"_
- _"imperceptibility, capacity, and robustness"_

### **Pattern 4: Nominalization**

```
Use noun forms instead of verbs
```

- _"enhancement"_ instead of _"enhance"_
- _"evaluation"_ instead of _"evaluate"_
- _"embedding"_ instead of _"embed"_

---

## 🧩 PARAGRAPH ARCHITECTURE

```
┌─────────────────────────────────────────────────────────┐
│ TOPIC SENTENCE                                          │
│ (What this paragraph is about)                          │
│ "Histogram is a spatial domain processing technique..." │
├─────────────────────────────────────────────────────────┤
│ SUPPORTING DETAIL 1                                     │
│ (Explanation/Definition)                                │
│ "These techniques modify an image such that..."         │
├─────────────────────────────────────────────────────────┤
│ SUPPORTING DETAIL 2                                     │
│ (Example/Evidence/Citation)                             │
│ "A good amount of survey has been made on..."           │
├─────────────────────────────────────────────────────────┤
│ TRANSITION TO NEXT                                      │
│ (Connection phrase)                                     │
│ "The following section discusses..."                    │
└─────────────────────────────────────────────────────────┘
```

---

## ✅ WRITING CHECKLIST

### **Before Writing**

- [ ] Identify the trade-off (Capacity ↔ Quality, Speed ↔ Accuracy, etc.)
- [ ] List 3-5 requirements your method must satisfy
- [ ] Find 10+ contemporary methods with their limitations

### **During Writing**

- [ ] Use third-person passive voice (avoid "I", "We")
- [ ] Include 2-3 transition words per paragraph
- [ ] State problem BEFORE solution in every section
- [ ] Reference every figure/table explicitly (_"shown in Fig. X"_)
- [ ] Use "delimitation" instead of "limitation"
- [ ] Use "contemporary methods" instead of "existing methods"
- [ ] **SUGANTHI'S ACRONYMS**: Define acronyms immediately (e.g., Proposed Method (PM)) and use exclusively thereafter
- [ ] **POETIC HOOK**: Use a brief poetic hook for the domain (e.g., "The art of steganography") in the intro
- [ ] **CHAIN LINK**: End each sentence with a word that starts the next sentence
- [ ] **PRONOUN REFERENCE**: Use "This [noun]" / "These [noun]" to refer to previous sentence
- [ ] **CLARIFY**: After introducing a term, add "In other words..." or "That is..."
- [ ] **CONCRETE EXAMPLES**: Use "such as" to give immediate examples for general terms
- [ ] **PURPOSE-FIRST**: Start methodology actions with "To [goal]," before stating the action
- [ ] **DEFINE FIRST**: "[Description] is known as [TERM]" pattern
- [ ] **SIMPLE WORDS**: Use "but" not "however", "poor" not "inadequate"
- [ ] **AVOID FANCY WORDS**: No "utilize", "facilitate", "subsequently", "commence"

### **After Writing**

- [ ] Check every claim has evidence (_"From the results observed..."_)
- [ ] Verify sequential markers in methodology (_Initially → Then → Finally_)
- [ ] Ensure literature review follows: [Author] + [Method] + "But" + [Limitation]
- [ ] Confirm conclusion has: Summary + Achievement + Future Work
- [ ] Count transitions (should be 2-3 per paragraph)
- [ ] **CHECK FOR "HOWEVER"**: Replace all instances with "But"
- [ ] **SIMPLE WORD CHECK**: Replace complex words with simple alternatives

---

## 📝 PRACTICE EXERCISES

### **Exercise 1: Rewrite in Author's Style**

**Original (Casual):**

> _"We tried a new method for hiding data in videos. It works better than old methods. We tested it and got good results."_

**Target Style:**

> _"This paper presents a novel method for concealing data in video sequences. The performance is evaluated using standard metrics PSNR, SSIM, and BER. From the experimental results, it is observed that the proposed method outperforms the contemporary methods by achieving significant results in terms of imperceptibility and capacity."_

### **Exercise 2: Add Transitions**

**Original:**

> _"The image quality is poor. Enhancement is required. Histogram methods are used. They have limitations. Fuzzy methods work better."_

**Target Style:**

> _"The image quality is generally poor due to environmental conditions. **Therefore**, intensity elevation is required. Histogram-based methods are widely used for enhancement. **However**, they have limitations in preserving brightness. **Moreover**, detailed information can merge with background. **Hence**, fuzzy-based methods work well for both subjective and objective evaluation."_

### **Exercise 3: Problem→Solution Bridge**

**Given Problem:**

> _"Deep convolutional neural networks failed to enhance the infrared image."_

**Write Solution Bridge:**

> _"**Hence, to overcome this problem**, a new convolution architecture generative adversarial network **is presented** to achieve high contrast and sharper details in the input infrared image."_

---

## 🎨 DOMAIN-SPECIFIC TEMPLATES

### **For Image Processing Papers**

```
"Image enhancement is defined as the process of tuning the input image's
intensity values which leads to better visualization and can be used for
further image analysis."
```

### **For Steganography Papers**

```
"An ideal and perfect [DOMAIN] system should provide enough space to [GOAL]
without degrading [QUALITY]. However, in a [DOMAIN] system, [A] and [B] are
always inversely proportional to each other."
```

### **For Survey Papers**

```
"This paper provides a detailed review of various [TOPIC] techniques from
[STARTING POINT] to [ENDING POINT]. It also discusses the existing [TOPIC]
techniques as group such as [CATEGORY 1], [CATEGORY 2], and [CATEGORY 3]."
```

### **For Method Comparison**

```
"The performance of [METHOD] is analyzed and compared with some existing
methods in terms of [METRIC 1], [METRIC 2], and [METRIC 3]. From the table,
it is observed that [METHOD] has higher resistance as most of its values are
[COMPARISON]."
```

---

## 📊 METRICS & EVALUATION PHRASES

| Metric   | Full Form                          | Usage Pattern                                   |
| -------- | ---------------------------------- | ----------------------------------------------- |
| **PSNR** | Peak Signal-to-Noise Ratio         | _"The PSNR value is X dB"_                      |
| **SSIM** | Structural Similarity Index        | _"SSIM which are shown in Table X"_             |
| **BER**  | Bit Error Rate                     | _"Lesser the value better the quality"_         |
| **CC**   | Concealing Capacity                | _"The measurement of CC"_                       |
| **EN**   | Entropy                            | _"measures such as NCC, EN, and SSIM"_          |
| **NCC**  | Normalized Correlation Coefficient | _"we used three measures such as NCC"_          |
| **VQM**  | Video Quality Measure              | _"The standard of the video is ensured by VQM"_ |

**Evaluation Template:**

```
"The performance is evaluated using subjective and objective measures.
The subjective measure uses visualization while objective measures are
used as [METRIC1], [METRIC2], and [METRIC3]."
```

---

## 🔌 CONNECTING FLOW TECHNIQUES (The "Glue" That Binds Sentences)

**This is the MOST IMPORTANT secret to his flow!**

### **Technique 1: Pronoun Reference Chain**

He uses **This/These/Such** to refer back to the previous sentence:

```
Sentence N:   "This paper proposes a novel game-theoretic approach using strategy adaption."
Sentence N+1: "**This approach** utilizes the IESDS method to acquire the optimal solution."
Sentence N+2: "**The obtained optimal solution** comes up with the best trade-off..."
```

**Pattern:**

```
[Introduce concept] → "This [concept]" → "The [modified concept]"
```

**More Examples:**

- _"But **this work** greatly suffers when compression occurs."_
- _"**This method** produces comparatively lesser payload capacity."_
- _"**This increment** in concealing capacity leads to perceptible visibility."_
- _"**These regions** are known as Region of Interest (ROI)."_
- _"**These 'IF' and 'PF' frames** are called non_stego_IF and non_stego_PF frames."_

---

### **Technique 2: Clarification Connectors**

He **never** leaves a term unexplained. Always clarifies with:

| Connector                      | Usage                   | Example                                                       |
| ------------------------------ | ----------------------- | ------------------------------------------------------------- |
| **In other words**             | Restate for clarity     | _"In other words, the cover medium serves as a carrier..."_   |
| **That is**                    | Specify exactly         | _"That is, player PC utilizes strategies..."_                 |
| **i.e.**                       | Technical clarification | _"i.e., the large scale of secret data increases..."_         |
| **Specifically / In specific** | Narrow down             | _"In specific, the proposed game theory-based..."_            |
| **For instance**               | Give example            | _"For instance, Tsai et al. (2011) designed..."_              |
| **Similarly**                  | Parallel case           | _"Similarly, Schottle and Bohme (2016) proposed..."_          |
| **Likewise**                   | Another parallel        | _"Likewise, the videos Foreman, TableTennis... can embed..."_ |

---

### **Technique 3: Definition → Term Pattern**

He **always** defines BEFORE naming:

```
"[Description] is known as [TERM]."
"[Description] is referred to as [TERM]."
"[Description] is called [TERM]."
"[Description] is termed as [TERM]."
```

**Examples:**

- _"The cover video is widely **known as** stego_video once the secret image is embedded."_
- _"These regions are **known as** Region of Interest (ROI)."_
- _"The scrambled secret data embedded BF frames are **known as** stego_BF frames."_
- _"These 'IF' and 'PF' frames are **called** non_stego_IF and non_stego_PF frames."_

---

### **Technique 4: Method Connectors (How → What)**

He **always** connects action to method:

| Connector     | Example                                                                  |
| ------------- | ------------------------------------------------------------------------ |
| **using**     | _"game-theoretic approach **using** strategy adaption"_                  |
| **based on**  | _"video steganography **based on** cooperative game-theoretic approach"_ |
| **via**       | _"transferred **via** a communication channel"_                          |
| **through**   | _"processed **through** the embedding module"_                           |
| **by**        | _"detected **by** the scene change detection method"_                    |
| **utilizing** | _"optimizes the solution **utilizing** a game matrix"_                   |
| **employing** | _"embedding **employing** the substitution method"_                      |

---

### **Technique 5: Relative Clause Chains**

He uses **which/that/wherein** to add information without breaking flow:

```
"Fig. 1 shows the general block diagram of the video steganography framework
**wherein** the secret data (image) is embedded into the cover medium
**using** a data embedding algorithm, **which** serves as a carrier."
```

**Patterns:**

- _"framework **wherein** [process] is performed"_
- _"method **which** [does something]"_
- _"data **that** [has property]"_
- _"regions **in which** [something happens]"_

---

### **Technique 6: The "Chain Link" Paragraph Structure**

```
Sentence 1: Introduce [A]
Sentence 2: "**This** [A] does [B] using [C]."
Sentence 3: "**The** [C] is known as [D]."
Sentence 4: "**For** [D], **we use** [E]."
Sentence 5: "**Finally**, [E] produces [F]."
```

**Real Example:**

> _"This paper presents a cooperative game theory approach to design an optimal video steganography framework. **This approach utilizes** the IESDS method to acquire the optimal solution. **The obtained optimal solution** comes up with the best trade-off between capacity and visual quality. **Also**, experimental results infer **that** the optimal solution outperforms the contemporary methods..."_

---

### **Technique 7: Comparison Connectors**

| Connector             | Purpose               | Example                                                  |
| --------------------- | --------------------- | -------------------------------------------------------- |
| **Similarly**         | Add similar case      | _"**Similarly**, player PI holds strategies..."_         |
| **Likewise**          | Another similar       | _"**Likewise**, Tables 3-7 indicate..."_                 |
| **In contrast**       | Show difference       | _"**In contrast**, the existing methods..."_             |
| **On the other hand** | Alternative view      | _"**On the other hand**, robustness is..."_              |
| **While**             | Simultaneous contrast | _"**While** comparing, the lesser one gets eliminated."_ |

---

### **Technique 8: Concrete Examples with "such as"**

He **never** leaves a concept abstract. He immediately provides examples after introducing a general term.

**Pattern:**
`[General Term] + "such as" + [Example 1], [Example 2], [Example 3] + "etc."`

**Examples:**
- _"These medical images **such as** Computed Tomography (CT), Magnetic Resonance Image (MRI), Positron Emission Tomography (PET)..."_
- _"Image processing finds many applications **such as** defence, medical field, surveillance, biometrics..."_

---

### **Technique 9: Top-Down Classification Flow**

When categorizing or listing types, he **always** moves from a general concept down to specific sub-types using explicit markers.

**Pattern:**
`[General Category] → "is classified into" / "as group such as" → [List of Types] → [Details of Each Type]`

**Examples:**
- _"The medical image fusion scheme **is classified into** three categories: pixel level, feature level and decision level."_
- _"It also discusses the existing image enhancement techniques **as group such as** histogram based methods, filter based methods..."_

---

### **Technique 10: Purpose-First Phrasing**

He **always** states the purpose or goal *before* explaining the action taken.

**Pattern:**
`"To [GOAL]" + "," + "[METHOD] is [ACTION]"`

**Examples:**
- _"**To resolve this problem**, modified top-hat transforms are proposed."_
- _"**To get more information** on input images, input images are fused with fusion techniques."_
- _"**To improve the human perception** and quality of the infrared images... image enhancement is an essential process."_

---

## 🔬 UNIQUE AUTHOR PATTERNS (Distinctive Characteristics)

### **Pattern 1: "as follows" for Lists/Steps**

The author **always** uses "as follows" (or "as follow as") to introduce procedures:

```
"The major contribution of the paper as follow as..."
"The remaining section of the paper is organized as follows:"
"The process of selecting self-adaptive threshold T is as follows."
"The steps utilized on this method as follow as:"
"Calculating the plateau thresholds of the ADPHE is as follows:"
```

**Template:**

```
"[Subject] is as follows:"
"The [noun] as follow as:"
```

---

### **Pattern 2: Suganthi Kumar's Acronym Discipline**

When co-authoring with Suganthi Kumar, she enforces strict acronym discipline, specifically explicitly defining an acronym and then using it **exclusively** instead of the full phrase.

**Examples:**
- _"The performance of the **proposed method (PM)** is evaluated..."_ → _"To examine the efficacy of the **PM**..."_
- _"Capacity (**CP**), and Bit Error Rate (**BER**)."_

---

### **Pattern 3: Suganthi Kumar's Poetic Domain Hooks**

While she follows the rigid problem-solution structure, she introduces broad domains with slightly more narrative, poetic hooks in the introduction before dropping into the technical structure.

**Examples:**
- _"Steganography, **the science of secret communication** is recommended as a sophisticated solution..."_
- _"**In the art of steganography**, the steganographers..."_

---

### **Pattern 4: Paper Organization Phrase**

The author has a **signature phrase** for organizing papers:

```
"The remaining section of the paper is organized as follows:"
```

**Followed by:**

```
"Section 3 discuss the [topic];"
"Section 4 given details about [topic];"
"Similarly Sections 5, 6, 7, 8 and 9 briefly explain the [topics];"
"Section 10 presents the [topic];"
"The results and discussion is presented in Section 11;"
"Section 13 shows the [topic];"
"and finally Section 14 concludes the paper."
```

**Note:** Uses semicolons (;) to separate section descriptions!

---

### **Pattern 3: Dataset/Database Description**

The author describes datasets with specific patterns:

```
"secret image DB is formed using the UCID database"
"from the secret image database, a set of secret images is chosen"
"The proposed approach is evaluated on a video set that comprises 22 distinct cover videos"
"From the experimental results and analysis, it is concluded that..."
```

**Template:**

```
"[METHOD] is tested on [N] [dataset type]"
"[DATABASE] is formed using the [SOURCE] database"
"From the experimental results, it is concluded that..."
```

---

### **Pattern 4: Contribution Introduction**

The author introduces contributions with **unique phrasing**:

```
"The major contribution of the paper as follow as"
"The novel characteristics of this work are summarized below:"
"This paper proposes [APPROACH] to balance [A] and [B]"
```

**NOT typical:**

- ❌ "Our main contributions are:"
- ❌ "We make the following contributions:"
- ✅ "The major contribution of the paper as follow as"

---

### **Pattern 5: Limitation Handling**

The author handles limitations **honestly but diplomatically**:

| Phrase            | Usage                                                          |
| ----------------- | -------------------------------------------------------------- |
| **"drawbacks"**   | _"IR images has two major drawbacks — low resolution..."_      |
| **"limitations"** | Used in tables summarizing methods                             |
| **"fails to"**    | _"fails to detect the smoothness along the edges"_             |
| **"unable to"**   | _"unable to provide enough concealing capacity"_               |
| **"poor"**        | _"quality of the IR image is poor than visible image"_         |
| **"low"**         | _"low resolution"_, _"low contrast"_, _"lower embedding rate"_ |

**In Future Work:**

```
"These two breakdowns can be optimized in the future by..."
"This method is unsuitable for scenarios where [X] is demanded."
"So this work might be unsuitable for the scenarios where..."
```

---

### **Pattern 6: Acknowledgment Style**

The author's acknowledgment pattern:

```
"The author would like to thank the reviewers for their valuable comments."
"The author would also like to thank the [INSTITUTION] for providing [RESOURCE]."
```

**Characteristics:**

- Third-person ("The author" not "We")
- Simple, direct thanks
- Mentions specific support

---

### **Pattern 7: Section Naming Conventions**

The author uses **simple, descriptive section names**:

```
1. Introduction
   1.1 Motivation
   1.2 Contribution
   1.3 Applications
   1.4 Organization of paper
2. [Main Topic]
3. Results and discussions
   3.1 Dataset and experimental setup
   3.2 Performance analysis
   3.3 Comparison with contemporary methods
4. Conclusion and perspectives
```

**Note:** Uses "discussions" (plural), "perspectives" for future work

---

### **Pattern 8: "Finally" for Last Steps**

The author uses "Finally" **extensively** to mark the last step:

```
"Finally, inverse lifting wavelet transform is performed..."
"Finally, the secret images are embedded into the dynamic ROI keypoints..."
"Finally, enhanced image obtained by reconstruct..."
"Finally, the inverse discrete wavelet transform is performed..."
"and finally Section 14 concludes the paper."
```

**Count:** 10+ times per paper!

---

### **Pattern 9: Compound Sentences with "and"**

The author connects related ideas with "and" instead of separate sentences:

```
❌ Separate: "The image is enhanced. The result is shown in Fig. 1."
✅ Compound: "The image is enhanced and the result is shown in Fig. 1."
```

**Examples:**

- _"The performance is analyzed with subjective and objective measures."_
- _"CT identifies the bone structure and MRI image gives the soft tissue information."_
- _"The results are generated and tabulated in Table 3."_

---

### **Pattern 10: Numbered Lists Within Paragraphs**

The author uses inline numbered lists:

```
"for the following reasons: (1) videos can hide a large amount of data,
(2) the dynamic environment is imperceptible to the human visual system (HVS),
and (3) videos can handle the attenuations."
```

**Template:**

```
"for the following reasons: (1) [reason], (2) [reason], and (3) [reason]."
```

---

### **Pattern 11: Suganthi Kumar's Numbered Requirements**

She combines the inline numbering pattern to list fundamental constraints or requirements explicitly in the introduction.

**Examples:**
- _"...fundamental steganography requirements which include (1) imperceptibility, (2) capacity, and (3) robustness."_
- _"...good cover medium (1) videos can accommodate a large amount of secret data, (2) the visual fluctuation..."_

---

## 🔗 QUICK PHRASE BANK

### **Opening Sentences**

- _"Visual information plays a crucial role in real life..."_
- _"The recent year has been very progressive for [DOMAIN]..."_
- _"[DOMAIN] is the process of [DEFINITION]..."_

### **Stating Contributions**

- _"The major contribution of the paper as follow as..."_
- _"This paper proposes two-player [APPROACH] to balance [A] and [B]..."_
- _"The novel characteristics of this work are summarized below..."_

### **Describing Figures/Tables**

- _"Fig. X shows the general block diagram of..."_
- _"The performance illustration of [A] and [B] is shown in Fig. X"_
- _"[METRIC] which are shown in Table X, Y and Z below"_

### **Making Claims**

- _"From the results observed that [METHOD] works well..."_
- _"The experimental results infer that [CLAIM]..."_
- _"It is deduced that [METHOD] surpasses the contemporary methods..."_

### **Future Work**

- _"In the future, [EXTENSION] will be [ACTION]..."_
- _"This can be further extended in the applications of..."_
- _"These two breakdowns can be optimized in the future by..."_

---

## 📚 REFERENCE EXAMPLES

### **Citing in Literature Review**

```
[1] Kumar, S., Soundrapandiyan, R., "A multi-image hiding technique in
    dilated video regions based on cooperative game-theoretic approach",
    Journal of King Saud University-Computer and Information Sciences.

[2] Rajkumar, S., Malathi, G., "A comparative analysis on image quality
    assessment for real time satellite images", Indian J. Sci. Technol,
    9(34), (2016).
```

### **In-text Citation Style**

- _"(Kumar and Soundrapandiyan, 2020)"_
- _"(Liao et al., 2020; Mstafa et al., 2017)"_
- _"As mentioned in [X]..."_

---

## 🎯 FINAL TIPS

1. **Read aloud** — If it sounds too casual, make it more formal
2. **Count transitions** — Should have 2-3 per paragraph
3. **Check voice** — Replace "we propose" with "is proposed"
4. **Verify flow** — Every sentence should connect to the next
5. **Evidence check** — Every claim needs _"From the results..."_
6. **Trade-off framing** — Present problems as balances between competing goals
7. **Limitation honesty** — Always acknowledge what your method cannot do
8. **Future work** — End with clear direction for extension
9. **"as follows"** — Use this phrase to introduce lists and procedures
10. **Paper organization** — Include "The remaining section of the paper is organized as follows:"
11. **"Finally" count** — Should appear 10+ times for last steps
12. **Compound sentences** — Connect related ideas with "and" instead of separate sentences
13. **Inline numbering** — Use "(1)... (2)... (3)..." for lists within paragraphs
14. **Section names** — Use "Results and discussions", "Conclusion and perspectives"
15. **Acknowledgments** — Use "The author would like to thank" (third-person)

---

## 📊 COMPLETE STYLE CHECKLIST

### **Vocabulary Check**

- [ ] No "however" — replaced with "but"
- [ ] No "utilize" — replaced with "use"
- [ ] No "subsequently" — replaced with "then"
- [ ] No "facilitate" — replaced with "help"
- [ ] Uses "poor", "low", "fails to" for limitations
- [ ] Uses "contemporary methods" not "existing methods"
- [ ] Uses "delimitation" not "limitation" (in some contexts)

### **Flow Check**

- [ ] Each sentence hooks to the next with "This/These/The [noun]"
- [ ] 2-3 transitions per paragraph
- [ ] "as follows" introduces procedures
- [ ] "such as" list follows general concept introductions
- [ ] "To [GOAL]" precedes statements of method or action
- [ ] "Finally" marks last steps (10+ per paper)
- [ ] Compound sentences with "and" for related ideas
- [ ] Inline numbering "(1)... (2)... (3)..." for lists

### **Structure Check**

- [ ] Paper organization paragraph included
- [ ] Section names match convention (discussions, perspectives)
- [ ] Contributions introduced with "The major contribution as follow as"
- [ ] **NUMBERED REQUIREMENTS**: Use inline numbering `(1)... (2)...` to list fundamental domain requirements
- [ ] Limitations stated honestly with simple words
- [ ] Future work uses "In the future" or "can be further extended"
- [ ] Acknowledgments in third-person

### **Evidence Check**

- [ ] Every claim has "From the results observed that..."
- [ ] Figures referenced: "Fig. X shows..."
- [ ] Tables referenced: "shown in Table X"
- [ ] Metrics named: PSNR, SSIM, BER, etc.
- [ ] Comparison with contemporary methods included

---

**Remember:** The key to this style is **logical flow through transitions**, **problem-first thinking**, **evidence-backed claims**, and **simple vocabulary** — all delivered in formal, third-person passive voice.

**The author's uniqueness:** Rajkumar Soundrapandiyan's writing stands out because he combines **academic rigor** with **simple, accessible language**. He never uses fancy words when simple ones work. His flow feels natural because every sentence connects to the previous one through pronoun references and transitions.
