"""Own decoder (integration of issue #553, 14 Nov 2026), not the contributor's verify.py: apply key.json to
transcription.txt, print the letters per page gap, and align the glyph sequence with Tomokiyo's transcription
(../elizabeth_moray.txt) position by position. Standard library only.  python3 own_decode.py"""
import collections, json, os
H = os.path.dirname(os.path.abspath(__file__))
key = {k: v['value'] for k, v in json.load(open(os.path.join(H, 'key.json'))).items() if not k.startswith('_')}
seq = []
for line in open(os.path.join(H, 'transcription.txt')):
    if line.startswith('L'):
        tag, body = line.split(':', 1)
        print(tag + ': ' + ' | '.join(''.join(key[t] for t in g.split()) for g in body.split('|')))
        seq += body.replace('|', ' ').split()
tm = [t for l in open(os.path.join(H, '..', 'elizabeth_moray.txt')) if not l.startswith('#')
      for t in l.strip().strip(';').split(';') if t]
print(len(seq), 'glyphs here,', len(tm), "in Tomokiyo's transcription")
if len(seq) == len(tm):
    m = collections.defaultdict(collections.Counter)
    for a, b in zip(seq, tm):
        m[b][a] += 1
    for b in sorted(m):
        if len(m[b]) > 1:
            print('Tomokiyo', b, 'split here into', dict(m[b]))
