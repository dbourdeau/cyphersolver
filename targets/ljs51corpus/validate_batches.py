"""Run the standard chance test on whole LJS 51 ciphers, grouped by starting folio."""
from concurrent.futures import ProcessPoolExecutor
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "docs"))
import _validate as validator


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def ordinary_batches():
    rows = [line for line in (HERE / "validation.tsv").read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("#")]
    chains = {}
    pending = []
    previous = None
    for line in rows:
        if line == "?\t?":
            pending.append(line)
            continue
        chain = line.split(":", 1)[0]
        if chain != previous and chain in chains:
            raise ValueError(f"Non-contiguous cipher {chain}")
        pairs = chains.setdefault(chain, [])
        pairs.extend(pending)
        pending.clear()
        pairs.append(line)
        previous = chain
    chains[previous].extend(pending)
    if [line for pairs in chains.values() for line in pairs] != rows:
        raise ValueError("Cipher blocks did not reproduce validation.tsv")
    expected = set(read_json(HERE / "texts/stats.json")["keyed_ids"]) - {"14v.7", "63v.trees"}
    if set(chains) != expected:
        raise ValueError(f"Letter-key inventory mismatch: {set(chains) ^ expected}")
    batches = {}

    def location(chain):
        folio, side, line = re.fullmatch(r"(\d+)([rv])\.(\d+)", chain.split("+")[0]).groups()
        return int(folio), side, int(line)

    for chain in sorted(chains, key=location):
        folio = location(chain)[0]
        first = (folio - 1) // 12 * 12 + 1
        label = f"{first}-{min(first + 11, 106)}"
        ids, pairs = batches.setdefault(label, ([], []))
        ids.append(chain)
        pairs.extend(chains[chain])
    return [(label, ids, pairs) for label, (ids, pairs) in batches.items()]


def special_inputs():
    # The vetted undotted class table has no deposited sign-by-sign alignment.
    # Use the labelled pilot clusters only to check letter-model applicability.
    pilot = read_json(HERE / "keys/f14v_tashifi.json")
    signs = ["?\t?"] * pilot["signs"]
    for row in pilot["alignment"]:
        i = row["sign"]
        if signs[i] != "?\t?":
            raise ValueError(f"Duplicate pilot sign {i}")
        signs[i] = f"14v.7:cluster{row['cls']}\t{row['letter']}"
    trees = read_json(HERE / "keys_eye/63v.trees.json")["trees"]
    branches = [f"63v.trees:L{t['left_branches']}R{t['right_branches']}\t{t['rule_letter']}"
                for t in trees]
    return [("undotted-pilot", ["14v.7"], signs), ("trees", ["63v.trees"], branches)]


def run_batch(batch):
    label, ids, pairs = batch
    count = sum(not s.endswith("\t?") for s in pairs)
    if not 0 < count <= validator.MAX_TOKENS:
        raise ValueError(f"Batch {label} has {count} scored occurrences")
    content = ("# model: ar-mamluk\n" + "\n".join(pairs) + "\n").encode("utf-8")
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / (label + ".tsv")
        path.write_bytes(content)
        result = validator.validate("ljs51corpus", pairs=path, seed=1)
    if result["tokens"] != count:
        raise ValueError(f"Validator count differs for {label}")
    print(label, len(ids), count, result["verdict"], flush=True)
    return {"batch": label, "chains": ids, "input_sha256": sha256(content).hexdigest(),
            "validation": result}


def companion_inputs():
    folder = HERE.parent / "ljs51f48r"
    key = read_json(folder / "key.json")
    pairs = []
    for line in (folder / "transcription.txt").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        location, *tokens = line.split()
        for sign in tokens:
            if sign == "|":
                continue
            # The companion decoder documents the two readings of this shape.
            value = {"21r02": "ح", "21r03": "ش"}[location] if sign == "EK" else key[sign]
            pairs.append(f"{sign}\t{value}")
    _, signs, values = validator.read_pairs(HERE.parent / "qaysarani1350/validation.tsv")
    return [("48r-with-21r", ["48r.8"], pairs),
            ("106v", ["106v.6"], [f"{s}\t{v}" for s, v in zip(signs, values)])]


if __name__ == "__main__":
    ordinary = ordinary_batches()
    specials = special_inputs()
    # A separate pooled run includes the trees at the same effort as the
    # letter keys. The tree-only run retains the validator's length cutoff.
    _, ids, pairs = next(batch for batch in ordinary if batch[0] == "61-72")
    _, tree_id, branches = specials[1]
    pooled = ("61-72-with-trees", ids + tree_id, pairs + ["?\t?"] + branches)
    inputs = ordinary + specials + [pooled] + companion_inputs()
    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(run_batch, inputs))
    output = {"validator": "docs/_validate.py", "seed": 1, "quick": False, "batches": results}
    (HERE / "validation_batches.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
