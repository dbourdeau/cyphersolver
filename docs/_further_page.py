"""Build docs/further.html and docs/further/<slug>.html: the readings left partial, and what a helper (or the helper's
AI agent) can do to take each one further.

The list is the write-ups whose extent is partial (PAGES, from profile.json), with the open pieces each one's NOTES.md
lists under "## Remaining gaps" (one bullet per piece, "blocker: <type>", _check_writeup.BLOCKERS) and the
"## Escalation" checklist. further.html is a thin table, most workable first; each row opens the reading's own page,
which carries a plain-text task to hand an agent with one URL (same pattern as the catalogue's docs/solve/ pages).

Called from _build_site.py: build_html(PAGES) before the pages are processed (so further.html gets the nav and
footer like any page), build_pages(PAGES) after (the per-reading pages copy that shell from the built further.html).
"""
import html, json, pathlib, re
from urllib.parse import urlencode
import _check_writeup as CW
import _methods as M

HERE = pathlib.Path(__file__).parent
SITE = 'https://dbourdeau.github.io/cyphersolver/'
REPO = 'https://github.com/dbourdeau/cyphersolver'
# blocker types as a contributor would put them; the first three can be done now from what is online, the rest need a new source
GAP_LABEL = {'open-codes': 'code groups open', 'not-attempted': 'not yet tried', 'left-open': 'left open',
             'illegible': 'hard to read on the scan', 'no-key-material': 'no key known', 'too-short': 'too short to break',
             'needs-physical-access': 'needs the archive'}
WORKABLE = {'open-codes', 'not-attempted', 'left-open'}


def esc(t):
    return html.escape(str(t), quote=False)


def plain(h):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', h or ''))).strip()


def bullets(text):
    """Top-level '- ' bullets of a NOTES section, continuation lines joined."""
    out = []
    for line in (text or '').splitlines():
        if re.match(r'^[-*]\s', line): out.append(line[2:].strip())
        elif out and line.startswith((' ', '\t')) and line.strip(): out[-1] += ' ' + line.strip()
    return out


def gaps_of(folder):
    """[(text, blocker)] for the open pieces in NOTES.md "## Remaining gaps"; pieces marked closed carry no blocker."""
    out = []
    for b in bullets(CW.section(CW.read(CW.tdir(folder) / 'NOTES.md'), 'Remaining gaps')):
        m = re.search(r'blocker:\s*([a-z-]+)', b, re.I)
        if m: out.append((b, m.group(1).lower()))
    return out


def escalation_of(folder):
    """[(done, step, text)] from NOTES.md "## Escalation"."""
    out = []
    for b in bullets(CW.section(CW.read(CW.tdir(folder) / 'NOTES.md'), 'Escalation')):
        m = re.match(r'\[([ xX])\]\s*([\w-]+)\s*:?\s*(.*)', b)
        if m: out.append((m.group(1).lower() == 'x', m.group(2), m.group(3)))
    return out


def entries(pages):
    out = []
    for p in pages:
        if p.get('extent') != 'partial' or not p.get('folders'): continue
        fs = [f for f in p['folders'] if f not in CW.FAMOUS and (CW.tdir(f) / 'NOTES.md').is_file()]
        if not fs: continue
        gaps = [(f, t, b) for f in fs for t, b in gaps_of(f)]
        try: frac = float(p.get('frac')) if p.get('frac') not in (None, '') else None
        except ValueError: frac = None
        out.append(dict(p=p, folders=fs, gaps=gaps, frac=frac, work=sum(b in WORKABLE for _, _, b in gaps),
                        esc=[(f,) + x for f in fs for x in escalation_of(f)]))
    return sorted(out, key=lambda e: (e['work'] == 0, -(e['frac'] or 0), e['p']['slug']))


def href(e):
    return f'further/{e["p"]["slug"]}.html'


def chips(e):
    n = {}
    for _, _, b in e['gaps']: n[b] = n.get(b, 0) + 1
    order = sorted(n, key=lambda b: (b not in WORKABLE, -n[b]))
    return ''.join(f'<span class="gap{" w" if b in WORKABLE else ""}">{esc(GAP_LABEL.get(b, b))}{f" ×{n[b]}" if n[b] > 1 else ""}</span>' for b in order) \
        or '<span class="gap">no gaps listed</span>'


