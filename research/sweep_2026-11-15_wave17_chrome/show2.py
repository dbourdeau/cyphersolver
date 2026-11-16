"""Tight cipher-context snippets from saved Manus details. Usage: show2.py id ..."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
RX = re.compile(r"decifr|crittogr|criptat|in cifra|cifrat|cifrario|scrittura segreta|ziferis|poligraf", re.I)
for i in sys.argv[1:]:
    t = open(os.path.join(HERE, "raw", "manus_detail", i + ".json"), encoding="utf8").read()
    t = re.sub(r"\u003c[^>]*?\u003e|<[^>]+>", " ", t); t = re.sub(r'"[a-zA-Z]+": null,?|\s+', " ", t)
    m0 = re.search(r'Firenze|Roma|Napoli|Milano|Mantova|Vigevano|Parma|Pisa|San Gimignano|Modena|Campobasso|Monreale', t)
    print("=====", i, t[m0.start():m0.start()+90] if m0 else "")
    seen = 0
    for m in RX.finditer(t):
        if m.start() < seen: continue
        print("   ..", t[max(0, m.start()-200): m.end()+200]); seen = m.end()+200
