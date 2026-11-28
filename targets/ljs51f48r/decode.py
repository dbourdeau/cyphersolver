"""Apply key.json to transcription.txt (Penn LJS 51, f. 48r l.8 - 48v l.13, then 21r l.1-5). Prints one line per manuscript line.
| is the dotted-stem word divider; a word may run over a line end. Usage: python decode.py"""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(D, 'key.json'), encoding='utf8'))
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf8'):
    if line.startswith('#') or not line.strip():
        continue
    lab, *toks = line.split()
    letters = [' ' if t == '|' else key[t] for t in toks]
    # The horned sign has two attested readings, one per line in the continuation.
    if 'EK' in toks:
        letters[toks.index('EK')] = {'21r02': 'ح', '21r03': 'ش'}[lab]
    print(lab, ''.join(letters).strip())
