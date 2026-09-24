"""Extract cipher token lines from an agent transcript (lines starting 'm.NN' or 'Cn:'), dropping clear text,
{notes}, '?' marks and line labels. Writes <name>.tok (one manuscript line per line, clear text as [ ])."""
import re, sys
src, out = sys.argv[1], sys.argv[2]
merge = dict(kv.split(':') for kv in sys.argv[3].split(',')) if len(sys.argv) > 3 else {}
lines = []
for l in open(src, encoding='utf-8'):
    m = re.match(r'\s*(m\.\d+b?|C\d+|L\d+[^:]*):?\s(.*)', l)
    if not m: continue
    body = re.sub(r'\{[^}]*\}', ' ', m.group(2))
    body = re.sub(r'\(ink blot[^)]*\)', ' ', body)
    body = re.sub(r'\([^)]*\)', ' ', body) if '[' not in body else body
    toks = []
    for t in re.split(r'(\[[^\]]*\])|\s+', body):
        if not t: continue
        if t.startswith('['): toks.append('[x]'); continue
        if t in ('/', '??'): continue
        t = t.rstrip('?')
        if not t: continue
        toks.append(merge.get(t, t))
    if any(not t.startswith('[') for t in toks): lines.append(' '.join(toks))
open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print(len(lines), sum(len([t for t in l.split() if not t.startswith('[')]) for l in lines))
