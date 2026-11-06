"""Print a transcription line by line with a key applied (clear words kept in brackets)."""
import re, sys
KEY = dict((kv[0], kv[2:]) for kv in sys.argv[2].split())
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    n, body = l[:2], l[3:].rstrip('\n')
    out = []
    for tok in re.findall(r'\[[^\]]*\]|\S+', body):
        if tok.startswith('[') or re.fullmatch(r'[\d/]+', tok):
            out.append(tok)
        else:
            out.append(''.join(KEY.get(g, g.upper() if g.isalpha() else g) for g in tok))
    print(n, ' '.join(out))
