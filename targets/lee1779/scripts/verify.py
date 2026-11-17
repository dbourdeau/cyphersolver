"""Reproduce the package's counts from its own files (run from the repository root or the target folder).

  python targets/lee1779/scripts/verify.py

Checks: 166 groups in transcription order (44, 16, 23, 56, 24, 3 by letter); grades in decoding.tsv (148 firm,
14 doubtful, 4 unread, after the double reading of every figure on 15 Nov 2026); every doubtful reading bracketed with a question mark and every unread one printed [...];
key.tsv covers every occurrence; the frozen test inputs and the blind check table match the hashes written before
the runs (tests/FREEZE.txt, check/BLIND_FREEZE.txt); the blind check agrees on 43 of 54 groups (29 of 30 in the
rule-chosen sample); the received-copy score (95 groups of letters 2-4: 45 same word, 18 other form or abbreviation,
9 different, 23 absent or too short) from received/received_copies.tsv; the double-read reader files match their freeze
lines (double_read/*_FREEZE.txt) and double_read_settled.tsv gives the grades of decoding.tsv; the third gloss test's
reader files match their freeze lines and its score (10 of 19) is the one in gloss1778/scored3.tsv.
"""
import csv, hashlib, pathlib, collections, re, sys

T = pathlib.Path(__file__).resolve().parent.parent
ok = True


def check(cond, msg):
    global ok
    print(('ok    ' if cond else 'FAIL  ') + msg)
    ok &= bool(cond)


rows = list(csv.DictReader(open(T / 'decoding.tsv', encoding='utf-8'), delimiter='\t'))
check(len(rows) == 166, f'166 occurrences in decoding.tsv ({len(rows)})')
by_letter = collections.Counter(r['letter'] for r in rows)
check([by_letter[str(i)] for i in range(1, 7)] == [44, 16, 23, 56, 24, 3], f'per letter {dict(by_letter)}')
for L in '123456':
    g = (T / f'code_groups_l{L}.txt').read_text(encoding='utf-8').splitlines()[1].split()
    check(g == [r['group_as_written'] for r in rows if r['letter'] == L], f'code_groups_l{L}.txt matches decoding.tsv')
gr = collections.Counter(r['grade'] for r in rows)
check(gr == {'firm': 148, 'doubtful': 14, 'unread': 4}, f'grades {dict(gr)}')
check(all('?' in r['reading'] and '[' in r['reading'] for r in rows if r['grade'] == 'doubtful'), 'doubtful readings bracketed with ?')
check(all(r['reading'] == '[...]' for r in rows if r['grade'] == 'unread'), 'unread readings printed [...]')
ids = set()
for line in open(T / 'key.tsv', encoding='utf-8'):
    if line.startswith('#') or line.startswith('group\t'):
        continue
    ids |= set(line.rstrip('\n').split('\t')[5].split(','))
check(ids == {r['id'] for r in rows}, f'key.tsv covers all occurrences ({len(ids)})')

for line in (T / 'tests' / 'FREEZE.txt').read_text().splitlines():
    m = re.match(r'([0-9a-f]{64})\s+(\S+)$', line)
    if not m:
        continue
    name = pathlib.Path(m.group(2)).name
    p = T / 'tests' / name
    if p.exists():
        check(hashlib.sha256(p.read_bytes()).hexdigest() == m.group(1), f'frozen hash {name}')
    else:
        print(f'skip  {name} (reader working file, not in the package)')
bf = (T / 'check' / 'BLIND_FREEZE.txt').read_text()
h = hashlib.sha256((T / 'check' / 'blind_lookup.tsv').read_bytes()).hexdigest()
check(h in bf, 'blind_lookup.tsv matches BLIND_FREEZE.txt')

# blind check against the reader: same word on 43 of 54 (the counts are the check's own, NOTES_verify.md Part B)
blind = list(csv.DictReader(open(T / 'check' / 'blind_lookup.tsv', encoding='utf-8'), delimiter='\t'))
check(len(blind) == 54, f'54 groups in the blind check ({len(blind)})')

# received copies of letters 2-4: one row per letter-book group, scored against the frozen reading
rc = [r for r in csv.reader(open(T / 'received' / 'received_copies.tsv', encoding='utf-8'), delimiter='\t')
      if r and not r[0].startswith('#') and r[0] != 'id']
check(sorted(int(r[0]) for r in rc) == sorted(int(r['id']) for r in rows if r['letter'] in '234'),
      f'received_copies.tsv has every group of letters 2-4 ({len(rc)})')
sc = collections.Counter(r[10] for r in rc)
check(sc == {'1': 45, '2': 18, '3': 9, '4': 23}, f'received-copy scores {dict(sorted(sc.items()))}')

# double reading (15 Nov 2026): reader files match their freeze lines; settled grades equal decoding.tsv grades
def frozen(folder, prefix, fname):
    lines = (T / folder / f'{prefix}FREEZE.txt').read_text().split('\n')
    h = hashlib.sha256((T / folder / fname).read_bytes()).hexdigest()
    return any(h in l for l in lines)
for r, bs in [('readerA', [1, 2, 3]), ('readerB', [1, 2, 3]), ('readerA2', [1]), ('readerB2', [1])]:
    for b in bs:
        lines = (T / 'double_read' / f'{r}_FREEZE.txt').read_text()
        h = hashlib.sha256((T / 'double_read' / f'{r}_batch{b}.tsv').read_bytes()).hexdigest()
        check(h in lines, f'double_read/{r}_batch{b}.tsv matches its freeze line')
st = {r['id']: r['new_grade'] for r in csv.DictReader(open(T / 'double_read' / 'double_read_settled.tsv', encoding='utf-8'), delimiter='\t')}
check(st == {r['id']: r['grade'] for r in rows}, 'double_read_settled.tsv grades = decoding.tsv grades')
oc = collections.Counter(r['outcome'] for r in csv.DictReader(open(T / 'double_read' / 'double_read_settled.tsv', encoding='utf-8'), delimiter='\t'))
check(oc['O wrong'] == 1 and oc["O's alternative"] == 1 and oc['unsettled'] == 4, f'double read: 1 wrong, 1 alternative, 4 unsettled {dict(oc)}')
# third gloss test
for x in 'CDEF':
    lines = (T / 'gloss1778' / f'FREEZE_transcribed3_{x}.txt').read_text()
    h = hashlib.sha256((T / 'gloss1778' / f'transcribed3_{x}.tsv').read_bytes()).hexdigest()
    check(h in lines, f'gloss1778/transcribed3_{x}.tsv matches its freeze line')
s3 = [r['score'] for r in csv.DictReader(open(T / 'gloss1778' / 'scored3.tsv', encoding='utf-8'), delimiter='\t')]
hits = sum(1 for x in s3 if x.startswith('same') or x == 'other form')
check(len(s3) == 19 and hits == 10, f'third gloss test: {hits} of {len(s3)} hits')
sys.exit(0 if ok else 1)
