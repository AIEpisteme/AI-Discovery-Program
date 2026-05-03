## Research workflow checklist (high-level)
- **Define scope & deliverable** (audience, length, “intelligence” vs “AI capability,” include/exclude consciousness).
- **Build a cross-disciplinary definition map** (neuroscience, cognitive science, psychology/psychometrics, CS/AI, philosophy of mind).
- **Catalogue mechanisms** of learning/reasoning/adaptation in biological vs artificial systems at multiple levels of analysis.
- **Evaluate competing theories** using explicit criteria (explanatory power, formalizability, measurability, unification).
- **Compare measurement approaches** (IQ/g, cognitive tasks, AI benchmarks, formal measures like Legg–Hutter).
- **Synthesize toward (or against) a general theory** and identify irreducible pluralism vs possible unifiers.
- **Produce an annotated bibliography + comparison tables** with primary sources and key disputes.

---

# Detailed instructions for the researcher (first-person perspective)

## 1) Clarify scope, definitions, and success criteria (before reading deeply)
1. **State my intended deliverable format** (report/essay/whitepaper) and constraints that are currently unspecified:
   - Target **length** (open-ended unless I specify).
   - Target **audience** (specialist vs generalist; open-ended unless I specify).
   - Depth: conceptual overview vs technical detail (open-ended).
   - Whether to cover **consciousness/phenomenology** as part of “intelligence” (open-ended, but I should at least address why it is included/excluded).
   - Whether to treat “AI” as **current ML systems** (deep learning/transformers/RL), **classical GOFAI**, and/or **theoretical agents** (e.g., AIXI-style idealizations). If not specified, cover all three distinctly.
2. **Create a working glossary** with operational definitions for:
   - Intelligence, cognition, rationality, reasoning, learning, generalization, adaptation, agency, autonomy, understanding, representation, abstraction, planning.
3. **Commit to a multi-level analysis framework** to keep disciplines commensurable:
   - Use something like **Marr’s levels** (computational / algorithmic / implementational) or an equivalent framework and explicitly map each discipline’s claims onto these levels.

**Output requirement:** include a short “Scope & assumptions” section up front listing all open-ended choices and how I resolved them (or leave them explicitly unresolved if I choose breadth).

---

## 2) Build a cross-disciplinary “definition map” of intelligence
1. **Collect definitions** of intelligence from each discipline, prioritizing:
   - **Primary sources** (seminal papers/books) and **high-quality review articles** in peer-reviewed venues.
   - For AI/CS: primary conference/journal sources (NeurIPS, ICML, ICLR, AAAI, JMLR, Nature/Science reviews where relevant).
   - For psychology: psychometrics textbooks/reviews; for neuroscience/cog sci: authoritative reviews and classic theory papers; for philosophy: major monographs and SEP-style reference entries (as orientation, not as sole authority).
2. **For each definition**, extract the same attributes so they can be compared:
   - What capacities are central (learning, reasoning, abstraction, transfer, planning, social cognition, language, etc.).
   - Whether intelligence is treated as **unitary** vs **plural** (e.g., general intelligence vs multiple intelligences).
   - Normative vs descriptive stance (what an agent *should* do vs what organisms *do*).
   - Individual vs collective intelligence; static trait vs dynamic process.
   - Whether embodiment, affect, and social context are essential or optional.
3. **Create a comparison table** (required) with columns like:
   - Discipline / Source / Definition (paraphrased) / Level (Marr) / Core mechanisms implied / Measurement approach implied / Key criticisms.

**Output requirement:** a “Definitions & Taxonomy” section with at least one table plus a narrative synthesis identifying convergences and persistent fault lines.

---

## 3) Mechanisms: how biological and artificial systems learn, reason, adapt, solve problems
### 3A) Biological mechanisms (neuroscience + cognitive science + psychology)
1. Organize by mechanistic level:
   - **Neural learning**: synaptic plasticity (Hebbian, STDP), neuromodulation, credit assignment hypotheses, hippocampal memory systems, cortical hierarchy, predictive processing candidates.
   - **Cognitive architecture**: working memory, attention, executive function, compositionality, concept learning, planning, cognitive control, developmental learning, metacognition.
   - **Behavioral/psychological**: reinforcement learning in animals, heuristics vs optimality, bounded rationality, expertise, transfer and generalization in humans.
2. Explicitly separate:
   - Mechanisms with strong empirical grounding vs speculative proposals.
   - What is known at “parts list” level vs what is known at “system-level computation” level.

### 3B) Artificial mechanisms (computer science + modern ML)
1. Cover at least these families distinctly:
   - **Symbolic/GOFAI**: search, logic, planning, production systems.
   - **Statistical ML**: supervised/unsupervised learning, representation learning.
   - **Deep learning**: gradient-based optimization, architectures (CNN/RNN/Transformers), attention, scaling behavior (describe carefully and cite).
   - **Reinforcement learning**: model-free/model-based, exploration, credit assignment, offline RL.
   - **Neuro-inspired / hybrid**: differentiable memory, world models, neurosymbolic methods.
2. For each family, extract:
   - What “learning” means (parameter fitting vs structure learning vs program induction).
   - How they represent knowledge (distributed vectors, explicit symbols, probabilistic programs, etc.).
   - How they generalize and where they fail (OOD generalization, brittleness, adversarial vulnerability, compositional generalization).

**Output requirement:** a “Mechanisms” section with two parallel subsections (Biological / Artificial) and a bridging subsection explicitly mapping analogies and disanalogies (e.g., gradient descent vs biological learning; attention in transformers vs cognitive attention—similarities/limits).

---

