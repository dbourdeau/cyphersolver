"""Replay the four frozen comparisons offline in a disposable directory."""
import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def records(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader((line for line in stream if not line.startswith("#")), delimiter="\t"))


def check_crosswalk(key, shapes):
    values = defaultdict(set)
    for row in records(key):
        values[row["label"]].update(row["valeur"].split("|"))
    joined = {row["published_label"] for row in records(shapes) if " / " in row["published_label"]}
    aliases = records(HERE / "34r/crosswalk.tsv")
    require(len(aliases) == 6 and {row["plate"] for row in aliases} == joined, "plate alias inventory")
    for row in aliases:
        names = row["plate"].split(" / ")
        parts = [values[name] for name in names]
        require(len(set.union(*parts)) == 1 and all(len(x) == 1 for x in parts), row["plate"])
        require(row["representative"] == names[0], row["plate"])
        require(row["attested_values"] == " ; ".join(next(iter(x)) for x in parts), row["plate"])


def stage(source, dest):
    dest.parent.mkdir(exist_ok=True, parents=True)
    shutil.copyfile(source, dest)


def run_case(root, name, registered):
    fourth = name == "32v_4"
    source = HERE / ("32v_2_4" if name in ("32v_2_3", "32v_4") else name)
    local = root / "study" / name
    scorer = source / "check.py" if name == "34r" else registered
    stage(scorer, local / "check.py")
    stage(source / "reference.txt", local / "reference.txt")
    if name == "34r":
        stage(source / "crosswalk.tsv", local / "crosswalk.tsv")
    for tag in ("reader_a", "reader_b"):
        filename = Path(tag) / "reading.tsv"
        stage(source / filename, local / filename)
        if name == "32v_2_3":
            lines = (local / filename).read_bytes().splitlines(keepends=True)
            (local / filename).write_bytes(b"".join(row for row in lines if not row.startswith(b"c\t")))

    script = "score_fourth.py" if fourth else "check.py"
    if fourth:
        stage(source / script, local / script)
    subprocess.run([sys.executable, "-I", "-B", str(local / script)], check=True, stdout=subprocess.DEVNULL)
    prefix = "fourth_" if fourth else ""
    result = local / (prefix + "result.json")
    scores = local / ("fourth_controls.txt" if fourth else "control_scores.txt")
    positions = local / (prefix + "positions.tsv")
    expected = HERE / "results" / name
    original = json.loads((HERE / "results/original_sha256.json").read_text())[name]
    require(result.read_bytes() == (expected / "result.json").read_bytes(), f"{name} result")
    for path, field in [(result, "result_sha256"), (scores, "ordered_control_lines_sha256"), (positions, "positions_sha256")]:
        require(digest(path) == original[field], f"{name} {field}")
    control_vector = scores.read_text().split()
    require(len(control_vector) == 1000 and control_vector == (expected / "controls.txt").read_text().split(),
            f"{name} ordered controls")
    if name == "34r":
        normalized = [{key: value or "?" for key, value in row.items()} for row in records(positions)]
        require(normalized == records(source / "positions.tsv"), "34r rendered position table")
    data = json.loads(result.read_text())
    print(f"{name}: score {data['score']}, maximum {data['control_max']}, pass={data['pass']}. "
          "Result, positions and 1,000 ordered controls reproduced.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=HERE.parents[3],
                        help="existing #828 checkout (default: repository containing this directory)")
    args = parser.parse_args()
    target = args.repo / "targets/gonzaga1549/beling_october1552"
    key = args.repo / "targets/figueroa1534/validation/K4.tsv"
    shapes = target / "shape_index.tsv"
    registered = target / "interior/registered_scorer.py"
    require(digest(key) == "a456e5bba6ee788371827d73ffa263ae034c98615bfb1f91dfdac3de90632ed6", "K4.tsv")
    require(digest(shapes) == "07ca1d9636889655e57d20e6feaec18dc2ef70c6f4e83534b8df5b91278eabcb", "shape index")
    require(digest(registered) == "e32d83034ace301318dec7f3ddd619551920b9b75c64ca2705c97bb9051935a2", "32v scorer")
    for line in (HERE / "SHA256SUMS").read_text().splitlines():
        checksum, path = line.split(maxsplit=1)
        require(digest(HERE / path) == checksum, path)
    check_crosswalk(key, shapes)
    with TemporaryDirectory() as temp:
        root = Path(temp)
        # These historical path names are embedded in the byte-identical registered programs.
        stage(key, root / "crawford_rebase/targets/figueroa1534/validation/K4.tsv")
        stage(shapes, root / "priority_review/modena_shape_reference/shape_index.tsv")
        for name in ("32v_2_3", "32v_4", "32v_5_6", "34r"):
            run_case(root, name, registered)


if __name__ == "__main__":
    main()
