"""Decode a transcription with a key.
usage: python3 decrypt.py KEY.tsv TRANSCRIPTION.txt [line-prefix]
KEY.tsv: sign<TAB>value<TAB>basis. TRANSCRIPTION: line id<TAB>tokens, clear runs in {...}.
A sign with no value prints _ ; a trailing ? on a sign (doubtful reading) is ignored; clear runs print as ' | '."""
import sys, re
key = {}
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or '\t' not in l: continue
    f = l.rstrip('\n').split('\t'); key[f[0]] = f[1]
pref = sys.argv[3] if len(sys.argv) > 3 else ''
for l in open(sys.argv[2], encoding='utf-8'):
    if '\t' not in l or l.startswith('#') or not l.startswith(pref): continue
    lid, t = l.rstrip('\n').split('\t', 1); t = re.sub(r'\{[^}]*\}', ' {clear} ', t); out = []
    for tok in t.split():
        if tok == '{clear}': out.append(' | '); continue
        s = tok.rstrip('?'); out.append(key.get(s, '_') if s else '?')
    print(lid + '\t' + ''.join(out))
