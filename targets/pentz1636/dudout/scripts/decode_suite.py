"""Assemble transcription arbitrée (A + écarts DIFF-AB arbitrés) -> TRANSCRIPTION-SUITE.json ; décode avec KEY-v3 gelée (inchangée)."""
import json, pathlib, re, sys
H = pathlib.Path(__file__).resolve().parent
key = json.loads((H.parent / 'key_history/KEY-v3.json').read_text())
# arbitrages (ligne entière remplacée) issus de DIFF-AB.tsv
ARB = {
 ('402','L05'): '11 47x 54 42 56 55 54 61 49 62 33 18 17 34 33 21',
 ('402','L09'): '64 31 21 18 22 33 21 22 35 30 37 34 33? 17 10',
 ('403','L12'): '48 46 40 45 41 46 42 54 42 56 55 54 61 44',
 ('405','L01'): '63 23 21 37 35 23 29 21 23',
 ('405','L10'): '63 37? 36 34 37 17 35 14 24 17 31',
 ('408','L01'): '12 57 42 59 38 57 46 57 14 61 44',
 ('411','L02'): '37 17 34 33 21 24 33 22 23 11 54 61 44 56? 60 61 41 42 57',
 ('411','L04'): '62 24 17 24 17 33 24 33 17 35 37 22 23 33 15 15 32 24 21',
 ('412','L23'): '36 35 39 14 18 25 35 36 28 35 25',
 ('420','L05'): '21 33 17 22 36 24 21 31 29 17 30 18 35 30 22 23 33 21',
 ('420','L09'): '39 37 33 35 18 24 27 31 28 35 39 62 25 29 21',
 # second lecteur indépendant (pass C, 14/11), arbitrage sur l'image : DIFF-AC-420.tsv
 ('420','L06'): '31? 33 32 37 30 21 12 53 42 57 41 38 57 38 61 54 57',
 ('420','L13'): '23 24 17 31 36 33 29 13 53 42 46 55 42 49 61 38 40 45',
 ('420','L14'): '61 60? 55? 45? 54 57 43 43 55? 49 9 37 19 18 24 27 31 28',
}
LETTERS = {
 'pentz_1645-03-31': ['402','403'],
 'pentz_1645-04-08': ['404','405'],
 'pentz_1645-04-20_chancellor': ['408'],
 'pentz_1645-04-20_king': ['411','412'],
 'pentz_1645_img420': ['420'],
}
def tok(t):
    t2 = t.rstrip('?x')
    if not t2 or not t2.isdigit(): return {'v': None, 'raw': t}
    return {'v': int(t2), 'raw': t, 'doubt': t.endswith('?'), 'struck': t.endswith('x')}
docs = {}
for d, pages in LETTERS.items():
    lines = []
    for p in pages:
        for ln in (H.parent / 'transcriptions/suite' / f'A-{p}.txt').read_text().splitlines():
            if not ln.strip() or ln.startswith('#'): continue
            lab, rest = ln.split(' ', 1)
            rest = ARB.get((p, lab), rest)
            lines.append({'page': p, 'line': lab, 'figs': rest.split()})
    docs[d] = lines
(H.parent / 'transcriptions/suite/TRANSCRIPTION-SUITE.json').write_text(json.dumps(docs, ensure_ascii=False, indent=0))
def decode(lines):
    tab = 'T1'; out = []
    for L in lines:
        s = []
        for t in L['figs']:
            x = tok(t)
            if x['v'] is None: s.append('‹?›'); continue
            if x.get('struck'): s.append('[x]'); continue
            g = str(x['v'])
            if g in key['index']: tab = key['index'][g]; s.append('|'); continue
            if g in key['nulls']: s.append('·'); continue
            if x['v'] >= 100: s.append(f'[{g}]'); continue
            c = key[tab].get(g)
            s.append((c if c else f'({g}?)') + ('?' if x.get('doubt') else ''))
        out.append(f"{L['page']} {L['line']}  " + ''.join(s))
    return out
for d, lines in docs.items():
    o = decode(lines)
    (H.parent / 'decryptions' / f'{d}.txt').write_text('\n'.join(o) + '\n')
    print('==', d); print('\n'.join(o))
