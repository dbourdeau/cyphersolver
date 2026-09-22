"""Scoreboard for index.html, computed from the result tables in ../README.md.

Run  python _build_stats.py  from docs/ (then _build_site.py as usual). Idempotent: rewrites the block between
<!-- stats:start --> and <!-- stats:end -->, inserting it after <main> the first time, and adds the jump link.

Categories are the README's own sections. Every number on the page is derived here, nothing is typed in:
  solved    ### Solved: key broken here         (key recovered here by cryptanalysis; text meets the read bar)
  read      ### Read with an existing key       (text meets the read bar with a key or decipherment that already existed)
  nothing   ### Explained                        (shown to carry no message)
  partsolved ### Partly solved                   (key broken here, text below the read bar)
  partly    ### Partly read with an existing key (text below the read bar)
  found     ### Found already solved by others   (the lists were stale)
  closed    ### Attempted and closed             (attacked with controls; the notes say why it stops)
  offline   ### Offline only                     (nothing more can be done online)
  active    ### In progress
Overrides: rows whose target text matches OVERRIDE are moved (none at present).
"""
import re, pathlib, html, datetime

HERE = pathlib.Path(__file__).parent
README = HERE.parent / 'README.md'
INDEX = HERE / 'index.html'
YEAR_NOW = datetime.date.today().year

SECTIONS = [
    ('solved',  '### Solved'),
    ('read',    '### Read with'),
    ('nothing', '### Explained'),
    ('partsolved', '### Partly solved'),
    ('partly',  '### Partly read'),
    ('found',   '### Found already solved'),
    ('closed',  '### Attempted and closed'),
    ('offline', '### Offline only'),
    ('active',  '### In progress'),
]
# Rows whose date carries no year but can be bracketed: counted at the latest possible year, so the
# years-of-silence sum is never overstated. Egmond: to the grand maître (Montmorency, from 1526); Charles died June 1538.
YEAR_BRACKET = {'Charles of Egmond': 1537}
OVERRIDE = {}  # README row text -> category, for rows filed in a table that does not match their outcome
LABEL = {
    'solved': 'solved here', 'read': 'read with an existing key', 'nothing': 'no message', 'partsolved': 'partly solved here', 'partly': 'partly read with an existing key', 'found': 'already solved elsewhere',
    'closed': 'closed, with the reason', 'offline': 'waiting on an archive', 'active': 'in progress',
}
COLOR = {  # CSS variables from style.css
    'solved': 'var(--green)', 'read': 'color-mix(in srgb, var(--green) 50%, var(--blue))', 'nothing': 'var(--blue)', 'partsolved': 'var(--violet)', 'partly': 'color-mix(in srgb, var(--violet) 50%, var(--blue))', 'found': 'var(--amber)',
    'closed': 'var(--red)', 'offline': 'var(--muted)', 'active': 'var(--gold)',
}

def parse_year(s):
    s = s.strip()
    m = re.search(r'(\d{4})', s)
    if m:
        y = int(m.group(1))
        return y + 5 if re.search(r'\d{4}s', s) else y     # "c.1950s" -> 1955
    m = re.search(r'(\d{2})th c', s)
    if m:
        return (int(m.group(1)) - 1) * 100 + 50           # "17th c." -> 1650
    return None

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
            items.append(dict(name=name, date=date.strip(), year=parse_year(date) or next((y for k, y in YEAR_BRACKET.items() if name.startswith(k)), None), cat=c, note=note,
                              notehead=head2, when=when, whenhead=cols[2] if len(cols) >= 5 else '',
                              href=m.group(1) if m else ''))
    return items

