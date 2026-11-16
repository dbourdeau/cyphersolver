"""BNP Horizon keyword searches: cipher term AND an African place word. Reuses the parser of research/sweep_2026-11_bnp_portugal/harvest.py.
usage: bnp_africa.py "cifr* angola" ...   -> prints total and page-1 hits"""
import sys, time, urllib.parse, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "sweep_2026-11_bnp_portugal"))
import harvest as h
for t in sys.argv[1:]:
    s = h.get(h.BASE + urllib.parse.quote_plus(t))
    total, hits = h.parse(s)
    print("##", t, "total", total, flush=True)
    for b, ti in hits: print("   ", b, ti[:150])
    time.sleep(2.5)
