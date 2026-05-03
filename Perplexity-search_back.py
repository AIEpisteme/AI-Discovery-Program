from __future__ import annotations

import csv
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from perplexity import Perplexity

DEFAULT_MODEL = os.getenv("PERPLEXITY_MODEL", "sonar")
DEFAULT_MAX_RESULTS = int(os.getenv("PERPLEXITY_MAX_RESULTS", "5"))
DEFAULT_MAX_FILE_CHARS = int(os.getenv("PERPLEXITY_MAX_FILE_CHARS", "25000"))
PROMPT_PREFIX = ">"
ASCII_LOGO = r"""
  ____                 _            _ _ _         
 |  _ \ ___  ___  ___ | | ___  _ __(_) | |_ _   _ 
 | |_) / _ \/ __|/ _ \| |/ _ \| '__| | | __| | | |
 |  __/  __/\__ \ (_) | | (_) | |  | | | |_| |_| |
 |_|   \___||___/\___/|_|\___/|_|  |_|_|\__|\__, |
                                             |___/ 
"""

LATEX_ESCAPE_MAP: dict[str, str] = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


@dataclass
class SearchHit:
    title: str
    url: str
    snippet: str
    date: str | None = None
    last_updated: str | None = None


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        key = item.strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(item.strip())
    return out


def prompt_input(prompt: str = "") -> str:
    if prompt:
        return input(f"{PROMPT_PREFIX} {prompt} ").strip()
    return input(f"{PROMPT_PREFIX} ").strip()


def read_multiline_input(prompt: str, allow_empty: bool = False) -> str:
    print(prompt)
    print("Finish input with an empty line. Enter lines with '> '.")
    lines: list[str] = []
    while True:
        try:
            line = input(f"{PROMPT_PREFIX} ")
        except EOFError:
            break

        if line == "":
            if lines or allow_empty:
                break
            print("Please enter at least one line.")
            continue
        lines.append(line.rstrip())
    return "\n".join(lines).strip()


def parse_query_lines(raw_text: str) -> list[str]:
    queries: list[str] = []
    for line in raw_text.splitlines():
        cleaned = re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", line).strip()
        if cleaned:
            queries.append(cleaned)
    return _dedupe(queries)


def is_search_mode_unsupported_error(exc: Exception) -> bool:
    message = str(exc).lower()
    return "search_mode" in message and "not supported" in message


def yes_no(prompt: str, default: bool = True) -> bool:
    suffix = "[Y/n]" if default else "[y/N]"
    answer = prompt_input(f"{prompt} {suffix}:").lower()
    if not answer:
        return default
    return answer in {"y", "yes"}


def ask_int(prompt: str, default: int, minimum: int = 1, maximum: int = 50) -> int:
    raw = prompt_input(f"{prompt} [{default}]:")
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError:
        print(f"Invalid number. Using default {default}.")
        return default
    return max(minimum, min(maximum, value))


def choose_search_mode() -> str:
    options = {"1": "academic", "2": "web", "3": "sec"}
    print("Choose search mode: 1) academic  2) web  3) sec")
    choice = prompt_input("Mode [1]:") or "1"
    return options.get(choice, "academic")


def resolve_file_path(raw_path: str) -> Path:
    path = Path(raw_path.strip()).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    return path


def _read_text_with_limit(path: Path, max_chars: int = DEFAULT_MAX_FILE_CHARS) -> tuple[str, bool]:
    with path.open("r", encoding="utf-8", errors="replace") as file:
        text = file.read(max_chars + 1)
    truncated = len(text) > max_chars
    return (text[:max_chars] if truncated else text), truncated


