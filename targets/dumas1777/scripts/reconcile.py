"""Reconcile pass A (forward) and pass B (backward) transcriptions and decode with the frozen key.

    python3 reconcile.py            -> writes readings/auto/<image>.txt and readings/reconcile_summary.tsv

For each image: lines are matched by line tag (Lnn / Rnn); pass B lines are reversed; tokens are aligned with difflib.
Token forms: 123, 123/a (gloss), 457?/487 (uncertain), # (illegible), [x123] (struck), {word}.
Output per line: merged token stream where agreement -> number, disagreement -> <A|B>, plus the decoded letters
(key: key/key_positions.json, sha256 36276e0a...). Unagreed numbers are decoded both ways.
"""
import os, re, json, difflib, glob, unicodedata, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = {int(k): v for k, v in json.load(open(os.path.join(ROOT, 'key', 'key_positions.json')))['positions'].items()}

def letter(n):
    c = KEY.get(n)
    if c is None: return '[%d]' % n
    b = unicodedata.normalize('NFD', c)[0].lower()
    return {'-': '=', '*': '*'}.get(b, b)

def parse(path, backward):
    lines = collections.OrderedDict(); runs = {}
    cur = None
    for raw in open(path, encoding='utf8', errors='ignore'):
        s = raw.rstrip('\n')
        m = re.match(r'#\s*run\s*(\S+)(.*)', s)
        if m: cur = s[1:].strip(); continue
        m = re.match(r'([LR])(\d+[a-z]*)\s*:\s*(.*)', s)
        if not m: continue
        tag = m.group(2).lstrip('0') or '0'
        toks = re.findall(r'\{[^}]*\}|\[x[^\]]*\]|\S+', m.group(3))
        if backward: toks = toks[::-1]
        key = tag
        while key in lines: key += "'"
        lines[key] = toks; runs[key] = cur
    return lines, runs

def num(tok):
    m = re.match(r'^(\d+)', tok)
    return int(m.group(1)) if m else None

def base(tok):
    """number part only, for comparison"""
    t = tok.split('/')[0].rstrip('?')
    return t

def dec(tok):
    if tok.startswith('{'): return tok
    if tok.startswith('[x'): return ''
    n = num(tok)
    if n is None: return '#'
    alt = re.match(r'^\d+\?/(\d+)', tok)
    return letter(n) if not alt else '(%s/%s)' % (letter(n), letter(int(alt.group(1))))

def merge(a, b):
    sm = difflib.SequenceMatcher(a=[base(x) for x in a], b=[base(x) for x in b], autojunk=False)
    out = []; nag = ndis = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(i2 - i1):
                ta, tb = a[i1 + k], b[j1 + k]
                out.append(('=', ta if '?' not in ta else (tb if '?' not in tb else ta), tb)); nag += 1
        else:
            A, B = a[i1:i2], b[j1:j2]
            for k in range(max(len(A), len(B))):
                out.append(('!', A[k] if k < len(A) else '-', B[k] if k < len(B) else '-')); ndis += 1
    return out, nag, ndis

def main():
    os.makedirs(os.path.join(ROOT, 'readings', 'auto'), exist_ok=True)
    summ = ['image\trange\tlines\tagreed\tdisagree\tdecoded_agreed_text_head']
    for adir in sorted(glob.glob(os.path.join(ROOT, 'transcriptions', 'R?_A'))):
        rng = os.path.basename(adir)[:2]
        bdir = adir[:-1] + 'B'
        for fa in sorted(glob.glob(os.path.join(adir, '*.txt'))):
            name = os.path.basename(fa)[:-4]
            fb = os.path.join(bdir, os.path.basename(fa))
            A, ra = parse(fa, False)
            B, rb = parse(fb, True) if os.path.exists(fb) else ({}, {})
            out = [f'# {name}: pass A {fa}\n#        pass B {fb}\n# per line: merged tokens (<A|B> = disagreement), then decode']
            def k_(t):
                m = re.match(r'(\d+)', t); return (int(m.group(1)) if m else 0, t)
            # page-level alignment: pass B lines are ordered top to bottom (by tag) and each reversed
            seqA = []; seqB = []
            for t in sorted(A, key=k_): seqA += [(t, x) for x in A[t]] + [(t, '|')]
            for t in sorted(B, key=k_): seqB += [(t, x) for x in B[t]] + [(t, '|')]
            seqA = [x for x in seqA if x[1] != '|']; seqB = [x for x in seqB if x[1] != '|']
            m, TA, TB = merge([x[1] for x in seqA], [x[1] for x in seqB])
            # attach A line tags
            full = []; ia = 0; curtag = None; toks = []; letters = []; lastrun = None
            def flush():
                if curtag is not None:
                    out.append(f'L{curtag}: ' + ' '.join(toks)); out.append('   => ' + ''.join(letters))
            for st, ta, tb in m:
                tag = seqA[ia][0] if (ta != '-' and ia < len(seqA)) else curtag
                if ta != '-': ia += 1
                if tag != curtag:
                    flush(); toks = []; letters = []; curtag = tag
                    if ra.get(tag) and ra.get(tag) != lastrun:
                        out.append('# ' + ra[tag]); lastrun = ra[tag]; full.append(' / ')
                if st == '=':
                    toks.append(ta); l = dec(ta)
                else:
                    toks.append(f'<{ta}|{tb}>')
                    da = dec(ta) if ta != '-' else ''; db = dec(tb) if tb != '-' else ''
                    l = da if da == db else f'<{da}|{db}>'
                letters.append(l); full.append(l)
            flush()
            tag_all = list(A)
            text = ''.join(full)
            out.append('\n# FULL (agreed letters; <a|b> where passes differ):\n' + text)
            open(os.path.join(ROOT, 'readings', 'auto', name + '.txt'), 'w').write('\n'.join(out) + '\n')
            summ.append(f'{name}\t{rng}\t{len(tag_all)}\t{TA}\t{TB}\t{text[:80]}')
    open(os.path.join(ROOT, 'readings', 'reconcile_summary.tsv'), 'w').write('\n'.join(summ) + '\n')
    print('\n'.join(summ))

main()
