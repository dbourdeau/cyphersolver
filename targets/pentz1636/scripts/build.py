"""build.py: decode both Pentz documents with the frozen Pentz 1636 key and count them, per document.
Standard library only. Run from the target folder:  python3 -I scripts/build.py
Writes decryptions/*.txt, units.tsv, counts.txt. Reads nothing outside this folder.

Rules (the same as the sessions that made the first passes):
- Vienna 1636 (b106): units = the reader's word division written before the one run (segmentation/vienna_1636-03-26_seg.tsv,
  a verbatim copy of SEG in scripts/original/b106_dec_pentz.py). I = index number (not a unit). C = code with no value (E).
  X = figures left unread (N). Table-1/2 words: S if they decode with no hole and are not declared E; declared E before the run:
  wowen, ?erpetuum.
- Glueckstadt c.1629-30 (b157): decoded with table 1 only (no 62/13 in the text); units and S/E/N classes were set by the
  reader after the one decode (segmentation/glueckstadt_c1630_img2_units_b157.tsv). That tally is checked here, not remade.
- Strict = S / (S+E+N). '?' rule (Dan Bourdeau's): a unit holding a doubtful figure counts as a hole even if classed S.
"""
import hashlib, re, collections, os

def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()

KF = 'key_history/KEY_pentz1636_T1T2.py'
TX_V = 'transcriptions/vienna_1636-03-26.txt'
TX_G = 'transcriptions/glueckstadt_c1630_img2.txt'
assert md5(KF) == '8306f733e78da38f1f86ac61d6bfd582', 'key md5'
assert md5(TX_V) == '953fd40913212af269df6dd4bc128b86', 'Vienna transcription md5 (frozen 12 Nov 2026 04:11:09 UTC)'
assert md5(TX_G) == '1e70795fd31a4ee8c1c30dce00354226', 'Glueckstadt transcription md5 (frozen 12 Nov 2026 13:30:55 UTC)'
ns = {}; exec(open(KF).read(), ns); T1, T2 = ns['T1'], ns['T2']

# key.tsv must hold exactly the decoder's values
kt = {'T1': {}, 'T2': {}}
for l in open('key.tsv', encoding='utf8'):
    if l.startswith('#') or l.startswith('table\t'): continue
    t, f, v = l.split('\t')[:3]
    if t in kt: kt[t][int(f)] = v
assert kt['T1'] == T1 and kt['T2'] == T2, 'key.tsv differs from the frozen tables'

os.makedirs('decryptions', exist_ok=True)
units_rows = ['doc\tn\tfigures\tkind\tdecoded\tclass\tdoubtful_figure\tnote']
C = []  # counts.txt lines
C.append('counts.txt: written by scripts/build.py. Strict = S/(S+E+N) per word unit, per document; never pooled.')
C.append(f'key: {KF} md5 {md5(KF)} (= key v1, b106, frozen 12 Nov 2026 before the Vienna run); key.tsv checked equal.')
C.append('')

# ---------- A. Vienna 1636 ----------
toks = []
for l in open(TX_V, encoding='utf8'):
    if not re.match(r'\d\d ', l): continue
    toks += [t for t in re.sub(r'<[^>]*>', ' | ', l[3:]).split() if t not in ('.', '|')]
SEG = []
for l in open('segmentation/vienna_1636-03-26_seg.tsv', encoding='utf8'):
    if l.startswith('#') or l.startswith('n\t'): continue
    n, figs, kind, decl = l.rstrip('\n').split('\t')
    SEG.append((int(n), figs, kind, decl))
assert toks == [x for _, s, _, _ in SEG for x in s.split()], 'segmentation does not match the frozen figures'
out = []; tally = collections.Counter(); qrule = collections.Counter(); idx = collections.Counter()
for n, s, k, decl in SEG:
    if k == 'I':
        out.append(f'  index {s}'); idx[s] += 1; continue
    if k == 'C':
        out.append(f'E code {s}'); tally['E'] += 1; qrule['E'] += 1
        units_rows.append(f'vienna_1636-03-26\t{n}\t{s}\tcode\t[{s}]\tE\t{"yes" if "?" in s else "no"}\tcode with no value')
        continue
    if k == 'X':
        out.append(f'N unread {s} (table 1 would give ' + ''.join(T1[int(x)] for x in s.split()) + ')')
        tally['N'] += 1; qrule['N'] += 1
        units_rows.append(f'vienna_1636-03-26\t{n}\t{s}\tunread\t-\tN\tno\tfigures not read')
        continue
    T = T1 if k == '1' else T2
    d = ''.join(T.get(int(x), '?') if x.isdigit() else '?' for x in s.split())
    c = 'E' if decl == 'E' else 'S'
    assert c == 'E' or '?' not in d
    doubt = '?' in s
    tally[c] += 1; qrule['E' if (doubt or c == 'E') else 'S'] += 1
    out.append(f'{c} table {k} {s} = {d}')
    units_rows.append(f'vienna_1636-03-26\t{n}\t{s}\ttable {k}\t{d}\t{c}\t{"yes" if doubt else "no"}\t{"declared E before the run" if decl else ""}')
