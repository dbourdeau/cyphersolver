# rakoczi1632: George I Rákóczi's instructions for Germany, 1632 (BSB Clm 10401 n.139)

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

Not in the catalogue. Found in WAINUT's sweep for cipher documents with a contemporary decipherment; Halm's
manuscript catalogue (1874) names the cipher and Camerarius's solution. Contributed by WAINUT, 3 Nov 2026.

| Document | Cipher | Job | Cipher words | Read by the frozen key | From the gloss only (cipher departs) | Not read | Status |
|---|---|---|---|---|---|---|---|
| fol. 491r (scan 1199) | numbers 1-99, ten extra signs, three code groups, embedded in clear Latin | transcription job, interlinear gloss | 69 | 54 (78.3%) | 11 | 4 | read in part |
| fol. 491v-492v (scans 1200-1202) | same | transcription job, interlinear gloss | not counted | 12 held-out words only | | | not done |

The page also has 78 clear Latin words (3 doubtful). Counting them, fol. 491r gives 140 of 147 words (95.2%), but
those words were never enciphered, so that figure is not the measure of this work.

Status: **read in part**. Fol. 491r is 1 of 4 cipher pages. Of its 69 cipher words, 54 are read by the frozen key
(78.3%); another 11 come only from the contemporary gloss where the cipher departs from the key (65/69 = 94.2%);
4 are not read. Fol. 491v-492v (scans 1200-1202) are not done beyond 12 held-out words. (Counting the page's 78 clear
Latin words, which were never enciphered, gives 140/147 = 95.2%; that figure says little about the cipher and is not
the headline.) Since the key was built from the glosses of this same page, "read by the key" on fol. 491r means
"consistent with the gloss"; the only independent test of the key is the held-out test on fol. 491v. This is a **transcription job, not a break** (CONTRIBUTING rule 6): Ludwig Camerarius's interlinear
decipherment covers nearly every cipher word.

## Document

Munich, BSB, Clm 10401 (Collectio Camerariana vol. 51), n.139. Halm 1874 p. 114 (running head "Cam. 51", checked on
the catalogue page; Cam. 51 = Clm 10401 holds), "Ragocii mandata in Germaniam missa (in Chiffern geschrieben mit
Auflösungen von Ludw. Cam. Hand), nebst Bericht über dieselben". MDZ bsb00117497 (1326 scans, microfilm, 1442 px
wide): cipher on scans 1199-1202 (fol. 491r-492v; folio numbers as written), the "Bericht" in clear Latin on scans
1203-1205 (fol. 493-494: "Quod in conditionibus stabiliendi inter S. R. M.tem Sueciae et Ragozium Principem
foederis..."; a separate text, not the decipherment, not used as a crib). Neighbours: n.138 Capitulation of Landgrave
Georg, Höchst 19 Nov 1632 (scans 1197-1198); n.140 a Dutch extract of 31 Jan 1641. Margin of fol. 491r in
Camerarius's hand: "Ragocij Mandata missa a se in Germaniam data". Undated; content (Saxony and the "United Princes"
as partners of the King of Sweden alive, i.e. before Lützen, 16 Nov 1632) fits 1631-32.

## System

Homophonic substitution of the Latin letters by numbers 1-99 written with dots between groups, a few extra signs
(written {a}, {phi}, {d}, {c}, {mu}, {x}, {E}, {z}, {s}, {b} in the files), and 3-digit code words for names
(217.11.99 and 218.88 = King of Sweden, 307 = Principes). Cipher words are embedded in clear Latin. Two to nine
numbers per letter (e: 32, 56, 80, {phi}; s: 38, 62, 86, {x}; ...). u after q is not written.

## Key (`key.tsv`)

72 entries built only from glossed pairs on fol. 491r, then frozen. (The gloss over word 44, found later by the
independent check, was not added; its groups agree with the key anyway.) Two groups take two values on this page, both
glossed: 28 (d 4x, i 4x) and 76 (d in adversas, o in nostro). 41 = g comes from an unglossed word only (marked).
Values for 44 (t, and b on fol. 491v) and {s} (l, and c on fol. 491v) show the table has more such cases.

**Held-out test** (`scripts/heldout.py`, `heldout_f491v.tsv`): first lines of fol. 491v, read after the key was
frozen; 12 glossed words, 87 letters: the frozen key agrees on **79 = 90.8%**; 2000 shuffled tables: mean 5.5,
best 25. The "expected" letters were aligned to the groups **by hand, after seeing the cipher**: hae- for
*hereditatum*, e dropped from *omnes* and *impetitores*, *nemini* started at its second letter (first group cut off).
Each of these choices can only raise the score, so 90.8% is an upper estimate on 12 words. Disagreements: 44 = b twice, {s} = c twice, 45 = h, a delta-like sign = s, 19 for i, 32 for m.

