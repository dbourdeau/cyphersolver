"""Scoreboard for index.html, computed from the result tables in ../README.md.

Run  python _build_stats.py  from docs/ (then _build_site.py as usual). Idempotent: rewrites the block between
<!-- stats:start --> and <!-- stats:end -->, inserting it after <main> the first time, and adds the jump link.

Categories are the README's own sections, one per outcome method (docs/_methods.py, George Lasry's categories):
  ct, extpt, adjpt   the key recovered here: ciphertext-only, from external plaintext, from adjacent plaintext
  extkey, known      an existing key applied: one matched here from elsewhere, or one already identified
  deciph             an existing complete decipherment transcribed and checked
  notsolved, na      attempted without result; not a cipher or not reachable
  active             ### In progress
Every number on the page is derived here, nothing is typed in. The Extent column (complete / partial) is counted too.
Overrides: rows whose target text matches OVERRIDE are moved (none at present).
"""
import json, re, pathlib, html, datetime

HERE = pathlib.Path(__file__).parent
README = HERE.parent / 'README.md'
INDEX = HERE / 'index.html'
YEAR_NOW = datetime.date.today().year

import sys; sys.path.insert(0, str(HERE))
import _methods as M
SECTIONS = [(M.KEY[m], M.SECTION[m]) for m in M.METHODS] + [('active', '### In progress')]
# Rows whose date carries no year but can be bracketed: counted at the latest possible year, so the
# years-of-silence sum is never overstated. Egmond: to the grand maître (Montmorency, from 1526); Charles died June 1538.
YEAR_BRACKET = {'Charles of Egmond': 1537}
OFF_TIMELINE = ('Kaliningrad bottle post',)  # counted in the ledger, not drawn on the timeline (BC/BCE rows are left off by parse_year)
OVERRIDE = {}  # README row text -> category, for rows filed in a table that does not match their outcome
LABEL = {M.KEY[m]: M.LABEL[m] for m in M.METHODS}
LABEL.update(na='not a cipher or not reachable', active='in progress')
COLOR = {  # CSS variables from style.css
    'ct': 'var(--green)', 'extpt': 'color-mix(in srgb, var(--green) 65%, var(--blue))', 'adjpt': 'color-mix(in srgb, var(--green) 40%, var(--blue))',
    'extkey': 'var(--violet)', 'known': 'color-mix(in srgb, var(--violet) 50%, var(--blue))', 'deciph': 'var(--amber)',
    'notsolved': 'var(--red)', 'na': 'var(--muted)', 'active': 'var(--ink2)',
}

def parse_year(s):
    s = s.strip()
    if re.search(r'\bBC(E)?\b', s):
        return None                                       # Linear A, Indus: off the 1400-2000 timeline
    m = re.search(r'(\d{4})', s)
    if m:
        y = int(m.group(1))
        return y + 5 if re.search(r'\d{4}s', s) else y     # "c.1950s" -> 1955
    m = re.search(r'(\d{2})th c', s)
    if m:
        return (int(m.group(1)) - 1) * 100 + 50           # "17th c." -> 1650
    return None

import _credits as CR
_PROFILES = CR.load_all()
def outside(folders):
    """True when an outside contributor produced the row's result (profile outcome.provenance contributed or mixed)."""
    return any(CR.provenance_of(_PROFILES.get(f.lower())) in ('contributed', 'mixed') for f in folders)

def strip_md(s):
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'[`*]', '', s)
    return html.unescape(s).strip()

def load():
    text = README.read_text(encoding='utf-8')
    items = []
    for cat, head in SECTIONS:
        i = text.find(head)
        if i < 0:
            continue
        j = text.find('\n### ', i + 1); j = len(text) if j < 0 else j
        k = text.find('\n## ', i + 1)
        if 0 <= k < j: j = k
        cols = []
        for line in text[i:j].splitlines():
            if line.startswith('| Target'):
                cols = [c.strip() for c in line.strip().strip('|').split('|')]
                continue
            if not line.startswith('| ') or line.startswith('|---'):
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) < 2:
                continue
            name, date = strip_md(cells[0]), cells[1]
            c = cat
            for key, dest in OVERRIDE.items():
                if key in name:
                    c = dest
            m = re.search(r'write-up\]\((?:https://dbourdeau\.github\.io/cyphersolver/)?([\w.-]+\.html)\)', cells[-1])
            note = strip_md(cells[-2]) if len(cells) >= 4 else ''
            head2 = cols[-2] if len(cols) >= 4 else ''
            when = strip_md(cells[2]) if len(cells) >= 5 else ''
            ext = strip_md(cells[cols.index('Extent')]) if 'Extent' in cols and len(cells) == len(cols) else ''
            folders = re.findall(r'targets/([\w.-]+)/', cells[-1])
            items.append(dict(ext=ext, name=name, outside=outside(folders), date=date.strip(), year=parse_year(date) or next((y for k, y in YEAR_BRACKET.items() if name.startswith(k)), None), cat=c, note=note,
                              notehead=head2, when=when, whenhead=cols[2] if len(cols) >= 5 else '',
                              href=m.group(1) if m else ''))
    return items

