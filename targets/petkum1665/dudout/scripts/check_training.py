"""Compare the post-hoc training transcription with key T (information only, not a measure).
Usage (from dudout/):  python3 -I scripts/check_training.py > results/training_vs_T.tsv"""
import json, os, re, unicodedata
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t = json.load(open(os.path.join(HERE, 'key', 'table_T.json'), encoding='utf-8'))
T, obs = t['T'], set(t['obs'])
def norm(s):
    return re.sub('[^a-z]', '', unicodedata.normalize('NFD', s.lower()))
n = agree = 0; seen = set(); diffs = []
for l in open(os.path.join(HERE, 'transcriptions', 'training_A_posthoc.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    p = l.rstrip('\n').split('\t'); toks = p[0].split('.'); seen |= set(toks); n += 1
    pred = ''.join(T.get(x, '[%s]' % x) for x in toks)
    if norm(pred) == norm(p[1]):
        agree += 1
    else:
        diffs.append((p[0], pred, p[1], p[2] if len(p) > 2 else ''))
print('# glossed passages\t%d' % n)
print('# T value = gloss (a-z)\t%d' % agree)
print('# T keys marked seen (obs) not met in this transcription\t%s' % ' '.join(sorted(obs - seen)) )
print('# differing passages: groups\tT gives\tgloss\tremark')
for d in diffs:
    print('\t'.join(d))