def _summarize_delimited_file(path: Path, delimiter: str, preview_rows: int = 15) -> str:
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as file:
        reader = csv.reader(file, delimiter=delimiter)
        try:
            header = next(reader)
        except StopIteration:
            return f"Experiment file: {path}\nThe file is empty."

        rows: list[list[str]] = []
        scanned_rows = 0
        max_scan_rows = 50000
        for row in reader:
            scanned_rows += 1
            if len(rows) < preview_rows:
                rows.append(row)
            if scanned_rows >= max_scan_rows and len(rows) >= preview_rows:
                break

    format_name = "CSV" if delimiter == "," else "TSV"
    lines = [
        f"Experiment file: {path}",
        f"Detected format: {format_name}",
        f"Columns ({len(header)}): {', '.join(header) if header else '<none>'}",
        f"Rows scanned (excluding header): {scanned_rows}",
        "Preview rows:",
    ]
    if rows:
        for i, row in enumerate(rows, start=1):
            row_text = " | ".join(cell.strip() for cell in row)
            if len(row_text) > 400:
                row_text = row_text[:400] + "..."
            lines.append(f"{i}. {row_text}")
    else:
        lines.append("<no rows>")
    if scanned_rows >= max_scan_rows:
        lines.append("Note: Row scanning was capped at 50,000 rows for speed.")
    return "\n".join(lines)


def _summarize_json_file(path: Path, max_chars: int = DEFAULT_MAX_FILE_CHARS) -> str:
    text, truncated_input = _read_text_with_limit(path, max_chars=max_chars * 2)
    try:
        data = json.loads(text)
        rendered = json.dumps(data, indent=2)
    except json.JSONDecodeError:
        rendered = text

    truncated_output = len(rendered) > max_chars
    if truncated_output:
        rendered = rendered[:max_chars]

    lines = [
        f"Experiment file: {path}",
        "Detected format: JSON",
        "Content preview:",
        rendered.strip(),
    ]
    if truncated_input or truncated_output:
        lines.append(f"Note: JSON preview truncated to {max_chars} characters.")
    return "\n".join(lines).strip()


def load_experiment_file_context(raw_path: str) -> str:
    path = resolve_file_path(raw_path)
    if not path.exists():
        raise OSError(f"File not found: {path}")
    if not path.is_file():
        raise OSError(f"Not a file: {path}")

    suffix = path.suffix.lower()
    if suffix in {".csv", ".tsv"}:
        delimiter = "," if suffix == ".csv" else "\t"
        return _summarize_delimited_file(path, delimiter=delimiter)
    if suffix == ".json":
        return _summarize_json_file(path)

    text, truncated = _read_text_with_limit(path, max_chars=DEFAULT_MAX_FILE_CHARS)
    lines = [
        f"Experiment file: {path}",
        f"Detected format: {suffix.lstrip('.') or 'text'}",
        "Content preview:",
        text.strip(),
    ]
    if truncated:
        lines.append(f"Note: File content truncated to {DEFAULT_MAX_FILE_CHARS} characters.")
    return "\n".join(lines).strip()


def collect_experiment_data_context() -> str:
    print("Choose experiment data input: 1) Load from file  2) Paste text")
    choice = prompt_input("Data source [1]:") or "1"

    if choice == "2":
        return read_multiline_input(
            "Paste data, summary statistics, or CSV snippet for analysis (multi-line):"
        )

    file_path = prompt_input("Experiment data file path:")
    if not file_path:
        print("No file path provided.")
        return ""

    try:
        context = load_experiment_file_context(file_path)
    except OSError as exc:
        print(f"Could not read experiment file: {exc}")
        if yes_no("Fallback to pasted data instead?", default=True):
            return read_multiline_input(
                "Paste data, summary statistics, or CSV snippet for analysis (multi-line):"
            )
        return ""

    print("\nLoaded experiment data context preview:\n")
    preview_limit = 1200
    preview = context[:preview_limit]
    if len(context) > preview_limit:
        preview += "\n...<preview truncated>"
    print(preview)
    return context


def latex_escape(text: str) -> str:
    return "".join(LATEX_ESCAPE_MAP.get(ch, ch) for ch in text)