def share(e):
    """The share read, one decimal; a partial reading never shows 100% (whole letters or pages may be untouched)."""
    return f'{min(e["frac"] * 100, 99.9):.1f}%'


def pct(e):
    return share(e) if e['frac'] is not None else '&ndash;'


def row(e):
    p = e['p']
    first = plain(e['gaps'][0][1]) if e['gaps'] else 'See the notes for what is open.'
    first = re.sub(r'\s*[-–—]\s*blocker:.*$', '', first)
    sort = (f'data-frac="{e["frac"] if e["frac"] is not None else -1}" data-y="{p["y"]}" data-gaps="{len(e["gaps"])}" '
            f'data-title="{html.escape(plain(p["title"]).lower())}"')
    return (f'<tr class="e" data-href="{href(e)}" data-work="{e["work"]}" {sort}>'
            f'<td class="prio"><b>{pct(e)}</b></td>'
            f'<td class="date">{p["year"]}</td>'
            f'<td class="item"><a class="t" href="{href(e)}">{p["title"]}</a><span class="pill">{p["stt"]}</span><span class="sub">Open: {esc(first)}</span></td>'
            f'<td class="gaps">{chips(e)}</td></tr>')


def build_html(pages):
    E = entries(pages)
    n_work = sum(1 for e in E if e['work'])
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Read Further — {len(E)} readings left partial</title>
<meta name="description" content="{len(E)} historical cipher readings left partial, each with its open gaps and instructions to hand to an AI agent to take it further.">
<link rel="stylesheet" href="style.css">
</head>
<body id="top" class="nojs">
<!-- site:nav -->

<section class="hero">
  <p class="kicker">{len(E)} readings left partial · {n_work} with gaps you can close now from what is online</p>
  <h1>Read <span class="stk">Further<a class="sticker alt" href="#list" title="Pick a reading below"><span><b>Finish<br>It!</b><small>pick a gap</small></span></a></span></h1>
  <p class="sub">Ciphers read in part: the key works, but code groups, names, passages or whole letters are still open. Pick one, open its page, and give that page&rsquo;s address to your AI agent: the page lists every open gap, what has already been tried, and the instructions.</p>
  <ol class="steps"><li><b>1</b>pick a reading</li><li><b>2</b>open its page</li><li><b>3</b>point your agent at the URL</li><li><b>4</b>send back one closed gap</li></ol>
</section>

<main>
<div class="qbar jsonly" id="list">
  <input type="search" id="q" placeholder="Search: name, place, year, kind of gap…" aria-label="Search the readings">
  <label class="only"><input type="checkbox" id="work"> only readings you can push further now</label>
  <select id="msort" aria-label="Sort the readings"><option value="work">Most to do now</option><option value="frac">Most read</option><option value="y">Oldest first</option><option value="title">Title A–Z</option></select>
  <span class="count" id="count"></span>
</div>
<div class="tw"><table class="cat fur" id="cat">
<colgroup><col class="c-prio"><col class="c-date"><col class="c-item"><col class="c-gaps"></colgroup>
<thead><tr><th class="prio" data-sort="frac" title="sort by share read">Read</th><th data-sort="y" title="sort by date">Date</th><th data-sort="title" title="sort by title">Reading</th><th data-sort="work" aria-sort="descending" title="sort by gaps you can close now, then all gaps">Open gaps</th></tr></thead>
<tbody>
{"".join(row(e) for e in E)}
</tbody></table></div>
<div class="legend"><span>click a column to sort, a row for its page</span><span>Read: share of the cipher tokens that give sense now</span><span><span class="gap w">gold</span> can be done now: the images and the key are online</span><span><span class="gap">grey</span> needs a new source first: a key, a better scan, an edition or the archive (<a href="archives.html">archive requests, by archive</a>)</span></div>

