"""Reproduce both held-out tests and compare every byte of the archived output."""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile

here = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("corpus", type=Path, help="path to upstream targets/esp318/lit/quijote.txt")
parser.add_argument("--work-dir", type=Path, default=here,
                    help="writable workspace folder for temporary replay files (default: beside this script)")
args = parser.parse_args()
if not args.corpus.is_file():
    parser.error(f"Spanish corpus file missing: {args.corpus}")
if not args.work_dir.is_dir():
    parser.error(f"Replay workspace directory missing: {args.work_dir}")
required = ["candidate.tsv", "candidate15.tsv", "oct14.runs", "oct15.runs", "score.py", "score15.py",
            "diez_gloss.tsv", "oct14_results.json", "oct15_results.json"]
for filename in required:
    if not (here / filename).is_file():
        parser.error(f"Required frozen input or result missing: {here / filename}")

with tempfile.TemporaryDirectory(dir=args.work_dir, prefix="october-replay-") as temp:
    work = Path(temp).resolve()
    # Preserve the frozen October 14 script's original directory layout.
    project = work / "batch18b" / "mexico"
    project.mkdir(parents=True)
    for name in ["candidate.tsv", "oct14.runs"]:
        (project / name).symlink_to(here / name)
    (project / "score.py").write_bytes((here / "score.py").read_bytes())
    july = work / "batch18" / "mexico"
    july.mkdir(parents=True)
    (july / "diez_gloss.tsv").symlink_to(here / "diez_gloss.tsv")
    lit = work / "crawford_rebase" / "targets" / "esp318" / "lit"
    lit.mkdir(parents=True)
    (lit / "quijote.txt").symlink_to(args.corpus.resolve())
    tests = [
        (14, [str(project / "score.py")]),
        (15, [str(here / "score15.py"), str(here), str(args.corpus.resolve())]),
    ]
    for day, argv in tests:
        got = subprocess.check_output([sys.executable, "-I", *argv])
        if got != (here / f"oct{day}_results.json").read_bytes():
            raise SystemExit(f"October {day} output differs from the archived result")
        print(f"October {day} results match byte for byte")
