"""The key figure at the top of a write-up page, in the manner of George Lasry's reports.

Lasry's write-ups open with the key as a table: every plaintext letter with its cipher sign(s) under it, then the
nomenclator (codes for syllables, words and names), then the nulls. This module builds the same table from the key
file a target already keeps (profile outcome.key_file, else key.tsv / key.json / key.txt / key.md in the folder):

    key_figure_html(page, profiles, profile_paths) -> '<!-- keyfig:start --> ... <!-- keyfig:end -->' or ''

A key file that is an image (png/jpg/svg) is shown as is. Text keys are parsed loosely (TSV with or without header,
`sign - value`, `sign = value`, `sign: value`, JSON objects, Markdown tables); a file that yields fewer than
MIN_PAIRS sign/value pairs gives no figure rather than a wrong one. Pages carrying George Lasry's own report already
show his key at the top and get no second one. Called from _build_site.py on every build.
"""
import html, json, pathlib, re, shutil

MIN_PAIRS = 4
NOMEN_MAX = 96                      # nomenclator cells shown; the rest are counted and linked
VALUE_MAX = 28                      # a "value" longer than this is a note, not a value
SIGN_MAX = 40
IMG_EXT = {'.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp'}
REPO_BLOB = 'https://github.com/dbourdeau/cyphersolver/blob/main/'
HEAD_SIGN = re.compile(r'^(sign|cipher|code|token|group|symbol|glyph|ct|number|num|figure|chiffre|key)s?\b', re.I)
VALUE_COLS = ('value_reading', 'value', 'plain', 'plaintext', 'pt', 'meaning', 'reading', 'letter', 'clear')
NULL_WORDS = {'', 'null', 'nulle', 'nul', '(null)', '-', '—', 'nihil', 'nulla', 'null sign'}


def _clean(s):
    return re.sub(r'\s+', ' ', str(s)).strip().strip('`*').strip()


def _ok(sign, val):
    return sign and len(sign) <= SIGN_MAX and len(val) <= VALUE_MAX and not sign.startswith('#')


def parse_tsv(text):
    rows = [l.split('\t') for l in text.splitlines() if l.strip() and not l.lstrip().startswith('#')]
    rows = [r for r in rows if len(r) >= 2]
    if not rows: return []
    si, vi = 0, 1
    if HEAD_SIGN.match(rows[0][0].strip()) or any(c.strip().lower() in VALUE_COLS for c in rows[0]):
        head = [c.strip().lower() for c in rows[0]]
        for name in VALUE_COLS:
            if name in head: vi = head.index(name); break
        rows = rows[1:]
    return [(_clean(r[si]), _clean(r[vi]) if vi < len(r) else '') for r in rows]


def parse_lines(text):
    out = []
    for l in text.splitlines():
        if not l.strip() or l.lstrip()[:1] in '#<': continue
        m = re.match(r'^\s*(\S{1,16}?)\s*(?:\t| - | – | = |=|: |\|)\s*(.*?)\s*$', l)
        if m: out.append((_clean(m.group(1)), _clean(m.group(2))))
    return out


def parse_md(text):
    out, flip = [], False
    for l in text.splitlines():
        if not l.strip().startswith('|') or re.match(r'^\s*\|[\s:|-]+\|\s*$', l): continue
        cells = [_clean(c) for c in l.strip().strip('|').split('|')]
        if len(cells) < 2: continue
        if HEAD_SIGN.match(cells[0]): flip = False; continue
        if re.match(r'^(pt|plain|letter|value|meaning|clear|word|plaintext)\b', cells[0], re.I): flip = True; continue
        # side-by-side tables (code | word | code | word): every pair of columns is one entry
        step = 2 if len(cells) >= 4 and len(cells) % 2 == 0 else len(cells)
        for i in range(0, len(cells) - 1, step):
            a, b = cells[i], cells[i + 1]
            if a or b: out.append((b, a) if flip else (a, b))
    return out


def parse_json(text):
    d = json.loads(text)
    if isinstance(d, dict):
        for k in ('key', 'table', 'mapping', 'signs'):
            if isinstance(d.get(k), (dict, list)): d = d[k]; break
    if isinstance(d, dict):
        return [(_clean(k), _clean(v if not isinstance(v, list) else '/'.join(map(str, v)))) for k, v in d.items()
                if isinstance(v, (str, int, list))]
    if isinstance(d, list):
        out = []
        for e in d:
            if isinstance(e, dict):
                s = next((e[k] for k in e if HEAD_SIGN.match(k)), None)
                v = next((e[k] for k in VALUE_COLS if k in e), None)
                if s is not None and v is not None: out.append((_clean(s), _clean(v)))
        return out
    return []


def parse_key(path):
    try: text = path.read_text(encoding='utf-8', errors='replace')
    except OSError: return []
    ext = path.suffix.lower()
    try:
        if ext == '.json': pairs = parse_json(text)
        elif ext == '.md': pairs = parse_md(text) or parse_lines(text)
        elif ext == '.tsv' or (ext in ('.txt', '') and text.count('\t') >= MIN_PAIRS): pairs = parse_tsv(text)
        elif ext in ('.txt', ''): pairs = parse_lines(text)
        else: pairs = []
    except (ValueError, TypeError):
        return []
    # plaintext written first (value | sign): numbers or symbols on the right, words on the left
    if pairs:
        dig = lambda x: bool(re.search(r'\d', x))
        if sum(dig(v) and not dig(s) for s, v in pairs) > 0.6 * len(pairs): pairs = [(v, s) for s, v in pairs]
    pairs = [(s, v) for s, v in pairs if _ok(s, v)]
    seen, out = set(), []
    for p in pairs:
        if p not in seen: seen.add(p); out.append(p)
    return out if len(out) >= MIN_PAIRS else []


