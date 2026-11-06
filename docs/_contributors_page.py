"""docs/contributors.html and the landing page's contributors strip, from the credits in every profile.json
(outcome.credits, _credits.py) and the registry ../contributors.json.  Called by _build_site.py; nothing here is
typed by hand except the prose.

contributors.html: who has contributed and how (a table with a count per kind of contribution, each count a link
into writeups.html filtered to that person), one card per contributor with every target they are credited on, the
project's own share, the scholarship and archives the ledger builds on, the readings that wait for an
independent check (the verification queue), and the partial readings someone could take further, each with the kinds
of gap its NOTES.md lists as open.
"""
import html, collections, datetime, re
import _credits as CR
import _methods as M
from _check_writeup import FAMOUS  # no profile data: kept out of every count here
import _check_writeup as CW

REPO = 'https://github.com/dbourdeau/cyphersolver'
e = lambda s: html.escape(str(s), quote=True)

# columns of the main table: (label, roles counted)
COLUMNS = [('Solutions', ('solution', 'new cipher with solution')), ('New ciphers', ('new cipher', 'new cipher with solution')),
           ('Verifications', ('verification',)), ('Keys corrected', ('key corrected',)),
           ('Transcriptions, identifications', ('transcription', 'identification')), ('Pointers', ('pointer',)),
           ('Keys used', ('key or decipherment used',)), ('Earlier solutions', ('prior solution',))]
QUEUE_METHODS = (M.CT, M.EXT_PT, M.ADJ_PT, M.EXT_KEY)
# NOTES.md "## Remaining gaps" blocker types (_check_writeup.BLOCKERS), as a contributor would put them
GAP_LABEL = {'open-codes': 'code groups open', 'illegible': 'passages hard to read', 'no-key-material': 'no key known',
             'too-short': 'too short to break', 'needs-physical-access': 'needs the archive', 'not-attempted': 'not yet tried',
             'left-open': 'left open'}


def target_link(folder, pages_by_folder, profiles):
    p = pages_by_folder.get(folder)
    if p: return f'<a href="{p["slug"]}.html">{p["title"]}</a>'
    t = e((profiles.get(folder) or {}).get('title') or folder)
    return f'<a href="{REPO}/tree/main/targets/{e(folder)}" rel="noopener">{t}</a> <span class="cmuted">notes</span>'


def name_html(c):
    n = e(c['name'])
    return f'<a href="{e(c["url"])}" rel="noopener">{n}</a>' if c.get('url') else n


def leads(reg):
    """Who runs the project (kind "lead"): shown first, with the project's own targets, not ranked from credits."""
    return [c for c in reg.values() if c.get('kind') == 'lead']


def own_targets(profiles):
    return [f for f, p in profiles.items() if CR.provenance_of(p) == 'project']


# The lead's row splits the project's own targets by outcome, so its cells add up to the Targets count.
OWN_GROUPS = [('Key recovered here', M.KEY_RECOVERED), ('Read with an outside key or decipherment', {M.EXT_KEY, M.KNOWN, M.DECIPH}),
              ('Not solved', {M.NOT}), ('Not applicable', {M.NA})]


def lead_counts(profiles):
    """The project's own targets per OWN_GROUPS label (outcome.method); a missing method shows as 'No outcome yet'."""
    own = [profiles[f] for f in own_targets(profiles)]
    meth = collections.Counter((p.get('outcome') or {}).get('method') for p in own)
    out = {l: sum(meth[m] for m in ms) for l, ms in OWN_GROUPS}
    rest = len(own) - sum(out.values())
    if rest: out['No outcome yet'] = rest
    return out


def lead_row(c, n_own, lc):
    bits = ' &middot; '.join(f'{l.lower()} <b>{n}</b>' for l, n in lc.items() if n)
    return (f'<tr id="row-{c["id"]}"><td><a href="#{c["id"]}">{e(c["name"])}</a> <span class="cmuted">project lead</span></td>'
            f'<td class="n"><a href="writeups.html" title="the project&rsquo;s own targets">{n_own}</a></td>'
            f'<td colspan="{len(COLUMNS)}" class="cmuted">own targets by outcome: {bits}</td></tr>')


def lead_card(c, n_own, lc, n_verified):
    bits = ''.join(f'{l.lower()} &times;{n} &middot; ' for l, n in lc.items() if n)
    return (f'<article class="ccard" id="{c["id"]}">\n<h3>{name_html(c)}</h3>\n'
            + (f'<p class="cnote">{e(c["note"])}</p>\n' if c.get('note') else '')
            + f'<p class="ckinds">project lead &middot; {n_own} of the project&rsquo;s own targets: {bits}'
              f'besides these, {n_verified} outside solutions checked and filed &middot; '
              f'<a href="writeups.html">all write-ups &rarr;</a> &middot; <a href="#project">the project&rsquo;s share</a></p>\n</article>')


def counts(entry, roles):
    return sum(1 for f in entry['targets'] if any(c['role'] in roles for ff, c in entry['items'] if ff == f))