## 4) Competing theories to evaluate (scientific + philosophical)
### 4A) Computational and formal theories
1. Include and contrast:
   - Computationalism / physical symbol system hypothesis vs dynamical systems vs enactive/embodied accounts.
   - Bayesian cognition, predictive processing, free-energy style approaches (clearly distinguish broad Bayesianism from specific formal claims).
   - Information-theoretic perspectives: Shannon information, efficient coding, rate–distortion, predictive information.
   - Algorithmic information theory: Kolmogorov complexity perspectives; formal agent measures such as **Legg–Hutter universal intelligence** (if included, explain assumptions and critiques).
2. Require explicit discussion of:
   - What is being optimized (reward, prediction error, description length, free energy bound, etc.).
   - Whether the theory is **testable/falsifiable**, and what empirical signatures it predicts.

### 4B) Philosophical frameworks (philosophy of mind / epistemology)
1. Evaluate:
   - Functionalism, identity theory, eliminativism, representationalism.
   - Intentionality and the symbol grounding problem.
   - Arguments about “understanding” (e.g., Chinese Room-style concerns) and what they do/don’t show about intelligence.
   - Whether intelligence requires consciousness, and whether “phenomenal intelligence” is a coherent category.
2. Keep the philosophical analysis tethered to the research question:
   - I am investigating whether intelligence can be **defined, measured, unified**—so each philosophical view should be tested against those aims.

**Output requirement:** a “Theories & Frameworks” section with a matrix table comparing theories by: explananda covered, formalizability, measurability, scope (human/animal/AI), empirical support, major objections.

---

## 5) Measurement: can intelligence be formally defined and quantified?
1. Build a dedicated measurement chapter that treats “measurement” as multi-domain rather than single-score:
   - **Human psychometrics**: IQ, g factor, test validity, cultural/loadings critiques, what IQ does/doesn’t measure.
   - **Cognitive task batteries**: working memory, reasoning, planning tasks; construct validity issues.
   - **Animal cognition**: species-appropriate tasks and the interpretation challenge.
   - **AI evaluation**: benchmark design pitfalls (data contamination, narrowness, metric gaming), generalization measures, robustness, sample efficiency.
   - **Formal measures**: expected performance over task distributions; universal intelligence style proposals; MDL/information criteria; discussion of computability and practicality.
2. Require explicit criteria for “good measurement”:
   - Reliability, validity (construct/predictive), fairness, invariance across groups/domains, susceptibility to overfitting/gaming, and external ecological validity.

**Output requirement:** a table comparing measurement approaches (human vs AI vs formal) and a written position on whether a single scalar “intelligence” measure is coherent or necessarily plural.

---

## 6) Unification attempt: is there a general scientific theory of intelligence?
1. Create a synthesis section that attempts unification in **three passes**:
   - **Pass 1 (minimal unifier):** identify the weakest common principle that many accounts share (e.g., adaptive problem-solving under constraints).
   - **Pass 2 (formal unifier):** propose candidate formalizations (e.g., expected goal achievement across environments, compression/prediction, control/optimization) and test against counterexamples.
   - **Pass 3 (mechanistic unifier):** assess whether shared principles correspond to shared mechanisms (likely not fully) and what “multiple realizability” implies.
2. Explicitly address failure modes of unification:
   - Category error: mixing normative rationality with descriptive cognition.
   - Overgeneralization: definitions so broad they become vacuous.
   - Anthropocentrism vs “agent-agnostic” definitions.
3. End with a reasoned conclusion that is allowed to be pluralist:
   - “Unified theory is possible only at abstract level X” vs “intelligence is a cluster concept,” etc., with supporting arguments and citations.

**Output requirement:** a concluding section with (a) my best candidate definition(s), (b) what can be measured today, (c) what remains theoretically underdetermined.

---

## 7) Research method: ensure rigor and traceability
1. Use a **systematic search strategy** (even if not fully formal PRISMA):
   - Define keywords per discipline (e.g., “general intelligence,” “predictive processing,” “universal intelligence measure,” “bounded rationality,” “embodied cognition,” “information bottleneck,” “agent evaluation”).
   - Track inclusion/exclusion criteria: peer-reviewed, foundational works, major critiques, and the most recent high-quality surveys (verify up to **March 5, 2026**).
2. Keep a **source ledger** (required):
   - Citation, discipline, claim supported, evidence type (theoretical/empirical), and whether it’s contested.
3. Where disciplines disagree, present **paired citations** (pro and con) and identify what data or conceptual clarification would resolve the dispute.

**Output requirement:** include an annotated bibliography and a short “Disputes & Open Problems” section listing unresolved controversies and what would count as progress.

---

# Deliverable structure (required headers)
1. **Abstract**
2. **Scope, Assumptions, and Method**
3. **Definitions of Intelligence Across Disciplines** (with comparison table)
4. **Mechanisms in Biological Intelligence**
5. **Mechanisms in Artificial Intelligence**
6. **Competing Theories & Frameworks** (with theory matrix table)
7. **Measurement and Formalization**
8. **Human vs AI: Similarities, Differences, and Limits of Analogy**
9. **Toward a Unified Theory (or Case for Pluralism)**
10. **Open Problems and Research Agenda**
11. **Annotated Bibliography** (+ source ledger as appendix)

---

## Validation (self-check before finalizing)
- I included all requested disciplines (neuroscience, cognitive science, psychology, computer science, philosophy of mind).
- I addressed learning, reasoning, adaptation, and problem-solving mechanisms in both biological and artificial systems.
- I evaluated computational, information-theoretic, and philosophical frameworks with explicit criteria.
- I covered definability, measurability, and prospects for unification, with explicit attention to limitations.
- I used required tables (definitions comparison, theory matrix, measurement comparison) and provided an annotated bibliography/source ledger.