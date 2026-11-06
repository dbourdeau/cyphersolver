"""Working key for R91, step d: k2c plus 26 = co (a code not in Meister's table) and et on 1 (Meister prints et 1).

26 = co, found by the 64r-64v reader from ~15 readings (contrario x2, conoscere, consideri, considera, particolari,
concorrer, con, comune, loco, cosa, publico, conduca; 2 6 0 6 = co+me "come", 2 6 0 6 2 6 = l+tur+co "l Turco"):
+262 nats over k2c, word coverage 0.549 -> 0.594. With 26 = co, 24 = ci (cioe = 24 9 5, medicina, iudicio) and
23 is undetermined (19 occurrences; ci, ca, co or off all within 4 nats): kept at Meister's ci, unconfirmed.
1 = et: +113 nats; readings "il grado et honor suo", "lo imperator et il re", "l'uno per amico et l'altro".
"""
from k2c import KEY as _K
KEY = {k: list(v) for k, v in _K.items()}
KEY['23'] = ['ci']
KEY['24'] = ['ci']
KEY['26'] = ['co']
KEY['1'] = KEY['1'] + ['et']