def table_html(rows, reg, first=''):
    head = '<tr><th>Contributor</th><th class="n">Targets</th>' + ''.join(f'<th class="n">{l}</th>' for l, _ in COLUMNS) + '</tr>'
    body = [first] if first else []
    for w, ent in rows:
        cells = ''.join(f'<td class="n">{counts(ent, roles) or "&middot;"}</td>' for _, roles in COLUMNS)
        body.append(f'<tr id="row-{w}"><td><a href="#{w}">{e(reg[w]["name"])}</a></td>'
                    f'<td class="n"><a href="writeups.html#by={w}" title="their write-ups">{len(ent["targets"])}</a></td>{cells}</tr>')
    return f'<div class="tw"><table class="ctable">\n<thead>{head}</thead>\n<tbody>\n' + '\n'.join(body) + '\n</tbody></table></div>'


def card_html(w, ent, reg, pages_by_folder, profiles):
    c = reg[w]
    bits = [f'{CR.ROLE_LABEL[r]} &times;{n}' if n > 1 else CR.ROLE_LABEL[r]
            for r, n in sorted(ent['roles'].items(), key=lambda rn: CR.ROLES.index(rn[0]))]
    gh = ''.join(f' <a class="gh" href="https://github.com/{e(g)}" rel="noopener">@{e(g)}</a>' for g in c.get('github', []))
    items = []
    by_folder = collections.defaultdict(list)
    for f, cr in ent['items']: by_folder[f].append(cr)
    order = sorted(by_folder, key=lambda f: (pages_by_folder.get(f, {}).get('y', 9999), f))
    for f in order:
        roles = []
        for cr in by_folder[f]:
            lab = 'unpublished earlier solution' if cr['role'] == 'prior solution' and cr.get('published') is False else CR.ROLE_LABEL[cr['role']]
            note = f': <span class="cmuted">{e(cr["note"])}</span>' if cr.get('note') else ''
            src = f' <a class="src" href="{e(cr["source"])}" rel="noopener">source</a>' if str(cr.get('source', '')).startswith('http') else ''
            roles.append(f'<b>{lab}</b>{note}{src}')
        items.append(f'<li>{target_link(f, pages_by_folder, profiles)} &mdash; ' + '; '.join(roles) + '</li>')
    more = ''
    if len(items) > 8:
        more = (f'<details class="cmore"><summary>{len(items) - 8} more</summary><ul>' + ''.join(items[8:]) + '</ul></details>')
        items = items[:8]
    return (f'<article class="ccard" id="{w}">\n<h3>{name_html(c)}{gh}</h3>\n'
            + (f'<p class="cnote">{e(c["note"])}</p>\n' if c.get('note') else '')
            + f'<p class="ckinds">{" &middot; ".join(bits)} &middot; <a href="writeups.html#by={w}">their write-ups &rarr;</a></p>\n'
            + '<ul>' + ''.join(items) + '</ul>' + more + '\n</article>')


def queue(pages, profiles):
    """Write-ups whose key was recovered or matched here and that no one outside the project has checked."""
    out = []
    for p in pages:
        if p.get('method') not in QUEUE_METHODS or not p.get('folders'): continue
        if p.get('extent') not in ('complete', 'partial'): continue
        ver = {v for f in p['folders'] for v in ((profiles[f].get('outcome') or {}).get('verification') or [])}
        if 'independent verification' in ver or any(c['role'] == 'verification' for c in p.get('credits') or []): continue
        out.append(p)
    return sorted(out, key=lambda p: (M.METHODS.index(p['method']), p['extent'] != 'complete', p['y']))


def further(pages):
    """Write-ups read in part, each with the blocker types its NOTES.md lists under Remaining gaps, most workable first."""
    out = []
    for p in pages:
        if p.get('extent') != 'partial' or not p.get('folders'): continue
        gaps = collections.Counter(m.lower() for f in p['folders'] if f not in FAMOUS
                                   for m in re.findall(r'^\s*[-*].*?blocker:\s*([a-z-]+)', CW.section(CW.read(CW.tdir(f) / 'NOTES.md'), 'Remaining gaps') or '', re.M | re.I))
        out.append((p, gaps))
    workable = lambda g: -(g['open-codes'] + g['not-attempted'])
    return sorted(out, key=lambda pg: (workable(pg[1]) == 0, pg[0]['y']))


# Progress over time: the targets solved, day by day, stacked by how the text was obtained, against the targets taken on.
START = '2026-09-01'      # the work began in September 2026; an older date in a log is a document's or a source's, not the work's
BREAK_KINDS = {'reading', 'sibling key', 'key from source', 'crib', 'solver'}
SOLVING = M.KEY_METHODS | {M.DECIPH}
# (band, label, .vchart colour slot), bottom of the stack first
SERIES = [('key', 'Key recovered here', 's1'), ('ext', 'Outside key applied', 's2'),
          ('dec', 'Existing decipherment', 's3'), ('con', 'Solved by contributors', 's4')]
