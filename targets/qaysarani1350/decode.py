"""Apply key.json to transcription.txt and print the letter-for-letter decode, one cipher line per line."""
import json, pathlib, re
here = pathlib.Path(__file__).resolve().parent
key = json.loads((here / 'key.json').read_text(encoding='utf8'))['key']
for line in (here / 'transcription.txt').read_text(encoding='utf8').splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    n, body = line.split(':', 1)
    out = []
    for tok in body.split():
        t = re.sub(r'[()\[\]]', '', tok)
        out.append(' ' if t == '|' else key[t])
    print(n + ': ' + ''.join(out).strip())
