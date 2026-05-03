## Primary Hypothesis

Across human participants and contemporary AI agents, a latent **adaptability** construct operationalized as *learning rate and transfer on procedurally novel tasks with feedback* predicts cross-domain held-out task performance better than static, single-shot accuracy measures, indicating a partially unifiable operational notion of “intelligence” grounded in goal-achievement under novelty.

## Null Hypothesis

After controlling for static task performance, **adaptability has no incremental predictive validity** for held-out cross-domain performance (i.e., regression coefficient(s) for adaptability = 0 and ΔR² = 0), and any latent factors are not measurement-invariant across humans vs AI.

## Measurable Predictions

1) **Human incremental validity of adaptability**
- **IV:** Adaptability score = mean within-person slope of performance over 5 feedback trials per task across 40 procedurally generated tasks (standardized within domain).  
- **DV:** Held-out transfer performance = mean accuracy/reward on 20 novel tasks (new generators/parameters).  
- **Expected effect:** ΔR² ≈ 0.08–0.15 beyond first-trial (static) performance.  
- **Test:** Multiple regression with covariates: static score, age, education; **H0:** β_adapt = 0; **H1:** β_adapt > 0.  
- **Power / N:** For detecting ΔR² = 0.10 at α=0.05 with ~5 predictors, target **N ≈ 250–300** humans (80%+ power).

2) **AI incremental validity of adaptability**
- **IV:** Same adaptability score computed for each AI agent (e.g., 20–30 diverse models/agents; fixed tool budget).  
- **DV:** Held-out transfer performance on the same 20 novel tasks.  
- **Expected effect:** ΔR² ≈ 0.15+ beyond static score (larger than humans if models vary widely in in-context adaptation).  
- **Test:** Agent-level regression or Spearman rank correlation on residualized transfer (transfer ~ static); **H0:** ρ = 0 (or β_adapt = 0); **H1:** ρ > 0.  
- **Power / N:** With **M ≥ 25 agents**, detectable ρ≈0.5 with ~80% power; fewer agents yields low power, so preregister **M ≥ 25**.

3) **Cross-population measurement invariance (unification test)**
- **IVs:** Domain-specific adaptability indicators (reasoning, planning, memory, causal inference, social inference; each as slope/AUC).  
- **DV:** Latent factor model fit across groups (humans vs AI).  
- **Expected effect:** **Partial metric invariance** (most factor loadings equal; some intercepts differ).  
- **Test:** Multi-group CFA comparing (i) configural vs (ii) metric-invariant models; **H0:** ΔCFI ≤ 0.01 fails (i.e., invariance rejected); **H1:** ΔCFI ≤ 0.01 holds for ≥70% loadings.  
- **Power / N:** Humans N≈300; AI agents M≈25; tasks provide repeated indicators improving precision.

4) **Resource-boundedness reveals distinct signatures**
- **IV:** Resource constraint manipulation: humans (time pressure vs none); AI (context length/tool-call budget reduced vs full).  
- **DV:** Change in adaptability and transfer (difference scores).  
- **Expected effect:** Under constraint, adaptability decreases less steeply than static performance (i.e., adaptability is more robust), with interaction d≈0.3–0.5.  
- **Test:** Mixed-effects model: performance ~ constraint * trial + (1|agent) + (1|task); **H0:** interaction = 0; **H1:** interaction ≠ 0.  
- **Power / N:** With 60 tasks × repeated trials, mixed-model power largely task-driven; preregister at least **60 tasks**.

## Rationale

- Psychometrics and cognitive science converge on intelligence involving **understanding complex ideas, adapting effectively, learning from experience, and reasoning**—all closely aligned to measurable *adaptation under novelty* rather than one-shot test taking. ([mun.ca](https://www.mun.ca/biology/scarr/APA%201985%20Intelligence%20-%20Knowns%20and%20Unknowns.pdf))
- A prominent AI-theoretic synthesis defines intelligence as **goal achievement across a wide range of environments**, explicitly emphasizing breadth and adaptation; this motivates measuring *transfer under changing task distributions* as central. ([ar5iv.org](https://ar5iv.org/pdf/0712.3329))
- Any putatively “general” measure must grapple with environment/task-distribution dependence; **No-Free-Lunch** results imply that superiority “in general” is ill-posed without specifying a distribution, so adaptability should be evaluated on preregistered environment generators rather than fixed benchmarks. ([victoryepes.blogs.upv.es](https://victoryepes.blogs.upv.es/wp-content/uploads/2020/10/No-free-lunch.pdf))
- Modern AI evaluation work highlights that results are sensitive to prompting/adaptation details and that models differ in how they exploit evaluation setups—supporting a design that explicitly measures *learning dynamics* (slopes/AUC), not just endpoint accuracy. ([friedeggs.github.io](https://friedeggs.github.io/files/helm.pdf))
- **Assumptions (explicit):** (i) “Intelligence” here is scoped to *performance-relevant cognitive/agentic competence* (not consciousness/semantics); (ii) procedural generation reduces leakage; (iii) trial-by-trial feedback is comparable across humans and AI (same information content).
- **Alternative explanations & discriminating predictions:**
  1) *Language proficiency / interface effects* (not intelligence) drive results: predicts strong group differences concentrated in verbal tasks; invariance fails specifically for nonverbal/causal tasks (preplanned subgroup CFA).  
  2) *Data contamination / memorization* in AI: predicts high static (trial-1) scores but **near-zero learning slopes** on truly novel procedural tasks; adaptability loses predictive power when tasks are regenerated with secret seeds.  

Recommended design (concise): preregister a **shared human–AI task battery** with procedurally generated environments, fixed feedback channels, strong anti-leakage controls (secret seeds; held-out generators), and a mixed-effects analysis plan to mitigate task/agent heterogeneity and benchmark gaming.