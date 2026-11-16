"""corrections.html: the public log of corrections, built from docs/corrections.json (16 Nov 2026).

Each entry: date (ISO), pages (write-up slugs), what changed, reported_by, why. Newest first. A published claim,
count or reading that is corrected or withdrawn gets an entry here as well as its dated note on the page.
"""
import json, html, pathlib, datetime

HERE = pathlib.Path(__file__).parent


def build_html(version=''):
    data = json.loads((HERE / 'corrections.json').read_text(encoding='utf-8'))
    rows = sorted(data['corrections'], key=lambda c: c['date'], reverse=True)
    e = lambda s: html.escape(s, quote=False)
    def when(iso):
        d = datetime.date.fromisoformat(iso)
        return f'{d.day} {d:%B %Y}'
    def pages(ps):
        out = []
        for p in ps:
            out.append(f'<a href="{p}.html">{p}</a>' if (HERE / f'{p}.html').exists() else f'<span translate="no">{p}</span>')
        return ', '.join(out)
    items = ''.join(
        f'<article class="corr" id="c{i}">\n<h3><time datetime="{c["date"]}">{when(c["date"])}</time></h3>\n'
        f'<p>{e(c["what"])}</p>\n<dl class="gloss">\n<dt>Pages</dt><dd>{pages(c["pages"])}</dd>\n'
        f'<dt>Reported by</dt><dd>{e(c["reported_by"])}</dd>\n<dt>Why it was wrong</dt><dd>{e(c["why"])}</dd>\n</dl>\n</article>\n'
        for i, c in enumerate(rows, 1))
    page = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Corrections &mdash; what this site got wrong, and when it was put right</title>\n'
        '<meta name="description" content="The log of corrections to readings, counts and claims published on Cyphersolver: '
        'date, pages, what changed, who reported it and why it was wrong.">\n'
        f'<link rel="stylesheet" href="style.css?v={version}">\n</head>\n<body id="top">\n<!-- site:nav -->\n\n'
        '<section class="hero">\n  <p class="kicker">Reference &middot; corrections</p>\n  <h1>Corrections</h1>\n'
        '  <p class="sub">What this site has published and then had to correct or withdraw: the date, the pages, what '
        'changed, who reported it and why it was wrong. Newest first. A reading here stays open to correction; '
        '<a href="method.html#contest">how to contest one</a>.</p>\n'
        '  <p class="meta">Daniel Bourdeau and contributors</p>\n</section>\n\n<main>\n\n'
        f'<p>{len(rows)} entries. The log starts on 16 November 2026; earlier entries were gathered from the dated notes '
        'already on the pages and in the repository, and are not complete before that date. The full history of every '
        'file is in the <a href="https://github.com/dbourdeau/cyphersolver/commits/main" rel="noopener">repository</a>.</p>\n\n'
        f'{items}\n</main>\n<!-- site:footer -->\n</body>\n</html>\n')
    (HERE / 'corrections.html').write_text(page, encoding='utf-8')
    return len(rows)


if __name__ == '__main__':
    print(build_html(), 'corrections')
