"""Selection des chaines FRAICHES de mesure (jamais mesurees) et extraction des .sig. N'affiche jamais le clair.
Regle (fixee avant tout resultat sur ces chaines) :
  eligible = keys_eye present, separateurs presents, clair du compilateur present (chains_all plaintext.text,
  answered == 'yes'), hors 18 chaines deja mesurees (ljs51-aveugle), hors exclusions des autres pistes ;
  on prend toutes les eligibles >= 90 signes ; s'il y en a moins de 10, on complete par longueur decroissante
  (ordre alphabetique a egalite) jusqu'a 10.
  Fuite : proportion des 12-grammes (lettres seules) du clair presents dans le corpus du modele 4-grammes
  OU dans le corpus du lexique ; une chaine > 5 % est remplacee par la suivante dans l'ordre."""
import json, subprocess, sys, os
sys.path.insert(0, "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/scripts")
from common import words, strip_meta, CORPUS, TRAIN
C = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/cyphersolver-pr/clone"
REF = "d8ac608093e1149f9456eaa2c99bb456ca0abc92"
B = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-22r1-61r3/"
OUT = B + "transcriptions/"
os.makedirs(OUT, exist_ok=True)
def show(p): return subprocess.run(["git","-C",C,"show",f"{REF}:{p}"],capture_output=True,text=True,check=True).stdout
MEASURED = {"20r.8+47r.1","22r.1","19r.7","105v.6","18r.11","23r.9","61r.3","30r.4","42r.2","39v.12",
            "56v.8","6v.11","41r.3","31r.11","35v.8","69v.11","46r.11","82r.9"}
EXCL = {"14v.7","22v.9","37v.12","48r.8","3v.12","98v.10","1r.2","30v.7","47r.1","20r.8"}
EXCL_PREFIX = ("12v.","106v.","63v.","21r.","37v.","38r.","38v.","3v.","4r.","98v.")
chains = {c['chain_id']: c for c in json.loads(show("targets/ljs51corpus/chains_all.json"))}
names = [n for n in subprocess.run(["git","-C",C,"ls-tree","--name-only",REF,"targets/ljs51corpus/keys_eye/"],capture_output=True,text=True).stdout.split() if n.endswith('.json')]
def lines_of(d):
    cl = d.get('cipher_lines') or {}
    if not isinstance(cl,(dict,list)): return []
    vals = list(cl.values()) if isinstance(cl,dict) else list(cl)
    return [' '.join(v) if isinstance(v,list) else v for v in vals]
def plain_of(cid):
    c = chains.get(cid)
    if not c or not isinstance(c.get('plaintext'),dict) or c.get('answered') != 'yes': return None
    return c['plaintext'].get('text') or None
elig = []
for n in names:
    cid = os.path.basename(n)[:-5]
    if cid in MEASURED or cid in EXCL or cid.startswith(EXCL_PREFIX): continue
    d = json.loads(show(n)); L = lines_of(d)
    toks = [t for l in L for t in l.split() if t != '|']
    if not any('|' in l for l in L) or plain_of(cid) is None: continue
    elig.append((len(toks), cid, len(set(toks)), L))
elig.sort(key=lambda x: (-x[0], x[1]))
LEXF = open(B + "modele/CORPUS-LM2.txt").read().strip().split(',')
need = {}
for s, cid, K, L in elig[:30]:
    p = ''.join(words(plain_of(cid)))
    need[cid] = [p[i:i+12] for i in range(len(p)-11)]
allg = set(g for v in need.values() for g in v); found = set()
for f in sorted(set(TRAIN) | set(LEXF)):
    t = ''.join(words(strip_meta(open(CORPUS + f, encoding='utf8', errors='ignore').read())))
    for i in range(len(t)-11):
        g = t[i:i+12]
        if g in allg: found.add(g)
rows = []; kept = 0
for s, cid, K, L in elig[:30]:
    lk = sum(g in found for g in need[cid]) / max(1, len(need[cid]))
    take = (s >= 90 or kept < 10) and lk <= 0.05
    if kept >= 10 and s < 90: take = False
    rows.append((cid, s, K, round(lk,4), 'M' if take else ('fuite' if lk > 0.05 else '-')))
    if take:
        kept += 1
        open(OUT + cid + '.sig', 'w').write('\n'.join(L) + '\n')
with open(OUT + 'SELECTION.tsv', 'w') as f:
    f.write("chaine\tsignes\tclasses\tfuite12\tstatut\n")
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
print(open(OUT + 'SELECTION.tsv').read())
