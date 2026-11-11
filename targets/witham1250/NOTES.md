# River Witham sword, gold-wire blade inscription (British Museum 1858,1116.5)


Found 1825 near Lincoln, dated 1250-1330. Inscription, one blade face, gold wire inlaid in steel, framed by two crosses:
`+NDXOXCHWDRGHDXORVI+` (18 letters, no word division, per Harrison/British Library 2015 and Winter 2016).

## What exists already (checked 9 Nov 2026)

- British Library appeal 11 Aug 2015 (Julian Harrison): "as yet indecipherable"; perhaps a religious invocation; Welsh floated.
- Cipher Mysteries (Jan 2016, comments by Nick Pelling) / Language Log threads (2016): about twenty commenter readings (Latin initials, "Christ reigns,
  conquers, commands", gematria, Hebrew, Croats ...), none checkable. Parallels named: Alphen aan den Rijn sword,
  Berlin and Swedish swords (shared curved X, I-S ligature); Wagner/Worley 2009, 2013 on "talking" swords.
- Harald Winter, Waffen- und Kostuemkunde 58/2 (2016), revised 2026-03-13, doi 10.71475/wkk.2016.2.115248:
  initials reading, N(omine) D(omini) X=CH(risti) / O(pe) X=CH(risti) CH(evalier) W / D(efendit) R(e)g(em)
  H(onorem) D(omini) X=CH(risti) OR(bos) VI(duas). "In the name of our Lord Jesus Christ. With Christ's help
  Sir W defends the king, the honour of God, orphans and widows."

## Assessment

- Letters: vowels O, O, I = 3 of 18 (17%), against about 40% in Latin text. That fits an abbreviation or initials
  inscription, and does not fit running text in any language. D x3, X x3 repeat.
- Nothing here can be tested. Every proposal picks the expansion of each letter after the fact, with X taken as
  Chi, cross or spacer at will. 18 letters under free abbreviation have no unicity: many Latin, Germanic and Welsh
  phrases fit equally. Winter's reading is internally coherent and period-plausible but unverified (X=CH, W as a
  name, "chevalier" mixed into Latin are all choices made to fit).
- No key, no plaintext, no clear copy. Only route to an evidence-based reading: a corpus of sibling inscriptions
  (Alphen, Berlin, Swedish, Thames, Ulfberht-type) read as a family, which needs photographs and the Wagner/Worley
  catalogue (not seen).

## Sibling check (9 Nov 2026)

The Alphen aan den Rijn blade (BENEDOXO ... MTINIUSCS, myarmoury.com/talk/viewtopic.23973.html) is itself only
speculatively read ("Benedictus, Sanctus Martinus"). Siblings share the Benedicat/Trinity-style XOX flavour but
supply no verified key, so they cannot anchor a reading of the Witham letters.

## Remaining gaps

None that this session can close: ciphertext-only on 18 letters; sibling corpus needs outside material (catalogue,
photographs, museum access).

## Escalation

Siblings: named above, not digitised in reach. Clear pages, known keys, print, key rebuild: not applicable (no
cipher key exists; abbreviation inscription). Retry: not warranted without new material.

## Transcription check and family match (Brice Dudout, with Claude, 11 Nov 2026)

Class unchanged: **not read**. What is added is a corrected transcription and a measured family classification; no
expansion of the letters is claimed or testable. Files, scripts and sources: `dudout/README.md`.

