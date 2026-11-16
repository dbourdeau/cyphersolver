"""R23 b3: split a kurtz1639 reading into clear and cipher words by aligning it to read/<rec>.txt
({clear} and [cipher decode]), then count holes per side by the v2_score rules."""
import sys, re, os, difflib
W = sys.argv[1]   # repository root; usage: python research/reading_audit/r23_kurtz_split.py . R3811 [R3812+ ...] (+ prints the labelled words)
sys.path.insert(0, W+'/research/reading_audit'); sys.path.insert(0, W+'/docs')
os.chdir(W)
import b06_align as b6, v2_score as v2
WORD = re.compile(r'[^\W\d_]+')

def lstream(rec):
    """normalised stream with a label per char: 'C' clear, 'X' cipher; '#' = a hole mark in the transcription/decode."""
    s, lab = [], []
    for l in b6.sections(rec):
        if l.startswith('#'): continue
        l = re.sub(r'\{[^{}]*\[[^\]]*\][^{}]*\}', ' ', l)
        l = l.replace('...', '#').replace('…', '#').replace('?', '#')
        cur = None
        for c in l:
            if c == '{': cur = 'C'; continue
            if c == '}': cur = None; continue
            if c == '[': cur = 'X'; continue
            if c == ']': cur = None; continue
            n = c if c == '#' else b6.norm(c)
            for ch in n:
                s.append(ch); lab.append(cur or 'C')
    return ''.join(s), lab

def run(rec, verbose=False):
    s, lab = lstream(rec)
    body = b6.body(rec)
    body = '\n'.join(l for l in body.split('\n') if not l.lstrip().startswith(('|', '#', '>')))
    b = v2.holes(body)
    toks = [m.group(0) for m in re.finditer(r'\[\?\]|\(\?\)|[^\W\d_]+', b)]
    # concat words
    r, spans = '', []
    for k, t in enumerate(toks):
        if t in ('[?]', '(?)'): continue
        a = len(r); r += b6.norm(t); spans.append((k, a, len(r)))
    sm = difflib.SequenceMatcher(None, r, s, autojunk=False)
    m = [None] * len(r)
    for blk in sm.get_matching_blocks():
        if blk.size >= 3:
            for i in range(blk.size): m[blk.a + i] = blk.b + i
    label = {}
    pos = {}   # token -> (first stream pos, last stream pos)
    for k, a, e in spans:
        ps = [m[i] for i in range(a, e) if m[i] is not None]
        if ps:
            c = sum(lab[p] == 'X' for p in ps)
            label[k] = 'X' if c * 2 >= len(ps) else 'C'
            pos[k] = (min(ps), max(ps))
    # unmatched words: label from neighbours in stream
    ks = [k for k, _, _ in spans]
    for i, k in enumerate(ks):
        if k in label: continue
        prev = next((pos[j] for j in reversed(ks[:i]) if j in pos), None)
        nxt = next((pos[j] for j in ks[i+1:] if j in pos), None)
        lo = prev[1] + 1 if prev else 0; hi = nxt[0] if nxt else len(s)
        seg = lab[lo:hi] if hi > lo else []
        label[k] = 'X' if (not seg or 'X' in seg) else 'C'
    # holes: by the gap in the stream between neighbouring matched words
    holesX = holesC = dX = dC = 0
    for k, t in enumerate(toks):
        if t not in ('[?]', '(?)'): continue
        if t == '(?)':
            j = max((x for x in ks if x < k), default=None)
            if j is not None and label.get(j) == 'C': dC += 1
            else: dX += 1
            continue
        pj = max((x for x in pos if x < k), default=None)
        nj = min((x for x in pos if x > k), default=None)
        lo = pos[pj][1] + 1 if pj is not None else 0
        hi = pos[nj][0] if nj is not None else len(s)
        seg = lab[lo:hi] if hi > lo else []
        # neighbours' labels when the gap is empty
        nb = [label[x] for x in (pj, nj) if x is not None]
        if seg and 'X' not in seg: holesC += 1
        elif not seg and nb and all(x == 'C' for x in nb): holesC += 1
        else: holesX += 1
    wX = sum(1 for k in ks if label[k] == 'X'); wC = len(ks) - wX
    tot = (len(ks), holesX + holesC, dX + dC)
    sh = lambda w, h, d: round(1 - (h + d) / (w + h), 3) if w + h else None
    print(f"{rec}: whole body words {tot[0]} holes {tot[1]} doubt {tot[2]} share {sh(*tot)} | cipher words {wX} holes {holesX} doubt {dX} share {sh(wX,holesX,dX)} | clear words {wC} holes {holesC} doubt {dC}")
    if verbose:
        out = []
        for k, t in enumerate(toks):
            out.append(t if t in ('[?]','(?)') else (t.upper() if label[k]=='X' else t.lower()))
        print(' '.join(out)[:3000])

for rec in sys.argv[2:]:
    run(rec.strip('+'), rec.endswith('+'))
