"""Do proposed relatives of Minoan match Linear A better than languages that cannot be related?

Each lexicon's words are spelled by fixed Linear B rules (decided before any result was seen):
  * letters normalised: s-like -> s; t, th -> t; k, g, q, kh, h-dot, h-breve, x, gh -> k; b, p, ph, f -> p;
    d, dh -> d; l -> r; y -> j; v -> w; glottal and pharyngeal stops and plain h dropped; long vowels,
    doubled letters and tones collapsed;
  * every vowel starts a syllable with the consonant just before it (or none);
  * a consonant before another consonant is dropped if it is s, r, m or n, otherwise written with the
    next vowel; a word-final consonant is dropped.
Exact matches with Linear A word types (3+ signs) are counted for each lexicon and compared with the
matches its own syllables give when shuffled across its words (word lengths kept, 1,000 runs). Real
words beat that null even in unrelated languages, so the test that counts is family against controls:
a proposed relative should exceed its null by more than the controls exceed theirs (binomial split of
all matches in proportion to the null expectations). Proposed: Luwian (Melchert 1993), Akkadian and
Ugaritic (Semitic), Hurrian (Laroche 1980), Etruscan (Tyrsenian). Not proposed: Greek (60,000 Kaikki entries), Sumerian.
Controls: Hawaiian, Maori, Samoan, Tongan, Yoruba. Egyptian (no vowels) and Hittite (481 mostly
logographic entries) are left out. Hurrian is tested with h read as dropped and, as a check, as h-breve (k).
Positive control and power: the same rules and null applied to Greek against the Linear B vocabulary,
the one case where the relation is known, and an equal-size Greek sample against 491 random Linear B
types (the size of the Linear A target).
The semantic check asks, for the three Linear A words whose sense is known from the arithmetic
(KU-RO total, KI-RO deficit, PO-TO-KU-RO grand total), whether any language supplies a same-spelled word
with a fitting meaning, and how often a control language does the same.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import random
import re
import unicodedata as ud

ROOT = Path(__file__).resolve().parent.parent
LEX = ROOT / 'data/lexica'
VOW = set('aeiou')
MAP = [('sh', 's'), ('th', 't'), ('kh', 'k'), ('ph', 'p'), ('dh', 'd'), ('gh', 'k'), ('ng', 'n'), ('gb', 'k'),
       ('kp', 'k'), ('ts', 'z')]
CHAR = {'š': 's', 'ś': 's', 'ṣ': 's', 'ṯ': 's', 'ṡ': 's', 'ẓ': 'z', 'ṭ': 't', 'θ': 't', 'ṭ': 't', 'ḳ': 'k',
        'q': 'k', 'g': 'k', 'ḫ': 'k', 'ḥ': 'k', 'x': 'k', 'ġ': 'k', 'ẖ': 'k', 'c': 'k', 'æ': 'k', 'b': 'p',
        'f': 'p', 'ḏ': 'd', 'ð': 'd', 'l': 'r', 'y': 'j', 'v': 'w', 'ŋ': 'n', 'ə': 'e', 'ü': 'u', 'ö': 'o',
        'ɛ': 'e', 'ɔ': 'o'}
DROP = set("ʔʕʾʿ'’h-·.=˚*()[]/ ")


def spell(word):
    """Linear B-style syllable spelling of a romanised word, or None."""
    w = ud.normalize('NFD', word.lower())
    w = ''.join(ch for ch in w if not ud.combining(ch) or ch in '̱')  # strip accents, tones, macrons
    w = ud.normalize('NFC', w)
    for a, b in MAP:
        w = w.replace(a, b)
    w = ''.join(CHAR.get(ch, ch) for ch in w)
    w = ''.join(ch for ch in w if ch not in DROP)
    if not w or any(ch not in VOW and ch not in 'dkmnprstwzj' for ch in w):
        return None
    w = re.sub(r'(.)\1+', r'\1', w)  # geminates and long vowels
    out, i = [], 0
    while i < len(w):
        ch = w[i]
        if ch in VOW:
            out.append(ch)
            i += 1
            continue
        nxt = w[i + 1] if i + 1 < len(w) else None
        if nxt is None:
            i += 1  # final consonant dropped
        elif nxt in VOW:
            out.append(ch + nxt)
            i += 2
        else:
            if ch not in 'srmn':  # stop before consonant: written with the next vowel
                v = next((c for c in w[i + 1:] if c in VOW), None)
                if v:
                    out.append(ch + v)
            i += 1
    return tuple(out) if out else None


def kaikki(name, field):
    words = []
    for line in open(LEX / f'{name}.jsonl', encoding='utf-8'):
        r = json.loads(line)
        if r.get('pos') in ('character', 'symbol', 'romanization', 'letter', 'suffix', 'prefix', 'affix', 'infix'):
            if not (field == 'romanization-entry' and r.get('pos') == 'romanization'):
                continue
        g = '; '.join(g for s in r.get('senses', []) for g in s.get('glosses', [])[:1])
        if field == 'word':
            forms = [r['word']]
        elif field == 'romanization-entry':
            if r.get('pos') != 'romanization':
                continue
            forms = [r['word']]
        else:  # vocalised romanization in forms
            roms = [f['form'] for f in r.get('forms', []) if 'romanization' in f.get('tags', [])]
            forms = [x for x in roms if any(c in 'aeiouāēīūâêîûàá' for c in x)][:1]
        for f in forms:
            if ' ' not in f.strip():
                words.append((f, g))
    return words


def luwian():
    t = (LEX / 'LUVLEX.txt').read_text(encoding='utf-8')
    words = []
    for block in t.split('_' * 20):
        lines = [l.strip() for l in block.strip('_\n ').splitlines() if l.strip()]
        if len(lines) < 2:
            continue
        head = re.sub(r'^\(?˚?\)?\*?\[?', '', lines[0]).strip(']')
        gloss = lines[1] if lines[1].startswith(("'", '"', '‘')) else ''
        if not re.match(r"^[a-zāēīūšæḫ()/\-]+$", head):
            continue
        stem = re.sub(r'\([^)]*\)', '', head.split('/')[0]).rstrip('-')
        if len(stem) >= 2:
            words.append((stem, gloss.strip("'")))
    return words


def hurrian():
    """Headwords of Laroche, Glossaire de la langue hourrite (1980), from the Internet Archive OCR text
    (local cache only). OCR usually gives h-breve as plain h, which the spelling rules drop."""
    t = (LEX / 'laroche_glh.txt').read_text(encoding='utf-8').splitlines()
    end = next(i for i in range(18500, len(t)) if t[i].strip().startswith('zugulluhli')) + 5
    out = []
    for i in range(1580, end):
        m = re.fullmatch(r"([a-zšḫṯ][a-zšḫṯ]{1,18})-?(?:\s+[\"“]([^\"”]{1,60})[\"”]?)?", t[i].strip())
        if m:
            out.append((m.group(1), m.group(2) or ''))
    return out


SOURCES = {
    'Luwian': ('proposed', luwian),
    'Hurrian': ('proposed', hurrian),
    'Akkadian': ('proposed', lambda: kaikki('Akkadian', 'word')),
    'Ugaritic': ('proposed', lambda: kaikki('Ugaritic', 'forms')),
    'Etruscan': ('proposed', lambda: kaikki('Etruscan', 'romanization-entry')),
    'Greek': ('not proposed', lambda: greek_words()),
    'Sumerian': ('not proposed', lambda: kaikki('Sumerian', 'romanization-entry')),
    'Hawaiian': ('control', lambda: kaikki('Hawaiian', 'word')),
    'Maori': ('control', lambda: kaikki('Maori', 'word')),
    'Samoan': ('control', lambda: kaikki('Samoan', 'word')),
    'Tongan': ('control', lambda: kaikki('Tongan', 'word')),
    'Yoruba': ('control', lambda: kaikki('Yoruba', 'word')),
}
KNOWN = {('ku', 'ro'): 'total', ('ki', 'ro'): 'deficit / owed', ('po', 'to', 'ku', 'ro'): 'grand total'}
FIT = {('ku', 'ro'): r'\b(all|whole|total|sum|entire|every|complete)', ('ki', 'ro'): r'\b(debt|owe|lack|deficit|missing|remain|short)',
       ('po', 'to', 'ku', 'ro'): r'\b(all|whole|total|sum)'}


def la_types():
    rows = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
    sub = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
    out = defaultdict(set)
    for r in rows:
        for t in r['transliteratedWords']:
            t = t.translate(sub).strip().lower()
            parts = t.split('-')
            if len(parts) >= 2 and all(re.match(r'^[a-z]+[0-9]?$', p) for p in parts):
                out[tuple(parts)].add(r['name'])
    return out


GREEK = dict(zip('αβγδεζηθικλμνξοπρστυφχψωϝς', ['a', 'b', 'g', 'd', 'e', 'z', 'e', 'th', 'i', 'k', 'l', 'm', 'n', 'ks', 'o', 'p', 'r', 's', 't', 'u', 'ph', 'kh', 'ps', 'o', 'w', 's']))


def greek_words():
    """Ancient Greek lemmas not chosen for any link to Linear B: the first 60,000 entries of the
    Kaikki Ancient Greek extract (all letters of the alphabet), romanised. The positive control."""
    out = []
    for line in open(LEX / 'AncientGreek_head.jsonl', encoding='utf-8'):
        r = json.loads(line)
        if r.get('pos') not in ('noun', 'adj', 'name', 'verb'):
            continue
        g = ud.normalize('NFD', r['word'].lower())
        g = ''.join(ch for ch in g if not ud.combining(ch))
        if ' ' in g or '-' in g:
            continue
        out.append((''.join(GREEK.get(ch, ch) for ch in g), ''))
    return out


def lb_types():
    import names_lb
    sites, _ = names_lb.lb_vocabulary()
    return {w for w in sites if len(w) >= 3}


def shuffle_null(forms3, target, rng, reps):
    """Matches expected from the language's own syllables: shuffle syllables across its forms, lengths kept."""
    pool = [x for f in forms3 for x in f]
    lens = [len(f) for f in forms3]
    out = []
    for _ in range(reps):
        rng.shuffle(pool)
        k, n = 0, 0
        for L in lens:
            if tuple(pool[k:k + L]) in target:
                n += 1
            k += L
        out.append(n)
    return out


