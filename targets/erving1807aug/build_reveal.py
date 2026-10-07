"""Erving to Madison, 10 Aug 1807: the group list for measuring, and the "watch it decipher" passage for the site.

  python targets/erving1807aug/build_reveal.py

Writes groups.txt (one line per aligned run: ref, then its code groups, for docs/_check_profile.py --measure
--drop-first) and docs/reveal/erving1807aug.json (Godoy's counter-project, frame 0363 right page, 67 groups with the
clear words between them). Values come from aligned.txt; each one is checked against key_pinckney.tsv, and a value
the key does not list for that group, a conjecture (?) or a group with digits hidden in the binding (#) is marked
uncertain. X = no value.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent

def aligned():
    out = []
    for line in (HERE / 'aligned.txt').read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or '|' not in line: continue
        ref, rest = line.split('|', 1)
        for tok in rest.split():
            g, v = tok.split('=', 1)
            out.append((ref.strip(), g, v))
    return out

def key():
    k = {}
    for line in (HERE / 'key_pinckney.tsv').read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or not line.strip(): continue
        cols = line.split('\t')
        k[cols[0]] = {re.sub(r'\(.*?\)', '', v).strip().lower() for v in cols[1].split('/')} if len(cols) > 1 else set()
    return k

def norm(g):
    return re.sub(r'\(.*?\)|[{}^#]', '', g).strip()

TOKS = aligned()
KEY = key()

# 1. groups.txt
lines, cur, ref0 = [], [], None
for ref, g, v in TOKS:
    if ref != ref0 and cur: lines.append(f'{ref0} ' + ' '.join(cur)); cur = []
    ref0 = ref; cur.append(g)
lines.append(f'{ref0} ' + ' '.join(cur))
(HERE / 'groups.txt').write_text('# Erving 10 Aug 1807, code groups in order, one aligned run per line (from aligned.txt by build_reveal.py)\n'
                                 + '\n'.join(lines) + '\n', encoding='utf-8')

# 2. the reveal passage: frame 0363 right page, "The [f]irst part ... a [603]"
tr = next(l for l in (HERE / 'transcription.txt').read_text(encoding='utf-8').splitlines() if l.startswith('0363R.1'))
start, end = tr.index('- The [f]irst part'), tr.index('that it is scarcely to be')
span = tr[start + 2:end]
span = span.replace('(struck group)', ' ')
pieces = re.findall(r'\[[^\]]*\d[^\]]*\]|[^\[\]\s]*(?:\[[a-z]+\][^\[\]\s]*)+|\S+', span)
seq = [t for t in TOKS if t[0] in ('0363D', '0363E', '0363F', '0363G', '0363H', '0363I')]
i, tokens = 0, []
for p in pieces:
    if p.startswith('[') and re.search(r'\d', p):
        for g in re.split(r'\.(?![^()]*\))', p[1:-1].replace('{..}', 'X')):
            g = g.strip()
            if not g: continue
            ref, ag, v = seq[i]; i += 1
            a, b = norm(g), norm(ag)
            assert a == b or a.lstrip('.') in b or b.startswith('X') or b.endswith(a), (g, ag)
            base = re.sub(r'[\^#]', '', ag)
            if v == 'X' or b.startswith('X') and v == 'X':
                tokens.append({'g': base.replace('X', '?'), 'p': '?', 'cls': 'unk'}); continue
            vv = v.rstrip('?').lower()
            cls = ''
            if '?' in v or '#' in ag or vv not in KEY.get(base, set()): cls = 'unc'
            t = {'g': base.replace('X', '?'), 'p': v.rstrip('?')}
            if cls: t['cls'] = cls
            tokens.append(t)
    else:
        w = p.replace('[', '').replace(']', '').strip()
        if w: tokens.append({'g': '', 'p': w, 'cls': 'plain'})
assert i == len(seq), (i, len(seq))
data = {
    'slug': 'erving1807aug',
    'anchor': 'counter',
    'title': 'Godoy’s counter-project, frame 0363, right page',
    'caption': 'Erving to Madison, Madrid, 10 August 1807, No. 24 Duplicate: the passage on the separate peace with England '
               'and the "dernier resort", NARA RG 59, M31 reel 12, frame 0363. Clear words as Erving wrote them; '
               'letters lost in the binding restored in the clear text only.',
    'unit': 'code groups',
    'key_note': 'Values from the Pinckney code as rebuilt for this letter (key_pinckney.tsv, 414 entries), fitted against the '
                'decoded text in Founders Online 99-01-02-1993. Marked uncertain: groups whose first digits are hidden in the '
                'binding (restored from context), conjectures, and values the key gives differently. 767, 679 and 378 have no value.',
    'tokens': tokens,
}
out = ROOT / 'docs' / 'reveal' / 'erving1807aug.json'
out.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(f'groups.txt: {len(TOKS)} groups in {len(lines)} runs; reveal: {sum(1 for t in tokens if t["g"])} groups, '
      f'{sum(1 for t in tokens if t.get("cls") == "plain")} clear words, '
      f'{sum(1 for t in tokens if t.get("cls") == "unc")} uncertain, {sum(1 for t in tokens if t.get("cls") == "unk")} unread')
