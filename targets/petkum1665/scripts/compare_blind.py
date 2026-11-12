# compare_blind.py  (run from anywhere; standard library only; python3 -I)
# Token agreement between the first transcription and the blind second one (difflib, autojunk off; the unsure mark ~ stripped).
# Part 1 is the contributor's b96 compare.py (30 Nov 1665: R1 against R2, R2 sign names mapped to the key's names; agreement = equal / R1 tokens).
# Part 2 is the contributor's b115 compare5.py (five letters: first reader against blind reader; agreement = equal / alignment columns).
# Logic unchanged; only the file paths are fixed to this folder.
import os, re, difflib
F = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def P(*a): return os.path.join(F, 'transcriptions', *a)
M = {'ll':'LL','b':'B','x':'X','psi':'PSI','beta':'BET','ms':'MT','tq':'QX','lam':'LAM','y':'Y','g':'G','theta':'TH','hash':'HSH','u4':'U4','hz':'HB','q':'Q','dx':'DB'}

def toks1(path, pref=None, mapit=False):
    out = []
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or '|' not in l: continue
        lid, body = l.rstrip('\n').split('|', 1)
        if pref and not lid.startswith(pref): continue
        for r in re.findall(r'<([^>]*)>', body):
            for t in r.split('.'):
                t = t.strip().rstrip('~')
                if not t: continue
                out.append((M.get(t, t) if mapit else t, lid))
    return out

print('PART 1. 30 Nov 1665, R1 (first reader) against R2 (blind)')
r2 = P('petkum_1665-11-30_R2_blind.txt'); tot = [0, 0, 0, 0, 0]
for name, pref, r1 in (('573', '573', P('petkum_1665-11-30_p2-3_R1.txt')), ('572R+574L', ('572', '574'), P('petkum_1665-11-30_p1-p4_R1_heldout.txt'))):
    a = toks1(r1); b = toks1(r2, pref, True)
    sm = difflib.SequenceMatcher(None, [t for t, _ in a], [t for t, _ in b], autojunk=False)
    eq = sub = ins = dele = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': eq += i2 - i1
        else:
            n = min(i2 - i1, j2 - j1); sub += n; dele += (i2 - i1) - n; ins += (j2 - j1) - n
            print('  DIFF %s R1[%s] %s | R2[%s] %s' % (tag, a[i1][1] if i1 < len(a) else '-', ' '.join(t for t, _ in a[i1:i2]), b[j1][1] if j1 < len(b) else '-', ' '.join(t for t, _ in b[j1:j2])))
    print('%s: R1 tokens %d, R2 tokens %d; equal %d, substituted %d, only-R1 %d, only-R2 %d; agreement on R1 = %d/%d = %.2f%%' % (name, len(a), len(b), eq, sub, dele, ins, eq, len(a), 100 * eq / len(a)))
    for i, v in enumerate((len(a), len(b), eq, sub, dele + ins)): tot[i] += v
print('POOLED: R1 %d, R2 %d, equal %d, substituted %d, indel %d; agreement %d/%d = %.2f%%' % (*tot, tot[2], tot[0], 100 * tot[2] / tot[0]))

def toks2(p):
    out = []
    for l in open(p, encoding='utf8'):
        if l.startswith('#') or '|' not in l: continue
        lid, body = l.rstrip('\n').split('|', 1)
        for r in re.findall(r'<([^>]*)>', body):
            for t in r.split('.'):
                t = t.strip()
                if t: out.append((t.rstrip('~'), lid, t.endswith('~')))
    return out

print('\nPART 2. Five letters, first reader against blind reader')
names = ['petkum_1665-04-28', 'petkum_1665-06-23', 'petkum_1665-09-17', 'petkum_1666-01-18', 'petkum_1666-04-06']
T = [0] * 6
for n in names:
    b = toks2(P(n + '_blind.txt')); a = toks2(P(n + '.txt'))
    sm = difflib.SequenceMatcher(None, [t for t, _, _ in a], [t for t, _, _ in b], autojunk=False)
    eq = sub = da = ib = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': eq += i2 - i1; continue
        k = min(i2 - i1, j2 - j1); sub += k; da += (i2 - i1) - k; ib += (j2 - j1) - k
        print('  %s %s first[%s] %s | blind[%s] %s' % (n[-10:], tag, a[i1][1] if i1 < len(a) else '-', ' '.join(t for t, _, _ in a[i1:i2]), b[j1][1] if j1 < len(b) else '-', ' '.join(t + ('~' if u else '') for t, _, u in b[j1:j2])))
    al = eq + sub + da + ib
    print('%s: first %d tok, blind %d tok; equal %d, subst %d, only-first %d, only-blind %d; agreement = equal/alignment cols = %d/%d = %.2f%%' % (n, len(a), len(b), eq, sub, da, ib, eq, al, 100 * eq / al))
    for i, v in enumerate((len(a), len(b), eq, sub, da, ib)): T[i] += v
al = T[2] + T[3] + T[4] + T[5]
print('POOLED: first %d, blind %d, equal %d, subst %d, only-first %d, only-blind %d; agreement %d/%d = %.2f%%' % (*T, T[2], al, 100 * T[2] / al))
