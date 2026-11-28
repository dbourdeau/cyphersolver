"""Shared loaders for the frozen plan run (scripts/run_plan.py) of 25 Nov 2026 (AI-written, Claude Opus 5.5).

Copied on 27 Nov 2026 from the contributor's work folder (where the folder was named cehm1462). The one change: the
plan run's own inputs are read from plan/frozen_run/ (keys/ and transcription/) in this target folder, by the new name
INPUTS, where the work folder had them at keys/ and transcription/. Nothing else was changed.

Inputs outside this folder:
- REPO: a checkout of dbourdeau/cyphersolver (lexicon lang/lexicons/es.json.gz; targets/duron1911/siblings/syl.py,
  targets/mccarty1911/key.tsv, targets/mexico1911/key.tsv, targets/hernandez1911/key.tsv,
  targets/dallas1911/key_card_1557-1.tsv). Set the environment variable CYPHERSOLVER_REPO, default: the repository
  root three levels up when this folder sits at <repo>/targets/<name>/.
- ALLEN_JSON: Ashton Allen's decode-result.json, github.com/ashtonwallen/pancho-villa-telegram-decipherment at commit
  0dc067a460fc66a9e36eb6c796ab7a4ba86d4779. It is not copied into this folder (no licence is stated in his repository);
  download it and set ALLEN_JSON to its path.
"""
import gzip
import json
import os
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
INPUTS = HERE / 'plan' / 'frozen_run'
REPO = Path(os.environ.get('CYPHERSOLVER_REPO', HERE.parent.parent))
ALLEN_JSON = Path(os.environ.get('ALLEN_JSON', HERE / 'decode-result.json'))


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn' and c.isalpha())


def tokens(tid):
    """Settled transcription rows: (line, kind, value, doubt)."""
    out = []
    lines = (INPUTS / 'transcription' / f'{tid}_settled.tsv').read_text(encoding='utf-8').splitlines()[1:]
    for row in lines:
        line, pos, kind, value, doubt = (row.split('\t') + [''] * 5)[:5]
        out.append((line, kind, value, doubt))
    return out


def runs(tid):
    """Coded runs between clear words: list of dicts with groups, left and right clear anchors."""
    res, cur, left = [], [], None
    for line, kind, value, doubt in tokens(tid):
        if kind == 'clear':
            if cur:
                res.append({'groups': cur, 'left': left, 'right': value})
                cur = []
            left = value
        else:
            cur.append(value)
    if cur:
        res.append({'groups': cur, 'left': left, 'right': None})
    return res


# ---------------- keys ----------------

def grid_keys():
    keys = {}
    for row in (INPUTS / 'keys' / 'grids_1557-1.tsv').read_text(encoding='utf-8').splitlines():
        if row.startswith('#') or not row.strip():
            continue
        name, scan, rdig, letters, cdig = row.split('\t')
        k = keys.setdefault(name, {})
        for r in rdig.split(','):
            for c, letter in zip(cdig.split(), letters.split()):
                k[r + c] = letter
    out = {}
    for name, k in keys.items():
        out[f'K-{name}-RC'] = dict(k)
        out[f'K-{name}-CR'] = {g[1] + g[0]: v for g, v in k.items()}
    return out


def clave0_words():
    d = {}
    for row in (INPUTS / 'keys' / 'clave0_words.tsv').read_text(encoding='utf-8').splitlines():
        if row.startswith('#') or not row.strip():
            continue
        n, w = row.split('\t')
        d[n] = w
    return d


def alfabeto21():
    k1, k2 = {}, {}
    for row in (INPUTS / 'keys' / 'alfabeto_21.tsv').read_text(encoding='utf-8').splitlines():
        if row.startswith('#') or not row.strip():
            continue
        sign, a, b = row.split('\t')
        if not a.endswith('?'):
            k1[a.zfill(2)] = sign
        if not b.endswith('?'):
            k2[b.zfill(2)] = sign
    return k1, k2


def syl_keys():
    txt = (REPO / 'targets/duron1911/siblings/syl.py').read_text(encoding='utf-8')
    rows = re.search(r"rows='(\d+)'", txt).group(1)
    cols = re.search(r"cols='(\d+)'", txt).group(1)
    table = re.search(r"T='''(.*?)'''", txt, re.S).group(1).split('\n')
    rc, cr = {}, {}
    for r, line in zip(rows, table):
        for c, v in zip(cols, line.split()):
            rc[r + c] = v
            cr[c + r] = v
    return {'K-SYL-RC': rc, 'K-SYL-CR': cr}


