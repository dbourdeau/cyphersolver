"""Build docs/key-evolution.html: how the cipher keys in the targets change from 1400 to 1950.

Called from _build_site.py before the pages are processed (like archives.html), so it gets the nav and footer; or
  python docs/_key_evolution_page.py           writes the page (and pg-key-evolution.css)
  python docs/_key_evolution_page.py --table   prints the per-period numbers only

Every number on the page is counted here from targets/*/profile.json (the `system` block and the documents' years and
countries) and docs/keys.json (the key web: targets that share one key are counted as one cipher system). Nothing is
typed in. A field that is "unknown" in a profile is left out of that measure, and each measure shows how many systems
it rests on. The page's rules are STYLE below, written to pg-key-evolution.css.
"""
import collections, html, json, pathlib, re, statistics, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
# --root DIR counts from another checkout (a worktree at origin/main), so a stale working tree does not date the numbers
ROOT = pathlib.Path(sys.argv[sys.argv.index('--root') + 1]).resolve() if '--root' in sys.argv else HERE
OUT = HERE / 'docs' / 'key-evolution.html'
CSS = HERE / 'docs' / 'pg-key-evolution.css'
C = collections.Counter
E = html.escape
START, END, STEP = 1400, 1950, 50
BINS = list(range(START, END, STEP))
MIN_N = 5            # a share resting on fewer known systems is drawn hollow and greyed in the table

FAMILIES = [('mono', 'Simple substitution', 'one sign for each letter'),
            ('homo', 'Homophonic alphabet', 'several signs for a letter, or signs for syllables, and no word list'),
            ('nomen', 'Nomenclator', 'an alphabet together with a list of signs for names and words'),
            ('code', 'Code', 'a list of groups for words and phrases; typed as a code in the profile and not as a nomenclator'),
            ('poly', 'Polyalphabetic, transposition, polygraphic', 'the letters are shifted by a changing key, reordered, or taken in groups')]
SIGNS = [('symbols', 'Invented signs', 'symbols, alone or with letters'),
         ('mixed', 'Digits with letters or signs', 'figures mixed with letters or symbols'),
         ('digits', 'Digits only', 'figures only'),
         ('letters', 'Letters', 'letters only')]
POWERS = [('France', ('France',)), ('Spain', ('Spain',)), ('England and Britain', ('England', 'Great Britain', 'United Kingdom')),
          ('Italian states', ('Italy', 'Milan', 'Florence', 'Siena', 'Mantua', 'Ferrara', 'Naples', 'Venice', 'Savoy', 'Genoa',
                              'Urbino', 'Modena', 'Lucca', 'Parma', 'Tuscany', 'Duchy of Milan', 'Kingdom of the Two Sicilies')),
          ('Papacy', ('Papal', 'Papacy', 'Vatican')),
          ('German lands and the Empire', ('Germany', 'Holy Roman Empire', 'Austria', 'Prussia', 'Saxony', 'Bavaria', 'Hesse',
                                           'Brandenburg', 'Palatinate')),
          ('Netherlands', ('Dutch Republic', 'Netherlands', 'The Netherlands', 'United Provinces', 'Batavian Republic', 'Kingdom of Holland')),
          ('United States', ('United States', 'Confederate States'))]


def d(x):
    return x if isinstance(x, dict) else {}


def family(s):
    t = set(s.get('types') or [])
    if 'not a cipher' in t:
        return None
    if t & {'polyalphabetic', 'transposition', 'polygraphic'}:
        return 'poly'
    if 'nomenclator' in t or (d(s.get('nomenclator')).get('present') is True and 'code' not in t):
        return 'nomen'
    if 'code' in t:
        return 'code'
    if t & {'homophonic', 'polyphonic', 'syllabic'}:
        return 'homo'
    if 'monoalphabetic' in t:
        return 'mono'
    return 'undet'


def signs(s):
    k = s.get('symbol_kind')
    return {'symbols': 'symbols', 'letters and symbols': 'symbols', 'letters': 'letters', 'digits': 'digits',
            'digits and symbols': 'mixed', 'digits and letters': 'mixed'}.get(k)


def flag(v):
    return v if isinstance(v, bool) else None


SKIPPED = []          # profiles typed "not a cipher": not counted


def load():
    """One row per cipher system: the targets joined by a shared key in the key web count once (the earliest)."""
    web = json.loads((ROOT / 'docs' / 'keys.json').read_text(encoding='utf-8'))
    parent = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for l in web['links']:
        if l['how'] in ('read unchanged', 'rebuilt from', 'partial'):
            parent[find('t:' + l['target'])] = find(l['key'])
    del SKIPPED[:]
    groups, n_targets = collections.defaultdict(list), 0
    for f in sorted((ROOT / 'targets').glob('*/profile.json')):
        try:
            p = json.loads(f.read_text(encoding='utf-8'))
        except ValueError:
            continue
        s = p.get('system') or {}
        fam = family(s)
        if fam is None:
            SKIPPED.append(p['target'])
            continue
        n_targets += 1
        years = [x['year'] for x in p['documents'] if isinstance(x.get('year'), int)]
        country = C(x.get('country') for x in p['documents']).most_common(1)[0][0]
        nom = d(s.get('nomenclator'))
        t = set(s.get('types') or [])
        syl = None if fam == 'undet' else ('syllabic' in t or 'syllables' in (nom.get('kinds') or []))
        order = s.get('key_order')
        wd = s.get('word_division')
        groups[find('t:' + p['target'])].append(dict(
            target=p['target'], title=p.get('title', ''), year=min(years) if years else None, country=country, fam=fam,
            signs=signs(s), summary=s.get('summary') if isinstance(s.get('summary'), str) else '',
            size=s['distinct_symbols'] if isinstance(s.get('distinct_symbols'), int) else None,
            entries=nom['entries'] if isinstance(nom.get('entries'), int) else None,
            homophones=flag(d(s.get('homophones')).get('used')), nulls=flag(d(s.get('nulls')).get('present')),
            marks=flag(d(s.get('diacritics')).get('used')), syllables=syl,
            disordered={'random': True, 'alphabetical': False, 'partly alphabetical': False}.get(order),
            wordbreaks={'kept': True, 'partial': True, 'none': False, 'separator symbol': False}.get(wd),
            method=d(p.get('outcome')).get('method', ''), page=(ROOT / 'docs' / (p['target'] + '.html')).exists()))
    rows = []
    for g in groups.values():
        g.sort(key=lambda r: (r['year'] is None, r['year'] or 0, r['target']))
        rows.append(g[0])
    return rows, n_targets


FEATURES = [('homophones', 'Homophones', 'more than one sign for a letter'),
            ('nulls', 'Nulls', 'signs that mean nothing'),
            ('syllables', 'Syllable signs', 'signs for syllables, in the alphabet or the list; a lower bound'),
            ('marks', 'Marks on the signs', 'dots, strokes or bars that change a sign’s value'),
            ('disordered', 'Disordered key', 'values in no alphabetical order; a partly alphabetical key counts as ordered'),
            ('wordbreaks', 'Word breaks kept', 'the gaps between words survive, wholly or in part; a separator sign does not count')]


