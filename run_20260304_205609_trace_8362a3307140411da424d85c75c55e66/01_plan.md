## Quick checklist (what I want you to do)
- Build a **cross-disciplinary map of definitions** of “intelligence” (neuroscience, cognitive science, psychology, CS/AI, philosophy of mind).
- Analyze **mechanisms** of learning, reasoning, adaptation, and problem-solving in **biological vs artificial** systems.
- Compare and evaluate **competing theories/frameworks** (computational, information-theoretic, dynamical/enactive, philosophical).
- Assess whether intelligence can be **formally defined**, **measured**, and/or **unified** under a general scientific theory.
- Produce a **structured report + comparison tables + argument matrix + annotated bibliography** grounded primarily in **primary sources**.

---

## Deliverable format I want (final output structure)
Please produce a single, rigorous report in markdown with the following required headers:

1. **Abstract** (150–250 words)  
2. **Executive Summary** (key takeaways + where consensus vs disagreement lies)  
3. **Research Design & Methods** (how you selected sources and evaluated claims)  
4. **Definitions of Intelligence Across Disciplines**  
5. **Mechanisms of Intelligence in Biological Systems**  
6. **Mechanisms of Intelligence in Artificial Systems**  
7. **Competing Theories & Frameworks (Comparative Evaluation)**  
8. **Formalization & Measurement: Can Intelligence Be Defined/Measured/Unified?**  
9. **Human vs AI: Similarities, Differences, and Limits of Comparison**  
10. **Candidate Unifying Principles (or reasons unification may fail)**  
11. **Philosophical Implications (mind, meaning, understanding, consciousness)**  
12. **Open Problems & Research Agenda**  
13. **Annotated Bibliography** (primary sources prioritized)

### Tables I want included (required)
- **Table A — Definitions Matrix:** rows = disciplines/authors; columns = definition, key criteria, what’s excluded, operationalization/measurement, major critiques.
- **Table B — Mechanisms Comparison:** biological vs artificial (learning, memory, generalization, reasoning, planning, abstraction, embodiment, social cognition, etc.).
- **Table C — Theory/Framework Scorecard:** frameworks vs evaluation criteria (explanatory scope, predictive power, formal clarity, empirical support, computability, alignment with neuroscience, etc.).
- **Table D — Measurement & Benchmarks:** human psychometrics + animal cognition + AI benchmarks, what they measure, failure modes, Goodhart risks.
- **Table E — Argument Matrix:** major claims (rows) × pro/con arguments + best supporting citations (columns).
- **Table F — Research Tracking Plan:** tasks, subtasks, target sources, dates (relative is fine), status.

---

## 1) Scope control (what you must clarify up front)
Because the prompt is broad, start by explicitly stating which dimensions are **open-ended** unless I specify otherwise:
- **Time horizon:** include classic foundations + modern AI (especially deep learning and post-2020 work). If you include “most recent,” verify what counts as *current as of March 5, 2026* rather than assuming.
- **Type of intelligence:** human-only vs animal vs machine; individual vs collective; narrow vs general; embodied vs disembodied.
- **Level of analysis:** computational/algorithmic/implementational (e.g., Marr) vs phenomenology vs social/behavioral.
- **Normative vs descriptive:** what intelligence *is* vs what we *value* as intelligent behavior.

If any of these need a boundary to keep the project manageable, propose 2–3 “scope options” (narrow / standard / expansive) and proceed with the standard option unless I later constrain it.

---

## 2) Research design & standards of rigor (how I want you to evaluate everything)
### Evidence hierarchy (prioritize in this order)
1. **Primary scientific sources**: peer-reviewed neuroscience/cog-sci/psych papers, computational learning theory, information theory, core AI papers.
2. **Primary philosophy sources**: classic texts and leading journal articles.
3. **High-quality syntheses**: handbooks, review articles, major academic monographs.
4. **Avoid** blog/aggregator summaries unless used only to locate primary sources.

### Evaluation criteria (apply consistently)
For each definition/theory, explicitly judge:
- **Clarity** (are terms operational or metaphorical?)
- **Explanatory scope** (what phenomena it covers)
- **Predictive/empirical adequacy** (testable predictions; evidence quality)
- **Mechanistic depth** (does it specify mechanisms vs labels?)
- **Cross-level coherence** (brain ↔ cognition ↔ behavior; algorithm ↔ implementation)
- **Comparative adequacy** (humans, animals, AI systems)
- **Failure modes** (edge cases, counterexamples, Goodharting)

