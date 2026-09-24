"""Round 67 (saturation loop 9): change over time, with Phaistos (Middle Minoan II) against the Late Minoan IB
archives, and what vessel inscriptions name. BH at 5% across the six.

Phaistos lies a few kilometres from Haghia Triada but its tablets are some two centuries older, so a Phaistos
difference that other non-HT sites do not show points to time rather than place.

Y1 Phaistos word types occur at Haghia Triada less often than word types of the other non-HT sites.
Y2 Phaistos sign tokens (in words) are signs unattested at Haghia Triada more often than other non-HT sites' tokens.
Y3 Phaistos single-commodity lists write the commodity sign on a larger share of entries than LM IB lists.
Y4 Phaistos lists run largest-first (mean Kendall tau above the within-list shuffle).
Y5 Words on clay vessels are name-slot types more often than descriptor-slot types (share of vessel types found in
   each slot set, compared with the slot sets' sizes by a label shuffle).
Y6 Phaistos words are shorter (signs per word type) than words of the other non-HT sites.
"""
from collections import defaultdict
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round59 as N  # noqa: E402
import round60 as PP  # noqa: E402
import round64 as U  # noqa: E402
import round43 as FF  # noqa: E402
import vigorous2 as W2  # noqa: E402

B, X = R.B, R.X


def site_types():
    d = defaultdict(set)
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] in N.WORD and '-' in t['label']:
                d[r['site']].add(t['label'])
    return d


ST = site_types()
HT = ST['Haghia Triada']
OTHER = [s for s in ST if s not in ('Haghia Triada', 'Phaistos')]


def Y1():
    items = [(s == 'Phaistos', w in HT) for s in ['Phaistos'] + OTHER for w in ST[s]]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1], lower=True)
    return p, 'Phaistos words occur at Haghia Triada less often', {'Phaistos': a, 'other_nonHT': b, 'p': round(p, 4)}, {}


def Y2():
    ht_signs = {s for w in HT for s in w.split('-')}
    items = [(s == 'Phaistos', sg not in ht_signs) for s in ['Phaistos'] + OTHER for w in ST[s] for sg in w.split('-')]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Phaistos uses signs unattested at Haghia Triada more often', {'Phaistos': a, 'other_nonHT': b, 'p': round(p, 4)}, {}


def Y3():
    r_, p, a, b = R.flag_compare(U.L, lambda x: x['site'] == 'Phaistos', lambda x: x['share'])
    return p, 'Phaistos lists repeat the commodity sign more', {'Phaistos': a, 'LM_IB': b, 'p': round(p, 4)}, {}


def Y4():
    lists = []
    for r in B.READ['records']:
        if r['site'] != 'Phaistos' or r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(int)
        for t in r['tokens']:
            if t['cls'] == 'number':
                ents[t['entry']] += t['value']
        q = [v for _, v in sorted(ents.items()) if v > 0]
        if len(q) >= 3:
            lists.append(q)
    real, p, nm = FF.shuffle_within(lists, lambda ls: sum(W2.tau(q) for q in ls) / max(1, len(ls)))
    return p, 'Phaistos lists run largest-first', {'mean_tau': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(lists)}, {}


def Y5():
    vessel = {t['label'] for r in B.READ['records'] if r['support'] == 'Clay vessel' for t in r['tokens'] if t['cls'] in N.WORD and '-' in t['label']}
    labels = [x['label'] for x in N.TOK]
    slots = [x['slot'] for x in N.TOK]

    def stat(sl):
        ns = {l for l, s in zip(labels, sl) if s == 'name'}
        ds = {l for l, s in zip(labels, sl) if s == 'desc'}
        return len(vessel & ns) / max(1, len(ns)) - len(vessel & ds) / max(1, len(ds))
    real = stat(slots)
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(slots)
        null.append(stat(slots))
    p = R.pv_hi(null, real)
    return p, 'Vessel words are name-slot words more often', {'diff': round(real, 4), 'null': round(sum(null) / len(null), 4), 'p': round(p, 4), 'vessel_types': len(vessel), 'in_name': len(vessel & PP.NSET), 'in_desc': len(vessel & PP.DSET)}, {}


def Y6():
    items = [(s == 'Phaistos', len(w.split('-'))) for s in ['Phaistos'] + OTHER for w in ST[s]]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1], lower=True)
    return p, 'Phaistos words are shorter', {'Phaistos': a, 'other_nonHT': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round67', 'change over time, and what vessels name', __doc__, [Y1, Y2, Y3, Y4, Y5, Y6])
