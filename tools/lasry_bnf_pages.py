"""Write-up pages for George Lasry's BnF cipher research (report of 10 Oct 2026, filed here 13 Oct 2026).

  python tools/lasry_bnf_pages.py import <codex dir>   copy each entry's report text and images into the repository
                                                       (targets/<slug>/lasry_entry.md, docs/<slug>_lasry_p<page>_<n>.png|jpg)
  python tools/lasry_bnf_pages.py build                write docs/<slug>.html for every item, the PAGES entries between the
                                                       lasry-bnf markers in docs/_build_site.py, and the README links

George asked (14 Oct 2026) for each item to read like the other write-ups instead of a link to a NOTES.md. Every page
is generated from his report entry (metadata, key, plaintext sources, excerpts and translations, his key tables and
manuscript crops) and from the target's NOTES.md (our spot-check, corrections, Gallica links). Run _build_site.py after.
"""
import sys, re, json, html, shutil, pathlib, hashlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS, TARGETS = ROOT / 'docs', ROOT / 'targets'
RENAME = {'vergier1690': 'vergier1696', 'dubellay1555b': 'dubellay65'}
SKIP = {'labbe1577lasry'}                 # already a write-up of its own (labbe1582), which records his solution
REPORT = ('George Lasry, with ChatGPT Astra 6 and Anthropic Opus 5.5, <i>BnF cipher research</i>, 10 October 2026 '
          '(sent to Daniel Bourdeau on 13 October 2026 for publication here)')
e = lambda s: html.escape(s or '', quote=False)
ea = lambda s: html.escape(s or '', quote=True)


def slugs():
    return sorted(p.parent.name for p in TARGETS.glob('*/lasry_entry.md'))


# ---------------------------------------------------------------------------
# import

def is_key_table(path):
    """George's key tables are drawn with blue headings; the manuscript crops are greyscale."""
    from PIL import Image
    import numpy as np
    im = Image.open(path).convert('RGB')
    im = im.resize((300, max(1, round(300 * im.size[1] / im.size[0]))))
    a = np.asarray(im).astype(int)
    return float(((a[..., 2] - a[..., 0] > 60) & (a[..., 2] - a[..., 1] > 60)).mean()) > 0.003


def do_import(codex):
    from PIL import Image
    src = pathlib.Path(codex) / 'e'
    n = 0
    for d in sorted(src.iterdir()):
        if d.name in SKIP: continue
        slug = RENAME.get(d.name, d.name)
        t = TARGETS / slug
        if not t.is_dir(): print('no folder for', d.name); continue
        shutil.copyfile(d / 'entry.md', t / 'lasry_entry.md')
        imgs = []
        for f in sorted(d.glob('p*.png')):
            page, k = re.match(r'p(\d+)_(\d+)', f.stem).groups()
            key = is_key_table(f)
            im = Image.open(f)
            if im.size[0] > 1400: im = im.resize((1400, round(1400 * im.size[1] / im.size[0])), Image.LANCZOS)
            if key:
                out = f'{slug}_lasry_p{page}_{k}.png'
                im.convert('RGB').quantize(colors=48).save(DOCS / out, optimize=True)
            else:
                out = f'{slug}_lasry_p{page}_{k}.jpg'
                im.convert('L').save(DOCS / out, quality=82, optimize=True)
            imgs.append(dict(file=out, page=int(page), n=int(k), key=key, w=im.size[0], h=im.size[1]))
        (t / 'lasry_images.json').write_text(json.dumps(imgs, indent=1) + '\n', encoding='utf-8')
        n += 1
    print(n, 'entries imported')


# ---------------------------------------------------------------------------
# parse a report entry

LABELS = ['Contents', 'Ciphertext-only', 'Sender', 'Recipient', 'Year', 'Key', 'Ciphertext']
PAGE_JUNK = re.compile(r'^(BnF cipher research|\d+ / 134|Ciphertext-only|Deciphered using a matching key|Plaintext available)$')