I want you to be explicit about when you are:
- summarizing consensus,
- reporting contested debates,
- making your own synthesis/inference.

---

## 3) Build a taxonomy of “intelligence” (so definitions are comparable)
Before surveying disciplines, construct a shared “comparison vocabulary” that you’ll reuse throughout:
- **Core capacities:** perception, representation, prediction, learning, memory, attention, abstraction, compositionality, reasoning, planning, problem-solving, communication, social cognition, metacognition.
- **Performance properties:** generalization, transfer, robustness, sample efficiency, compute/energy efficiency, adaptability under distribution shift, exploration, creativity/novelty, goal-directedness.
- **Constraints:** embodiment, resource bounds, real-time control, developmental learning, cultural scaffolding.
- **Normative components:** rationality, optimality, coherence, alignment with human values.

Then define “intelligence” as a **cluster concept** initially (working definition), and later test whether the cluster can be reduced to a more formal unified definition.

---

## 4) Discipline-by-discipline investigation plan (what to extract from each field)
### A) Neuroscience
I want you to extract:
- Candidate neural mechanisms enabling intelligent behavior (learning rules, plasticity, neuromodulation, predictive coding, hippocampal memory systems, prefrontal control, etc.).
- What neuroscience treats as “intelligence” vs “cognition” vs “executive function.”
- How constraints (metabolic cost, wiring, noise, embodiment) shape intelligence.

**Output requirement:** a subsection that translates neural claims into computational/algorithmic statements (and notes where translation fails).

### B) Cognitive science
Extract:
- Representational vs dynamical/enactive approaches.
- Compositionality, systematicity, symbol grounding debates.
- Cognitive architectures (if used) and what they claim about generality.

### C) Psychology (incl. psychometrics)
Extract:
- Competing models of human intelligence (e.g., g factor, multiple intelligences, etc.) and **what is actually measured**.
- Validity, reliability, bias/fairness, and the link between test scores and real-world adaptive success.
- How “intelligence” relates to executive function, working memory, and learning.

**Output requirement:** connect measurement constructs to mechanisms (where possible) and flag gaps.

### D) Computer science / AI
Extract:
- Definitions used in AI (agentic goal achievement, generalization, capability sets).
- Mechanisms: supervised/self-supervised learning, reinforcement learning, planning, search, probabilistic inference, representation learning, tool use, memory, etc.
- Distinctions: narrow vs general, symbolic vs connectionist, hybrid systems, embodied AI.

**Output requirement:** identify where “intelligence” is treated as (i) benchmark performance, (ii) general capability, (iii) efficient learning, or (iv) something else.

### E) Philosophy of mind
Extract:
- Competing views: computationalism, functionalism, anti-functionalism, embodied/enactive mind, externalism, etc.
- Intentionality, meaning/understanding, consciousness (only insofar as it bears on “intelligence”).
- Key conceptual pitfalls: behavioral vs internal criteria; semantics vs syntax; necessary vs sufficient conditions.

**Output requirement:** an explicit “conceptual audit” of hidden assumptions in scientific definitions.

---

## 5) Mechanisms comparison (bio vs artificial) — how I want it analyzed
For each capacity (learning, reasoning, adaptation, problem-solving), I want you to do:
1. **Mechanistic description** in biology (neural circuits/systems level where possible).
2. **Mechanistic description** in AI (algorithms + training dynamics + architecture).
3. **Computational equivalence vs difference:** what is genuinely analogous vs superficially similar.
4. **Constraints comparison:** data, compute, energy, embodiment, developmental time, safety constraints.
5. **Generalization and failure cases:** adversarial brittleness, hallucinations, confabulation, out-of-distribution failures, cognitive biases.

This must feed directly into **Table B (Mechanisms Comparison)**.

---

## 6) Competing theories/frameworks to evaluate (minimum set)
I want you to include, at minimum, representative theories from each category below (choose leading sources; justify inclusion/exclusion):

### Computational / algorithmic perspectives
- Intelligence as **efficient learning**, **compression**, **prediction**, **planning**, **control**, or **search**.
- Computational learning theory perspectives (PAC, sample complexity, generalization bounds—only if you can connect them to “intelligence” claims).

### Information-theoretic perspectives
- Formal measures that might ground intelligence (entropy, mutual information, information bottleneck, predictive information, empowerment, minimum description length, etc.).
- Critiques: what information measures capture vs miss (semantics, goals, embodiment).

