"""Apply key.json to transcription.txt (Penn LJS 51, f. 48r l.8 - 48v l.13). Prints one line per manuscript line.
| is the dotted-stem word divider; a word may run over a line end. Usage: python decode.py"""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(D, 'key.json'), encoding='utf8'))
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf8'):
    if line.startswith('#') or not line.strip():
        continue
    lab, *toks = line.split()
    print(lab, ''.join(' ' if t == '|' else key.get(t, '?') for t in toks).strip())
