"""keytable.py : write key.tsv, the frozen KEY_v2 with the evidence for each value. Run from the target folder.
Columns: cipher, plain, pair (involution), in KEY_v1 (f.5 anneal + two hand edits), KEY_v2 anneal value (f.5+f.6, no edit),
worksheet frame 168 (pair written there), exact contemporary gloss words on frames 3 and 51 whose cipher contains the letter,
occurrences in the training text f.5+f.6, source class."""
import re, sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode as D
k2 = D.load_key('gloss/KEY_lasa_v2.txt'); k1 = D.load_key('gloss/KEY_lasa_v1.txt')
inv = dict(k2); inv.update({v: c for c, v in k2.items() if v not in k2})
P = {a: b for l in open('gloss/worksheet_frame168.txt') if not l.startswith('#') and l.strip() for a, b in [l.split()]}
P.update({b: a for a, b in list(P.items())})
def norm(s): return re.sub('[^a-z]', '', s.lower().replace('v', 'u').replace('j', 'i'))
ex = collections.Counter()
for l in open('gloss/catalogus_frame3_check_b160.txt', encoding='utf-8'):
    m = re.match(r"\s+(.+?)\s+->\s+.*?gloss '(.+?)'", l)
    if not m: continue
    cw = [w for w in re.split(r'[ ,]+', m.group(1)) if w]; gl = [norm(w) for w in re.split(r'[ ,]+', m.group(2)) if norm(w)]
    for c, g in zip(cw, gl):
        if ''.join(inv.get(x, '?') for x in c.lower()) == g:
            for x in set(c.lower()): ex[x] += 1
for l in open('gloss/postscript_frame51_gloss_b160.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c, g = l.rstrip('\n').split('\t'); c = c.replace(' ', '')
    if D.dec_word(c, k2) == norm(g):
        for x in set(c): ex[x] += 1
tr = collections.Counter(c for f in ['transcriptions/f5f6_combined_anneal_input.txt'] for l in open(f) if not l.startswith('#') for c in l if c.isalpha())
o = ['cipher\tplain\tpair\tKEY_v1\tKEY_v2_anneal\tworksheet_f168\tgloss_words_exact_f3_f51\ttraining_occurrences_f5_f6\tsource']
for c in sorted(set(k2) | {'m'}):
    p = inv[c]; src = 'ciphertext-only anneal (f.5+f.6), no edit' if c in k2 else 'not in the frozen file (decodes ?); value x from the involution x=m and the frame-168 worksheet'
    o.append(f'{c}\t{p}\t{"".join(sorted((c, p)))}\t{k1.get(c, "-")}\t{k2.get(c, "-")}\t{"yes" if P.get(c) == p else "no"}\t{ex[c]}\t{tr[c]}\t{src}')
o.append('# Frozen file gloss/KEY_lasa_v2.txt md5 c8fade565852b5bda3d671f4c0489a90 (b160, 2026-11-12 13:47:27 UTC by the session log). No value comes from context or from a gloss: every value')
o.append('# in the file is the annealer\'s; the glosses and the worksheet were checked after the freeze and agree. j (once in f.6) had the anneal value x, left out of the frozen file;')
o.append('# v (written by reader 2 for a v-like glyph) is not a cipher letter of the table. Both decode as ? and count as holes.')
pathlib.Path('key.tsv').write_text('\n'.join(o) + '\n', encoding='utf-8'); print('\n'.join(o))