### Dynamical systems / enactivism / embodiment
- Intelligence as emergent from brain-body-environment coupling; critique of representation-heavy accounts.

### Philosophical frameworks
- Functionalism, computationalism, anti-computational arguments, Chinese Room-style concerns (in a careful, non-caricatured way).
- Clarify whether the framework targets **intelligence**, **understanding**, or **consciousness**—and keep them distinct.

**Output requirement:** Use **Table C (Theory Scorecard)** + **Table E (Argument Matrix)** so readers can see exactly why one framework does/doesn’t support unification.

---

## 7) Formal definition + measurement: the core “unification” test
I want you to explicitly test three hypotheses:

### H1: Intelligence can be formally defined (necessary/sufficient conditions)
- Attempt candidate formalizations (agent performance across tasks, expected utility under resource bounds, sample-efficient generalization, compression/prediction competence, etc.).
- Stress-test with counterexamples: narrow savants, benchmark overfitting, tool-augmented agents, socially scaffolded intelligence, etc.

### H2: Intelligence can be measured robustly
- Compare human psychometrics, animal cognition paradigms, and AI benchmarks.
- Include measurement pathologies: Goodhart’s law, proxy collapse, distribution shift, training contamination, construct validity problems.

### H3: Intelligence can be unified under a general scientific theory
- Identify what a “general theory” would need: primitives, laws/regularities, bridging principles across levels (neural/algorithmic/behavioral), and falsifiable predictions.

**Output requirement:** conclude with a “unification verdict” section that is nuanced (e.g., partial unification possible; or unification depends on which concept of intelligence we mean).

---

## 8) Human vs AI comparison (avoid category errors)
I want you to:
- Separate **competence** (what a system can do) from **process** (how it does it) and from **phenomenology** (what it’s like, if anything).
- Identify which comparisons are legitimate (e.g., functional/behavioral) and which require extra assumptions (e.g., semantics/understanding).
- Discuss “generalization” in humans vs AI: few-shot learning, transfer, causal reasoning, compositional generalization, robustness.
- Address social and developmental aspects: learning from culture, instruction, norms, and long-horizon goals.

This must feed into **Table B** and a dedicated narrative section.

---

## 9) Source collection plan (what I want you to gather)
### Minimum source set
- **Foundational classics** (discipline-specific “anchor” texts/papers).
- **A curated set of modern primary research** (include post-2015 and post-2020 developments where relevant).
- **A small number of integrative handbooks/reviews** to triangulate.

### For every source in the annotated bibliography, include
- Full citation
- 2–3 sentence summary of the claim
- What definition of intelligence it implies/assumes
- Evidence type (theory / experiment / simulation / argument)
- Key limitations and critiques
- How it contributes to (or challenges) unification

---

## 10) Writing and synthesis requirements (so the output is genuinely “investigative”)
- Use **clear, stable terminology**: define intelligence vs cognition vs rationality vs consciousness.
- Keep a running list of **disagreements** and what would resolve them (new experiments? better benchmarks? conceptual clarification?).
- End with **testable predictions / empirical discriminators** where possible (even in philosophy-adjacent debates).
- Include a **research agenda**: 5–10 concrete open problems, each with suggested methods and what success would look like.

---

## 11) Project management (how I want you to execute and present progress)
Create **Table F (Research Tracking Plan)** with:
- Workstream (definitions / biology / AI / philosophy / measurement / synthesis)
- Concrete tasks
- Target sources to locate
- Planned completion date (relative is OK)
- Status + notes/risks

If time is limited, propose a staged plan:
- Stage 1: definitions + taxonomy + preliminary matrices  
- Stage 2: deep dive mechanisms + theory scorecard  
- Stage 3: unification analysis + final synthesis  

---

## 12) Final validation (self-check before you deliver)
Before finalizing, verify explicitly that you have:
- Covered definitions in **neuroscience, cognitive science, psychology, computer science, philosophy of mind**.
- Analyzed mechanisms for **learning, reasoning, adaptation, problem-solving** in both biological and artificial systems.
- Evaluated **computational**, **information-theoretic**, and **philosophical** theories (at least one strong representative of each).
- Addressed whether intelligence can be **defined**, **measured**, and **unified**, with clear arguments and counterarguments.
- Included all required tables (A–F) and an annotated bibliography emphasizing primary sources.

If any item is missing, add a “To complete” note listing what remains.