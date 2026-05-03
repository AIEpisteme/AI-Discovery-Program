## Research workflow checklist (primary steps)
- **Clarify scope + deliverables:** define what “intelligence” must cover (human/animal/machine; individual vs collective; narrow vs general) and what counts as a “general theory.”
- **Build a cross-disciplinary definition map:** extract and compare operational definitions across neuroscience, cognitive science, psychology, CS/AI, and philosophy of mind.
- **Survey mechanisms + constraints:** compile mechanistic accounts of learning/reasoning/adaptation in brains and in AI systems, including limits and failure modes.
- **Compare competing theoretical frameworks:** computational, information-theoretic, dynamical/embodied, Bayesian/predictive, symbolic vs connectionist, etc.
- **Assess formalizability + measurement:** evaluate whether intelligence can be defined/measured/unified; audit existing metrics and propose evaluation criteria.
- **Synthesize into candidate unifying principles + open problems:** present what can be unified now vs what remains philosophically/empirically underdetermined.

---

## Detailed instructions for the researcher (write as if I’m directing the project)

### 1) Define scope, constraints, and “success criteria”
1. **State my target outcome** as: a rigorous scientific *and* philosophical investigation that ends with (a) a taxonomy of definitions, (b) a comparative analysis of mechanisms, (c) an evaluation of theories, and (d) a reasoned conclusion about formal definition/measurement/unification.
2. **Explicitly note open-ended dimensions** (no constraints were specified by me), and decide how you will handle them:
   - Biological scope: humans only vs animals vs general biological intelligence.
   - Artificial scope: current ML systems vs broader AI paradigms (symbolic, hybrid, evolutionary, neuromorphic).
   - Level of analysis: computational/algorithmic/implementational; individual vs social/collective intelligence.
   - Relationship to consciousness, intentionality, and understanding (include as separate modules so the core intelligence analysis doesn’t depend on controversial commitments).
3. **Create evaluation criteria** you will use consistently across disciplines, e.g.:
   - Operational clarity (measurable? falsifiable?).
   - Explanatory power (does it predict behavior/learning curves/generalization?).
   - Mechanistic grounding (links to neural circuits or algorithms).
   - Cross-domain generality (transfer, abstraction, planning).
   - Normative adequacy (rationality, optimality, bounded rationality).
   - Practical testability (benchmarks, tasks, neuro/behavioral experiments).

### 2) Collect a representative, primary-source literature set (cross-disciplinary)
1. **Prioritize primary sources**: seminal papers/books + recent review articles in top venues (Neuron, Nature Neuroscience, Trends in Cognitive Sciences, Psychological Review, Science, Nature, JMLR, NeurIPS/ICML proceedings, PhilMind/Nous, Stanford Encyclopedia of Philosophy entries as orientation but not as final authority).
2. **Time sensitivity:** because “AI” changes quickly, include **the most recent** surveys/position papers available **up to the present date (March 5, 2026)** and clearly label publication dates in the final write-up.
3. **Build an annotated bibliography** with 1–3 sentence notes per source: what definition of intelligence it assumes, what mechanism/theory it supports, and what evidence it uses.

### 3) Produce a “definition matrix” across disciplines (required table)
Create a table with at least these columns (expand as needed):

| Discipline | Definition of intelligence (verbatim/near-verbatim) | Type (descriptive / normative / operational) | Core capacities (learning, reasoning, etc.) | Level (computational/algorithmic/implementational) | Measurement implied | Key proponents / canonical sources | Main objections |
|---|---|---|---|---|---|---|---|

Instructions:
- Extract definitions from **neuroscience**, **cognitive science**, **psychology**, **computer science/AI**, and **philosophy of mind**.
- Identify **hidden assumptions** (e.g., internal representations, symbol manipulation, embodiment, goal-directedness).
- Mark where definitions are **family-resemblance** vs **necessary-and-sufficient**.

### 4) Map mechanisms enabling intelligence in biological vs artificial systems (required table)
Deliver two linked products:

**A) Mechanism map (table):**

| Capacity | Biological mechanisms (neural/cognitive) | Artificial mechanisms (algorithmic/architectural) | Evidence type | Strengths | Known limitations/failures |
|---|---|---|---|---|---|

Include at minimum: learning (supervised/unsupervised/ reinforcement), memory (working/episodic/semantic vs artificial memory), reasoning/inference, planning, abstraction/compositionality, generalization/transfer, exploration, metacognition/uncertainty, social cognition/communication.

**B) Explanatory alignment notes:**
- For each capacity, state whether the AI mechanism is **analogous**, **homologous**, or merely **functionally similar** to biological mechanisms, and justify the classification.

### 5) Compare competing theories/frameworks (required comparison table)
Construct a framework comparison table:

| Framework | Core claim about intelligence | Formalism (if any) | What it explains well | What it struggles with | Predictions / tests | Representative sources |
|---|---|---|---|---|---|---|

