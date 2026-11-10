"""Backfill outcome.credits for work done before 13 Oct 2026 (one-off; kept for the record).

  python tools/backfill_credits.py seeds <outdir>     write <outdir>/<folder>.seed.json: credits found mechanically
  python tools/backfill_credits.py apply <indir>      merge <indir>/<folder>.json drafts into the profiles

Seeds come from three structured sources: the key web (docs/keys.json: a scholar's or DECODE key linked to a page),
the page bylines (PAGES author= in docs/_build_site.py) and the pull requests and issues merged from GitHub
(PULLS below, read from `gh pr list` / `gh issue list` on 13 Oct 2026).  The drafts that 'apply' reads were made
from the seeds plus each target's NOTES.md, README row and profile prose, and checked by hand.

'apply' edits profile.json as text: it inserts "provenance" and "credits" before the closing brace of "outcome",
so the rest of each hand-formatted file is left as it is, and checks that the result parses to the intended object.
"""
import sys, re, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'docs'))
import _methods as M
import _credits as C

REPO = 'https://github.com/dbourdeau/cyphersolver'
# (number, kind, contributor id, folders, role, note)
PULLS = [
    (1, 'pull', 'arya', ['hesse1603'], 'solution', "the King's ciphered passages in Rommel 1840 read with Rommel's 1846 key"),
    (2, 'pull', 'arya', ['sormano1529'], 'solution', 'key verified, letters unread'),
    (3, 'pull', 'arya', ['herbault1626'], 'solution', 'decipherment found three folios away'),
    (4, 'pull', 'arya', ['lorraine1592'], 'solution', 'cipher broken, key recovered'),
    (7, 'pull', 'arya', ['maisse1592'], 'solution', 'published keys applied, f. 370 deciphered'),
    (8, 'pull', 'arya', ['sessa1593'], 'solution', "the office's own key found"),
    (9, 'pull', 'arya', ['nevers1589'], 'solution', 'no ciphertext there; eleven items resolved'),
    (10, 'pull', 'arya', ['poyntz1527'], 'solution', "read at the time, Tuke's decipherment in print"),
    (15, 'pull', 'setsunaatto', ['champagne1590'], 'verification', 'blind test of key no. 57 on no. 10'),
    (17, 'pull', 'beck', ['malsburg1637'], 'solution', 'alphabetic key recovered, critical reading'),
    (18, 'pull', 'beck', ['foix1563'], 'solution', 'proposed partial decipherment'),
    (27, 'pull', 'beck', ['foix1563'], 'verification', 'five-sign audit'),
    (20, 'pull', 'robinson', ['labbe1582'], 'solution', 'solution added'),
    (21, 'pull', 'feyseel', ['erving1807aug'], 'solution', 'Erving 10 Aug 1807 written up'),
    (22, 'pull', 'feyseel', ['aerssen1601', 'battier1686'], 'new cipher with solution', 'Nationaal Archief targets'),
    (24, 'pull', 'zarco', ['dinteville1592'], 'solution', 'deciphered, key rebuilt'),
    (25, 'pull', 'zarco', ['matignon1586'], 'solution', "f. 276 deciphered with Tomokiyo's key"),
    (29, 'pull', 'lccompany', ['michell1751'], 'solution', 'cabinet code of 1751 rebuilt and blind-tested on R1957'),
    (30, 'pull', 'lccompany', ['sp106r927'], 'verification', 'independent key and transcription comparison'),
    (31, 'pull', 'lccompany', ['r1892', 'r2242'], 'key corrected', 'sign-label splits, sign values, transcription corrections'),
    (32, 'issue', 'tunarob', ['nevers1593'], 'key corrected', 'key no. 60 corrections, partial reading of f. 88r'),
    (28, 'issue', 'yuanyi', ['desmarets1710'], 'pointer', "readable with Tomokiyo's published 1710 table"),
    (16, 'issue', 'noautopilot', ['mercy1648'], 'solution', 'a cryptanalytic reading, no prior decipherment located'),
    (14, 'issue', 'bean', [], 'transcription', 'Oswald telegram transcription corrected'),
    (13, 'issue', 'setsunaatto', [], 'solution', 'read in full with Tomokiyo no. 57'),
    (23, 'issue', 'wanglu', ['sunyatsen'], 'identification', 'Chinese-side candidate for the former contract, two emendations'),
]


def page_authors():
    s = (ROOT / 'docs' / '_manifest.py').read_text(encoding='utf-8')
    body = s.split('PAGES = [', 1)[1].split('\nIMAGES', 1)[0]
    out = {}
    for b in re.split(r'\n    dict\(slug=', body):
        a = re.search(r"author='([^']+)'", b)
        if a: out[b.split("'")[1]] = a.group(1)
    return out


def match_who(text, reg):
    """Registry ids named in a free-text 'by' field."""
    text = text or ''
    hits = []
    for cid, c in reg.items():
        if c['kind'] == 'project': continue
        names = [c['name']] + c.get('aliases', [])
        if any(re.search(r'(?<![\w])' + re.escape(n) + r'(?![\w])', text) for n in names if len(n) > 2):
            hits.append(cid)
    return hits


