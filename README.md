# AI-Discovery-Program
Einsteinian Labs helps researchers turn ideas into discovery by using end-to-end AI automation—from literature review to report generation—while keeping the process rigorous, measurable, and deeply human at its core

# Einstein Research Console

## Overview

`Vibe_researchv1a.py` is a multi-mode AI research assistant built on the OpenAI Agents SDK. It can:

- run a guided research pipeline from question to report
- search the web for background and supporting sources
- generate hypotheses and experiment designs
- run a prototype experiment or simulation with a code interpreter
- analyze results and produce a conclusion
- generate a LaTeX research report and optionally compile it to PDF
- launch a local web chat server for browser-based interaction
- launch a separate lab workflow through `Perplexity-search.py`

The script also includes model fallback logic, optional SQLAlchemy-backed session memory, ANSI-styled CLI menus, and helper commands for model switching and question suggestion.

## Main workflow

The core pipeline runs these stages in order:

1. Plan
2. Background Research
3. Hypothesis
4. Experiment Design
5. Experiment Run Output
6. Data Analysis
7. Conclusion
8. Search Plan
9. Search Sources
10. LaTeX Report

Outputs can be saved to a timestamped run directory, and the final LaTeX report can also be converted into an academic PDF.

## Features

### 1. Interactive research pipeline

Interactive mode prompts you for a research question and optional experiment data or a data-file path. It then walks through the pipeline step by step, pausing between stages so you can review or stop.

Helpful commands in interactive mode:

- `/model` - show the current model and recommended models
- `/model <name>` - switch models
- `/suggest <partial>` - ask the agent to complete a partial research question
- `/quit` - exit

### 2. Automated pipeline mode

Auto mode runs the same pipeline non-interactively from command-line arguments. This is the best choice for repeatable runs, scripts, or batch use.

### 3. LaTeX and PDF generation

The pipeline generates a LaTeX report, validates and fixes citations if needed, saves the `.tex` output, and can compile it into an academic PDF. A standalone `latex2pdf` mode is also provided for converting an existing `.tex` file.

### 4. Local web chat server

Serve mode starts a local HTTP server that serves `index.html` and exposes a chat API at `/api/chat`. It also provides a `/health` endpoint.

### 5. Lab research launcher

Lab mode launches an external script named `Perplexity-search.py`. This makes the console extensible for a separate search-oriented lab workflow.

## Requirements

### Python packages

Install the core dependencies used by the script:

```bash
pip install openai openai-agents pydantic
```

Optional memory support:

```bash
pip install sqlalchemy aiosqlite
```

### External requirements

For PDF compilation, install at least one of these TeX tools:

- `tectonic`
- `latexmk`
- `pdflatex`

### Files expected by some modes

- `index.html` for web server mode
- `Perplexity-search.py` for lab mode

## How to run

### Show the startup menu

If you run the script without a subcommand, it opens the interactive startup menu:

```bash
python Vibe_researchv1a.py
```

From the menu you can choose:

- `1` Core Research Pipeline
- `2` Lab Research (Perplexity Search)
- `3` Web Chat Server
- `0` Exit

You can also switch models from the menu with:

```text
/model gpt-5.2-pro
```

### Run interactive mode directly

```bash
python Vibe_researchv1a.py interactive
```

Save outputs and choose a model:

```bash
python Vibe_researchv1a.py --save outputs --model gpt-5.2 interactive
```

### Run automated mode

With an inline question only:

```bash
python Vibe_researchv1a.py auto --question "Does retrieval augmentation improve factual accuracy in biotech QA systems?"
```

With inline data:

```bash
python Vibe_researchv1a.py auto \
  --question "Does retrieval augmentation improve factual accuracy in biotech QA systems?" \
  --data "sample_id,condition,score\n1,A,0.82\n2,B,0.76"
```

With a data file and saved outputs:

```bash
python Vibe_researchv1a.py --save outputs auto \
  --question "Does retrieval augmentation improve factual accuracy in biotech QA systems?" \
  --data-file ./data/results.csv
```

Pause after every stage:

```bash
python Vibe_researchv1a.py auto --question "Your question here" --pause
```

Skip PDF generation:

```bash
python Vibe_researchv1a.py --no-pdf auto --question "Your question here"
```

### Convert an existing LaTeX file to PDF

```bash
python Vibe_researchv1a.py latex2pdf --tex-file ./report.tex
```

Write the academic `.tex` and `.pdf` into a specific folder:

```bash
python Vibe_researchv1a.py latex2pdf --tex-file ./report.tex --output-dir ./compiled
```

### Run the web chat server

```bash
python Vibe_researchv1a.py serve
```

Custom host, port, and HTML entry file:

```bash
python Vibe_researchv1a.py serve --host 127.0.0.1 --port 8000 --index index.html
```

Then open the served page in your browser and use the backend chat endpoint:

- `GET /`
- `GET /health`
- `POST /api/chat`

Example JSON request for `/api/chat`:

```json
{
  "message": "Summarize the tradeoffs of wet-lab automation for biotech startups.",
  "history": [
    {"role": "user", "content": "I am researching biotech automation."},
    {"role": "assistant", "content": "Got it. What aspect are you exploring?"}
  ],
  "model": "gpt-5.2",
  "session_id": "demo_session_1"
}
```

### Run lab mode

```bash
python Vibe_researchv1a.py lab
```

This looks for and runs:

```text
Perplexity-search.py
```

If that file is missing, the lab launcher exits with an error message.

## Command-line options

### Global options

- `--save` - directory where pipeline outputs are saved
- `--model` - model used for pipeline and chat agents
- `--no-pdf` - skip LaTeX-to-PDF conversion

### Subcommands

- `interactive` - prompt-driven research run
- `lab` - launch the lab research script
- `auto` - run the pipeline with CLI inputs
- `latex2pdf` - convert `.tex` to academic `.pdf`
- `serve` - run the local web server

## Output files

When `--save` is used, the pipeline writes a timestamped run directory containing step outputs such as:

- `01_plan.md`
- `01b_background_research.md`
- `01b_background_sources.txt`
- `02_hypothesis.md`
- `03_experiment_design.md`
- `04_experiment_run.md`
- `05_data_analysis.md`
- `06_conclusion.md`
- `00_search_plan.md`
- `00_search_summaries.md`
- `00_sources.txt`
- `07_report.tex`

It also writes a timestamped LaTeX file in the current directory like:

```text
research_report_YYYYMMDD.HHMMSS.tex
```

If PDF conversion succeeds, the compiled academic PDF is saved next to the TeX file.

## Notes and behavior

- Default model: `gpt-5.2`
- Recommended models include `gpt-5.2`, `gpt-5.2-pro`, `gpt-5`, `gpt-5-mini`, and `gpt-5-nano`
- The script retries with fallback models on retryable API or timeout errors
- If no dataset is provided, the experiment runner can generate synthetic data and still produce a prototype analysis
- SQLAlchemy-backed session memory is optional and controlled through environment variables

## Example quick start

```bash
pip install openai openai-agents pydantic sqlalchemy aiosqlite
python Vibe_researchv1a.py --save outputs interactive
```

Enter your research question, optionally provide data, and review each pipeline stage as the system builds a structured report and LaTeX paper.
