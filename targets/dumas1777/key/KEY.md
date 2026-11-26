# The key: "le grand chiffre des 13 lignes"

**Who established it.** Dumas set out the system and the line totals himself, in his letter of 30 April 1776 to the
Committee of Secret Correspondence (Papers of the Continental Congress, item 93 vol. 1, images 14-19; printed in the
Papers of Benjamin Franklin 22:403-412). Satoshi Tomokiyo (Cryptiana, "Dumas' Cipher - Benjamin Franklin's Favorite
Cipher", 2008-09, https://cryptiana.web.fc2.com/code/franklin.htm) established the 13 lines of key text from the
Committee's enciphering table and showed the homophonic structure. We did not recover the key; we rebuilt it from these
sources and tested it against the contemporary glosses.

**Key text.** Thirteen printed lines of Dumas's 1775 Amsterdam edition of Vattel, *Le Droit des gens*, "Lettre de
l'éditeur à Monsieur ***": page III (last 3 lines), page IV (7 lines), page V (first 3 lines). From "Voulez-vous sentir la
différence?" to "dans leur juste résistance." File: `keytext_1775.txt` (one line per printed line). Wording from the 1830
Paris reprint (HathiTrust uc1.a0000513937, seq. 62-63) adjusted to Dumas's line totals, and Tomokiyo's transcription
where the reprint differs ("jettez", "reconnoîtrez", "colons vous" without comma, "ceux, qui,", "& la dureté", the
printed line-end hyphens "révolte-|rez", "trem-|bler", "sou-|haiter").

**Counting rule** (Dumas, 30 April 1776: "Tout a son nombre"). Spaces are not counted. Every other printed character is:
letters, apostrophes, hyphens (including line-end hyphens), commas, full stops, the question mark, "&" and the reference
mark "*" (one character). Positions run 1 to 682 straight through the 13 lines; the line ends fall at 57, 114, 168, 223,
278, 335, 394, 445, 499, 555, 612, 666 and 682, exactly Dumas's totals (`build_key.py` checks this). Accents are ignored
in use. Every occurrence of a letter is an alternative number for it (e, with its accented forms, has 129 numbers and s has 60, counted in `key_positions.json`). The text has
no k and no w; Dumas told the Committee to use c for k and v (or vv) for w, hence "Van Berchel". The hyphen (7, 223, 370,
499 ...) is used as a dash or an abbreviation mark ("F=" for France).

**The one difference from Cryptiana's page.** A second AI agent of ours built the key independently from the 13 lines
printed on Cryptiana (`key_second_agent_from_cryptiana.txt`, 682 characters, spaces and accents dropped, "=" for the
hyphen). It differs from ours in one position of 682: position 515, where Cryptiana's page prints "suciombent" and we have
"succombent". The page's form is a typing slip: the line total needs ten letters in the word either way, and 515 = c is
confirmed in use (it gives the c of "ici" in the letter of 14 June 1778, where the decipherer wrote c). The second agent's
file has the slip corrected and is then identical to ours in all 682 positions.

**Frozen.** `key_positions.json` (position -> character) sha256
`36276e0a73f3dd58d8940202b7c97033fb706bb576317083a083a2808744ae74`; `keytext_1775.txt` sha256
`77674df311e706f693c6000ce02fd5e49b5a808f68f7c2081275b614b9151de2`. Both hashes are written in `FREEZE.txt` and were
recorded in the test 2 plan before that test was run. Rebuilt and re-hashed on 14 Nov 2026 with `python build_key.py`
(same hashes).

**Check against the glosses.** `build_key.py` also compares the key with the 369 numbers glossed on M332 images 9, 10,
13 and 20 (the first reading's gloss key, `../tests/test1/key_full.json`): 363 agree. The six others are glossers' letter
forms or misreadings (u written n, j written l, long s read as &, a comma read as d), the number 54 discussed with the
letter of 14 June 1778, and one real Dumas/decipherer conflict (545).
