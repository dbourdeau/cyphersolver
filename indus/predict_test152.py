"""Hundred-and-fifty-second registered prediction set (PREDICTIONS.md, LC1-LC6): the capture-recapture method of set
147 on Linear B (DAMOS corpus, Tiripode lexicon; path from the LINB environment variable). Writes
results/predict_test152.md."""
import csv
import json
import os
from collections import defaultdict

import rtools as R
from predict_test147 import chapman

LINB = os.environ.get('LINB', 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher--claude-worktrees-florence-1414-'
                      'cipher-160632/03a95ee0-e290-45c7-bab7-1e38cbd68d34/scratchpad/linb')
INDUS = {'ratio': 2968 / 585, 'shared': 20 / 130, 'one': 536 / 585}


def classes():
    per, tit = set(), set()
    with open(os.path.join(LINB, 'lexicon_tiripode.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            d = (r.get('definition') or '').lower()
            w = r['linear_b'].strip()
            if 'anthroponym' in d and not any(x in d for x in ('occupation', 'title', 'anthroponym or', 'or anthroponym', 'anthroponym?')):
                per.add(w)
            elif ('occupation' in d or 'title' in d) and 'anthroponym' not in d:
                tit.add(w)
    return per, tit


def main():
    rd = R.Round('Hundred-and-fifty-second registered predictions: the capture-recapture method on Linear B', 'predict_test152')
    site = {}
    for ln in open(os.path.join(LINB, 'corpus_damos_documents.jsonl'), encoding='utf-8'):
        d = json.loads(ln)
        site[d['id']] = d['site']
    per, tit = classes()
    docs = defaultdict(set)
    where = defaultdict(set)
    with open(os.path.join(LINB, 'corpus_damos_words.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            s = site.get(r['doc_id'])
            if s in ('Knossos', 'Pylos') and r['status'] == 'complete' and r['uncertain'] == '0' and r['erased'] == '0' and r['badsign'] == '0':
                docs[r['word']].add(r['doc_id'])
                where[r['word']].add(s)
    stats = {}
    for lab, cls in (('persons', per), ('titles', tit)):
        ws = [w for w in cls if w in where]
        kn = {w for w in ws if 'Knossos' in where[w]}
        py = {w for w in ws if 'Pylos' in where[w]}
        obs = len(kn | py)
        lp = chapman(len(kn), len(py), len(kn & py))
        one = sum(len(docs[w]) == 1 for w in ws)
        stats[lab] = {'ratio': lp / max(1, obs), 'shared': len(kn & py) / max(1, min(len(kn), len(py))), 'one': one / max(1, obs),
                      'kn': len(kn), 'py': len(py), 'm': len(kn & py), 'obs': obs, 'lp': lp, 'n1': one}
        rd.say('- %s: lexicon %d, attested %d (Knossos %d, Pylos %d, both %d); estimate %.0f (%.2fx); shared %.3f; one document %d (%.2f).' % (
            lab, len(cls), obs, len(kn), len(py), len(kn & py), lp, stats[lab]['ratio'], stats[lab]['shared'], one, stats[lab]['one']))
    rd.say()
    P, Tt = stats['persons'], stats['titles']
    rd.rec('LC1', 'persons: a large population', 'estimate %.0f against %d observed (%.2fx); threshold 3x' % (P['lp'], P['obs'], P['ratio']), P['ratio'] >= 3)
    rd.rec('LC2', 'titles: a small population', 'estimate %.0f against %d observed (%.2fx); threshold at most 1.5x' % (Tt['lp'], Tt['obs'], Tt['ratio']), Tt['ratio'] <= 1.5)
    sm = lambda s: min(s['kn'], s['py'])
    rd.ltl('LC3', 'persons are shared less', 'shared, persons', [True] * P['m'] + [False] * (sm(P) - P['m']), [True] * Tt['m'] + [False] * (sm(Tt) - Tt['m']))
    rd.thr('LC4', 'persons on one document', 'persons on exactly one document', P['n1'], P['obs'], 0.6)
    rd.ltl('LC5', 'titles on one document less often', 'one document, titles', [True] * Tt['n1'] + [False] * (Tt['obs'] - Tt['n1']),
           [True] * P['n1'] + [False] * (P['obs'] - P['n1']))
    close = {k: abs(INDUS[k] - P[k]) < abs(INDUS[k] - Tt[k]) for k in INDUS}
    rd.rec('LC6', 'the Indus names look like persons', 'Indus %s; persons %s; titles %s; closer to persons: %s' % (
        ', '.join('%s %.2f' % (k, v) for k, v in INDUS.items()), ', '.join('%s %.2f' % (k, P[k]) for k in INDUS),
        ', '.join('%s %.2f' % (k, Tt[k]) for k in INDUS), close), all(close.values()))
    rd.finish()


if __name__ == '__main__':
    main()
