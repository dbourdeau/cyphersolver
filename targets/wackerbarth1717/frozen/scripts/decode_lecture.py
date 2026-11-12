# Décodage de lecture (Avenant 3) : relevé gelé -> texte brut par ligne, clé c ; nombres absents de la clé = ‹n›.
# usage: decode_lecture.py KEY RELEVE...   (aucune correction du relevé ; doutes N/M? -> 1re lecture, alternative signalée)
import sys, re
K = {}
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t')
    K[f[0]] = f[1] if len(f) > 1 else ''
def val(n):
    if n not in K: return '‹%s›' % n
    v = K[n]
    return '·' if v == '' else (v.upper() if v.startswith('[') else v)
for path in sys.argv[2:]:
    print('=====', path.split('/')[-1])
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('#'): print(line); continue
        m = re.match(r'\s*([A-Z]+\d+) C: ?(.*)', line)
        if not m: continue
        out = []
        for t in re.finditer(r'\{([^}]*)\}|(\S+)', m.group(2)):
            if t.group(1) is not None: out.append(' «' + t.group(1) + '» '); continue
            x = t.group(2)
            if x.startswith('~') or x in ('…', '...'): out.append('…' if not x.startswith('~') else ''); continue
            if '>' in x: x = x.split('>')[1]
            alt = None
            x = x.rstrip('?')
            if '/' in x: x, alt = x.split('/')[:2]
            if not re.fullmatch(r'\d+', x): out.append('?'+x); continue
            s = val(x)
            if alt and re.fullmatch(r'\d+', alt) and val(alt) != s: s = '(%s|%s)' % (s, val(alt))
            out.append(s)
        print(m.group(1), ''.join(out))