<h2>What counts as further</h2>
<p>One closed gap is a contribution: a value for a code group with every place it occurs, a passage re-read at the image, a key or a clear copy found in another volume or in print, a photograph from the archive. A reading becomes <b>complete</b> when at least 95% of its cipher tokens give sense, measured from a reading file, no gap is left untried, every letter is covered, and what stays open is scattered code groups or pieces blocked from outside (README, Conventions). Each step is credited on the write-up. How to send it: <a href="contribute.html#further">contribute</a>.</p>
</main>
<!-- site:footer -->
<script>
(function(){{
document.body.classList.remove('nojs');
var rows=[].slice.call(document.querySelectorAll('#cat tr.e')),q=document.getElementById('q'),w=document.getElementById('work'),c=document.getElementById('count');
function render(){{var s=q.value.trim().toLowerCase(),n=0;rows.forEach(function(r){{var ok=(!s||r.textContent.toLowerCase().indexOf(s)>=0)&&(!w.checked||r.dataset.work!=='0');r.hidden=!ok;if(ok)n++;}});c.textContent=n+' of '+rows.length+' readings';}}
rows.forEach(function(r){{r.addEventListener('click',function(ev){{if(ev.target.closest('a'))return;if(ev.ctrlKey||ev.metaKey)window.open(r.dataset.href);else location.href=r.dataset.href;}});}});
var tb=document.querySelector('#cat tbody'),hs=[].slice.call(document.querySelectorAll('#cat th[data-sort]')),srt={{k:'work',d:-1}};
function val(r,k){{if(k==='title')return r.dataset.title;if(k==='work')return (+r.dataset.work)*1000+(+r.dataset.gaps);return +r.dataset[k];}}
var ms=document.getElementById('msort');
function sortBy(k,keep){{srt.d=keep?(k==='title'||k==='y'?1:-1):srt.k===k?-srt.d:(k==='title'||k==='y'?1:-1);srt.k=k;ms.value=k;
 rows.slice().sort(function(a,b){{if(k==='frac'&&(a.dataset.frac==='-1')!==(b.dataset.frac==='-1'))return a.dataset.frac==='-1'?1:-1;var x=val(a,k),y=val(b,k);return x<y?-srt.d:x>y?srt.d:(+b.dataset.frac)-(+a.dataset.frac);}}).forEach(function(r){{tb.appendChild(r);}});
 hs.forEach(function(h){{h.setAttribute('aria-sort',h.dataset.sort===k?(srt.d<0?'descending':'ascending'):'none');}});}}
hs.forEach(function(h){{h.addEventListener('click',function(){{sortBy(h.dataset.sort);}});}});
ms.addEventListener('change',function(){{sortBy(ms.value,true);}});
q.addEventListener('input',render);w.addEventListener('change',render);render();
}})();
</script>
</body>
</html>
'''
    (HERE / 'further.html').write_text(page, encoding='utf-8')
    return len(E)


def issue_url(e):
    p = e['p']
    return f'{REPO}/issues/new?' + urlencode({'template': 'further-reading.yml', 'title': f'Further reading: {p["slug"]}',
                                              'page': f'{p["slug"]}.html'})


def agent_text(e):
    p, fs = e['p'], e['folders']
    url = SITE + href(e)
    lines = [f'TASK: take a partial decipherment further: {plain(p["title"])}',
             f'This page: {url}',
             '',
             'You are helping a public research project finish reading historical cipher letters. This one is read in part:',
             'the key works, but some pieces are still open. Your job is to close one or more of the open gaps below.',
             '',
             'THE READING',
             f'  Write-up:   {SITE}{p["slug"]}.html (read it first: how the text was read, the key, the reading)',
             f'  Date:       {plain(p["year"])}',
             f'  Outcome:    {plain(p["stt"])}',
             f'  Read now:   {share(e)} of the deciphered cipher tokens give sense (pieces below may be untouched)' if e['frac'] is not None else '  Read now:   not measured']
    for f in fs:
        lines.append(f'  Files:      {REPO}/tree/main/targets/{f} (NOTES.md, key, transcription, reading, scripts)')
    lines += ['', 'OPEN GAPS (from NOTES.md, "## Remaining gaps")']
    if e['gaps']:
        for i, (f, t, b) in enumerate(e['gaps'], 1):
            kind = 'doable now' if b in WORKABLE else 'needs a new source'
            lines.append(f'  {i}. [{b}: {kind}] {plain(t)}')
    else:
        lines.append('  None listed: read the notes and the write-up for what is open.')
    if e['esc']:
        lines += ['', 'ALREADY TRIED (from NOTES.md, "## Escalation")']
        lines += [f'  [{"x" if d else " "}] {k}: {plain(t)}' for _, d, k, t in e['esc']]
    folder = f'targets/{fs[0]}/'
    lines += ['',
              'STEPS',
              '0. Set up. If you can run a shell, fork and clone the repository and work inside it:',
              f'     git clone {REPO}.git',
              '   Then read, in this order: CONTRIBUTING.md (how a contribution is sent and credited); README.md, sections',
              f'   "Repository layout" and "Conventions" (how readings are measured and named); {folder}NOTES.md in full, and the',
              '   key, transcription and reading files it names; lang/README.md (shared language models).',
              f'   Work in {folder}. Add your findings to NOTES.md under a dated heading without rewriting what is there, and',
              '   update the "## Remaining gaps" line of every gap you close. Keep WORKLOG.md there: one dated line per step',
              '   (hypothesis, value tried, solver run, crib, control), failures included. Do not edit docs/ (the site is generated).',
              '   If you cannot run a shell, fetch the files from the links above and keep your work in files you send with the issue.',
              '1. Pick a gap. Start with the ones marked "doable now" (open-codes, not-attempted, left-open): the images and the key',
              '   are online, so they need only work. A gap marked "needs a new source" (no-key-material, too-short, illegible,',
              '   needs-physical-access) can be closed only by something new: a key',
              '   or a deciphered sibling found elsewhere, a better image, a printed edition or calendar, a photograph from the archive.',
              '   For those, search for that material first, and say where you looked even when you find nothing.',
              '2. Start from the existing key and transcription in the folder. Do not rebuild the key from scratch, and do not',
              '   re-read parts that are already read unless you find an error in them.',
              '3. For a code group or sign value: list every place the group occurs, show how each reads with the value you propose,',
              '   and say what still does not fit. For a passage: re-read it at the image and give the folio and line. For a missing',
              '   letter or leaf: say where it is held and how it can be reached.',
              '4. Measure again. Apply the key to the whole text, write the reading file, and count the share of cipher tokens that',
              '   give sense (not an estimate). The reading is "complete" only when (1) at least 95% of its cipher tokens give sense;',
              '   (2) no gap is left untried; (3) every letter in it is covered; (4) what stays open is scattered code groups or names,',
              '   or pieces blocked from outside. Otherwise it stays "partial": say which gaps are still open and why.',
              '5. Be honest. Mark every uncertain word with [?], leave unread groups as their numbers or signs, and never fill a gap',
              '   with a plausible guess. A gap retried and still open, with what was ruled out, is worth reporting.',
              '',
              'REPORT BACK',
              f'With a clone: open a pull request with your changes to {folder}. Say in the description which gaps you worked on,',
              '  the share read before and after, and how you want to be credited (name, initials or handle, and a link).',
              f'Without one: open an issue: {issue_url(e)}',
              '  Give the write-up, the gap you worked on (its line in Remaining gaps, or the code group, folio and line), what you',
              '  propose, the evidence (every occurrence, the images or sources), the share read before and after, your step log,',
              '  and the tools and AI model you used.',
              'If you cannot open issues or pull requests, write this report for your human to send. Credit goes to the person who sends it.']
    return '\n'.join(lines)


SOLVE_JS = ('<script>(function(){var b=document.querySelector(\'.agentbox .copy\'),p=document.getElementById(\'agent\');if(!b||!p)return;'
            'b.addEventListener(\'click\',function(){var t=p.textContent;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject())'
            '.then(function(){b.textContent=\'Copied\';setTimeout(function(){b.textContent=\'Copy\';},1600);},'
            'function(){var r=document.createRange();r.selectNodeContents(p);var s=getSelection();s.removeAllRanges();s.addRange(r);});});})();</script>')


def archive_html(e):
    """The reading's open archive requests (archive_requests.json), so a visitor near the archive can take one."""
    import _archives_page as AR
    rs = [r for f in e['folders'] for r in AR.requests_for(f)]
    if not rs: return ''
    def take(r):
        return f', <a href="{html.escape(AR.issue_url(r))}" rel="noopener">I can do this</a>' if r['status'] == 'open' else ''
    li = ''.join(f'<li><b>{r["id"]}</b> {esc(r["archive"])}{(", " + esc(r["city"])) if r.get("city") else ""}: {esc(r["need"])} '
                 f'({AR.STATUS[r["status"]]}{take(r)})</li>' for r in rs)
    return (f'<h2>Needs the archive</h2><p>These gaps can only be closed from the original or a book out of reach. '
            f'If you can visit or order, take one: <a href="archives.html">all archive requests</a>.</p><ul class="gaplist">{li}</ul>')


def one_page(e, shell):
    p = e['p']
    url = SITE + href(e)
    gaps = ''.join(f'<li><span class="gap{" w" if b in WORKABLE else ""}">{esc(GAP_LABEL.get(b, b))}</span> {esc(plain(t))}</li>' for _, t, b in e['gaps']) \
        or '<li>None listed in the notes.</li>'
    escl = ''.join(f'<li>{"&#9745;" if d else "&#9744;"} <b>{esc(k)}</b> {esc(plain(t))}</li>' for _, d, k, t in e['esc'])
    files = ' · '.join(f'<a href="{REPO}/tree/main/targets/{f}" rel="noopener">targets/{f}</a>' for f in e['folders'])
    body = f'''<section class="hero">
  <p class="kicker"><a href="further.html">Read further</a> · read {pct(e)} · {p["stt"]}</p>
  <h1>{p["title"]}</h1>
  <p class="sub">{p.get("blurb") or ""}</p>
  <dl class="facts">
    <dt>Date</dt><dd>{p["year"]}</dd>
    <dt>Read now</dt><dd>{pct(e)} of the cipher tokens give sense</dd>
    <dt>Write-up</dt><dd><a href="{p["slug"]}.html">{p["slug"]}.html</a></dd>
    <dt>Files</dt><dd>{files}</dd>
    <dt>Open gaps</dt><dd>{chips(e)}</dd>
  </dl>
