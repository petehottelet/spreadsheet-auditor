"""Audit every workbook in a corpus and record findings, crashes, and timeouts.

    python benchmarks/corpus/run_corpus.py spreadsheetbench
    python benchmarks/corpus/run_corpus.py spreadsheetbench --limit 500 --workers 8 --no-recalc

Results go to benchmarks/corpus/results/<source>/ (gitignored): one findings
JSON per workbook plus run_summary.json with per-file status and aggregate
counts. The include glob defaults to the source's `default_include_glob`
(SpreadsheetBench: the _input workbooks only, to skip near-duplicate answers).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpuslib import DATA_DIR, RESULTS_DIR, load_sources, render_run_table, run_corpus  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    sources = load_sources()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", choices=sorted(sources))
    parser.add_argument("--data-dir", default=str(DATA_DIR))
    parser.add_argument("--out-dir", default=None, help="Default benchmarks/corpus/results/<source>.")
    parser.add_argument("--limit", type=int, default=None, help="Random sample of this many workbooks (seeded).")
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=180, help="Per-workbook wall-clock limit in seconds.")
    parser.add_argument("--include-glob", default=None, help="Only file names matching this glob; default from sources.json.")
    parser.add_argument("--all-files", action="store_true", help="Ignore the source's default include glob.")
    parser.add_argument("--no-recalc", action="store_true", help="Disable LibreOffice recalculation for speed.")
    args = parser.parse_args(argv)

    meta = sources[args.source]
    data_dir = Path(args.data_dir) / args.source / "files"
    if not data_dir.exists():
        raise SystemExit(f"{data_dir} not found; run fetch.py {args.source} first.")
    out_dir = Path(args.out_dir) if args.out_dir else RESULTS_DIR / args.source
    include_glob = None if args.all_files else (args.include_glob or meta.get("default_include_glob"))
    extra_args: list[str] = []
    if args.no_recalc:
        config = out_dir / "config.json"
        config.parent.mkdir(parents=True, exist_ok=True)
        config.write_text(json.dumps({"recalc": {"enabled": False}}), encoding="utf-8")
        extra_args += ["--config", str(config)]

    def progress(done: int, total: int) -> None:
        print(f"  {done}/{total} workbooks audited", flush=True)

    from corpuslib import list_workbooks

    if not list_workbooks(data_dir, include_glob):
        raise SystemExit(f"no workbooks under {data_dir} match {include_glob or '*'}; nothing to audit.")

    summary = run_corpus(
        args.source,
        data_dir,
        out_dir,
        limit=args.limit,
        seed=args.seed,
        workers=args.workers,
        timeout=args.timeout,
        include_glob=include_glob,
        extra_args=extra_args,
        progress=progress,
    )
    print(render_run_table(summary))
    print(f"\nwrote {out_dir / 'run_summary.json'} in {summary['wall_clock_seconds']} s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
