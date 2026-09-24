"""Post-test check on Z3 (twentieth set; not registered): leave fish-category (Q) and signs.FISH heads out of both
sides. Writes results/robust20.md."""
import os
from collections import Counter
import predict_test13 as T
from predict_test14 import cat_of, hyper_ge
from signs import FISH
cat = cat_of()
a = na = c = nc = 0
kinds = {'740': Counter(), '520': Counter()}
for b, e in T.names(T.sample('A') + T.sample('B')):
    k = cat.get(b[-1])
    if not k or k == 'Q' or b[-1] in FISH:
        continue
    kinds[e][k] += 1
    if e == '740':
        a += k in 'AHIK'; na += 1
    else:
        c += k in 'AHIK'; nc += 1
p = hyper_ge(a, na - a, c, nc - c)
out = ['# Check on Z3 (after the test, not registered)', '',
       '- without fish heads: 740 heads human / weapon / implement / measure %d of %d (%.1f%%); 520 heads %d of %d (%.1f%%); p = %.4f.' % (
           a, na, 100 * a / na, c, nc, 100 * c / max(1, nc), p),
       '- categories of the remaining heads: 740 %s; 520 %s.' % (dict(kinds['740'].most_common()), dict(kinds['520'].most_common()))]
print('\n'.join(out))
open(os.path.join(T.HERE, 'results', 'robust20.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