Frameworks to include (at least):
- **Computationalism / physical symbol system** traditions
- **Connectionism / neural computation**
- **Bayesian cognition / probabilistic inference**
- **Predictive processing / free-energy–style approaches**
- **Dynamical systems / enactivism / embodiment**
- **Information-theoretic perspectives** (e.g., compression, information bottlenecks, MDL-like ideas)
- **Rationality and bounded rationality** (incl. resource-rational views)
- **Evolutionary/ecological perspectives** (fitness, niche adaptation)
- **Philosophy of mind** positions relevant to AI: functionalism, behaviorism, representationalism, externalism; and the “understanding/semantics” critique traditions (treat separately from performance intelligence claims)

### 6) Address “can intelligence be formally defined?” with a structured argument
1. **Separate tasks**:
   - Formal definition of *intelligence* as a construct.
   - Formal definition of *general intelligence* vs *task competence*.
   - Formal definition of *agentic intelligence* (goal-directed) vs *non-agentic* problem-solving.
2. **Catalog candidate formalizations**, and for each:
   - State the mathematical object (function class, policy, objective, resource constraints).
   - Identify what it quantifies (performance, adaptability, sample efficiency, generalization, compression, etc.).
   - Note dependence on environment/task distribution and whether it avoids circularity.
3. **Include impossibility/limitation considerations**:
   - Underdetermination by behavior (multiple internal mechanisms yield same performance).
   - No-free-lunch style issues (dependence on task distribution).
   - Measurement validity pitfalls (Goodharting, benchmark overfitting).

### 7) Evaluate “can intelligence be measured?” (required metrics audit table)
Create a metrics audit:

| Measurement approach | What it measures | Domain (human/animal/AI) | Validity threats | Susceptible to gaming? | Cross-domain comparability | Key sources |
|---|---|---|---|---|---|---|

Include:
- Human psychometrics (g-factor tradition; cognitive batteries)
- Behavioral/ecological measures (adaptation in naturalistic tasks)
- AI benchmarks (task suites; generalization tests; robustness; out-of-distribution)
- Efficiency measures (sample efficiency, compute efficiency, energy efficiency)
- Uncertainty/calibration, interpretability proxies, reliability and safety-relevant competence measures

Require explicit discussion of:
- Construct validity (is it “intelligence” or “test-taking skill”?)
- External validity (real-world generalization)
- Normative vs descriptive goals (what should count as intelligence?)

### 8) Human cognition vs artificial systems: similarities, differences, and boundary claims
In a dedicated section, require the researcher to:
1. Compare **architectural constraints**:
   - Brains: noisy, energy-limited, embodied, evolved, developmentally staged learning.
   - AI: scalable compute, data regimes, brittle OOD behavior, modularity options, tool use.
2. Compare **learning regimes**:
   - Human: few-shot, curriculum, social learning, intrinsic motivation.
   - AI: large-scale pretraining, RL, self-supervision, tool-augmented reasoning.
3. Compare **representation and reasoning**:
   - Compositionality, abstraction, systematic generalization, causal reasoning.
4. Clearly distinguish:
   - **Behavioral equivalence** vs **mechanistic equivalence**
   - **Competence** vs **performance**
   - **Task intelligence** vs **agentic/general intelligence**

### 9) Synthesis: candidate unifying principles + a “what would count as a general theory?”
Ask the researcher to propose **2–4 candidate unifying principles** (clearly labeled as tentative), each with:
- Statement of the principle
- Scope conditions (where it applies)
- Formal sketch (if possible)
- Empirical predictions / discriminating tests
- Philosophical commitments (minimal vs substantial)

Also require a section: **“Criteria for a General Scientific Theory of Intelligence”**:
- What unification would mean (common variables? common mechanisms? common formalisms?)
- What would falsify it
- What data would be needed (neuro, behavioral, computational scaling, developmental)

### 10) Output format requirements (final deliverable structure)
In the final output, I want a **report** with these headers (in this order):
1. **Executive Summary** (key findings + bottom-line stance on definability/measurability/unification)
2. **Methodology** (how sources were chosen; evaluation criteria)
3. **Definitions Across Disciplines** (include the definition matrix table)
4. **Mechanisms of Learning/Reasoning/Adaptation** (include mechanism map table)
5. **Comparative Theory Evaluation** (include framework comparison table)
6. **Formal Definitions: Prospects and Limits**
7. **Measurement: Metrics, Validity, and Failure Modes** (include metrics audit table)
8. **Human vs AI: Convergences, Divergences, and Open Questions**
9. **Candidate Unifying Principles + Research Agenda**
10. **Annotated Bibliography** (primary sources first, then high-quality reviews)

### 11) Validation pass (required)
Before finalizing, instruct the researcher to run a checklist:
- Did I include all five disciplines explicitly (neuroscience, cognitive science, psychology, CS, philosophy of mind)?
- Did I treat **mechanisms** and **definitions** separately?
- Did I evaluate **competing theories** rather than presenting one?
- Did I answer the three core questions: **formal definition**, **measurement**, **unification**?
- Did I clearly label what is well-supported vs speculative?

If any of these are incomplete, add a “Clarifications Needed” subsection listing what to fill in next.