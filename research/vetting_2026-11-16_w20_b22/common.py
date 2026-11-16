import json, sys, subprocess, os
BY = "claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting"
def tomo(terms): return f"Tomokiyo's list of unsolved ciphers (cryptiana.web.fc2.com/code/unsolved.htm, the copy fetched 15 Nov 2026) was searched with tags stripped for {terms}: no entry for this item."
def lasry(terms): return f"Lasry's list of BnF and other readings (cryptiana.web.fc2.com/code/GL.htm, the copy fetched 15 Nov 2026) was searched with tags stripped for {terms}: no entry for this item."
def put(lid, entry):
    p = f'e{lid}.json'
    json.dump({str(lid): entry}, open(p, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    subprocess.run([sys.executable, '-I', '-X', 'utf8', 'put.py', p])
def V(seen, prior, key, dup, verdict, closed=None):
    v = {"date": "2026-11-16", "by": BY, "seen": seen, "prior_art": prior, "key_check": key, "duplicates": dup, "verdict": verdict}
    if closed: v["closed"] = closed
    return v
