## Primary Hypothesis

Across humans and diverse AI agents, a single latent **generalization** factor estimated from performance on a **procedurally generated, contamination-controlled** cognitive task battery will predict **out-of-distribution (OOD)** task success **better** than (i) traditional human psychometric scores and (ii) standard AI benchmark scores.

## Null Hypothesis

After controlling for measurement error and interface differences, the latent generalization factor provides **no incremental predictive validity** for OOD task success beyond traditional psychometric/benchmark scores (i.e., \(\Delta R^2 = 0\) when adding the factor score to models predicting OOD performance).

## Measurable Predictions

1. **Cross-domain positive manifold / 1-factor structure**
   - **IV:** Task identity (multiple domains: sequence learning, relational reasoning, planning under uncertainty, causal inference, compositional generalization), with matched input/output interfaces for humans vs AI.
   - **DV:** Standardized accuracy/reward per task (and for adaptive tasks, final performance after a fixed interaction budget).
   - **Expected effect:** A 1-factor model fits well within each population (humans; AI) and captures **≥40%** of common variance (e.g., \(\omega_h \ge .40\)).
   - **Metric/test:** Confirmatory factor analysis / hierarchical IRT; test \(H_0:\omega_h < .25\) vs \(H_1:\omega_h \ge .40\).
   - **Power/sample:** Humans **N≈250** typically supports stable factor recovery for ~12–20 tasks with moderate communalities; AI agents: evaluate ≥10 distinct systems with ≥5 random seeds each (power mainly via repeated trials).

2. **Incremental validity for OOD generalization**
   - **IV:** Predictor set = (A) standard scores (humans: IQ composite; AI: benchmark aggregate) vs (B) standard scores + latent generalization factor \(G^\*\).
   - **DV:** OOD performance composite on held-out procedural distributions (new generators/parameters, not just new items).
   - **Expected effect:** Adding \(G^\*\) improves prediction by **\(\Delta R^2 \approx 0.10\)** (e.g., from .20 to .30) in both humans and AI.
   - **Metric/test:** Nested regression with cross-validated \(R^2\); test \(H_0:\Delta R^2=0\) vs \(H_1:\Delta R^2>0\) (permutation test or likelihood-ratio test).
   - **Power/sample:** With N≈250, \(\Delta R^2=.10\) is typically detectable at 80% power (exact power depends on predictor correlations; recommend preregistered simulation).

3. **Benchmark Goodhart/contamination sensitivity (AI-specific discriminator)**
   - **IV:** Degree of contamination risk (low vs high), operationalized by (i) strict generator novelty, (ii) training-data overlap audits, (iii) prompt leakage checks.
   - **DV:** Gap between in-distribution benchmark score and OOD score.
   - **Expected effect:** High-contamination-risk benchmarks show **larger** benchmark–OOD gaps (e.g., mean gap difference **d≈0.5** across models) than low-risk procedural tests.
   - **Metric/test:** Mixed-effects model with random intercepts for model and task family; test \(H_0:\beta_{\text{risk}}=0\) vs \(H_1:\beta_{\text{risk}}>0\).
   - **Power/sample:** ≥10 models × ≥10 tasks/family × ≥5 seeds yields adequate power for medium effects in mixed models.

4. **Resource-boundedness links to generalization (mechanism-leaning, cross-population)**
   - **IV:** Resource constraint manipulation (humans: time pressure / dual-task load; AI: inference-time compute limits or context-window truncation).
   - **DV:** Change in \(G^\*\)-relevant tasks (planning, working-memory-like tasks) vs perceptual/rote tasks.
   - **Expected effect:** Resource constraints selectively reduce performance on control/planning tasks with **interaction** effect (constraint × task-type) **d≈0.3–0.5**.
   - **Metric/test:** Repeated-measures ANOVA or hierarchical regression; \(H_0:\) no interaction vs \(H_1:\) negative interaction.
   - **Power/sample:** Humans N≈200 with within-subject manipulation typically detects d≈0.3; AI: deterministic evaluation with multiple seeds.

**Recommended study design (concrete):** A preregistered, multi-task evaluation using *procedurally generated* environments (to reduce memorization) plus a small fixed “benchmark-style” subset; apply a **measurement-invariance** framework so “generalization” is a comparable latent construct across humans and AI. Include controls for interface differences, prior exposure, and differential practice.

## Rationale

- **Psychometrics** operationalizes intelligence via the “positive manifold” and latent factors (historically \(g\)), implying that “intelligence” is at least partly a **measurement model** over task performance rather than a single mechanism. ([psychclassics.yorku.ca](https://psychclassics.yorku.ca/Spearman/chap5.htm?utm_source=openai))  
- **AI theory** has proposed explicitly formal, cross-environment definitions of machine intelligence (e.g., expected performance across computable environments), but these are typically idealized and motivate practical approximations/tests. ([vetta.org](https://www.vetta.org/documents/legg-hutter-2007-universal-intelligence.pdf?utm_source=openai))  
- **Universal / anytime testing proposals** aim to compare humans and machines on the **same scale**, aligning directly with the unification goal while highlighting interface and resource issues. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0004370210001554?utm_source=openai))  
- **Assumptions (explicit):**
  1. Procedural generation meaningfully reduces contamination/memorization relative to static benchmarks.
  2. A shared latent trait \(G^\*\) is identifiable despite differing implementations (brains vs silicon), consistent with Marr-style level-separation (functional similarity without mechanistic identity).
- **Alternative explanation 1 (training exposure masquerading as “generalization”):** AI OOD success might reflect broader pretraining coverage rather than a unified capability; predicts that stricter novelty/auditing will sharply reduce AI–human comparability and weaken factor stability (larger drop in \(\omega_h\) and \(\Delta R^2\) for AI only).  
- **Alternative explanation 2 (interface + tool scaffolding):** Apparent “general intelligence” could be driven by language interface fluency or tool access; predicts that removing language mediation (e.g., purely visuomotor tasks) will substantially change factor structure for LLM-agents but not for humans (lack of measurement invariance).  

If you want, I can convert this into a full preregistration-style protocol (task families, contamination audit rules, factor/IRT model specification, exclusion criteria, and a simulation-based power plan) while keeping the same core hypothesis.