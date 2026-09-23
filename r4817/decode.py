"""Reproduce the literal reading. IDs name manuscript signs, not plaintext letters.

The formatted reading changes U to V in UOM only (one shared U/V sign).
No emendation of GEFAE is made in this decoder. Run from any directory.
"""
import json
from pathlib import Path
from collections import Counter

HERE = Path(__file__).resolve().parent
key = json.loads((HERE / 'key.json').read_text(encoding='utf-8'))
lines = [line.split() for line in (HERE / 'transcription.txt').read_text().splitlines() if line.strip()]
word_lengths = [[5,7,3], [3,5,3,6], [3,5,3,4], [4,5,5,3], [5,3,3,4]]
decoded = []
ledger = []
for line_no, (tokens, sizes) in enumerate(zip(lines, word_lengths), 1):
    assert len(tokens) == sum(sizes)
    chars = [key[t]['value'].upper() for t in tokens]
    for pos, (token, char) in enumerate(zip(tokens, chars), 1):
        anomaly = (line_no, pos) == (3, 8)
        ledger.append({'line':line_no, 'position':pos, 'sign':token, 'literal':char,
                       'grade':'M' if anomaly else 'I', 'coherent_without_emendation':not anomaly})
    words=[]
    start=0
    for size in sizes:
        words.append(''.join(chars[start:start+size])); start += size
    decoded.append(' '.join(words))
literal='\n'.join(decoded)+'\n'
(HERE / 'literal.txt').write_text(literal, encoding='utf-8')
(HERE / 'token_ledger.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
summary = {'tokens':len(ledger), 'distinct_signs':len(set(x['sign'] for x in ledger)),
           'line_lengths':[len(x) for x in lines], 'assigned':len(ledger),
           'coherent_without_emendation':sum(x['coherent_without_emendation'] for x in ledger),
           'grades':dict(Counter(x['grade'] for x in ledger))}
(HERE / 'verification.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(literal)
print(json.dumps(summary))
