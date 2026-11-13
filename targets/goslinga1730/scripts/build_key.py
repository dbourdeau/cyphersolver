"""Build the key of catalogue 2534 from pairs.tsv (cipher groups paired with the contemporary decipherment slip).
Standard library only.   python scripts/build_key.py [--write]

1. Checks that the groups of pairs.tsv, in order, are exactly the code groups of transcription_goslinga1730.txt.
2. Builds the key from all pairs (key.tsv) and, for the held-out test, a training key from part A only.
3. Held-out test: applies the part-A key to every group of part B and compares with the slip.
--write also writes key.tsv and key_frozen.tsv (the frozen copy is the key used for every decryption).
"""
import pathlib, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent

def code_groups(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        out += [t for t in line.split()[1:] if not t.startswith('=')]
    return out

def read_pairs():
    rows = []
    for line in open(ROOT / 'pairs.tsv', encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        f = line.rstrip('\n').split('\t')
        f += [''] * (6 - len(f))
        rows.append(dict(kind=f[0], groups=f[1].split(), slip=f[2], aligned=f[3], part=f[4], note=f[5]))
    return rows

def letters(aligned):
    return aligned.split('|') if '|' in aligned else list(aligned)

def build(rows):
    val = collections.defaultdict(collections.Counter)   # group -> Counter(value)
    typ = {}
    for r in rows:
        if r['kind'] == 'W':
            val[r['groups'][0]][r['slip']] += 1; typ[r['groups'][0]] = 'word'
        elif r['kind'] == 'L':
            ls = letters(r['aligned'].lower())
            assert len(ls) == len(r['groups']), (r, ls)
            for g, l in zip(r['groups'], ls):
                val[g][l] += 1; typ[g] = 'letter'
    return val, typ

rows = read_pairs()
seq = [g for r in rows for g in r['groups']]
tr = code_groups(ROOT / 'transcription_goslinga1730.txt')
if seq != tr:
    for i, (a, b) in enumerate(zip(seq, tr)):
        if a != b:
            print('FAIL pairs and transcription part at group', i, a, b); break
    else:
        print('FAIL length', len(seq), len(tr))
    sys.exit(1)
print(f'pairs cover all {len(tr)} code groups of the transcription, in order')
full, typ = build(rows)
conf = {g: c for g, c in full.items() if len(c) > 1}
for g, c in sorted(conf.items(), key=lambda x: int(x[0].rstrip('^'))):
    print('CONFLICT', g, dict(c))
nl = sum(1 for g in full if typ[g] == 'letter'); nw = len(full) - nl
print(f'full key: {len(full)} groups ({nl} letter groups, {nw} word/name groups), {len(conf)} conflicts')

# held-out test
train, _ = build([r for r in rows if r['part'] == 'A'])
tot = right = unknown = wrong = 0
words_ok = words_tot = 0
for r in rows:
    if r['part'] != 'B' or r['kind'] not in 'WL':
        continue
    want = [r['slip']] if r['kind'] == 'W' else letters(r['aligned'].lower())
    ok_word = True
    for g, w in zip(r['groups'], want):
        tot += 1
        if g not in train:
            unknown += 1; ok_word = False
        elif train[g].most_common(1)[0][0] == w:
            right += 1
        else:
            wrong += 1; ok_word = False; print('  held-out mismatch', g, train[g].most_common(1)[0][0], 'slip', w)
    words_tot += 1; words_ok += ok_word
print(f'held-out (part B, {words_tot} words, {tot} groups) with the part-A key: {right} groups right, '
      f'{unknown} not in the part-A key, {wrong} wrong; of the groups the part-A key knows, {right}/{right + wrong} '
      f'= {100 * right / max(1, right + wrong):.1f}% agree with the slip; {words_ok}/{words_tot} words fully right')
if '--write' in sys.argv:
    for name in ('key.tsv', 'key_frozen.tsv'):
        with open(ROOT / name, 'w', encoding='utf-8', newline='\n') as f:
            f.write('# group\tvalue\ttype\tseen\tsource\n')
            for g in sorted(full, key=lambda x: (x.endswith('^'), int(x.rstrip('^')))):
                v, n = full[g].most_common(1)[0]
                f.write(f'{g}\t{v}\t{typ[g]}\t{sum(full[g].values())}\tslip scan 25 (Compiègne 23 July 1730)\n')
    print('wrote key.tsv and key_frozen.tsv')
