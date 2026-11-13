"""python scripts/pairs_litB.py key_1741.tsv transcription_litB_all.txt : print each row as group=value pairs (unknown = ?)"""
import sys
sys.path.insert(0, __file__.rsplit('pairs_litB.py',1)[0])
from decrypt_litB import load_key, tokens
k = load_key(sys.argv[1])
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab, rest = l.split(' ', 1)
    print(lab, ' '.join(t[1] if t[0] != 'g' else '%s=%s' % (t[1], k.get(t[1], '?')) for t in tokens(rest)))
