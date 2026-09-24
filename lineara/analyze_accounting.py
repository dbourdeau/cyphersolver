"""Exploratory accounting audit, using raw sign identities and Unicode numerals.

No supplied translations or transliterated numbers enter the arithmetic.
All candidate rankings are exploratory, not an independent decipherment test.
"""
from collections import Counter, defaultdict
from fractions import Fraction
import json
from pathlib import Path
import unicodedata as ud

ROOT = Path(__file__).resolve().parent
ROWS = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
DAMAGE = '\U0001076b'
DIVIDER = '\U00010101'
KIRO = '\U00010638\U00010601'
KURO = '\U00010642\U00010601'
FRACTIONS = {'\U00010743': Fraction(1, 4), '\U00010746': Fraction(1, 2),
             '\U00010755': Fraction(3, 4)}

def integer(s):
    if s and all(ud.name(c, '').startswith('AEGEAN NUMBER ') for c in s):
        return sum(int(ud.numeric(c)) for c in s)
    return None

def quantity(s):
    n = integer(s)
    if n is not None:
        return Fraction(n)
    if s and all(c in FRACTIONS for c in s):
        return sum((FRACTIONS[c] for c in s), Fraction())
    return None

def tokens(row):
    # Newlines in words are editorial entry boundaries, not physical lines.
    # Remove only newlines; preserve dividers, damage, and the horizontal rule.
    out = []
    for raw in row['words']:
        if raw.isspace():
            continue
        n = quantity(raw)
        if n is not None and out and out[-1]['n'] is not None:
            out[-1]['n'] += n
            out[-1]['raw'] += raw
        else:
            out.append({'raw': raw, 'n': n})
    return out

def word(s):
    return len(s) >= 2 and all(0x10600 <= ord(c) <= 0x10655 for c in s)

def following_kind(s):
    if s is None:
        return 'end_of_record'
    clean = s.replace(DAMAGE, '')
    if clean and all(ud.name(c, '').startswith('AEGEAN NUMBER ') or 0x10740<=ord(c)<=0x1075f for c in clean):
        return 'damaged_quantity' if DAMAGE in s else 'quantity_signs'
    return 'other_sign_group'

def label(s):
    return '-'.join(ud.name(c, f'U+{ord(c):04X}').replace('LINEAR A SIGN ', '') for c in s)