## Reading of fol. 491r

Files: `transcription_f491r.txt`, `words_f491r.tsv` (69 cipher words: pass 1, settled reading, gloss, reading,
note), `decryption_f491r.txt` (rebuilt by the checker), `reading_f491r.md` (Latin), `translation_f491r.md` (English).
`key_frozen.tsv` is the table as frozen before the held-out test; `key.tsv` has the same values.
`python scripts/check_marks.py f491r` rebuilds the decryption from transcription, table and key and fails on any
unmarked departure from the key, any mark without a doubt under it, and any gloss-only reading whose gloss differs.
Result: ok. Counts: clear words 78 (3 doubtful), cipher words 69 (65 read, 11 of them from the gloss over a cipher
departure; 4 not read).

Transcription method: pass 1 from whole-width strips at 1.1x; pass 2 from half-width bands at 2.0x; disagreements
(8 words, column `pass1`) settled on 3x crops. After the independent check (VERIFY.md) word 41 was rechecked on the
full-size crop: its first group is 86, as in pass 1 (pass 2 had 80); the key then gives *substantiasque* (gloss
*substantiarumque*), kept as the cipher reading like *ipsis*/*nemine*/*inibunt*. Digits were recorded before the glosses were used. Several signs are
ambiguous on the microfilm (32/82, 80/86, 30/80, 40/46, 23/28).

**Cipher-vs-gloss differences (findings, not repaired):** the cipher spells *constr[in]gamus* where the decipherer
wrote *coniungamus* (word 27); *thesauri* where the gloss is abbreviated *thesaur.*; *ipsis* (gloss *ipsi*);
*nemine* (gloss *neminem*); *inibunt* (gloss read *inibant*); *substantiasque* (gloss *substantiarumque*);
*advenient* (gloss *adveniant* or *advenient*); 11 words where single groups break the key (listed by the checker:
perveniens, coniungamus, adversa, amissionem, deserent, personis, auxilio, adveniant, scitum, fato, fungi); some are probably microfilm misreads, some encipherer's slips.

Summary: an instruction ("Memoriale") for an envoy of the Prince of Transylvania: travel discreetly to the King of
Sweden and treat with him, Saxony, the other Protestant electors and the United Princes; avoid capture. If they ask
the Prince to join the common cause, they must swear not to abandon him in good or bad fortune, to help him in
person if needed, to make no peace without his knowledge and consent, and, should he die, to take over the care and
defence of his heirs. Context: George I Rákóczi's approaches to Gustavus Adolphus in 1631-32 (the mission of the
Swedish envoy Paul Strassburg to Transylvania, 1631-33).

## Remaining gaps (fol. 491r)

- [?Itinere] (word 2): decodes "itiner"; the following "a" is either its last letter or a preposition.
- [?agat] (11): 41 = g only here, unglossed.
- substantiasque (41): settled as 86 (see above); the gloss and the grammar want *substantiarumque*.
- <deserent> (44): glossed after all (the solver missed it); the cipher has a doubled 32 (de-e-serent).
- [?de] (65): decodes "ie"; unglossed.
- [...] (69): decodes a-?-e-l-a-t-u-n-t (or a-?-e-l-a-b-u-n-t with 44 = b as on fol. 491v); the gloss (perhaps
  "habebunt") not legible with certainty.
- Clear text: [?a] (line 2), [?usque] (line 18), [?illam] (line 29).
- Outside blocker: microfilm only; a colour scan of fol. 491r would settle most single-sign doubts.

## Other keys tested

- This repository, Rákóczi targets: the DECODE R639 Bonac-Groffey table (`targets/rakoczi1704`, `rakoczi1707`, Francis II
  Rákóczi, 1703-11) agrees on 3 of 229 glossed occurrences (1%) (`scripts/test_repo_keys.py`, run on the table of targets/rakoczi1707): a different cipher.
  The Keresdi Bethlen key of `targets/transylvania1645` is a letter alphabet with no numbers: not applicable.
- WAINUT's own working reading of a Camerarius code of 1621-22 (not submitted): a word nomenclator with numbers to ~3200; its
  letter numbers do not fit ("Land-drosten" 60.49.43.50.63.19.42 = d r o s t e n there; here 60 = f, 49 = i, 43 = t,
  50 = p): not the same system, so this is its own folder.

## Collision check (3 Nov 2026)

origin/main (head d803a1d8d): no target for Clm 10401, the Camerariana or George I Rákóczi's 1632 instructions;
Rákóczi targets are rakoczi1704/1707/1711 (Francis II) and transylvania1645 (Keresdi Bethlen). Open PRs #201, #216,
#227 unrelated.

## Prior art (3 Nov 2026, one search)

