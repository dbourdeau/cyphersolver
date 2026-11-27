# House count for the four vocbatavia texts (Dan Bourdeau's review of PR #996, 27 Nov 2026): cipher words only, sure
# words only. Run from targets/vocbatavia:  python -I scripts/house_count.py
# The checks were done with AI tools and no person checked each record by hand.
import csv, re

def load_key(*files):
    k = {}
    for f in files:
        for r in csv.reader(open(f, encoding='utf-8'), delimiter='\t'):
            if r and r[0].strip().isdigit(): k[int(r[0])] = r[1].strip()
    return k

def report(name, rows):
    n = len(rows); h = sum(1 for _, ok, _ in rows if not ok)
    for w, ok, why in rows: print(f'  {"read" if ok else "HOLE"} {w}{"  - " + why if why else ""}')
    print(f'{name}: cipher_words {n} holes {h} read_share {(n - h) / n:.3f}\n')

# 1623: number cipher; key = 1634 glosses + post-hoc values from context (SECOND_PASS_values.tsv, all confirmed word for
# word by the 1079 margins) + 4 = k (EMENDATIONS.md 1). Hole: a letter the key does not give, or an emended word.
d = 'letters/1623_1634/'
k = load_key('key/K1634_key.tsv', d + 'SECOND_PASS_values.tsv'); k[4] = 'k'
EMENDED = {'kolden': 'read konden: 26 = l taken as a slip (EMENDATIONS.md 2)'}
rows = []
for r in csv.DictReader(open(d + 'decode_1623_firstpass.tsv', encoding='utf-8'), delimiter='\t'):
    w = ''.join(k.get(int(x), '?') for x in r['groups'].split())
    rows.append((r['block'] + ' ' + w, '?' not in w and w not in EMENDED, EMENDED.get(w, '?' in w and 'unvalued number' or '')))
report('1623', rows)

# 1634: the key source. Every word is glossed in the margin of inv. 1108; the K1634 key built from the glosses gives
# every letter of every word (differences from the gloss are the glossator's spelling: embarcadero/enbocadero ...).
k = load_key('key/K1634_key.tsv'); rows = []
for line in open(d + 'T1634_transcription.txt', encoding='utf-8'):
    if line.startswith('#') or '|' not in line: continue
    p, g, c = [x.strip() for x in line.split('|')]
    for w in [w.split() for w in c.split('/') if w.strip()]:
        dec = ''.join(k.get(int(x), '?') for x in w)
        rows.append((p + ' ' + dec, '?' not in dec, ''))
report('1634', rows)

# 1640 postscript: system-A words from the first-pass decode (KEY_v2); a word with an unvalued or illegible group is a
# hole (12 = b and the blotted group = 57 come from the 617 gloss, not the key). Every letter-cipher (system B) word is a
# hole: LC_KEY_v1 failed its test. LC words from the frozen transcription, split at spaces and dots; plus the three words
# 'k bd. p.' after 'Amsterdam' that the image and reader 2 show and the frozen transcription skips (NOTES, emendations).
rows = []
for r in csv.DictReader(open('letters/1640/decryptions/decode_1640_firstpass.tsv', encoding='utf-8'), delimiter='\t'):
    w = r['decode']; rows.append(('A ' + w, '?' not in w, '?' in w and 'group without a key value (gloss only)' or ''))
t = open('letters/1640/transcriptions/T1640_transcription.txt', encoding='utf-8').read()
for lc in re.findall(r'\[LC: ([^\]]*)\]', t):
    for w in re.split(r'[\s.]+', lc):
        if w: rows.append(('LC ' + w, False, 'letter cipher, no tested key'))
for w in ['k', 'bd', 'p']: rows.append(('LC ' + w, False, 'skipped in the frozen transcription (image, reader 2)'))
report('1640 postscript', rows)

# 1643: words from the frozen transcription (copy 2). Each <letter word> is one cipher word (system B: read only from the
# copy-1 gloss, so a hole); each run of numbers between other items is one word, except run 901.1, which the frozen
# DP word rule splits into d'advisen + uyt; the code numerals XXI and IV (905.3, written in clear brackets) are two
# words, read only from the gloss and Leupe 1858 (holes). A number run is read when the first-pass decode gives every
# letter and the frozen DP rule covers the whole run with one dictionary word.
dec = {r['groups']: r for r in csv.DictReader(open('letters/1643/decode_1643_firstpass.tsv', encoding='utf-8'), delimiter='\t')}
rows = []
for line in open('letters/1643/T1643_transcription.txt', encoding='utf-8'):
    if line.startswith('#') or '|' not in line: continue
    pl, body = [x.strip() for x in line.split('|', 1)]
    if 'XXI ende IV' in body:
        rows += [(pl + ' XXI', False, 'code numeral, from the gloss'), (pl + ' IV', False, 'code numeral, from the gloss')]
    body = re.sub(r'\[[^\]]*\]', ' | ', body)
    for item in re.findall(r'<[^>]*>|[\d ]+|\|', body):
        item = item.strip()
        if not item or item == '|': continue
        if item.startswith('<'): rows.append((pl + ' ' + item, False, 'letter cipher (system B), gloss only')); continue
        r = dec.get(item)
        if item.startswith('33 9 65'):
            rows += [(pl + " d'advis?n", False, "74 has no key value (copy 1 writes 70)"), (pl + ' uyt', True, '')]
        elif r and int(r['covered']) == int(r['len']) and '?' not in r['decode']:
            rows.append((pl + ' ' + r['decode'], True, ''))
        else:
            rows.append((pl + ' ' + (r['decode'] if r else item), False, 'not one keyed dictionary word'))
report('1643', rows)
