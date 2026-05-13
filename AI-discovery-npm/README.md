# AI Discovery CLI

`AI Discovery CLI` is an npm/Node.js terminal interface for science workflows inspired by Codex-style slash commands and the local `EinsteinResearch.py` pipeline.

## Run

```powershell
npm start
```

One-shot examples:

```powershell
npm start -- "Can a new catalyst improve CO2 reduction yield?"
npm start -- /research "Can a new catalyst improve CO2 reduction yield?"
npm start -- /hypothesis "Can a new catalyst improve CO2 reduction yield?"
npm start -- /experiment "Design a controlled catalyst screening experiment"
npm start -- /writer "Draft a final-format paper from the current experiment"
```

Use `OPENAI_API_KEY` for live OpenAI Responses API generation. Without `OPENAI_API_KEY`, the CLI automatically uses deterministic dry-run output so the workflow still runs locally.

In interactive mode, typing any research question starts the end-to-end workflow:

```text
ai-discovery> Can a new catalyst improve CO2 reduction yield?
```

For each research workflow:

```text
ai-discovery> /hypothesis Can AI improve catalyst screening?
ai-discovery:hypothesis> expand with a stronger null hypothesis
ai-discovery:hypothesis> /exit
ai-discovery> /writer Draft the paper
ai-discovery:writer> rewrite the conclusion more carefully
```

The live literature-review stage uses the hosted Responses API web-search tool. Disable that stage's web-search tool with `--no-web-search` or `AI_DISCOVERY_DISABLE_WEB_SEARCH=1` when the prompt contains sensitive material or when hosted search is unavailable.

## Slash Commands

- `/research <question>` runs the full workflow: plan, literature review, hypothesis, experiment, experiment runner, data analysis, draft paper, technical review, final Markdown paper, and final LaTeX paper.
- Bare text also runs `/research`.
- `/hypothesis [question]` generates a falsifiable hypothesis package. In interactive mode, `/hypothesis` without a question prompts for one.
- `/experiment [brief]` creates an experiment design and saves runnable Node.js experiment code.
- `/writer [instructions]` writes a final-format paper from the current session artifacts.
- `/model [name]` shows or changes the model used by all science agents.
- `/status` shows model, mode, output path, artifacts, and token usage.
- `/new` starts a fresh science session.
- `/clear` clears the terminal view and resets visible session artifacts.
- `/history` lists completed commands.
- `/output [directory]` shows or changes the artifact output directory.
- `/quit` or `/exit` exits the CLI.

## Artifacts

Each session writes files under `ai_discovery_runs/run_<timestamp>/`:

Full `/research` workflow:

- `01_research_plan.md`
- `02_literature_review.md`
- `03_hypothesis.md`
- `04_experiment_design.md`
- `05_experiment_code.js`
- `06_experiment_run.json`
- `06_experiment_run.md`
- `07_data_analysis.md`
- `08_draft_paper.md`
- `09_technical_review.md`
- `10_final_paper.md`
- `10_final_paper.tex`
- `session.json`

Single-stage commands also write their focused artifacts:

- `01_hypothesis.md`
- `02_experiment_design.md`
- `02_experiment_code.js`
- `03_research_paper.md`
- `03_research_paper.tex`
- `session.json`

Generated experiment code is not executed automatically. The full workflow's experiment-runner stage uses deterministic synthetic data so the pipeline can proceed safely. Review generated code first, then run it in a controlled environment:

```powershell
node .\ai_discovery_runs\<run>\05_experiment_code.js
```

## Validation

```powershell
npm run check
```

Dry-run smoke check:

```powershell
npm start -- --dry-run "Can a new catalyst improve CO2 reduction yield?"
```
