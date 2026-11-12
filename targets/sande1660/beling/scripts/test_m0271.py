"""sande1660 cipher A: the pre-registered test of key.txt on scan m0271 (see ../PREREG.md).

    python3 -I scripts/test_m0271.py          (run from beling/; writes results/test_m0271_result.json and
                                               results/test_m0271_output.txt)

Standard library only. Inputs (frozen in results/frozen_inputs.sha256): key/key.txt, key/transcription_build.txt,
lexicon/pt.json.gz, transcription/m0271.txt.
"""
import gzip
import json
import os
import random
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 1660
N_SHUFFLED = 200
MIN_LETTERS = 600
MIN_WORD = 3
MAX_WORD = 24


def load_key(path):
    """The letter table of key.txt: lines 'x  n, m ...' (letter, then numbers). Code groups are not read."""
    key = {}
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            m = re.match(r'^([a-z])(?:/[a-z])?\s+(\d+(?:,\s*\d+)*)', line)
            if m:
                for n in m.group(2).split(','):
                    key[int(n)] = m.group(1)
            if line.startswith('Code groups'):
                break
    return key


def load_lines(path):
    """Return [(tag, [token, ...])]. Tokens: int, or None for a sign not read. Word gaps ('|') are ignored."""
    out = []
    with open(path, encoding='utf-8') as fh:
        for raw in fh:
            if not raw.startswith('@'):
                continue
            tag, body = raw.rstrip('\n').split(' ', 1)
            toks = []
            for t in re.split(r'[.|]', body):
                t = t.strip().rstrip('*')
                if not t:
                    continue
                toks.append(int(t) if t.isdigit() else None)
            out.append((tag, toks))
    return out


def skeleton(s, cedilla_to='s'):
    s = s.lower().replace('ç', cedilla_to)
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))
    s = re.sub(r'c(?=[ei])', 's', s)
    s = s.replace('z', 's').replace('h', '').replace('j', 'i').replace('y', 'i').replace('v', 'u')
    s = re.sub(r'(.)\1+', r'\1', s)
    return s


def load_lexicon(path, cedilla_to='s'):
    words = json.load(gzip.open(path, 'rt', encoding='utf-8'))
    lex = set()
    for w in words:
        if w.isalpha():
            k = skeleton(w, cedilla_to)
            if len(k) >= MIN_WORD:
                lex.add(k)
    return lex


def segments(toks, key):
    """Decrypt one line to segments. Code groups (>= 60) and unread signs break the line; a number below 60 that
    the key lacks becomes '#', a letter position no word can cover."""
    segs, cur = [], ''
    for t in toks:
        if t is None or t >= 60:
            if cur:
                segs.append(cur)
            cur = ''
        else:
            cur += key.get(t, '#')
    if cur:
        segs.append(cur)
    return segs


def norm_seg(seg, cedilla_to='s'):
    # skeleton on the letters, keeping '#' in place
    parts = seg.split('#')
    return '#'.join(skeleton(p, cedilla_to) for p in parts)


def cover(s, lex):
    """Most letters of s covered by lexicon words (len >= MIN_WORD); returns (covered, parse)."""
    n = len(s)
    best = [0] * (n + 1)
    back = [None] * (n + 1)
    for i in range(1, n + 1):
        best[i], back[i] = best[i - 1], (i - 1, False)
        for j in range(max(0, i - MAX_WORD), i - MIN_WORD + 1):
            if s[j:i] in lex and best[j] + (i - j) > best[i]:
                best[i], back[i] = best[j] + (i - j), (j, True)
    parse, i = [], n
    while i > 0:
        j, word = back[i]
        parse.append(s[j:i].upper() if word else s[j:i])
        i = j
    return best[n], ''.join(reversed(parse))


