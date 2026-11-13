"""confirm.py : check the frozen ciphertext-only KEY_v2 against the three contemporary sources in the file.
Run from the target folder: python3 -I scripts/confirm.py > controls/confirmations.txt
1. frame 3 'Catalogus' (enciphered name-words with clear glosses), b160's reading in gloss/catalogus_frame3_check_b160.txt
2. frame 51 postscript (interlinear Latin glosses), b160's reading in gloss/postscript_frame51_gloss_b160.tsv
3. frame 168 key worksheet, gloss/worksheet_frame168.txt
Readings of the three sources were made after KEY_v2 was frozen; the frame-51 glosses were written down before the words were decoded."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode as D
k = D.load_key('gloss/KEY_lasa_v2.txt')
inv = dict(k); inv.update({v: c for c, v in k.items() if v not in k})   # add reverse of one-way entries (m from x=m)
def norm(s): return re.sub('[^a-z]', '', s.lower().replace('v', 'u').replace('j', 'i'))
print('KEY_v2 file entries:', len(k), '; letters with no entry:', sorted(set('abcdefghijklmnopqrstuvwxyz') - set(k)))
print('one-way entries completed by the involution:', {c: v for c, v in inv.items() if c not in k})
print('\n1. Catalogus, frame 3 (13 name-words or pairs)')
ex = inv_ok = 0; n = 0
for l in open('gloss/catalogus_frame3_check_b160.txt', encoding='utf-8'):
    m = re.match(r"\s+(.+?)\s+->\s+.*?gloss '(.+?)'", l)
    if not m: continue
    n += 1; cw = [w for w in re.split(r'[ ,]+', m.group(1)) if w]; gl = [norm(w) for w in re.split(r'[ ,]+', m.group(2)) if norm(w)]
    d1 = [D.dec_word(w, k) for w in cw]; d2 = [''.join(inv.get(c, '?') for c in w.lower()) for w in cw]
    g = gl[:len(cw)]; a = d1 == g; b = d2 == g; ex += a; inv_ok += b
    print(f'   {" ".join(cw):28s} file key: {" ".join(d1):28s} involution: {" ".join(d2):28s} gloss: {" ".join(g):28s} {"EXACT" if a else ("EXACT by involution" if b else "DIFFERS")}')
print(f'   exact with the frozen file: {ex}/{n}; exact with the involution (adds m=x): {inv_ok}/{n}')
print('\n2. Postscript, frame 51 (18 glossed cipher words)')
W = L = Lok = Lpos = 0
for l in open('gloss/postscript_frame51_gloss_b160.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c, g = l.rstrip('\n').split('\t'); c = c.replace(' ', ''); g = norm(g)
    d = D.dec_word(c, k); W += 1
    import difflib
    sm = difflib.SequenceMatcher(None, d, g, autojunk=False); same = sum(b.size for b in sm.get_matching_blocks())
    L += len(g); Lok += same; Lpos += sum(x == y for x, y in zip(d, g))
    print(f'   {c:18s} -> {d:18s} gloss {g:18s} {"EXACT" if d == g else f"{same}/{len(g)} letters"}')
ok = sum(1 for l in open('gloss/postscript_frame51_gloss_b160.tsv') if not l.startswith('#') and D.dec_word(l.split('\t')[0].replace(' ',''), k) == norm(l.split('\t')[1]))
print(f'   words exact: {ok}/{W}')
print(f'   gloss letters equal position by position from the start of each word (the measure b160 filed): {Lpos}/{L} = {100*Lpos/L:.2f}%')
print(f'   gloss letters matched allowing one shift (difflib matching blocks): {Lok}/{L} = {100*Lok/L:.2f}%')
print('\n3. Key worksheet, frame 168 (AMPHICTYONES over zxwurqlkgfdb)')
P = [l.split() for l in open('gloss/worksheet_frame168.txt') if not l.startswith('#') and l.strip()]
agree = sum(1 for a, b in P if inv.get(a) == b and inv.get(b) == a); infile = sum((a in k and k[a] == b) + (b in k and k[b] == a) for a, b in P)
print(f'   pairs: {len(P)}; pairs equal to the KEY_v2 involution in both directions: {agree}/{len(P)}; directed values present in the frozen file: {infile}/{2*len(P)}')
cover = sorted(set(x for p in P for x in p)); print(f'   letters covered by the worksheet: {len(cover)} ({"".join(cover)}); KEY_v2 letters: {len(set(k)|set(k.values()))}')
