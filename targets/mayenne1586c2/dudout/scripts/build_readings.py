"""Before/after reading of f. 120 in one notation, for counting with Daniel's 95 % rule.
plain = sure ; {x} = probable ; [x] = restored ; [?x] = unresolved (x = the decode letters, or ___ = a code sign
with no value, 3 letter-units) ; [?] = 1 unit, [?…] = 3 units. Outside the re-read stretches both texts are the b21
reading word for word. BEFORE = b21 with its holes in the re-read stretches filled with the decode letters."""
import sys
b21 = open(sys.argv[1], encoding='utf-8').read().strip()
# (b21 segment, BEFORE = b21 holes filled, AFTER = re-read)
SEG = [
 ("Et au reste, que [?E] est tout resolu, que quelque [?…]ment et conjuration que vous s[?] puis [?…] faire de [?s'en] aler, et partir si [?] qu'il saura",
  "Et au reste, que [?___] est tout resolu, que quelque [?ende]ment et conjuration que vous [?s] puis [?sies] faire de [?s'en] aler, et partir si [?___] qu'il saura",
  "Et au reste, que [?___] est tout resolu, quelque [comme]ndement et coniuration que vous [luy] puissies faire de s'en aler, et partir si [tost] qu'il saura"),
 ("je suis encore incertain si je irai[s], [?s'ay en dray], ce que l'on m'en dira.",
  "je suis encore incertain si je irai[s], [?s'ay en dray], ce que l'on m'en dira.",
  "je suis encore incertain si je irai, [?s'ay en dray] ce que l'on m'en dira."),
 ("qui [?suivent] [?…] et font [?] ofres ; mais nous somes [en] un corps si debile qui ne peut a faire profit de n[?] [?15] [?…] tombé entre les mains un[e] [?] du secretaire La Marsilière, qui nous le sort particulierement des afaires de [?]spe[?…]ment, des [?finances], et semble qu'il y facent",
  "qui [?suivent] [?apler] et font [?ts] ofres ; mais nous somes [en] un corps si debile qui ne peut a faire profit de n [?___] [?ilmest] tombé entre les mains un[e] [?___] du secretaire La Marsilière, qui nous le sort particulierement des afaires de [?___]spe[?ade]ment, des [?finances], et semble qu'il y facent",
  "qui [?suieaent apler] et font [?ts] ofres ; mais nous somes {comme} un corps si debile qui ne peut afaire profit de [?n___]. Il m'est tombé entre {les} mains une [?___] du secretaire La Marsiliere, qui nous [?le fort] particulierement des afaires de [?___], spe[ci]alement des [f]inances, et semble qu'ils facent"),
 ("pour [?un] temps. L'on ne sauroit [?…] rendre l[?…] tort que la rupture de ceste armée faict [?a user …]. Car",
  "pour [?un] temps. L'on ne sauroit [?comi] rendre l[?x] tort que la rupture de ceste armée faict [?auser iceduu]. Car",
  "pour u[n] temps. L'on ne sauroit com{p}rendre l[e] tort que la rupture de ceste armée faict au ser[v]ice du [Roy]. Car"),
]
before, after = b21, b21
for old, bef, aft in SEG:
    assert old in b21, old[:40]
    before = before.replace(old, bef); after = after.replace(old, aft)
open(sys.argv[2], 'w', encoding='utf-8').write(before + '\n')
open(sys.argv[3], 'w', encoding='utf-8').write(after + '\n')