def parse(md):
    lines, page = [], None
    for ln in md.splitlines():
        s = ln.strip()
        m = re.match(r'--- PDF page (\d+)', s)
        if m: page = int(m.group(1)); continue
        if not s or PAGE_JUNK.match(s): continue
        lines.append((page, s))
    title = lines[0][1]
    head, rest = [], []
    cut = next((i for i, (_, s) in enumerate(lines) if s in ('Excerpt and Translation', 'Manuscript lines')), len(lines))
    head, rest = lines[1:cut], lines[cut:]
    fields, order, status, cur = {}, [], '', None
    for _, s in head:
        m = re.match(r'^([A-Z][A-Za-z ,/()\-]{1,70}?):\s*(.*)$', s)
        if m and not s.startswith(('Gallica', 'http')):
            cur = m.group(1)
            if cur in fields: fields[cur] += ' ' + m.group(2)
            else: fields[cur] = m.group(2); order.append(cur)
            continue
        if re.search(r'transcribed|deciphered', s, re.I) and len(s) < 90 and cur in ('Contents', None):
            status = s; cur = None; continue
        if s.startswith(('Gallica', '· Source', 'Source')) or s in ('·',): cur = None; continue
        if cur: fields[cur] += ' ' + s
    for k in fields:
        fields[k] = re.sub(r'\s*·\s*(Source)?\s*$', '', re.sub(r'\s+', ' ', fields[k])).strip()
        fields[k] = re.sub(r'\b(the|of|and|lines?)(\d)', r'\1 \2', fields[k])   # "the81-value": PDF extraction joins
    # excerpts: Excerpt / where / text ... / Translation / text ...
    ex, mode, cur = [], None, None
    ms_pages = {p for p, s in rest if s == 'Manuscript lines'}
    ex_pages = {p for p, s in rest if s in ('Excerpt and Translation', 'Excerpt')}
    LOC = re.compile(r'^(ff?|pp?|PDF)\.?\s?\d')
    for _, s in rest:
        if s == 'Manuscript lines': mode = 'skip'; continue
        if s == 'Excerpt and Translation': mode = 'pre'; continue
        if s == 'Excerpt': cur = dict(where='', text=[], tr=[]); ex.append(cur); mode = 'where'; continue
        if mode == 'skip': continue
        if mode == 'pre': cur = dict(where='', text=[], tr=[]); ex.append(cur); mode = 'where'
        if s == 'Translation' and cur is not None: mode = 'tr'; continue
        if mode == 'where':
            if LOC.match(s) and len(s) < 80:
                s = re.sub(r'(lines?)(\d)', r'\1 \2', s)
                cur['where'] = cur['where'] + ('; ' if cur['where'] else '') + s; continue
            mode = 'text'
        if mode == 'text': cur['text'].append(s)
        elif mode == 'tr': cur['tr'].append(s)
    for x in ex:
        x['text'], x['tr'] = ' '.join(x['text']), ' '.join(x['tr'])
    return dict(title=title, fields=fields, order=order, status=status, excerpts=ex, ms_pages=ms_pages, ex_pages=ex_pages)


def notes_sections(text):
    out, cur = {}, None
    for ln in text.splitlines():
        m = re.match(r'## (.+)', ln)
        if m: cur = m.group(1).strip(); out[cur] = []; continue
        if cur: out[cur].append(ln)
    return {k: '\n'.join(v).strip() for k, v in out.items()}


def md_inline(s):
    s = e(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\[([^\]]+)\]\(\.\./([\w.-]+)/NOTES\.md\)',
               lambda m: f'<a href="{m.group(2)}.html">{m.group(1)}</a>' if (DOCS / f'{m.group(2)}.html').exists()
               else f'<a href="https://github.com/dbourdeau/cyphersolver/tree/main/targets/{m.group(2)}">{m.group(1)}</a>', s)
    s = re.sub(r'&lt;(https?://[^&\s]+)&gt;', r'<a href="\1" rel="noopener">\1</a>', s)
    s = re.sub(r'(?<!["=>])(https?://[^\s<)]+)', r'<a href="\1" rel="noopener">\1</a>', s)
    return s


