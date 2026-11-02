"""One-part-code test on the Japanese copies (python stats_initials.py).

If the Japanese reconstructed an alphabetical (one-part) code, an unknown group lies between two known groups, so its wrong
reading or its truncation should share the initial of the true word more often than chance. initials_pairs.tsv holds the
137 substitutions and 119 truncations aligned on the FRUS text (selection rules written before the calculation).
Control: the FRUS words are shuffled among the pairs, 10,000 draws, seed 1932; p = share of draws >= observed (+1).
"""
import csv, os, random
rows = [r for r in csv.reader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'initials_pairs.tsv'),
        encoding='utf-8'), delimiter='\t') if r and not r[0].startswith('#')][1:]
random.seed(1932)
for cat in ('substitution', 'truncation'):
    pairs = [(r[2].lower(), r[3].lower()) for r in rows if r[0] == cat and r[2] and r[3]]
    obs = sum(a[:1] == b[:1] for a, b in pairs)
    jp, fr = [a for a, _ in pairs], [b for _, b in pairs]
    draws = []
    for _ in range(10000):
        random.shuffle(fr)
        draws.append(sum(a[:1] == b[:1] for a, b in zip(jp, fr)))
    p = (sum(d >= obs for d in draws) + 1) / (len(draws) + 1)
    print(f'{cat}: same initial {obs}/{len(pairs)} ({obs / len(pairs):.0%}); shuffled mean {sum(draws) / len(draws) / len(pairs):.1%}; p = {p:.5f}')
