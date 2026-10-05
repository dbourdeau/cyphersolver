"""Joint context scoring of R1892's recurring word signs (3 Oct 2026).

For each sign, every candidate word (the 400 commonest words of the nl corpus + Gedenkstukken I-II) is put into
ALL its occurrences at once; the score is the summed nl-modern log-prob of a window of up to 20 read letters each
side (other unread signs cut the window). Prints the top candidates per sign with per-occurrence ranks, so a value
can be accepted only when it fits every occurrence.
usage: python solve_signs.py '<H>' '<hook>' ... [+=word1,word2 to add and always show candidates]
"""
import os, sys, re, glob, collections, importlib.util
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('ap', os.path.join(HERE, 'apply.py'))
ap = importlib.util.module_from_spec(spec); spec.loader.exec_module(ap)
m = lm.load('nl-modern', spaces=False)
CTX = 20


def toks():
    out = []
    for line in open(os.path.join(HERE, 'transcription_p2.txt'), encoding='utf8'):
        if line.lstrip().startswith('{'):
            continue
        for kind, lab, v in ap.tokens(line):
            if kind == 'note':
                if lab.startswith('['):          # bracketed clear words are real text
                    w = re.sub(r'[^a-z ]', '', lab.lower())
                    if w and '..' not in lab and '?' not in lab:
                        out.append(('clear', lab, w.replace(' ', '')))
                continue
            out.append((kind, lab, lm.norm(v, spaces=False).replace('y', 'ij') if v else None))
    return out


def vocab(n=400):
    c = collections.Counter()
    c.update(re.findall(r'[a-z]+', lm.norm(open(os.path.join(HERE, '..', '..', 'lang', 'corpora', 'nl-gutenberg.txt'), encoding='utf8', errors='replace').read())))
    for g in glob.glob(os.path.join(HERE, '..', 'r2242', 'gs_corpus', 'gs*_*.txt')):
        c.update(re.findall(r'[a-z]+', lm.norm(open(g, encoding='utf8').read())))
    return [w for w, _ in c.most_common(n) if len(w) > 1 or w in ('u',)]


def occurrences(T, sign):
    occ = []
    for i, (k, lab, v) in enumerate(T):
        if k == 'sign' and lab == sign:
            L = ''; j = i - 1
            while j >= 0 and T[j][2] is not None and len(L) < CTX:
                L = T[j][2] + L; j -= 1
            R = ''; j = i + 1
            while j < len(T) and T[j][2] is not None and len(R) < CTX:
                R = R + T[j][2]; j += 1
            occ.append((L[-CTX:], R[:CTX]))
    return occ


def score(L, w, R):
    s = L + w + R
    return m.score(s) - m.score(L) - m.score(R)   # gain of the joined string over its parts


if __name__ == '__main__':
    T = toks(); V = vocab()
    extra = [a[2:] for a in sys.argv[1:] if a.startswith('+=')]
    V = V + [w for x in extra for w in x.split(',') if w not in V]
    for sign in [a for a in sys.argv[1:] if not a.startswith('+=')]:
        occ = occurrences(T, sign)
        print(f'== {sign}: {len(occ)} occurrences')
        for L, R in occ:
            print(f'   ...{L} [ ] {R}...')
        tab = {w: [score(L, w, R) for L, R in occ] for w in V}
        ranks = [sorted(V, key=lambda w: -tab[w][k]) for k in range(len(occ))]
        tot = sorted(V, key=lambda w: -sum(tab[w]))
        show = tot[:10] + [w for x in extra for w in x.split(',') if w not in tot[:10]]
        for w in show:
            print(f'   {w:12s} {sum(tab[w]):8.1f}  ranks per occurrence: {[r.index(w) + 1 for r in ranks]}')
