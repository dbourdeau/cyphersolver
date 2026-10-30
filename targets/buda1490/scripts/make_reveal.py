"""Write docs/reveal/buda1490.json: lines P2L19-P2L22 (the dowry "no king ever received") decoded unit by unit by
measure.emit (key.json + the retry's extended values), with word breaks from the alignment.

    python scripts/make_reveal.py
"""
import importlib.util, json, pathlib

H = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('measure', H / 'measure.py')
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
LINES = ('P2L19', 'P2L20', 'P2L21', 'P2L22')

recs, adds = M.classify()
status = {r['w']: r['status'] for r in recs}
toks, prev_w = [], None
for p in M.P:
    if p['type'] == 'skip' or p['line'] not in LINES: continue
    w = M.WID[p['a']] if p['a'] < p['b'] else prev_w
    if prev_w is not None and w != prev_w: toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
    e = M.emit(p)
    t = {'g': p['sign'], 'p': e.strip('{}') if e else '·'}
    if e == '': t['cls'] = 'null'
    elif e.startswith('{'): t['cls'] = 'code'
    elif e in ('_', '#'): t['cls'] = 'unk'; t['p'] = '?'
    elif status.get(w) not in M.SENSE or (status.get(w) in ('exact', 'spelling') and not M.ok(p)): t['cls'] = 'unc'
    toks.append(t); prev_w = w
out = {'slug': 'buda1490', 'anchor': 'reading',
       'title': 'Milan, 30 November 1490: "no king ever received such a sum"',
       'caption': 'Page 2, lines 19-22 of Maffeo da Treviglio\'s cipher letter to Tamás Bakócz (MNL OL DL 46150), decoded sign by '
                  'sign under the key rebuilt from the clear minute; signs as transcribed (labels name shapes, not values).',
       'unit': 'signs',
       'key_note': 'Homophonic Latin cipher: about 60 letter signs (e has five, i four, a three), polyphonic qA (s/i/t) and qB '
                   '(u/s/f), pair units (oH = q, Ho = p), doubled-letter signs (sl = cc, X = ss), code signs and nulls; no word '
                   'division (spaces are editorial). Grey = a word not counted as read.',
       'tokens': toks}
(H.parents[1] / 'docs/reveal/buda1490.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len([t for t in toks if t['g']]), 'signs')
print(''.join(t['p'] if t['p'] != '·' else '' for t in toks))