def _format_latex_paragraphs(text: str) -> str:
    paragraphs = [part.strip() for part in text.strip().split("\n\n") if part.strip()]
    formatted: list[str] = []
    for paragraph in paragraphs:
        lines = [latex_escape(line.strip()) for line in paragraph.splitlines() if line.strip()]
        if lines:
            formatted.append(r"\\ ".join(lines))
    return "\n\n".join(formatted)


def _safe_url_for_latex(url: str) -> str:
    return url.replace("\\", "/").replace("{", "%7B").replace("}", "%7D")


def _append_latex_section(lines: list[str], title: str, body: str) -> None:
    if not body.strip():
        return
    lines.append(rf"\section*{{{latex_escape(title)}}}")
    lines.append(_format_latex_paragraphs(body))


def build_latex_document(
    topic: str,
    queries: list[str],
    results_by_query: dict[str, list[SearchHit]],
    hypotheses: str,
    data_analysis: str,
    final_paper: str,
) -> str:
    lines = [
        r"\documentclass[11pt]{article}",
        r"\usepackage[margin=1in]{geometry}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[hidelinks]{hyperref}",
        r"\title{AI Research Session Export}",
        r"\date{}",
        r"\begin{document}",
        r"\maketitle",
    ]

    if topic:
        lines.append(r"\section*{Topic}")
        lines.append(latex_escape(topic))

    if queries:
        lines.append(r"\section*{Queries}")
        lines.append(r"\begin{itemize}")
        for query in queries:
            lines.append(rf"\item {latex_escape(query)}")
        lines.append(r"\end{itemize}")

    if results_by_query:
        lines.append(r"\section*{Search Results}")
        for query, hits in results_by_query.items():
            lines.append(rf"\subsection*{{{latex_escape(query)}}}")
            if not hits:
                lines.append("No results returned.")
                continue

            lines.append(r"\begin{enumerate}")
            for hit in hits:
                title = latex_escape(hit.title)
                date_text = f" ({latex_escape(hit.date)})" if hit.date else ""
                url = _safe_url_for_latex(hit.url)
                item = rf"\item \textbf{{{title}}}{date_text}\\ \url{{{url}}}"
                if hit.snippet:
                    item += rf"\\ {latex_escape(hit.snippet)}"
                lines.append(item)
            lines.append(r"\end{enumerate}")

    _append_latex_section(lines, "Hypotheses", hypotheses)
    _append_latex_section(lines, "Data Analysis", data_analysis)
    _append_latex_section(lines, "Final Paper Draft", final_paper)

    lines.append(r"\end{document}")
    return "\n".join(lines) + "\n"


def save_session_to_latex(
    output_path: str,
    topic: str,
    queries: list[str],
    results_by_query: dict[str, list[SearchHit]],
    hypotheses: str,
    data_analysis: str,
    final_paper: str,
) -> str:
    final_path = output_path.strip() or "research_session_export.tex"
    if not final_path.lower().endswith(".tex"):
        final_path += ".tex"

    latex_doc = build_latex_document(
        topic=topic,
        queries=queries,
        results_by_query=results_by_query,
        hypotheses=hypotheses,
        data_analysis=data_analysis,
        final_paper=final_paper,
    )
    with open(final_path, "w", encoding="utf-8") as file:
        file.write(latex_doc)
    return final_path


def print_banner() -> None:
    print(ASCII_LOGO)
    print("AI Research Assistant")
    print(f"Model: {DEFAULT_MODEL}")
    print("=" * 64)


def print_menu() -> None:
    print("\n+-----------------------------------------------+")
    print("| 1) New literature search                      |")
    print("| 2) Generate hypotheses                        |")
    print("| 3) Analyze experiment data                    |")
    print("| 4) Draft final research paper                 |")
    print("| 5) Save session to LaTeX                      |")
    print("| 6) Run full pipeline                          |")
    print("| 0) Exit                                       |")
    print("+-----------------------------------------------+")


