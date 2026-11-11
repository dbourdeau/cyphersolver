"""Parse the frozen 1813 numerals (plus the one correction after the freeze) and the 1814 groups; load the key.
Tokens keep their marks: alt = list of digit readings ({a|b}), mark = ° ◇ + ^ suffixes, unk = contains '?'.
Paths are relative to this file: ../ is this folder (beling/), ../../ the target folder (targets/poinsett1813/)."""
import csv, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
BEL = HERE.parent
TGT = BEL.parent
FROZEN = BEL / 'transcription' / 'numerals_1813_frozen.txt'
KEY = BEL / 'key' / 'we025_poinsett.tsv'
POST = BEL / 'key' / 'we025_postfreeze_corrections.tsv'


def load_key(full_table=None, post_freeze=True):
    """{number: element}. Default: the WE025 rows of this folder (key/we025_poinsett.tsv). full_table: our complete
    transcription of WE025 (we025_table.tsv, not in the repository), for the shuffled-key control."""
    src = full_table or KEY
    we = {int(r['number']): r['element'] for r in csv.DictReader(open(src, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)
          if r['element'] or full_table}
    if post_freeze:
        for r in csv.DictReader(open(POST, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            we[int(r['number'])] = r['corrected']
    return we


def tok(t):
    m = re.match(r'^\{([^}]*)\}(.*)$', t)
    if m:
        alts = m.group(1).split('|'); rest = m.group(2)
    else:
        mm = re.match(r'^([0-9?]+)(.*)$', t)
        if not mm: return None
        alts = [mm.group(1)]; rest = mm.group(2)
    return {'raw': t, 'alts': alts, 'mark': rest, 'unk': any('?' in a for a in alts)}


def load_1813(apply_corrections=True):
    lines = []
    for L in open(FROZEN, encoding='utf-8'):
        if L.startswith('#') or not L.strip(): continue
        label, rest = L.rstrip('\n').split(' ', 1)
        clear = re.findall(r'\[([^\]]{3,})\]', rest)
        body = re.sub(r'\[[^\]]{3,}\]', ' ', rest)
        toks = []
        for t in body.split():
            if t == '[X]': toks.append({'raw': '[X]', 'alts': [], 'mark': 'X', 'unk': True}); continue
            x = tok(t)
            if x: toks.append(x)
        lines.append({'label': label, 'clear': clear, 'toks': toks, 'rest': rest})
    if apply_corrections:   # transcription/corrections_after_freeze.txt item 1: P9.3 1160 -> 1106
        for l in lines:
            if l['label'] == 'P9.3':
                for t in l['toks']:
                    if t['alts'] == ['1160']: t['alts'] = ['1106']; t['raw'] = '1106'
    return lines


def load_1814():
    """Merged text from Daniel Bourdeau's ciphertext_1814.txt (RC with gutter ends from the Duplicate), plus the clerk's
    gloss per line from transcription_1814.tsv."""
    rows = []
    for L in open(TGT / 'transcription_1814.tsv', encoding='utf-8'):
        if L.startswith('#') or L.startswith('passage'): continue
        f = L.rstrip('\n').split('\t')
        rows.append({'label': f[0] + f[1], 'dup': f[2], 'rc': f[3], 'gloss': f[4]})
    ct = [l.split() for l in open(TGT / 'ciphertext_1814.txt', encoding='utf-8') if l.strip()]
    for r, c in zip(rows, ct): r['groups'] = c
    return rows


def load_daniel_1813():
    """Rows of Daniel Bourdeau's transcription.tsv for P1-P9 (P0 is not transcribed), in order."""
    rows = []
    for L in open(TGT / 'transcription.tsv', encoding='utf-8'):
        if L.startswith('#') or L.startswith('passage'): continue
        f = L.rstrip('\n').split('\t')
        if f[3] == 'ILLEGIBLE': continue
        rows.append({'passage': f[0], 'frame': f[1], 'line': f[2], 'groups': f[3].split(), 'context': f[4] if len(f) > 4 else ''})
    return rows
