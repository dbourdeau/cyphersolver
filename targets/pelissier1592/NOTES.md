# A. Pelissier → Pierre Jeannin, Burgos, 13 September 1592 — **read in part** (90.9% of plaintext words measured 5 Oct 2026 after pass 4, doubtful (?) words counted unread; 95.3% lenient; 183 gaps; key calibrated)

BnF fr. 3982 no. 22, ff. 46r–50r, nine pages; address leaf f. 50v. Gallica ark `btv1b9060543f`; canvases 100–108.
The letter is mostly cipher, with clear-text passages and a few scattered interlinear glosses by a contemporary
decipherer ("non clair" in one margin is the decipherer's own note).

Status before this work: Tomokiyo (cryptiana `league.htm`) calls it "mostly in cipher, only partially deciphered".
He reconstructed Pelissier's key from ff. 111 and 50 (nos. 45/46, Madrid, 27 Oct 1592, which have a clean
decipherment on f. 115). His key image is `league2_key.png`, with zoomed crops in `crops/k0-k3.png`. A web search
(2026-09-18) found no published decipherment of no. 22.

## Pass 3 (2026-09-18/19): key calibrated against nos. 45/46, whole letter re-read

- **Calibration.** Pelissier's letters nos. 45 and 46 (ff. 111r, 113r-v; Madrid, 27 Oct 1592) were aligned sign by sign
  with their clear-text decipherment on f. 115r-v: 1,764 signs (`cal/align_111.txt`, `cal/align_113.txt`, tables in
  `cal/table_*.txt`, exemplar crops in `cal/atlas/`). This confirms Tomokiyo's key and splits the look-alike glyph families
  that pass 1-2 had merged. The result is `GLYPHS.md`. Main corrections: plain 4 is n (or m), never t (t is the hooked z4 / 4y);
  T with a tail is s (and the hooked τ is g); plain 56 = y, flourished s6 = c; the barred 8 = q; + = h and II = l, never e;
  π = i, never s (ϖ = s); 7 = b (or h).
- **Diagnostic.** Before re-reading, a decode that let every token take any letter at a penalty (`diag.py`) showed the merged
  tokens directly (4 → t 355 times, + → e, II → e, o → r/c, T → p/g), matching what the calibration found.
- **Re-reading.** All nine pages were re-read row by row against the scans with the split tokens (`PASS3.md`; `# p3:`
  comments in `t*.txt`; pass-2 states frozen as `t*_p2.txt`, `reading_*_p2.md`).
- **Coverage.** Counting words inside the deciphered {…} stretches: pass 2 read 3,342 words with 413 [?] gaps (89%, 82%
  firm); pass 3 reads 3,734 words with 256 gaps (94%, 90% firm; (?) doubtful words fell from 278 to 158). The remaining gaps
  are single hard glyphs, holes in the paper (f. 50r C13), and a few names.
