"""Structural reading of the whole Linear A working corpus.

Every token of every record gets one class and, where the evidence allows, a gloss:

  read as sense   number, fraction, commodity logogram, accounting term, validated toponym
  read as sound   syllabic word whose sign values carry over from Linear B (soundvalues.py),
                  with its function in the document: heading, entry label, formula word, other
  unread          unidentified logogram or sign (*301, A-numbers), single signs of unknown use
  apparatus       dividers, damage, rules (not counted)

Glosses are deliberately few and each has a stated basis. Commodity logograms follow the GORILA
labels, which rest on Linear B continuity of sign shape and use. Fraction values are those of
Corazza et al. 2021, except H and A, which fraction_constraints.py disputes and which stay unglossed.
Totals are checked with exact fractions; every KU-RO / PO-TO-KU-RO is tested against several
section windows so that a balance found by choosing a window is reported as such.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
from pathlib import Path
import re
import unicodedata as ud

ROOT = Path(__file__).resolve().parent.parent
ROWS = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
NAMECOUNT = Counter(r['name'] for r in ROWS)
SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
DAMAGE, DIVIDER, RULE = '\U0001076b', '\U00010101', '—'
SYL = re.compile(r'^[A-Z]+[0-9]?$')

FRACTION_VALUES = {'J': F(1, 2), 'E': F(1, 4), 'F': F(1, 8), 'B': F(1, 5), 'D': F(1, 6), 'K': F(1, 10),
                   'L2': F(1, 20), 'L3': F(1, 30), 'L4': F(1, 40), 'L6': F(1, 60), 'JE': F(3, 4)}
FRACTION_DISPUTED = {'H', 'A'}  # see FRACTIONS_REPORT.md

COMMODITIES = {  # GORILA labels; meanings from Linear B continuity (Ventris-Chadwick ideograms)
    'GRA': 'grain', 'VIN': 'wine', 'OLIV': 'olives', 'OLE': 'oil', 'CYP': 'cyperus (aromatic sedge)',
    'VIR': 'man/men', 'HIDE': 'hide', 'AROM': 'aromatic', 'CAP': 'goat', 'TELA': 'cloth', 'OVIS': 'sheep',
    'SUS': 'pig', 'BOS': 'cattle', 'FIC': 'figs', 'VAS': 'vessel', 'TWE': 'vessel (TWE)', 'GAL': 'milk?',
}
TERMS = {  # accounting vocabulary; basis in RESEARCH_REPORT.md and FRACTIONS_REPORT.md
    'KU-RO': ('total', 'balances list sums on HT 88, 94b, 117a, 104 and others (tested here)'),
    'PO-TO-KU-RO': ('grand total', 'sums KU-RO subtotals (HT 122b; Younger); position after KU-RO lines'),
    'KI-RO': ('deficit / amount owed', 'heads lists that KU-RO totals (HT 88, 94b, 117a); remainder 100-70=30 on HT 34.6'),
}
TOPONYMS = {  # exact matches to Linear B place names, significant against a null (soundvalues.py)
    'PA-I-TO': 'Phaistos (LB pa-i-to)', 'SU-KI-RI-TA': 'Sybrita (LB su-ki-ri-ta)', 'SE-TO-I-JA': 'Setoija (LB se-to-i-ja)',
}
TOPONYMS_PROPOSED = {  # published proposals, not validated by the test here
    'TU-RU-SA': 'Tylissos? (LB tu-ri-so)', 'KU-DO-NI': 'Kydonia? (LB ku-do-ni-ja)', 'DI-KI-TE': 'Dikte?',
    'I-DA': 'Ida?', 'A-SE-SA-RA': 'libation-formula word', 'RU-KI-TO': 'Lyktos? (LB ru-ki-to)',
}
CORR = json.loads((ROOT / 'reading/corrections.json').read_text(encoding='utf-8'))['corrections']
TRANSACTION = {  # recurrent administrative words; function from distribution (READING.md), meaning unknown
    'SA-RA2': 'transaction term (grain, cyperus; Haghia Triada only)', 'A-DU': 'heading term (with VIR, GRA)',
    'KA-PA': 'heading term', 'TE': 'heading abbreviation (with VIN, GRA)', 'PA3': 'subtraction term? (HT 34.6, HT 9)',
}
ADMIN = {'Tablet', 'Lames (short thin tablet)', '3-sided bar', '4-sided bar', 'Label'}
SEALINGS = {'Nodule', 'Roundel', 'Sealing'}


def is_number(w):
    return bool(w) and all(ud.name(c, '').startswith('AEGEAN NUMBER') for c in w)


def is_fraction_char(c):
    return 0x10740 <= ord(c) <= 0x1075f


def fraction_value(w):
    """Value of a run of fraction signs, or None if any sign is unvalued."""
    total = F(0)
    for c in w:
        if c == DAMAGE:
            continue
        s = ud.name(c).split()[-1]
        if s not in FRACTION_VALUES:
            return None
        total += FRACTION_VALUES[s]
    return total


def classify_record(r):
    """Tokens with class and gloss; entry = editorial line (newline-separated)."""
    toks = []
    entry = 0
    words = r['words']
    trans = r['transliteratedWords'] if len(r['transliteratedWords']) == len(words) else [''] * len(words)
    for w, t in zip(words, trans):
        if w == '\n':
            entry += 1
            continue
        t = (t or '').translate(SUB).strip()
        tok = {'glyphs': w, 'label': t, 'entry': entry, 'damaged': DAMAGE in w}
        core = w.replace(DAMAGE, '')
        if w == DIVIDER or t == RULE or w == RULE or not core:
            tok['cls'] = 'apparatus'
        elif is_number(core):
            tok['cls'] = 'number'
            tok['value'] = sum(int(ud.numeric(c)) for c in core)
        elif all(is_fraction_char(c) for c in core):
            v = fraction_value(core)
            signs = [ud.name(c).split()[-1] for c in core]
            tok['fraction_signs'] = signs
            if v is not None:
                tok['cls'], tok['value'] = 'fraction', v
            elif set(signs) & FRACTION_DISPUTED:
                tok['cls'] = 'fraction-disputed'
            else:
                tok['cls'] = 'fraction-unvalued'
        elif all(is_number(c) or is_fraction_char(c) or c == DAMAGE for c in core):
            tok['cls'] = 'quantity-mixed'
        elif t in TERMS:
            tok['cls'], tok['gloss'] = 'term', TERMS[t][0]
        elif t in TOPONYMS:
            tok['cls'], tok['gloss'] = 'toponym', TOPONYMS[t]
        else:
            heads = re.findall(r'[A-Z]{3,}', t)
            com = [h for h in heads if h in COMMODITIES]
            if com and not re.fullmatch(r'[A-Z0-9]+(-[A-Z0-9]+)+', t):
                tok['cls'] = 'commodity'
                tok['gloss'] = COMMODITIES[com[0]] + (' (ligature ' + t + ')' if '+' in t else '')
            elif '-' in t and all(SYL.match(s) for s in t.split('-')):
                tok['cls'] = 'word'
                if t in TOPONYMS_PROPOSED:
                    tok['proposal'] = TOPONYMS_PROPOSED[t]
            elif '-' in t:
                tok['cls'] = 'word-with-unknown-sign'
            elif SYL.match(t):
                tok['cls'] = 'single-sign'
            else:
                tok['cls'] = 'unidentified-sign'
        toks.append(tok)
    for c in CORR:  # documented edition corrections
        if c['record'] != r['name']:
            continue
        for i, x in enumerate(toks):
            if x['label'] == c['find_label']:
                y = next((z for z in toks[i + 1:] if z['cls'] == 'number'), None)
                if y is not None and y['value'] == c['next_number_from']:
                    y['value'], y['corrected'] = c['next_number_to'], c['source']
    # Functions of words and single signs from their position.
    first_q = next((i for i, x in enumerate(toks) if x['cls'] in ('number', 'fraction', 'quantity-mixed',
                                                                  'fraction-disputed', 'fraction-unvalued')), None)
    support = r['support']
    vir_record = any(x['cls'] == 'commodity' and x['label'].startswith('VIR') for x in toks)
    for i, x in enumerate(toks):
        if x['cls'] not in ('word', 'word-with-unknown-sign', 'single-sign'):
            continue
        nxt = next((y for y in toks[i + 1:] if y['cls'] != 'apparatus'), None)
        same_entry_q = nxt is not None and nxt['entry'] == x['entry'] and nxt['cls'] in (
            'number', 'fraction', 'quantity-mixed', 'fraction-disputed', 'fraction-unvalued', 'commodity')
        if support in SEALINGS:
            x['function'] = 'sealing mark'
        elif support not in ADMIN:
            x['function'] = 'formula/votive'
        elif x['cls'] == 'single-sign' and same_entry_q:
            x['function'] = 'logogram/abbreviation'
            if x['label'] == 'NI':
                x['gloss'] = 'figs? (NI = LB *30 FIC)'
        elif same_entry_q:
            x['function'] = 'entry label'
            if x['label'] in TRANSACTION:
                x['role'] = TRANSACTION[x['label']]
            elif vir_record and x['cls'] == 'word':
                x['role'] = 'probable personal name (entry in a VIR list)'
        elif first_q is None or i < first_q:
            x['function'] = 'heading'
            if x['label'] in TRANSACTION:
                x['role'] = TRANSACTION[x['label']]
        else:
            x['function'] = 'in-list, no quantity'
    return toks


def attach_commodity(toks):
    """Commodity (logogram label) governing each quantity: nearest preceding commodity in the same entry."""
    cur, entry = None, None
    for x in toks:
        if x['entry'] != entry:
            cur, entry = None, x['entry']
        if x['cls'] == 'commodity':
            cur = re.findall(r'[A-Z]{3,}', x['label'])[0]
        elif x['cls'] in ('number', 'fraction'):
            x['commodity'] = cur


def totals(r, toks, prev_face=None):
    """Check each KU-RO / PO-TO-KU-RO followed by a quantity against section windows.
    prev_face: tokens of the other face of the same object (recto), prepended for a whole-object window."""
    out = []
    attach_commodity(toks)
    body = [x for x in toks if x['cls'] != 'apparatus' or x['label'] == RULE or x['glyphs'] == RULE]
    for i, x in enumerate(body):
        if x['label'] not in ('KU-RO', 'PO-TO-KU-RO'):
            continue
        # stated total: following quantity tokens in the same entry
        stated, j, dmg, unval = F(0), i + 1, False, False
        while j < len(body) and body[j]['entry'] == x['entry'] and body[j]['cls'] in (
                'number', 'fraction', 'fraction-disputed', 'fraction-unvalued', 'quantity-mixed', 'commodity'):
            if body[j]['cls'] in ('number', 'fraction'):
                stated += body[j]['value']
            elif body[j]['cls'] != 'commodity':
                unval = True
            dmg |= body[j]['damaged']
            j += 1
        if stated == 0:
            continue
        # candidate windows: since record start, last rule, last KU-RO/KI-RO/heading term
        starts = {'record start': 0}
        for k in range(i - 1, -1, -1):
            if body[k]['glyphs'] == RULE or body[k]['label'] == RULE:
                starts.setdefault('last rule', k + 1)
            if body[k]['label'] in ('KU-RO', 'KI-RO', 'PO-TO-KU-RO'):
                starts.setdefault('after last ' + body[k]['label'], k + 1)
        res = {}
        segs = {name: body[s:i] for name, s in starts.items()}
        if prev_face:
            segs['whole object (other face first)'] = [y for y in prev_face if y['cls'] != 'apparatus'] + body[:i]
            sub = [k for k, y in enumerate(prev_face) if y['label'] in ('KU-RO',)]
            if sub:  # grand total over subtotals of both faces
                segs['subtotals of both faces'] = [prev_face[k + 1] for k in sub if k + 1 < len(prev_face)] +                     [body[k + 1] for k in range(i) if body[k]['label'] == 'KU-RO' and k + 1 < i]
        tot_com = next((y for y in body[i + 1:j] if y['cls'] == 'commodity'), None)
        if tot_com is not None:
            c = re.findall(r'[A-Z]{3,}', tot_com['label'])[0]
            segs['same commodity since record start'] = [y for y in body[:i] if y.get('commodity') == c]
        for name, seg in segs.items():
            q = [y for y in seg if y['cls'] in ('number', 'fraction')]
            bad = any(y['cls'] in ('fraction-disputed', 'fraction-unvalued', 'quantity-mixed') for y in seg)
            d = any(y['damaged'] for y in seg)
            if len(q) >= 2:
                res[name] = {'sum': str(sum(y['value'] for y in q)), 'balances': sum(y['value'] for y in q) == stated,
                             'unvalued_or_disputed_signs': bad, 'damage': d}
        # post hoc: any contiguous run of quantities ending just before the total
        qs = [y for y in body[:i] if y['cls'] in ('number', 'fraction')]
        suffix = next((len(qs) - k for k in range(len(qs) - 1, -1, -1)
                       if len(qs) - k >= 2 and sum(y['value'] for y in qs[k:]) == stated), None)
        natural = any(v['balances'] for v in res.values())
        best = min((abs(F(v['sum']) - stated) for v in res.values()), default=None)
        out.append({'record': r['name'], 'term': x['label'], 'stated': str(stated), 'stated_damaged': dmg,
                    'stated_has_unvalued': unval, 'windows': res,
                    'balances_in_some_window': natural,
                    'post_hoc_suffix_entries': suffix,
                    'smallest_discrepancy': None if best is None else str(best),
                    'damage_in_windows': any(v['damage'] for v in res.values())})
    return out


def render(r, toks):
    """One-line-per-entry reading with glosses in brackets."""
    lines = defaultdict(list)
    for x in toks:
        if x['cls'] == 'apparatus':
            continue
        lab = x['label'] or '?'
        if x['cls'] == 'number':
            s = str(x['value']) + ('(corr.)' if x.get('corrected') else '')
        elif x['cls'] == 'fraction':
            s = str(x['value'])
        elif x['cls'] in ('fraction-disputed', 'fraction-unvalued'):
            s = '{' + ' '.join(x['fraction_signs']) + '}'
        elif x.get('gloss'):
            s = f"{lab} [{x['gloss']}]"
        elif x.get('role', '').startswith('probable personal name'):
            s = f"{lab} <name>"
        elif x.get('role'):
            s = f"{lab} <{x['role'].split(' (')[0]}>"
        else:
            s = lab
        if x['damaged'] and x['cls'] not in ('number',):
            s += '[?]'
        elif x['damaged']:
            s += '[?]'
        lines[x['entry']].append(s)
    return [' '.join(v) for _, v in sorted(lines.items())]


def main():
    records, checks = [], []
    faces = {}
    roles = Counter()
    cls_tokens, cls_signs = Counter(), Counter()
    func = Counter()
    heading_words = defaultdict(set)
    label_words = defaultdict(set)
    for r in ROWS:
        toks = classify_record(r)
        for x in toks:
            if x['cls'] == 'apparatus':
                continue
            key = x['cls'] + ('/' + x['function'] if 'function' in x else '')
            cls_tokens[key] += 1
            n = sum(1 for c in x['glyphs'] if c not in (DAMAGE, DIVIDER))
            cls_signs[key] += n
            if x.get('role'):
                roles[x['role']] += 1
            if x.get('function') == 'heading' and x['cls'] == 'word':
                heading_words[x['label']].add(r['name'])
            if x.get('function') == 'entry label' and x['cls'] == 'word':
                label_words[x['label']].add(r['name'])
        if NAMECOUNT[r['name']] == 1 and r['support'] in ADMIN:
            m = re.fullmatch(r'(.+?)b', r['name'])
            prev = faces.get(m.group(1) + 'a') if m else None
            checks.extend(totals(r, toks, prev))
            faces[r['name']] = toks
        records.append({'name': r['name'], 'site': r['site'], 'support': r['support'], 'scribe': r.get('scribe', ''),
                        'reading': render(r, toks),
                        'tokens': [{k: (str(v) if isinstance(v, F) else v) for k, v in x.items() if k != 'glyphs'}
                                   for x in toks]})
    sense = {'number', 'fraction', 'commodity', 'term', 'toponym'}
    sense_tok = sum(v for k, v in cls_tokens.items() if k.split('/')[0] in sense)
    sense_tok += sum(v for k, v in cls_tokens.items() if k == 'single-sign/logogram/abbreviation') * 0  # not counted
    total_tok = sum(cls_tokens.values())
    sound = sum(v for k, v in cls_tokens.items() if k.startswith('word/') or k.startswith('single-sign'))
    total_sign = sum(cls_signs.values())
    sense_sign = sum(v for k, v in cls_signs.items() if k.split('/')[0] in sense)
    admin_rows = [r for r in ROWS if r['support'] in ADMIN]
    summary = {
        'records': len(ROWS), 'administrative_records': len(admin_rows),
        'tokens_by_class': dict(cls_tokens.most_common()), 'signs_by_class': dict(cls_signs.most_common()),
        'tokens_total': total_tok, 'tokens_read_as_sense': sense_tok,
        'share_tokens_read_as_sense': round(sense_tok / total_tok, 3),
        'share_signs_read_as_sense': round(sense_sign / total_sign, 3),
        'tokens_read_as_sound_only': sound, 'share_tokens_read_as_sound_only': round(sound / total_tok, 3),
        'roles': dict(roles.most_common()),
        'totals_checked': len(checks),
        'totals_balancing_in_some_window': sum(c['balances_in_some_window'] for c in checks),
        'totals_clean_and_balancing': sum(1 for c in checks if c['balances_in_some_window'] and not c['stated_damaged']),
        'heading_words_3plus_records': {k: sorted(v) for k, v in sorted(heading_words.items(), key=lambda x: -len(x[1]))
                                        if len(v) >= 3},
        'entry_labels_3plus_records': {k: sorted(v) for k, v in sorted(label_words.items(), key=lambda x: -len(x[1]))
                                       if len(v) >= 3},
    }
    out = ROOT / 'reading'
    (out / 'reading.json').write_text(json.dumps({'method': __doc__.strip(), 'summary': summary, 'totals': checks,
                                                  'records': records}, ensure_ascii=False, indent=1) + '\n',
                                      encoding='utf-8')
    with open(out / 'edition.txt', 'w', encoding='utf-8') as f:
        f.write('# Linear A working corpus, structural reading (build_reading.py). [..] = gloss; [?] = damage;\n'
                '# {H}/{A} = fraction signs with disputed values. Words are sound-values only unless glossed.\n')
        for rec in records:
            f.write(f"\n{rec['name']}  ({rec['site']}; {rec['support']}{'; ' + rec['scribe'] if rec['scribe'] else ''})\n")
            for line in rec['reading']:
                f.write('    ' + line + '\n')
    print(json.dumps({k: v for k, v in summary.items() if not k.endswith('records')}, ensure_ascii=False, indent=1))
    print('heading words (3+ records):', {k: len(v) for k, v in summary['heading_words_3plus_records'].items()})
    print('entry labels (3+ records):', {k: len(v) for k, v in summary['entry_labels_3plus_records'].items()})


if __name__ == '__main__':
    main()
