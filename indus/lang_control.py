"""Second-language control for the rebus baseline (rebus_checks.py R4).

The Tamil test asked: for a fixed list of picture concepts, how often does some word for
the picture begin a star name ending in the word for 'star' (Tamil -min)? Here the same
question for Sanskrit, from Monier-Williams (Cologne csl-orig mw.txt): star names are
compounds whose last member is tara / taraka / naksatra / rksa and whose gloss names a
star, asterism, constellation or planet; picture words are MW entries whose first sense
names the concept. And the numeral test: which numbers begin a star name in each language.

Usage: python lang_control.py mw.txt dedr_entry_v11.csv
Writes results/lang_control.md.
"""
import os
import re
import sys
from collections import defaultdict

import rebus_checks as rc

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
STAR_LAST = ('tArA', 'tAraka', 'tArakA', 'nakzatra', 'fkza')
STAR_GLOSS = re.compile(r'\b(star|stars|asterism|constellation|lunar mansion|planet|nakshatra|pleiades|ursa)\b', re.I)
SKT_NUM = {1: 'eka', 2: 'dvi', 3: 'tri', 4: 'catur', 5: 'paYca', 6: 'zaw', 7: 'sapta', 8: 'azwa',
           12: 'dvAdaSa'}


def say(s=''):
    OUT.append(s)
    print(s)


def slp_simple(w):
    """SLP1 -> plain key: long = short, retroflex = dental, sibilants merged, geminates reduced."""
    w = w.lower()
    w = re.sub(r'[^a-z]', '', w)
    w = re.sub(r'(.)\1+', r'\1', w)
    return w