def normalize_search_hit(item: Any) -> SearchHit:
    if hasattr(item, "model_dump"):
        item = item.model_dump()

    if isinstance(item, dict):
        return SearchHit(
            title=str(item.get("title", "<no title>")),
            url=str(item.get("url", "<no url>")),
            snippet=str(item.get("snippet", "")),
            date=item.get("date"),
            last_updated=item.get("last_updated"),
        )
    if isinstance(item, (tuple, list)):
        title = str(item[0]) if len(item) > 0 else "<no title>"
        url = str(item[1]) if len(item) > 1 else "<no url>"
        snippet = str(item[2]) if len(item) > 2 else ""
        return SearchHit(title=title, url=url, snippet=snippet)
    return SearchHit(title=str(item), url="<unknown>", snippet="")


def unpack_results(raw_results: Any, queries: list[str]) -> dict[str, list[SearchHit]]:
    results_by_query: dict[str, list[SearchHit]] = {query: [] for query in queries}
    if not raw_results:
        return results_by_query

    if isinstance(raw_results, list) and raw_results and isinstance(raw_results[0], (list, tuple)):
        for i, query in enumerate(queries):
            bucket = raw_results[i] if i < len(raw_results) else []
            results_by_query[query] = [normalize_search_hit(item) for item in bucket]
        return results_by_query

    if isinstance(raw_results, dict):
        for query in queries:
            bucket = raw_results.get(query, [])
            if isinstance(bucket, list):
                results_by_query[query] = [normalize_search_hit(item) for item in bucket]
        return results_by_query

    if isinstance(raw_results, list):
        items = [normalize_search_hit(item) for item in raw_results]
        first_query = queries[0] if queries else "query"
        results_by_query[first_query] = items
        return results_by_query

    return results_by_query


def print_results(results_by_query: dict[str, list[SearchHit]]) -> None:
    for i, (query, hits) in enumerate(results_by_query.items(), start=1):
        print(f"\nResults for query {i}: {query}")
        if not hits:
            print("  No results returned.")
            continue
        for j, hit in enumerate(hits, start=1):
            date_text = f" ({hit.date})" if hit.date else ""
            print(f"  {j}. {hit.title}{date_text}")
            print(f"     URL: {hit.url}")
            if hit.snippet:
                print(f"     Snippet: {hit.snippet}")
        print("---")


def _extract_content_text(content: Any) -> str:
    if isinstance(content, str):
        return content.strip()
    if not isinstance(content, list):
        return ""

    parts: list[str] = []
    for chunk in content:
        if hasattr(chunk, "model_dump"):
            chunk = chunk.model_dump()
        if isinstance(chunk, dict):
            text = chunk.get("text")
            if isinstance(text, str) and text.strip():
                parts.append(text.strip())
    return "\n".join(parts).strip()


def extract_message_text(response: Any) -> str:
    if hasattr(response, "response") and getattr(response, "response") is not None:
        response = getattr(response, "response")

    choices = getattr(response, "choices", None)
    if choices is None and isinstance(response, dict):
        choices = response.get("choices")
    if not choices:
        return ""

    texts: list[str] = []
    for choice in choices:
        message = getattr(choice, "message", None)
        if message is None and isinstance(choice, dict):
            message = choice.get("message")
        if message is None:
            message = getattr(choice, "delta", None)
        if message is None and isinstance(choice, dict):
            message = choice.get("delta")
        if message is None:
            continue

        content = getattr(message, "content", None)
        if content is None and isinstance(message, dict):
            content = message.get("content")
        text = _extract_content_text(content)
        if text:
            texts.append(text)
    return "\n".join(texts).strip()


