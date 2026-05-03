## Experimental Design
**Goal:** Test whether an **adaptability construct**—operationalized as *learning dynamics under feedback on procedurally novel tasks*—better predicts **held-out cross-domain performance** than static, one-shot accuracy, and whether that construct is **partly measurement-invariant** across **humans vs contemporary AI agents**.

**Core design:** A shared **human–AI task battery** with (i) **procedurally generated** tasks to reduce memorization/leakage, (ii) **multiple feedback trials** per task to measure within-task learning, and (iii) a **held-out transfer set** generated from new seeds/rule-parameters. Procedural generation is explicitly motivated by RL generalization work (e.g., Procgen) and is used here to define a preregistered “environment distribution.” ([openai.com](https://openai.com/research/procgen-benchmark?utm_source=openai))

**Structure**
- **Populations (between):**
  - Humans: online adult participants.
  - AI agents: a preregistered set of ≥25 agents spanning LLM-based agents, RL policies, and (optionally) symbolic baselines.
- **Resource-boundedness (between, randomized for humans; manipulated for AI):**
  - Humans: time pressure vs no time pressure.
  - AI: constrained context/tool budget vs unconstrained (plus fixed “prompting protocol”).
- **Tasks (within):** 60 training tasks (5 trials each) + 20 held-out transfer tasks (1–3 trials each; minimal adaptation allowed, depending on condition).
- **Domains (within; 5 domains × 12 tasks each):**
  1) Rule induction / concept learning (feedback-based classification)
  2) Planning in small MDPs / gridworlds (goal achievement under changing rules/costs)
  3) Partial observability & memory (sequence and delayed-information tasks; inspired by PsychLab-style cognitive tasks and memory suites) ([deepmind.google](https://deepmind.google/blog/open-sourcing-psychlab?utm_source=openai))  
  4) Causal inference / intervention selection (learn causal structure from feedback)
  5) Social inference (learn opponent/partner type in iterated games)

**Primary hypothesis test (humans and AI separately, then jointly):**
- Incremental validity: does **adaptability** explain **held-out transfer** beyond **static trial-1 performance** (ΔR²; β_adapt > 0)?
- Unification probe: multi-group latent model (humans vs AI) testing partial **metric invariance** on domain-specific adaptability indicators.

## Procedure
1. **Preregistration**
   - Publish: task generators (high-level spec), scoring rules, exclusion criteria, analysis plan, and the exact AI prompting/evaluation protocol (including how feedback is formatted).
   - Freeze: the list of AI agents and versions (including release date / checkpoint hashes where possible).

2. **Task battery implementation**
   - Build each task as a **generator** `G(seed, params) -> (instructions, observations, scoring, feedback)` with:
     - **Secret seeds** (never published) for the held-out transfer set.
     - **Public seeds** (published after study) for reproducibility of training-set tasks.
   - Feedback channel standardized as: `{correct/incorrect or reward, brief explanation allowed?, next-trial observation}`.

3. **Human session (≈60–75 minutes total)**
   - Consent, demographics, brief tutorial with 2–3 practice tasks (not used in scoring).
   - Complete 60 tasks, each with **5 feedback trials**:
     - Trial: participant responds → immediate feedback → next trial.
   - Complete 20 held-out tasks (new generators/params), with limited trials (e.g., 1–3).
   - Resource condition:
     - **Time pressure** group: strict per-trial deadline (calibrated in pilot).
     - **No pressure** group: generous time window.

