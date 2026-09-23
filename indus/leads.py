"""Fifth pass, corpus leads.

L2  Names against titles across sites (seals only). If a text is [opening] [name] [ending],
    names should be local and openings / endings shared. For each recurring two-sign unit on
    seals (8+ seals), the share of its seals at the commoner of Mohenjo-daro and Harappa, against
    the expectation from those two sites' seal counts; units grouped by their role (opening pair,
    ending pair, name pair with a fish/leaf/crab sign, other).
L6  The short stroke pair (ICIT 2): position, neighbours, what alternates with it in the
    same frame, and how many seals open with [opener][pair or alternant][name sign].

Writes results/leads.md.
"""
import os
from collections import Counter, defaultdict

from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
OPENERS = {'817', '820', '861'}
ENDING = {'740', '520', '400', '90', '151', '154', '156', '741'}
NAMEMARK = FISH | {'803', '806', '798', '794'}


def say(s=''):
    OUT.append(s)
    print(s)


def role(u):
    a, b = u.split()
    if a in OPENERS:
        return 'opening'
    if b in ENDING and a in ENDING | {'176', '100', '760', '752'}:
        return 'ending'
    if a in NAMEMARK or b in NAMEMARK:
        return 'name'
    return 'other'


def l2(rows):
    say('## L2 Names against titles across sites (seals only)')
    say()
    seals = [r for r in rows if r['type'].startswith('SEAL') and r['site'] in ('Mohenjo-daro', 'Harappa')]
    base = Counter(r['site'] for r in seals)
    pm = base['Mohenjo-daro'] / sum(base.values())
    say('Seals: Mohenjo-daro %d, Harappa %d (Mohenjo-daro share %.0f%%).' % (
        base['Mohenjo-daro'], base['Harappa'], 100 * pm))
    say()
    units = defaultdict(Counter)
    for r in seals:
        seen = set()
        for ln in r['seq']:
            for a, b in zip(ln, ln[1:]):
                seen.add(a + ' ' + b)
        for u in seen:
            units[u][r['site']] += 1
    by = defaultdict(list)
    for u, c in units.items():
        n = sum(c.values())
        if n < 8:
            continue
        # |z| of the Mohenjo-daro count against the base share: comparable across unit sizes
        skew = abs(c['Mohenjo-daro'] - pm * n) / (n * pm * (1 - pm)) ** 0.5
        by[role(u)].append((skew, u, c['Mohenjo-daro'], c['Harappa']))
    say('| role | units (8+ seals) | mean abs z against the base site share | units at one site only | examples |')
    say('|---|---|---|---|---|')
    for k in ('opening', 'name', 'ending', 'other'):
        v = by[k]
        if not v:
            continue
        one = sum(1 for _, _, m, h in v if m == 0 or h == 0)
        ex = ', '.join('%s (%d/%d)' % (u, m, h) for _, u, m, h in sorted(v, reverse=True)[:4])
        say('| %s | %d | %.2f | %d | %s |' % (k, len(v), sum(s for s, *_ in v) / len(v), one, ex))
    import random
    random.seed(2)
    name = [x[0] for x in by['name']]
    shared = [x[0] for x in by['opening'] + by['ending']]
    obs = sum(name) / len(name) - sum(shared) / len(shared)
    pool = name + shared
    ge = 0
    for _ in range(10000):
        random.shuffle(pool)
        a, b = pool[:len(name)], pool[len(name):]
        ge += (sum(a) / len(a) - sum(b) / len(b)) >= obs
    say()
    say('- name units minus opening/ending units, mean abs z: %.2f; label permutations as large: %.3f.'
        % (obs, ge / 10000))
    say()


def l6(rows):
    say('## L6 The short stroke pair (ICIT 2)')
    say()
    L = [ln for r in rows for ln in r['seq']]
    nx, pv, pos = Counter(), Counter(), Counter()
    for ln in L:
        for i, g in enumerate(ln):
            if g == '2':
                nx[ln[i + 1] if i + 1 < len(ln) else '>'] += 1
                pv[ln[i - 1] if i else '<'] += 1
                pos['initial' if i == 0 else 'final' if i == len(ln) - 1 else 'medial'] += 1
    tot = sum(pos.values())
    say('- %d tokens: %s; before it %s; after it %s.' % (
        tot, dict(pos), ', '.join('%s x%d' % kv for kv in pv.most_common(6)),
        ', '.join('%s x%d' % kv for kv in nx.most_common(8))))
    op = sum(pv[g] for g in OPENERS)
    nm = sum(c for g, c in nx.items() if g in NAMEMARK)
    say('- after an opener (817, 820, 861): %d (%.0f%%); before a fish, leaf or crab sign: %d (%.0f%%).'
        % (op, 100 * op / tot, nm, 100 * nm / tot))
    slot = defaultdict(Counter)
    for ln in L:
        for i in range(1, len(ln) - 1):
            slot[(ln[i - 1], ln[i + 1])][ln[i]] += 1
    alt = Counter()
    for c in slot.values():
        if '2' in c:
            for g, n in c.items():
                if g != '2':
                    alt[g] += n
    say('- signs found in the same frame (same neighbours) instead of it: %s.' % ', '.join(
        '%s x%d' % kv for kv in alt.most_common(8)))
    seals = [r for r in rows if r['type'].startswith('SEAL')]
    k = 0
    for r in seals:
        s = r['flat']
        if len(s) >= 3 and s[0] in OPENERS and s[1] in ('2', '60', '1') and s[2] in NAMEMARK:
            k += 1
    say('- seals that open [817/820/861] + [2, 60 or 1] + [fish, leaf or crab sign]: %d of %d.' % (k, len(seals)))
    say()


