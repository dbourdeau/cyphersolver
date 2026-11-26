"""Apply a key to nov_transcription_v2.tsv. Bracket alternatives ([23] etc.) are expanded;
a candidate with a key value is preferred. Usage: python decode_nov.py [key.tsv ...]"""
import csv, re, sys, itertools, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def load_key(paths):
    k = {}
    for p in paths:
        for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'):
            n = r['number'].strip(); v = r['value'].strip()
            if n.isdigit() and v and ' / ' not in v and '?' not in v:
                k[int(n)] = re.sub(r'\s*\(.*', '', v)
    return k
def expand(tok):
    t = tok.replace('?', '').replace('…', '')
    parts = re.findall(r'\[(\d+)\]|(\d)', t)
    if not parts: return []
    opts = [list(a) if a else [b] for a, b in parts]
    return [int(''.join(c)) for c in itertools.product(*opts)][:16]
import os
VERB = os.environ.get('VERB')
ONLY = os.environ.get('ONLY','')
if __name__ == '__main__':
    key = load_key(sys.argv[1:] or ['sept_key_from_pair.tsv', 'key_nov_extension.tsv'][:1])
    rows = list(csv.DictReader(open('nov_transcription_v2.tsv', encoding='utf-8'), delimiter='\t'))
    tot = hit = 0; cur = None; out = []
    for r in rows:
        if ONLY and not r['folio'].startswith(ONLY): continue
        fl = (r['folio'], r['line'])
        if fl != cur:
            if out: print(' '.join(out))
            out = [f"{r['folio']}.{r['line']}:"]; cur = fl
        if r['kind'] == 'clear': out.append(r['text']); continue
        c = expand(r['text']); tot += 1
        v = next((key[x] for x in c if x in key), None)
        if v: hit += 1; out.append((r['text']+'=' if VERB else '‹') + v + ('' if VERB else '›'))
        else: out.append('{' + r['text'] + '}')
    print(' '.join(out)); print(f'# groups {tot}, with a key value {hit} ({hit/tot:.3f})')
