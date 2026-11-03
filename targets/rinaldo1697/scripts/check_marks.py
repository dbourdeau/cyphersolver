"""Rebuild the decryption of cc. 73r-73v from transcription_c73.txt and key.tsv, check the marked reading against it
(exit 1 on any unmarked departure), count words, and run the held-out test (key frozen on 73r, applied to 73v):
(a) graded against a key-free reading of the 73v gloss (validation/gloss_raw_V.txt), (b) scored with a small Italian
letter-bigram model; both against 1000 shuffled tables. Standard library only."""
import pathlib, re, sys, random, math, collections
R = pathlib.Path(__file__).resolve().parent.parent
def key(frozen=False):
    k = {}
    for l in (R / 'key.tsv').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or l.startswith('group') or not l.strip(): continue
        g, v, st = l.split('\t')[:3]
        if frozen and st != 'frozen': continue
        k[g] = v
    return k
def lines():
    for l in (R / 'transcription_c73.txt').read_text(encoding='utf8').splitlines():
        if l[:1] in 'LV' and '\t' in l:
            n, t = l.split('\t'); yield n, [x for x in t.split() if x not in ('.', ',', '-', '[TXT]')]
def units(gs, k):
    return [(g.rstrip('?'), k.get(g.rstrip('?'), '[' + g.rstrip('?') + ']'), g.endswith('?')) for g in gs]
def main():
    k = key(); out = []; bad = []
    rd = {l.split('\t')[0]: l.split('\t')[1] for l in (R / 'reading_marked_c73.txt').read_text(encoding='utf8').splitlines() if l[:1] in 'LV'}
    words = collections.Counter()
    for n, gs in lines():
        us = units(gs, k)
        out.append(f'{n}\tgroups\t' + ' '.join(g for g, _, _ in us)); out.append(f'{n}\tvalues\t' + ' '.join(v + ('?' if d else '') for _, v, d in us))
        t = rd.get(n, ''); i = 0
        for it in re.findall(r'\[[^\]]*\]|\{[^}]*\}|[a-z]', t.lower()):
            if it.startswith('{+'): continue
            if i >= len(us): bad.append(f'{n}: reading longer than the groups at {it}'); break
            g, v, d = us[i]
            if it.startswith('['):
                if it[1:].split()[0] != g.lower(): bad.append(f'{n}: code {it} but group {g}')
            elif it.startswith('{?'):
                if not d or it[2] != v: bad.append(f'{n}: {it} not on a doubtful group of that value ({g}={v})')
            else:
                if v != it: bad.append(f'{n}: unmarked departure: reading {it}, group {g}={v}')
                elif d: bad.append(f'{n}: {it} rests on doubtful group {g} without {{?}}')
            i += 1
        if i != len(us): bad.append(f'{n}: {len(us) - i} groups not covered')
    (R / 'decryption_c73.txt').write_text('# rebuilt by scripts/check_marks.py\n' + '\n'.join(out) + '\n', encoding='utf8')
    for b in bad: print('FAIL', b)
    # words: a line ending in '-' joins the next line's '-' piece; brackets are kept whole
    full = ''
    for n in [x for x in rd]:
        t = rd[n].strip()
        full = full[:-1] + t[1:] if full.endswith('-') and t.startswith('-') else (full + ' ' + t)
    keep = []
    prot = re.sub(r'\[[^\]]*\]', lambda m: (keep.append(m[0]), '#%d#' % (len(keep) - 1))[1], full)
    for w in re.split(r'[\s.,;:\-]+', prot):
        if not w: continue
        br = [keep[int(i)] for i in re.findall(r'#(\d+)#', w)]
        kind = 'plain'
        if '{' in w: kind = 'marked'
        if any(not re.match(r'\[\S+ \?', b) for b in br) and kind == 'plain': kind = 'gloss_code'
        if any(re.match(r'\[\S+ \?\S', b) for b in br): kind = 'code_proposed'
        if any(re.fullmatch(r'\[\S+ \?\]', b) for b in br): kind = 'code_open'
        words[kind] += 1
    tot_w = sum(words.values()); sense = words['plain'] + words['marked'] + words['gloss_code']
    print('words in the cipher reading:', dict(sorted(words.items())), 'total', tot_w)
    print(f'read as sense (plain + marked + gloss_code): {sense}/{tot_w} ({100*sense/tot_w:.1f}%)')
    # held-out
    fk = key(True); train = (R / 'validation' / 'italian_train.txt').read_text(encoding='utf8').lower()
    train = re.sub(r'[^a-z]', '', train)
    bg = collections.Counter(zip(train, train[1:])); uni = collections.Counter(train)
    lp = lambda a, b: math.log((bg[(a, b)] + 0.5) / (uni[a] + 13))
    seqs = []
    for n, gs in lines():
        if n.startswith('V'):
            s = [g.rstrip('?') for g in gs if re.fullmatch(r'\d\d', g.rstrip('?'))]
            seqs.append(s)
    tot = sum(len(s) for s in seqs); cov = sum(1 for s in seqs for g in s if g in fk)
    def score(m):
        sc = 0; c = 0
        for s in seqs:
            t = [m[g] for g in s if g in m]
            for a, b in zip(t, t[1:]): sc += lp(a, b); c += 1
        return sc / max(c, 1)
    real = score(fk); vals = list(fk.values()); random.seed(1); better = 0; sh = []
    for _ in range(1000):
        random.shuffle(vals); m = dict(zip(fk.keys(), vals)); x = score(m); sh.append(x); better += x >= real
    # (a) against the key-free reading of the 73v gloss
    gl = []
    for l in (R / 'validation' / 'gloss_raw_V.txt').read_text(encoding='utf8').splitlines():
        p = l.split(chr(9))
        if len(p) == 3 and p[1] == 'M':
            for pr in p[2].split(';'):
                if '=' not in pr: continue
                num, txt = pr.split('=', 1); num = num.strip()
                txt = re.sub(r'[()?\[\]]', '', txt.split('(')[0] if '(' in txt and len(txt.split('(')[0].strip()) == 1 else txt).strip().lower()
                txt = txt.replace('ſ', 's').replace('v', 'u')
                if num in fk and len(txt) == 1 and txt.isalpha(): gl.append((num, txt))
    agree = lambda m: sum(1 for g, x in gl if m[g].replace('v', 'u') == x)
    ra = agree(fk); vals2 = list(fk.values()); random.seed(2); sa = []
    for _ in range(1000):
        random.shuffle(vals2); sa.append(agree(dict(zip(fk.keys(), vals2))))
    print(f'held-out 73v vs key-free gloss reading: {ra}/{len(gl)} gloss letters agree with the frozen key ({100*ra/len(gl):.1f}%); '
          f'shuffled tables mean {sum(sa)/len(sa):.1f}, max {max(sa)}')
    print(f'held-out 73v: {tot} letter groups, {cov} have a frozen value ({100*cov/tot:.1f}%); mean bigram log-prob frozen key {real:.3f}, '
          f'shuffled tables mean {sum(sh)/len(sh):.3f}, max {max(sh):.3f}; shuffled >= frozen: {better}/1000')
    sys.exit(1 if bad else 0)
main()
