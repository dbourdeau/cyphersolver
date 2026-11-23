"""Replay both registered May tests using their unchanged scorers and surviving text inputs."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

SOURCE = Path(__file__).resolve().parent


def replay(root, folder, original_name, scorer):
    archived = SOURCE / folder
    work = root / original_name
    work.mkdir()

    for item in archived.iterdir():
        if item.name in ("controls.tsv", "result.json"):
            continue  # Frozen scorers write fresh outputs and refuse an existing file.
        target = work / item.name
        if item.name in ("FREEZE.txt", "RUN_FREEZE.txt"):
            lines = item.read_text().splitlines()
            kept = [lines[0]]
            for record in lines[1:]:
                _, location = record.split("  ", 1)
                if Path(location).suffix.lower() not in {".png", ".jpg", ".jpeg"}:
                    kept.append(record)
            target.write_text("\n".join(kept) + "\n")
        else:
            shutil.copyfile(item, target)

    subprocess.run([sys.executable, "-I", "-B", str(work / scorer)], check=True)
    for name in ("result.json", "controls.tsv"):
        expected, actual = archived / name, work / name
        if actual.exists() != expected.exists():
            raise ValueError(f"{folder}: unexpected presence or absence of {name}")
        if expected.exists() and expected.read_bytes() != actual.read_bytes():
            raise ValueError(f"{folder}: replay differs from saved {name}")
    return json.loads((work / "result.json").read_text())


def main():
    # Recreate the relative paths recorded in both original scorers and their hashes.
    with TemporaryDirectory() as temporary:
        root = Path(temporary) / "output/codex_2026-11-17b"
        key = root / "nov20_william_transfer/alphabet.tsv"
        key.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE / "june/alphabet.tsv", key)
        may10 = replay(root, "may10", "nov20_william_may", "test_may.py")
        may09 = replay(root, "may09", "nov20_william_may_fresh", "score.py")
    if may10["status"] != "unscorable" or may10["eligible"] or len(may10["groups"]) != 10:
        raise ValueError("May 10 stop record")
    if len(may09["groups"]) != 34 or sum(row["sure_ink"] for row in may09["groups"]) != 10:
        raise ValueError("May 9 transcription counts")
    pairs = [(r["group"], r["a"], r["b"], r["output"], r["gloss"])
             for r in may09["groups"] if "output" in r]
    if pairs != [("T08", "RQH2", "RQH2", "ONE", "our")]:
        raise ValueError("May 9 eligible pair")
    if (may09["status"], may09["whole_matches"], may09["tied"], may09["holdout"]) != ("miss", 0, 1000, None):
        raise ValueError("May 9 outcome")
    print("May 10: no eligible pair among 10 groups; stopped with no controls.")
    print("May 9: 34 groups, 10 complete row-2 readings, 1 eligible; T08 RQH2 yields ONE against 'our'.")
    print("Reproduced both result files and all 1,000 tied May 9 controls. No unglossed group decoded.")


if __name__ == "__main__":
    main()