def tabulate(rows):
    T = {}
    for b in BINS:
        rs = [r for r in rows if r['year'] is not None and b <= r['year'] < b + STEP]
        det = [r for r in rs if r['fam'] != 'undet']
        row = dict(n=len(rs), det=len(det), fam=C(r['fam'] for r in det), signs=C(r['signs'] for r in rs if r['signs']))
        row['signs_n'] = sum(row['signs'].values())
        for k, _, _ in FEATURES:
            known = [r[k] for r in rs if r[k] is not None]
            row[k] = (sum(known), len(known))
        for k in ('size', 'entries'):
            v = sorted(r[k] for r in rs if r[k])
            row[k] = (v[len(v) // 4], statistics.median(v), v[min(len(v) - 1, (3 * len(v)) // 4)], len(v)) if v else None
        T[b] = row
    return T


def pct(a, n):
    return round(100 * a / n) if n else None


def label(b):
    return f'{b}–{str(b + STEP - 1)[2:]}'


# ---- charts: inline SVG on the site's .vchart classes (style.css; slots s1 to s5 are the validated series colours) ----
W, PL, PR = 760, 44, 10
BW = (W - PL - PR) / len(BINS)
SIGN_ORDER = ['symbols', 'mixed', 'digits', 'letters', None]
SIGN_CLASS = {'symbols': 'k-sym', 'mixed': 'k-mix', 'digits': 'k-dig', 'letters': 'k-let', None: 'k-unk'}
SIGN_NAME = {k: nm for k, nm, _ in SIGNS}
FAM_NAME = {k: nm for k, nm, _ in FAMILIES}
UNIT, TILE = 5, 5.2                      # the dot timelines: one tile per system, in columns of UNIT years
UX0, UX1 = 8, W - 8
USTEP = (UX1 - UX0) / ((END - START) / UNIT)


def tip(text):
    return f' data-tip="{E(text, quote=True)}"'


def power_of(r):
    for name, keys in POWERS:
        if isinstance(r['country'], str) and r['country'].startswith(keys):
            return name
    return 'Elsewhere'


def xmid(i):
    return PL + BW * (i + .5)


def unit_tip(r):
    bits = [FAM_NAME.get(r['fam'], 'kind not determined'), SIGN_NAME.get(r['signs'], 'signs not recorded').lower()]
    return f'{r["year"]} · {short(r)}\n{bits[0]}, {bits[1]}'


def short(r, n=64):
    t = r['title'] or r['target']
    for sep in (': ', '; '):
        if sep in t and len(t.split(sep)[0]) > 18:
            t = t.split(sep)[0]
    if len(t.split(' (')[0]) > 30:
        t = t.split(' (')[0]
    return t if len(t) <= n else t[:n - 1].rsplit(' ', 1)[0] + '\u2026'


def num(v):
    """A median: whole when it is whole, one decimal when it falls between two values."""
    return f'{v:,.0f}' if float(v).is_integer() else f'{v:,.1f}'


def columns(rs):
    """Systems grouped into UNIT-year columns, each sorted by sign kind so the colours band."""
    cols = collections.defaultdict(list)
    for r in rs:
        cols[(r['year'] - START) // UNIT].append(r)
    for c in cols.values():
        c.sort(key=lambda r: (SIGN_ORDER.index(r['signs']), r['year'], r['target']))
    return cols


def century_axis(y0, y1, ylab):
    out = []
    for c in range(START, END + 1, 100):
        x = UX0 + (c - START) / UNIT * USTEP
        out.append(f'<line class="grid" x1="{x:.1f}" x2="{x:.1f}" y1="{y0}" y2="{y1}"/>'
                   f'<text x="{x + 4:.1f}" y="{ylab}">{c}</text>')
    return ''.join(out)


def tile(r, x, y):
    return (f'<rect class="u {SIGN_CLASS[r["signs"]]}" x="{x:.1f}" y="{y:.1f}" width="{TILE}" height="{TILE}" rx="1.4"'
            f'{tip(unit_tip(r))}/>')


def hero_strip(dated):
    cols = columns(dated)
    tall = max(len(c) for c in cols.values())
    top, base = 8, 8 + tall * USTEP
    ranges = []
    for j, (k, nm, _) in enumerate(SIGNS):
        ys = sorted(r['year'] for r in dated if r['signs'] == k)
        if len(ys) < 8:
            continue
        q1, md, q3 = ys[len(ys) // 4], ys[len(ys) // 2], ys[(3 * len(ys)) // 4]
        X = lambda y: UX0 + (y - START) / UNIT * USTEP
        y = base + 52 + len(ranges) * 17
        right = X(q3) < W * .62
        ranges.append(f'<g{tip(f"{nm}\nhalf of these systems fall between {q1} and {q3}; median {md}; {len(ys)} systems")}>'
                      f'<rect class="hit" x="{UX0}" y="{y - 8}" width="{UX1 - UX0}" height="16"/>'
                      f'<rect class="kq {SIGN_CLASS[k]}" x="{X(q1):.1f}" y="{y - 1.75}" width="{max(X(q3) - X(q1), 4):.1f}" height="3.5" rx="1.75"/>'
                      f'<circle class="kq {SIGN_CLASS[k]}" cx="{X(md):.1f}" cy="{y}" r="4.2"/>'
                      f'<text class="kqt" x="{(X(q3) + 9) if right else (X(q1) - 9):.1f}" y="{y + 3.5}" text-anchor="{"start" if right else "end"}">'
                      f'{E(nm)} <tspan class="kqy">{q1}–{q3}</tspan></text></g>')
    H = base + 22 + (34 + len(ranges) * 17 if ranges else 0)
    out = [f'<svg class="vchart kunits" viewBox="0 0 {W} {H:.0f}" role="img" aria-label="Every cipher system counted, one square each, placed at its year and coloured by what its ciphertext is written in">',
           century_axis(top, base, f'{base + 16:.0f}'), f'<line class="axis" x1="{UX0}" x2="{UX1}" y1="{base + 1:.1f}" y2="{base + 1:.1f}"/>']
    for i, c in sorted(cols.items()):
        for j, r in enumerate(c):
            out.append(tile(r, UX0 + i * USTEP + (USTEP - TILE) / 2, base - (j + 1) * USTEP + (USTEP - TILE) / 2))
    if ranges:
        out.append(f'<text class="kqh" x="{UX0}" y="{base + 36:.0f}">WHERE THE MIDDLE HALF OF EACH FALLS</text>' + ''.join(ranges))
    out.append('</svg>')
    return ''.join(out)


def sign_legend(extra='', unknown=True):
    return ('<ul class="klegend">' + ''.join(f'<li class="kf" data-k="{SIGN_CLASS[k]}" role="button" tabindex="0"><i class="sw {SIGN_CLASS[k]}"></i><b>{E(nm)}</b></li>' for k, nm, _ in SIGNS)
            + ('<li class="kf" data-k="k-unk" role="button" tabindex="0"><i class="sw k-unk"></i><b>Not recorded</b></li>' if unknown else '') + extra + '</ul>')


def lanes(dated):
    names = [n for n, _ in POWERS] + ['Elsewhere']
    by = collections.defaultdict(list)
    for r in dated:
        by[r['power']].append(r)
    y, out = 18, []
    for name in names:
        rs = by.get(name)
        if not rs:
            continue
        cols = columns(rs)
        tall = max(len(c) for c in cols.values())
        h = max(tall * USTEP + 10, 26)
        ys = sorted(r['year'] for r in rs)
        out.append(f'<rect class="lane" x="0" y="{y:.1f}" width="{W}" height="{h + 20:.1f}" rx="8"/>'
                   f'<text class="lname" x="{UX0 + 4}" y="{y + 14:.1f}">{E(name)}</text>'
                   f'<text class="lmeta" x="{UX1 - 4}" y="{y + 14:.1f}" text-anchor="end">{len(rs)} systems · {ys[0]}–{ys[-1]}</text>')
        mid = y + 20 + h / 2
        for i, c in sorted(cols.items()):
            for j, r in enumerate(c):
                out.append(tile(r, UX0 + i * USTEP + (USTEP - TILE) / 2, mid + (j - len(c) / 2) * USTEP + (USTEP - TILE) / 2))
        y += h + 20 + 8
    H = y + 18
    grid = century_axis(4, y - 4, f'{y + 12:.0f}')
    return (f'<svg class="vchart kunits klanes" viewBox="0 0 {W} {H:.0f}" role="img" aria-label="The cipher systems of each power, one square each, by year, coloured by what the ciphertext is written in">'
            + ''.join(o for o in out if o.startswith('<rect class="lane"')) + grid + ''.join(o for o in out if not o.startswith('<rect class="lane"')) + '</svg>')


def stacked(T, cats, field, nfield, name, classes=None):
    H, top, base = 300, 12, 258
    out = [f'<svg class="vchart kstack" viewBox="0 0 {W} {H}" role="img" aria-label="{E(name)}">']
    for g in (0, 25, 50, 75, 100):
        y = base - (base - top) * g / 100
        out.append(f'<line class="{"axis" if g == 0 else "grid"}" x1="{PL}" x2="{W - PR}" y1="{y:.1f}" y2="{y:.1f}"/>'
                   f'<text x="{PL - 8}" y="{y + 4:.1f}" text-anchor="end">{g}%</text>')
    for i, b in enumerate(BINS):
        n = T[b][nfield]
        x, w = PL + BW * i + 6, BW - 12
        out.append(f'<text x="{xmid(i):.1f}" y="{base + 18}" text-anchor="middle" class="lab">{label(b)}</text>'
                   f'<text x="{xmid(i):.1f}" y="{base + 33}" text-anchor="middle" class="nn">{n} systems</text>')
        if not n:
            continue
        y, col = base, []
        for j, (k, nm, _) in enumerate(cats):
            v = T[b][field][k]
            if not v:
                continue
            h = (base - top) * v / n
            cls = classes[k] if classes else f's{j + 1}'
            col.append(f'<rect class="seg {cls}" x="{x:.1f}" y="{y - h + 1:.1f}" width="{w:.1f}" height="{max(h - 2, 1.5):.1f}" rx="3"'
                       f'{tip(f"{label(b)} · {nm}\n{v} of {n} systems ({pct(v, n)}%)")}/>')
            y -= h
        out.append(f'<g class="col{" thin" if n < 25 else ""}">{"".join(col)}</g>')
    out.append('</svg>')
    legend = ''.join(f'<li class="kf" data-k="{classes[k] if classes else f"s{j + 1}"}" role="button" tabindex="0"><i class="sw {classes[k] if classes else f"s{j + 1}"}"></i><b>{E(nm)}</b> <span>{E(gloss)}</span></li>'
                     for j, (k, nm, gloss) in enumerate(cats))
    if classes:
        return sign_legend(unknown=False) + f'<div class="vfig">{"".join(out)}</div>'
    return f'<ul class="klegend wide">{legend}</ul><div class="vfig">{"".join(out)}</div>'


def rows_chart(T, cats, field, nfield, unit):
    vw, top, full = 572, 18, 112            # full = height of a 100% bar; every row uses it, rows are only as tall as their peak
    bw = vw / len(BINS)
    rows = []
    for k, nm, gloss in cats:
        vals = [(T[b][field][k], T[b][nfield]) for b in BINS]
        shares = [a / n if n else 0 for a, n in vals]
        peak = max(range(len(BINS)), key=lambda i: shares[i])
        vh = top + max(round(full * shares[peak]), 10) + 1
        s = [f'<svg class="vchart krowsvg" viewBox="0 0 {vw} {vh}" role="img" aria-label="{E(nm)}: share by half-century">',
             f'<line class="axis" x1="0" x2="{vw}" y1="{vh - .5}" y2="{vh - .5}"/>']
        for i, b in enumerate(BINS):
            a, n = vals[i]
            h = max(full * shares[i], 1.2 if a else 0)
            x = i * bw + 5
            s.append(f'<rect class="hit" x="{i * bw:.1f}" y="0" width="{bw:.1f}" height="{vh}"{tip(f"{label(b)} \u00b7 {nm}\n{a} of {n} {unit} ({pct(a, n) or 0}%)")}/>')
            if a:
                s.append(f'<rect class="rb{" pk" if i == peak else ""}{" thin" if n < 25 else ""}" x="{x:.1f}" y="{vh - h:.1f}" width="{bw - 10:.1f}" height="{h:.1f}" rx="2.5" pointer-events="none"/>')
            if i == peak or (a and i in (0, len(BINS) - 1)):
                s.append(f'<text class="rv{" pk" if i == peak else ""}" x="{i * bw + bw / 2:.1f}" y="{vh - h - 4:.1f}" text-anchor="middle">{pct(a, n)}%</text>')
        s.append('</svg>')
        rows.append(f'<div class="krow"><div class="kl"><b>{E(nm)}</b><span>{E(gloss)}</span></div>{"".join(s)}</div>')
    ax = [f'<svg class="vchart krowsvg" viewBox="0 0 {vw} 30" aria-hidden="true">']
    for i, b in enumerate(BINS):
        ax.append(f'<text class="lab" x="{i * bw + bw / 2:.1f}" y="12" text-anchor="middle">{b}</text>'
                  f'<text class="nn" x="{i * bw + bw / 2:.1f}" y="25" text-anchor="middle">{T[b][nfield]}</text>')
    ax.append('</svg>')
    rows.append(f'<div class="krow kaxis"><div class="kl"><span>half-century from<br>{unit} counted</span></div>{"".join(ax)}</div>')
    return '<div class="krows">' + ''.join(rows) + '</div>'


def multiples(T):
    pw, ph, ml, mt = 250, 132, 8, 14
    panels = []
    for k, nm, gloss in FEATURES:
        x0, x1, y0, y1 = ml, pw - 34, ph - 22, mt
        s = [f'<svg class="vchart" viewBox="0 0 {pw} {ph}" role="img" aria-label="{E(nm)}: share of systems by half-century">']
        for g in (0, 50, 100):
            y = y0 - (y0 - y1) * g / 100
            s.append(f'<line class="{"axis" if g == 0 else "grid"}" x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}"/>')
        pts = []
        for i, b in enumerate(BINS):
            a, n = T[b][k]
            if n:
                pts.append((x0 + (x1 - x0) * (i + .5) / len(BINS), y0 - (y0 - y1) * a / n, b, a, n))
        solid = [p for p in pts if p[4] >= MIN_N]
        if len(solid) > 1:
            line = ' L'.join(f'{x:.1f} {y:.1f}' for x, y, *_ in solid)
            s.append(f'<path class="karea" d="M{solid[0][0]:.1f} {y0} L{line} L{solid[-1][0]:.1f} {y0} Z"/><path class="line s1" d="M{line}"/>')
        for x, y, b, a, n in pts:
            s.append(f'<g class="pt"><circle class="hit" cx="{x:.1f}" cy="{y:.1f}" r="10"{tip(f"{label(b)} · {nm}\n{a} of {n} systems where it is recorded ({pct(a, n)}%)")}/>'
                     f'<circle class="s1{"" if n >= MIN_N else " hollow"}" cx="{x:.1f}" cy="{y:.1f}" r="3.2"/></g>')
        if solid:
            x, y, b, a, n = solid[-1]
            s.append(f'<text class="endv" x="{x + 8:.1f}" y="{y + 4:.1f}">{pct(a, n)}%</text>')
        for i in (0, 4, 8):
            s.append(f'<text x="{x0 + (x1 - x0) * (i + .5) / len(BINS):.1f}" y="{ph - 6}" text-anchor="middle">{BINS[i]}</text>')
        s.append('</svg>')
        peak = max(solid, key=lambda p: p[3] / p[4]) if solid else None
        head = (f'<b class="big">{pct(peak[3], peak[4])}%</b><span>at its height, {label(peak[2])}</span>' if peak else '')
        known, total = sum(T[b][k][1] for b in BINS), sum(T[b]['n'] for b in BINS)
        if peak:
            s.insert(-1, f'<circle class="pkdot" cx="{peak[0]:.1f}" cy="{peak[1]:.1f}" r="4.6" pointer-events="none"/>')
        panels.append(f'<figure class="kpanel"><h3>{E(nm)}</h3><p class="gloss">{E(gloss)}</p><p class="peak">{head}</p>{"".join(s)}'
                      f'<p class="kn"><i style="--w:{pct(known, total)}%"></i>recorded for {known} of {total} systems</p></figure>')
    return '<div class="kgrid">' + ''.join(panels) + '</div>'


def sizes(T):
    import math
    H, top, base = 290, 14, 246
    lo, hi = math.log10(10), math.log10(2000)

    def Y(v):
        return base - (base - top) * (math.log10(min(max(v, 10), 2000)) - lo) / (hi - lo)
    cut = PL + BW * BINS.index(1850)
    out = [f'<svg class="vchart ksize" viewBox="0 0 {W} {H}" role="img" aria-label="Distinct signs or groups per cipher system, median and middle half, by half-century">',
           f'<rect class="dim" x="{cut:.1f}" y="{top}" width="{W - PR - cut:.1f}" height="{base - top}" rx="6"/>',
           f'<text class="dimlab" x="{cut + 10:.1f}" y="{top + 18}">from 1850 the count is often</text><text class="dimlab" x="{cut + 10:.1f}" y="{top + 32}">the alphabet, not the code</text>']
    for g in (10, 30, 100, 300, 1000):
        out.append(f'<line class="{"axis" if g == 10 else "grid"}" x1="{PL}" x2="{W - PR}" y1="{Y(g):.1f}" y2="{Y(g):.1f}"/>'
                   f'<text x="{PL - 8}" y="{Y(g) + 4:.1f}" text-anchor="end">{g:,}</text>')
    path = []
    for i, b in enumerate(BINS):
        out.append(f'<text x="{xmid(i):.1f}" y="{base + 18}" text-anchor="middle" class="lab">{label(b)}</text>')
        if not T[b]['size']:
            continue
        q1, med, q3, n = T[b]['size']
        late = b >= 1850
        if not late:
            path.append(f'{xmid(i):.1f} {Y(med):.1f}')
        out.append(f'<text x="{xmid(i):.1f}" y="{base + 33}" text-anchor="middle" class="nn">{n} systems</text>'
                   f'<g class="pt"><rect class="iqr" x="{xmid(i) - 11:.1f}" y="{Y(q3):.1f}" width="22" height="{max(Y(q1) - Y(q3), 3):.1f}" rx="5"'
                   f'{tip(f"{label(b)}\nmedian {num(med)} signs or groups\nmiddle half {q1:,} to {q3:,} · {n} systems")}/>'
                   f'<circle class="s1{" hollow" if late or n < MIN_N else ""}" cx="{xmid(i):.1f}" cy="{Y(med):.1f}" r="5.5" pointer-events="none"/>'
                   f'<text class="medv" x="{xmid(i):.1f}" y="{Y(q3) - 8:.1f}" text-anchor="middle">{num(med)}</text></g>')
    out.insert(3, f'<path class="line s1 trend" d="M{" L".join(path)}"/>')
    out.append('</svg>')
    return f'<div class="vfig">{"".join(out)}</div>'


def cell(a, n):
    if not n:
        return '<td class="na">–</td>'
    p = pct(a, n)
    return f'<td{" class=\"thin\"" if n < MIN_N else ""} style="--h:{p}"{tip(f"{a} of {n} systems")}>{p}%</td>'


def data_table(T):
    head = ('<tr><th>Period</th><th>Systems</th>' + ''.join(f'<th>{E(nm)}</th>' for _, nm, _ in FAMILIES) + '<th>Digits only</th>'
            + ''.join(f'<th>{E(nm)}</th>' for _, nm, _ in FEATURES) + '<th>Median size</th><th>Median list</th></tr>')
    body = []
    for b in BINS:
        r = T[b]
        body.append(f'<tr><th>{label(b)}</th><td>{r["n"]}</td>' + ''.join(cell(r['fam'][k], r['det']) for k, _, _ in FAMILIES)
                    + cell(r['signs']['digits'], r['signs_n']) + ''.join(cell(*r[k]) for k, _, _ in FEATURES)
                    + (f'<td>{num(r["size"][1])}<small> /{r["size"][3]}</small></td>' if r['size'] else '<td class="na">–</td>')
                    + (f'<td>{num(r["entries"][1])}<small> /{r["entries"][3]}</small></td>' if r['entries'] else '<td class="na">–</td>') + '</tr>')
    return f'<div class="vfig"><table class="ktable heat"><thead>{head}</thead><tbody>{"".join(body)}</tbody></table></div>'


def powers_table(dated):
    out = []
    for name, _ in POWERS:
        rs = [r for r in dated if r['power'] == name]
        if not rs:
            continue
        ys = sorted(r['year'] for r in rs)
        dig = sorted((r['year'], r['target']) for r in rs if r['signs'] == 'digits')
        last_sym = sorted((r['year'], r['target']) for r in rs if r['signs'] == 'symbols')
        code = sorted((r['year'], r['target']) for r in rs if r['fam'] == 'code')
        big = max((r for r in rs if r['size']), key=lambda r: r['size'], default=None)
        f = lambda v: f'{v[0]} <small>{E(v[1])}</small>' if v else '–'
        out.append(f'<tr><th>{E(name)}</th><td>{len(rs)}</td><td>{ys[0]}–{ys[-1]}</td><td>{f(dig[0] if dig else None)}</td>'
                   f'<td>{f(last_sym[-1] if last_sym else None)}</td><td>{f(code[0] if code else None)}</td>'
                   f'<td>{f"{big["size"]:,} <small>{E(big["target"])}, {big["year"]}</small>" if big else "–"}</td></tr>')
    return ('<div class="vfig"><table class="ktable left"><thead><tr><th>Power</th><th>Systems</th><th>Years</th><th>First digits-only cipher</th>'
            '<th>Last cipher in invented signs</th><th>First code</th><th>Largest key</th></tr></thead><tbody>' + ''.join(out) + '</tbody></table></div>')


def credit_of(r):
    """The credit the write-up gives the picture whose thumbnail is used, or None (then the card is not used)."""
    page = ROOT / 'docs' / (r['target'] + '.html')
    if not r.get('thumb') or not page.exists():
        return None
    base = re.sub(r'-480\.webp$', '', r['thumb'])
    m = re.search(r'<figure[^>]*data-credit="([^"]+)"[^>]*>\s*<img src="' + re.escape(base) + r'\.', page.read_text(encoding='utf-8'))
    return m.group(1) if m else None


def era(dated, lo, hi, k=3):
    """An era block: what the counts say in one line, and up to k systems with a page (and a picture) on the site."""
    rs = [r for r in dated if lo <= r['year'] < hi]
    det = [r for r in rs if r['fam'] != 'undet']
    def tops(counter):
        best = counter.most_common(1)[0][1]
        return [k for k, v in counter.most_common() if v == best], best
    fams, fn = tops(C(r['fam'] for r in det))
    sgs, sn = tops(C(r['signs'] for r in rs if r['signs']))
    sn_all = sum(1 for r in rs if r['signs'])
    pws, tn = tops(C(r['power'] for r in rs if r['power'] != 'Elsewhere'))
    the = lambda t: t if t.startswith(('France', 'Spain', 'England')) else 'the ' + t
    name = ' and '.join(f'{tn} from {the(t)}' for t in pws)
    WORDS = {'nomen': ('nomenclator',), 'code': ('code',), 'homo': ('homophon',), 'mono': ('simple substitution', 'monoalphabetic', 'one sign'),
             'poly': ('transposition', 'polyalphabetic', 'vigen', 'columnar')}
    says = lambda r: any(w in r['summary'].lower() for w in WORDS[r['fam']]) and not (r['fam'] != 'code' and 'code' in r['summary'].lower()[:60] and r['fam'] == 'nomen')
    cand = sorted((r for r in rs if r['page'] and r['thumb'] and r['fam'] != 'undet' and 40 < len(r['summary']) < 300 and says(r) and credit_of(r)),
                  key=lambda r: (r['year'], r['target']))
    seen, pick = set(), []
    for r in cand:                                    # one per kind of system first, then spread across the years
        if r['fam'] not in seen and len(pick) < k:
            seen.add(r['fam'])
            pick.append(r)
    for r in cand[len(cand) // 2:] + cand:
        if len(pick) < k and r not in pick:
            pick.append(r)
    pick.sort(key=lambda r: r['year'])
    cards = ''.join(
        f'<a class="card hasthumb" href="{E(r["target"])}.html"><img class="thumb" src="thumbs/{E(r["thumb"])}" alt="" loading="lazy">'
        f'<div class="eyebrow"><span>{E(FAM_NAME[r["fam"]])}</span><span class="when">{r["year"]}</span></div>'
        f'<h3>{E(short(r, 58))}</h3><p>{E(r["summary"])}</p><span class="go">Write-up &rarr;</span></a>' for r in pick)
    return (f'<section class="kera"><h3 class="tier">{lo} to {hi - 1} <small>{E(name)}</small></h3>'
            f'<p class="eraline"><b>{len(rs)}</b> systems &middot; ' + ' and '.join(f'<b>{pct(fn, len(det))}%</b> {E(FAM_NAME[f].lower())}' for f in fams)
            + f' (of the {len(det)} whose kind is determined) &middot; ' + ' and '.join(f'<b>{pct(sn, sn_all)}%</b> in {E(SIGN_NAME[g].lower())}' for g in sgs)
            + f' (of {sn_all} recorded)</p>'
            f'<div class="cards">{cards}</div>'
            + '<p class="cap kcred">Images: ' + ' '.join(f'<b>{r["year"]}</b> {credit_of(r)}.' for r in pick) + '</p></section>')


STYLE = '''
.khero{max-width:var(--maxw);margin:0 auto;padding:0 1.2rem}
.khero figure{margin:0;text-align:left}
.kunits .u{stroke:none;transition:opacity .15s}
.kunits .u:hover{stroke:var(--head);stroke-width:1.4}
.k-sym{fill:var(--gold);background:var(--gold)}.k-mix{fill:var(--green);background:var(--green)}
.k-dig{fill:var(--ink);background:var(--ink)}.k-let{fill:var(--violet);background:var(--violet)}
.k-unk{fill:var(--muted);background:var(--muted);opacity:.38}
.vchart rect.seg.k-sym,.vchart rect.seg.k-mix,.vchart rect.seg.k-dig,.vchart rect.seg.k-let{stroke:none}
.klanes .lane{fill:var(--panel)}
.klanes .lname{fill:var(--head);font-size:12.5px;font-weight:600}.klanes .lmeta{fill:var(--muted);font-size:10.5px}
.klegend{list-style:none;padding:0;margin:.9rem 0 .2rem;display:flex;flex-wrap:wrap;gap:.4rem 1.3rem;font-size:.84rem;color:var(--muted);
 --s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181}
:root[data-theme="light"] .klegend{--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--s4:#eda100;--s5:#e87ba4}
.klegend li{display:flex;align-items:baseline;gap:.45rem;margin:0}
.klegend b{color:var(--ink2);font-weight:500;white-space:nowrap}
.klegend.wide{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:.4rem 1.6rem}
.klegend.wide li{display:block;line-height:1.4;padding-left:1.15rem;text-indent:-1.15rem}
.klegend.wide .sw{display:inline-block;margin-right:.43rem;text-indent:0}
.klegend .sw{flex:none;width:.72rem;height:.72rem;border-radius:3px;transform:translateY(1px)}
.klegend .sw.s1{background:var(--s1)}.klegend .sw.s2{background:var(--s2)}.klegend .sw.s3{background:var(--s3)}
.klegend .sw.s4{background:var(--s4)}.klegend .sw.s5{background:var(--s5)}
.kfinds{display:grid;grid-template-columns:repeat(auto-fit,minmax(205px,1fr));gap:1rem;margin:2.2rem 0 1rem}
.kfind{position:relative;background:var(--panel);border:1px solid var(--rule);border-radius:var(--radius);padding:1.15rem 1.2rem 1.2rem;overflow:hidden}
.kfind::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--gold)}
.kfind .n{font-family:var(--ui);font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}
.kfind b{display:block;font-family:var(--display);font-weight:500;font-size:2.15rem;line-height:1.05;color:var(--head);margin:.45rem 0 .5rem;letter-spacing:-.01em;white-space:nowrap}
.kfind b i{font-style:normal;color:var(--muted);font-size:.7em;margin:0 .12em}
.kfind p{margin:0;font-size:.9rem;line-height:1.45;color:var(--ink2)}
.ksec{margin:3.6rem 0 0}
.ksec > h2{margin:0 0 .5rem}
.ksec > .lede{font-size:1.06rem;color:var(--ink2);max-width:68ch;margin:0 0 1.1rem}
.kfig{text-align:left;background:var(--panel);border:1px solid var(--rule);border-radius:var(--radius);padding:1.1rem 1.2rem 1rem;margin:1.2rem 0 .6rem}
.kfig > h4{margin:0;font-family:var(--ui);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);font-weight:600}
.kfig .vfig{overflow-x:auto;margin:.7rem 0 0}
.kfig .vchart{width:100%;height:auto;display:block}
.kfig .vfig .vchart{min-width:600px}
.khero .kfig .vfig .vchart{min-width:0}
.kfig .cap,.ksec .cap,.khero .cap{font-size:.84rem;color:var(--muted);margin:.7rem 0 0;line-height:1.45}
.vchart rect.seg{stroke:none;transition:opacity .15s}
.kstack .col.thin{opacity:.78}
.kstack:hover .col{opacity:.5}.kstack .col:hover{opacity:1}
.vchart .nn{font-size:9.5px;fill:var(--muted)}
.kgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem;margin:1.2rem 0 .6rem}
.kpanel{margin:0;text-align:left;background:var(--panel);border:1px solid var(--rule);border-radius:var(--radius);padding:1rem 1.1rem .7rem}
.kpanel h3{margin:0;font-size:1.08rem;color:var(--head)}
.kpanel .gloss{margin:.15rem 0 .5rem;font-size:.82rem;line-height:1.35;color:var(--muted);min-height:2.2em}
.kpanel .peak{margin:0 0 .2rem;display:flex;align-items:baseline;gap:.5rem;font-size:.8rem;color:var(--muted)}
.kpanel .big{font-family:var(--display);font-weight:500;font-size:1.7rem;line-height:1;color:var(--head)}
.kpanel .vchart{width:100%;height:auto;display:block}
.vchart .karea{fill:var(--s1);opacity:.13;stroke:none}
.vchart .endv{fill:var(--ink2);font-size:11px;font-family:var(--mono)}
.ksize .dim{fill:var(--muted);opacity:.09}.ksize .dimlab{fill:var(--muted);font-size:10.5px;font-style:italic}
.ksize .iqr{fill:var(--s1);opacity:.24;stroke:none}.ksize .pt:hover .iqr{opacity:.4}
.ksize .trend{opacity:.55;stroke-dasharray:1 5;stroke-linecap:round}
.ksize .medv{fill:var(--head);font-size:12px;font-family:var(--mono);font-weight:600}
.kera{margin:0 0 1.2rem}.kera .eraline{margin:-.3rem 0 0;color:var(--muted);font-size:.92rem}.kera .eraline b{color:var(--head);font-weight:600}
.kera .cards{grid-template-columns:repeat(auto-fit,minmax(250px,1fr));margin:1rem 0 0}
.kera .card h3{font-size:1.08rem;line-height:1.25}.kera .card p{font-size:.88rem}
.kera .card .thumb{aspect-ratio:16/8}
.ktable{font-size:.8rem;font-variant-numeric:tabular-nums;min-width:920px;margin:.4rem 0}
.ktable th,.ktable td{padding:.42rem .55rem;text-align:right;white-space:nowrap}
.ktable thead th{white-space:normal;vertical-align:bottom;line-height:1.25;font-size:.68rem;letter-spacing:.06em}
.ktable tbody th{text-align:left;background:none;color:var(--ink2);text-transform:none;letter-spacing:0;font-family:var(--mono);font-size:.78rem}
.ktable.left td,.ktable.left th{text-align:left}
.ktable small{color:var(--muted);font-size:.72rem}.ktable .thin,.ktable .na{color:var(--muted)}
.ktable.heat td[style]{background:color-mix(in srgb,var(--gold) calc(var(--h) * .34%),transparent)}
#ktip{position:fixed;z-index:80;pointer-events:none;max-width:300px;padding:.5rem .7rem;border-radius:9px;background:var(--panel3);border:1px solid color-mix(in srgb,var(--gold) 45%,transparent);
 box-shadow:var(--shadow);color:var(--ink);font:400 .8rem/1.4 var(--ui);white-space:pre-line;opacity:0;transition:opacity .12s}
#ktip.on{opacity:1}#ktip::first-line{color:var(--head);font-weight:600}
.kfig .vchart,.kpanel .vchart{--s1:var(--ink2)}
.kunits .kq{stroke:var(--bg);stroke-width:1.2;opacity:1}.kunits rect.kq{stroke:none;opacity:.85}
.kunits .kqt{fill:var(--ink2);font-size:10.5px}.kunits .kqy{fill:var(--muted);font-family:var(--mono);font-size:9.5px}
.kunits .kqh{fill:var(--muted);font-size:8.5px;letter-spacing:.14em}
.kunits .hit{fill:transparent}.klegend li[hidden]{display:none}
.kfinds{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:2.4rem 0 1.4rem;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.kfind{background:none;border:0;border-left:1px solid var(--rule);border-radius:0;padding:1.3rem 1.3rem 1.4rem}
.kfind:first-child{border-left:0;padding-left:0}.kfind::before{display:none}
.kfind b{font-size:2.5rem;margin:.5rem 0 .55rem}.kfind b i{color:var(--gold);font-size:.6em;margin:0 .18em;vertical-align:.12em}
.kfind p{font-size:.88rem;color:var(--muted)}
.ksec{margin:3.4rem 0 0;padding-top:2.4rem;border-top:1px solid var(--rule)}
.ksec > h2{font-size:1.85rem;line-height:1.15;gap:.9rem}
.ksec > h2 .num{font-family:var(--display);font-size:1rem;letter-spacing:.04em;color:var(--gold);opacity:.9}
.ksec > .lede{font-size:1.1rem;line-height:1.55;max-width:64ch}
.kfig{padding:1.3rem 1.4rem 1.1rem;background:linear-gradient(180deg,var(--panel),transparent 140%)}
.klegend .kf{cursor:pointer;padding:.16rem .6rem .16rem .5rem;margin:0 -.2rem;border-radius:999px;border:1px solid transparent;transition:border-color .15s,opacity .15s,background .15s;user-select:none}
.klegend .kf:hover,.klegend .kf:focus-visible{border-color:var(--rule);outline:none;background:var(--panel)}
.klegend.wide .kf{border-radius:10px;padding-left:1.6rem}
.kfig[data-only] .klegend .kf{opacity:.45}
.kfig[data-only] .klegend .kf.on{opacity:1;border-color:color-mix(in srgb,var(--gold) 55%,transparent);background:var(--panel)}
.kfig[data-only] .kunits .u,.kfig[data-only] .kstack .seg{opacity:.1}
.kfig[data-only="k-sym"] .k-sym,.kfig[data-only="k-mix"] .k-mix,.kfig[data-only="k-dig"] .k-dig,.kfig[data-only="k-let"] .k-let{opacity:1 !important}
.kfig[data-only="k-unk"] .k-unk{opacity:.75 !important}
.kfig[data-only] .kstack:hover .col{opacity:1}
.krows{margin:1rem 0 0}
.krow{display:grid;grid-template-columns:minmax(150px,220px) 1fr;gap:0 1.4rem;align-items:end;padding:.55rem 0 0}
.krow + .krow{border-top:1px dashed var(--rule)}
.krow .kl{padding-bottom:.45rem}
.krow .kl b{display:block;color:var(--head);font-weight:600;font-size:.98rem;line-height:1.25}
.krow .kl span{display:block;color:var(--muted);font-size:.8rem;line-height:1.35;margin-top:.15rem}
.krow.kaxis{border-top:0;padding-top:.3rem;align-items:start}.krow.kaxis .kl{padding:0}.krow.kaxis .kl span{font-size:.72rem;margin:0}
.krowsvg{width:100%;height:auto;display:block;overflow:visible}
.krowsvg .rb{fill:var(--ink2);opacity:.62}.krowsvg .rb.thin{opacity:.36}.krowsvg .rb.pk{fill:var(--gold);opacity:1}
.krowsvg .rv{fill:var(--muted);font-size:10px;font-family:var(--mono)}.krowsvg .rv.pk{fill:var(--head);font-weight:600;font-size:11px}
.krowsvg .hit{fill:transparent}.krowsvg .hit:hover{fill:var(--panel2)}
.kpanel .pkdot{fill:var(--gold);stroke:var(--bg);stroke-width:1.5}
.kpanel .kn{margin:.5rem 0 0;padding-top:.55rem;border-top:1px solid var(--rule);font-size:.74rem;color:var(--muted);position:relative}
.kpanel .kn i{position:absolute;left:0;top:-1px;height:2px;width:var(--w);background:var(--gold);opacity:.8}
.kpanel .big{font-size:1.9rem}
.ksize .trend{stroke:var(--gold);opacity:.8}
.kera{margin:0 0 2rem}
.kera .kcred{font-size:.74rem;line-height:1.5}.kera .kcred b{color:var(--ink2);font-weight:600;font-family:var(--mono)}
@media (max-width:760px){.kfinds{grid-template-columns:1fr 1fr}.kfind{padding:1.1rem 1rem}.kfind:nth-child(odd){border-left:0;padding-left:0}.kfind:nth-child(n+3){border-top:1px solid var(--rule)}
 .krow{grid-template-columns:1fr;gap:.1rem}.krow .kl{padding-bottom:0}.krow.kaxis .kl{display:none}}
@media (max-width:640px){.khero .kfig .vfig .vchart{min-width:560px}.kfig{padding:1rem .9rem .9rem}.kfind b{font-size:1.8rem}}
'''

SCRIPT = '''<script>
(function(){var tip=document.createElement('div');tip.id='ktip';document.body.appendChild(tip);
function show(e){var el=e.target.closest&&e.target.closest('[data-tip]');if(!el){tip.classList.remove('on');return}
 tip.textContent=el.dataset.tip;tip.classList.add('on');var w=tip.offsetWidth,h=tip.offsetHeight,x=e.clientX+14,y=e.clientY+16;
 if(x+w>innerWidth-8)x=e.clientX-w-12;if(y+h>innerHeight-8)y=e.clientY-h-12;tip.style.left=Math.max(6,x)+'px';tip.style.top=Math.max(6,y)+'px'}
document.addEventListener('mousemove',show);document.addEventListener('click',show);
document.addEventListener('scroll',function(){tip.classList.remove('on')},{passive:true})})();
(function(){function pick(li){var fig=li.closest('.kfig');if(!fig)return;var k=li.dataset.k,off=fig.dataset.only===k;
 fig.querySelectorAll('.kf').forEach(function(x){x.classList.toggle('on',!off&&x===li)});if(off)delete fig.dataset.only;else fig.dataset.only=k}
document.addEventListener('click',function(e){var li=e.target.closest&&e.target.closest('.kf');if(li)pick(li)});
document.addEventListener('keydown',function(e){if((e.key==='Enter'||e.key===' ')&&e.target.classList&&e.target.classList.contains('kf')){e.preventDefault();pick(e.target)}})})();
</script>'''


def build():
    rows, n_targets = load()
    thumbs = sorted(p.name for p in (ROOT / 'docs' / 'thumbs').glob('*-480.webp')) if (ROOT / 'docs' / 'thumbs').exists() else []
    for r in rows:
        mine = [t for t in thumbs if t.startswith(r['target'] + '_')]
        r['thumb'] = next((t for t in mine if 'key' in t or 'cipher' in t), mine[0] if mine else None)
        r['power'] = power_of(r)
    T = tabulate(rows)
    dated = [r for r in rows if r['year'] is not None and START <= r['year'] < END]
    out_of_range = sum(1 for r in rows if r['year'] is not None and not START <= r['year'] < END)
    undated = sum(1 for r in rows if r['year'] is None)
    undet = sum(1 for r in dated if r['fam'] == 'undet')
    web = json.loads((ROOT / 'docs' / 'keys.json').read_text(encoding='utf-8'))
    kinds = C(k['kind'] for k in web['keys'])
    n_powers = len({r['country'] for r in dated if isinstance(r['country'], str) and r['country'] != 'unknown'})
    und = C(r['method'] for r in dated if r['fam'] == 'undet')
    lean = [n for n, _ in C(r['power'] for r in dated if r['power'] != 'Elsewhere').most_common(3)]
    lean = [n if n.startswith(('France', 'Spain', 'England')) else 'the ' + n for n in lean]
    late_letters = C(r['fam'] for r in dated if r['year'] >= 1850 and r['signs'] == 'letters')
    mono_zero = [label(b) for b in BINS if T[b]['det'] and not T[b]['fam']['mono']]

    def share(b0, b1, field, key, nfield):        # pooled share over the bins b0..b1 (inclusive starts)
        bs = [b for b in BINS if b0 <= b <= b1]
        return pct(sum(T[b][field][key] for b in bs), sum(T[b][nfield] for b in bs))

    def feat(b0, b1, k):
        bs = [b for b in BINS if b0 <= b <= b1]
        return pct(sum(T[b][k][0] for b in bs), sum(T[b][k][1] for b in bs))

    def med(b):
        return f'{T[b]["size"][1]:,.0f}' if T[b]['size'] else '?'

    nom_all = share(1400, 1750, 'fam', 'nomen', 'det')
    nom_min = min(pct(T[b]['fam']['nomen'], T[b]['det']) for b in BINS if b < 1800)
    sym15, sym18 = share(1400, 1450, 'signs', 'symbols', 'signs_n'), share(1700, 1750, 'signs', 'symbols', 'signs_n')
    dig = [share(c, c + 50, 'signs', 'digits', 'signs_n') for c in (1400, 1500, 1600, 1700)]
    code_early, code_1750, code_1800 = share(1400, 1700, 'fam', 'code', 'det'), pct(T[1750]['fam']['code'], T[1750]['det']), pct(T[1800]['fam']['code'], T[1800]['det'])
    arrow = '<i>&rarr;</i>'

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>How cipher keys changed, 1400 to 1949</title>
<meta name="description" content="A count across {len(dated)} cipher systems worked on in this project: which kinds of key the project's systems show in each half-century from 1400 to 1949, what they are written in, how large they are, and which devices come and go.">
<link rel="stylesheet" href="style.css">
</head>
<body id="top" class="pg-key-evolution">
<!-- site:nav -->
<section class="hero">
  <p class="kicker">Five and a half centuries of keys</p>
  <h1>How cipher keys changed</h1>
  <p class="sub">{len(dated)} cipher systems from {START} to {END - 1}, counted from the project's own records: what kind of key each one was, what it was written in, how large it grew, and which devices came and went.</p>
</section>
<div class="khero">
<figure class="kfig">
<h4>Every system counted, one square each, at the year of its earliest document</h4>
{sign_legend()}
<div class="vfig">{hero_strip(dated)}</div>
<p class="cap">The colour is what the ciphertext is written in. Hover a square for the cipher; click a colour in the legend to pick it out. The bars under the axis mark the years between which half of each kind's systems fall, with the median as a dot. The height of a column is how many systems the project holds for those five years, which follows what is digitised and what was chosen, not how much was enciphered.</p>
</figure>
</div>
<main>
<div class="kfinds">
<div class="kfind"><span class="n">Kind</span><b>{nom_all}%</b><p>of the systems from 1400 to 1799 whose kind is determined are nomenclators: an alphabet with a list of names and words.</p></div>
<div class="kfind"><span class="n">Signs</span><b>{sym15}%{arrow}{sym18}%</b><p>in invented signs, fifteenth century against eighteenth, of the systems whose signs are recorded.</p></div>
<div class="kfind"><span class="n">Size</span><b>{med(1400)}{arrow}{med(1750)}</b><p>distinct signs in the median key, 1400&ndash;49 ({T[1400]['size'][3]} systems) against 1750&ndash;99 ({T[1750]['size'][3]}).</p></div>
<div class="kfind"><span class="n">Codes</span><b>{code_early}%{arrow}{code_1800}%</b><p>codes that are not nomenclators, before 1750 against 1800&ndash;49, of the systems whose kind is determined.</p></div>
</div>
<nav class="toc"><span>On this page</span><a href="#families">Kinds</a><a href="#signs">Signs</a><a href="#powers">Powers</a><a href="#devices">Devices</a><a href="#size">Size</a><a href="#periods">Examples</a><a href="#method">What is counted</a></nav>

<section class="ksec" id="families">
<h2><span class="num">01</span>The nomenclator holds for four centuries</h2>
<p class="lede">From the first half-century counted to the end of the eighteenth, the nomenclator is never under {nom_min}% of the systems whose kind is determined. Systems typed as codes and not as nomenclators are {code_early}% before 1750, {code_1750}% in 1750&ndash;99 and {code_1800}% in 1800&ndash;49.</p>
<figure class="kfig">
<h4>Kinds of system: share of each half-century's systems</h4>
{rows_chart(T, FAMILIES, 'fam', 'det', 'systems')}
<p class="cap">Every row is on the same scale, so a bar twice as tall is twice the share. The gold bar is the kind's peak. A system that combines kinds is counted once, under the first it matches in this order: polyalphabetic, transposition or polygraphic; nomenclator; code; homophonic; simple. A system with a word list beside its alphabet is a nomenclator even when the profile also calls it a code. Paler bars rest on fewer than 25 systems.</p>
</figure>
<p>Polyalphabetic, transposition and polygraphic systems are {share(1400, 1700, 'fam', 'poly', 'det')}% before 1750 and {share(1850, 1900, 'fam', 'poly', 'det')}% from 1850 on. Simple substitution is {share(1400, 1750, 'fam', 'mono', 'det')}% of the systems before 1800 and {share(1800, 1900, 'fam', 'mono', 'det')}% after{(", with none in " + " or ".join(mono_zero)) if mono_zero else ""}.</p>
</section>

<section class="ksec" id="signs">
<h2><span class="num">02</span>Invented signs give way to figures</h2>
<p class="lede">Ciphers written in figures alone are {dig[0]}% of the fifteenth-century systems, {dig[1]}% of the sixteenth, {dig[2]}% of the seventeenth and {dig[3]}% of the eighteenth. From 1850 letters are {share(1850, 1900, 'signs', 'letters', 'signs_n')}% of the systems; of those {sum(late_letters.values())} systems, {late_letters['poly']} are polyalphabetic, transposition or polygraphic and {late_letters['code']} are codes.</p>
<figure class="kfig">
<h4>What the ciphertext is written in, share by half-century</h4>
{stacked(T, SIGNS, 'signs', 'signs_n', 'What the ciphertext is written in, by half-century', {k: SIGN_CLASS[k] for k in SIGN_CLASS if k})}
<p class="cap">Share of the systems whose sign inventory is recorded.</p>
</figure>
</section>

<section class="ksec" id="powers">
<h2><span class="num">03</span>The change falls in different decades for each power</h2>
<p class="lede">The same squares, one lane per power. The move from invented signs to figures is not one date: read along a lane to see when the gold ends for that power in what the project holds.</p>
<figure class="kfig">
<h4>The systems of each power, by year</h4>
{sign_legend()}
<div class="vfig">{lanes(dated)}</div>
<p class="cap">The power is the country the profile gives for most of a target's documents. It is usually the owner of the cipher, but not always: an envoy's letters can be filed under the court he wrote from, and a few lanes hold private manuscripts. The dates are those of the systems counted here, not of first or last use anywhere.</p>
</figure>
<details class="fold"><summary>First and last cases by power</summary>
{powers_table(dated)}
<p class="cap">Read these as pointers into the collection, with the same caution about the country label: several of the cases named are filed under a country that did not own the cipher, and some are unread or of undetermined kind.</p>
</details>
</section>

<section class="ksec" id="devices">
<h2><span class="num">04</span>Devices that come and go</h2>
<p class="lede">Of the systems where the profile says either way, {feat(1400, 1600, 'homophones')}% have homophones from 1400 to 1649 and {feat(1800, 1900, 'homophones')}% from 1800 on. Nulls go the same way ({feat(1400, 1600, 'nulls')}% and {feat(1800, 1900, 'nulls')}%).</p>
{multiples(T)}
<p class="cap">Each panel is the share of systems that have the device, among those where the profile records it either way; the figure at the right is the latest half-century with at least {MIN_N} such systems. A hollow point rests on fewer than {MIN_N}. Syllable signs are the exception: a system counts as without them whenever its kind is determined and the profile lists none, so that share is a lower bound. For the disordered key, keyword-derived keys and systems with no sign table are left out.</p>
<p>Marks that change a sign's value are {feat(1500, 1650, 'marks')}% of the systems from 1500 to 1699 against {feat(1700, 1900, 'marks')}% after. The disordered key is {feat(1400, 1650, 'disordered')}% before 1700 and {feat(1700, 1900, 'disordered')}% from 1700; it is recorded for fewer systems than the other devices.</p>
</section>

<section class="ksec" id="size">
<h2><span class="num">05</span>Keys grow with the eighteenth century</h2>
<p class="lede">The median key has {med(1400)} distinct signs in 1400&ndash;49 and {med(1650)} in 1650&ndash;99. It reaches {med(1700)} in 1700&ndash;49 and {med(1750)} in 1750&ndash;99, with the nomenclators in figures.</p>
<figure class="kfig">
<h4>Distinct signs or groups per system: median, and the middle half</h4>
{sizes(T)}
<p class="cap">Counted in the key where it survives, otherwise from the ciphertext, where it is a lower bound: a short letter uses a small part of a large key. Logarithmic scale. From 1850 the profile often records the alphabet a code is spelled in (26 letters), not its number of groups, so the low medians there are not a return to small keys.</p>
</figure>
</section>

<section class="ksec" id="periods">
<h2><span class="num">06</span>Examples by period</h2>
{era(dated, 1400, 1500)}
{era(dated, 1500, 1650)}
{era(dated, 1650, 1800)}
{era(dated, 1800, 1950)}
</section>

<section class="ksec" id="method">
<h2><span class="num">07</span>What is counted</h2>
<div class="stats">
<div class="stat"><b>{len(dated)}</b><span>systems, {START}&ndash;{END - 1}</span></div>
<div class="stat"><b>{n_targets}</b><span>target profiles counted</span></div>
<div class="stat"><b>{len(web["keys"])}</b><span>keys in the key web</span></div>
<div class="stat"><b>{n_powers}</b><span>country labels in the profiles</span></div>
</div>
<p>The unit is a cipher system: one key, or one code, as recorded in a target's <code>profile.json</code>. Targets that the <a href="keys.html">key web</a> joins to the same key count once, at the earliest dated document. That gives {len(rows)} systems from {n_targets} targets ({len(SKIPPED)} more profiles are not ciphers and are left out); {len(dated)} are dated between {START} and {END - 1} ({out_of_range} fall outside those years and {undated} have no year). For {undet} of the {len(dated)} the kind of system is not determined ({und['not solved']} of them not solved); they are left out of the first chart and stay in the others where the field in question is known.</p>
<div class="callout amber"><p>This is a count of what the project has worked on, not a sample of what chanceries produced. It leans towards {lean[0]}, {lean[1]} and {lean[2]}, towards 1500 to 1650, and towards collections that are digitised. A key that survives without a letter, and a letter nobody has photographed, are both missing.</p></div>
<p>The key web holds {kinds["rebuilt here"]} keys rebuilt here, {kinds["scholar's key"]} recovered by other scholars, {kinds["DECODE key record"]} DECODE key records, {kinds["contemporary key"]} contemporary keys and {kinds["archive key"]} archive keys. Its entries carry a year and a description in prose, not the fixed fields used above, so this page counts from the profiles; keys in the web that no target uses yet are not counted.</p>
<details class="fold"><summary>The numbers behind every chart</summary>
{data_table(T)}
<p class="cap">Shares are of the systems where the field is recorded; hover a cell for the count. Shares on fewer than {MIN_N} systems are greyed. Median size is in distinct signs or groups and median list is the number of nomenclator or code entries, each with the number of systems that record it. The commentary on this page states what the counts show and is not set against the literature on the nomenclator and the code.</p>
</details>
</section>
</main>
{SCRIPT}
</body>
</html>
'''
    return page, T, rows


def build_html():
    page, T, rows = build()
    css = STYLE.strip() + '\n'
    if not CSS.exists() or CSS.read_text(encoding='utf-8') != css:
        CSS.write_text(css, encoding='utf-8', newline='\n')
    OUT.write_text(page, encoding='utf-8', newline='\n')
    return len(rows)


if __name__ == '__main__':
    if '--table' in sys.argv:
        page, T, rows = build()
        for b in BINS:
            r = T[b]
            print(label(b), 'n', r['n'], 'det', r['det'], dict(r['fam']), '| signs', dict(r['signs']), '|',
                  {k: r[k] for k, _, _ in FEATURES}, '| size', r['size'], '| entries', r['entries'])
    else:
        print(f'wrote {OUT}: {build_html()} systems, counted from {ROOT}')