def scan():
    name_counts = Counter(r['name'] for r in ROWS)
    tablet_rows = [r for r in ROWS if r['support'] == 'Tablet']
    mismatch_classes = Counter()
    for r in ROWS:
        a = ''.join(r['transcription'].split())
        b = ''.join(''.join(r['words']).split())
        if a == b:
            mismatch_classes['identical_ignoring_whitespace'] += 1
        elif not a:
            mismatch_classes['empty_transcription_field'] += 1
        elif a.replace(DAMAGE, '') == b.replace(DAMAGE, ''):
            mismatch_classes['damage_marker_placement_only'] += 1
        else:
            mismatch_classes['other_difference_needs_classification'] += 1
    result = {'method': 'Exploratory prefix-sum screen: unique-name tablet records; sections split at horizontal rules; exclude sections containing damage or fractional signs; candidate is a multi-sign group directly followed by an integer; at least two preceding numeric entries. No commodity equivalence assumed, so failures are not lexical falsifications.',
              'records': len(ROWS), 'distinct_names': len(name_counts),
              'duplicate_names': {k:v for k,v in name_counts.items() if v>1},
              'alignment_mismatches': [r['source_key'] for r in ROWS if len(r['words']) != len(r['transliteratedWords'])],
              'words_vs_transcription_mismatches': [r['source_key'] for r in ROWS
                  if ''.join(r['transcription'].split()) != ''.join(''.join(r['words']).split())],
              'tablet_records': len(tablet_rows),
              'field_comparison_categories':dict(mismatch_classes),
              'known_limitations': ['Missing uncertainty marks in upstream data are not repaired by this filter.', 'Record names are not necessarily independent artefacts; recto/verso can share an object.', 'Numeric quantities can denote different commodities.', 'Transcription and words may disagree.'],
              'kiro_occurrences': [], 'prefix_sum_candidates': []}
    # Labels are for display only; grouping uses glyph strings.
    aliases = defaultdict(set)
    for r in ROWS:
        if len(r['words']) == len(r['transliteratedWords']):
            for raw, alias in zip(r['words'], r['transliteratedWords']):
                aliases[raw].add(alias)
    candidates = defaultdict(list)
    for r in tablet_rows:
        ts = tokens(r)
        for i,t in enumerate(ts):
            if t['raw'].replace(DAMAGE, '') == KIRO:
                j = i+1
                while j<len(ts) and ts[j]['raw'] == DIVIDER:
                    j += 1
                result['kiro_occurrences'].append({'document':r['name'], 'token_index':i,
                    'damaged_marker':DAMAGE in t['raw'],
                    'following_kind':following_kind(ts[j]['raw'] if j<len(ts) else None),
                    'next_raw':ts[j]['raw'] if j<len(ts) else None,
                    'next_value':str(ts[j]['n']) if j<len(ts) and ts[j]['n'] is not None else None,
                    'scribe':r['scribe']})
        if name_counts[r['name']] != 1:
            continue
        sections = [[]]
        for t in ts:
            if t['raw'] == '—':
                sections.append([])
            else:
                sections[-1].append(t)
        for section_id, section in enumerate(sections):
            joined = ''.join(t['raw'] for t in section)
            if DAMAGE in joined or any(0x10740 <= ord(c) <= 0x1075f for c in joined):
                continue
            for i,t in enumerate(section):
                if not word(t['raw']):
                    continue
                j = i+1
                while j<len(section) and section[j]['raw']==DIVIDER:
                    j += 1
                before = [z['n'] for z in section[:i] if z['n'] is not None]
                if len(before)<2 or j==len(section) or section[j]['n'] is None:
                    continue
                stated = section[j]['n']
                total = sum(before)
                candidates[t['raw']].append({'document':r['name'], 'section':section_id,
                    'preceding_values':[str(x) for x in before], 'sum':str(total),
                    'following_number':str(stated), 'match':total==stated})
    for raw, cases in candidates.items():
        result['prefix_sum_candidates'].append({'sign_ids':label(raw),'display':sorted(aliases[raw]),
            'matches':sum(x['match'] for x in cases),'opportunities':len(cases),'cases':cases})
    result['prefix_sum_candidates'].sort(key=lambda x:(-x['matches'],-x['opportunities'],x['sign_ids']))
    # A separate, preselected replication of known headed lists.
    controls = []
    for name in ['HT88','HT94b','HT117a']:
        r = next(r for r in ROWS if r['name']==name)
        ts = tokens(r)
        a = next(i for i,t in enumerate(ts) if t['raw']==KIRO)
        b = next(i for i in range(a+1,len(ts)) if ts[i]['raw']==KURO)
        block = ts[a+1:b]
        entries = [t['n'] for t in block if t['n'] is not None]
        assert DAMAGE not in ''.join(t['raw'] for t in block)
        assert all(n.denominator==1 for n in entries)
        total = ts[b+1]['n']
        controls.append({'document':name,'scribe':r['scribe'],'entries':[int(n) for n in entries],
                         'sum':int(sum(entries)), 'stated_total':int(total),'matches':sum(entries)==total})
    result['headed_list_replications'] = controls
    # Exact arithmetic consistency check; X cancels, so no X value is assumed.
    # HT123+124a, rows 1 and 2: 31*r=8+E+1+X; (31+J)*r=8+J+E+X.
    j = Fraction(1,2)
    inferred_ratio = (j - 1) / j
    result['ht123_ratio_check'] = {'assumptions':['KI-RO numbers add to *308 amounts',
        'same positive ratio applies to the first two rows', 'same X sign has same numeric value',
        'J=1/2; transcription is correct'],
        'equations':['31*r = 8+E+1+X', '(31+J)*r = 8+J+E+X'],
        'derived_relation':'J*r = J-1', 'implied_ratio':str(inferred_ratio),
        'positive_ratio_possible':inferred_ratio>0,
        'interpretation':'The conjunction of assumptions fails. It does not individually refute KI-RO=deficit. Younger already reports a discrepancy here.'}
    # Integrity controls: expected exact sums and a deliberate off-by-one perturbation.
    assert all(c['matches'] for c in controls)
    assert all(sum(c['entries']) != c['stated_total']+1 for c in controls)
    assert inferred_ratio == -1
    (ROOT/'accounting_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Measurement export: code points in the segmented glyph field, not words or
    # phonemes. Include encoded Linear A signs and Aegean numerals only. This is
    # the digital snapshot's count, not the archaeological corpus's sign count.
    lines = []
    for r in ROWS:
        signs = [f'U+{ord(c):05X}' for w in r['words'] for c in w
                 if ud.name(c, '').startswith(('LINEAR A SIGN ', 'AEGEAN NUMBER '))]
        lines.extend(['# '+r['source_key'], ' '.join(signs)])
    (ROOT/'data/corpus_symbols.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['kiro_occurrences','prefix_sum_candidates','words_vs_transcription_mismatches']},ensure_ascii=False,indent=2))
    print('CANDIDATE RANKING')
    for x in result['prefix_sum_candidates'][:12]:
        print(x['display'],x['matches'], '/',x['opportunities'], [c['document'] for c in x['cases'] if c['match']])
    print('KI-RO contexts:',len(result['kiro_occurrences']))

if __name__ == '__main__':
    scan()
