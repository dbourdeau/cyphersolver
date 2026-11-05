"""Decode transcription.txt with key/key274.json plus key/overrides.json (context-corrected values).
usage: python tools/decode.py [ctx N N ...]   -> full decode, or contexts of the listed groups"""
import json, re, sys
def load():
    k = {int(a): b for a, b in json.load(open('key/key274.json', encoding='utf8')).items()}
    try:
        o = json.load(open('key/overrides.json', encoding='utf8'))
        for a, v in o.items():
            k[int(a)] = v['value'] if isinstance(v, dict) else v
    except FileNotFoundError:
        pass
    return k
def tokens():
    out = []; fol = ''
    for l in open('transcription.txt', encoding='utf8'):
        l = l.rstrip('\n')
        if l.startswith('#'): continue
        if l.startswith('@'): fol = l[1:]; out.append((fol, '@', None)); continue
        for t in re.findall(r'\[[^\]]*\]|\([^)]*\)|\d+[?~^]*|[|]', l.replace('¶', '')):
            out.append((fol, t, l))
    return out
def val(k, t):
    if t.startswith('['): return t
    if t.startswith('('): return ''
    if t == '|': return '/'
    n = int(t.rstrip('?~^'))
    return k.get(n, '#%d' % n) + ('~' if t.endswith('~') else '')
if __name__ == '__main__':
    k = load(); toks = tokens()
    if len(sys.argv) > 1 and sys.argv[1] == 'ctx':
        for target in map(int, sys.argv[2:]):
            print('=====', target, k[target]); shown = 0
            for i, (f, t, l) in enumerate(toks):
                if re.fullmatch(str(target) + r'[?~^]*', t):
                    seg = toks[max(0, i-6):i+7]
                    print(f, ' '.join(('<<' + val(k, x[1]) + '>>' if x is toks[i] else val(k, x[1])) for x in seg if x[1] != '@'))
    else:
        for f, t, l in toks:
            if t == '@': print('\n@' + f); continue
            print(val(k, t), end=' ')
        print()
