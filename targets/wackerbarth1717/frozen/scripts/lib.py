# Bibliothèque commune : lecture des relevés, normalisation, décodage.
import re, unicodedata, glob, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = os.path.join(D, 'releves')

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('j', 'i').replace('v', 'u')
    return re.sub(r'[^a-z#]', '', s)

def tokens(cline):
    """Jetons d'une ligne C: -> liste de ('n', '44') | ('t', 'mot clair') ; biffés et illisibles ignorés."""
    out = []
    for m in re.finditer(r'\{([^}]*)\}|(\S+)', cline):
        if m.group(1) is not None:
            out.append(('t', m.group(1))); continue
        t = m.group(2)
        if t.startswith('~') or t in ('…', '...'):
            continue
        if '>' in t:
            t = t.split('>')[1]
        t = t.rstrip('?')
        if '/' in t:
            t = t.split('/')[0]
        if re.fullmatch(r'\d+', t):
            out.append(('n', t))
    return out

def read_releve(path):
    """-> liste de passages : dict(scan, nom, lines=[(Lid, tokens, gloss)], nogloss)"""
    scan = os.path.basename(path)[2:6]
    ps = []; cur = None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('## '):
            cur = dict(scan=scan, nom=line[3:], lines=[], nogloss='SANS GLOSE' in line); ps.append(cur); continue
        m = re.match(r'(L\d+) ([CG]): ?(.*)', line)
        if not m or cur is None: continue
        lid, kind, txt = m.groups()
        if kind == 'C':
            cur['lines'].append([lid, tokens(txt), ''])
        else:
            g = txt.strip()
            if g in ('—', '-'): g = ''
            g = re.sub(r'~[^~]*~', '', g)
            # glose de la ligne lid
            for L in cur['lines'][::-1]:
                if L[0] == lid: L[2] += ' ' + g.replace('|', ' '); break
            else:
                cur['lines'].append([lid, [], g])
    return ps

def train_passages():
    ps = []
    for p in sorted(glob.glob(os.path.join(REL, 'T-*.txt'))):
        ps += read_releve(p)
    return ps

def load_key(path):
    K = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        f = line.rstrip('\n').split('\t')
        if len(f) >= 2 and f[1] != '':
            K[f[0]] = f[1]
    return K
