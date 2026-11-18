# The Hungarian court cipher of 1482: Beatrice d'Aragona to Eleonora (DECODE R1140, R1141) and Matthias Corvinus to Ercole I d'Este (R1156), Pozsony, May–June 1482

Status: found already in print (MDE III, 1877, nos. 10 and 12 for the queen's letters and no. 11 by Vestigia's record for the king's, not no. 14 as written here before: 14 is the page; Fraknói 1895 no. 131). See RESULT.md for verification limits. Since 14 Nov 2026 the
1482 key is rebuilt from the period clear copies (Brice Dudout, PR #620; `vestigia/`), and one run of R1141 that the print
leaves out is restored. The king's letter of 1 June 1482 (R1156, until 14 Nov 2026 the separate target `matthias1482`)
is in the same key and was folded in here the same day: its folder is [`matthias1482/`](matthias1482/), with its old
notes and profile kept as `NOTES_matthias1482.md` and `profile_matthias1482.json` (see "Fold of matthias1482" below).

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 160 grouped five DECODE
records by sender. This entry keeps the two 1482 letters (R1140, R1141), in the 1482 alphabet. The others now have
their own folders and pages (each a different cipher, or none, with its own page):
- R1142, Buda, 8 March 1486: [`targets/beatrice1486/`](../beatrice1486/NOTES.md). Its alphabet looks different from the
  1482 one, and the letter says it uses "the old cipher" and encloses a new one;
- R1143, Buda, 2 May 1486: [`targets/beatrice1486b/`](../beatrice1486b/NOTES.md). Two months after the new cipher was
  sent; not shown to share a key with R1142;
- R1154, Naples, 29 May 1505: [`targets/beatrice1505/`](../beatrice1505/NOTES.md). Plain Italian, not a cipher.

RESULT.md (the research report on all five), metadata.json, original_catalogue_entry.json and fetch_decode.py stay
here as shared material; the OCR extracts for R1142, R1143 and R1154 moved to the new folders' `readings/`.

Research begun 20 September 2026 from the user's goal-objective attachment.
No new cryptanalytic reading claimed. The table below preserves the starting DECODE metadata; corrections and primary-source evidence are in RESULT.md.

| Record | Date | From / to | Shelfmark suffix | Pages |
|---|---|---|---|---|
| R1140 | 31 May 1482 | Pozsony / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 4a | 1 |
| R1141 | 8 June 1482 | Pozsony / Eleonora | Cancelleria 1523 [name says 1623], b. 2/2, 2, 5a | 1 |
| R1142 | 8 March 1486 | Buda / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 10 | 5 |
| R1143 | 2 May 1486 | Buda / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 18 | 5 |
| R1154 | 29 May 1504 | Naples / Ippolito | Carteggio Principi Esteri 1623, b. 2/7, 11 | 1 |

The attachment's umbrella shelfmark b. 2/2 and origin Pozsony do not apply to all five.
Metadata recovered from repository research/catalogue_harvest/decode/views*.jsonl.
DECODE images carry an archive-permission requirement for publication; images stay local and ignored.

## Prior work checked before cryptanalysis

- Tomokiyo, Cryptiana index https://cryptiana.web.fc2.com/code/crypto.htm: retrieved; no dedicated Beatrice entry found in the index. This does not establish absence throughout his publications.
- Berzeviczy, *Aragoniai Beatrix ... okiratok* (1914), https://archive.org/details/aragoniaibeatrix00berz, OCR saved as sources/berzeviczy1914.txt. No. LVI, pp. 81 onward, prints the 8 March 1486 letter, with explicit omissions of passages printed in *Matyas korabeli diplomacziai emlekek* III p. 67 and IV p. 367. Need compare to R1142 images before treating this as its decipherment.
- Vestigia public API accessible, but simple search does not search dates and quoted full-name search gave zero results. Search Beatrice returns 418 documents, 5 per page.
- User confirms an existing DECODE cookie is available. Located targets/bordeaux/decode/cookie.txt; use only as request header to de-crypt.org, never reproduce it in notes or logs.

## Completed source identification

See RESULT.md and readings/ for the record-by-record findings and earlier Italian texts. Eighteen images downloaded successfully. R1154 is 29 May 1505 and is plain Italian. R1143 has three written pages photographed five times, including views with slips moved. Four cipher letters have readings in MDE III (1877) and IV (1878); March 1486 editorial markers remain unexplained. Research write-up prepared in `.worktrees/beatrice1482/` on `codex/beatrice1482`. No manuscript images are included in the write-up.

## 14 Nov 2026: key rebuilt from the Vestigia cipher/clear pairs (Brice Dudout, Claude Opus 5.5)

Vestigia (https://www.vestigia.hu) publishes both letters with their period clear copies ("exemplum"): 1957 ↔ 1958
(R1140) and 1960 ↔ 1961 (R1141). Blind glyph transcriptions of both letters, a key rebuilt from R1140 only and one
pre-registered measurement on the whole of R1141 (648 signs): characters 0.900 against 0.290 for the best of 200 keys
shuffled within value classes. The alphabet is the one of matthias1482 (17 shared values; 9 = d and 2 = g here
against the figures in that key). R1141 has a cipher run the 1877 print leaves out, "Venetiani da sua offesa",
restored from the copy's margin and the key (readings/R1141_reading.md). Details: [`vestigia/README.md`](vestigia/README.md).

### Integration check (14 Nov 2026, PR #620)

- **Reproduction.** `vestigia/measure.py K_V.json R1141_V1960_transcription.txt ref_R1141_MDE.txt relabel_R1141`:
  648 signs, characters 0.900, precision 0.867, words 0.644; best of 200 within-class shuffled keys 0.290, mean
  0.166; pass. The fourth argument (the relabelling of the new shapes) is needed: without it the figure is 0.891.
  `train_key.py` on R1140 gives the values of `K_V.json`. SHA-256 of `PREREG.md` (3d7bc070...3229) and `K_V.json`
  (0ae0cdbe...32b5) match the README.
- **Second scorer.** A scorer written here (longest matching blocks instead of Levenshtein): K_V 0.901, 300
  shuffles of the single-letter values at most 0.346.
- **Order of events** (protocol, then key from R1140, then one measurement on R1141): by the contributor's record;
  one commit, the hashes prove the files are unchanged, not when they were written.
- **The key is seeded.** `train_key.py` aligns R1140 with a starting table (`SEED`) that already holds 9 = d and
  2 = g, so "33/33" and "10/10" are not independent counts. Re-run here with both removed from the seed: 2 = g
  10/10, 9 = d 29/33 (the other four are alignment slips onto *d* plus a neighbour). The values stand.
- **Images.** Vestigia's web images of 1960 (cipher) and 1961 (clear copy) were opened (not kept). 62 signs of
  R1141 compared with the transcription (line 2 *grande dispiacere*, the end of line 5 and line 6 *avari che per
  sparagnare ... lo ducato*): all agree. The margin of 1961 reads *et tale che non solamente havia tolto Venetiani
  da sua offesa ma li haria ridocti a carastia de defenderse*: the restored run is on the copy as stated.
- **Key state: partial.** Three shapes of R1141 have no value in `K_V.json` (ZIG 4 times, where the print has *x*;
  WEDGE twice; LAMBDAFLAG twice) and one sign is unread: 9 of 648 signs. Two values (round c = n, Λ = o) come from
  the matthias1482 key, not from R1140.
- **Outcome.** The text of both letters is still the printed decipherment of 1877 (method: read from existing
  decipherment). The key is a second part: key recovered based on plaintext from external sources (the period
  clear copy and the print), partial.
- **Prior art not checked.** Vestigia's records of 1960 and 1961 (R1141) list a later edition, "GUERRA 2010: 12"
  (the records were opened; the edition itself was not; the records of R1140 were not opened). Whether it already prints *Venetiani da sua offesa*
  from the clear copy is not checked: the run is new against the 1877 print only.
- **What the PR commits from Vestigia:** no image. Text only: the contributor's own shape transcriptions, reference
  lines taken from the 1877 print, and the quoted margin sentence of the clear copy. Vestigia states no licence;
  its documents are cited by number.

## Fold of matthias1482 (14 Nov 2026, round 15): one key, checked on the king's letter itself

**Question.** The key drawn up for R1156 on 19 Sept 2026 (`matthias1482/texts/key.md`) and the key rebuilt for the
queen's letters (`vestigia/K_V.json`) shared sixteen letter values and the sign for the King of Hungary, and
differed on d (2 there, 9 here), g (hooked L there, 2 here), e (5, 4, 9, ς there, one sign here) and the sign
for the Venetians (a looped & there, × with a small circle here). The matthias1482 folder had no sign-level
transcription, and its images were behind the DECODE login.

**Source found.** Vestigia publishes the letter with open images, as it does the queen's: document 2626
(the cipher original, b. 1622, 1, fasc. 2, no. 2a, DF 295613; four files) and document 2627 (a clear copy of the
time, no. 2b, DF 295614; three files), https://www.vestigia.hu/documents/2626 and /2627. Found through Vestigia's
search (`api/search?search=Hunyadi Mátyás levele Ercole`); no login, no bot check. The clear copy was not known to
this project before: DECODE's record and the earlier notes name only the original. No image is kept here (the
IIIF manifest of 2626 states CC BY-NC-SA 4.0; the document pages state nothing).

**What was done.** The cipher runs of 2626 were transcribed sign by sign from the web image with the clear copy
beside it (not blind): 69 runs, 409 signs, of which 10 are name signs and 2 are the large unread signs after *regina*
(`matthias1482/vestigia/R1156_V2626_transcription.txt`). The earlier estimate was "about 15 runs, roughly 330
signs". Labels are those of `vestigia/sign_inventory.md`. `matthias1482/vestigia/check_r1156.py` counts which sign
stands for each letter of the copy and decodes the letter with the queen's key.

| point | earlier key of R1156 | on the image of R1156 | queen's key (K_V) | result |
|---|---|---|---|---|
| d | 2 (*disposituros*, *diverti*) | a 9-form with a curled, open head in *subsidium*, *transeundi* (twice), *disposituros*, *diverti*, *confundere*; in *modum* (twice) the head is too small to tell. The figure 2 proper (as in *Mager*) is never d. 8 places | 9 = d | K_V holds; "2" was a label for the open 9 |
| g | hooked L | the figure 2 in *Mager* and *quingentos*; an L-form in *excogitare*, *congregabit* (twice) and where the sense wants *gentibus* | 2 = g | K_V holds on both places with 2; the L-form is a second sign for g (or the s-sign: the copy of the time reads *sentibus*) |
| e | 5, 4, 9, ς | three signs: the figure 5 (24 places in words of matching length), a hook with a detached dot at the upper left and a blob at the foot (10), and the 4-like sign with a long tail (7) | one sign, the 4-like ϟ | the 4-like sign is shared; 5 and the dotted hook are further signs for e that the queen's two letters do not use. The "9 = e" of the earlier key is the dotted hook, a different sign from the 9-form of d |
| Venetians | looped & | a cross with small circles at its right ends, three times (*terras Venetorum*, *confinia Venetorum*, *diverti Veneti*) | × with a small circle | the same sign (compared with line 5 of Vestigia 1960) |
| King of Hungary | q with a looped tail | barred G/q sign, twice | Ǥ | the same sign |

Decoding the 397 letter signs against the words of the clear copy (same script):

| key | letters of the copy recovered |
|---|---|
| K_V as it stands (built on the queen's letter of 31 May only) | 283 of 399 = 0.709 |
| K_V plus the signs only this letter has (5 and the dotted hook = e, crossed o = i, square bracket = s, reversed E = u/v) | 389 of 399 = 0.975 |
| the same with the earlier key's 9 = e and 2 = d (or 2 = i) | 379 of 399 = 0.950 |

The second and third rows differ only on the ten places that decide the question (eight d, two g): all ten go
to the queen's values. This is a check on a transcription made with the plaintext in view, and the extra signs
were given their values from this letter; it is not a held-out test and no controls were run.

**Verdict: the same key.** Every value of K_V that occurs in the king's letter reads it, and the two values the
keys disagreed on (9 = d, 2 = g) are confirmed on the king's letter itself. The differences that remain are signs
the king's secretary uses and the queen's does not, in about 1,500 signs of her two letters: two more signs for e,
one more for i (crossed o), one for u/v (reversed E), an L-form for g, and the name signs for King Ferdinand
(crossed square), the Duke of Ferrara (star) and the Emperor (triangle). Her letters in turn have signs his
Latin does not need (ll, ss, ff, z). Not excluded: that the queen's copy of the table was a shorter one. One
shape needs care: K_V gives "reversed capital E" to *ll*; on Vestigia 1960 that sign has its middle bar drawn out
to the left like an arrow, and the reversed E of the king's letter (u/v, 17 places) has not. They are taken as
two signs.

**Corrections to the earlier key of R1156** (`matthias1482/texts/key.md`, left as filed): d is the 9-form, not 2;
g is 2 (and an L-form); 9 = e is the dotted hook; ς and "4" are one sign, the 4-like ϟ of the queen's letters;
the looped & is the × with small circles; i = 2 rests on one small z-like sign in *mittere* (line 8) and is
dropped; + for o, t and e, ᑐ for d and m, ᒧ for l, ϲ for n and S for s do not occur in this transcription and
are dropped; x = H (*excogitare*) and u/v = 1 (*viam*, *subsidium*) are added, both as in K_V.

**What the clear copy (2627) adds to the reading of R1156.**
- *quingentos **electos** equites*: the word is in the cipher (run of seven signs at the head of line 9) and in the
  copy; the 1895 print and the first reading here lack it.
- *valent*, *Speramus cito nos res nostras ita disposituros ut meliori postea modo vos iuvare possemus*, and the
  closing sentence *Rex Hungarie scripsit Regi Ferdinando quomodo possent diverti Veneti et confundere eos et cum
  paucis pecuniis* as part of the letter: the copy has all three as the notes of 19 Sept read them. They were
  called corrections to Fraknói there; they are corrections to the print, and the decipherer of the time already
  had them.
- *pluribus gentibus*: the copy reads *sentibus*, which is what the signs spell with the s-sign; Fraknói printed
  *servis*. *gentibus* is by the sense and by the same L-form standing for g in three other places.
- *statim significet Regi Hungarie et illic faciet quod venient*: so the copy. The sign after *significet* is the
  king's sign; what stands after *faciet* is the ordinary abbreviation of *quod* in clear, not a code sign. The
  open point "faciet ꝗ venient" of the earlier notes is closed.
- More of the letter is in cipher than the first reading showed: *transituri*, *loca*, the Emperor's sign,
  *conflictamus*, *modum transeundi tutum*, *transire* (twice), *terras*, *scripsimus*, the signs for King
  Ferdinand and the Duke of Ferrara, *excogitare*, *mitti*. Reading and translation revised
  (`matthias1482/texts/R1156_reading.md`, `R1156_en.md`).
- The two large signs after *regina* (line 10) have nothing to match in the copy and stay unread.

**Number in the 1877 edition.** The earlier notes give R1156 as MDE III "no. 14", from Fraknói's reference
"Diplomatiai Emlékek. III. 14." Vestigia's records of 2626 and 2627 give "DEM: III, 11". No. 10 ends on p. 14 and
no. 12 begins on p. 16, so the letter is no. 11 and Fraknói's 14 is the page. The 1877 volume was not opened for
this letter.

**Credits.** The printed decipherments are Nagy and Nyáry's (MDE III, 1877) and Fraknói's (1895). The first
reading of R1156 from the image, its working key and the comparison with the print are the project's (19 Sept
2026). The queen's key, the sign transcriptions of R1140 and R1141, the held-out test and the two values now
confirmed (9 = d, 2 = g, which Brice Dudout proposed to re-check on R1156) are Brice Dudout's (PR #620, with AI
agents). The Vestigia pair 2626/2627, the sign transcription of R1156 and this check are the project's (14 Nov
2026).

