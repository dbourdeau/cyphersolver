"""Terminology and style lint for the write-ups (George Lasry, 24 Sept 2026: "non-standard or ambiguous
cryptologic-related terminology ... 'read' has many meanings", and the LLM writing style).

  python docs/_check_terms.py <slug> [...]     hits on those pages, with line numbers and the suggested wording
  python docs/_check_terms.py --all            count of hits per page, worst first
  python docs/_check_terms.py --rules          the rule list

Only the page's own prose is checked: the hero and <main>, without the generated nav, footer, contents strip,
outcome line, replay and reveal blocks, and without quotations (<q>, <blockquote>, <i lang>, <code>, <pre>), since a
source is quoted as written. A deliberate use can be kept with data-term-ok on the enclosing element.
Exit code 1 when any named page has hits.
"""
import re, sys, html, pathlib

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent

# (id, pattern, what to write instead). Patterns are case-insensitive and matched on the plain text of the prose.
RULES = [
    # outcome words: the method and extent are stated by the outcome line; prose uses the glossary's words
    ('read-status', r'\b(?:read|solved) in (?:part|full|substance)\b|\bpartly (?:read|solved)\b',
     'state the extent ("partial", "complete", "92% of the cipher") or say what was deciphered'),
    ('read-verb', r'\b(?:was|were|is|are|been|being|now|not yet|never) read\b(?! (?:aloud|as|by the recipient))',
     '"deciphered", "decrypted" or "transcribed", whichever happened; "read" is ambiguous'),
    ('solved-here', r'\bsolved here\b|\bbroken here\b|\bsolved it\b',
     'name the method: "key recovered from the ciphertext alone", "key recovered from the clear passages" ...'),
    ('cracked', r'\bcrack(?:ed|ing|s)?\b', '"recovered the key" / "broke the cipher"'),
    ('first-reading', r'\bfirst (?:reading|decipherment|time)\b|\bnever (?:before )?(?:been )?(?:deciphered|decoded)\b|\bnobody had\b|\bno one had\b',
     'a novelty claim: keep it only if profile prior_solution backs it, and say what was checked ("no decipherment found in X, Y")'),
    ('undeciphered', r'\bundeciphered\b|\bunsolved\b|\bnon-decrypted\b',
     'catalogue wording: say what it means ("no contemporary decipherment is known"; Tomokiyo\'s "undeciphered" is not "unsolved")'),
    ('figure-cipher', r'\bfigure ciphers?\b', '"numerical cipher" / "cipher in figures (digits)"'),
    ('sign', r'\bsigns?\b(?= (?:cipher|alphabet|value))', '"symbol" for a cipher character; "sign" is fine for graphic signs, not digits'),
    # internal jargon
    ('read-bar', r'\bread bar\b', '"95% of the cipher gives sense" (glossary: extent)'),
    ('jargon', r'\bsegmenter\b|\bpinning\b|\bpinned\b|\bbeam (?:search|plateau)\b|\banchors?\b(?= (?:word|pair|group))',
     'describe the step in plain terms ("dividing the figures into units", "fixing a value") or drop it'),
    # style tells
    ('not-but', r'\bnot (?:just |merely |only |simply )?(?:a |an |the )?\w+(?: \w+)?, but\b|\bisn\'t \w+,? (?:it\'s|but)\b',
     'say the positive statement directly'),
    ('hype', r'\b(?:notably|crucially|importantly|remarkably|strikingly|tellingly|intriguingly|fittingly|delve|tapestry|testament to|'
     r'it is worth noting|worth noting|it turns out|as it happens|in short|simply put)\b', 'drop it'),
    ('colon-reveal', r'\bthe answer: |\bthe twist: |\bthe catch: |\bthe verdict: ', 'plain sentence'),
]
EMDASH_PER_1000 = 6          # more em-dashes than this per 1000 words is flagged once per page

STRIP = [r'<header class="nav">.*?</header>', r'<div class="search".*?</div>\n</div>', r'<footer.*?</footer>',
         r'<nav class="toc".*?</nav>', r'<!-- replay:start -->.*?<!-- replay:end -->', r'<figure class="creveal".*?</figure>',
         r'<p class="outcome">.*?</p>', r'<p class="meta">.*?</p>', r'<script.*?</script>', r'<style.*?</style>',
         r'<(q|blockquote|code|pre)\b[^>]*>.*?</\1>', r'<i lang="[^"]*">.*?</i>', r'<(\w+)[^>]*data-term-ok[^>]*>.*?</\1>',
         r'<figure class="sreplay".*?</figure>', r'<head>.*?</head>', r'<div class="seal [a-z]+"[^>]*>.*?</div>']

def prose(s):
    """Page text as lines, generated and quoted parts blanked out (line numbers kept)."""
    for pat in STRIP:
        s = re.sub(pat, lambda m: '\n' * m.group(0).count('\n'), s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return [html.unescape(l) for l in s.split('\n')]

def check(slug):
    f = HERE / f'{slug}.html'
    lines = prose(f.read_text(encoding='utf-8'))
    hits = []
    for i, l in enumerate(lines, 1):
        for rid, pat, fix in RULES:
            for m in re.finditer(pat, l, re.I):
                if rid == 'undeciphered' and 'Unsolved Historical Ciphers' in l: continue
                hits.append((i, rid, m.group(0), fix))
    words = sum(len(l.split()) for l in lines)
    dashes = sum(l.count('—') for l in lines)
    if words and dashes * 1000 / words > EMDASH_PER_1000:
        hits.append((0, 'em-dash', f'{dashes} em-dashes in {words} words', 'use commas, colons or full stops'))
    return hits

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--rules']:
        for rid, pat, fix in RULES: print(f'{rid:14s} {fix}')
        sys.exit(0)
    if a[:1] == ['--all']:
        import _check_writeup as cw
        res = []
        for f in sorted(HERE.glob('*.html')):
            if f.stem in ('index', 'catalogue', 'writeups', 'glossary') or f.stem in cw.TOOL_PAGES or f.stem.startswith('_'): continue
            res.append((len(check(f.stem)), f.stem))
        for n, s in sorted(res, reverse=True): print(f'{n:4d}  {s}')
        print(f'{sum(n for n, _ in res)} hits on {sum(1 for n, _ in res if n)} of {len(res)} pages')
        sys.exit(0)
    bad = 0
    for slug in a:
        hits = check(slug)
        bad += bool(hits)
        print(f'{slug}: {len(hits)} hit(s)')
        for i, rid, txt, fix in hits: print(f'  line {i:4d}  [{rid}] "{txt}" -> {fix}')
    sys.exit(1 if bad else 0)
