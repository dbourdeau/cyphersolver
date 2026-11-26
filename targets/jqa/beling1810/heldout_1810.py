"""Held-out test of ../code_table.tsv (frozen, unchanged) on the coded passages of JQA's despatches of 1810.

python heldout_1810.py [--shuffles 100] [--detail] [--codes FILE]   (FILE defaults to codes_1810.txt)

Plan and pass mark: PLAN.md (hash in PLAN.sha256, written before the first run). Uses align.py's own alignment,
imported unchanged, with the table alone (no pairs_jqa.txt, no 1810 material). For each passage of codes_1810.txt:
- agreement = valued groups the alignment places on the witness letters ("known") / valued groups
  ("known" + contradicted + dropped);
- coverage = groups with a value in the table / all groups;
- strict read words: a witness word counts as read only when every letter comes from a "known" group; a word that is
  wholly clear text in the manuscript is not a coded word and is left out.
Control: the same run with the table's value sets shuffled among its numbers (seed 20261122).
PASS: pooled agreement >= 0.80 and >= best shuffled + 0.30. Python standard library only.
"""
import os, re, sys, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import align as A  # noqa: E402

def run(blocks, tab):
    rows = []
    for b in blocks:
        out, _ = A.align(b['toks'], b['plain'], tab)
        k = mis = new = 0
        P = A.norm(b['plain'])
        status = []
        for how, tok, letters in out:
            isnum = tok is not None and re.match(r'\d', tok)
            n = int(re.match(r'\d+', tok).group()) if isnum else None
            if isnum:
                valued = n in tab
                if how == 'known': k += 1
                elif valued: mis += 1
                else: new += 1
            st = 'K' if how == 'known' else 'C' if how == 'word' else 'H'
            status += [st] * len(letters)
        # trailing/leading plaintext not consumed by the alignment is a hole
        status += ['H'] * (len(P) - len(status))
        words = [A.norm(w) for w in b['plain'].split()]
        pos = 0; read = coded = 0
        for w in words:
            if not w: continue
            seg = status[pos:pos + len(w)]; pos += len(w)
            if seg and all(s == 'C' for s in seg): continue
            coded += 1
            if all(s in 'KC' for s in seg): read += 1
        rows.append(dict(ref=b['ref'], known=k, mis=mis, new=new, words=coded, read=read, out=out))
    return rows

def pooled(rows):
    k = sum(r['known'] for r in rows); m = sum(r['mis'] for r in rows)
    return k / (k + m) if k + m else 0.0

def main():
    args = sys.argv[1:]
    nsh = int(args[args.index('--shuffles') + 1]) if '--shuffles' in args else 100
    tab = A.load_table([os.path.join(os.path.dirname(HERE), 'code_table.tsv')])
    codes = args[args.index('--codes') + 1] if '--codes' in args else os.path.join(HERE, 'codes_1810.txt')
    blocks = A.parse(codes)
    rows = run(blocks, tab)
    real = pooled(rows)
    print('passage\tgroups\tvalued\tknown\tcontradicted_or_dropped\tagreement\tcoverage\tcoded_words\tread_words_strict')
    for r in rows:
        g = r['known'] + r['mis'] + r['new']; v = r['known'] + r['mis']
        print(f"{r['ref']}\t{g}\t{v}\t{r['known']}\t{r['mis']}\t{r['known']/v if v else 0:.3f}\t{v/g if g else 0:.3f}\t{r['words']}\t{r['read']}")
    by = {}
    for r in rows:
        d = r['ref'].split(',')[0]
        a = by.setdefault(d, [0, 0, 0, 0, 0]); a[0] += r['known']; a[1] += r['mis']; a[2] += r['new']; a[3] += r['words']; a[4] += r['read']
    print('\ndespatch\tgroups\tagreement\tcoverage\tread_words_strict')
    for d, (k, m, n, w, rd) in by.items():
        print(f"{d}\t{k+m+n}\t{k/(k+m):.3f}\t{(k+m)/(k+m+n):.3f}\t{rd}/{w} = {rd/w:.3f}")
    K = sum(r['known'] for r in rows); M = sum(r['mis'] for r in rows); N = sum(r['new'] for r in rows)
    W = sum(r['words'] for r in rows); RD = sum(r['read'] for r in rows)
    print(f"\nall: groups {K+M+N}, valued {K+M}, agreement {real:.3f}, coverage {(K+M)/(K+M+N):.3f}, read words {RD}/{W} = {RD/W:.3f}")
    rng = random.Random(20261122)
    ks = sorted(tab); vs = [tab[x] for x in ks]; nulls = []
    for i in range(nsh):
        rng.shuffle(vs)
        nulls.append(pooled(run(blocks, dict(zip(ks, vs)))))
    nulls.sort()
    print(f"shuffled tables ({nsh}): best {nulls[-1]:.3f}, median {nulls[len(nulls)//2]:.3f}")
    ok = real >= 0.80 and real >= nulls[-1] + 0.30
    print('PASS' if ok else 'MISS', '(pass mark: agreement >= 0.80 and >= best shuffled + 0.30)')
    if '--detail' in args:
        for r in rows:
            print('\n@', r['ref'])
            print(' '.join(f"{t}={l}" if h == 'known' else f"{t}~{l}!" if h in ('mis', 'new') else (f"[{l}]" if h == 'skip' else f"{t}" if h == 'word' else f"({t})") for h, t, l in r['out']))

if __name__ == '__main__':
    main()
