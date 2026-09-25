"""The ciphertext-only list for Klaus Schmeh (George Lasry, email 25 Sept 2026), as HTML and PDF.

  python papers/lasry/_ct_list.py            writes papers/lasry/ciphertext-only-list.html and .pdf

Items, their primary and secondary sources and summaries are hand-kept in ct_sources.json. Method, extent and
the prior-solution note come from each target's profile.json, so a reclassification there shows up here. The PDF
is printed with headless Chrome or Edge.
"""
import html, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'docs'))
import _methods as M

SITE = 'https://dbourdeau.github.io/cyphersolver/'
DECODE = 'https://de-crypt.org/decrypt-web/RecordsView/'
BROWSERS = [r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe']
e = html.escape


def prior_note(prof):
    o, ps = prof['outcome'], prof['conditions'].get('prior_solution') or {}
    if o.get('first_break') == 'unpublished prior':
        where = ps.get('where', '')
        yr = next((w for w in ('2021', '2023', '2024') if f'in {w}' in where), '?')
        extra = ' (improved in February 2026)' if 'Feb 2026' in where else ''
        return (f'<b>Solved independently by the LLMs</b>, from the ciphertext alone and without knowledge of any '
                f'earlier solution. In private communications, Lasry wrote that he had also solved it in {yr}{extra}, '
                'but his solution has not been published.')
    return ''


def sources(text, links, decode=False):
    """The source text, DECODE record numbers linked, then any [label, url] links."""
    s = e(text)
    if decode:
        s = re.sub(r'\bR(\d{2,5})\b', lambda m: f'<a href="{DECODE}{m[1]}">R{m[1]}</a>', s)
    if links:
        s += ' &middot; ' + ' &middot; '.join(f'<a href="{e(u)}">{e(l)}</a>' for l, u in links)
    return s


def item(it, n):
    prof = json.loads((ROOT / it['profile'] / 'profile.json').read_text(encoding='utf-8'))
    method = prof['outcome'].get('method', 'unknown')
    if it['section'] == 'ct':
        assert method == M.CT, (it['slug'], method)
        assert prof['outcome'].get('first_break') is not False, it['slug']
    ext = M.extent(prof)
    note = prior_note(prof)
    url = SITE + it['slug'] + '.html'
    rows = [('Method', f'{e(M.LABEL.get(method, method))} &middot; {e(ext)}'),
            ('Primary source', sources(it['primary'], it.get('primary_links'))),
            ('Secondary source', sources(it['secondary'], it.get('secondary_links'), decode=True))]
    if note:
        rows.append(('Independent solution', note))
    if it.get('cipherbrain') and it['section'] == 'ct':
        rows.append(('Cipherbrain', 'also a Cipherbrain challenge'))
    rows.append(('Write-up', f'<a href="{url}">{e(url)}</a>'))
    dl = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in rows)
    return (f'<section class="item"><h3><span class="n">{n}.</span> {e(it["title"])}'
            f' <span class="date">{e(it["date"])}</span></h3><p>{e(it["summary"])}</p><dl>{dl}</dl></section>')


def main():
    data = json.loads((HERE / 'ct_sources.json').read_text(encoding='utf-8'))
    ct = [i for i in data['items'] if i['section'] == 'ct']
    cb = [i for i in data['items'] if i['section'] == 'cipherbrain']
    n = 0
    parts = []
    for head, intro, items in [
        ('Key recovered from ciphertext only', 'First breaks: the key was rebuilt from the ciphertext alone, with no '
         'plaintext and no existing key. Three items had also been solved earlier by '
         'George Lasry but never published; the LLMs solved them independently, and his unpublished solution is noted.', ct),
        ('Other Cipherbrain challenges (any method)', 'Challenges posted on Klaus Schmeh\'s Cipherbrain that this '
         'project read by other routes. The Soglia dispatch above is also a Cipherbrain challenge.', cb)]:
        parts.append(f'<h2>{e(head)}</h2><p class="intro">{e(intro)}</p>')
        for it in items:
            n += 1
            parts.append(item(it, n))
    excl = ''.join(f'<li><b>{e(x["slug"])}</b>: {e(x["why"])}</li>' for x in data['excluded'])
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>Ciphertext-only solutions</title>
<style>
@page {{ size: A4; margin: 16mm 15mm; }}
body {{ font: 10pt/1.4 Georgia, 'Times New Roman', serif; color: #111; }}
h1 {{ font-size: 17pt; margin: 0 0 2pt; }} .sub {{ color: #555; margin: 0 0 10pt; }}
h2 {{ font-size: 13pt; border-bottom: 1px solid #999; padding-bottom: 2pt; margin-top: 14pt; }}
.intro {{ color: #333; font-style: italic; }}
.item {{ break-inside: avoid; margin: 0 0 9pt; }}
h3 {{ font-size: 10.5pt; margin: 6pt 0 2pt; }} .n {{ color: #777; }} .date {{ font-weight: normal; color: #555; }}
.item p {{ margin: 0 0 3pt; }}
dl {{ display: grid; grid-template-columns: 30mm 1fr; gap: 1pt 6pt; margin: 0; font-size: 9pt; }}
dt {{ color: #555; }} dd {{ margin: 0; }} a {{ color: #124; }}
.foot {{ font-size: 8.5pt; color: #444; margin-top: 12pt; border-top: 1px solid #ccc; padding-top: 4pt; }}
</style></head><body>
<h1>Historical ciphers: ciphertext-only solutions</h1>
<p class="sub">cyphersolver project (Daniel Bourdeau, with George Lasry) &middot; {len(ct)} ciphertext-only first breaks
and {len(cb)} further Cipherbrain challenges &middot; list of 25 September 2026 &middot; {e(SITE)}</p>
{''.join(parts)}
<div class="foot"><b>Left out on purpose.</b><ul>{excl}</ul>
Primary source = the archive or printed original. Secondary source = where the item was found (DECODE, Tomokiyo's
cryptiana, Cipherbrain, the BnF catalogue). Percentages are measured or estimated shares of the cipher text read,
as recorded on each write-up.</div>
</body></html>'''
    out = HERE / 'ciphertext-only-list.html'
    out.write_text(doc, encoding='utf-8', newline='\n')
    pdf = HERE / 'ciphertext-only-list.pdf'
    exe = next((b for b in BROWSERS if pathlib.Path(b).exists()), None)
    if exe:
        subprocess.run([exe, '--headless', '--disable-gpu', '--no-pdf-header-footer',
                        f'--print-to-pdf={pdf}', out.as_uri()], check=True, capture_output=True)
    print(f'{len(ct)} ciphertext-only, {len(cb)} Cipherbrain -> {out.name}' + (f', {pdf.name}' if exe else ' (no browser, no PDF)'))


if __name__ == '__main__':
    main()