nV = sum(tally.values())
out.append('units %d %s strict %d/%d = %.2f%%' % (nV, dict(tally), tally['S'], nV, 100 * tally['S'] / nV))
lw = tally['S'] + 2 + 1  # as printed by b106 (S + 2 declared E + 1 N)
assert lw == sum(1 for r in SEG if r[2] in '12X')
out.append('letter words only: %d S of %d = %.2f%%' % (tally['S'], lw, 100 * tally['S'] / lw))
open('decryptions/vienna_1636-03-26.txt', 'w', encoding='utf8').write('\n'.join(out) + '\n')
orig = open('scripts/original/b106_dec_pentz_run1_output.txt', encoding='utf8').read().splitlines()
assert out == orig[:len(out)], 'Vienna decode differs from the b106 run'
C.append('## A. Vienna, 26 Mar / 5 Apr 1636 (catalogue 2543): TKUA Kejseren, unit 260651, images 37 right and 38 left')
C.append(f'transcription md5 {md5(TX_V)} (frozen 12 Nov 2026 04:11:09 UTC, b106, one reader, not blind); decoded once.')
C.append('decryptions/vienna_1636-03-26.txt = the first %d lines of the b106 run output, byte for byte (checked).' % len(out))
C.append('index numbers (not units): ' + ', '.join(f'{k} x{v}' for k, v in sorted(idx.items())))
C.append(f"S {tally['S']} + E {tally['E']} + N {tally['N']} = {nV}")
C.append(f"FIRST PASS (figure of record): strict {tally['S']}/{nV} = {100*tally['S']/nV:.2f}%")
C.append(f"  of the E: codes {sum(1 for r in SEG if r[2]=='C')} (64, 226x, 12, 168, 63, 226, 8, 9, 85, 168, 12, 11, 168), declared E words 2 (wowen, ?erpetuum); N 1 (32 29 25)")
C.append(f"'?' rule (doubtful figure = hole): {qrule['S']}/{nV} = {100*qrule['S']/nV:.2f}% (the only doubtful figure is in ?erpetuum, already E)")
C.append(f"letter words only (b106's second figure; codes left out): {tally['S']}/{lw} = {100*tally['S']/lw:.2f}%")
n165 = nV + 1
C.append(f"with code 165 added (b110, 12 Nov 04:40 UTC: a code on image 38 left, line 1, before '62 34 29 33 17', missed by the frozen transcription; counted E): {tally['S']}/{n165} = {100*tally['S']/n165:.2f}%. The transcription file is not changed.")
# post-hoc, not of record: key v2 (b110) reads 64, 12 (gloss, image 48) and 63, 11, 9, 8 (analogy only) as index numbers
gl = {'64', '12'}; an = {'63', '11', '9', '8'}
cg = sum(1 for r in SEG if r[2] == 'C' and r[1] in gl)
ca = sum(1 for r in SEG if r[2] == 'C' and r[1] in an)
C.append('POST-HOC, NOT OF RECORD (key v2, b110, made after this run from the Guenther gloss on image 48; key_history/KEY_pentz_v2_b110.txt):')
C.append(f"  v2 reads 64 and 12 as index numbers (gloss-attested; {cg} units here). Dropped from the units: {tally['S']}/{nV}-{cg} = {tally['S']}/{nV-cg} = {100*tally['S']/(nV-cg):.2f}%; with 165: {tally['S']}/{nV-cg+1} = {100*tally['S']/(nV-cg+1):.2f}%")
C.append(f"  v2 also reads 63, 11, 9, 8 as index numbers by analogy only ([unverified]; {ca} units here). Dropping those too: {tally['S']}/{nV-cg-ca} = {100*tally['S']/(nV-cg-ca):.2f}%; with 165: {tally['S']}/{nV-cg-ca+1} = {100*tally['S']/(nV-cg-ca+1):.2f}%")
C.append('  These re-scores change no reading and are not claimed: they rest on a later key, partly on analogy, after the run.')
C.append('')

