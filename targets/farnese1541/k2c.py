"""Working key for R91, step c: k2b with ci/co swapped (23 = co, 24 = ci; Meister prints ci 23, co 24).

Evidence: of the 24 orders of ca/ce/ci/co on 21-24 the 5-gram ranks this one first (-2553.4 vs -2567.4 for the
print), and the readings medi-24-na (medicina) and iudi-24-o (iudicio) need 24 = ci; every other syllable family
(d, l, m, n, r, s) keeps Meister's order, by 18-112 nats over the next permutation.
"""
from k2b import KEY as _K
KEY = {k: list(v) for k, v in _K.items()}
KEY['23'] = ['co']
KEY['24'] = ['ci']
