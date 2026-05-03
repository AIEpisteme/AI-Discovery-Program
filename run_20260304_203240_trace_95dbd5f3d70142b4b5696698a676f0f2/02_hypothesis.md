## Primary Hypothesis

In a procedurally generated, contamination-controlled cross-domain task battery, human participants’ task scores will exhibit a stronger single general factor (higher first-factor variance explained and higher average inter-task correlation) than a heterogeneous sample of contemporary AI agents, whose performance will be better fit by a multi-factor structure and will degrade more under out-of-distribution (OOD) task variants.

## Null Hypothesis

After controlling for measurement noise and task difficulty, there is no difference between humans and AI agents in (a) average inter-task correlations, (b) the proportion of variance explained by a single general factor, (c) the relative fit of one-factor vs multi-factor models, or (d) the magnitude of OOD performance degradation.

## Measurable Predictions

1) **Positive manifold strength (humans > AI)**
- **IV:** Agent type (human vs AI model-as-subject); **DV:** Fisher-z mean of all pairwise inter-task correlations across K tasks (e.g., K=12–16).
- **Expected direction/magnitude:** Humans show higher mean inter-task correlation by Δr ≈ 0.10–0.20 (z-difference ≈ 0.10–0.20).
- **Metric:** \(\Delta \bar{z} = \bar{z}_{human} - \bar{z}_{AI}\).
- **Test:** Two-sample t-test or permutation test on \(\bar{z}\). \(H_0:\Delta \bar{z}=0;\ H_1:\Delta \bar{z}>0\).
- **Power / N:** If Δr≈0.15, target **N≈300–500 humans** and **N≈80–150 AI agents** (distinct models/configs) for stable correlation and factor-structure estimation.

2) **General-factor dominance (variance explained; humans > AI)**
- **IV:** Agent type; **DV:** Proportion variance explained by first factor from EFA (or omega hierarchical, \(\omega_h\), from bifactor).
- **Expected direction/magnitude:** Humans exceed AI by ≥10 percentage points in first-factor variance explained (e.g., 0.40 vs 0.30).
- **Metric:** \(\Delta V_1 = V_{1,human}-V_{1,AI}\).
- **Test:** Bootstrap CI for \(\Delta V_1\) + permutation test. \(H_0:\Delta V_1=0;\ H_1:\Delta V_1>0\).
- **Power / N:** Effect size uncertain; preregister Monte Carlo simulation using pilot correlation matrices to set final N.

3) **Model comparison: one-factor vs two-factor (AI shows larger improvement with 2-factor)**
- **IV:** Latent model class (1-factor vs 2-factor/bifactor) within each group; **DV:** Fit indices (ΔCFI, RMSEA, AIC/BIC).
- **Expected direction/magnitude:** AI: 2-factor improves fit meaningfully (e.g., ΔCFI ≥ 0.02); Humans: smaller improvement (ΔCFI < 0.01).
- **Metric:** \(\Delta \mathrm{CFI}_{AI} - \Delta \mathrm{CFI}_{human}\).
- **Test:** Multi-group CFA with likelihood-ratio tests / information criteria. \(H_0:\) improvement equal across groups; \(H_1:\) AI improvement larger.
- **Power / N:** With K≈12 tasks, aim for N≥300 humans; AI N≥100 models to avoid overfitting in CFA.

4) **OOD robustness gap (AI degrades more than humans)**
- **IV:** Distribution shift condition (in-distribution vs OOD procedural perturbation: rule recombination, symbol remapping, irrelevant-text injection); **DV:** Accuracy/score drop.
- **Expected direction/magnitude:** AI shows larger relative drop by ~10–25 percentage points (task-dependent).
- **Metric:** \(\Delta_{OOD} = (S_{ID}-S_{OOD})\) per agent; compare group means.
- **Test:** Mixed-effects regression: \(S \sim Group * Shift + (1|Agent)\). \(H_0:\beta_{Group*Shift}=0;\ H_1:\beta_{Group*Shift}>0\).
- **Power / N:** Use within-agent repeated items (≥30 procedurally generated instances per task-condition) to tighten SEs.

5) **Contamination sensitivity check (AI “g” shrinks after anti-contamination controls)**
- **IV:** Evaluation regime (static items vs dynamic/procedural items + contamination probes); **DV:** change in AI general-factor estimate \(V_1\) and mean score.
- **Expected direction/magnitude:** AI \(V_1\) and mean scores decrease under dynamic/anti-contamination regime; humans minimally affected.
- **Test:** Paired comparison within AI models; \(H_0:\Delta V_1=0;\ H_1:\Delta V_1<0\).
- **Power / N:** AI N≥80; each model evaluated on both regimes.

## Rationale

- Human psychometrics robustly observes a **positive manifold** (broadly positive correlations among cognitive tests) and hierarchical factor structures, motivating the question of whether “general intelligence” is a unifying latent construct versus an emergent/statistical artifact. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7433699/))  
- In AI, formal definitions such as **Legg–Hutter universal intelligence** operationalize intelligence as goal achievement across environments, implying that broad batteries should reveal a general factor if a unified capacity exists (within the tested environment distribution). ([arxiv.org](https://arxiv.org/abs/0712.3329))  
- Empirically, large samples of LLMs tested on “cognitive-test-like” measures can show a **positive manifold** and a general factor correlated with parameter count—suggesting partial convergence with psychometric regularities, but not settling whether this reflects general intelligence vs shared training/benchmark artifacts. ([arxiv.org](https://arxiv.org/abs/2310.11616))  
- Benchmark **data contamination** can inflate apparent generalization in LLMs, so a preregistered design must prioritize procedural item generation and explicit contamination probing to avoid mistaking memorization for general intelligence. ([aclanthology.org](https://aclanthology.org/2024.naacl-long.482/))  

**Key assumptions (explicit):**
- (i) A cross-domain battery can approximate “range of environments” sufficiently to test unitary-vs-plural structure *within* that distribution; (ii) tasks can be rendered in a modality that is comparably usable by humans and AI (e.g., controlled text + simple diagrams); (iii) procedural generation meaningfully reduces leakage.

**Two plausible alternative explanations (with discriminating predictions):**
1) *Interface/representation mismatch:* AI appears multi-factor because some tasks are poorly elicited via the chosen interface. Prediction: making tasks more native (e.g., interactive tool-use for AI; richer perceptual displays for humans) increases cross-task correlations in the disadvantaged group more than in the advantaged group.
2) *Training-data/benchmark artifact:* AI’s apparent “g” is inflated by contamination or by broad internet coverage of task formats. Prediction: under dynamically generated tasks with adversarially novel surface forms, AI’s general factor and mean performance drop disproportionately, while humans remain stable (Prediction #5).

**Recommended design (one concrete option):**
- **Observational, preregistered multi-group psychometrics study**: N≈500 adults (stratified), plus N≈100 AI agents (diverse architectures/sizes). 12–16 tasks × 30 procedural instances × (ID/OOD). Key controls: fixed time/compute budgets, randomized task order, attention checks (humans), deterministic decoding protocols + multiple seeds (AI), contamination probes. Major threats: residual leakage, task-selection bias, and non-independence among AI “subjects”; mitigate with dynamic generation, blinded task release, and hierarchical models with robust SEs.