## Remaining gaps

- R1156, the two large signs after *regina* (line 10) - blocker: open-codes; they occur once and the clear copy leaves them out
- R1156, single signs: the z-like sign in *mittere* (line 8), the l-sign for o in *modum* (line 13), two shapes for rr in *terras* (line 14), a PI-form for p in *scripsimus* (line 15), a blotted sign in *plures* and one in *pecuniis*, and the two strokes inside *congregabit* and *disposituros* - blocker: illegible; a 4096-px web image, the original was not seen
- R1156, whether the L-form in *gentibus*, *congregabit*, *excogitare* is a sign of its own for g or the s-sign - blocker: illegible; the hooked and the plain L are not separable on the web image, and the copy of the time read s once
- R1140 and R1141, three shapes of K_V without a value (ZIG, WEDGE, LAMBDAFLAG; 8 signs) and one unread sign - blocker: too-short
- whether the queen's table had the further signs of the king's letter (5 and the dotted hook for e, crossed o, reversed E, the name signs) - blocker: no-key-material; no key sheet is known, only the three letters
- Guerra 2010 no. 12 (R1141) not opened; the 1877 print of R1156 not opened (the letter is quoted from Fraknói 1895, so whether the 1877 text has *electos* is not known) - blocker: needs physical access; neither was found online in full