def slug_to_folders():
    paths = M.profile_paths()
    inv = {}
    for folder in paths:
        inv.setdefault(PROFILE_SLUG.get(folder, folder), []).append(folder)
    for slug, folders in M.PAGE_PROFILES.items(): inv[slug] = folders
    return inv
PROFILE_SLUG = {'bordeaux': 'bordeaux1653'}


def seeds():
    reg = C.registry()
    out = {}
    add = lambda folder, c: out.setdefault(folder, []).append(c)
    kw = json.loads((ROOT / 'docs' / 'keys.json').read_text(encoding='utf-8'))
    keys = {k['id']: k for k in kw['keys']}
    s2f = slug_to_folders()
    for l in kw['links']:
        k = keys.get(l['key'])
        if not k or k['kind'] == 'rebuilt here': continue
        who = match_who(k.get('by'), reg)
        if not who:
            who = ['contemporary'] if k['kind'] in ('contemporary key', 'archive key') else ['decode'] if k['kind'] == 'DECODE key record' else []
        for folder in s2f.get(l['target'], []):
            for w in who:
                add(folder, dict(who=w, role='key or decipherment used', note=re.sub(r'\s+', ' ', k['label'])[:120],
                                 _evidence=f"keys.json {k['id']} ({k['kind']}, by {k.get('by')!r}) -> {l['target']} ({l['how']})"))
    for slug, author in page_authors().items():
        who = match_who(author, reg)
        for folder in s2f.get(slug, []):
            for w in who: add(folder, dict(who=w, role='solution', _evidence=f'page byline {author!r} on {slug}.html'))
    for n, kind, who, folders, role, note in PULLS:
        url = f'{REPO}/{"pull" if kind == "pull" else "issues"}/{n}'
        for folder in folders:
            add(folder, dict(who=who, role=role, note=f'{"PR" if kind == "pull" else "issue"} #{n}: {note}', source=url,
                             _evidence=f'GitHub {kind} #{n}'))
    return out


# ---------------------------------------------------------------------------

def outcome_span(text):
    """(start, end) of the outcome object's braces in the raw JSON text."""
    m = re.search(r'"outcome"\s*:\s*\{', text)
    i = m.end() - 1
    depth, instr, esc = 0, False, False
    for j in range(i, len(text)):
        ch = text[j]
        if instr:
            if esc: esc = False
            elif ch == '\\': esc = True
            elif ch == '"': instr = False
            continue
        if ch == '"': instr = True
        elif ch == '{': depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0: return i, j
    raise ValueError('unbalanced outcome')


def insert(text, fields):
    """Add or replace top-level keys of outcome, keeping the rest of the file's formatting."""
    prof = json.loads(text)
    want = json.loads(text)
    for k, v in fields.items():
        want['outcome'].pop(k, None)
    for k, v in fields.items():
        if v is not None: want['outcome'][k] = v
    for k in fields:
        if k in prof['outcome']: raise ValueError(f'outcome.{k} already present; edit it by hand')
    a, b = outcome_span(text)
    inner = text[a + 1:b]
    ind = re.search(r'\n([ \t]+)"', inner)
    ind = ind.group(1) if ind else '  '
    close = re.search(r'\n([ \t]*)$', inner)
    add = ''
    for k, v in fields.items():
        if v is None: continue
        if isinstance(v, list):
            items = (',\n' + ind + '  ').join(json.dumps(x, ensure_ascii=False) for x in v)
            val = '[\n' + ind + '  ' + items + '\n' + ind + ']' if v else '[]'
        else:
            val = json.dumps(v, ensure_ascii=False)
        add += ',\n' + ind + json.dumps(k) + ': ' + val
    body = inner.rstrip()
    new = text[:a + 1] + body + add + ('\n' + close.group(1) if close else '\n') + text[b:]
    if json.loads(new) != want: raise ValueError('insert changed more than outcome credits')
    return new


def apply(indir):
    reg = C.registry()
    paths = M.profile_paths()
    n = 0
    for f in sorted(pathlib.Path(indir).glob('*.json')):
        if f.name.endswith('.seed.json'): continue
        folder = f.stem
        d = json.loads(f.read_text(encoding='utf-8'))
        credits = [{k: v for k, v in c.items() if not k.startswith('_')} for c in d.get('credits', [])]
        bad = [c['who'] for c in credits if c.get('who') not in reg]
        if bad: print(f'{folder}: unknown contributor(s) {bad}; skipped'); continue
        if folder not in paths: print(f'{folder}: no profile; skipped'); continue
        p = paths[folder]
        text = p.read_text(encoding='utf-8')
        prov = d.get('provenance')
        fields = {'provenance': prov if prov and prov != 'project' else None, 'credits': credits or None}
        new = insert(text, fields)
        if new != text:
            p.write_text(new, encoding='utf-8'); n += 1
    print(f'{n} profiles updated')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['seeds']:
        out = pathlib.Path(a[1]); out.mkdir(parents=True, exist_ok=True)
        s = seeds()
        for folder, cs in s.items(): (out / f'{folder}.seed.json').write_text(json.dumps(cs, ensure_ascii=False, indent=1), encoding='utf-8')
        print(f'{sum(map(len, s.values()))} seed credits for {len(s)} targets -> {out}')
    elif a[:1] == ['apply']:
        apply(a[1])
    else:
        print(__doc__)
