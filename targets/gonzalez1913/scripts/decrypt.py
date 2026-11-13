"""Mechanical decryption with key_frozen.tsv. usage: decrypt.py TRANSCRIPTION OUT [KEY_TSV]  (default key_frozen.tsv)
Each group is replaced by its value; a group with an unread figure ('1?') or a group not in the key
is written [NN] (unread or unidentified). Word codes are written in capitals."""
import sys, re
import os, pathlib
T = str(pathlib.Path(__file__).resolve().parent.parent)   # the target folder
B = T
def key(path=None):
    k = {}
    for ln in open(path or os.path.join(B, 'key_frozen.tsv'), encoding='utf8'):
        if ln.startswith('#') or ln.startswith('group'): continue
        g, v, s = ln.rstrip('\n').split('\t'); k[g] = v
    return k
def segs(path):
    out = []
    for ln in open(path, encoding='utf8'):
        if ln.startswith('#') or not ln.strip(): continue
        sid, rest = ln.rstrip('\n').split('\t'); parts = rest.split(' | ')
        out.append((sid, parts[0], parts[1].split('-'), parts[2] if len(parts) > 2 else ''))
    return out
def dec(groups, k):
    o = []
    for g in groups:
        if re.fullmatch(r'\d\d', g) and g in k:
            v = k[g]; o.append(v.upper() if len(v) > 2 else v)
        else: o.append('[' + g + ']')
    return o
if __name__ == '__main__':
    k = key(sys.argv[3] if len(sys.argv) > 3 else None); lines = []
    for sid, pre, gr, post in segs(sys.argv[1]):
        d = dec(gr, k); unk = sum(1 for x in d if x.startswith('['))
        lines.append(f'{sid}\t{"".join(d)}\t# {len(gr)} groups, {unk} unread/unidentified')
    open(sys.argv[2], 'w', encoding='utf8').write('# Mechanical decryption with ' + (sys.argv[3] if len(sys.argv) > 3 else 'key_frozen.tsv') + ' (scripts/decrypt.py); capitals = word codes; [NN] = unread or unidentified group\n' + '\n'.join(lines) + '\n')
    print('\n'.join(lines))