def l5(rows):
    say('## L5 Time depth through object type (Kenoyer and Meadow 2010, CISI 3.1: xliv-lviii)')
    say()
    say('At Harappa, square seals with an animal run from late Period 3A (c. 2450 BC) through 3C; long '
        'rectangular (bar) seals with script only are confined to Period 3C (c. 2200-1900 BC); incised and '
        'moulded tablets run from mid-3B into 3C. Bar seals are therefore a late group; square seals span the '
        'whole Harappan phase.')
    say()
    groups = {'square seals (3A-3C)': [r for r in rows if r['type'] == 'SEAL:S'],
              'bar seals (3C only)': [r for r in rows if r['type'] == 'SEAL:R']}
    say('| measure | %s |' % ' | '.join(groups))
    say('|---|' + '---|' * len(groups))
    def share(rs, test):
        n = len(rs)
        return '%.0f%%' % (100 * sum(1 for r in rs if test(r)) / n)
    rowsdef = [
        ('objects', lambda rs: str(len(rs))),
        ('mean signs per object', lambda rs: '%.2f' % (sum(len(r['flat']) for r in rs) / len(rs))),
        ('ending 740 anywhere', lambda rs: share(rs, lambda r: '740' in r['flat'])),
        ('second ending 740 + 400/90/151', lambda rs: share(rs, lambda r: any(
            a == '740' and b in ('400', '90', '151') for a, b in zip(r['flat'], r['flat'][1:])))),
        ('opening 817/820/861 + 2', lambda rs: share(rs, lambda r: any(
            a in OPENERS and b == '2' for a, b in zip(r['flat'], r['flat'][1:])))),
        ('a fish-series sign', lambda rs: share(rs, lambda r: any(g in FISH for g in r['flat']))),
        ('a leaf or crab sign', lambda rs: share(rs, lambda r: any(g in ('803', '806', '798', '794') for g in r['flat']))),
        ('a numeral', lambda rs: share(rs, lambda r: any(g in ('1', '3', '4', '5', '31', '33', '34', '16', '17', '55')
                                                          for g in r['flat']))),
    ]
    for lab, f in rowsdef:
        say('| %s | %s |' % (lab, ' | '.join(f(rs) for rs in groups.values())))
    sq = Counter(g for r in groups['square seals (3A-3C)'] for g in set(r['flat']))
    br = Counter(g for r in groups['bar seals (3C only)'] for g in set(r['flat']))
    ns, nb = len(groups['square seals (3A-3C)']), len(groups['bar seals (3C only)'])
    diff = sorted(((br[g] / nb - sq[g] / ns), g) for g in set(sq) | set(br) if sq[g] + br[g] >= 15)
    say()
    say('- signs much commoner on the late bar seals: %s; commoner on square seals: %s (share of objects).' % (
        ', '.join('%s (%.0f%% vs %.0f%%)' % (g, 100 * br[g] / nb, 100 * sq[g] / ns) for d, g in diff[::-1][:6]),
        ', '.join('%s (%.0f%% vs %.0f%%)' % (g, 100 * br[g] / nb, 100 * sq[g] / ns) for d, g in diff[:6])))
    say()


def l7(rows):
    say('## L7 The seals found in the Gulf, Mesopotamia and Iran: Indus grammar or not?')
    say()
    from signs import WEST_ASIA
    west = [r for r in rows if r['type'].startswith('SEAL') and (r['site'] in WEST_ASIA or (
        r['site'] in ('Unknown', '') and r['type'] in ('SEAL:C', 'SEAL:CY')))]
    home = [r for r in rows if r['type'].startswith('SEAL') and r['site'] not in WEST_ASIA | {'Unknown', ''}]
    def stats(rs):
        n = len(rs)
        fin = sum(1 for r in rs if r['flat'][-1] in ('740', '520', '400', '90'))
        op = sum(1 for r in rs if r['flat'][0] in OPENERS)
        nm = sum(1 for r in rs if any(g in NAMEMARK for g in r['flat']))
        num = sum(1 for r in rs if any(g in ('1', '2', '3', '4', '5', '31', '32', '33', '55') for g in r['flat']))
        return n, fin, op, nm, num
    say('| group | seals | ending 740/520/400/90 last | opener first | a name sign | a numeral |')
    say('|---|---|---|---|---|---|')
    for lab, rs in (('South Asia', home), ('West Asia (and unprovenanced round/cylinder)', west)):
        n, fin, op, nm, num = stats(rs)
        say('| %s | %d | %d (%.0f%%) | %d (%.0f%%) | %d (%.0f%%) | %d (%.0f%%) |' % (
            lab, n, fin, 100 * fin / n, op, 100 * op / n, nm, 100 * nm / n, num, 100 * num / n))
    say()
    say('- the West Asian seals: ' + '; '.join('%s %s: %s' % (r['site'], r['type'], ' '.join(r['flat'])) for r in west))
    say()


def main():
    rows = [r for r in load() if r['flat']]
    say('# Fifth pass: corpus leads')
    say()
    l2(rows)
    l6(rows)
    l5(rows)
    l7(rows)
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'leads.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
