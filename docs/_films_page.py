"""Films: one list, two places.

FILMS below is the only list of the site's films. The build (_build_site.py) calls build_html(), which
  - writes films.html: every film with its own player, length, summary, write-up links and credits;
  - rewrites the poster shelf on index.html, between <!-- films:start --> and <!-- films:end -->: one small
    card per film (FILMS order) and a last card to films.html. The row scrolls sideways, so it keeps one height
    however many films there are;
  - makes each card's thumbnail, thumbs/film_<id>-480.webp, from the film's poster when it is missing.
On the home page a card opens the player dialog with the same data-film id (home.js); a card with no dialog is a
plain link to films.html#<id>. To add a film: put the .mp4 (and .vtt, poster) in docs/, add an entry here, and
add its dialog to index.html only if it should play in place on the home page.
"""
import html
from pathlib import Path

HERE = Path(__file__).resolve().parent

FILMS = [
    dict(id='codebooks1787', card='Jefferson’s lost codebooks', title='The Lost Codebooks: Jefferson’s Code No. 11 and No. 16',
         src='codebooks1787.mp4?v=1', vtt='codebooks1787.vtt?v=1', poster='codebooks1787_poster.jpg', secs=203,
         about='No codebook survives for two of Jefferson’s diplomatic codes. Starting from Thomas Barclay’s arrest at Bordeaux in '
               '1787, the film rebuilds them from the meanings written over the numbers, tests the editors’ guess “sea”, finds '
               'Pinckney’s London code of 1793 at Tunis in 1801, and reads a passage of 1807 that no one had decoded.',
         links=[('jefferson1787.html', 'Code No. 11'), ('pinckney1793.html', 'Code No. 16')],
         credit='Code No. 16 key: Andrew Beling. Images: Library of Congress; US National Archives; portraits from Wikimedia Commons, '
                'public domain. Synthetic narration (Kokoro); score synthesised.'),
    dict(id='burr', card='Burr’s secret letters', title='Aaron Burr’s two ciphers, 1804 and 1808',
         src='burr1804.mp4?v=2', vtt='burr1804.vtt?v=2', poster='burr1804_poster.jpg', secs=215,
         about='The Burr–Hamilton duel in cut paper, then Burr’s cipher letter to Joseph Alston a week later, deciphered sign by '
               'sign: whether to stand trial or go to Europe. Then Baltimore in 1808, where Burr in hiding writes to his daughter '
               'Theodosia in a six-alphabet number cipher, and sails for England.',
         links=[('burr1804.html', 'The 1804 letter'), ('burr1808.html', 'The 1808 letters')],
         credit='Letters: Gilder Lehrman Institute of American History, GLC01523, via the Hamilton Education Program. Portraits: '
                'Vanderlyn, Trumbull, Wikimedia Commons, public domain. Synthetic voices (Kokoro); score synthesised.'),
    dict(id='qabaqibi1350', card='A Mamluk love poem', title='A Mamluk cipher poem deciphered, step by step',
         src='qabaqibi1350.mp4?v=1', vtt='qabaqibi1350.vtt?v=1', poster='qabaqibi1350_poster.jpg', secs=195,
         about='Ibn al-Qabāqibī’s cipher verses in a Mamluk secretary’s book (Penn LJS 51, f. 106v): transcribed sign by sign, '
               'deciphered from five red letters, a repeated word and the metre, corrected by Alan Elbaum, and read aloud in '
               'Arabic and in English.',
         links=[('qaysarani1350.html', 'The write-up')],
         credit='Images: University of Pennsylvania, Kislak Center, via OPenn (public domain). Synthetic voices (Kokoro, Piper); '
                'score synthesised.'),
    dict(id='genoa1527', card='A cipher being solved', title='A 1527 cipher letter deciphered, step by step',
         src='genoa1527.mp4', vtt=None, poster='genoa1527_poster.jpg', secs=104,
         about='Lope de Soria’s cipher letter from Genoa, 7 March 1527, transcribed sign by sign and deciphered from its own '
               'patterns, with every stage on the page.',
         links=[('lannoy1527.html', 'The write-up')],
         credit='Synthetic narration (Kokoro); score synthesised.'),
    dict(id='intro', card='Cyphersolver in 45 seconds', title='Cyphersolver in under forty-five seconds',
         src='hero.mp4?v=6', vtt=None, poster='hero_poster.png', secs=41,
         about='What the project does, in a narrated pixel-art film: a real cipher passage, taken from the page to its reading.',
         links=[('writeups.html', 'All write-ups')],
         credit='Narration synthetic; captions in the picture.'),
]