**Transcription.** On two independent British Museum photographs (the inscription detail on the BL blog of
3 Aug 2015, "image courtesy of the British Museum", and BM collection image 00296785; examined, not reproduced: BM
images are CC BY-NC-SA by BM policy, but the live object page refused access, so we treat them as BM copyright) the
10th letter is an uncial N (two stems under an arch, curled foot, no bowl; the real R at #16 has bowl and leg) and the
11th is a C with a curled upper terminal, the mirror of the C at #6. Reading: `+NDXOXCHWDNCHDXORVI+`
(`inscription.txt`; the BL 2015 reading is kept there as a comment). Independent support:

- Stamford Mercury, 18 Aug 1826, "N D K O K C H S D N C H T K O R Y D" (quoted by Rob Wheeler, BL blog comment,
  7 Aug 2015): N and C at these two places.
- Marc van Hasselt (BL blog comment, 6 Aug 2015): `+ND XOX CH WDN CH DXO RVI+`, "not one C and one G". Several
  BL / Language Log commenters (Ellen, MetalJeeper, J. L. Gil, B. Rapallo) also took the first "R" for an n.
- The BM database (2019 snapshot) reads `+NDXOXCHWDRCHWDRCHDXORUN`: a dittography of CHWDR, and a final N that is the
  I touching the cross.

Uncertain: #17 V (Y-like; 1826 "Y"), #18 I (or N). The letter forms (O with an inner stroke, C with a curled terminal
read as C, rounded X, uncial N) are those Wagner et al. 2009 describe for Fyris UMF/B 74 and Karlstad (pp. 24, 30,
fn 74). Position-by-position table: `dudout/TRANSCRIPTION.md`. (Small date note: the BL post is of 3 Aug 2015; the
postscript with van Hasselt's note was added 7-10 Aug.)

**Family match (new measurement).** Longest common subsequence (LCS) of Witham with each of the 18 published sibling
inscriptions of 9 letters or more (Wagner et al. 2009 readings; two unverified blog transcriptions marked), against
5000 shuffles of the Witham letters (composition kept, order destroyed; p = (k+1)/(n+1)):

| sibling (Wagner et al. 2009) | LCS, new reading | p | p, BL 2015 reading |
|---|---|---|---|
| Fyris UMF/B 74 (p. 30) | 13/18 DXOXCDNCDXORI | 0.0002 (no shuffle reached 13) | 0.0008 (12/18) |
| Marburg (p. 33) | 11/18 NDXOHNDXORI | 0.0012 | 0.0006 |
| Oldenburg (Post, fn 58/82) | 8/18 | 0.058 | 0.027 |
| W 897 b, W 879 a | 7/18, 8/18 | 0.07, 0.08 | 0.05, 0.06 |
| the other 12 | 2-9 | 0.12-1.0 | 0.25-0.99 |

Multiple tests: Bonferroni over the 18 siblings gives 0.004 (Fyris 74) and 0.02 (Marburg); the siblings are not
independent (Marburg and W 879 share their formula), so this is conservative. Both readings were tested and both
pass, so the result does not depend on the correction. Controls, same test against Fyris 74 and Marburg (3000
shuffles): Ulfberht, IN NOMINE DOMINI, GICELIN ME FECIT, HOMO DEI, INGELRII ME FECIT, the St Benedict medal initials,
the laudes initials and Witham reversed all give p 0.3-1.0. The order of the Witham letters is the family's order.

**Prayer fit (negative).** Against 44 Latin prayers and formulas (Vulgate, Roman rite, the Pontifical's blessing of
a sword), taking each letter as an initial or a standard nomen sacrum, Witham's longest contiguous run is 3 letters,
p = 0.73 against 1000 shuffles (coverage by runs of 3 or more: p = 0.37). It is not the acrostic of a known prayer.
It reads as a shortened copy of the SDX invocation of the Fyris 74 / Marburg / W 879 group:
N(EH)DXO ... (E)HDXO(EH)R in Marburg and W 879 against NDXO ... CHDXOR here (C for E, as Alphen's CSD / ESD).

**Consequence for prior readings.** Winter 2016's "D(efendit) R(e)g(em) H(onorem)" (not seen by us; Daniel's summary
above) and the other DRGHD-based proposals rest on #10-11 as misread; "CH = chevalier" sits where the siblings have
EH. The meaning of the family elements (DX = Dominus Christus, O invocative, EH(R) = Middle High German "ehr(e)") is
Wagner et al.'s conjecture and is not tested here. Proposals scored in `dudout/PROPOSITIONS.md`.

**Evidential level.** Shown: membership in the SDX family (order-specific, controls null, survives correction for 18
comparisons). Not shown: any expansion of any letter.

Credits: Marc van Hasselt (Madoc 2014; BL blog 2015: the N/C reading and the family link), T. G. Wagner, J. Worley,
A. Holst Blennow and G. Beckholmen (WKK 51, 2009; Worley & Wagner WKK 55, 2013: sibling readings and letter forms),
Rob Wheeler (the 1826 newspaper), H. Winter (WKK 58/2, 2016, via Daniel's summary). Images: British Museum, cited by
number only.