</section>

<main>
<h2>Hand this page to your AI agent</h2>
<p>Give your agent (Claude, ChatGPT or any assistant that can open web pages) this address and ask it to do the task on the page:</p>
<p class="urlline">{url}</p>
<p>Or copy the block below into the chat. It is the whole task: the reading, every open gap, what has been tried, the steps, and how to report back.</p>
<div class="agentbox"><span class="sticker alt" aria-hidden="true"><span><b>Finish<br>It!</b><small>give this to your agent</small></span></span><button type="button" class="copy">Copy</button><pre id="agent">{html.escape(agent_text(e), quote=False)}</pre></div>

<h2>Open gaps</h2>
<p><span class="gap w">gold</span> can be done now: the images and the key are online, it needs only work. <span class="gap">grey</span> needs a new source first: a key, a better scan, an edition or the archive.</p>
<ul class="gaplist">{gaps}</ul>
{f'<h2>Already tried</h2><ul class="esc">{escl}</ul>' if escl else ''}
{archive_html(e)}

<h2>Send a result</h2>
<p>One closed gap counts: a code group valued, a passage re-read, a key or clear copy found elsewhere. It is credited to you on the write-up.</p>
<div class="btns"><a class="primary" href="{esc(issue_url(e))}" rel="noopener">Open a further-reading issue</a><a href="{REPO}/issues/new/choose" rel="noopener">Other kinds of report</a><a href="contribute.html#further">How credit works</a><a href="further.html">&larr; All partial readings</a></div>
</main>
'''
    title = plain(p['title'])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<base href="../">
<title>{esc(title)} — read it further</title>
<meta name="description" content="A cipher read in part ({pct(e).replace('&ndash;', 'not measured')}), with its open gaps and instructions for an AI agent to take it further.">
{shell["head"]}
</head>
<body id="top" class="pg-solve pg-further1">
{shell["nav"]}

{body}
{shell["footer"].replace('href="#top"', f'href="{href(e)}#top"')}
{SOLVE_JS}
{shell["scripts"]}
</body>
</html>
'''


def build_pages(pages):
    """Run after the site pages are processed: the nav, footer and scripts are taken from the built further.html."""
    s = (HERE / 'further.html').read_text(encoding='utf-8')
    shell = dict(
        head='\n'.join(re.findall(r'<link rel="(?:stylesheet|icon|apple-touch-icon)"[^>]*>', s)),
        nav=re.search(r'<header class="nav">.*?</header>\n<div class="search" id="search".*?</div>\n</div>', s, re.S).group(0),
        footer=re.search(r'<footer>.*?</footer>', s, re.S).group(0),
        scripts='\n'.join(re.findall(r'<script src="[^"]+"></script>', s)))
    out = HERE / 'further'
    out.mkdir(exist_ok=True)
    keep = set()
    for e in entries(pages):
        f = out / f'{e["p"]["slug"]}.html'; keep.add(f.name)
        f.write_text(one_page(e, shell), encoding='utf-8')
    for f in out.glob('*.html'):          # readings completed since lose their page
        if f.name not in keep: f.unlink()
    return len(keep)
