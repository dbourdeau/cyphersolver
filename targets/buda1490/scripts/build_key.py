"""Write key.json and key.md from scripts/data/key_external.json (the key rebuilt from the clear minute by
scripts/ext/report.py) and the sign-by-sign comparison with the ciphertext-only key14 (scripts/data/key14.json,
verdicts in scripts/data/key14_verdicts.json). Run from the target folder: python scripts/build_key.py"""
import json, collections, pathlib
H = pathlib.Path(__file__).resolve().parent.parent
K = json.load(open(H / 'scripts/data/key_external.json'))
V = json.load(open(H / 'scripts/data/key14_verdicts.json'))
NOTE = {
 've': 'code, two signs v+e: Illustrissimus Princeps (meus) / Dominus meus, the Duke; the D/x after it is the plain m of meum/meo',
 'ff': 'code: Serenissimus Dominus Rex (Hungarie), every case form; one extra ff on P2L03 has no counterpart in the minute',
 'Tx': 'code: Maiestas (sua), "prefata Maiestas regia"',
 'Ga': 'code, two signs G+a: affinitas',
 'Gp': 'code, two signs G+p: non (P1L25 "amabat non mediocriter", where the minute has a doubtful word)',
 'dt': 'code: quod (once "quod ab")', 'dx': 'code: quod', 'K': 'code: quoniam (third K at an illegible word of the minute, P3L24)',
 'fo': 'code: centum quinquaginta milia (150,000); the caret insertion "centum" of the minute is enciphered',
 'y': 'no letter value: twice at "ducenta milia / ducentorum milium" (200,000), once at the tt of admittendas, twice no counterpart; probably the code for 200,000 (2 cases), left unvalued',
 'X': 'double-letter sign ss', 'LL': 'pair unit 6/6A + gA = ll', 'Ob': 'double-letter sign mm (commiserat)', 'sl': 'double-letter sign cc (accepit)',
 'wL': 'double-letter sign tt (mittantur)', 'Od': 'double-letter sign dd (adduxit, additione); key14 had l',
 'Bd': 'x (rex), one case', '8C': 'open: i twice, x once, ii once (reiici); needs an image check',
 '&': 'et, at three places where the cipher adds an "et" the minute lacks',
 'qB': 'polyphonic u/s/f', 'ooA': 'polyphonic u/s', 'ooB': 's (52 of 53); key14 had u/s with u first', 's': 'polyphonic h/f, several with no counterpart',
 '3': 'n; g six times, probably 3G misread as 3', 'tp': 'b; a twice', 'gA': 'o; t twice',
 'A': 'null (8 of 9)', 'al': 'null (clause ends)', 'aN': 'null', 'Rx': 'null; key14 had e', 'e': 'null (once, inside the Blanca title)',
 'H': 'p once (= Ho with the o missed), once unexplained', '6': 'no stable value (c in cui, l in excellentia)',
 'nq': 'n before a u-sign = q', 'ni': 'n elsewhere = i', 'oH': 'pair o+H = q', 'Ho': 'pair H+o = p', 'Om': 'pair = m',
}
out = {}
for s, k in sorted(K.items(), key=lambda x: -x[1]['count']):
    v = V.get(s, {})
    out[s] = {'kind': k['kind'], 'values': k['values'], 'occurrences': k['count'], 'tokens': k['tokens'],
              'aligned_counts': k['counts'], 'key14': v.get('key14', ''), 'key14_verdict': v.get('verdict', ''),
              **({'note': NOTE[s]} if s in NOTE else {})}
meta = {'_about': 'Key of DL 46150 (catalogue 1235) rebuilt from the clear minute ASMi Sforzesco 642 (Vestigia 194) '
        'by EM alignment of the cipher with the minute (scripts/ext/em_align.py, report.py). kind: single | poly '
        '(several letters) | multi (one sign for a doubled letter or et) | code (word or title) | null. values: accepted '
        'values (>=2 aligned cases and >=4%). aligned_counts: every string the alignment gave the sign ("*" = code '
        'words, "" = no counterpart). key14 / key14_verdict: the ciphertext-only key of round 6 and whether it was right.'}
json.dump({**meta, **out}, open(H / 'key.json', 'w'), indent=1, ensure_ascii=False)
fmt = lambda k: ('code: ' + ' / '.join(k['values'])) if k['kind'] == 'code' else 'null' if k['kind'] == 'null' else ('/'.join(k['values']) or '(no value)')
L = ['# Key of DL 46150 (catalogue 1235): key from external plaintext', '',
     'Rebuilt from the clear minute (ASMi Sforzesco 642 = Vestigia 194, `reading/clear_minute.txt`) aligned with the',
     'cipher (`scripts/ext/em_align.py`, `report.py`; the alignment is `reading/align.md`). n = aligned occurrences',
     '(units, damage left out). key14 = the ciphertext-only key of round 6 (`scripts/data/key14.json`), with the verdict',
     'of the comparison. Machine-readable: `key.json` (with every aligned count).', '',
     '| sign | kind | value | n | key14 | key14 verdict | note |', '|---|---|---|---|---|---|---|']
for s, k in out.items():
    L.append(f"| `{s}` | {k['kind']} | {fmt(k)} | {k['occurrences']} | {k['key14'] or '(null)'} | {k['key14_verdict']} | {k.get('note', '')} |")
hom = collections.defaultdict(list)
for s, k in out.items():
    if k['kind'] in ('single', 'poly', 'multi'):
        for v in k['values']: hom[v].append(f"`{s}` {k['aligned_counts'].get(v, 0)}")
L += ['', '## Homophones per letter', ''] + [f"- **{v}**: " + ', '.join(hom[v]) for v in sorted(hom) if v]
right = sum(1 for k in out.values() if k['key14_verdict'].startswith('right'))
tok_right = sum(k['tokens'] for k in out.values() if k['key14_verdict'].startswith('right'))
tot = sum(k['tokens'] for k in out.values())
L += ['', f'## key14 against the external key', '',
      f'{right} of {len(out)} signs right or right in their majority value, covering {tok_right} of {tot} tokens '
      f'({100 * tok_right / tot:.1f}%). key14 missed the code signs (ff, Tx, Ga, Gp, dt, dx, K: nulls in key14; ve, fo '
      'unvalued), had ooB as u instead of s, and had Od, Rx, e, 6, H wrong. Every other letter sign with more than 10 '
      'occurrences was right.', '']
(H / 'key.md').write_text('\n'.join(L), encoding='utf-8')
print(right, len(out), tok_right, tot)
