"""Download and extract a corpus listed in sources.json.

    python benchmarks/corpus/fetch.py spreadsheetbench
    python benchmarks/corpus/fetch.py euses-modified --data-dir /tmp/corpora

Archives land in benchmarks/corpus/data/<source>/ (gitignored). Existing
extractions are reused; pass --force to download again.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tarfile
import urllib.request
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpuslib import DATA_DIR, list_workbooks, load_sources  # noqa: E402


def download(url: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_suffix(target.suffix + ".partial")
    request = urllib.request.Request(url, headers={"User-Agent": "spreadsheet-auditor corpus fetch"})
    with urllib.request.urlopen(request, timeout=120) as response, partial.open("wb") as handle:
        shutil.copyfileobj(response, handle, length=1 << 20)
    partial.replace(target)


def extract(archive: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    name = archive.name.lower()
    if name.endswith((".tar.gz", ".tgz")):
        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(destination, filter="data")
    elif name.endswith(".zip"):
        with zipfile.ZipFile(archive) as bundle:
            bundle.extractall(destination)
    else:
        raise SystemExit(f"Unsupported archive type: {archive.name}")


def main(argv: list[str] | None = None) -> int:
    sources = load_sources()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", choices=sorted(sources))
    parser.add_argument("--data-dir", default=str(DATA_DIR), help="Where corpora are stored (default benchmarks/corpus/data).")
    parser.add_argument("--force", action="store_true", help="Download and extract again even if present.")
    args = parser.parse_args(argv)

    meta = sources[args.source]
    target_dir = Path(args.data_dir) / args.source
    archive = target_dir / ("archive." + ("tar.gz" if meta["archive"].startswith("tar") else "zip"))
    extracted = target_dir / "files"
    if extracted.exists() and not args.force:
        print(f"{args.source}: already extracted at {extracted} ({len(list_workbooks(extracted))} workbooks). Use --force to refetch.")
        return 0
    print(f"{args.source}: downloading {meta['url']}")
    download(meta["url"], archive)
    print(f"{args.source}: extracting {archive.name} ({archive.stat().st_size / 1e6:.0f} MB)")
    if extracted.exists():
        shutil.rmtree(extracted)
    extract(archive, extracted)
    workbooks = list_workbooks(extracted)
    print(f"{args.source}: {len(workbooks)} workbooks under {extracted}")
    if meta["format"].startswith("xls "):
        print("note: this corpus is .xls; convert with LibreOffice (soffice --headless --convert-to xlsx) before running the auditor.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
