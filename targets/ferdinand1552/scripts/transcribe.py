"""Transcription of the glossed letters: machine labels (LM-corrected beam, work/beam_<letter>.tsv) plus the
corrections made by eye on the review strips (eye_<letter>.tsv).

    python scripts/transcribe.py 13oct      -> transcription_<letter>.txt and decryption_<letter>.txt

eye_<letter>.tsv, one line per corrected cipher line:  page.line <TAB> edits
  edits, space separated, sign indices as printed on the strips (0-based, before any edit):
    5=U        sign 5 is U
    5=-        sign 5 is not a sign (stroke, blot, clear-word fragment, gloss): dropped
    5=Ls,A     sign 5 is two signs (split by the segmenter wrongly merged)
    5+6=Th     signs 5 and 6 are one sign
    5<A        a sign A missed by the segmenter, before sign 5 ( 99<A appends at the end)
    5=x?       x, doubtful (kept, marked in the transcription with {?})
  A whole line typed by eye instead:  page.line <TAB> = lab lab lab ...
"""
import sys, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

key = {}
for l in open(ROOT / 'key.tsv', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    p = l.rstrip('\n').split('\t'); key[p[0]] = p[1]


def emit_letters(lab):
    if lab == '-': return []
    v = key.get(lab.rstrip('?'), '?')
    if v == 'null': return []
    if v.startswith('['): return [v]
    if v == '?': return ['?']
    return list(v)


def toks(s):
    s = '' if s == "''" else s
    s = s.replace('v', 'u').replace('V', 'U').replace('j', 'i').replace('J', 'I')
    return re.findall(r'\[[QH][0-9?]+\]|[a-z]', s.replace('[q', '[Q').replace('[h', '[H').lower().replace('[q', '[Q').replace('[h', '[H'))


def apply(labs, edits):
    if edits.startswith('='):
        return edits[1:].split()
    rep = {}; ins = {}; merge = {}
    for e in edits.split():
        m = re.match(r'^(\d+)\+(\d+)=(.+)$', e)
        if m:
            a, b = int(m.group(1)), int(m.group(2)); merge[a] = (b, m.group(3)); continue
        m = re.match(r'^(\d+)<(.+)$', e)
        if m:
            ins.setdefault(int(m.group(1)), []).extend(m.group(2).split(',')); continue
        m = re.match(r'^(\d+)=(.+)$', e)
        if m:
            rep[int(m.group(1))] = m.group(2); continue
        raise ValueError(f'bad edit {e!r}')
    out = []; skip = set()
    for i, l in enumerate(labs):
        out += ins.get(i, [])
        if i in skip: continue
        if i in merge:
            b, v = merge[i]; skip.update(range(i + 1, b + 1)); out.append(v); continue
        v = rep.get(i, l)
        if v == '-': continue
        out += v.split(',')
    out += ins.get(99, []) + ins.get(len(labs), [])
    return out


def load_lines(L):
    lines = {}
    for l in open(ROOT / f'work/beam_{L}.tsv', encoding='utf8'):
        f = l.rstrip('\n').split('\t')
        k = f'{f[0]}.{f[1]}'
        lines[k] = [f[0], int(f[1]), [int(x) for x in f[6].split()], f[3].split()]
    eye = ROOT / f'eye_{L}.tsv'
    if eye.exists():
        for l in open(eye, encoding='utf8'):
            if l.startswith('#') or not l.strip(): continue
            k, e = l.rstrip('\n').split('\t', 1)
            if k in lines:
                lines[k][3] = apply(lines[k][3], e.strip())
            else:
                p, j = k.split('.'); lines[k] = [p, int(j), [], e.strip()[1:].split()]
    reading = {}
    rf = ROOT / f'reading_{L}.txt'
    if rf.exists():
        for l in open(rf, encoding='utf8'):
            if l.startswith('#') or not l.strip(): continue
            k, t = l.rstrip('\n').split('\t'); reading[k] = t
    return {k: tuple(v) for k, v in lines.items()}, reading


def decrypt(labs):
    out = ''
    for l in labs:
        e = emit_letters(l)
        s = ''.join(e)
        out += f'({s})' if l.endswith('?') and s else s
    return out


if __name__ == '__main__':
    L = sys.argv[1]
    lines, reading = load_lines(L)
    order = list(lines)
    with open(ROOT / f'transcription_{L}.txt', 'w', encoding='utf8') as f, \
         open(ROOT / f'decryption_{L}.txt', 'w', encoding='utf8') as g:
        f.write(f'# Ferdinand I to Castaldo, letter of {L}: cipher signs line by line (names: sign_inventory.md).\n'
                f'# Machine labels (scripts/seg3.py, classify3.py, beam.py) corrected by eye on review strips (eye_{L}.tsv).\n'
                f'# x? = doubtful. Line ids: page.line as in cipher_lines.tsv.\n')
        g.write(f'# Decryption of transcription_{L}.txt with key.tsv; nulls dropped; (x) = doubtful sign.\n')
        for k in order:
            p, j, idx, labs = lines[k]; labs = [x for x in labs if x != '-']
            f.write(f'{k}\t{" ".join(labs)}\n'); g.write(f'{k}\t{decrypt(labs)}\n')
    print('wrote', len(order), 'lines')
