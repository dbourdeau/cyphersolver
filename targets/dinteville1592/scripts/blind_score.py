"""Blind test: decode the independent blind transcription with key130 and compare, token by token, with the
published reading (reading130.tsv). A token agrees if its key value admits the reading letter (or both are null)."""
import decode, measure
k = decode.key('../key.tsv'); k.update({'rho': '-', 'newPx': 'i'})
R = measure.readings('../reading_f130.tsv')
tot = ok = 0
for l in open('../blind/blind_transcription.txt'):
    if l.startswith('#'): continue
    n, s = l.rstrip('\n').split('\t'); B = ' '.join(t.split('|')[0] for t in s.split()).replace('a rho', 'aP').split(); r = R[n]
    assert len(B) == len(r), (n, len(B), len(r))
    a = 0
    for t, c in zip(B, r):
        if c == '?': continue
        v = k.get(t, '?'); allowed = {'-'} if v == '-' else {measure.eq(x) for x in v.split('/')}
        a += (c == '-' and v == '-') or measure.eq(c) in allowed or False
    m = sum(1 for c in r if c != '?'); tot += m; ok += a
    print(f'{n}: {a}/{m} letters agree')
print(f'blind transcription reproduces {ok}/{tot} = {ok/tot:.1%} of the reading')