def extract_citations(response: Any) -> list[str]:
    if hasattr(response, "response") and getattr(response, "response") is not None:
        response = getattr(response, "response")

    citations = getattr(response, "citations", None)
    if citations is None and isinstance(response, dict):
        citations = response.get("citations")
    if not isinstance(citations, list):
        return []
    return _dedupe([str(item) for item in citations if item])


def search_queries(
    client: Perplexity,
    queries: list[str],
    max_results: int,
    search_mode: str = "academic",
) -> dict[str, list[SearchHit]]:
    payload: str | list[str] = queries if len(queries) > 1 else queries[0]
    request_kwargs: dict[str, Any] = {"query": payload, "max_results": max_results}
    if search_mode:
        request_kwargs["search_mode"] = search_mode

    try:
        response = client.search.create(**request_kwargs)
    except Exception as exc:
        if not is_search_mode_unsupported_error(exc):
            raise
        request_kwargs.pop("search_mode", None)
        response = client.search.create(**request_kwargs)
    raw_results = getattr(response, "results", None)
    if raw_results is None and isinstance(response, dict):
        raw_results = response.get("results")
    return unpack_results(raw_results, queries)


def ask_model(
    client: Perplexity,
    system_prompt: str,
    user_prompt: str,
    *,
    model: str = DEFAULT_MODEL,
    search_mode: str = "academic",
    num_search_results: int = 8,
    disable_search: bool = False,
) -> tuple[str, list[str]]:
    request_kwargs: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "num_search_results": num_search_results,
        "disable_search": disable_search,
    }
    if search_mode and not disable_search:
        request_kwargs["search_mode"] = search_mode

    try:
        response = client.chat.completions.create(**request_kwargs)
    except Exception as exc:
        if not is_search_mode_unsupported_error(exc):
            raise
        request_kwargs.pop("search_mode", None)
        response = client.chat.completions.create(**request_kwargs)
    return extract_message_text(response), extract_citations(response)


def generate_query_suggestions(client: Perplexity, queries: list[str], limit: int = 5) -> list[str]:
    system_prompt = (
        "You are a research query optimizer. Suggest focused, diverse follow-up search queries "
        "for literature review. Output only one query per line with no numbering."
    )
    user_prompt = "Existing queries:\n" + "\n".join(f"- {query}" for query in queries)
    text, _ = ask_model(
        client,
        system_prompt,
        user_prompt,
        disable_search=True,
        search_mode="academic",
        num_search_results=1,
    )
    suggestions = parse_query_lines(text)
    existing = {q.lower() for q in queries}
    filtered = [q for q in suggestions if q.lower() not in existing]
    return filtered[:limit]


def build_evidence_context(results_by_query: dict[str, list[SearchHit]], max_hits_per_query: int = 3) -> str:
    lines: list[str] = []
    source_id = 1
    for query, hits in results_by_query.items():
        lines.append(f"Query: {query}")
        for hit in hits[:max_hits_per_query]:
            lines.append(f"[{source_id}] {hit.title}")
            lines.append(f"URL: {hit.url}")
            if hit.date:
                lines.append(f"Date: {hit.date}")
            if hit.snippet:
                lines.append(f"Snippet: {hit.snippet}")
            lines.append("")
            source_id += 1
    return "\n".join(lines).strip()


def print_citations(citations: list[str]) -> None:
    if not citations:
        return
    print("\nCitations:")
    for i, citation in enumerate(citations, start=1):
        print(f"  [{i}] {citation}")


def run_hypothesis_generation(
    client: Perplexity,
    topic: str,
    evidence: str,
) -> str:
    system_prompt = (
        "You are a scientific research assistant. Produce clear, testable hypotheses based on evidence. "
        "For each hypothesis include rationale, key variables, and a quick validation approach."
    )
    user_prompt = (
        f"Topic: {topic}\n\n"
        "Evidence from literature search:\n"
        f"{evidence}\n\n"
        "Return 3 to 5 hypotheses in a concise structured format."
    )
    text, citations = ask_model(client, system_prompt, user_prompt, search_mode="academic", num_search_results=10)
    print("\nHypothesis output:\n")
    print(text or "<no output>")
    print_citations(citations)
    return text


