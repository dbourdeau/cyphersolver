"""Mesure unique préenregistrée (PREREG.md). Usage : python3 -I measure.py <avenel_figures_V.txt> <out.json>
Clé : celle de Daniel (targets/richelieu/final.py, commit 9736c436), recopiée ci-dessous telle quelle (lettres + codes de mots).
Portion de test : CLIV + CLV (complétée par CLIII si < 300 signes notés)."""
import re, sys, json, random, unicodedata
KEY = {'10':'c','11':'b','12':'g','13':'p','14':'l','15':'o','16':'r','17':'f','18':'t','19':'a','20':'d','21':'i',
       '22':'n','23':'h','24':'m','25':'s','26':'u','27':'e','28':'q','29':'a','30':'e','31':'i','32':'o','33':'u',
       '34':'a','35':'e','36':'i','37':'o','38':'u','39':'et','40':'de','42':'la'}
LETTER_FIGS = [str(n) for n in range(10, 39)]
TEST, RESERVE, MIN_SIGNS = ['CLIV', 'CLV'], 'CLIII', 300
SEED, NWIT = 20261119, 200

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.translate(str.maketrans('jvy', 'iui'))

def parse(path):
    t = open(path, encoding='utf-8').read()
    letters = {}
    for m in re.finditer(r"== (\S+) \|(.*?)(?=\n== |\Z)", t, re.S):
        name, block = m.group(1), m.group(2)
        pages = []
        for l in block.splitlines():
            mm = re.match(r"# p\.(\d+): (.*)", l)
            if mm:
                notes = {}
                for part in mm.group(2).split(' | '):
                    pm = re.match(r"(\d+) (.*)", part.strip())
                    if pm: notes[int(pm.group(1))] = pm.group(2)
                pages.append(notes)
        body = '\n'.join(l for l in block.splitlines() if not l.startswith('#'))
        segs, cur, pi, prev = [], [], 0, None
        for mm in re.finditer(r"\[([^\]]*)\]|\{(\d+)\}|\^(\d+)", body):
            if mm.group(1) is not None:
                toks = [x.replace('‹?›', '') for x in mm.group(1).split() if re.fullmatch(r"~?\d+(‹\?›)?", x)]
                if toks: cur.append(('run', toks))
            elif mm.group(2): cur.append(('code', mm.group(2)))
            else:
                n = int(mm.group(3))
                if prev is not None and n <= prev: pi += 1
                prev = n
                gloss = pages[pi].get(n) if pi < len(pages) else None
                segs.append({'items': cur, 'call': n, 'page_idx': pi, 'gloss': gloss}); cur = []
        letters[name] = segs
    return letters

def dec(toks, key):
    out = ''
    for t in toks:
        d = t.startswith('~'); f = t.lstrip('~')
        v = key.get(f, '?')
        out += (v * 2 if d and len(v) == 1 else v)
    return out

def semi(r, g):
    # distance d'édition de r contre la meilleure sous-chaîne de g (extrémités de g gratuites)
    prev = [0] * (len(g) + 1)
    for i in range(1, len(r) + 1):
        cur = [i] + [0] * len(g)
        for j in range(1, len(g) + 1):
            cur[j] = min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + (r[i-1] != g[j-1]))
        prev = cur
    return min(prev)

def score(segs, key):
    dist = n = signs = 0
    for s in segs:
        if not s['gloss']: continue
        g = norm(s['gloss'])
        for kind, x in s['items']:
            if kind != 'run': continue
            r = dec(x, key)
            dist += semi(r, g); n += len(r); signs += len(x)
    return (1 - dist / n if n else None), signs, n

def main():
    L = parse(sys.argv[1])
    test = TEST[:]
    segs = [s for t in test for s in L[t]]
    _, signs, _ = score(segs, KEY)
    if signs < MIN_SIGNS:
        test.append(RESERVE); segs = [s for t in test for s in L[t]]
    acc, signs, nchar = score(segs, KEY)
    rng = random.Random(SEED); vals = [KEY[f] for f in LETTER_FIGS]; wit = []
    for _ in range(NWIT):
        v = vals[:]; rng.shuffle(v)
        k = dict(KEY); k.update(dict(zip(LETTER_FIGS, v)))
        wit.append(score(segs, k)[0])
    best = max(wit)
    res = {'test_letters': test, 'signs_scored': signs, 'decoded_chars': nchar, 'acc_key': round(acc, 4),
           'best_witness': round(best, 4), 'mean_witness': round(sum(wit) / len(wit), 4),
           'threshold_abs': 0.85, 'threshold_rel': round(best + 0.30, 4),
           'PASS': bool(acc >= 0.85 and acc >= best + 0.30),
           'segments_without_gloss': sum(1 for s in segs if not s['gloss'])}
    json.dump(res, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False); print(json.dumps(res, ensure_ascii=False, indent=1))
if __name__ == '__main__': main()
