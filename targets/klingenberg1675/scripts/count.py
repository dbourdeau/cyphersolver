"""count.py: the counter for targets/klingenberg1675 (own script, standard library only).

usage (from the target folder):  python3 scripts/count.py            prints every count in counts.txt
Rules, the same as the scripts the counts were first made with (scripts/original/sense2.py):
  token   = one cipher group of the transcription (a number or a letter sign); clear text in {} is not counted.
  strict  = the token lies in a gloss span whose decode, letter for letter, equals the judge's intended word.
  lenient = same, with Levenshtein distance <= 1 allowed (<= 2 when the intended word has 9 letters or more).
  E       = every other token: a code with no value in the map named, a token in a word that decodes wrongly,
            a token the judge could not gloss. A code is never counted on a value proposed from context.
"""
import re, json, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIGN = {"E":"e","y":"n","A":"r","F":"h","Q":"h","D":"u","G":"i","B":"i","X":"o","K":"s","L":"t","Z":"t","#":"c",
        "I":"l","x":"m","O":"a","o":"a","w":"d","H":"g","C":"f","V":"f","PP":"q","⊐":"k","T":"z","J":"k","P":"p","-":"b","U":"k","⊥":"z"}
def lines(path):
    """[(line_no, [(kind, raw, norm)])]; kind C clear, N number, L letter sign. Line 1 is a header if it starts '# '."""
    L = open(path, encoding='utf-8').read().splitlines()
    if L and L[0].startswith('# '): L = L[1:]
    txt = '\n'.join(L); out = []; ln = 1; cur = []
    for m in re.finditer(r'\{[^}]*\}|\S+|\n', txt, flags=re.S):
        tok = m.group(0)
        if tok == '\n':
            out.append((ln, cur)); ln += 1; cur = []; continue
        if tok.startswith('{'):
            cur.append(('C', tok, ' '.join(tok[1:-1].split())))
            nl = tok.count('\n')
            if nl: ln += nl
        else:
            t = tok.replace('"', '').replace('?', '')
            cur.append(('N' if t.isdigit() else 'L', tok, t))
    out.append((ln, cur))
    return [(n, c) for n, c in out if c]
def flat(path): return [(k, t) for _, c in lines(path) for k, _, t in c if k != 'C']
def load(name): return {k: v for k, v in json.load(open(os.path.join(HERE, 'maps', name), encoding='utf-8')).items() if not k.startswith('_')}
def dec1(k, t, table, words):
    if k == 'N': return table[t] if t in table else (words[t] if t in words else '[' + t + ']')
    return SIGN.get(t, '?')
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]
def gloss(path):
    g = []
    for l in open(path, encoding='utf-8'):
        if not l.strip() or l.startswith('#'): continue
        a, b, w = l.split(); g.append((int(a), int(b), w))
    return g
def score(tx, glossf, table, words):
    T = flat(tx); dec = [dec1(k, t, table, words) for k, t in T]
    st = le = gl = 0; cls = ['U'] * len(T); used = set(); wrong = []
    for a, b, w in gloss(glossf):
        assert not (set(range(a, b + 1)) & used); used |= set(range(a, b + 1))
        d = ''.join(dec[a:b + 1]).lower(); n = b - a + 1; dist = lev(d, w)
        s = d == w; l = dist <= (2 if len(w) >= 9 else 1)
        st += n * s; le += n * l; gl += n
        for i in range(a, b + 1): cls[i] = 'S' if s else 'W'
        if not s: wrong.append((a, b, d, w, l))
    opn = sum(1 for d in dec if d.startswith('['))
    return dict(N=len(T), strict=st, lenient=le, glossed=gl, open=opn, dec=dec, cls=cls, wrong=wrong, T=T)
if __name__ == '__main__':
    table = load('table_M3.json')
    for l in open(os.path.join(HERE, 'counts_input.tsv'), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        tag, tx, gl, mp, role = l.rstrip('\n').split('\t')
        r = score(os.path.join(HERE, tx), os.path.join(HERE, gl), table, load(mp) if mp != '-' else {})
        print(f"{tag}\t{role}\t{mp}\tstrict {r['strict']}/{r['N']} = {100*r['strict']/r['N']:.2f}%\tlenient {r['lenient']}/{r['N']} = {100*r['lenient']/r['N']:.2f}%\tglossed {r['glossed']}\topen-code tokens {r['open']}")