def run_data_analysis(client: Perplexity, topic: str, evidence: str, hypotheses: str = "") -> str:
    data_text = collect_experiment_data_context()
    if not data_text:
        print("No data provided for analysis.")
        return ""

    objective = (
        prompt_input("Analysis question/objective [Identify patterns, anomalies, and implications]:")
        or "Identify patterns, anomalies, and implications."
    )

    system_prompt = (
        "You are a data analysis assistant for scientific experiments. Analyze the provided data context, "
        "explain limitations, and provide actionable next analytical steps."
    )
    user_prompt = (
        f"Research topic: {topic}\n"
        f"Objective: {objective}\n\n"
        f"Current hypotheses:\n{hypotheses or 'N/A'}\n\n"
        f"Evidence context:\n{evidence}\n\n"
        f"Data input:\n{data_text}\n\n"
        "Provide: 1) key findings, 2) caveats, 3) recommended next analyses, 4) whether the hypotheses are "
        "supported, mixed, or not supported by the available data."
    )
    text, citations = ask_model(client, system_prompt, user_prompt, search_mode="academic", num_search_results=8)
    print("\nData analysis output:\n")
    print(text or "<no output>")
    print_citations(citations)
    return text


def run_final_paper(
    client: Perplexity,
    topic: str,
    evidence: str,
    hypotheses: str,
    data_analysis: str,
) -> str:
    venue_style = prompt_input("Target venue/style [general academic]:") or "general academic"
    output_format = prompt_input("Output format [markdown]:") or "markdown"
    extra_requirements = read_multiline_input(
        "Additional paper requirements (optional):",
        allow_empty=True,
    )

    system_prompt = (
        "You are an academic and technical writer. Draft a complete research paper using the supplied evidence. "
        "Use clear sectioning, keep claims grounded, and avoid inventing methods or results."
    )
    user_prompt = (
        f"Topic: {topic}\n"
        f"Target venue/style: {venue_style}\n"
        f"Requested format: {output_format}\n"
        f"Additional requirements:\n{extra_requirements or 'N/A'}\n\n"
        f"Evidence context:\n{evidence}\n\n"
        f"Hypotheses:\n{hypotheses or 'N/A'}\n\n"
        f"Experiment data analysis:\n{data_analysis or 'N/A'}\n\n"
        "Write a full research paper with these sections: Title, Abstract, Introduction, Related Work, "
        "Hypotheses, Methods, Results, Discussion, Limitations, Conclusion, References."
    )
    text, citations = ask_model(client, system_prompt, user_prompt, search_mode="academic", num_search_results=10)
    print("\nFinal paper draft:\n")
    print(text or "<no output>")
    print_citations(citations)
    return text


def run_search_flow(client: Perplexity) -> tuple[list[str], dict[str, list[SearchHit]]]:
    raw_input = read_multiline_input(
        "Enter one or more search queries (one query per line):"
    )
    queries = parse_query_lines(raw_input)
    if not queries:
        print("No valid queries detected.")
        return [], {}

    if yes_no("Generate AI query suggestions?", default=True):
        try:
            suggestions = generate_query_suggestions(client, queries)
        except Exception as exc:
            print(f"Could not generate suggestions: {exc}")
            suggestions = []
        if suggestions:
            print("\nAI suggestions:")
            for i, suggestion in enumerate(suggestions, start=1):
                print(f"  {i}. {suggestion}")
            if yes_no("Add all suggestions to the query set?", default=True):
                queries = _dedupe(queries + suggestions)

    search_mode = choose_search_mode()
    max_results = ask_int("Max results per query", DEFAULT_MAX_RESULTS, 1, 20)
    print(f"\nRunning {search_mode} search on {len(queries)} query(s)...")

    try:
        results_by_query = search_queries(
            client=client,
            queries=queries,
            max_results=max_results,
            search_mode=search_mode,
        )
    except Exception as exc:
        print(f"Search failed: {exc}")
        return queries, {}

    print_results(results_by_query)
    return queries, results_by_query


