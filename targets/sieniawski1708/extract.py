"""Pull the cipher out of transcr/R74xx.txt: runs of 2-digit numbers (letter cipher) and 3-digit code numbers.

Output: runs.json  [{rec, line, nums:[...], sup:{i: letter}}], codes.json {code: [(rec, line, context)]}
Tokens: 10-79 two-digit numbers in a run of >=2 count as letter cipher; 100-599 three-digit numbers are codes.
Uncertain digits ("5?8", "78?|28") take the first reading; {?split} strings are split into pairs.
"""
import json, re, glob, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))

def clean_line(s):
    s = re.sub(r'\([^)]*\)', ' ', s)                 # drop transcriber comments in parentheses
    s = re.sub(r'~~[^~]*~~', ' ', s)                 # struck
    s = re.sub(r'\{\?split[^}]*\}', '', s)
    return s

TOK = re.compile(r"(\d+\??(?:\|\d+)?)(\^\[[^\]]*\]|\^[a-zäöü/?]+)?|([A-Za-zÄÖÜäöüß\[\]?]+\.?)|([.,;:])")

def parse(path):
    rec = os.path.basename(path)[:-4]
    out = []
    for raw in open(path, encoding='utf-8'):
        m = re.match(r'\[(P\w+) l\.(\d+)\]\s*(.*)', raw)
        if not m:
            mm = re.match(r'##\s*margin[^:]*:\s*"?(.*)', raw)
            if not mm: continue
            m = (None, 'margin', '0', mm.group(1))
            pg, ln, txt = m[1], m[2], m[3]
        else:
            pg, ln, txt = m.group(1), m.group(2), m.group(3)
        txt = clean_line(txt)
        toks = []
        for t in TOK.finditer(txt):
            if t.group(1):
                d = t.group(1).split('|')[0].replace('?', '')
                sup = t.group(2)[1:].strip('[]') if t.group(2) else None
                toks.append(('n', d, sup))
            elif t.group(3):
                toks.append(('w', t.group(3), None))
            else:
                toks.append(('p', t.group(4), None))
        out.append((rec, '%s:%s' % (pg, ln), toks))
    return out

def runs_and_codes(lines):
    runs, codes = [], collections.defaultdict(list)
    cur = None
    for rec, ln, toks in lines:
        for i, (k, v, sup) in enumerate(toks):
            nxt = toks[i+1] if i+1 < len(toks) else None
            if k == 'n' and (len(v) == 2 or (len(v) == 1 and (cur is not None or (nxt and nxt[0] == 'n' and len(nxt[1]) == 2)))):
                if cur is None:
                    cur = dict(rec=rec, line=ln, nums=[], sup={})
                if sup: cur['sup'][len(cur['nums'])] = sup
                cur['nums'].append(v)
                continue
            if k == 'n' and len(v) > 2 and len(v) % 2 == 0 and not (100 <= int(v) < 600 and len(v) == 3):
                # run-together digit string: split into pairs
                if cur is None: cur = dict(rec=rec, line=ln, nums=[], sup={})
                cur['nums'] += [v[j:j+2] for j in range(0, len(v), 2)]
                continue
            if cur is not None and k == 'p' and v == '.':
                cur['nums'].append('.'); continue
            if cur is not None:
                while cur['nums'] and cur['nums'][-1] == '.': cur['nums'].pop()
                if len([x for x in cur['nums'] if x != '.']) >= 2: runs.append(cur)
                cur = None
            if k == 'n' and len(v) == 3:
                ctx = ' '.join(x[1] for x in toks[max(0, i-4):i+5])
                codes[v].append((rec, ln, ctx, sup))
            if k == 'n' and len(v) == 1:
                pass
    if cur is not None and len(cur['nums']) >= 2: runs.append(cur)
    return runs, codes

if __name__ == '__main__':
    allruns, allcodes = [], collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(HERE, 'transcr', 'R*.txt'))):
        r, c = runs_and_codes(parse(p))
        allruns += r
        for k, v in c.items(): allcodes[k] += v
    json.dump(allruns, open(os.path.join(HERE, 'runs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    json.dump(allcodes, open(os.path.join(HERE, 'codes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n = sum(len([x for x in r['nums'] if x != '.']) for r in allruns)
    cnt = collections.Counter(x for r in allruns for x in r['nums'] if x != '.')
    print('runs', len(allruns), 'pairs', n, 'distinct', len(cnt))
    print(sorted(cnt.items(), key=lambda x: -x[1]))
    print('codes', sorted((k, len(v)) for k, v in allcodes.items()))
