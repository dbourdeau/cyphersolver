"""Encipher b189's reading of the clear drafts in LASA A 1 Nr. 529 with the frozen KEY_v2 (reciprocal)
and compare letter by letter with our frozen transcriptions of f.5 and f.6 (Nr. 530).
Standard library only. Usage: python3 -I scripts/compare_nr529.py (run from the target folder)."""
import os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS = 'az bs cq de fn go hu ir ky lt mx pw'.split()
ENC = {}
for p in PAIRS:
    ENC[p[0]] = p[1]; ENC[p[1]] = p[0]

def enc(w):
    return ''.join(ENC.get(c, '?') for c in w)

def tokens(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#'):
            continue
        out += [t for t in line.split() if t != '|']
    return out

def align(a, b):
    """Levenshtein alignment; returns (matches, subs, ins, dels) turning a (expected) into b (transcribed)."""
    n, m = len(a), len(b)
    D = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0] = i
    for j in range(m+1): D[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+(a[i-1] != b[j-1]))
    i, j = n, m; mt = sb = ins = de = 0
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i-1][j-1]+(a[i-1] != b[j-1]):
            if a[i-1] == b[j-1]: mt += 1
            else: sb += 1
            i -= 1; j -= 1
        elif i > 0 and D[i][j] == D[i-1][j]+1:
            de += 1; i -= 1
        else:
            ins += 1; j -= 1
    return mt, sb, ins, de

def subs_list(a, b):
    n, m = len(a), len(b)
    D = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0] = i
    for j in range(m+1): D[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+(a[i-1] != b[j-1]))
    i, j = n, m; out = []
    while i > 0 and j > 0:
        if D[i][j] == D[i-1][j-1]+(a[i-1] != b[j-1]):
            if a[i-1] != b[j-1]: out.append(a[i-1] + '>' + b[j-1])
            i -= 1; j -= 1
        elif D[i][j] == D[i-1][j]+1: i -= 1
        else: j -= 1
    return out

def control(pairs, seed, n=1000):
    import random
    rng = random.Random(seed)
    letters = sorted(ENC)
    best = 0; ge = 0
    pr = [(p.rstrip('?'), c.replace('+', '')) for c, p in pairs if p != '-']
    tot = sum(len(p) for p, _ in pr)
    true = sum(align(enc(p), t)[0] for p, t in pr)
    for _ in range(n):
        L = letters[:]; rng.shuffle(L)
        K = {}
        for k in range(0, len(L), 2):
            K[L[k]] = L[k+1]; K[L[k+1]] = L[k]
        sc = sum(align(''.join(K.get(ch, '?') for ch in p), t)[0] for p, t in pr)
        best = max(best, sc); ge += sc >= true
    return true, tot, best, ge, n

def run(name, pairs_file, tx_file, out):
    pairs = []
    for line in open(pairs_file, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        c, p = line.rstrip('\n').split('\t')
        pairs.append((c, p))
    seq = [t for c, _ in pairs for t in c.split('+')]
    tx = tokens(tx_file)
    assert seq == tx, 'pairs file does not follow the frozen transcription word for word'
    T = dict(words=0, exact=0, letters=0, match=0, sub=0, ins=0, dele=0, unaligned=0, doubt=0)
    T_sure = dict(words=0, exact=0, letters=0, match=0)
    out.append('## %s' % name)
    out.append('cipher_tx\tclear_draft\tclear_enciphered_KEY_v2\tmatch\tsub\tins\tdel\texact')
    for c, p in pairs:
        if p == '-':
            T['unaligned'] += 1
            out.append('%s\t-\t-\t\t\t\t\tnot in draft' % c); continue
        doubt = p.endswith('?'); clear = p.rstrip('?')
        e = enc(clear); t = c.replace('+', '')
        mt, sb, ins, de = align(e, t)
        ex = int(e == t)
        T['words'] += 1; T['exact'] += ex; T['letters'] += len(e); T['match'] += mt
        T['sub'] += sb; T['ins'] += ins; T['dele'] += de; T['doubt'] += doubt
        if not doubt:
            T_sure['words'] += 1; T_sure['exact'] += ex; T_sure['letters'] += len(e); T_sure['match'] += mt
        out.append('%s\t%s\t%s\t%d\t%d\t%d\t%d\t%s' % (c, p, e, mt, sb, ins, de, 'yes' if ex else 'no'))
    out.append('')
    out.append('%s totals: cipher words in frozen file %d; aligned to the draft %d (of which %d with a doubtful clear reading); not in draft %d' % (
        name, len(tx), T['words'], T['doubt'], T['unaligned']))
    out.append('  words exact: %d/%d = %.2f%%' % (T['exact'], T['words'], 100*T['exact']/T['words']))
    out.append('  letters: matches %d of %d enciphered-clear letters = %.2f%% (substitutions %d, letters missing from tx %d, extra letters in tx %d)' % (
        T['match'], T['letters'], 100*T['match']/T['letters'], T['sub'], T['dele'], T['ins']))
    out.append('  excluding doubtful clear readings: words exact %d/%d = %.2f%%; letters %d/%d = %.2f%%' % (
        T_sure['exact'], T_sure['words'], 100*T_sure['exact']/T_sure['words'], T_sure['match'], T_sure['letters'], 100*T_sure['match']/T_sure['letters']))
    from collections import Counter
    C = Counter()
    for c, p in pairs:
        if p != '-':
            C.update(subs_list(enc(p.rstrip('?')), c.replace('+', '')))
    out.append('  substitutions (expected cipher letter > letter in our transcription): ' + ', '.join('%s x%d' % kv for kv in C.most_common()))
    for seed in (20261112, 7):
        true, tot, best, ge, n = control(pairs, seed)
        out.append('  control, %d random reciprocal keys at seed %d: true %d/%d letters; best random %d; random >= true %d/%d' % (n, seed, true, tot, best, ge, n))
    out.append('')
    return T

out = ['# Frozen KEY_v2 (gloss/KEY_lasa_v2.txt, md5 c8fade56) applied to b189 reading of the Nr. 529 clear drafts; compared with frozen Nr. 530 transcriptions.',
       '# The draft wording is not always the wording that was enciphered: words the cipher clerk changed count against us here.', '']
run('f.5 vs Nr. 529 frame 875 (fol. 801r, ad Diarium No. 31)', os.path.join(HERE, 'nr529/f5_vs_frame875_pairs.tsv'),
    os.path.join(HERE, 'transcriptions/f5_frame8_R1_v2_training.txt'), out)
run('f.6 vs Nr. 529 frames 881-882 (fol. 807r-v, ad Diarium No. 32)', os.path.join(HERE, 'nr529/f6_vs_frame881_882_pairs.tsv'),
    os.path.join(HERE, 'transcriptions/f6_frame10_R1_training.txt'), out)
sys.stdout.write('\n'.join(out) + '\n')
