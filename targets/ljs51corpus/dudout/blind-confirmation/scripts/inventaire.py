"""Inventaire des chaines keys_eye : longueur en signes, classes, presence d'un clair.
N'affiche JAMAIS le clair ni la cle. Ecrit inventaire.tsv."""
import json, subprocess, sys, os
C = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/cyphersolver-pr/clone"
REF = "d8ac608093e1149f9456eaa2c99bb456ca0abc92"
out = sys.argv[1]
names = subprocess.run(["git","-C",C,"ls-tree","--name-only",REF,"targets/ljs51corpus/keys_eye/"],capture_output=True,text=True).stdout.split()
rows=[]
def lines_of(d):
    cl = d.get('cipher_lines') or {}
    if not isinstance(cl,(dict,list)): return []
    vals = list(cl.values()) if isinstance(cl, dict) else list(cl)
    out=[]
    for v in vals:
        out.append(' '.join(v) if isinstance(v, list) else v)
    return out
for n in names:
    if not n.endswith('.json'): continue
    d = json.loads(subprocess.run(["git","-C",C,"show",f"{REF}:{n}"],capture_output=True,text=True).stdout)
    toks = [t for t in lines_of(d) for t in t.split() if t != '|']
    cl = {i:l for i,l in enumerate(lines_of(d))}
    has_plain = bool(d.get('plaintext'))
    rows.append((os.path.basename(n)[:-5], len(toks), len(set(toks)), int(has_plain), int(any('|' in v for v in cl.values()))))
with open(out,'w') as f:
    f.write("chain\tsigns\tclasses\thas_plain\thas_dividers\n")
    for r in sorted(rows): f.write("\t".join(map(str,r))+"\n")
print(len(rows), "chaines")