- **Code groups.** 315 = the Béarnais (again confirmed: "appeler [315] (comme par miracle) a la succession de ceste
  dignite"). 310 (f. 50r) = probably the Duke of Savoy: "ne correspondront pas a ce que pretend [310], et l'ambassadeur a
  esté renvoyé sans aultre esclaircissement sur ses demandes", next to the governor of Milan. 441 (f. 49v) = probably
  France: "non seulement en [441] mais en toutes aultres regions de la Chrestiente". Each occurs once; context only.
- **Newly read, for example:** the 500-ducat grant "qui valent enuiron quatre cens cinquante escus, ou plus", payable at
  Madrid "ou Je me pouuois retirer auec les ambassadeurs et aultres estans par deça de la part de princes estrangiers" (46r);
  Corbie and Amiens among the Picardy places at risk (46v); the need "que l'on mist sus deux armées" (47r); Mayenne under
  the cardinal de Bourbon pressing for his "deliurance" (47v); a war "si sanglante … ne pardonnant a aage ni sexe" (48r);
  "un corps de sept ou huit mil Alemans … Espaignolz et Wallons" (48v); Chartres, Noyon, "les forces d'Allemaigne et
  Angleterre iointes au [315]", Caudebec, Chasteau Thierry (49r); Philip as "liberateur de la Chrestienté" (49v);
  "ilz luy diminuent le credit … l'abaisser le plus qu'ilz pourront. Dieu veulle que je me trompe" and Pelissier's plan to
  take his leave if not provided for within the month (50r).
- **Still open.** The confessor's name on f. 50r reads c-o-r-n-e | n-t-(u/e) ("Cornente"?), doubtful; about 250 [?] words,
  listed per page under "Rows still unresolved" in `reading_<folio>.md`.

## Result (pass 2)

- **The key.** Tomokiyo's key reads this letter. It is a homophonic alphabet: 2–7 signs per letter, some two-digit
  number signs (24/26/28/30/33/36/44/56/60/80), `vv` = et, a few doubled-letter signs (rr, ss, uu) and several nulls.
  A three-digit code group **315 = the Béarnais (Henri IV)** fits every context: "le [315] ayant incontinant tourné
  la teste et s'estant campé pres l'armée catholique", and "les forces d'Allemaigne … iointes au [315]". **310**
  (f. 50r) is a second code group; it is not read.
- **Transcription.** 377 cipher runs, about 18,400 signs, were transcribed sign by sign (`t46r.txt` … `t50r.txt`) and
  decoded with a quadgram beam search over each sign's possible letters (`beam.py`, `cands.txt`).
- **Coverage.** About half to two-thirds of the ciphered text now reads as continuous French. The rest is marked
  [?] in `READING.md`, and every page's `reading_<folio>.md` lists its open rows with their tokens. The clear text
  is read in full.
- **Glosses.** They agree with the key wherever they can be checked: "de", "auisa", "meschans", "roy", "Les tirer",
  "Noyon", "a la main qu", "nauoit", "en atendant", "quar la bataille", "mais le retour", "de crainte", "langaiges",
  "Valentia", "a gens matez des", "(quay)ant pleu a dieu", and others. One gloss ("os a orc" over "nos forces")
  shows the glosser applying the ϙ = a cell literally where the sense needs f.

## What the key really looks like (lessons from the transcription)

The first-pass token set (`TOKENS.md`) merged several look-alike signs that the key keeps apart. Most residual
errors come from these merges, not from the key.

- `56`: the flourished s6 is **c** and the plain 56 is **y**. Both are cells in the key, and the gloss "roy"
  confirms y.
- δ: the plain δ is **o**. The δ with a long curling hook is **c** (c column, cell 1). The closed-loop ∂ with a
  curled top is **r** (r column, cell 2).
- T: the flat-topped ⊤ is **a**. The hooked τ is **p** (p column, cell 1). The small curled "Tz" is **g** (the 12
  cell).
- I: the plain Ɨ is **l**. The bold-footed Ɨ is ⊥, **o**. The double-barred one is **Ƒ, o**.
- `vv`: **et**, and also **ff** (affection, difficulté, deffence, souffert, suffisantes).
- ϙ: **a** in the key, but **f** in many words (faire, fortifier, fidélité). This is probably the key's `9` f cell.
- ℋ is q. ℋ with a lead-in stroke is **h** (Chartres, empesché). `3` is **b**, not a null (subiectes, bons).
- The small plain r is **f** (fin, fruict, fascheux). `∞`/`oo` is m, and once "et" (gloss).
- The scribe sometimes repeats the tail of a line at the start of the next line after restarting. Each repeated
  run is transcribed once.

`cands.txt` gives each token the key letter first, with these alternatives at small penalties, so the decoder can
arbitrate. Do not try to re-derive the key by letter-frequency hill-climbing. Two attempts here (`solve.py`,
`refine2.py`) collapsed to the all-e attractor on noisy transcriptions. The key is right, and the remaining errors
are in the glyph reading.

## Content (summary)

Pelissier was the League's (Mayenne's) agent at Philip II's court. He writes to Jeannin, Mayenne's councillor.

1. **f. 46r.** Pelissier reached Valladolid as the court was leaving. Don Juan de Idiáquez put business off to
   Palencia. In cipher he says his credit has run out (he cannot repay loans made in Madrid), takes the King's
   silence as a refusal, and asks leave to return to France. The answer is that the King has his own ministers in
   France, and Pelissier may go or stay. Idiáquez has seen Mayenne's circular letters calling the Estates. The King
   grants Pelissier **500 ducats (≈450 écus)** payable in Madrid, so that he can wait for news.
2. **f. 46v.** At Burgos, Don Juan gives him a private hour. Pelissier argues that a state's reputation is
   everything, and illustrates this with Parma's army of 1592. While it flourished, the royalist Catholic nobility
   went home and towns began to treat. If it had wintered in France, [315] would have been ruined and the Germans
   would not have dared come. Its return to the Low Countries undid all this; La Fère, Soissons and Picardy are in
   danger.
3. **ff. 47r–47v.** The French do willingly what they are asked, never under force, as the revolt against "the
   last king" (Henri III) showed; mildness and benefits will win them. The King questions him: does he speak on
   Mayenne's orders? Pelissier has had no word from Mayenne since the armies faced each other at Caudebec, and
   speaks from his friends' reports. The Spanish reply is that no king has ever given such help, and any failure is
   the fault of those who received it. Pelissier's reasons for delaying the Estates are taken as a trick. The
   minister admits that the League's French would take it very badly if Spain delayed "la nomination d'un roy
   legitime pour l'opposer a l'heretique et tyran". "Ilz ont les oreilles delicates."