def allen_key():
    d = json.loads(ALLEN_JSON.read_text(encoding='utf-8'))
    return {str(k).zfill(2): v.lower() for k, v in d['verified_key'].items()}


ALPHA30 = ['a', 'b', 'c', 'ch', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'o', 'p', 'q',
           'r', 'rr', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
COLS_X = [6, 3, 1, 9, 4, 2, 8, 5, 0, 7]
ROWS_X = {1: 0, 6: 0, 9: 0, 2: 1, 5: 1, 8: 1, 3: 2}


def allen_x():
    """K-ALLEN-X: the alphabet model formed from Allen's published values (see PLAN.md)."""
    k = {}
    for tens, row in ROWS_X.items():
        for pos, unit in enumerate(COLS_X):
            k[f'{tens}{unit}'] = ALPHA30[row * 10 + pos]
    return k


def ddn():
    plain2ciph = {}
    for row in (INPUTS / 'keys' / 'ddn_card.tsv').read_text(encoding='utf-8').splitlines():
        if row.startswith('#') or not row.strip():
            continue
        p, c = row.split('\t')
        plain2ciph[p.lower()] = c.lower()
    return plain2ciph


def letter_keys():
    """Letter cards for T6, as filed upstream."""
    out = {}
    # Clave G.A. (digraphic)
    lines = [l for l in (REPO / 'targets/mccarty1911/key.tsv').read_text(encoding='utf-8').splitlines()
             if l and not l.startswith('#')]
    cols = lines[0].split('\t')[1:]
    ga = {}
    for l in lines[1:]:
        f = l.split('\t')
        for r in f[0].split():
            for c, v in zip(cols, f[1:]):
                ga[(r + c).lower()] = v.lower()
    out['K-GA'] = ('di', ga)
    hm = {}
    for l in (REPO / 'targets/mexico1911/key.tsv').read_text(encoding='utf-8').splitlines()[1:]:
        if '\t' in l and not l.startswith('#'):
            c, p = l.split('\t')[:2]
            hm[c.lower()] = p.lower()
    out['K-HM'] = ('mono', hm)
    her = {}
    for l in (REPO / 'targets/hernandez1911/key.tsv').read_text(encoding='utf-8').splitlines()[1:]:
        if '\t' in l and not l.startswith('#'):
            a, b = l.split('\t')[:2]
            her[a.lower()] = b.lower()
            her[b.lower()] = a.lower()
    out['K-HER'] = ('swap', her)
    pk = {}
    for l in (REPO / 'targets/dallas1911/key_card_1557-1.tsv').read_text(encoding='utf-8').splitlines():
        if l.startswith('#') or l.startswith('bigram') or '\t' not in l:
            continue
        b, p = l.split('\t')[:2]
        pk[b.lower()] = p.lower()
    out['K-P'] = ('di', pk)
    d = ddn()
    out['K-DDN-dec'] = ('mono', {c: p for p, c in d.items()})
    out['K-DDN-enc'] = ('mono', dict(d))
    return out


# ---------------- language measure ----------------

NAMES = ['ornelas', 'avila', 'villa', 'juarez', 'chihuahua', 'gonzalez', 'garza', 'torreon', 'carranza', 'madero',
         'bonilla', 'luque', 'ojinaga', 'diaz']


def lexicon(minc=3):
    d = json.load(gzip.open(REPO / 'lang/lexicons/es.json.gz'))
    lex = {w.replace('ñ', 'n') for w, c in d.items() if c >= minc and len(w) >= 2}
    lex.update(NAMES)
    return lex


def coverage(text, lex, maxlen=20):
    """Share of letters covered by the best segmentation into lexicon words (>= 2 letters); '?' never covered."""
    t = text.replace('ñ', 'n')
    n = len(t)
    if n == 0:
        return 0.0, []
    best = [0] * (n + 1)
    back = [None] * (n + 1)
    for i in range(1, n + 1):
        best[i], back[i] = best[i - 1], None
        for j in range(max(0, i - maxlen), i - 1):
            w = t[j:i]
            if w in lex and best[j] + (i - j) > best[i]:
                best[i], back[i] = best[j] + (i - j), j
    seg, i = [], n
    while i > 0:
        if back[i] is None:
            seg.append(t[i - 1].upper())
            i -= 1
        else:
            seg.append(t[back[i]:i])
            i = back[i]
    return best[n] / n, list(reversed(seg))