# ---------- B. Glueckstadt c.1629-30 ----------
o = []; tab = T1
for l in open(TX_G, encoding='utf8'):
    if not l.startswith('L'): continue
    lid, tk = l.split('|'); w = []
    for t in tk.split():
        if t in '.,': w.append(t); continue
        if t.startswith('{'): w.append('{x}'); continue
        n = int(t.rstrip('?'))
        if n == 62: tab = T1; w.append('<62>'); continue
        if n == 13: tab = T2; w.append('<13>'); continue
        v = tab.get(n)
        w.append(v.upper() if v and t.endswith('?') else (v if v else '[%s]' % t))
    o.append(lid.strip() + ' ' + ' '.join(w))
    o.append('     ' + ''.join(x if len(x) == 1 and x not in '.,' else (' ' if x in '.,' else ' ' + x + ' ') for x in w))
open('decryptions/glueckstadt_c1630_img2.txt', 'w', encoding='utf8').write('\n'.join(o) + '\n')
assert open('decryptions/glueckstadt_c1630_img2.txt', 'rb').read() == open('scripts/original/b157_decode_pz002_ONCE_output.txt', 'rb').read(), 'Glueckstadt decode differs from the b157 run'
# the unit list must spell out the decode stream exactly (codes and dividers aside)
stream = ''.join(re.sub(r'\[[^\]]*\]|\{x\}|[ .,]', '', o[i]) for i in range(1, len(o), 2))
U = []
for l in open('segmentation/glueckstadt_c1630_img2_units_b157.tsv', encoding='utf8'):
    if l.startswith('#'): continue
    p = l.rstrip('\n').split('\t'); U.append((int(p[0]), p[1], p[2], p[3] if len(p) > 3 else ''))
assert [u[0] for u in U] == list(range(1, len(U) + 1)) and len(U) == 68
assert ''.join(re.sub(r'\[[^\]]*\]', '', u[1]) for u in U) == stream, 'units do not spell the decode'
g = collections.Counter(u[2] for u in U); gq = collections.Counter()
codes = [u for u in U if u[1].startswith('[')]
for n, d, c, note in U:
    letters = re.sub(r'\[[^\]]*\]', '', d)
    doubt = any(ch.isupper() for ch in letters) or '?' in d
    gq['E' if (c == 'S' and doubt) else c] += 1
    units_rows.append(f'glueckstadt_c1630_img2\t{n}\t-\t{("code" if c == "E" else "fragment") if d.startswith("[") else "table 1"}\t{d}\t{c}\t{"yes" if doubt else "no"}\t{note}')
nG = len(U)
C.append('## B. Glueckstadt, c.1629-30: SHLK A IV 89 (Relationer fra guvernoer i Glueckstadt Christian Pentz 1629-45), unit 274999, image 2 (recto)')
C.append(f'transcription md5 {md5(TX_G)} (frozen 12 Nov 2026 13:30:55 UTC, b157, one reader, NOT blind: he had applied table 1 to line 1 in his head before the freeze); decoded once with key v1 table 1, unchanged.')
C.append('decryptions/glueckstadt_c1630_img2.txt is byte-identical to the b157 run output (checked). Units and classes: the b157 reader, after the decode.')
C.append(f"S {g['S']} + E {g['E']} + N {g['N']} = {nG}")
C.append(f"FIRST PASS (figure of record): strict {g['S']}/{nG} = {100*g['S']/nG:.2f}%")
C.append(f"S+E (sense, holes included): {g['S']+g['E']}/{nG} = {100*(g['S']+g['E'])/nG:.2f}%")
C.append(f"code units {len(codes)}; letter units {nG-len(codes)}; strict on letter units {g['S']}/{nG-len(codes)} = {100*g['S']/(nG-len(codes)):.2f}% (b157's line, reproduced)")
true_codes = [u for u in codes if u[2] == 'E']
C.append(f"  correction: those {len(codes)} bracketed units include the fragment [2?] (N); true code units {len(true_codes)}; letter units {nG-len(true_codes)}; strict on letter units {g['S']}/{nG-len(true_codes)} = {100*g['S']/(nG-len(true_codes)):.2f}%")
sq = [u[1] for u in U if u[2] == 'S' and any(ch.isupper() for ch in u[1])]
C.append(f"'?' rule (doubtful figure = hole): {gq['S']}/{nG} = {100*gq['S']/nG:.2f}% (S units with a doubtful figure: {', '.join(sq)})")
z = [u[1] for u in U if u[1] in ('andwzrt', 'bekzme', 'anherkzmen')]
assert len(z) == 3
C.append(f"units where figure 28 (= z in table 1) stands where o is wanted: {', '.join(z)} (3; a homophone 28 = o is suspected and NOT applied; no count here uses it)")
C.append('')
C.append('Not pooled. The two documents are different letters of different years.')
open('units.tsv', 'w', encoding='utf8').write('\n'.join(units_rows) + '\n')
open('counts.txt', 'w', encoding='utf8').write('\n'.join(C) + '\n')
print('\n'.join(C))