4. **f. 48r.** New counsels are needed, a "third means". This is the wrong time to hold the Estates, because the
   people, clergy and nobility are exhausted and would sooner accept an accord that makes a king against "celuy qui
   se pretend". The war may end only in the extermination of one of the two royal lines. He backs the plan of **two
   armies**: one to push the enemy from the Seine to the Loire, one to take the Seine towns and free Paris and Rouen.
   The cost would be nearly **300,000 écus a month**, but only for a few months.
5. **f. 48v.** The army should be mostly French, stiffened by Germans, Spaniards and Walloons. A victory would ruin
   the enemy; a defeat could be absorbed by Philip's own nations. The current piecemeal aid only ruins the
   provinces. If Philip showed "quelque affection particuliere en la nomination du roy", everyone would follow him.
6. **f. 49r.** A narrative of the 1591–92 campaigns: Chartres, Noyon, the Prince of Ascoli's relief, Caudebec,
   Henri's offer of battle, the League army's retreat towards Château-Thierry, and Henri master of the countryside
   at Châlons. Parma is blamed for letting chances to fight go by. Rumours spread that Philip defends the cause only
   to keep the French busy while he subdues his Low Countries rebels.
7. **f. 49v.** Men say Philip wants France kept in balance so he can take his share of a divided crown. The
   case made for recognising Navarre is set out: God called him "comme par miracle"; he is poor and worn out from
   his youth, will want peace, and the Catholics would be released from their oath if he turned on them. War-weary
   people listen. Philip alone can cure this and become "liberateur de la Chrestienté".
8. **f. 50r.** "They" are undermining Mayenne's authority (finances, command, credit). A figure at court "a la
   pulce en l'oreille" (learned from his Jacobin confessor). An ambassador has been sent back without an answer. A
   plea for union. Pelissier stays at court to press for the **50,000 écus** the Idiáquez keep promising, and will
   wait out the month. Signed "Vre bien humble et obeissant serviteur Pelissier", Burgos, xiij septembre 1592,
   marked "Tripta" (triplicate). The postscript concerns someone sent to Palencia and honoured by the King, down to
   horses sent for his audiences.

## Files

- `t<folio>.txt`: token transcription per page, with `#` comments recording pass-2 corrections.
- `reading_<folio>.md`: reading, summary, gloss table and open rows per page.
- `READING.md`: the nine readings in sequence.
- `beam.py` and `cands.txt`: the decoder. Run `python beam.py t46r.txt`. `dec_<folio>.txt` holds the raw decoder
  output.
- `TOKENS.md`: the token vocabulary and glyph descriptions.
- `PASS2.md`: the second-pass brief. `agent_reports.md` holds the first-pass reports.
- `crop.py` and `bands3.py`: crop helpers. `img/` holds the full-res scans; it is not committed.

## Next steps

- A third pass on the open rows, splitting the merged tokens above in the transcriptions themselves (not only as
  decoder alternatives).
- Read code group 310, and the confessor's name on f. 50r.
- Nos. 45 and 46 (ff. 111, 113, with the clean text on f. 115) are the calibration letters. Checking their
  sign-to-letter pairs row by row would settle the remaining homophone doubts.

## Remaining gaps

- code group 310 (f. 50r, probably Savoy), 441 (f. 49v, probably France) and the confessor's name on f. 50r - blocker: open-codes; each occurs once; context only
- 183 [?] words across the nine pages - blocker: illegible; after pass 4 every gap was re-cropped; the rest are legible signs that do not decode under the key, blots, and empty-sign gaps; recurring name groups `z 6 z`, `z 6 1`, `z 5 8` tested at every occurrence (z 6 z and 26 I are also ordinary letters elsewhere; no single value forced), listed per page in reading_<folio>.md
- holes in the paper, f. 50r C13 - blocker: illegible; paper lost; no other copy of no. 22

## Escalation

- [x] siblings: nos. 45/46 (ff. 111, 113) aligned with their decipherment on f. 115
- [x] clear-pages: f. 115 clear decipherment used for calibration; interlinear glosses checked
- [x] known-keys: Tomokiyo's Pelissier key applied and confirmed
- [x] print: Tomokiyo league.htm; web search 18 Sept 2026 found no printed decipherment of no. 22
- [x] key-rebuild: key calibrated on 1,764 aligned signs, look-alike classes split (GLYPHS.md)
- [x] retry: pass 4 (5 Oct 2026, PASS4.md): every [?] on all nine pages re-cropped and re-read; 256 -> 183 gaps, 0.909 strict (doubtful (?) words unread, the project rule) / 0.953 lenient