def load_mw(path):
    entries = []           # (k2 parts, gloss)
    cur = None
    with open(path, encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('<L>'):
                m = re.search(r'<k2>([^<]*)', ln)
                cur = [m.group(1) if m else '', '']
            elif ln.startswith('<LEND>'):
                if cur:
                    entries.append(cur)
                cur = None
            elif cur is not None:
                cur[1] += ln
    out = []
    for k2, body in entries:
        gloss = body.split('¦', 1)[1] if '¦' in body else body
        gloss = re.sub(r'<[^>]+>', ' ', gloss)
        parts = [p for p in re.split(r'[—\-]', k2.replace('°', '')) if p]
        out.append((parts, gloss))
    return out


def main(mw_path, dedr_path):
    mw = load_mw(mw_path)
    say('# Second-language control: Sanskrit against Tamil')
    say()
    stars = []
    for parts, gloss in mw:
        if len(parts) >= 2 and parts[-1] in STAR_LAST and STAR_GLOSS.search(gloss[:200]):
            stars.append((parts, gloss.strip()[:80]))
    keys = {slp_simple(p[0]) for p, _ in stars}
    say('Sanskrit star names ending in a word for star (tara, taraka, naksatra, rksa) in MW: %d; '
        'distinct first members: %d. (Tamil, Parpola\'s list: 34 star names in -min, 31 keys.)' % (
            len(stars), len(keys)))
    say()
    say('Examples: ' + '; '.join('%s (%s)' % ('-'.join(p), g.split(';')[0].strip()) for p, g in stars[:12]))
    say()
    # picture words
    words = defaultdict(set)
    for parts, gloss in mw:
        if len(parts) != 1:
            continue
        first = re.split(r'[;,(]', gloss.strip())[0].lower()
        if re.match(r'^\s*((m|f|n|mfn|ind|mf|du|pl)\.\s*)*n\.\s*of\b', first):
            continue                     # proper names ('N. of a man') are not picture words
        first = re.sub(r'^\s*((m|f|n|mfn|ind|mf|du|pl)\.\s*)+', '', first).strip()
        words[slp_simple(parts[0])].add(first)
    primary_hits = anysense_hits = 0
    hit_rows = []
    for c in rc.CONCEPTS:
        pat = re.compile(r'\b%s(s|es)?\b' % re.escape(c))
        ws = {w for w, gs in words.items() if any(pat.search(g) for g in gs)}
        h = sorted(w for w in ws if w in keys)
        primary_hits += bool(h)
        if h:
            hit_rows.append((c, len(ws), h))
    n = len(rc.CONCEPTS)
    say('## Picture concepts (the %d of the Tamil test)' % n)
    say()
    say('- Sanskrit, first sense of the gloss, strict: %d/%d (%.0f%%) of concepts have a word that '
        'begins a star name ending in a star word.' % (primary_hits, n, 100 * primary_hits / n))
    say('- Tamil, same measure (rebus_checks.py R4): 15/98 (15%) strict, 29/98 (30%) loose.')
    say()
    for c, k, h in hit_rows:
        say('  - %s (%d words): %s' % (c, k, ' '.join(h)))
    say()
    say('## The first step of every fish reading: is a word for "fish" also a word for "star"?')
    say()
    fishw = {w for w, gs in words.items() if any(re.search(r'\bfish\b', g) for g in gs)}
    starw = {w for w, gs in words.items() if any(STAR_GLOSS.search(g) for g in gs)}
    say('- Sanskrit (MW, first sense): %d words for fish, %d for star/asterism/planet; forms shared: %s.'
        % (len(fishw), len(starw), ', '.join(sorted(fishw & starw)) or 'none'))
    tam = rc.load_tamil(dedr_path)
    tf = {w for w, ms in tam.items() if any(re.search(r'\bfish\b', re.split('[;,]', m)[0]) for m in ms)}
    ts = {w for w, ms in tam.items() if any(re.search(r'\b(star|stars|planet|asterism|constellation)\b', re.split('[;,]', m)[0]) for m in ms)}
    say('- Tamil (DEDR, first sense): %d words for fish, %d for star/planet; forms shared: %s.'
        % (len(tf), len(ts), ', '.join(sorted(tf & ts)) or 'none'))
    say()
    say('## Numerals that begin a star name')
    say()
    tamil_star = {k for c, _, k, _ in rc.load_min() if 'S' in c}
    say('| number | Sanskrit | Sanskrit star names | Tamil star name in -min | corpus: before plain fish (ICIT / M77) |')
    say('|---|---|---|---|---|')
    corpus = {1: '5 / 6', 3: '19 / 20', 4: '6 / 4', 5: '0 / 0', 6: '10 / 16', 7: '1 / 1', 12: '8 / 9',
              2: 'short pair 11 / 16', 8: '0 / 0'}
    for v, s in SKT_NUM.items():
        sk = [('-'.join(p), g.split(';')[0].strip()) for p, g in stars if slp_simple(p[0]).startswith(slp_simple(s)[:4])]
        ta = [f for f in rc.TAMIL_NUMERALS.get(v, []) if rc.simplify(f) in tamil_star]
        say('| %d | %s | %s | %s | %s |' % (v, s, '; '.join('%s (%s)' % x for x in sk[:3]) or 'none',
                                            ', '.join(ta) or 'none', corpus.get(v, '')))
    if len(sys.argv) > 3:
        sumerian(sys.argv[3])
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'lang_control.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


def sumerian(path):
    """ePSD2 glossary (ORACC, CC0), extracted to TSV (cf, gw, pos, senses). Sumerian star names
    are written MUL + a word: the constellation names (pos CN) name what they depict."""
    import csv
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    cn = [r for r in rows if r['pos'] == 'CN']
    say()
    say('## Sumerian (ePSD2 glossary, %d entries; %d constellation names)' % (len(rows), len(cn)))
    say()
    hits = []
    for c in rc.CONCEPTS:
        pat = re.compile(r'\b%s(s|es)?\b' % re.escape(c), re.I)
        h = sorted({r['cf'] for r in cn if pat.search(r['gw'] + ' ' + r['senses'])})
        if h:
            hits.append((c, h))
    n = len(rc.CONCEPTS)
    say('- picture concepts whose picture is itself a Sumerian constellation (MUL + that word): %d/%d '
        '(%.0f%%): %s.' % (len(hits), n, 100 * len(hits) / n,
                           '; '.join('%s = %s' % (c, ', '.join(h)) for c, h in hits)))
    fish = {r['cf'].lower() for r in rows if r['pos'] == 'N' and re.search(r'\bfish\b', r['gw'])}
    star = {r['cf'].lower() for r in rows if re.search(r'\b(star|stars|planet)\b', r['gw'])} | \
        {r['cf'].lower() for r in cn}
    say('- words for fish (guide word): %d; star words and constellation names: %d; forms shared: %s.' % (
        len(fish), len(star), ', '.join(sorted(fish & star)) or 'none'))
    nums = [r for r in cn if re.search(r'\b(one|two|three|four|five|six|seven|eight|twelve)\b', r['gw'] + r['senses'], re.I)]
    say('- constellation names built on a number: %s (the Pleiades are MUL.MUL "the stars", not a '
        'number; "the Seven" is not a CN entry in ePSD2).' % (', '.join(r['cf'] for r in nums) or 'none'))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