Searched for the 1632 instruction in the Hungarian source editions. Not found online in the time allowed. The likely
place is Szilágyi Sándor (ed.), *Okirattár Strassburg Pál 1631-1633-iki követsége és I. Rákóczy György első
diplomácziai összeköttetései történetéhez* (Budapest 1882; full text on MEK, https://www.mek.oszk.hu/20100/20169/),
and Szilágyi's *Okmánytár I. Rákóczy György svéd és franczia szövetkezéseinek történetéhez* (1873). If the
instruction is printed there, that is a crib and the result is a pointer, not a first reading. Not checked.

## Images

https://www.digitale-sammlungen.de/en/view/bsb00117497?page=1199 (fol. 491r), ?page=1200-1202 (cipher continued),
?page=1203 (Bericht). Halm 1874: https://www.digitale-sammlungen.de/en/view/bsb11184610?page=124 . Fetched by
`scripts/fetch.py` (IIIF, one request at a time, 1 s apart, User-Agent WAINUT-research); no blocks met. Scans not for
git. Transcription and reading were done by AI language-model agents working from the images. No human palaeographer
has checked them.

## Prior art check, Szilágyi 1882 (3 Nov 2026)

Szilágyi, *Okirattár Strassburg Pál 1631-1633. követsége és II. Rákóczy György 1649-1667. svéd szövetkezése
történetéhez* (Budapest 1882), the full text on MEK (mek.oszk.hu/20100/20169), was searched by phrase in its OCR text
for words of the fol. 491r reading: "Memoriale", "circumspecte", "vigilanter", "manus adversas", "adhaereamus",
"iuramenti/juramenti sacramento", "haeredum nostrorum", "Saxone". None occurs. The memorial is therefore not printed
in that volume as far as an OCR search can show; OCR errors or a paraphrase could still hide it. Other editions of
Rákóczi's 1632 correspondence were not searched.

## Prior art check, Szilágyi 1873 (3 Nov 2026, after the independent check)

Szilágyi Sándor (ed.), *Okmánytár I. Rákóczy György svéd és franczia szövetkezéseinek történetéhez* (Budapest 1873,
Monumenta Hungariae Historica, Diplomataria 21), BSB copy bsb11156963, searched through the MDZ IIIF full-text
search service (one query at a time, paced). The search works on this volume (controls: "Strassburg" 7 hits,
"Gustavus" 2). No hit for: adhaereamus, circumspecte, vigilanter, juramenti, iuramenti, Saxone, exposcimus, obligent,
conjungamus, coniungamus, Unitis. Hits for common words fall in other documents: "Memoriale" (p. 118) is a Hungarian
memorial of 18 Nov 1643; "incidat", "pervenire", "jacturam", "defensionem", "prospera", "adversa", "sacramento" occur
only in other letters. Closest: p. 27-29 print alliance conditions with the King of France ("Christianissimus Rex")
that use like clauses ("nullaque ratione et praetextu eos deserent"; the care of the Prince's widow, children and
heirs), a later treaty text of the same family, not the 1632 memorial. Result: the memorial is not printed in the
1873 volume as far as an OCR search can show (OCR errors could hide single words, but not all eleven distinctive
ones). Not searched: Szilágyi's 1874 *Okmánytár II* and the 1874 French *Actes et documents*, Hungarian
periodicals, Swedish editions (e.g. Rikskansleren Axel Oxenstiernas skrifter). So: no edition found; not proven new.

## Independent check and what was changed (3 Nov 2026)

`VERIFY.md` is the report of an independent AI language-model agent (not the solver), kept unchanged. Verdict: fix;
status "read in part" stands. Blind transcription of about 508 signs (fol. 491r lines 1-28, 433 signs, and the first
five lines of fol. 491v): raw disagreement 17/508 = 3.3%; after full-size crops the solver was wrong in 2 (0.4%),
9 stay ambiguous on the microfilm (at most 2.2%), none changes the sense. Rebuild in a scratch copy was
byte-identical; negative tests made the checker fail as it should. Reading grade B.

Changes made after it (the counts above are after them):

- Headline restated on cipher words (was 138/147 = 93.9% of all words, which included the 78 clear words).
- Word 44: the gloss "deserent." is there (the solver had it as unglossed); now `<deserent>`. On our crop the end of
  the gloss is faint; *deserunt* cannot be excluded, but the cipher has -ent either way.
- Word 41: first group 86, not 80, on the full-size crop (also the solver's pass 1); now read by the key as
  *substantiasque*, the gloss *substantiarumque* noted.
- Held-out test: the hand alignment of expected letters is now stated (above and in `heldout_f491v.tsv`).
- Prior art: Szilágyi 1873 searched (above); nothing found.
- Line 4 group 28/25 in *perveniens* (verifier weakly 25) left as 28: both give i, the word is a gloss reading anyway.
- Not changed: the key. The gloss of word 44 came after the freeze and was not added.