def run_full_pipeline(
    client: Perplexity,
) -> tuple[list[str], dict[str, list[SearchHit]], str, str, str]:
    queries, results_by_query = run_search_flow(client)
    if not results_by_query:
        print("Pipeline stopped: no search results available.")
        return queries, results_by_query, "", "", ""

    topic = queries[0] if queries else "Research topic"
    evidence = build_evidence_context(results_by_query, max_hits_per_query=3)

    hypotheses = ""
    data_analysis = ""
    final_paper = ""

    if yes_no("Continue to hypothesis generation?", default=True):
        hypotheses = run_hypothesis_generation(client, topic, evidence)
    else:
        print("Skipping hypothesis generation.")

    if yes_no("Continue to experiment data analysis?", default=True):
        data_analysis = run_data_analysis(client, topic, evidence, hypotheses=hypotheses)
    else:
        print("Skipping data analysis.")

    if yes_no("Continue to final paper drafting?", default=True):
        final_paper = run_final_paper(client, topic, evidence, hypotheses, data_analysis)
    else:
        print("Skipping final paper drafting.")

    return queries, results_by_query, hypotheses, data_analysis, final_paper


def main() -> None:
    print_banner()

    client = Perplexity()
    active_queries: list[str] = []
    results_by_query: dict[str, list[SearchHit]] = {}
    latest_hypotheses = ""
    latest_data_analysis = ""
    latest_final_paper = ""

    while True:
        print_menu()
        choice = prompt_input("Choose an option:")

        if choice == "0":
            print("Exiting.")
            break

        if choice == "1":
            active_queries, results_by_query = run_search_flow(client)
            latest_hypotheses = ""
            latest_data_analysis = ""
            latest_final_paper = ""
            continue

        if choice == "6":
            (
                active_queries,
                results_by_query,
                latest_hypotheses,
                latest_data_analysis,
                latest_final_paper,
            ) = run_full_pipeline(client)
            continue

        if choice == "5":
            if not results_by_query and not any([latest_hypotheses, latest_data_analysis, latest_final_paper]):
                print("Nothing to export yet. Generate results first.")
                continue

            topic = active_queries[0] if active_queries else "Research topic"
            export_path = prompt_input("Output LaTeX file [research_session_export.tex]:") or "research_session_export.tex"
            try:
                saved_path = save_session_to_latex(
                    output_path=export_path,
                    topic=topic,
                    queries=active_queries,
                    results_by_query=results_by_query,
                    hypotheses=latest_hypotheses,
                    data_analysis=latest_data_analysis,
                    final_paper=latest_final_paper,
                )
                print(f"LaTeX file saved to: {saved_path}")
            except OSError as exc:
                print(f"Could not save LaTeX file: {exc}")
            continue

        if choice not in {"2", "3", "4"}:
            print("Invalid option.")
            continue

        if not results_by_query:
            print("Run a literature search first (option 1).")
            continue

        topic = active_queries[0] if active_queries else "Research topic"
        evidence = build_evidence_context(results_by_query, max_hits_per_query=3)

        try:
            if choice == "2":
                latest_hypotheses = run_hypothesis_generation(client, topic, evidence)
            elif choice == "3":
                latest_data_analysis = run_data_analysis(client, topic, evidence, hypotheses=latest_hypotheses)
            elif choice == "4":
                latest_final_paper = run_final_paper(
                    client,
                    topic,
                    evidence,
                    latest_hypotheses,
                    latest_data_analysis,
                )
        except Exception as exc:
            print(f"Feature execution failed: {exc}")


if __name__ == "__main__":
    main()