def key_sources(folder_dir, prof):
    o = (prof or {}).get('outcome') or {}
    kf = o.get('key_file')
    kf = [kf] if isinstance(kf, str) else list(kf or [])
    cands = [folder_dir / k for k in kf if not str(k).startswith('http')]
    cands += [folder_dir / n for n in ('key.tsv', 'key.json', 'key.txt', 'key.md', 'KEY.md', 'key_frozen.tsv')]
    seen, out = set(), []
    for c in cands:
        if c.is_file() and c not in seen: seen.add(c); out.append(c)
    return out


def _cell(sign, val, cls=''):
    return (f'<span class="kc{cls}"><b>{html.escape(val)}</b><i>{html.escape(sign)}</i></span>')


def sign_images(base, folder, docs_dir):
    """targets/<folder>/key_signs/<letter>.png: cut-outs from the manuscript, one per plaintext letter (& = et.png).
    Copied to docs/keyfig/<folder>/ and returned as {letter: src}."""
    d = base / 'key_signs'
    if not d.is_dir(): return {}
    out = {}
    for f in sorted(d.glob('*.png')) + sorted(d.glob('*.jpg')):
        dst = docs_dir / 'keyfig' / folder / f.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.is_file() or dst.stat().st_mtime < f.stat().st_mtime: shutil.copyfile(f, dst)
        out[{'et': '&'}.get(f.stem, f.stem.lower())] = f'keyfig/{folder}/{f.name}'
    return out


def table_html(pairs, imgs=None):
    imgs = imgs or {}
    alpha, nomen, nulls = {}, [], []
    for s, v in pairs:
        low = v.lower()
        if low in NULL_WORDS: nulls.append(s)
        elif re.fullmatch(r'[^\W\d_]', v): alpha.setdefault(low, []).append(s)
        elif v == '&' and '&' in imgs: alpha.setdefault('&', []).append(s)
        else: nomen.append((s, v))
    parts = []
    if alpha:
        for l in imgs:
            if l not in alpha and len(l) == 1: alpha[l] = []
        def signs(l):
            if l in imgs:
                return (f'<img src="{imgs[l]}" alt="{html.escape(l)}: ' + html.escape(', '.join(alpha[l]) or 'as written')
                        + ' (cut from the manuscript)" loading="lazy">')
            return ''.join(f'<i>{html.escape(s)}</i>' for s in alpha[l])
        cls = ' kimg' if imgs else ''
        cells = ''.join(f'<span class="kc"><b>{html.escape(l.upper() if len(l) == 1 else l)}</b>' + signs(l) + '</span>'
                        for l in sorted(alpha, key=lambda x: (x == '&', x)))
        parts.append(f'<div class="kgrp"><p class="kh">Alphabet</p><div class="kgrid{cls}">{cells}</div></div>')
    if nomen:
        more = len(nomen) - NOMEN_MAX
        cells = ''.join(_cell(s, v) for s, v in nomen[:NOMEN_MAX])
        tail = f'<p class="muted kmore">and {more} more in the key file</p>' if more > 0 else ''
        label = 'Syllables, words and names' if alpha else 'Code'
        parts.append(f'<div class="kgrp"><p class="kh">{label}</p><div class="kgrid kn">{cells}</div>{tail}</div>')
    if nulls:
        cells = ''.join(f'<span class="kc kz"><i>{html.escape(s)}</i></span>' for s in nulls)
        parts.append(f'<div class="kgrp"><p class="kh">Nulls and signs without a value</p><div class="kgrid">{cells}</div></div>')
    return '\n'.join(parts)


def key_figure_html(page, profiles, profile_paths, docs_dir, repo_root):
    if not page: return ''
    figs = []
    for f in page.get('folders') or []:
        base = profile_paths[f].parent if f in profile_paths else repo_root / 'targets' / f
        if (base / 'lasry' / 'report' / 'report.json').is_file(): return ''   # his own key is already at the top
        rel = base.resolve().relative_to(repo_root.resolve()).as_posix()
        for src in key_sources(base, profiles.get(f)):
            link = f'<a href="{REPO_BLOB}{rel}/{src.relative_to(base).as_posix()}">{html.escape(src.name)}</a>'
            if src.suffix.lower() in IMG_EXT:
                name = f'keyfig/{f}_{src.name}'
                dst = docs_dir / name
                dst.parent.mkdir(exist_ok=True)
                if not dst.is_file() or dst.stat().st_mtime < src.stat().st_mtime: shutil.copyfile(src, dst)
                figs.append(f'<img src="{name}" alt="The key of {html.escape(f)}" loading="lazy"><figcaption>The key ({link}).</figcaption>')
                break
            pairs = parse_key(src)
            if pairs:
                cap = (f'The key{" of " + html.escape(f) if len(page.get("folders") or []) > 1 else ""}: plaintext above, '
                       f'cipher sign(s) below. Signs are given as transcribed; from {link}, where its status and sources are recorded.')
                imgs = sign_images(base, f, docs_dir)
                if imgs:
                    cap = cap.replace('cipher sign(s) below. Signs are given as transcribed;',
                                      'cipher signs below, cut from the manuscript key where shown (sources in key_signs/README.md); the rest as transcribed,')
                figs.append(table_html(pairs, imgs) + f'\n<figcaption>{cap}</figcaption>')
                break
    if not figs: return ''
    return ('<!-- keyfig:start -->\n<section class="keyfig" aria-labelledby="key">\n<h2 id="key">The key</h2>\n'
            + '\n'.join(f'<figure class="keytable">{x}</figure>' for x in figs) + '\n</section>\n<!-- keyfig:end -->\n')
