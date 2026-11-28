"""PASS 2: ONE decode with the key leaf's key (KEY_LEAF.tsv), written 25 Nov 2026 before the freeze (FREEZE_PENT.txt).
Inputs: tx2/f004r.txt f004v.txt f015r.txt f159r.txt f034r_p34.txt (first-pass transcriptions with the SIGNS8 changes)
and tx/PENTACLES.txt (new). Refuses to run if any frozen file's sha256 differs from FREEZE_PENT.txt.
Writes DECODE_KEYLEAF.txt and work/decode_keyleaf_counts.txt. No emendation; unknown signs print as [?].

Rules, all from the leaf (KEY_LEAF.tsv), applied in this order inside a word:
  - whole word `4 Cl` = enim, `Lm Cl` = autem;
  - pairs: Tk+D1 re, Tk+Cl ri, Ds+D1 ti, Ds+Cl tr, Cl+Ds rt (left to right; a pair consumes both signs);
  - D1 or Cl in any other place: no value, [?];
  - D2 (..) and D3 (.:) = the letter of the nearest preceding sign in the word marked with an inner dot (*).
    D3 is "the same letter, when it is repeated again": it takes the value the last D2 or D3 of the word took.
    DECLARED FALLBACK (the transcriptions mark inner dots only where seen, and the first-pass files never do): when no
    sign before it in the word carries *, D2 takes the value of the nearest preceding lambda (Lm, a), box (Bx, o) or
    x (X, i) - the three signs ../SIGNS.md records as often carrying an inner dot. If there is none, [?];
  - dot above (+^) = m, dot below (+_) = n, after the sign's letters; diaeresis (+") = the sign's value twice;
  - Tk@ followed by a dot above = rum (leaf); Oe with a dot above = quae (leaf), Oe" = quod, Oe~ = quem, Oe^m = quam;
  - a bar (~) on a sign whose barred form is not on the leaf = the sign's value followed by ~ (usual Latin suspension,
    leaf: "Andre Abbreviationes ... forstaaes aff sig selff"); ~ is printed, not expanded, not counted as a letter;
  - any label not in the key = [?]. The placeholder ? has no value.
"""
import sys, os, hashlib, re

K = '/home/claude/keyless/round40c/basel_anv9/keyleaf/'
FROZEN = ['KEY_LEAF.tsv', 'tx/PENTACLES.txt', 'tx2/f004r.txt', 'tx2/f004v.txt', 'tx2/f015r.txt', 'tx2/f159r.txt',
          'tx2/f034r_p34.txt', 'scripts/decode_keyleaf.py']
frz = open(K + 'FREEZE_PENT.txt').read()
for f in FROZEN:
    h = hashlib.sha256(open(K + f, 'rb').read()).hexdigest()
    assert h in frz, 'frozen file changed: ' + f

KEY = {}
for ln in open(K + 'KEY_LEAF.tsv', encoding='utf-8'):
    if ln.startswith('#') or ln.startswith('token'):
        continue
    p = ln.rstrip('\n').split('\t')
    KEY[p[0]] = p[1]
PAIRS = {('Tk', 'D1'): 're', ('Tk', 'Cl'): 'ri', ('Ds', 'D1'): 'ti', ('Ds', 'Cl'): 'tr', ('Cl', 'Ds'): 'rt'}
WORDS = {('4', 'Cl'): 'enim', ('Lm', 'Cl'): 'autem'}
BASES = sorted(set([k for k in KEY if k[0] not in '+#'] + ['D1', 'D2', 'D3', 'Cl', 'Ec', 'Sz', 'Yy', '?']),
               key=lambda s: -len(s))
SEP = {'^': '+^', '_': '+_', '"': '+"'}
DOTTABLE = {'Lm', 'Bx', 'X'}


