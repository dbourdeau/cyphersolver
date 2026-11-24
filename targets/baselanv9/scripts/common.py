"""Shared parsing for baselANV9: transcription files -> words of tokens; clear text -> words of letters."""
import re

BASES = ['Lmt', 'Oei', '5b', '6s', '6L', '6v', '6t', '6r', 'Am', 'Ab', 'Ar', 'As', 'Bl', 'Bx', 'Cd', 'Cl', 'Cs',
         'D1', 'D2', 'D3', 'Dh', 'Dl', 'Ds', 'Dv', 'Ea', 'Hk', 'Lb', 'Lm', 'Lr', 'Oc', 'Oe', 'Pe', 'Ph', 'Pl', 'Q3',
         'Rt', 'Tk', 'Xc', 'Yy', 'Sz', 'Ec', 'X', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?']
NOVALUE = {'Fill', 'Eq'}
# Modifiers kept as separate tokens: dot above (^), dot below (_), diaeresis ("). Marks that change the glyph's look
# (big loop @, bar ~, superscript m ^m) stay attached to the base and form a base token of their own.
SEP_MODS = {'^': '+^', '_': '+_', '"': '+"'}


def split_sign(sg):
    """'Tk^@' -> ['Tk@', '+^'];  'Oe^m' -> ['Oe^m'];  '6L_' -> ['6L', '+_'];  'X"' -> ['X', '+"']"""
    base = None
    for b in BASES:
        if sg.startswith(b):
            base = b
            break
    if base is None:
        return ['?']
    rest = sg[len(base):]
    attached, sep = '', []
    i = 0
    while i < len(rest):
        if rest.startswith('^m', i):
            attached += '^m'; i += 2
        elif rest[i] in '@~':
            attached += rest[i]; i += 1
        elif rest[i] == '"' and base == 'Oe':
            attached += '"'; i += 1          # dots above the oe-sign form a sign of their own (not a doubling)
        elif rest[i] in SEP_MODS:
            sep.append(SEP_MODS[rest[i]]); i += 1
        else:
            attached += rest[i]; i += 1
    return [base + attached] + sep


def read_tx(path):
    """Return list of (line_id, [word, ...]) with word = list of sign strings (Fill dropped, Eq kept as marker)."""
    out = []
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        lid, txt = ln.rstrip('\n').split('\t')
        words = []
        for w in txt.split(' / '):
            sg = [s for s in w.split() if s and s != 'Fill']
            if sg:
                words.append(sg)
        out.append((lid, words))
    return out


def words_with_joins(lines):
    """Flatten lines to a word list; a word ending in Eq is joined to the next word (line-end hyphen or a mid-line
    double bar, which is then dropped). Each word: dict(signs, tokens, line, eq_joined)."""
    flat = []
    for lid, words in lines:
        for w in words:
            flat.append((lid, w))
    res = []
    carry = None
    for lid, w in flat:
        sg = list(w)
        if carry is not None:
            sg = carry['signs'] + sg
            lid = carry['line'] + '+' + lid
            carry = None
        if sg and sg[-1] == 'Eq':
            sg = sg[:-1]
            if not sg:
                continue
            carry = {'signs': sg, 'line': lid}
            continue
        sg = [s for s in sg if s != 'Eq']
        if not sg:
            continue
        toks = []
        for s in sg:
            toks += split_sign(s)
        res.append({'signs': sg, 'tokens': toks, 'line': lid})
    if carry is not None:
        toks = []
        for s in carry['signs']:
            toks += split_sign(s)
        res.append({'signs': carry['signs'], 'tokens': toks, 'line': carry['line']})
    return res


def norm_latin(s):
    s = s.lower()
    s = s.replace('[', '').replace(']', '')
    s = s.replace('j', 'i').replace('v', 'u').replace('y', 'i').replace('k', 'c').replace('w', 'u')
    s = s.replace('æ', 'ae').replace('œ', 'oe')
    return re.sub('[^a-z]', '', s)


def read_clear(path):
    ws = []
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        for w in ln.split():
            n = norm_latin(w)
            if n:
                ws.append(n)
    return ws
