# [Guise] to the duc de Mercœur, 1587 (BnF fr. 15564; DECODE R4155, R4158, R4167)

Catalogue entry "Unknown sender to Philippe-Emmanuel, duke of Mercoeur, 3 ciphertexts". Session 2026-09-22.

Status: read. f. 78 (R4158), the one letter no one had read, is read at 98% of cipher tokens with George Lasry's
2022 key. The other two records were already done: f. 27 was read by Lasry, and f. 151 is closed as too short.

## The three records

| DECODE | folio | what it is | state |
|---|---|---|---|
| R4155 | f. 27 | Guise(?) → Mercœur, in the Guise→Mercœur cipher | **read by Lasry 2022** (cryptiana GL.htm, overlay `GL_BnFfr15564f27decipher.png`) |
| R4158 | f. 78 | same cipher, 3 images of one letter, "Ce xvj Avril 1587" | **read here** (`f78_reading.txt`) |
| R4167 | f. 151 | "MR" slip, 26 June | not this cipher; catalogue item 13, closed as too short in `mercoeur1586/` |

DECODE lists all three as "Non-decrypted", sender unknown, and dates the group 4 Feb – 20 Jun 1587. Lasry's key
names the cipher "Guise → Mercœur" (Tomokiyo: "probably from the Duke of Guise"). f. 78 says "MON FRERE"
(probably Mayenne), "Bellièvre", "estans d'une mesme maison", which fits Henri, duc de Guise, writing to Mercœur,
who was a Lorraine cousin.

## Method

1. Found in the literature: cryptiana GL.htm, "Duke of Guise? in BnF fr.15564": Lasry solved ff. 27, 78, 119 and
   142 in 2022, but published only the key table (`GL_BnFfr15564.png`) and the f. 27 decipherment.
2. Images: DECODE filesrv with the cookie (`img/`, git-ignored).
3. f. 78: every sign labelled in `f78_labels.txt` (one line per cipher run, 952 tokens, with nomenclator groups
   as one token). The cipher is homophonic with a small nomenclator. `beam2.py` runs a beam search over each
   label's key values under `fr-1600-letters` (order 5); `cands.py` holds the candidate values.
4. Three sign-by-sign passes against native-resolution crops (subagent, logged in `f78_decipher.md`) added sign
   values that are missing from or wider than Lasry's sheet: ɋ/ƀ = M, ɛ = F, ≈ʃ = P, the R shape = B, :: = H,
   ∽ = G, ∩ = Y, and ʃʃɤ = MON, ʃbn = NOUS, gb = MONSIEUR, g2 = DUC.
5. Tally: 998 cipher signs (group members counted singly). 983 read as sense: about 900 certain and about 80 from
   context. 15 are open.

## Reading (summary; full text in `f78_reading.txt`)

Guise is glad that "their" advice agrees that the troubles make Mercœur's presence in his government
(Brittany) necessary. He asks Mercœur to put off his decision a few days, until his brother can go and take the
place once Bellièvre arrives. In clear text: the reiter levy is certain, and there is English assurance. In
cipher: the Duke of Parma's troops cannot stay, and it is more important than ever to settle "our affairs" and
stop the passage. On "23": handle it "par la douceur". A lady has gone too far into affairs and persuaded her
husband that "his brother and we" seek only his own contentment. He wants his pensions paid "par la reddition des
places". Guise asks Mercœur to write to "Monsieur de [8ı]" freely, "que le bien general en servira de beaucoup".

## Remaining gaps
- three code groups not in the key (ʃʃ in run 3, ᶜʃʃ in run 7, ≈ƀ in run 22): blocker: open-codes. Each occurs once, and the context guesses (MAIS, QUELQUE, PEU DE) are graded M.
- twelve unresolved signs in runs 3, 17, 18 and 19 (e.g. "EN P[?]", "[??] EMPESCHER", "CE[T ORAGE?]"): blocker: open-codes. All are legible, but no key value or French fits the letter count.
- name codes in the clear text (8ı "Monsieur de …", 23, 12 N): blocker: open-codes. Each occurs once or twice and is not on Lasry's sheet.

## Escalation
- [x] siblings: R4155 (f. 27), R4157, R4162, R4165 and R4167 opened; f. 27 overlay used to calibrate sign shapes. ff. 119 and 142 not on DECODE in this group.
- [x] clear-pages: none. f. 78 has clear text interleaved but no decipherment.
- [x] known-keys: Lasry's fr. 15564 key fits unchanged.
- [x] print: cryptiana GL.htm and henryiii.htm grepped. No printed decipherment of f. 78 was found.
- [x] key-rebuild: LM beam plus three sign-by-sign passes extended the key by about 15 values.
- [x] retry: third pass reran every open span with the extended table and resolved runs 4, 11, 14, 15, 18, 19, 23 and 24.
