"""Disagreements between the two digital editions of Linear A, for reporting upstream.

lineara.xyz (R. Hogan, after GORILA via G. Douros) and SigLA (E. Salgarella and S. Castellan) are compared
word by word within each document that has one unique name in both (collate_sigla.py). For every SigLA
multi-sign word whose signs SigLA marks as confident and unerased, and which has no identical word in the
same lineara.xyz document, the closest lineara.xyz word (by sign-sequence similarity) is found and the
difference classified:

  substitution   same length, one sign differs
  indel          one sign more or less, the rest identical
  segmentation   the SigLA word equals two adjacent lineara.xyz words joined, or the reverse
  other          anything else (listed with the nearest candidate)
  no counterpart no lineara.xyz word shares half its signs

A disagreement is not an error in either edition: readings, ligatures and word division are editorial
choices. The list is a checklist for the editors, sorted with the most specific cases first. Corpus-level
problems found in earlier passes are appended.
"""
from collections import defaultdict
from difflib import SequenceMatcher
import json
from pathlib import Path
import re
import unicodedata as ud

ROOT = Path(__file__).resolve().parent
SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')


def canonical(ch):
    m = re.fullmatch(r'LINEAR A SIGN (AB|A)(\d+)([A-Z]*)', ud.name(ch, ''))
    return f'{m[1]}{int(m[2]):03d}' if m else None


def main():
    corpus = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
    unmatched = json.loads((ROOT / 'data/sigla_unmatched_words.json').read_text(encoding='utf-8'))
    by_name = defaultdict(list)
    for r in corpus:
        by_name[r['name'].replace(' ', '')].append(r)
    # sign id -> conventional value, learned from lineara.xyz words whose transliteration splits cleanly
    value = {}
    for r in corpus:
        for w, t in zip(r['words'], r['transliteratedWords']):
            ids = [canonical(c) for c in w]
            parts = t.translate(SUB).split('-')
            if ids and None not in ids and len(ids) == len(parts):
                for i, p in zip(ids, parts):
                    value.setdefault(i, p)
    show = lambda ids: '-'.join(value.get(i, i) if i else '?' for i in ids)
    out = []
    for u in unmatched:
        if not (u['confident_signs'] and u['unmarked']) or None in u['ids']:
            continue
        recs = by_name.get(u['document'].replace(' ', ''), [])
        if len(recs) != 1:
            continue
        r = recs[0]
        words = [(k, [canonical(c) for c in w if canonical(c)]) for k, w in enumerate(r['words'])]
        words = [(k, ids) for k, ids in words if ids]
        s = u['ids']
        best, kind = None, 'no counterpart'
        for j, (k, ids) in enumerate(words):
            joined = ids + (words[j + 1][1] if j + 1 < len(words) else [])
            if joined == s and j + 1 < len(words):
                best, kind = (k, joined), 'segmentation'
                break
            ratio = SequenceMatcher(None, s, ids).ratio()
            if best is None or ratio > best[2]:
                best = (k, ids, ratio)
        if kind != 'segmentation' and best is not None:
            k, ids, ratio = best
            if len(ids) == len(s) and sum(a != b for a, b in zip(ids, s)) == 1:
                kind = 'substitution'
            elif abs(len(ids) - len(s)) == 1 and SequenceMatcher(None, s, ids).ratio() >= 2 * min(len(s), len(ids)) / (len(s) + len(ids)) - 1e-9:
                kind = 'indel'
            elif ratio >= 0.5:
                kind = 'other'
            else:
                kind = 'no counterpart'
        k, ids = best[0], best[1]
        out.append({'document': u['document'], 'kind': kind, 'sigla_word_index': u['word_index'],
                    'sigla': show(s).upper(), 'lineara_xyz': show(ids).upper() if kind != 'no counterpart' else None,
                    'lineara_xyz_word_position': k if kind != 'no counterpart' else None,
                    'sigla_url': 'https://sigla.phis.me/document/' + u['document'].replace(' ', '%20') + '/'})
    order = {'substitution': 0, 'indel': 1, 'segmentation': 2, 'other': 3, 'no counterpart': 4}
    out.sort(key=lambda x: (order[x['kind']], x['document']))
    corpus_level = [
        {'document': 'HT34', 'issue': 'KI-RO quantity given as 37; GORILA and Younger read 30 with a 7 erased (30 [[7]]).'
                      ' On the tablet 100 - 70 = 30 (SA+MU+KU 100, PA3 70, KI-RO 30).'},
        {'document': 'KH101', 'issue': 'Two records share the name KH101; one has an empty transcription.'},
        {'document': 'KNZg57b', 'issue': 'Glyph array present but no transliteration array; KNZg58 is an empty record.'
                      ' Both are faces of the Anetaki ivory sceptre (Kanta et al., Ariadne 2025).'},
    ]
    counts = {k: sum(1 for x in out if x['kind'] == k) for k in order}
    res = {'method': __doc__.strip(), 'counts': counts, 'word_disagreements': out, 'corpus_level': corpus_level}
    (ROOT / 'errata_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(counts)
    for x in out[:40]:
        print(f"  {x['document']:12} {x['kind']:13} SigLA {x['sigla']:22} lineara.xyz {x['lineara_xyz']}")


if __name__ == '__main__':
    main()
