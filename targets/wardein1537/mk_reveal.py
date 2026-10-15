"""Write docs/reveal/wardein1537.json: P1 lines 6-9 of R9414 sign by sign, with the values mk_validation.py pairs
(keyb + chosen alternatives, kept only where they agree with r9414/reading_v5.txt; otherwise 'unc' with the decrypt
letter, or '?'). Clear text in brackets is shown as plain. Runs mk_validation.py (which rewrites validation.tsv
unchanged) to reuse its tables. Run: python targets/wardein1537/mk_reveal.py"""
import io, os, re, json, runpy, difflib, contextlib
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(H))
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(os.path.join(H, 'mk_validation.py'))
T, D, R, dp, nz = g['T'], g['D'], g['R'], g['dp'], g['nz']

raw = {}
for l in io.open(os.path.join(H, 'r9414', 'transcription_p12.txt'), encoding='utf8'):
    m = re.match(r'(\d\d) (.*)', l)
    if m and m.group(1) not in raw:
        raw[m.group(1)] = m.group(2)
toks = []
for no in ('06', '07', '08', '09'):
    k = ('P1', no)
    signs = list(T[k]); dec = D.get(k, ''); rd = R.get(k, '')
    m = re.match(r'\[([^\]]*)\]', raw[no])
    if m:
        for w in m.group(1).split():
            toks.append({'g': '', 'p': w + ' ', 'cls': 'plain'})
    pos = dp(signs, dec)
    dn = ''.join(nz(c) for c in dec); rn = ''.join(nz(c) for c in rd)
    ok = set()
    for a, b, size in difflib.SequenceMatcher(None, dn, rn, autojunk=False).get_matching_blocks():
        ok.update(range(a, a + size))
    for s, p in zip(signs, pos):
        if p is None:
            toks.append({'g': s, 'p': '', 'cls': 'null'})
        elif p in ok and dec[p].isalpha():
            toks.append({'g': s, 'p': dec[p], 'cls': ''})
        elif dec[p].isalpha():
            toks.append({'g': s, 'p': dec[p], 'cls': 'unc'})
        else:
            toks.append({'g': s, 'p': '?', 'cls': 'unk'})
out = {
 'slug': 'wardein1537',
 'anchor': 'reading',
 'title': 'Wardein, 14 March 1537: the glossed lines',
 'caption': 'Lines 6–9 of the first page of R9414 (BayHStA Kurbayern Äußeres Archiv 4591 f. 257r), the lines a clerk of the time glossed, decoded sign by sign with the key recovered here: “mittler zeit wider in Ungern gezogen bin, got weis wie mich die rais mit groser sorg ist ankummen, wie auch mein genadiger furst und herr mich hat abgefertigt”. Signs marked uncertain take a value the reading does not confirm at that place; signs with no letter are nulls or dropped by the alignment.',
 'unit': 'signs',
 'key_note': 'A homophonic alphabet: several signs for e, n, r, s and t. Signs are shown as the transcription codes of r9414/transcription_p12.txt.',
 'tokens': toks,
}
json.dump(out, io.open(os.path.join(ROOT, 'docs', 'reveal', 'wardein1537.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len([t for t in toks if t['g']]), 'signs;', sum(t['cls'] == 'unc' for t in toks), 'unc;', sum(t['cls'] == 'null' for t in toks), 'null')
print(''.join(t['p'] if t['cls'] != 'null' else '·' for t in toks))