def bullets(block):
    items = [re.sub(r'^-\s+', '', l).strip() for l in block.splitlines() if l.strip().startswith('- ')]
    return '<ul>\n' + '\n'.join(f'<li>{md_inline(i)}</li>' for i in items) + '\n</ul>' if items else ''


def paras(block):
    ps = [p.strip() for p in re.split(r'\n\s*\n', block) if p.strip() and not p.strip().startswith('- ')]
    return '\n'.join(f'<p>{md_inline(re.sub(r"\s+", " ", p))}</p>' for p in ps)


# ---------------------------------------------------------------------------
# build

def year_of(prof, parsed):
    for d in prof.get('documents', []):
        if isinstance(d.get('year'), int): return d['year']
    m = re.search(r'1[3-9]\d\d', parsed['fields'].get('Year', '') + ' ' + prof.get('title', ''))
    return int(m.group(0)) if m else None


def gallica_ark(links):
    for url, _ in links:
        m = re.search(r'ark:/12148/(\w+)/f(\d+)', url)
        if m: return f'Gallica {m.group(1)} view {m.group(2)}'
    return 'via Gallica'


def page_html(slug):
    t = TARGETS / slug
    prof = json.loads((t / 'profile.json').read_text(encoding='utf-8'))
    P = parse((t / 'lasry_entry.md').read_text(encoding='utf-8'))
    N = notes_sections((t / 'NOTES.md').read_text(encoding='utf-8'))
    imgs, seen = [], set()
    for im in json.loads((t / 'lasry_images.json').read_text(encoding='utf-8')):   # the report repeats some crops
        h = hashlib.md5((DOCS / im['file']).read_bytes()).hexdigest()
        if h not in seen: seen.add(h); imgs.append(im)
    F = P['fields']
    full = prof['title']
    h1 = full.split(' (')[0] if ' (' in full else full
    shelf = re.split(r' — | – ', P['title'])[0].strip()
    shelf = 'BnF ' + shelf if not shelf.startswith('BnF') else shelf
    links = re.findall(r'<(https?://[^>]+)>\s*—\s*(.*)', N.get('Links', ''))
    credit = f'George Lasry, BnF cipher research (10 Oct 2026); manuscript: Biblioth&egrave;que nationale de France, {e(shelf[4:])}, {gallica_ark(links)}'
    year = year_of(prof, P)
    lang = next((d.get('language') for d in prof.get('documents', []) if d.get('language') not in (None, 'unknown')), None)

    def fig(im, cap):
        alt = 'George Lasry&rsquo;s reconstructed key table' if im['key'] else 'Manuscript lines with the cipher, from George Lasry&rsquo;s report'
        cls = ' class="keytab"' if im['key'] else ''
        return (f'<figure{cls} data-credit="{credit}"><img src="{im["file"]}" alt="{alt}" width="{im["w"]}" height="{im["h"]}" loading="lazy">'
                f'<figcaption>{cap}</figcaption></figure>')

    keys = [im for im in imgs if im['key']]
    others = [im for im in imgs if not im['key']]
    def other_cap(im):
        if im['page'] in P['ms_pages'] or im['page'] in P['ex_pages']:
            where = P['excerpts'][0]['where'] if P['excerpts'] else ''
            return f'The manuscript lines of the excerpt{(" (" + e(where) + ")") if where else ""}, from the report, p. {im["page"]}.'
        return f'From the report, p. {im["page"]}: the manuscript or key page George Lasry shows for this item.'

    # the letter
    rows = [('Shelfmark', shelf + (' &middot; ' + e(re.split(r' — | – ', P['title'], 1)[1]) if re.search(r' — | – ', P['title']) else '')),
            ('Sender', e(F.get('Sender'))), ('Recipient', e(F.get('Recipient'))), ('Date', e(F.get('Year'))),
            ('Language', e(lang)), ('Report status', e(P['status'])), ('Ciphertext', e(F.get('Ciphertext')))]
    table = '<div class="tw"><table class="facts">\n' + '\n'.join(f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in rows if v) + '\n</table></div>'
    # key and plaintext sources: every other field of his entry, as he gave it
    extra = [k for k in P['order'] if k not in LABELS]
    keysrc = [k for k in extra if k.lower().startswith('key')]
    ptsrc = [k for k in extra if k not in keysrc]
    dl = lambda ks: '<dl class="gloss">\n' + '\n'.join(f'<dt>{e(k)}</dt><dd>{md_inline(F[k])}</dd>' for k in ks) + '\n</dl>' if ks else ''
    cto = F.get('Ciphertext-only', '')
    method = prof['outcome'].get('method', '')
    # excerpts
    exs = []
    for x in P['excerpts']:
        exs.append(f'<p class="exwhere">{e(x["where"])}</p>\n<blockquote class="plain">{e(x["text"])}</blockquote>\n'
                   + (f'<p class="trans"><b>Translation.</b> {e(x["tr"])}</p>' if x['tr'] else ''))
    sec, n = [], 0
    def h2(id_, text):
        nonlocal n; n += 1
        return f'<h2 id="{id_}"><span class="num">{n:02d}</span> {text}</h2>'
    sec.append(h2('the-letter', 'The letter'))
    sec.append(table)
    sec.append(h2('the-key', 'The key'))
    sec.append(f'<p>{e(F.get("Key", ""))}' + (' The key was recovered from the ciphertext alone.' if cto.lower().startswith('yes') else '') + '</p>')
    if keysrc: sec.append(dl(keysrc))
    sec += [fig(im, f'George Lasry&rsquo;s reconstruction of the key, as drawn in his report (p. {im["page"]}).') for im in keys]
    sec.append(h2('the-decipherment', 'The decipherment'))
    if others: sec += [fig(im, other_cap(im)) for im in others]
    sec += exs or ['<p>The report gives no excerpt for this item.</p>']
    if ptsrc:
        sec.append(h2('plaintext', 'Plaintext and other sources'))
        sec.append('<p>Where a decipherment or clear copy already existed, as George Lasry gives it:</p>')
        sec.append(dl(ptsrc))
    sec.append(h2('our-check', 'Our check'))
    sec.append('<p>This result is George Lasry&rsquo;s. This project did not re-solve the cipher: it checked one sample against the '
               'Gallica image and recorded what it found.</p>')
    sc = next((v for k, v in N.items() if k.startswith('Spot-check')), '')
    sec.append(bullets(sc))
    if N.get('Notes and corrections', '').strip():
        sec.append(h2('notes', 'Notes and corrections'))
        sec.append(paras(N['Notes and corrections']))
    sec.append(h2('sources', 'Sources'))
    src = [f'<li>{REPORT}, p. {min(im["page"] for im in imgs) if imgs else ""}; his other items are listed on '
           f'<a href="contributors.html#lasry">his contributor card</a>.</li>']
    src += [f'<li><a href="{ea(u)}" rel="noopener">{e(lbl)}</a></li>' for u, lbl in links]
    src.append(f'<li>The working folder: <a href="https://github.com/dbourdeau/cyphersolver/tree/main/targets/{slug}" rel="noopener">'
               f'<code>targets/{slug}/</code></a> (his entry as extracted from the report, our spot-check, <code>profile.json</code>).</li>')
    sec.append('<ul>\n' + '\n'.join(src) + '\n</ul>')
    ex0 = P['excerpts'][0]['text'] if P['excerpts'] else ''
    strip = e(ex0[:110]) + ('&hellip;' if len(ex0) > 110 else '')
    kicker = f'{shelf} &middot; contributed by George Lasry' + (f' &middot; {e(lang)}' if lang else '')
    desc = f'{h1}, {shelf}: {F.get("Contents", "")} Deciphered by George Lasry (BnF cipher research, October 2026); spot-checked here.'
    sub = (f'{e(F.get("Contents", ""))} Deciphered by George Lasry, working with ChatGPT Astra 6 and Anthropic Opus 5.5, '
           f'in his <i>BnF cipher research</i> of October 2026: {e(F.get("Ciphertext", "").rstrip("."))}.')
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(h1)} ({e(shelf)})</title>
<meta name="description" content="{ea(re.sub(r"<[^>]+>", "", desc))}">
<link rel="stylesheet" href="style.css">
</head>
<body id="top">
<!-- site:nav -->

