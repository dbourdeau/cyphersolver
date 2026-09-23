"""Signs and field motifs: the pictorial-bilingual idea (Parpola 2005, Fig. 4) tested on
the whole corpus.

Seals carry an animal or scene (the 'field motif') and a text. If some signs name or
qualify the motif, they should occur with it more often than chance. For every sign
(>= 8 seal occurrences) and every motif class (>= 15 seals), count the seals that carry
both, and compare with a permutation null that reshuffles motifs among seals (texts
fixed, 2,000 permutations). Report pairs whose count is reached in <= 0.1% of
permutations, i.e. surviving a rough Bonferroni over the pairs tested.

Motif codes (ICONOGRAPHY table): Bull1 and its sub-types = 'unicorn', Bull3 = 'bull',
Bult/Zebu = zebu, Gaur, Buff, Elep, Rhin, Tigr, Gavi, Goat, Hare, Fish, Anth ...

Writes results/motif_checks.md.
"""
import os
import random
from collections import Counter, defaultdict

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
random.seed(7)


def motif_class(m):
    if not m:
        return None
    if m.startswith('Bull1'):
        return 'unicorn'
    if m in ('Bult', 'Zebu'):
        return 'zebu'
    if m.startswith('Goat'):
        return 'goat'
    return m


def main():
    rows = [r for r in load() if r['flat'] and r['type'].startswith('SEAL')]
    seals = [(motif_class(r['motif']), set(r['flat']), r) for r in rows if motif_class(r['motif'])]
    mot = Counter(m for m, _, _ in seals)
    keep = {m for m, c in mot.items() if c >= 15}
    seals = [s for s in seals if s[0] in keep]
    sign_n = Counter(g for _, ss, _ in seals for g in ss)
    signs = {g for g, c in sign_n.items() if c >= 8}
    obs = Counter((m, g) for m, ss, _ in seals for g in ss if g in signs)
    motifs = [m for m, _, _ in seals]
    sets = [ss for _, ss, _ in seals]
    P = 2000
    ge = Counter()
    for _ in range(P):
        random.shuffle(motifs)
        c = Counter((m, g) for m, ss in zip(motifs, sets) for g in ss if g in signs)
        for k, v in obs.items():
            if c[k] >= v:
                ge[k] += 1
    out = ['# Signs and field motifs', '',
           'Seals with a known motif: %d; motif classes kept (>= 15 seals): %s.' % (
               len(seals), ', '.join('%s %d' % (m, mot[m]) for m in sorted(keep, key=lambda x: -mot[x]))),
           'Signs tested (>= 8 of these seals): %d; sign-motif pairs with any co-occurrence: %d; '
           'permutations: %d.' % (len(signs), len(obs), P), '',
           '| motif | sign | seals with both | expected | seals with the sign | share of the sign\'s seals | permutations >= |',
           '|---|---|---|---|---|---|---|']
    hits = []
    for (m, g), v in obs.items():
        exp = sign_n[g] * mot[m] / len(seals)
        if ge[(m, g)] <= P * 0.001 and v > exp:
            hits.append((m, g, v, exp))
    for m, g, v, exp in sorted(hits, key=lambda x: (x[0], -x[2] / x[3])):
        out.append('| %s | %s | %d | %.1f | %d | %.0f%% | %d |' % (
            m, g, v, exp, sign_n[g], 100 * v / sign_n[g], ge[(m, g)]))
    out += ['', 'Pairs listed: %d. With %d pairs tested at p <= 0.001, about %.1f would pass by '
            'chance.' % (len(hits), len(obs), len(obs) * 0.001)]
    # the strongest: signs that are nearly exclusive to one non-unicorn motif
    out += ['', 'Signs of which at least half the occurrences are on one non-unicorn motif:']
    for g in sorted(signs, key=lambda x: -sign_n[x]):
        best = max(((m, obs[(m, g)]) for m in keep), key=lambda x: x[1])
        if best[0] != 'unicorn' and best[1] >= 0.5 * sign_n[g]:
            out.append('- %s: %d of %d on %s (motif is %.0f%% of seals)' % (
                g, best[1], sign_n[g], best[0], 100 * mot[best[0]] / len(seals)))
    out += copper_tablets()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'motif_checks.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    print('\n'.join(out))


def copper_tablets():
    """Copper tablets: does the text fix the image (and the image the text)?"""
    tabs = [r for r in load() if r['flat'] and r['type'] == 'TAB:C'
            and r['motif'] not in ('', 'Othr', 'Unknown')]
    by_motif = defaultdict(Counter)
    by_text = defaultdict(Counter)
    for r in tabs:
        m = motif_class(r['motif'])
        t = ' '.join(r['flat'])
        by_motif[m][t] += 1
        by_text[t][m] += 1
    out = ['', '## Copper tablets (Mohenjo-daro): text and image', '',
           'Tablets with a named motif: %d. For each motif, the texts on its tablets; the tablets '
           'come in duplicate sets, so a motif with one text means the text and the image go '
           'together.' % len(tabs), '',
           '| motif | tablets | texts (reading order) x count | share with the commonest text |',
           '|---|---|---|---|']
    for m, c in sorted(by_motif.items(), key=lambda x: -sum(x[1].values())):
        n = sum(c.values())
        out.append('| %s | %d | %s | %.0f%% |' % (m, n, '; '.join('%s x%d' % kv for kv in c.most_common(4)),
                                                  100 * c.most_common(1)[0][1] / n))
    multi = [(t, c) for t, c in by_text.items() if sum(c.values()) >= 3]
    pure = sum(1 for t, c in multi if len(c) == 1)
    out += ['', '- texts on 3 or more tablets with a named motif: %d; with a single motif: %d.'
            % (len(multi), pure)]
    return out


if __name__ == '__main__':
    main()