def timeline_svg(items):
    dated = [it for it in items if it['year']]
    x0, x1 = min(1480, min(it['year'] for it in dated) // 50 * 50 - 10), 2000
    c0 = (x0 // 100 + 1) * 100          # first century line on the axis
    W, top, lane_h, r = 1000, 34, 13, 4.6
    def X(y): return 30 + (y - x0) / (x1 - x0) * (W - 60)
    # lane assignment: greedy, avoid overlap within 11 px
    lanes, placed = [], []
    for it in sorted(dated, key=lambda d: d['year']):
        x = X(it['year'])
        for li, last in enumerate(lanes):
            if x - last >= 11:
                lanes[li] = x; placed.append((it, x, li)); break
        else:
            lanes.append(x); placed.append((it, x, len(lanes) - 1))
    nl = len(lanes)
    base = top + nl * lane_h + 6
    H = base + 30
    out = [f'<div class="tlwrap"><svg class="tl" viewBox="0 0 {W} {H}" role="img" aria-label="Every target placed by date and coloured by outcome" preserveAspectRatio="xMidYMid meet">']
    out.append('<defs><filter id="tlglow" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="3.2"/></filter>'
               '<linearGradient id="tlfade" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="currentColor" stop-opacity="0"/>'
               '<stop offset="1" stop-color="currentColor" stop-opacity=".07"/></linearGradient></defs>')
    for k, c in enumerate(range(c0 - 100, 2000, 100)):   # alternating century bands with a faint era label
        a, b = max(30, X(c)), X(c + 100)
        if k % 2 == 0:
            out.append(f'<rect class="band" x="{a:.1f}" y="{top-18}" width="{b-a:.1f}" height="{base-top+18}" fill="url(#tlfade)"/>')
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
    for n, (it, x, li) in enumerate(placed):
        y = base - 9 - li * lane_h
        e = lambda v: html.escape(v, quote=True)
        title = e(f"{it['name']} ({it['date']}): {LABEL[it['cat']]}")
        attrs = (f' data-name="{e(it["name"])}" data-date="{e(it["date"])}" data-year="{it["year"]}" data-cat="{it["cat"]}"'
                 f' data-label="{e(LABEL[it["cat"]])}" data-note="{e(it["note"])}" data-notehead="{e(it["notehead"])}"'
                 f' data-when="{e(it["when"])}" data-whenhead="{e(it["whenhead"])}"')
        dot = (f'<circle class="halo" cx="{x:.1f}" cy="{y}" r="{r+2.5}" fill="{COLOR[it["cat"]]}" filter="url(#tlglow)"/>'
               f'<circle class="core" cx="{x:.1f}" cy="{y}" r="{r}" fill="{COLOR[it["cat"]]}"/>')
        style = f' style="--i:{n};--dy:{base - y}px"'
        if it['href']:
            out.append(f'<a class="pt {it["cat"]}" href="{it["href"]}" aria-label="{title}"{attrs}{style}>{dot}</a>')
        else:
            out.append(f'<g class="pt {it["cat"]}" tabindex="0" aria-label="{title}"{attrs}{style}>{dot}</g>')
    out.append('</svg><div class="tltip" role="tooltip" hidden></div></div>')
    return '\n'.join(out)

def build(items):
    n = {c: sum(1 for it in items if it['cat'] == c) for c, _ in SECTIONS}
    total = len(items)
    attacked = total - n['offline']                     # everything that got a real attempt online
    nread = n['solved'] + n['read']                     # texts that meet the read bar
    decided = nread + n['nothing'] + n['found']     # outcomes with a definite answer
    read = [it for it in items if it['cat'] in ('solved', 'read') and it['year']]
    silence = sum(YEAR_NOW - it['year'] for it in read)
    oldest = min(read, key=lambda d: d['year'])
    span = [it['year'] for it in items if it['year']]
    pct = round(100 * nread / attacked)
    order = ['solved', 'read', 'nothing', 'found', 'partsolved', 'partly', 'active', 'closed', 'offline']
    bar = ''.join(
        f'<span class="seg {c}" style="flex:{n[c]};background:{COLOR[c]}" title="{n[c]} {LABEL[c]}"></span>'
        for c in order if n[c])
    legend = ''.join(
        f'<button type="button" class="lg" data-cat="{c}" aria-pressed="false"><i style="background:{COLOR[c]}"></i>{n[c]} {LABEL[c]}</button>' for c in order if n[c])
    lines = []
    lines.append('<!-- stats:start -->')
    lines.append('<section class="scoreboard" id="scoreboard" aria-labelledby="sb-h">')
    lines.append('<h2 id="sb-h"><span class="num">&sum;</span> The ledger so far</h2>')
    lines.append(f'<p class="sb-lede">{total} targets taken from the three lists. {attacked} were attacked online; {n["offline"]} stop at an archive door before any cryptanalysis is possible. Every outcome is one of eight kinds, and the honest denominator for a &ldquo;success rate&rdquo; is the {attacked} attacked, not the {total}.</p>')
    lines.append(f'<div class="sb-bar" role="img" aria-label="Outcomes of {total} targets">{bar}</div>')
    lines.append(f'<div class="sb-legend">{legend}</div>')
    lines.append('<div class="sb-grid">')
    lines.append(f'<div class="sb-big"><b>{nread} <small>of {attacked}</small></b><span>attacked targets read in full or in substance, {pct}&nbsp;%: {n["solved"]} solved here (the key broken by cryptanalysis), {n["read"]} read with a key or decipherment that already existed. One completes an alphabet another solver published (Boswell 1643); one applies a table already in print to letters never before decoded (Catinat 1691).</span></div>')
    lines.append(f'<div class="sb-big"><b>{decided}</b><span>questions settled one way or another: read, shown to carry no message, or found already solved in print, in a comment thread, or on GitHub.</span></div>')
    lines.append(f'<div class="sb-big"><b>{n["closed"]}</b><span>attacks that stop with a stated reason and a control that passed where the target failed. A negative here says something; it is not a shrug.</span></div>')
    lines.append(f'<div class="sb-big"><b>{silence:,}</b><span>years of silence ended, summed over the {len(read)} texts read' + (f' that carry a date ({nread - len(read)} undated)' if len(read) != nread else '') + f': each had waited from its date until {YEAR_NOW}. The oldest is {oldest["name"].split(",")[0].split(" (")[0]} ({oldest["date"]}).</span></div>')
    lines.append('</div>')
    lines.append(f'<p class="sb-note">Every target by date, {min(span)}&ndash;{max(span)}. Hover or tap a dot for the story; click a colour in the legend to isolate an outcome.</p>')
    lines.append(timeline_svg(items))
    lines.append(f'<p class="sb-foot">Counted from the results tables in the <a href="https://github.com/dbourdeau/cyphersolver#results">repository README</a> by <code>_build_stats.py</code>; regenerated {datetime.date.today():%d %B %Y}. &ldquo;Already solved elsewhere&rdquo; and &ldquo;no message&rdquo; are not decipherments and are not counted as such. Rows are documents, not correspondents: S&eacute;gur f.&nbsp;143 and Urquhart&rsquo;s distich stand as separate open items beside the letters and the octastich that were read.</p>')
    lines.append('</section>')
    lines.append('<!-- stats:end -->')
    return '\n'.join(lines), n

def main():
    items = load()
    block, n = build(items)
    s = INDEX.read_text(encoding='utf-8')
    if '<!-- stats:start -->' in s:
        s = re.sub(r'<!-- stats:start -->.*?<!-- stats:end -->', lambda m: block, s, flags=re.S)
    else:
        s = s.replace('<main>\n', '<main>\n\n' + block + '\n\n', 1)
    if 'href="#scoreboard"' not in s:
        s = s.replace('<div class="jump"><a href="#recent">', '<div class="jump"><a href="#scoreboard">The ledger</a><a href="#recent">', 1)
    INDEX.write_text(s, encoding='utf-8')
    for c, _ in SECTIONS:
        print(f'{c:8s} {n[c]:3d}  ' + '; '.join(it['name'][:28] for it in items if it['cat'] == c))
    print('total', len(items), 'undated:', [it['name'] for it in items if not it['year']])

if __name__ == '__main__':
    main()