def mmss(s):
    return f'{s // 60}:{s % 60:02d}'


def thumb(f):
    out = HERE / 'thumbs' / f"film_{f['id']}-480.webp"
    if not out.exists():
        from PIL import Image
        im = Image.open(HERE / f['poster']).convert('RGB')
        im.thumbnail((480, 270))
        out.parent.mkdir(exist_ok=True)
        im.save(out, 'WEBP', quality=78)
    return f"thumbs/{out.name}"


def shelf():
    cards = []
    for f in FILMS:
        cards.append(f'<li><a class="filmcard" href="films.html#{f["id"]}" data-film="{f["id"]}">'
                     f'<span class="fc-img"><img src="{thumb(f)}" width="240" height="135" alt="" loading="lazy" decoding="async">'
                     f'<span class="fc-play" aria-hidden="true"></span><span class="fc-len">{mmss(f["secs"])}</span></span>'
                     f'<span class="fc-t">{html.escape(f["card"])}</span></a></li>')
    cards.append(f'<li><a class="filmcard fc-all" href="films.html"><span class="fc-img"><span class="fc-n">{len(FILMS)}</span>'
                 f'<span class="fc-nl">films</span></span><span class="fc-t">All films &rarr;</span></a></li>')
    return ('<!-- films:start -->\n<nav class="filmshelf" aria-label="Films">\n'
            f'  <p class="fs-h">Films</p>\n  <ul>{"".join(cards)}</ul>\n</nav>\n<!-- films:end -->')


def page(version):
    items = []
    for f in FILMS:
        track = (f'<track kind="captions" src="{f["vtt"]}" srclang="en" label="English" default>' if f['vtt'] else '')
        links = ' &middot; '.join(f'<a href="{h}">{html.escape(t)} &rarr;</a>' for h, t in f['links'])
        items.append(
            f'<article class="film" id="{f["id"]}">\n'
            f'  <video controls playsinline preload="none" poster="{f["poster"]}" aria-label="{html.escape(f["title"])}, {mmss(f["secs"])}">'
            f'<source src="{f["src"]}" type="video/mp4">{track}</video>\n'
            f'  <h2>{html.escape(f["title"])} <span class="fl">{mmss(f["secs"])}</span></h2>\n'
            f'  <p>{html.escape(f["about"])}</p>\n  <p class="flinks">{links}</p>\n'
            f'  <p class="hv-credit">{html.escape(f["credit"])}</p>\n</article>')
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>Films &mdash; {len(FILMS)} short films of ciphers being deciphered</title>\n'
            '<meta name="description" content="Short narrated films of historical ciphers being deciphered on this site, each with its '
            'write-up: the manuscript, every stage of the work and the reading.">\n'
            f'<link rel="stylesheet" href="style.css?v={version}">\n</head>\n<body id="top">\n<!-- site:nav -->\n\n'
            '<section class="hero">\n'
            f'  <p class="kicker">Films &middot; {len(FILMS)}</p>\n'
            '  <h1>The decipherments, on film</h1>\n'
            '  <p class="sub">Short narrated films of ciphers worked on here: the manuscript, each stage of the decipherment and the '
            'reading, with captions. Each film links to its write-up, where the evidence is.</p>\n'
            '  <p class="meta">Daniel Bourdeau</p>\n</section>\n\n<main>\n<div class="filmlist">\n'
            + '\n'.join(items) + '\n</div>\n</main>\n</body>\n</html>\n')


def build_html(version):
    (HERE / 'films.html').write_text(page(version), encoding='utf-8')
    idx = HERE / 'index.html'
    s = idx.read_text(encoding='utf-8')
    a, b = s.find('<!-- films:start -->'), s.find('<!-- films:end -->')
    if a >= 0 and b > a:
        s = s[:a] + shelf() + s[b + len('<!-- films:end -->'):]
        idx.write_text(s, encoding='utf-8')
    return len(FILMS)


if __name__ == '__main__':
    print(build_html('dev'), 'films')
