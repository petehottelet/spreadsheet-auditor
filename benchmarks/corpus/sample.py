"""Draw a stratified sample of findings from a corpus run and write context cards.

    python benchmarks/corpus/sample.py spreadsheetbench --per-rule 20 --max-per-workbook 2

Writes benchmarks/corpus/samples/<source>.json (the sample with context, the
input to report.py) and benchmarks/corpus/samples/<source>.md (the same
findings as readable cards for labeling). Keys are stable across runs as long
as the workbook and the finding do not change, so labels survive re-runs.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpuslib import (  # noqa: E402
    DATA_DIR,
    RESULTS_DIR,
    SAMPLES_DIR,
    WorkbookCache,
    build_context,
    load_findings,
    load_sources,
    now_iso,
    render_cards,
    render_compact_cards,
    stratified_sample,
    write_json,
    write_text,
)


def main(argv: list[str] | None = None) -> int:
    sources = load_sources()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", choices=sorted(sources))
    parser.add_argument("--data-dir", default=str(DATA_DIR))
    parser.add_argument("--results-dir", default=None)
    parser.add_argument("--per-rule", type=int, default=20)
    parser.add_argument("--max-per-workbook", type=int, default=2)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args(argv)

    results_dir = Path(args.results_dir) if args.results_dir else RESULTS_DIR / args.source
    data_dir = Path(args.data_dir) / args.source / "files"
    items = load_findings(results_dir)
    chosen = stratified_sample(items, args.per_rule, args.max_per_workbook, args.seed)
    cache = WorkbookCache()
    sample_items = []
    for item in chosen:
        finding = item["finding"]
        sample_items.append(
            {
                "key": item["key"],
                "workbook": item["workbook"],
                "finding": {
                    key: finding.get(key)
                    for key in ("rule_id", "severity", "error_confidence", "location", "formula", "evidence", "suggested_fix")
                },
                "context": build_context(data_dir / item["workbook"], finding, cache),
            }
        )
    sample = {
        "source": args.source,
        "generated": now_iso(),
        "results_dir": str(results_dir),
        "seed": args.seed,
        "per_rule": args.per_rule,
        "max_per_workbook": args.max_per_workbook,
        "total_findings": len(items),
        "items": sample_items,
    }
    write_json(SAMPLES_DIR / f"{args.source}.json", sample)
    write_text(SAMPLES_DIR / f"{args.source}.md", render_cards(sample))
    write_text(SAMPLES_DIR / f"{args.source}.compact.md", render_compact_cards(sample))
    rules = sorted({item["finding"]["rule_id"] for item in sample_items})
    print(f"sampled {len(sample_items)} of {len(items)} findings across {len(rules)} rules -> {SAMPLES_DIR / (args.source + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