<section class="hero">
  <div class="cipherstrip">{strip}</div>
  <p class="kicker">{kicker}</p>
  <h1>{e(h1)}</h1>
  <p class="sub">{sub}</p>
  <p class="meta">George Lasry</p>
</section>

<main>
{chr(10).join(s for s in sec if s)}
</main>
<!-- site:footer -->
</body>
</html>
'''
    label = re.sub(r'\s*\(.*$', '', h1)
    label = label if len(label) <= 42 else label[:40].rsplit(' ', 1)[0] + '&hellip;'
    manifest = dict(slug=slug, label=label, year=str(year) if year else 'undated', y=float(year or 1600), place=shelf,
                    title=h1, blurb=re.sub(r'\s+', ' ', F.get('Contents', '')).strip(),
                    quote=re.sub(r'\s+', ' ', ex0[:90]).strip(), method=method)
    return page, manifest


PAGES_START, PAGES_END = '    # lasry-bnf:start (generated by tools/lasry_bnf_pages.py)\n', '    # lasry-bnf:end\n'




def build():
    man = []
    for slug in slugs():
        page, m = page_html(slug)
        (DOCS / f'{slug}.html').write_text(page, encoding='utf-8')
        man.append(m)
        nt = TARGETS / slug / 'NOTES.md'
        s = nt.read_text(encoding='utf-8')
        s2 = re.sub(r'^Status: no write-up \(result by George Lasry[^\n]*', f'Status: no write-up of our own (result by George Lasry, '
                    f'presented on docs/{slug}.html)', s, count=1, flags=re.M)
        if s2 != s: nt.write_text(s2, encoding='utf-8')
    # PAGES entries
    bs = DOCS / '_manifest.py'
    s = bs.read_text(encoding='utf-8')
    block = PAGES_START + ''.join(
        f"    dict(slug={m['slug']!r}, label={m['label']!r}, year={m['year']!r}, y={m['y']!r}, place={m['place']!r}, st='solved', stt='read',\n"
        f"         title={m['title']!r},\n         blurb={m['blurb']!r},\n         quote={m['quote']!r},\n         author='George Lasry'),\n"
        for m in man) + PAGES_END
    if PAGES_START in s:
        s = re.sub(re.escape(PAGES_START) + r'.*?' + re.escape(PAGES_END), lambda _: block, s, flags=re.S)
    else:
        raise SystemExit('lasry-bnf markers missing from docs/_manifest.py')
    IM_START, IM_END = '# lasry-bnf images:start (generated by tools/lasry_bnf_pages.py; the pages carry their own figures)\n', '# lasry-bnf images:end\n'
    iblock = IM_START + ''.join(f"IMAGES[{m['slug']!r}] = None\n" for m in man) + IM_END
    if IM_START in s: s = re.sub(re.escape(IM_START) + r'.*?' + re.escape(IM_END), lambda _: iblock, s, flags=re.S)
    else: s = s.replace('\nSURVEYS = (', '\n' + iblock + '\nSURVEYS = (', 1)
    bs.write_text(s, encoding='utf-8')
    # README rows: the write-up link goes to the item's page
    rd = ROOT / 'README.md'
    r = rd.read_text(encoding='utf-8')
    for m in man:
        r = re.sub(r'(\[`targets/%s/`\]\(targets/%s/\) · \[write-up\]\(https://dbourdeau\.github\.io/cyphersolver/)lasry-bnf\.html\)'
                   % (re.escape(m['slug']), re.escape(m['slug'])), r'\g<1>%s.html)' % m['slug'], r)
    rd.write_text(r, encoding='utf-8')
    print(len(man), 'pages')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['import']: do_import(a[1])
    elif a[:1] == ['build']: build()
    else: print(__doc__)
