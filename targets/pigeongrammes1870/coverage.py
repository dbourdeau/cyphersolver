"""Coverage of the inspectors' telegram (inspecteurs_2nov_partial.txt) by the values in anchors_inspecteurs.json.

Strict count (figure of record, README read bar): an occurrence counts as valued only when its group, as written,
has a value. Holes: the assumed digit slips in "_slips" (not checked on the scan), and the occurrences NOTES.md
itself calls a guess, unsupported or unread (listed in STRICT_OUT below). Marker groups ("_markers") are counted apart.
The looser count of the third pass also gives a slip its target's value. Run: python3 -I coverage.py"""
import re, json, os, collections
H = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(H, "anchors_inspecteurs.json"), encoding="utf8"))
T = open(os.path.join(H, "inspecteurs_2nov_partial.txt"), encoding="utf8").read()
S, M = A["_slips"], A["_markers"]
V = {k: v for k, v in A.items() if not k.startswith("_")}
# group -> (number of occurrences out, reason as NOTES.md gives it)
STRICT_OUT = {
    "5219": (1, "mademoiselle: 'Guess only' (Pillon test section)"),
    "9802": (2, "vin: only as VIN-OY, 'NOT supported', 'stays a guess'; Remaining gaps lists 9802 6124 as an unread name"),
    "3927": (1, "garde: 'in L-[3927]-E it is unread' (claims-review correction)"),
}
G = re.findall(r"\b\d{4}\b", T)
c = collections.Counter()
for g in G:
    if g in V: c["value"] += 1
    elif g in S and S[g] in V: c["slip"] += 1
    elif g in M: c["marker"] += 1
    else: c["unread"] += 1
out = sum(n for n, _ in STRICT_OUT.values())
n = len(G)
loose = c["value"] + c["slip"]
strict = c["value"] - out
print("groups %d, distinct %d; values %d, markers %d, assumed slips %d (%d occurrences with a valued target)"
      % (n, len(set(G)), len(V), len(M), len(S), c["slip"]))
print("with the assumed slips: %d of %d valued (%.3f); markers %d; unread %d" % (loose, n, loose / n, c["marker"], c["unread"]))
print("strict: %d of %d valued (%.3f); markers %d (%.3f); holes %d (%.3f) = unread %d + assumed slips %d + noted guesses/unread %d"
      % (strict, n, strict / n, c["marker"], c["marker"] / n, n - strict - c["marker"], (n - strict - c["marker"]) / n,
         c["unread"], c["slip"], out))
for g, (k, why) in STRICT_OUT.items(): print("  out %s x%d: %s" % (g, k, why))
