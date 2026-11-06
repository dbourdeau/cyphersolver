"""Working key for R91, step b: key 2 with b/c on 02 (Meister's "or" read as a misprint of 02), 11 = null, s/z on 1."""
from key2 import K2
SING = {'3': 'a', '5': 'e', '7': 'i', '9': 'o', '0': 'u', '8': 'c', '02': ['b', 'c', 'bb'], '01': 'dfg', '2': 'lp',
        '4': 'nm', '6': 'rt', '1': 'sz', '11': ['']}
KEY = {k: list(v) for k, v in K2.items() if len(k) == 2 and k not in ('01', '11')}
for c, outs in SING.items():
    KEY.setdefault(c, []).extend(list(outs))