def score(forms, target, rng, reps):
    f3 = [s for s in forms if len(s) >= 3]
    hits = sorted(s for s in f3 if s in target)
    null = shuffle_null(f3, target, rng, reps)
    mean = sum(null) / reps
    return f3, hits, {'forms_3plus': len(f3), 'matches': len(hits), 'per_1000': round(1000 * len(hits) / max(1, len(f3)), 2),
                      'shuffle_null_mean': round(mean, 2),
                      'ratio_to_null': round(len(hits) / mean, 2) if mean else None,
                      'p_ge': round((sum(n >= len(hits) for n in null) + 1) / (reps + 1), 4)}


def main(reps=1000, seed=20260923):
    la = la_types()
    la3 = {w for w in la if len(w) >= 3}
    rng = random.Random(seed)
    res = {'method': __doc__.strip(), 'linear_a_types_3plus': len(la3), 'reps': reps, 'languages': {},
           'positive_control_vs_linear_b': {}}
    lex = {}
    for name, (kind, fn) in SOURCES.items():
        forms = {}
        for word, gloss in fn():
            sp = spell(word)
            if sp and len(sp) >= 2:
                forms.setdefault(sp, (word, gloss))
        lex[name] = (kind, forms)
        f3, hits, st = score(forms, la3, rng, reps)
        known = {'-'.join(k): [{'word': forms[k][0], 'gloss': forms[k][1][:80],
                               'fits': bool(re.search(FIT[k], forms[k][1].lower()))}] if k in forms else []
                 for k in KNOWN}
        res['languages'][name] = dict(kind=kind, **st, matches_list=[
            {'linear_a': '-'.join(h).upper(), 'word': forms[h][0], 'gloss': forms[h][1][:80], 'la_records': sorted(la[h])[:4]}
            for h in hits], known_sense_words=known)
    # positive control: Greek against the Linear B word list, controls against the same list
    lb3 = lb_types()
    gforms = {}
    for w, g in greek_words():
        sp = spell(w)
        if sp and len(sp) >= 2:
            gforms.setdefault(sp, (w, g))
    # like-for-like power: equal-size lexicon samples against a 491-type sample of Linear B
    sizes = {n: res['languages'][n]['forms_3plus'] for n in ('Akkadian', 'Ugaritic', 'Luwian')}
    g3 = [x for x in gforms if len(x) >= 3]
    lb_list = sorted(lb3)
    power = {}
    for n, size in sizes.items():
        hits = []
        for _ in range(200):
            tgt = set(rng.sample(lb_list, len(la3)))
            hits.append(sum(1 for x in rng.sample(g3, size) if x in tgt))
        hits.sort()
        power[n] = {'lexicon_size': size, 'greek_vs_lb491_mean': round(sum(hits) / len(hits), 2),
                    'greek_vs_lb491_90ci': [hits[10], hits[189]], 'observed_vs_linear_a': res['languages'][n]['matches']}
    res['power_like_for_like'] = power
    for name, forms in [('Greek (true relative)', gforms)] + [(n, lex[n][1]) for n in ('Hawaiian', 'Maori', 'Yoruba', 'Akkadian', 'Ugaritic', 'Luwian')]:
        _, hits, st = score(forms, lb3, rng, reps)
        res['positive_control_vs_linear_b'][name] = st
    # Group test: does a proposed family exceed chance MORE than the controls do? Given all matches of
    # the group and the controls, split them in proportion to each side's shuffle-null expectation.
    from math import comb
    L = res['languages']
    ctrl = [n for n, v in L.items() if v['kind'] == 'control']
    groups = {'Semitic (Akkadian, Ugaritic)': ['Akkadian', 'Ugaritic'], 'Anatolian (Luwian)': ['Luwian'],
              'Hurro-Urartian (Hurrian)': ['Hurrian'],
              'Tyrsenian (Etruscan)': ['Etruscan']}
    co = sum(L[n]['matches'] for n in ctrl)
    ce = sum(L[n]['shuffle_null_mean'] for n in ctrl)
    res['group_tests'] = {}
    for g, members in groups.items():
        go = sum(L[n]['matches'] for n in members)
        ge = sum(L[n]['shuffle_null_mean'] for n in members)
        n, q = go + co, ge / (ge + ce)
        p_val = sum(comb(n, k) * q ** k * (1 - q) ** (n - k) for k in range(go, n + 1)) if n else 1.0
        res['group_tests'][g] = {'observed': go, 'shuffle_expected': round(ge, 2),
                                 'ratio': round(go / ge, 2) if ge else None, 'controls_ratio': round(co / ce, 2),
                                 'p_exceeds_controls': round(p_val, 3), 'bonferroni_4_groups': round(min(1, 4 * p_val), 3)}
    (ROOT / 'reading/lang_test_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('Group tests (excess over own-syllable null, compared with the controls):')
    for g, v in res['group_tests'].items():
        print(f"  {g:30} obs {v['observed']} exp {v['shuffle_expected']} ratio {v['ratio']} vs controls "
              f"{v['controls_ratio']}  p {v['p_exceeds_controls']} (x4: {v['bonferroni_4_groups']})")
    print(f'Linear A types (3+ signs): {len(la3)}')
    print(f"{'language':10} {'kind':13} {'forms3+':>7} {'hits':>4} {'/1000':>6} {'null':>6} {'ratio':>6} {'p':>7}  known-sense look-alikes")
    for name, v in res['languages'].items():
        ks = '; '.join(f"{k}={x[0]['word']}({'fits' if x[0]['fits'] else 'no fit'})" for k, x in v['known_sense_words'].items() if x)
        print(f"{name:10} {v['kind']:13} {v['forms_3plus']:7} {v['matches']:4} {v['per_1000']:6} {v['shuffle_null_mean']:6} {str(v['ratio_to_null']):>6} {v['p_ge']:7}  {ks}")
    print('Power, like for like (Greek sample of the same size vs 491 Linear B types):')
    for n, v in res['power_like_for_like'].items():
        print(f"  {n:9} size {v['lexicon_size']}: a Greek-like relative gives {v['greek_vs_lb491_mean']} {v['greek_vs_lb491_90ci']}; observed with Linear A {v['observed_vs_linear_a']}")
    print('Positive control: each lexicon against Linear B word types (3+ signs):', len(lb3))
    for name, v in res['positive_control_vs_linear_b'].items():
        print(f"  {name:24} forms {v['forms_3plus']:5} hits {v['matches']:4} /1000 {v['per_1000']:7} null {v['shuffle_null_mean']:6} ratio {v['ratio_to_null']} p {v['p_ge']}")


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