PG = dict(W=900, H=340, L=44, R=184, T=22, B=30)


def solve_group(p):
    """The band a solved target goes in; None when no text was obtained (not solved, key only, not applicable)."""
    m = (p.get('outcome') or {}).get('method')
    if m not in SOLVING or M.extent(p) not in ('complete', 'partial'): return None
    if CR.provenance_of(p) == 'contributed': return 'con'
    return 'key' if m in M.KEY_RECOVERED else 'dec' if m == M.DECIPH else 'ext'


def day_of(p, first, today, solved):
    """The day a target was taken on (its first logged step) or solved (its first step that broke or read it, else its
    last step). A log with no full dates falls back to the day its page was first posted."""
    ok = lambda d: isinstance(d, str) and len(d) == 10 and d >= START
    steps = sorted((s for s in p.get('solution') or [] if ok(s.get('date'))), key=lambda s: s['date'])
    if not steps: d = first if ok(first) else None
    elif not solved: d = steps[0]['date']
    else: d = next((s['date'] for s in steps if s.get('kind') in BREAK_KINDS and s.get('result') in ('worked', 'partial')), steps[-1]['date'])
    return min(d, today) if d else None


def spread(labels, gap, lo, hi):
    """Push end labels (y, ...) apart by at least gap, keeping them between lo and hi."""
    labels = sorted(labels)
    for i in range(1, len(labels)):
        if labels[i][0] < labels[i - 1][0] + gap: labels[i] = (labels[i - 1][0] + gap,) + labels[i][1:]
    over = labels[-1][0] - hi if labels else 0
    if over > 0: labels = [(y - over,) + rest for y, *rest in labels]
    return [(max(lo, y),) + tuple(rest) for y, *rest in labels]