def timeline_svg(items):
    dated = [it for it in items if it['year'] and not it['name'].startswith(OFF_TIMELINE)]
    x0, x1 = min(1480, min(it['year'] for it in dated) // 50 * 50 - 10), 2000
    c0 = (x0 // 100 + 1) * 100          # first century line on the axis
    W, top, r = 1000, 34, 4.6
    # Piecewise-linear axis: each half-century gets width in proportion to 1 + count**0.85, so the crowded
    # sixteenth century is spread out and the empty fifteenth and nineteenth are compressed. Every 50-year line is
    # drawn, so the uneven spacing stays visible.
    edges = list(range(x0 // 50 * 50, x1 + 1, 50))
    wts = [1 + sum(1 for it in dated if a <= it['year'] < a + 50) ** .85 for a in edges[:-1]]
    acc = [0.0]
    for w in wts: acc.append(acc[-1] + w)
    def X(y):
        y = min(max(y, edges[0]), edges[-1]); k = min(int((y - edges[0]) // 50), len(wts) - 1)
        f = (acc[k] + (y - edges[k]) / 50 * wts[k]) / acc[-1]
        return 30 + f * (W - 60)
    # beeswarm: each dot drops to the lowest height where it clears every dot already placed (2-D distance), so
    # neighbouring stacks interlock instead of each 11-px window building its own column
    gap, placed = 2 * r + 1.2, []
    # a dot may also slide sideways (up to 3 gaps) when that keeps it lower, so a pile of same-year rows spreads
    # into a mound rather than a spike; sideways costs 1.5x height, so dots stay near their year
    def lowest(x):
        near = [(px, h0) for _, px, h0 in placed if abs(px - x) < gap]
        for cand in sorted({0.0} | {h0 + ((gap ** 2 - (px - x) ** 2) ** .5) for px, h0 in near}):
            if all((px - x) ** 2 + (h0 - cand) ** 2 >= gap ** 2 - 1e-6 for px, h0 in near):
                return cand
    for it in sorted(dated, key=lambda d: d['year']):
        x0_ = X(it['year'])
        best = min(((lowest(x0_ + d) + 1.5 * abs(d), x0_ + d) for d in (k * gap / 4 for k in range(-12, 13))
                    if 30 <= x0_ + d <= W - 30))
        x = best[1]; h = lowest(x)
        placed.append((it, x, h))
    hmax = max(h for _, _, h in placed)
    base = top + hmax + 2 * r + 12
    H = round(base + 30)
    out = [f'<div class="tlwrap"><svg class="tl" viewBox="0 0 {W} {H}" role="img" aria-label="Every target placed by date and coloured by outcome" preserveAspectRatio="xMidYMid meet">']
    out.append('<defs><filter id="tlglow" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="3.2"/></filter>'
               '<linearGradient id="tlfade" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="currentColor" stop-opacity="0"/>'
               '<stop offset="1" stop-color="currentColor" stop-opacity=".07"/></linearGradient></defs>')
    for k, c in enumerate(range(c0 - 100, 2000, 100)):   # alternating century bands with a faint era label
        a, b = max(30, X(c)), X(c + 100)
        if k % 2 == 0:
            out.append(f'<rect class="band" x="{a:.1f}" y="{top-18}" width="{b-a:.1f}" height="{base-top+18}" fill="url(#tlfade)"/>')
        if b - a >= 70:                                    # compressed centuries are too narrow for a label
            out.append(f'<text class="era" x="{(a+b)/2:.1f}" y="{top-6}" text-anchor="middle">{c//100+1}th c.</text>')
    for c in range(c0 - 50, 2001, 50):
        x = X(c)
        if x < 30: continue
        out.append(f'<line x1="{x:.1f}" y1="{top-2}" x2="{x:.1f}" y2="{base}" class="grid{" major" if c % 100 == 0 else ""}"/>')
    out.append(f'<line x1="30" y1="{base}" x2="{W-30}" y2="{base}" class="axis"/>')
    for c in range(c0, 2001, 100):
        x = X(c)
        out.append(f'<line x1="{x:.1f}" y1="{base-4}" x2="{x:.1f}" y2="{base+4}" class="axis"/>')
        out.append(f'<text x="{x:.1f}" y="{base+18}" class="tick" text-anchor="middle">{c}</text>')
    out.append(f'<g class="cursor" aria-hidden="true"><line class="cur-line" x1="0" x2="0" y1="{top-2}" y2="{base}"/>'
               f'<rect class="cur-box" x="-19" y="{base+5}" width="38" height="17" rx="4"/><text class="cur-yr" x="0" y="{base+17.5}" text-anchor="middle"></text></g>')
    tip_data = []   # tooltip text, loaded by site.js from timeline.json so the page does not carry it per dot
    for n, (it, x, h) in enumerate(placed):
        y = round(base - 9 - h, 1)
        e = lambda v: html.escape(v, quote=True)
        title = e(f"{it['name']} ({it['date']}): {LABEL[it['cat']]}")
        attrs = f' data-i="{n}" data-year="{it["year"]}" data-cat="{it["cat"]}"'
        tip_data.append({'name': it['name'][:130], 'date': it['date'], 'note': it['note'][:230], 'notehead': it['notehead'], 'when': it['when'], 'whenhead': it['whenhead'], 'label': LABEL[it['cat']]})
        dot = (f'<circle class="halo" cx="{x:.1f}" cy="{y}" r="{r+2.5}" fill="{COLOR[it["cat"]]}" filter="url(#tlglow)"/>'
               f'<circle class="core" cx="{x:.1f}" cy="{y}" r="{r}" fill="{COLOR[it["cat"]]}"/>')
        style = f' style="--i:{n};--dy:{base - y}px"'
        if it['href']:
            out.append(f'<a class="pt {it["cat"]}" href="{it["href"]}" aria-label="{title}"{attrs}{style}>{dot}</a>')
        else:
            out.append(f'<g class="pt {it["cat"]}" tabindex="0" aria-label="{title}"{attrs}{style}>{dot}</g>')
    (pathlib.Path(__file__).parent / 'timeline.json').write_text(json.dumps(tip_data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    out.append('</svg><div class="tltip" role="tooltip" hidden></div></div>')
    return '\n'.join(out)

def build(items):
    n = {c: sum(1 for it in items if it['cat'] == c) for c, _ in SECTIONS}
    total = len(items)
    broke = n['ct'] + n['extpt'] + n['adjpt']            # key recovered here by cryptanalysis
    applied = n['extkey'] + n['known'] + n['deciph']     # an existing key or decipherment applied
    got = [it for it in items if it['cat'] in ('ct', 'extpt', 'adjpt', 'extkey', 'known', 'deciph')]
    keyonly = lambda cats: sum(1 for it in got if it['cat'] in cats and it['ext'].startswith('none'))  # key, text not read (Lasry, 24 Oct 2026)
    ko_b, ko_a = keyonly(('ct', 'extpt', 'adjpt')), keyonly(('extkey', 'known', 'deciph'))
    part = sum(1 for it in got if it['ext'].startswith('partial'))
    attacked = total - n['na'] - n['active']
    read = [it for it in got if it['ext'].startswith('complete') and it['year']]
    silence = sum(YEAR_NOW - it['year'] for it in read)
    oldest = min(read, key=lambda d: d['year'])
    span = [it['year'] for it in items if it['year'] and not it['name'].startswith(OFF_TIMELINE)]
    order = ['ct', 'extpt', 'adjpt', 'extkey', 'known', 'deciph', 'notsolved', 'active', 'na']     # three families, then the rest
    pc = lambda k, d: f'{100 * k / d:.0f}%' if d else '0%'     # share, whole percent
    share = lambda c: '' if c in ('active', 'na') else f' ({pc(n[c], attacked)})'      # every percentage is of the attempted entries
    bar = ''.join(
        f'<span class="seg {c}" style="flex:{n[c]};background:{COLOR[c]}" title="{n[c]} {LABEL[c]}{share(c)}"></span>'
        for c in order if n[c])
    legend = ''.join(
        f'<button type="button" class="lg" data-cat="{c}" aria-pressed="false"><i style="background:{COLOR[c]}"></i>{n[c]} {LABEL[c]}' + ('' if c in ('active', 'na') else f' <small>{pc(n[c], attacked)}</small>') + '</button>' for c in order if n[c])
    lines = []
    lines.append('<!-- stats:start -->')
    lines.append('<section class="scoreboard" id="scoreboard" aria-labelledby="sb-h">')
    lines.append('<h2 id="sb-h">Results so far</h2>')
    lines.append(f'<p class="sb-lede">{total} entries, one per row of the results tables, each classed by <a href="glossary.html">how its text was obtained</a>. {n["na"]} turned out not to be ciphers or could not be reached and {n["active"]} are in progress, which leaves {attacked} attempted; every percentage here is of those {attacked}.</p>')
    lines.append('<div class="sb-grid">')
    by_contrib = sum(1 for it in items if it['cat'] in ('ct', 'extpt', 'adjpt') and it['outside'])
    who = f' {by_contrib} of them with <a href="contributors.html">outside contributors</a>.' if by_contrib else ''
    lines.append(f'<div class="sb-big fam-key"><b>{broke}</b><em>{pc(broke, attacked)} of attempts</em><span>keys recovered by cryptanalysis</span><details><summary>breakdown</summary><span>{n["ct"]} from the ciphertext alone, {n["adjpt"]} from plaintext beside the ciphertext, {n["extpt"]} from plaintext found elsewhere.{who}' + (f' In {ko_b} of them the key was recovered but the text does not yet read.' if ko_b else '') + '</span></details></div>')
    lines.append(f'<div class="sb-big fam-ext"><b>{applied}</b><em>{pc(applied, attacked)} of attempts</em><span>obtained with a key or decipherment that already existed</span><details><summary>breakdown</summary><span>{n["known"]} with a known key, {n["extkey"]} with a key matched here from another document, {n["deciph"]} from a complete existing decipherment.' + (f' In {ko_a} of them the key was applied but the text does not yet read.' if ko_a else '') + '</span></details></div>')
    lines.append(f'<div class="sb-big fam-no"><b>{n["notsolved"]}</b><em>{pc(n["notsolved"], attacked)} of attempts</em><span>closed without recovering the text; each write-up says why</span></div>')
    lines.append(f'<div class="sb-big"><b>{silence:,}</b><em>years of silence ended</em><span>summed over the {len(read)} dated texts obtained in full ({part} more partial), each counted from its date to {YEAR_NOW}. The oldest is {oldest["name"].split(",")[0].split(" (")[0]} ({oldest["date"]}).</span></div>')
    lines.append('</div>')
    lines.append(f'<div class="sb-bar" role="img" aria-label="Outcomes of {total} entries by method">{bar}</div>')
    lines.append(f'<details class="sb-methods"><summary>All {sum(1 for c in order if n[c])} categories</summary><div class="sb-legend">{legend}</div></details>')
    lines.append(f'<p class="sb-note">Every entry by date, {min(span)}&ndash;{max(span)}. Hover or tap a dot for the story; open the categories and click one to isolate it.</p>')
    lines.append(timeline_svg(items))
    lines.append(f'<p class="sb-foot">Counted from the results tables in the <a href="https://github.com/dbourdeau/cyphersolver#results">repository README</a> by <code>_build_stats.py</code>; regenerated {datetime.date.today():%d %B %Y}. Rows are documents, not correspondents.</p>')
    lines.append('</section>')
    lines.append('<!-- stats:end -->')
    import _catalogue_page as C
    still_open = sum(1 for e in C.DATA['entries'] if e['counted'] and C.is_open(e))
    hero = (f'<p class="herostats"><a href="#scoreboard"><b>{broke}</b> keys recovered</a>'
            f'<a href="#scoreboard"><b>{applied}</b> from existing keys or decipherments</a><a href="catalogue.html"><b>{still_open:,}</b> ciphers still open</a></p>')
    return '\n'.join(lines), n, hero

def main():
    items = load()
    block, n, hero = build(items)
    s = INDEX.read_text(encoding='utf-8')
    if '<!-- stats:start -->' in s:
        s = re.sub(r'<!-- stats:start -->.*?<!-- stats:end -->', lambda m: block, s, flags=re.S)
    else:
        s = s.replace('<main>\n', '<main>\n\n' + block + '\n\n', 1)
    s = re.sub(r'<!-- herostats:start -->.*?<!-- herostats:end -->', lambda m: '<!-- herostats:start -->\n' + hero + '\n<!-- herostats:end -->', s, flags=re.S)
    INDEX.write_text(s, encoding='utf-8')
    for c, _ in SECTIONS:
        print(f'{c:8s} {n[c]:3d}  ' + '; '.join(it['name'][:28] for it in items if it['cat'] == c))
    print('total', len(items), 'undated:', [it['name'] for it in items if not it['year']])

if __name__ == '__main__':
    main()
