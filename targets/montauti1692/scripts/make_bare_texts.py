"""Write bare/P*_groups.txt and bare/P*_decode.txt from bare/bare_transcriptions.tsv with key v3 + context values.
Run from the target folder: python scripts/make_bare_texts.py"""
import json

def load(fn):
    return {a: b for a, b in json.load(open(fn, encoding='utf-8')).items() if not a.startswith('_')}

k = load('key/key_v3.json'); k.update(load('key/key_v3_context.json'))
ctx = {'ww', '62'}
P = {}
for l in open('bare/bare_transcriptions.tsv', encoding='utf-8'):
    if l.startswith('passage'):
        continue
    c = l.rstrip('\n').split('\t'); P.setdefault(c[0], []).append(c)
for p, rows in P.items():
    g = [f"# {p}: cipher groups as written ('+' = one sign shared by two groups; '?' = doubtful group; '##' = unread group). From bare/bare_transcriptions.tsv (one forward pass, doubtful clusters re-read)."]
    d = [f"# {p}: decode with key v3 + context values (x+ = context-only value ww = o; [n] = no letter value, probably a code number). Clear words before and after each run in braces."]
    for c in rows:
        g.append(f"# {c[1]} line {c[2]}"); g.append(c[4])
        out = []
        for tok in c[4].split():
            for t in tok.split('+'):
                t = t.lstrip('?')
                if t == '##':
                    out.append('[..]'); continue
                v = k.get(t); out.append(f"[{t}]" if v is None else v + ('+' if t in ctx else ''))
        d.append(f"{c[1]} line {c[2]}: {{{c[3]}}} " + ' '.join(out) + f" {{{c[6] if len(c) > 6 else ''}}}")
    open(f'bare/{p}_groups.txt', 'w', encoding='utf-8').write('\n'.join(g) + '\n')
    open(f'bare/{p}_decode.txt', 'w', encoding='utf-8').write('\n'.join(d) + '\n')