4. **AI evaluation runs**
   - For each agent:
     - Run the exact same 60×5 training trials and 20 held-out tasks.
     - Enforce resource condition:
       - **Constrained:** limited context window (history truncation), limited tool calls, and/or token budget.
       - **Unconstrained:** full allowed budget (still fixed and preregistered).
   - To address prompt sensitivity highlighted in holistic evaluation work, use a **structured, preregistered prompting template** and run **K prompt-variants** (e.g., K=3) as a robustness check, averaging performance (or modeling prompt as a random effect). ([crfm.stanford.edu](https://crfm.stanford.edu/2022/11/17/helm.html?utm_source=openai))

5. **Data freeze and analysis**
   - Lock raw logs and compute primary outcomes exactly as preregistered.
   - Run confirmatory models first (primary), exploratory second (clearly labeled).

## Controls
**Anti-leakage / anti-memorization**
- Procedural generation with **secret held-out seeds**; regenerate transfer tasks post hoc to test for contamination signatures (e.g., high trial-1 but near-zero learning). (Procedural generation rationale aligns with Procgen’s generalization motivation.) ([openai.com](https://openai.com/research/procgen-benchmark?utm_source=openai))
- Use **algorithmically novel** rules (e.g., random Boolean feature maps, randomly composed operators) rather than natural-language trivia.

**Interface and information parity**
- Provide **isomorphic task information** to humans and AI:
  - If humans see a grid, AI receives a symbolic grid encoding with identical observables.
  - If AI receives text feedback, humans receive the same semantic feedback (not extra hints).

**Baseline / sanity checks**
- Include a small set of “easy” calibration items to confirm attention and comprehension.
- Include non-adaptive, one-shot items to quantify pure static competence.

**Confounds**
- Humans: control for age, education, and reading speed (short reading-speed measure).
- AI: record model family/type, context length, tool availability; treat as covariates or stratification variables.

## Materials
**Task infrastructure**
- Web-based experiment platform for humans (keyboard/mouse responses; RT logging).
- Identical task engine callable via API for AI agents (same scoring codepath).

**Task sources to adapt/inspire**
- **PsychLab** (cognitive-task-like environments) and related memory task suites for the memory/partial observability domain. ([deepmind.google](https://deepmind.google/blog/open-sourcing-psychlab?utm_source=openai))
- Optional: procedurally generated RL-style tasks (Procgen-style principles) as inspiration for diversity and generalization design. ([openai.com](https://openai.com/research/procgen-benchmark?utm_source=openai))

**AI execution harness**
- A runner that:
  - Standardizes message formatting and feedback.
  - Enforces context/tool/token budgets.
  - Logs full transcripts, actions, and token counts.

**Data storage**
- Versioned dataset store (immutable logs), with a public release plan after de-identification.

## Sample Size and Power
**Humans**
- Target **N = 300** (after exclusions) to detect **ΔR² ≈ 0.10** in a multiple regression with ~5 predictors at α=0.05 with ≥80% power (aligns with your planning numbers).
- Oversample to **N ≈ 340–360** to accommodate exclusions (failed attention/comprehension, extreme noncompliance).

**AI agents**
- Target **M ≥ 25** distinct agents.
- For each agent, run **S ≥ 5** stochastic replicates (different random seeds / prompt-variant index) to stabilize estimates and allow mixed-effects modeling.

**Task-level power**
- With 60 tasks × 5 trials, learning-curve estimates (slopes/AUC) gain precision; model tasks as random effects to generalize beyond the sampled generators.

## Randomization and Blinding
**Randomization**
- Humans:
  - Randomly assign resource condition (time pressure vs none), stratified by recruitment platform strata if needed.
  - Randomize task order per participant with constraints (balanced domain interleaving).
- AI:
  - Randomize seed order and prompt-variant order; keep fixed across agents for comparability (or counterbalance).

**Blinding**
- Human participants: blinded to hypotheses (told study is about “learning across tasks”).
- Analysts:
  - Primary analysis scripts written and hashed before seeing condition labels (label masking).
  - AI agent identities can be anonymized during primary statistical modeling to reduce motivated tweaking.

## Metrics
**Primary variables**
- **Static performance:** mean trial-1 score across the 60 tasks (z-scored within domain, then averaged).
- **Adaptability (per domain, per subject/agent):**
  - Learning **slope** across trials 1–5 (mixed-effects estimate or within-task regression, then aggregated).
  - **AUC improvement**: AUC(trials 1–5) − trial-1 (robust to nonlinearity).
- **Held-out transfer:** mean performance on 20 novel tasks (new generators/params).

**Primary statistical tests**
1. **Incremental validity (humans):**  
   `transfer ~ static + adaptability + covariates` → test β_adapt > 0 and ΔR².
2. **Incremental validity (AI):**  
   agent-level regression or rank correlation on residualized transfer (transfer ~ static).
3. **Measurement invariance / unification test:**  
   multi-group latent factor model with 5 domain indicators of adaptability:
   - Configural → metric invariance; accept “partial metric invariance” if most loadings match and fit degradation is small (preregister criterion).
4. **Resource-boundedness signature:**  
   mixed-effects: `performance ~ constraint * trial + (1|subject/agent) + (1|task)`; test interaction.

**Secondary metrics (diagnostics)**
- Response time (humans), token usage and tool calls (AI), calibration (confidence vs accuracy if elicited), and reliability (test–retest subset on a second day).

## Data Collection
**Human logs**
- Trial-by-trial: stimulus/observation, response, correctness/reward, timestamp, RT.
- Device metadata (browser type, screen size) for QA.

**AI logs**
- Full transcripts/prompts/feedback, chosen actions, intermediate tool outputs, token counts, latency.
- Seed IDs and prompt-variant IDs.

**Quality control**
- Predefined exclusions:
  - Humans: failed comprehension checks; excessively fast responding; patterned responding.
  - AI: runner failures; exceeding budgets; non-parseable outputs (counted as errors if persistent).

**Reproducibility package**
- After publication: release generators (minus secret seeds), scoring code, analysis scripts, and de-identified data where allowed.

## Ethical and Practical Considerations
**Human subjects**
- Informed consent, right to withdraw, fair compensation, minimal deception (hypothesis masking only).
- Manage fatigue: allow breaks; keep session length bounded; pilot to calibrate time pressure.

**AI evaluation integrity**
- Avoid “benchmark gaming” by freezing prompts and budgets; document all deviations.
- Because AI evaluation outcomes are known to be sensitive to adaptation/prompting choices, transparently report all prompting templates and robustness runs (aligned with holistic evaluation concerns). ([crfm.stanford.edu](https://crfm.stanford.edu/2022/11/17/helm.html?utm_source=openai))

**Philosophical scope management (precommitted)**
- This experiment targets **operational intelligence-as-adaptability-under-novelty** (performance-relevant competence), not consciousness/understanding claims.
- Interpret results as: evidence for or against a *candidate cross-disciplinary operational unifier* (adaptability), not as a complete theory of mind.

**Practical constraints**
- Building human–AI isomorphic tasks is the main engineering risk; mitigate by:
  - Designing tasks in a **symbolic/structured observation format** that can be rendered visually for humans.
  - Running a small pilot to ensure tasks are neither trivial nor impossible in 5 trials.

If you want, I can also provide (a) a concrete list of 60 task-generator specs (one paragraph each) and (b) a preregistration-ready analysis plan (models, contrasts, invariance steps, and decision thresholds).