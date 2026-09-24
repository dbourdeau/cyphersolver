"""The L bench (set 195): how many of the world's language groups are compatible with the Indus typological profile,
in WALS (data/wals_profile.tsv) and Grambank (data/grambank_profile.tsv), both CLDF releases under CC-BY 4.0.
Profile = structure established without sound values (PREDICTIONS.md set 195)."""
import csv
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
WALS_CORE = {'26A': {'2', '3'}, '86A': {'1'}, '87A': {'1'}, '89A': {'1'}, '51A': {'1', '6'}}
WALS_CLASS = dict(WALS_CORE, **{'30A': {'2', '3', '4', '5'}})
GB_CORE = {'GB024': {'1', '3'}, 'GB065': {'1', '3'}, 'GB193': {'1', '3'}}
GB_CLASSF = ('GB051', 'GB052', 'GB053', 'GB054', 'GB192')


def rows(name):
    with open(os.path.join(HERE, 'data', name), encoding='utf-8') as f:
        return list(csv.DictReader((x for x in f if not x.startswith('#')), delimiter='\t'))


def wals_ok(r, prof, minc=3):
    coded = [k for k in prof if r[k]]
    if len(coded) < minc:
        return None
    return all(r[k] in prof[k] for k in coded)


def gb_ok(r, cls=False, minc=2):
    coded = [k for k in GB_CORE if r[k] in ('0', '1', '2', '3')]
    if len(coded) < minc:
        return None
    ok = all(r[k] in GB_CORE[k] for k in coded)
    if cls:
        cv = [r[k] for k in GB_CLASSF if r[k] in ('0', '1')]
        if not cv:
            return None
        ok = ok and '1' in cv
    return ok


def groups(rs, key, fn):
    g = defaultdict(list)
    for r in rs:
        o = fn(r)
        if o is not None:
            g[r[key]].append(o)
    return g


def share_excluded(g):
    return 1 - sum(any(v) for v in g.values()) / max(1, len(g))


def world():
    """(WALS core share of genera excluded, Grambank core share of families excluded)."""
    w = groups(rows('wals_profile.tsv'), 'genus', lambda r: wals_ok(r, WALS_CORE))
    g = groups(rows('grambank_profile.tsv'), 'family', gb_ok)
    return share_excluded(w), share_excluded(g)


def tolerant_wals(r, minc=3):
    prof = {'26A': {'2', '3'}, '86A': {'1', '3'}, '87A': {'1', '3'}, '89A': {'1', '3'}}
    return wals_ok(r, prof, minc)


def majority(g):
    """Groups whose assessed languages are mostly compatible (set 196)."""
    return {k for k, v in g.items() if sum(v) > len(v) / 2}


def world_tolerant():
    """(WALS genera excluded, Grambank families excluded), tolerant profile and majority rule (set 196)."""
    w = groups(rows('wals_profile.tsv'), 'genus', tolerant_wals)
    g = groups(rows('grambank_profile.tsv'), 'family', gb_ok)
    return 1 - len(majority(w)) / len(w), 1 - len(majority(g)) / len(g)