def score(lines, key, lex, cedilla_to='s', detail=False):
    cov = tot = 0
    rows = []
    for tag, toks in lines:
        segs = [norm_seg(g, cedilla_to) for g in segments(toks, key)]
        lc = lt = 0
        parses = []
        for g in segs:
            c, p = cover(g, lex)
            lc += c
            lt += len(g)
            parses.append(p)
        cov += lc
        tot += lt
        if detail:
            rows.append((tag, segments(toks, key), parses, lc, lt))
    return (cov / tot if tot else 0.0), tot, rows


def main():
    key = load_key(os.path.join(HERE, 'key', 'key.txt'))
    assert len(key) == 26, len(key)
    lex = load_lexicon(os.path.join(HERE, 'lexicon', 'pt.json.gz'))
    build = load_lines(os.path.join(HERE, 'key', 'transcription_build.txt'))
    held = load_lines(os.path.join(HERE, 'transcription', 'm0271.txt'))

    s_build, n_build, _ = score(build, key, lex)
    s_held, n_held, rows = score(held, key, lex, detail=True)

    rng = random.Random(SEED)
    syms = sorted(key)
    vals = [key[s] for s in syms]
    null = []
    for _ in range(N_SHUFFLED):
        v = vals[:]
        rng.shuffle(v)
        null.append(score(held, dict(zip(syms, v)), lex)[0])
    best_null = max(null)
    threshold = 0.85 * s_build
    margin = s_held - best_null
    too_small = n_held < MIN_LETTERS
    passed = (not too_small) and s_held >= threshold and margin >= 0.30

    # Secondary (not the test): the other reading of the PREREG's cedilla rule, ç -> c.
    lex_c = load_lexicon(os.path.join(HERE, 'lexicon', 'pt.json.gz'), cedilla_to='c')
    s_build_c = score(build, key, lex_c, cedilla_to='c')[0]
    s_held_c = score(held, key, lex_c, cedilla_to='c')[0]

    toks = [t for _, ts in held for t in ts]
    unkeyed = sorted({t for t in toks if t is not None and t < 60 and t not in key})
    result = {
        'key_numbers': len(key), 'lexicon_skeletons': len(lex),
        'build_lines': len(build), 'build_letters': n_build, 'S_build': round(s_build, 4),
        'held_lines': len(held), 'held_tokens': len(toks), 'held_letters': n_held, 'S_held': round(s_held, 4),
        'threshold_0.85xS_build': round(threshold, 4),
        'shuffled_n': N_SHUFFLED, 'seed': SEED, 'mean_shuffled': round(sum(null) / len(null), 4),
        'best_shuffled': round(best_null, 4), 'margin': round(margin, 4),
        'too_small': too_small, 'pass': passed,
        'held_unread_signs': sum(1 for t in toks if t is None),
        'held_code_group_tokens': sum(1 for t in toks if t is not None and t >= 60),
        'held_code_groups': sorted({t for t in toks if t is not None and t >= 60}),
        'held_unkeyed_numbers_below_60': unkeyed,
        'held_unkeyed_tokens': sum(1 for t in toks if t in unkeyed),
        'secondary_cedilla_to_c': {'S_build': round(s_build_c, 4), 'S_held': round(s_held_c, 4)},
    }
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'test_m0271_result.json'), 'w', encoding='utf-8') as fh:
        json.dump(result, fh, indent=1)
        fh.write('\n')
    with open(os.path.join(HERE, 'results', 'test_m0271_output.txt'), 'w', encoding='utf-8') as fh:
        fh.write('# m0271 under the frozen key, line by line. Segments: the raw decrypt (# = number the key lacks), '
                 'then the normalised parse (UPPER = lexicon word of 3+ letters, lower = not covered).\n')
        for tag, segs, parses, lc, lt in rows:
            fh.write('%s  %d/%d\n  raw:   %s\n  parse: %s\n' % (tag, lc, lt, ' | '.join(segs), ' | '.join(parses)))
        fh.write('\nshuffled-key scores (sorted): %s\n' % ', '.join('%.3f' % x for x in sorted(null)))
    print(result)


if __name__ == '__main__':
    sys.exit(main())
