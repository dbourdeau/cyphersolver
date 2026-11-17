"""Map the solver's 56-word division onto sign positions and report, per word, its signs in (1) the solver's text,
(2) my strict reconciled text (aligned), (3) the solver's text with my helpers' agreed readings."""
import re, json, difflib
m = json.load(open("my_map_from_key_image.json"))
def val(t):
    lab = m.get(t)
    if lab is None: return '?'
    if re.fullmatch(r'[A-Z]\d', lab): return lab[0].lower()
    if lab == 'nine_dot': return 'y'
    if lab == 'D_null': return ''
    return '<' + lab + '>'
def load(p, order):
    d = {}
    for l in open(p):
        mm = re.match(r'(L\d[ab]?):\s*(.*)', l)
        if mm and mm.group(1) not in d: d[mm.group(1)] = mm.group(2).split()
    return [t for L in order for t in d.get(L, [])]
sol = load("../repo_items_2026-11-16/i2857/transcription_reconciled.txt", ['L1','L2','L3','L4','L5','L6','L7','L8'])
mine = load("transcription_reconciled.txt", ['L1','L2','L3','L4','L5','L6','L7','L8b','L8a'])
fix = load("transcription_solver_plus_agreed_blind.txt", ['L1','L2','L3','L4','L5','L6','L7','L8'])
words = "los que aqyi pr?curan escandalos e daoruauan que [bnm] no entrase en la tregua diziendo que no tenian guela ni se han de modtrar parte pero no se led dio luga? a lo que querian antes se led hizo haze? lo que [dal] ara uera cerca deste caso porque fuera gran ync?nuiniente no se hazer asi".split()
# assign solver tokens to words
spans, i = [], 0
for w in words:
    start = i
    if w.startswith('['):
        i += 1
    else:
        n = 0
        while n < len(w):
            v = val(sol[i]) if not sol[i].startswith('[') else '?'
            n += len(v) if v and not v.startswith('<') else (1 if v == '?' else 0)
            i += 1
    spans.append((w, start, i))
assert i == len(sol), (i, len(sol))
sm = difflib.SequenceMatcher(a=sol, b=mine, autojunk=False)
amap = {}
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        for k in range(i2-i1): amap[i1+k] = mine[j1+k]
    else:
        for k in range(i2-i1): amap[i1+k] = 'D' if not (op == 'replace' and i2-i1 == j2-j1) else mine[j1+k]
out = []
for w, a, b in spans:
    s = sol[a:b]; mm_ = [amap.get(k, 'D') for k in range(a, b)]; f = fix[a:b]
    dm = ''.join('?' if t in ('D', '#') or val(t) == '?' else val(t) for t in mm_)
    df = ''.join(val(t) if not t.startswith('[') else '?' for t in f)
    out.append(f"{w}\t{' '.join(s)}\tmine:{' '.join(mm_)} -> {dm}\tsolver+blind:{df}")
open("words_table.tsv", "w").write("word(solver)\tsolver signs\tmine\tsolver+agreed-blind\n" + "\n".join(out) + "\n")
print("\n".join(out))
