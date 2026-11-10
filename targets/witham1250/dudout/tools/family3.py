# Controls for family2: same LCS-vs-shuffle test for other strings against fyris74 and marburg; Witham reversed.
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import TARGETS, SIBLINGS, CONTROLS
from family2 import lcs
random.seed(7)
N = 3000
tests = dict(CONTROLS); tests["witham_new_reversed"] = TARGETS["witham_new"][::-1]
tests["alphen_A"] = TARGETS["alphen_A"]; tests["alphen_B"] = TARGETS["alphen_B"]
tests["benedict_medal"] = "CSSMLNDSMDVRSNSMVSMQLIVB"; tests["laudes_initials"] = "XVXRXIXAOMND"
for name, s in tests.items():
    row = []
    for k in ["fyris74", "marburg"]:
        v = SIBLINGS[k][0]; obs = lcs(s, v); l = list(s); ge = 0
        for _ in range(N):
            random.shuffle(l); ge += lcs("".join(l), v) >= obs
        row.append("%s LCS %2d/%2d p=%.4f" % (k, obs, len(s), (ge+1)/(N+1)))
    print("%-20s %s" % (name, " | ".join(row)))