def progress(real, pages_by_folder, dates, today):
    """Stat tiles, a running-total / per-day chart (inline SVG, with a small inline script for the hover read-out) and a table."""
    import itertools, json
    solved, taken = collections.defaultdict(collections.Counter), collections.Counter()
    for f, p in real.items():
        first = dates.get(pages_by_folder[f]['slug'], {}).get('first') if f in pages_by_folder else None
        d = day_of(p, first, today, False)
        if d: taken[d] += 1
        g = solve_group(p)
        d = g and day_of(p, first, today, True)
        if d: solved[d][g] += 1
    if not solved: return ''
    d0, d1 = datetime.date.fromisoformat(min([*taken, *solved])), datetime.date.fromisoformat(today)
    iso = [(d0 + datetime.timedelta(i)).isoformat() for i in range((d1 - d0).days + 1)]
    n, keys = len(iso), [k for k, _, _ in SERIES]
    daily = {k: [solved[d][k] for d in iso] for k in keys}
    cum = {k: list(itertools.accumulate(daily[k])) for k in keys}
    tk = list(itertools.accumulate(taken[d] for d in iso))
    tot = [sum(cum[k][i] for k in keys) for i in range(n)]
    dtot = [sum(daily[k][i] for k in keys) for i in range(n)]
    W, H, L, R, T, B = (PG[k] for k in 'WHLRTB')
    pw, ph = W - L - R, H - T - B
    step = 100 if tk[-1] <= 800 else 200
    ymax = -(-max(tk[-1], tot[-1]) // step) * step
    dstep = 10 if max(dtot) <= 80 else 20
    dmax = -(-max(dtot) // dstep) * dstep
    X = lambda i: L + pw * i / max(1, n - 1)
    Y = lambda v, top=ymax: T + ph * (1 - v / top)
    fd = lambda s: f'{datetime.date.fromisoformat(s).day} {datetime.date.fromisoformat(s):%b}'
    pt = lambda x, y: f'{x:.1f},{y:.1f}'

    def axes(top, tick):
        g = ''.join(f'<line class="grid" x1="{L}" x2="{L + pw}" y1="{Y(v, top):.1f}" y2="{Y(v, top):.1f}"/>'
                    f'<text x="{L - 8}" y="{Y(v, top) + 4:.1f}" text-anchor="end">{v}</text>' for v in range(0, top + 1, tick))
        g += ''.join(f'<line class="axis" x1="{X(i):.1f}" x2="{X(i):.1f}" y1="{T + ph}" y2="{T + ph + 5}"/>'
                     f'<text x="{X(i):.1f}" y="{T + ph + 19}" text-anchor="middle">{fd(iso[i])}</text>' for i in range(0, n, 7))
        return g

    # running total: one stacked area per band, the taken-on line behind, a dot at every hundred
    areas, below = [], [0] * n
    for k, lab, cls in SERIES:
        above = [below[i] + cum[k][i] for i in range(n)]
        path = ' '.join(pt(X(i), Y(above[i])) for i in range(n)) + ' ' + ' '.join(pt(X(i), Y(below[i])) for i in reversed(range(n)))
        areas.append(f'<path class="ar {cls}" d="M{path}Z"><title>{lab}</title></path>')
        below = above
    taken_line = f'<path class="tk" d="M{" L".join(pt(X(i), Y(tk[i])) for i in range(n))}"/>'
    ms = []
    for h in range(100, tot[-1] + 1, 100):
        i = next(i for i in range(n) if tot[i] >= h)
        ms.append(f'<g class="ms"><circle cx="{X(i):.1f}" cy="{Y(tot[i]):.1f}" r="4"/>'
                  f'<text x="{X(i) - 8:.1f}" y="{Y(tot[i]) - 8:.1f}" text-anchor="end">{h} solved &middot; {fd(iso[i])}</text></g>')
    ends, base = [], 0
    for k, lab, cls in SERIES:
        ends.append((Y(base + cum[k][-1] / 2), lab, cum[k][-1], cls))
        base += cum[k][-1]
    ends.append((Y(tk[-1]), 'Taken on', tk[-1], 'tkl'))
    lx = L + pw + 10
    end_lab = ''.join(
        (f'<line class="tk" x1="{lx}" x2="{lx + 9}" y1="{y - 4:.1f}" y2="{y - 4:.1f}"/>' if cls == 'tkl' else
         f'<rect class="{cls}" x="{lx}" y="{y - 8.5:.1f}" width="9" height="9" rx="2"/>')
        + f'<text class="lab" x="{lx + 15}" y="{y:.1f}">{lab} <tspan class="v">{v}</tspan></text>'
        for y, lab, v, cls in spread(ends, 15, T + 6, T + ph))
    hit = f'<rect class="hit" x="{L}" y="{T}" width="{pw}" height="{ph}"/>'
    xh = f'<line class="xh" x1="0" x2="0" y1="{T}" y2="{T + ph}"/>'
    svg_cum = (f'<svg class="vchart pg-cum" viewBox="0 0 {W} {H}" role="img" aria-label="Targets solved, running total by day, '
               f'stacked by how the text was obtained: {tot[-1]} solved of {tk[-1]} taken on by {fd(today)}">'
               f'{axes(ymax, step)}<g class="reveal">{taken_line}{"".join(areas)}{"".join(ms)}{end_lab}</g>'
               f'{xh}<circle class="xdot" r="5" cx="0" cy="0"/>{hit}</svg>')

    # per day: stacked bars, the best day labelled
    bw = max(2.0, pw / n * .72)
    bars = []
    for i in range(n):
        if not dtot[i]: continue
        y, segs = dtot[i], []
        for k, lab, cls in reversed(SERIES):
            v = daily[k][i]
            if not v: continue
            top, y = Y(y, dmax), y - v
            segs.append(f'<rect class="{cls}" x="{X(i) - bw / 2:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{max(.5, Y(y, dmax) - top - 1):.1f}"/>')
        bars.append(f'<g class="bar" data-i="{i}">{"".join(segs)}</g>')
    best = max(range(n), key=lambda i: dtot[i])
    best_lab = (f'<text class="lab" x="{X(best) + bw:.1f}" y="{Y(dtot[best], dmax) + 4:.1f}">'
                f'{dtot[best]} in one day, {fd(iso[best])}</text>')
    svg_day = (f'<svg class="vchart pg-day" viewBox="0 0 {W} {H}" role="img" hidden aria-label="Targets solved per day, '
               f'stacked by how the text was obtained; the best day was {fd(iso[best])} with {dtot[best]}">'
               f'{axes(dmax, dstep)}<g class="reveal">{"".join(bars)}{best_lab}</g>{xh}{hit}</svg>')

    # tiles, legend, table
    last7 = sum(dtot[-7:])
    tiles = [(tot[-1], f'targets solved, of {tk[-1]} taken on'), (cum['key'][-1], 'keys recovered here by cryptanalysis'),
             (last7, 'solved in the last seven days'), (dtot[best], f'on the best day, {fd(iso[best])}')]
    tiles_html = ''.join(f'<div class="pg-stat"><b data-n="{v}">{v}</b><span>{t}</span></div>' for v, t in tiles)
    legend = ''.join(f'<span><i class="pg-sw {cls}"></i>{lab}</span>' for _, lab, cls in SERIES) + '<span><i class="pg-sw tkl"></i>Taken on</span>'
    weeks = []
    for w in range(0, n, 7):
        j = min(n, w + 7) - 1
        new = [sum(daily[k][w:j + 1]) for k in keys]
        weeks.append(f'<tr><td>{fd(iso[w])} &ndash; {fd(iso[j])}</td>' + ''.join(f'<td class="n">{v or "&middot;"}</td>' for v in new)
                     + f'<td class="n">{sum(new)}</td><td class="n"><b>{tot[j]}</b></td><td class="n">{tk[j]}</td></tr>')
    table = ('<details class="pg-table"><summary>The figures week by week</summary><div class="tw"><table class="ctable">'
             '<thead><tr><th>Week</th>' + ''.join(f'<th class="n">{lab}</th>' for _, lab, _ in SERIES)
             + '<th class="n">Solved that week</th><th class="n">Solved so far</th><th class="n">Taken on so far</th></tr></thead><tbody>'
             + ''.join(weeks) + '</tbody></table></div></details>')
    data = json.dumps({'d': iso, 's': [daily[k] for k in keys], 'lab': [l for _, l, _ in SERIES], 'cls': [c for _, _, c in SERIES],
                       'tk': tk, 'g': {'W': W, 'L': L, 'pw': pw, 'T': T, 'ph': ph, 'ymax': ymax}}, separators=(',', ':'))
    return f'''<div class="prog" id="pg">
<div class="pg-stats">{tiles_html}</div>
<div class="pg-bar"><div class="pg-legend">{legend}</div>
<div class="pg-mode" role="group" aria-label="Chart view"><button type="button" data-mode="cum" aria-pressed="true">Running total</button><button type="button" data-mode="day" aria-pressed="false">Per day</button></div></div>
<div class="vfig"><div class="pg-plot" tabindex="0" aria-label="Chart: move the pointer, or use the arrow keys, to read a day">
{svg_cum}
{svg_day}
<div class="pg-tip" hidden></div>
</div></div>
<script type="application/json" class="pg-data">{data}</script>
{table}
</div>
<script>{PG_JS}</script>'''


PG_JS = r'''(()=>{const f=document.getElementById('pg');if(!f)return;
const D=JSON.parse(f.querySelector('.pg-data').textContent),g=D.g,n=D.d.length,plot=f.querySelector('.pg-plot'),tip=f.querySelector('.pg-tip');
const cum=D.s.map(a=>{let t=0;return a.map(v=>t+=v)}),svg={cum:f.querySelector('.pg-cum'),day:f.querySelector('.pg-day')};
let mode='cum',cur=n-1;const X=i=>g.L+g.pw*i/Math.max(1,n-1);
const fmt=s=>new Date(s+'T12:00:00').toLocaleDateString('en-GB',{weekday:'short',day:'numeric',month:'short'});
function show(i){cur=i;const s=svg[mode],x=X(i),xh=s.querySelector('.xh');xh.setAttribute('x1',x);xh.setAttribute('x2',x);s.classList.add('hov');
 const v=D.s.map((a,k)=>mode==='cum'?cum[k][i]:a[i]),t=v.reduce((a,b)=>a+b,0);
 if(mode==='cum'){const d=s.querySelector('.xdot');d.setAttribute('cx',x);d.setAttribute('cy',g.T+g.ph*(1-t/g.ymax))}
 else s.querySelectorAll('.bar').forEach(b=>b.classList.toggle('on',+b.dataset.i===i));
 tip.innerHTML='<b>'+fmt(D.d[i])+'</b>'+v.map((x,k)=>[x,k]).reverse().map(([x,k])=>'<span><i class="pg-sw '+D.cls[k]+'"></i>'+D.lab[k]+'<em>'+x+'</em></span>').join('')
  +'<span class="t">'+(mode==='cum'?'Solved so far':'Solved that day')+'<em>'+t+'</em></span>'+(mode==='cum'?'<span class="k"><i class="pg-sw tkl"></i>Taken on so far<em>'+D.tk[i]+'</em></span>':'');
 tip.hidden=false;const w=s.getBoundingClientRect().width,px=x/g.W*w;
 tip.style.left=(px>w*.55?px-tip.offsetWidth-14:px+14)+'px'}
function hide(){svg[mode].classList.remove('hov');tip.hidden=true;svg.day.querySelectorAll('.bar.on').forEach(b=>b.classList.remove('on'))}
plot.addEventListener('pointermove',e=>{const r=svg[mode].getBoundingClientRect(),sx=(e.clientX-r.left)*g.W/r.width;
 show(Math.max(0,Math.min(n-1,Math.round((sx-g.L)/g.pw*(n-1)))))});
plot.addEventListener('pointerleave',hide);plot.addEventListener('blur',hide);
plot.addEventListener('keydown',e=>{const k={ArrowLeft:-1,ArrowRight:1}[e.key];
 if(k){show(Math.max(0,Math.min(n-1,cur+k)));e.preventDefault()}else if(e.key==='Home'||e.key==='End'){show(e.key==='Home'?0:n-1);e.preventDefault()}});
f.querySelectorAll('.pg-mode button').forEach(b=>b.addEventListener('click',()=>{hide();mode=b.dataset.mode;
 f.querySelectorAll('.pg-mode button').forEach(o=>o.setAttribute('aria-pressed',o===b));svg.cum.toggleAttribute('hidden',mode!=='cum');svg.day.toggleAttribute('hidden',mode!=='day');
 if(f.classList.contains('go')){const r=svg[mode].querySelector('.reveal');r.style.animation='none';r.getBoundingClientRect();r.style.animation=''}}));
if(matchMedia('(prefers-reduced-motion: reduce)').matches||!('IntersectionObserver' in window))return;
f.classList.add('pre');const io=new IntersectionObserver(es=>{if(!es.some(e=>e.isIntersecting))return;io.disconnect();f.classList.add('go');
 const t0=performance.now(),els=[...f.querySelectorAll('.pg-stat b')];
 (function tick(t){const p=Math.min(1,(t-t0)/1400),q=1-Math.pow(1-p,3);els.forEach(e=>e.textContent=Math.round(e.dataset.n*q));if(p<1)requestAnimationFrame(tick)})(t0)},{threshold:.3});
io.observe(plot)})();'''


def page(pages, profiles, reg, dates, version, today):
    t = CR.tally(profiles, reg)
    pages_by_folder = {f: p for p in pages for f in p.get('folders', [])}
    ranked = CR.ranked(t, reg)
    direct = [(w, ent) for w, ent in ranked if CR.direct_score(ent)]
    lead = leads(reg)
    n_people = len(ranked) + len(lead)
    n_credits = sum(len(ent['items']) for w, ent in t.items())
    n_direct = sum(CR.direct_score(ent) for w, ent in ranked)
    # the project's share
    real = {f: p for f, p in profiles.items() if f not in FAMOUS}
    own = own_targets(real)
    lc = lead_counts(real)
    own_keys = sum(1 for f in own if (real[f].get('outcome') or {}).get('method') in M.KEY_RECOVERED)
    contrib = sorted(f for f, p in real.items() if CR.provenance_of(p) in ('contributed', 'mixed'))
    models = collections.Counter(m for p in real.values() for m in ((p.get('conditions') or {}).get('models') or []) if isinstance(m, str) and m != 'unknown')
    # scholarship and archives
    builds = sorted([(w, ent) for w, ent in t.items() if reg[w]['kind'] in ('historical', 'archive', 'database')],
                    key=lambda we: (-len(we[1]['targets']), we[0]))     # ties by id: same order on every OS
    q = queue(pages, profiles)
    fq = further(pages)
    pg = progress(real, pages_by_folder, dates, today)
    # by month: direct contributions from outside, dated by the credit or the page
    months = collections.Counter()
    for w, ent in ranked:
        for f, c in ent['items']:
            if c['role'] not in CR.DIRECT: continue
            d = c.get('date') or (dates.get(pages_by_folder[f]['slug'], {}).get('first') if f in pages_by_folder else '')
            if d and len(d) >= 7 and d[:4] >= '2026': months[d[:7]] += 1
    hist = ''
    if months:
        top = max(months.values())
        hist = ('<div class="cmonths">' + ''.join(
            f'<div><span class="bar" style="height:{max(6, round(64 * n / top))}px" title="{n}"></span><b>{n}</b>'
            f'<i>{datetime.date(int(m[:4]), int(m[5:7]), 1):%b %Y}</i></div>' for m, n in sorted(months.items())) + '</div>')
    queue_rows = ''.join(
        f'<li><a href="{p["slug"]}.html"><span class="st {p["st"]}">{p["stt"]}</span><span class="t">{p["title"]}</span>'
        f'<span class="yr">{p["year"]}</span></a></li>' for p in q)
    further_rows = ''.join(
        f'<li><a href="{p["slug"]}.html"><span class="st {p["st"]}">{p["stt"]}</span><span class="t">{p["title"]}</span>'
        f'<span class="yr">{p["year"]}</span>'
        + (f'<span class="b">Open: {", ".join(GAP_LABEL.get(b, b) + (f" ({n})" if n > 1 else "") for b, n in g.most_common())}</span>' if g else '')
        + '</a></li>' for p, g in fq)
    n_verified = sum(CR.provenance_of(p) == 'contributed' for p in real.values())
    credited = {f for w, ent in ranked for f in ent['targets']}
    n_overlap = len(credited & set(own))
    cards = '\n'.join([lead_card(c, len(own), lc, n_verified) for c in lead] + [card_html(w, ent, reg, pages_by_folder, profiles) for w, ent in ranked])
    builds_rows = ''.join(
        f'<tr id="{w}"><td>{name_html(reg[w])}<span class="cmuted"> {e(reg[w].get("note", ""))}</span></td>'
        f'<td class="n"><a href="writeups.html#by={w}">{len(ent["targets"])}</a></td></tr>' for w, ent in builds)
    model_txt = ', '.join(f'{e(m)}' for m, _ in models.most_common(4))
    contrib_txt = (f' {len(contrib)} target{"s" if len(contrib) != 1 else ""} came wholly or partly from outside contributors '
                   f'and are marked as such: they are left out of the LLM-performance figures.') if contrib else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contributors &mdash; who has added to the ledger, and how</title>
<meta name="description" content="Everyone credited in the ledger of historical ciphers: solutions, new ciphers, verifications, key corrections and pointers, with the keys and decipherments the work builds on.">
<link rel="stylesheet" href="style.css?v={version}">
</head>
<body id="top">
<!-- site:nav -->

<section class="hero">
  <p class="kicker">Contributors &middot; {n_people} people &middot; {n_credits} credits</p>
  <h1>Contributors</h1>
  <p class="sub">The ledger is a shared project. Anyone can add to it: a solution to a cipher already listed, a reading left partial taken further, a new unsolved cipher, a new cipher with its solution, or an independent check of a reading already here. Every write-up names who contributed and whose keys or decipherments it used; this page adds them up.</p>
  <div class="jump"><a href="contribute.html">How to contribute</a><a href="#progress">Progress</a><a href="#who">Who</a><a href="#people">Contributions in detail</a><a href="#builds-on">What the work builds on</a><a href="#verify">Waiting for a check</a><a href="#further">Readings to take further</a></div>
  <p class="meta">Daniel Bourdeau and contributors</p>
</section>

<main>

<h2 id="progress"><span class="num">01</span> Progress</h2>
<p>Every target solved since the work began, day by day. A target counts as solved when its text was obtained, in full or in part, however that was done; the bands say how. The day is the first step in the target&rsquo;s solution log that broke or read it, or the day its page went up when the log has no dates. The dashed line is every target taken on, solved or not. Hover or use the arrow keys to read a day; switch to <i>Per day</i> to see the bursts.</p>
{pg}

<h2 id="who"><span class="num">02</span> Who has contributed</h2>
<p>{"".join(e(c["name"]) + " runs the project (" + str(len(own)) + " of its own targets). " for c in lead)}{len(ranked)} people are credited on {len(credited)} targets; {n_overlap} of those are also among the project&rsquo;s own, credited because a reading there used their key, decipherment or pointer, so the two figures overlap and do not add up to the total. {n_direct} of the credits are direct contributions (a solution, a new cipher, a verification, a key correction, a transcription, an identification or a pointer to a source); the rest record whose key, decipherment or earlier solution a reading used. A count is the number of targets; click it for the write-ups.</p>
{table_html(ranked, reg, ''.join(lead_row(c, len(own), lc) for c in lead))}
<p class="cmuted">The project lead&rsquo;s row splits the {len(own)} own targets by outcome. The {n_verified} outside solutions checked and filed here are counted under their contributors, not in that row.</p>
{('<h3 class="listhead">Direct contributions by month</h3>' + hist) if hist else ''}

<h2 id="people"><span class="num">03</span> Contributions in detail</h2>
<p>Each contributor with every target they are credited on, and for what. An earlier solution that was never published is marked as unpublished and is credited only with the solver&rsquo;s agreement.</p>
<div class="ccards">
{cards}
</div>

<h2 id="project"><span class="num">04</span> The project</h2>
<p>The rest of the work is the project&rsquo;s own: Daniel Bourdeau chose and checked the targets, and the transcription, cryptanalysis and write-ups were done with Anthropic&rsquo;s Claude models in Claude Code ({model_txt}). Of {len(real)} profiled targets, {len(own)} are the project&rsquo;s own results, and {own_keys} of them recovered a key by cryptanalysis.{contrib_txt} The project&rsquo;s share is not ranked above: the table is for contributors.</p>

<h2 id="builds-on"><span class="num">05</span> What the work builds on</h2>
<p>Keys and decipherments made at the time, earlier editions, and the databases the images and records come from. Most targets were taken from <a href="https://cryptiana.web.fc2.com/code/unsolved.htm">Satoshi Tomokiyo&rsquo;s catalogue</a>, <a href="https://elonka.com/UnsolvedCodes.html">Elonka Dunin&rsquo;s list</a> and <a href="https://scienceblogs.de/klausis-krypto-kolumne/the-top-50-unsolved-encrypted-messages/">Klaus Schmeh&rsquo;s Top 50</a>; a listing alone is not counted as a credit.</p>
<div class="tw"><table class="ctable narrow"><thead><tr><th>Source</th><th class="n">Targets</th></tr></thead><tbody>{builds_rows}</tbody></table></div>

<h2 id="verify"><span class="num">06</span> Waiting for an independent check</h2>
<p>{len(q)} readings whose key was recovered or matched here and that no one outside the project has checked yet. A check means taking the images and the key on the write-up, deciphering a passage independently, and reporting what agrees and what does not. It is the most useful contribution after a solution; <a href="contribute.html#verify">how to send one</a>.</p>
<ul class="list wl cqueue">
{queue_rows}
</ul>

<h2 id="further"><span class="num">07</span> Readings to take further</h2>
<p>{len(fq)} write-ups are read in part. Each lists what is still open in its notes: code groups with no value yet, passages hard to read on the images, letters for which no key is known, pieces that need the original in the archive. Any of these can be pushed towards a fuller reading: a value for a code group, a better reading of a line, a key found in another volume, a look at the manuscript. Those with open code groups come first, as the most workable from the images alone; <a href="contribute.html#further">how to send it</a>. Each one also has its own page with its gaps and instructions to hand an AI agent: <a href="further.html">Read further</a>. Gaps that need the original or a book out of reach are listed by archive on <a href="archives.html">To the archive</a>, for anyone who can visit or order. The same list, with the summaries, is <a href="writeups.html#extent=partial">on the write-ups page</a>.</p>
<ul class="list wl cqueue">
{further_rows}
</ul>

</main>
<!-- site:footer -->
</body>
</html>
'''


def helpband(pages, profiles):
    """The landing page's three ways to help, each behind its nav sticker, between <!-- help:start/end -->."""
    import _archives_page as AR, _catalogue_page as C
    still_open = sum(1 for x in C.DATA['entries'] if C.is_open(x))
    fn = sum(p.get('extent') == 'partial' and bool(p.get('folders')) for p in pages)
    na = sum(r['status'] in AR.LIVE for r in AR.load())
    q = len(queue(pages, profiles))
    def way(href, sticker, cls, count, what, how):
        return (f'<a class="hb-way" href="{href}"><span class="sticker{cls}" aria-hidden="true"><span><b>{sticker}</b></span></span>'
                f'<span class="hb-t"><b>{count:,}</b> {what}</span><span class="hb-d">{how}</span></a>')
    return f'''<!-- help:start -->
<section class="helpband" id="help" aria-labelledby="hb-h">
<h2 id="hb-h">Three ways to help</h2>
<div class="hb-grid">
{way('catalogue.html', 'Help<br>Solve!', '', still_open, 'ciphers with no known decipherment', 'Pick one and try it, by hand or with an AI agent: each has instructions to hand over.')}
{way('further.html', 'Finish<br>It!', ' alt', fn, 'readings left partial', 'A value for a code group, a better reading of a line, a key found in another volume.')}
{way('archives.html', 'Go<br>Look!', ' arc', na, 'pieces that need an archive', 'A visit, a reproduction order or a library loan, listed by archive.')}
</div>
<p class="hb-more">Or <a href="contributors.html#verify">check one of {q} readings</a> waiting for an independent check, or <a href="contribute.html#new">send a cipher that is not listed</a>. Every contribution is credited. <a class="btn" href="contribute.html">How to contribute &rarr;</a></p>
</section>
<!-- help:end -->'''


SOURCES = ('''<a href="https://cryptiana.web.fc2.com/code/unsolved.htm">Tomokiyo&rsquo;s catalogue</a>, the <a href="https://de-crypt.org/">DECODE</a> database, '''
           '''<a href="https://cryptoole.satoru.net/">Cryptoole</a>, <a href="https://crypto.hcportal.eu/">HCPortal</a>, sweeps of <a href="https://gallica.bnf.fr/">Gallica</a>, '''
           '''the <a href="https://www.nationaalarchief.nl/">Nationaal Archief</a>, the <a href="https://www.siv.archives-nationales.culture.gouv.fr/">Archives nationales</a> and '''
           '''<a href="https://francearchives.gouv.fr/">FranceArchives</a>, and <a href="https://sok.riksarkivet.se/">Riksarkivet</a>, calendars and printed editions, '''
           '''<a href="https://mysterytwister.org/">MysteryTwister</a>, <a href="https://elonka.com/UnsolvedCodes.html">Elonka Dunin&rsquo;s famous-codes list</a>, '''
           '''<a href="https://scienceblogs.de/klausis-krypto-kolumne/the-top-50-unsolved-encrypted-messages/">Schmeh&rsquo;s Top 50</a> and the contributors.''')


def strip(pages, profiles, reg, n=8):
    """The landing page's contributors and sources, between <!-- contrib:start/end -->."""
    t = CR.tally(profiles, reg)
    ranked = CR.ranked(t, reg)[:n]
    chips = ''.join(
        f'<li><a href="contributors.html#{w}"><b>{e(reg[w]["name"])}</b><span>{len(ent["targets"])} target{"s" if len(ent["targets"]) != 1 else ""}'
        + (f' &middot; {CR.direct_score(ent)} direct' if CR.direct_score(ent) else '') + '</span></a></li>' for w, ent in ranked)
    n_own = len(own_targets({f: p for f, p in profiles.items() if f not in FAMOUS}))
    chips = ''.join(
        f'<li><a href="contributors.html#{c["id"]}"><b>{e(c["name"])}</b><span>project lead &middot; {n_own} targets</span></a></li>'
        for c in leads(reg)) + chips
    return f'''<!-- contrib:start -->
<section class="contribstrip" id="contributors" aria-labelledby="cs-h">
<h2 id="cs-h">Contributors and sources</h2>
<div class="cs-grid">
<div class="cs-top">
<h3>Top contributors</h3>
<ol class="cs-people">{chips}</ol>
<p class="cs-all"><a href="contributors.html">All contributors and what each added &rarr;</a></p>
</div>
<div class="cs-top">
<h3>Where the targets come from</h3>
<p class="cs-src">{SOURCES}</p>
</div>
</div>
</section>
<!-- contrib:end -->'''
