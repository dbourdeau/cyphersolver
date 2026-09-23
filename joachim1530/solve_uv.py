"""Substitution search with a period Italian model retaining u/v distinction."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lang import lm
from joachim1530.solve import load, solve


def main():
    sources = [Path("lang/corpora/it-renaissance.txt"),
               Path("lang/corpora/it-nunziature.txt")]
    raw = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in sources)
    text = lm.norm(raw, "modern", False)
    # Unlike lang's early normalisation this retains separate u and v.
    model = lm.DenseLM.build(text, 4, lm.alphabet("modern", False))
    print("model", len(text), "chars", flush=True)
    solve(load(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),
          order=4, model_name="it-cinquecento-uv", plain="abcdefghilmnopqrstuvz",
          model_override=model)


if __name__ == "__main__":
    main()
