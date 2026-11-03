"""Final key: EM values on all pairs (key_em.tsv) plus hand-set code words (key_overrides.tsv), minus the EM fillers
listed in key_demoted.tsv -> key.tsv. Run from the target folder: python scripts/make_key.py
status: confirmed = seen >= 2 and the same value at >= 2/3 of the places; single = seen once; mixed = otherwise;
unresolved = an EM filler that crosses a boundary (kept for the record, not used by decode.py)."""
import sys
em = {}
for ln in open("key_em.tsv", encoding="utf-8"):
    if ln.startswith("#"): continue
    g, v, seen, agree, other = (ln.rstrip("\n").split("\t") + [""])[:5]
    seen, agree = int(float(seen)), int(float(agree))
    st = "single" if seen == 1 else ("confirmed" if agree >= 2 and agree * 3 >= seen * 2 else "mixed")
    em[g] = (v, seen, agree, st, other)
for ln in open("key_overrides.tsv", encoding="utf-8"):
    if ln.startswith("#") or not ln.strip(): continue
    g, v, note = ln.rstrip("\n").split("\t")
    s = em.get(g, (None, 0, 0, "", ""))
    em[g] = (v, s[1], s[2], "codeword, set by hand", note)
for ln in open("key_demoted.tsv", encoding="utf-8"):
    if ln.startswith("#") or not ln.strip(): continue
    g, v, cand, where = ln.rstrip(chr(10)).split(chr(9))
    s = em.get(g, (v, 0, 0, "", ""))
    em[g] = ("[?]", s[1], s[2], "unresolved (EM filler, not a key value)", f"EM gave {s[0]}; {cand}")
with open("key.tsv", "w", encoding="utf-8") as f:
    f.write("# Höpken-Carlson code, Constantinople 1739-41 (Riksarkivet R0003582). Partial code list rebuilt from the interlinear\n"
            "# French of images 255-257 and 260. value = the letters the group stands for (accents and apostrophes dropped; u = v).\n"
            "# seen/agree = places in the pairs and how many of them take this value. Only 'confirmed' values are firm.\n"
            "group\tvalue\tseen\tagree\tstatus\tother readings or note\n")
    for g in sorted(em):
        v, seen, agree, st, other = em[g]
        f.write(f"{g}\t{v}\t{seen}\t{agree}\t{st}\t{other}\n")
from collections import Counter
print(Counter(x[3] for x in em.values()))
