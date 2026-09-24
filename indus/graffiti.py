"""Tamil Nadu graffiti composites (Rajan and Sivanantham, Inscribed Potsherds of Tamil Nadu: Graffiti and Tamiḻi, vol. II,
Department of Archaeology, Government of Tamil Nadu, 2026; Table 6.1 concordance, freely downloadable from the Tamil
Digital Library). Extracted by table reading into the scratchpad (tngraffiti/concordance.tsv); not redistributed.
load() returns (sherd, composite number, elements in slot order prefix-3 ... suffix-3), deduplicated."""
import csv
import os

from lang_names import SP

SLOTS = ('p3', 'p2', 'p1', 'stem', 's1', 's2', 's3')


def load():
    seen, out = set(), []
    for r in csv.DictReader(open(os.path.join(SP, 'tngraffiti', 'concordance.tsv'), encoding='utf-8'), delimiter='\t'):
        k = (r['cat'], r['signno'])
        if k in seen:
            continue
        seen.add(k)
        seq = tuple(r[s] for s in SLOTS if r[s])
        if seq:
            out.append((r['cat'], r['signno'], seq))
    return out


def order_consistency(seqs, minn=3):
    from collections import Counter
    c = Counter()
    for t in seqs:
        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                if t[i] != t[j]:
                    c[(t[i], t[j])] += 1
    maj = tot = 0
    done = set()
    for (a, b), n in c.items():
        k = frozenset((a, b))
        if k in done:
            continue
        done.add(k)
        m = c[(b, a)]
        if n + m >= minn:
            maj += max(n, m)
            tot += n + m
    return maj / max(1, tot), tot
