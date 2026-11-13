# compare_second.py: numeral-by-numeral alignment of each second transcription with the first (difflib per line, as the
# session scripts b112 cmp.py and b125 cmp2.py). Standard library only.   python3 -I despatches/scripts/compare_second.py
# Writes controls/alignment.txt. Counts: aligned positions; agree; disagree; cut in the first and full in the second
# ('recovered'); cut in both; insertions/deletions.
import os, re, sys, difflib, hashlib
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build
PAIRS = [  # (despatch, label, second file, its frozen md5, first file, note)
    ('1676-02-12', '162L', '1676-02-12/transcriptions/162L_b125_second.txt', '601302116a70cc68e1aba29817bd84c9', '1676-02-12/transcriptions/162L_b124.txt', 'b125 decode-blind second transcription, frozen 08:10:02 UTC before b124 files were opened; first line of b124 162L segmentation seen at 08:12 after the freeze (session log)'),
    ('1676-02-12', '163L', '1676-02-12/transcriptions/163L_b125_second.txt', '27c18dff201196d60051f1e336af2af3', '1676-02-12/transcriptions/163L_b124.txt', 'as above'),
    ('1676-02-12', '164L', '1676-02-12/transcriptions/164L_b125_second.txt', 'ba48847e4c42285d006561c1a84a7f88', '1676-02-12/transcriptions/164L_b124.txt', 'as above'),
    ('1676-02-12', '165L', '1676-02-12/transcriptions/165L_b125_second.txt', '6dd544c0136c910d2a7d2c8efc16b92a', '1676-02-12/transcriptions/165L_b124.txt', 'as above'),
    ('1676-10-06', '318L blind', '1676-10-06/transcriptions/318L_b112_blind.txt', '405eb15d40f03d67dd007212b948d91a', '1676-10-06/transcriptions/318L_b111.txt', 'b112 blind of b111 files by its record, frozen 04:57:56 UTC; not decoded'),
    ('1676-10-06', '318R blind', '1676-10-06/transcriptions/318R_b112_blind.txt', '95f4e5fe7608029e7b2330c7b8139451', '1676-10-06/transcriptions/318R_b111.txt', 'as above'),
    ('1676-10-06', '318L adjudicated', '1676-10-06/transcriptions/318L_b112_second_adjudicated.txt', '8f236787c63b55a9c9717de31958bb0d', '1676-10-06/transcriptions/318L_b111.txt', 'b112 after adjudication against b111 (NOT blind); decoded once with v7'),
    ('1676-10-06', '318R adjudicated', '1676-10-06/transcriptions/318R_b112_second_adjudicated.txt', 'a5a9f0c733f1a1c0cc9c5e61ebb10dfa', '1676-10-06/transcriptions/318R_b111.txt', 'as above')]
def load(text):
    d = {}
    for n, body in build.rlines(text, 'all'): d[int(n)] = [p for p in re.findall(r'"[^"]*"|\S+', body) if not p.startswith('"')]
    return d
out = ['# Second transcriptions aligned with the first, numeral by numeral (scripts/compare_second.py).']
for d, label, sec, m, first, note in PAIRS:
    raw = open(P(sec), 'rb').read(); assert hashlib.md5(raw).hexdigest() == m, sec
    t = raw.decode('utf-8')
    if '_b125_' in sec: t = build.torfmt(t)[0]
    a = load(t); b = load(open(P(first), encoding='utf-8').read())
    st = dict(pos=0, agree=0, disagree=0, recovered=0, cut_in_second_only=0, cut_in_both=0, indel=0); lines = []
    for k in sorted(set(a) | set(b)):
        x = a.get(k, []); y = b.get(k, [])
        sm = difflib.SequenceMatcher(None, [q.rstrip('~') for q in x], [q.rstrip('~') for q in y], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
                for p, q in zip(x[i1:i2], y[j1:j2]):
                    st['pos'] += 1; pc = '~' in p; qc = '~' in q
                    if qc and not pc: st['recovered'] += 1; lines.append('  R%d recovered: first %s, second %s' % (k, q, p))
                    elif qc and pc: st['cut_in_both'] += 1
                    elif pc: st['cut_in_second_only'] += 1; lines.append('  R%d cut in second only: second %s, first %s' % (k, p, q))
                    elif p == q: st['agree'] += 1
                    else: st['disagree'] += 1; lines.append('  R%d disagree: second %s, first %s' % (k, p, q))
            else:
                st['indel'] += max(i2 - i1, j2 - j1); lines.append('  R%d %s: second [%s], first [%s]' % (k, op, ' '.join(x[i1:i2]), ' '.join(y[j1:j2])))
    full = st['agree'] + st['disagree']
    out.append('\n## %s %s: %s\n%s vs %s\n%s\nfull numerals in both: %d, the same %d (%.2f%%)' % (d, label, note, sec, first,
               ' '.join('%s %d' % kv for kv in st.items()), full, st['agree'], 100.0 * st['agree'] / full if full else 0))
    out += lines
open(P('controls', 'alignment.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(l for l in out if not l.startswith('  ')))