def split_sign(sg):
    """-> (base_with_attached_marks, dotted_inside, [separate mod tokens])"""
    star = '*' in sg
    sg = sg.replace('*', '')
    for full in ('Oe^m', 'Oe"', 'Oe~', 'Oe^', 'Tk@^', 'Bx~'):     # leaf forms that include a mark
        if sg.startswith(full):
            rest = sg[len(full):]
            return full, star, [SEP[c] for c in rest if c in SEP]
    base = next((b for b in BASES if sg.startswith(b)), None)
    if base is None:
        return '?', star, []
    rest, att, mods = sg[len(base):], '', []
    for c in rest:
        if c in SEP:
            mods.append(SEP[c])
        else:
            att += c
    return base + att, star, mods


def value(tok):
    if tok in KEY:
        return KEY[tok]
    if tok.endswith('~') and tok[:-1] in KEY:
        return KEY[tok[:-1]] + '~'
    return None


def decode_word(signs):
    signs = [s for s in signs if s not in ('Eq', 'Fill')]
    bases = [split_sign(s) for s in signs]
    if tuple(b[0] for b in bases) in WORDS and not any(b[2] for b in bases):
        return WORDS[tuple(b[0] for b in bases)], 0
    out, unk, i, hist, last_d = '', 0, 0, [], None   # hist: (letter value, dotted, base label)
    while i < len(bases):
        b, star, mods = bases[i]
        nxt = bases[i + 1][0] if i + 1 < len(bases) else None
        v = None
        if (b, nxt) in PAIRS and not mods:
            v = PAIRS[(b, nxt)]; mods = bases[i + 1][2]; i += 1
        elif b in ('D1', 'Cl'):
            v = None
        elif b == 'D3' and last_d is not None:
            v = last_d
        elif b in ('D2', 'D3'):
            ref = [x for x in hist if x[1]]
            if ref:
                v = ref[-1][0]
            else:
                vv = [x for x in hist if x[2] in DOTTABLE]
                v = vv[-1][0] if vv else None
            last_d = v
        else:
            v = value(b)
        if v is None:
            out += '[?]'; unk += 1; vv_ = ''
        else:
            out += v; vv_ = v.replace('~', '')
        for m in mods:
            if m == '+^':
                out += 'm'
            elif m == '+_':
                out += 'n'
            elif m == '+"':
                out += vv_
        hist.append((vv_, star, b))
        i += 1
    return out, unk


def run():
    FILES = [('TRAIN f4r', 'tx2/f004r.txt'), ('TRAIN f4v', 'tx2/f004v.txt'), ('H1', 'tx2/f015r.txt'),
             ('H2', 'tx2/f159r.txt'), ('H3', 'tx2/f034r_p34.txt'), ('PENT', 'tx/PENTACLES.txt')]
    lines, counts = [], []
    for tag, f in FILES:
        nlet = nunk = 0
        lines.append('## %s %s' % (tag, f))
        for ln in open(K + f, encoding='utf-8'):
            if ln.startswith('#') or not ln.strip():
                continue
            lid, txt = ln.rstrip('\n').split('\t')
            dec = []
            for w in txt.split(' / '):
                sg = w.split()
                if not sg or sg == ['Fill']:
                    continue
                d, u = decode_word(sg)
                if sg[-1] == 'Eq':
                    d += '='
                dec.append(d); nunk += u
                nlet += len(re.sub('[^a-z]', '', d.replace('[?]', '')))
            lines.append('%s %s\t%s' % (tag, lid, ' '.join(dec)))
        counts.append('%s %s: decoded letters %d, signs with no value %d' % (tag, f, nlet, nunk))
    hk = hashlib.sha256(open(K + 'KEY_LEAF.tsv', 'rb').read()).hexdigest()
    open(K + 'DECODE_KEYLEAF.txt', 'w').write(
        '# PASS 2: ONE decode with KEY_LEAF.tsv (sha256 %s), scripts/decode_keyleaf.py. "=" joins a word broken at a line end;'
        ' [?] = no value; ~ = Latin suspension mark (not expanded).\n' % hk + '\n'.join(lines) + '\n')
    open(K + 'work/decode_keyleaf_counts.txt', 'w').write('\n'.join(counts) + '\n')
    print('\n'.join(counts))


if __name__ == '__main__':
    run()
