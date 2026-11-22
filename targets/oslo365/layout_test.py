"""Test whether the recto recitations could supply a continuous verso exemplar.

Line 3 requires omega and tau, printed without underdots. Allow one proposed
letter to disagree per line. Selection uses lines 2-4 only. Report every
eligible chain; line 5 is then a separate test. Counts are not probabilities.
"""
from check_recto import PASSAGES

masks = ("γ.......φι","εωτ.....χ","λ....τα","τω....ξ")


def ends(text, mask, secure=()):
    hits = set()
    for i in range(len(mask),len(text)+1):
        word = text[i-len(mask):i]
        errors = [k for k,c in enumerate(mask) if c!="." and c!=word[k]]
        if len(errors)<=1 and not set(errors).intersection(secure):
            hits.add(i)
    return hits


for label, reverse, minwidth, maxwidth, drift, equal in [
    ("repeated column width",False,8,45,0,True),
    ("independently ragged lines",False,8,45,0,False),
    ("short name list",False,3,12,0,False),
    ("line four stops before physical margin",False,8,45,5,True),
    ("reversed continuous exemplar",True,8,45,5,False),
]:
    chains = []
    predicted = []
    for idx, source in enumerate(PASSAGES):
        text = source[::-1] if reverse else source
        h2,h3,h4,h5 = [ends(text,p,(1,2) if j==1 else ()) for j,p in enumerate(masks)]
        for a in h2:
            for b in h3:
                width = b-a
                if not minwidth<=width<=maxwidth:
                    continue
                for c in h4:
                    for margin in range(drift+1):
                        gap=c+margin-b
                        if not minwidth<=gap<=maxwidth or (equal and gap!=width):
                            continue
                        chains.append((idx,a,b,c,margin))
                        for d in h5:
                            gap5=d-c-margin
                            if minwidth<=gap5<=maxwidth and (not equal or gap5==width):
                                predicted.append((idx,a,b,c,d,text[d-7:d]))
    print(label,"2-4 chains",len(chains),"with line 5", sorted(set(predicted)))
