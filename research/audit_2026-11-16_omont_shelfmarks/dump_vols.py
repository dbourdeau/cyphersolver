"""Dump the cipher components of each named Français volume (notice + loupe search). python -I -X utf8 dump_vols.py N [N ...]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import am
for N in map(int, sys.argv[1:]):
    n, d = am.find_fr(N)
    if not n:
        print(f'=== fr. {N}: NOTICE NOT FOUND', flush=True); continue
    c = am.ciph(n)
    print(f'=== fr. {N} cc{n} {am.url(n)} | old {d["old"]} | gallica {d["gallica"]} | {len(d["items"])} items on page | head: {d["head"][:160]}', flush=True)
    for cid, tx in sorted(c.items(), key=lambda x: x[0]):
        print(f'   [{cid.split("_")[-1]}] {tx[:300]}', flush=True)
