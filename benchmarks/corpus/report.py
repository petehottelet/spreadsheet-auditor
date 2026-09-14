"""Join a sample and its labels into the real-world precision report.

    python benchmarks/corpus/report.py spreadsheetbench

Reads benchmarks/corpus/results/<source>/run_summary.json,
benchmarks/corpus/samples/<source>.json, and benchmarks/corpus/labels/<source>.json;
writes benchmarks/real_world_precision.md and benchmarks/real_world_precision.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpuslib import (  # noqa: E402
    LABELS_DIR,
    RESULTS_DIR,
    ROOT,
    SAMPLES_DIR,
    load_labels,
    load_sources,
    now_iso,
    precision_rows,
    render_report,
    write_json,
    write_text,
)


def main(argv: list[str] | None = None) -> int:
    sources = load_sources()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", choices=sorted(sources))
    parser.add_argument("--results-dir", default=None)
    parser.add_argument("--out", default=str(ROOT / "benchmarks" / "real_world_precision.md"))
    args = parser.parse_args(argv)

    results_dir = Path(args.results_dir) if args.results_dir else RESULTS_DIR / args.source
    run_summary = json.loads((results_dir / "run_summary.json").read_text(encoding="utf-8"))
    sample = json.loads((SAMPLES_DIR / f"{args.source}.json").read_text(encoding="utf-8"))
    labels = load_labels(LABELS_DIR / f"{args.source}.json")
    rows = precision_rows(sample, labels, run_summary)
    report = render_report(sources[args.source], run_summary, sample, labels, rows)
    out = Path(args.out)
    write_text(out, report)
    summary_without_records = {k: v for k, v in run_summary.items() if k != "records"}
    write_json(
        out.with_suffix(".json"),
        {"generated": now_iso(), "source": args.source, "run": summary_without_records, "rules": rows},
    )
    unlabeled = sum(row["unlabeled"] for row in rows)
    print(f"wrote {out} ({sum(row['sampled'] for row in rows)} sampled, {unlabeled} unlabeled)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
