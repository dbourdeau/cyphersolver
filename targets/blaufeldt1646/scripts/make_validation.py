"""Usage: python scripts/make_validation.py   (then python docs/_validate.py blaufeldt1646 --write in the repo)

Build validation.tsv for blaufeldt1646: every cipher token of transcription_24854.txt in text order with the
reading it carries in reading_24854.md. Holes and guesses over unsettled signs are left unread ('?')."""
import pathlib, re
D = pathlib.Path(__file__).resolve().parent.parent
key = {}
for line in open(D / 'key_frozen.tsv', encoding='utf-8'):
    if line.startswith('#') or line.startswith('token\t') or not line.strip():
        continue
    a, b = line.rstrip('\n').split('\t')[:2]
    key[a] = b
# readings given from sense in reading_24854.md (marked repairs): (line, index of the token in the line) -> value
REPAIR = {'50': 'e', '60': 'i', '70': 'i', '73': 'r', '80': 'u', '86': 'b'}
rows = []
for line in open(D / 'transcription_24854.txt', encoding='utf-8'):
    m = re.match(r'(L\d+):\s*(.*)$', line.rstrip('\n'))
    if not m:
        continue
    lid, body = m.groups()
    body = re.sub(r'<[^>]*>', ' | ', body)
    runs = [r.split() for r in body.split('|')]
    for ri, run in enumerate(runs):
        run = [t for t in run if t not in ('=', '.', 'f')]
        unread_run = (lid == 'L1' and ri == 2)            # [?partito] = ?ar???o: guess, counted as a hole
        for gi, t in enumerate(run):
            val = '?'
            if t != '?' and not unread_run:
                base = t.split('/')[0].rstrip('?')
                dbl = base.endswith('^')
                base = base.rstrip('^')
                v = key.get(base) or REPAIR.get(base)
                if v and not v.startswith('['):
                    val = v * (2 if dbl else 1)
            if lid == 'L4' and ri == 0 and gi == 4:          # 23 read c in "difficolta" (marked repair)
                val = 'c'
            if lid == 'L8' and 3 <= gi <= 11:                 # "[?febraro=feb???rdo]": the hole stretch
                val = '?'
            if lid == 'L8' and gi == 0:
                val = '?'
            rows.append((t, val, lid))
out = ['# model: it-cinquecento',
       '# source: transcription_24854.txt (tokens as copied) and reading_24854.md (values)',
       '# note: built 13 Nov 2026; glossed values from key_frozen.tsv; the six unglossed groups 50 60 70 73 80 86 carry the '
       'value the reading gives them from sense (marked repairs); 23 in "difficolta" is read c as in the reading; '
       'the guessed stretches [?partito] (L1) and the date line hole (L8) are left unread']
for t, v, lid in rows:
    out.append(f'{t}\t{v}')
(D / 'validation.tsv').write_bytes(('\n'.join(out) + '\n').encode('utf-8'))
print(len(rows), "tokens,", sum(1 for r in rows if r[1] != "?"), "read")
