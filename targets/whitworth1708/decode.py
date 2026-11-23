"""Apply key.tsv to the coded stretches of the duplicate of 1/12 Sept 1708 (stretches_1708-09-01.tsv) and write or
check decryption_1708-09-01.txt. The output is the unedited output of the key: a number that is not in the key is
shown as [number]; nothing is corrected or supplied.
Usage: python decode.py          check the decryption file against the key
       python decode.py --write  rewrite it
Also checks that the stretches hold the same groups, in the same order, as transcription_1708-09-01.txt, and that
key.tsv has the values frozen before the test (frozen/test2/table2_frozen.tsv)."""
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(here, *a)

def rows(path):
    return [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')][1:]

key = {r[0]: r[1] for r in rows(P('key.tsv'))}
frozen = {r[0]: r[1] for r in [l.rstrip('\n').split('\t') for l in open(P('frozen', 'test2', 'table2_frozen.tsv'), encoding='utf-8')][1:]}
assert key == frozen, 'key.tsv differs from the frozen table'

def transcription_groups(path):
    out = []
    for line in open(path, encoding='utf-8'):
        m = re.match(r'L\d+:\s*(.*)', line)
        if not m:
            continue
        for t in m.group(1).split():
            if t.startswith('{x:') or t.startswith('#'):
                continue
            t = t.strip('{^}')
            if re.fullmatch(r'[\d?]+(\|[\d?]+)*', t):
                out.append(t.split('|')[0])
    return out

st = rows(P('stretches_1708-09-01.tsv'))
flat = [g for r in st for g in r[2].split() if g != '/']
assert flat == transcription_groups(P('transcription_1708-09-01.txt')), 'stretches and transcription differ'

head = """# Whitworth to Boyle, Moscow, 1/12 Sept 1708, duplicate (SP 91/5, stamped f. 49): the 15 coded stretches.
# 'key:' is key.tsv applied group by group, unedited ([n] = number not in the key; '/' = a clear word between groups).
# '1886:' is NOT our decryption: it is the text the Sbornik of the Imperial Russian Historical Society, vol. 50, No. 22,
# prints between the same clear words, from the copy deciphered by the Secretary of State's office in 1708.
# Made by decode.py.
"""
lines = [head]
n_in = n_all = 0
for sid, place, groups, printed in st:
    gs = groups.split()
    dec = ' '.join('/' if g == '/' else key.get(g, f'[{g}]') for g in gs)
    n_all += sum(g != '/' for g in gs); n_in += sum(g in key for g in gs)
    lines.append(f'S{int(sid):02d} ({place})  {groups}\n   key:   {dec}\n   1886:  {printed}\n')
text = '\n'.join(lines)
if '--write' in sys.argv:
    open(P('decryption_1708-09-01.txt'), 'w', encoding='utf-8', newline='\n').write(text)
else:
    assert open(P('decryption_1708-09-01.txt'), encoding='utf-8').read() == text, 'decryption file is not what the key gives'
print(f'1708-09-01: {len(st)} coded stretches, {n_all} numbers, {n_in} in the key: ok')
print('result: ok')
