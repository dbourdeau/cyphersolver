"""MESURE UNIQUE (ljs51-22r1-61r3). Ne s'execute qu'avec --hash-poste=<URL ou note> et si mesure/RESULTATS.tsv
n'existe pas. Verifie d'abord gel/MANIFEST.sha256.
Pour chacune des 10 chaines fraiches (transcriptions/SELECTION.tsv, statut M) :
  - solveur MOTS (salex, mode 0, rho=-5, lambda=8, 20 relances, 500 000 iterations, graine 2811) ;
  - solveur CARACTERES de ljs51-aveugle (sa, lambda=8, memes reglages) = comparaison appariee ;
  chacun avec ses 200 temoins (signes melanges, separateurs conserves, random.Random(2811*100003+i), graine 2811+i).
Accord en caracteres (difflib, plus longue des deux, lettres seules) avec le clair du compilateur
(chains_all.json plaintext.text, normalise). Critere par chaine et par solveur : accord >= 0.85 ET >= meilleur temoin + 0.30.
Hypothese H soutenue si (validees MOTS) - (validees CARACTERES) >= 2."""
import sys, os, json, random, difflib, subprocess, hashlib, time
from multiprocessing import Pool
sys.path.insert(0, "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/scripts")
from common import LETTERS, words
from sigparse import read_sig
B = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-22r1-61r3/"
AV = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/"
C = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/cyphersolver-pr/clone"
REF = "d8ac608093e1149f9456eaa2c99bb456ca0abc92"
LM = AV + "modele/lm4_sp.bin"; LEX = B + "modele/lex.bin"
RHO, LAM, R, IT, SEED, NW = "-5", "8", "20", "500000", 2811, 200
def show(p): return subprocess.run(["git","-C",C,"show",f"{REF}:{p}"],capture_output=True,text=True,check=True).stdout
def acc(a, b):
    a = a.replace(' ', ''); b = b.replace(' ', '')
    return sum(x.size for x in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks())/max(len(a),len(b),1)
def wacc(a, b):
    a = a.split(); b = b.split()
    return sum(x.size for x in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks())/max(len(a),len(b),1)
def job(args):
    solver, cid, i, toks, K = args
    t = list(toks); seed = SEED
    if i > 0:
        rnd = random.Random(SEED*100003+i); pos = [j for j, x in enumerate(toks) if x >= 0]
        vals = [toks[j] for j in pos]; rnd.shuffle(vals)
        for j, v in zip(pos, vals): t[j] = v
        seed = SEED + i
    inp = f"{len(t)}\n{' '.join(map(str,t))}\n{K}\n"
    if solver == 'mots': cmd = [B+"scripts/salex", LM, LEX, RHO, LAM, R, IT, str(seed), "0"]
    else: cmd = [AV+"scripts/sa", LM, LAM, R, IT, str(seed)]
    out = subprocess.run(cmd, input=inp, capture_output=True, text=True, check=True).stdout.split('\n')
    d = out[0].split()[0]; key = list(map(int, out[1].split()))
    s = t[::-1] if d == '1' else t
    return solver, cid, i, int(d), ''.join(' ' if x < 0 else LETTERS[key[x]-1] for x in s)
def main():
    arg = [a for a in sys.argv[1:] if a.startswith('--hash-poste=')]
    if not arg: sys.exit("refus : --hash-poste=<URL du commentaire #1023> manquant (empreinte non publiee)")
    out = B + "mesure/RESULTATS.tsv"
    if os.path.exists(out): sys.exit("refus : RESULTATS.tsv existe deja (mesure unique)")
    for line in open(B + "gel/MANIFEST.sha256"):
        h, p = line.split(None, 1); p = p.strip()
        if hashlib.sha256(open(B + p, 'rb').read()).hexdigest() != h: sys.exit("refus : fichier gele modifie : " + p)
    open(B + "mesure/DEBUT.txt", 'w').write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + "\n" + arg[0] + "\n")
    sel = [l.split('\t') for l in open(B + "transcriptions/SELECTION.tsv").read().split('\n')[1:] if l]
    chains = [r[0] for r in sel if r[4] == 'M']
    allc = {c['chain_id']: c for c in json.loads(show("targets/ljs51corpus/chains_all.json"))}
    ref = {cid: ' '.join(words(allc[cid]['plaintext']['text'])) for cid in chains}
    jobs = []; meta = {}
    for cid in chains:
        toks, K, labels = read_sig(B + f"transcriptions/{cid}.sig"); meta[cid] = (toks, K)
        for solver in ('mots', 'car'): jobs += [(solver, cid, i, toks, K) for i in range(NW+1)]
    t0 = time.time(); res = {}
    with Pool(8) as p:
        for solver, cid, i, d, dec in p.imap_unordered(job, jobs, chunksize=1): res[(solver, cid, i)] = (d, dec)
    rows = []
    for cid in chains:
        toks, K = meta[cid]; n = sum(1 for t in toks if t >= 0)
        for solver in ('mots', 'car'):
            d, dec = res[(solver, cid, 0)]
            a = acc(dec, ref[cid]); w = wacc(dec, ref[cid])
            wit = [acc(res[(solver, cid, i)][1], ref[cid]) for i in range(1, NW+1)]
            mw = max(wit); mean = sum(wit)/NW; rank = 1 + sum(x >= a for x in wit)
            ok = a >= 0.85 and a >= mw + 0.30
            rows.append([cid, solver, n, K, d, round(a,4), round(w,4), round(mw,4), round(mean,4), rank, 'OUI' if ok else 'NON', dec])
    nv = {s: sum(1 for r in rows if r[1] == s and r[10] == 'OUI') for s in ('mots', 'car')}
    with open(out, 'w') as f:
        f.write("chaine\tsolveur\tsignes\tclasses\tsens_inverse\taccord_car\taccord_mots\tmeilleur_temoin\tmoyenne_temoins\trang_sur_201\tvalide\tdecodage_aveugle\n")
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    verdict = "H SOUTENUE" if nv['mots'] - nv['car'] >= 2 else "H NON SOUTENUE"
    with open(B + "mesure/BILAN.md", 'w') as f:
        f.write(f"# Bilan de la mesure unique\n\nValidees : solveur MOTS {nv['mots']}/10 ; solveur CARACTERES {nv['car']}/10.\n\n**{verdict}** (seuil : difference >= 2).\n\n")
        f.write("| chaine | signes | classes | MOTS accord | MOTS temoin max | MOTS valide | CAR accord | CAR temoin max | CAR valide |\n|---|---|---|---|---|---|---|---|---|\n")
        for cid in chains:
            m = [r for r in rows if r[0] == cid and r[1] == 'mots'][0]; c = [r for r in rows if r[0] == cid and r[1] == 'car'][0]
            f.write(f"| {cid} | {m[2]} | {m[3]} | {m[5]:.2f} | {m[7]:.2f} | {m[10]} | {c[5]:.2f} | {c[7]:.2f} | {c[10]} |\n")
    open(B + "mesure/HEURE.txt", 'w').write(f"mesure lancee apres publication : {arg[0]}\nfin UTC {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\nduree {time.time()-t0:.0f}s\n")
    print(open(B + "mesure/BILAN.md").read())
if __name__ == '__main__': main()
