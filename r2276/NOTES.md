# BnF fr. 20974 pp. 1-3 (DECODE R2276): a Nevers-Piles cipher letter from Reims on the chapter's postulation, 19 June [1589]

Read in part: 91.8% of 3,920 signs read as sense (measured), 88.9% in strict agreement with the key. Written up as `r2276`.


Catalogue item 194 ("Unknown sender (France?) to Duc de Guise?, 1 Jan 1556"). DECODE R2276: "Non-decrypted, 3 pp.,
unknown; graphic signs"; note: "3rd page looks upside down".

## What the document is

- Three pages of continuous cipher (no clear text), bound as pp. 1-3 of BnF fr. 20974 ("Clefs de la correspondance
  chiffrée de François, duc de Guise… (1556)", Gallica `btv1b9062131g`). Page 3 is bound upside down; the lower half
  of p. 3 is blank. Page 4 (Gallica f4) is the letter's blank verso with the 1556 key for "le général d'Albany"
  (Tomokiyo's no. 2) pasted onto its lower half. That pasted key is what dated the item "1556" and tied it to Guise.
  The letter is not in that key.
- The cipher is Tomokiyo's **Nevers-Piles** alphabet (cryptiana `nevers.htm`, from BnF fr. 3612 f. 9, not digitised):
  Tomokiyo, `guise.htm`: "In 2021, Norbert Biermann found that this can be read with the Nevers-Piles cipher"
  (private communication). No text of that reading was published anywhere we could find (web search 22 Sept 2026).
  So the identification is prior art. The transcription and reading here are new.
- Content (from the reading): the chapter of Reims and its **postulation** of a new archbishop, the grand archdeacon
  **Brulart**, the abbey of **Saint-Remi**, Rome and the pope, the vidame, the duc d'**Elbeuf**'s ransom
  (**cinquante mil escus**), **dix huict mil lansquenetz**, the Low Countries and the Duke of **Parma**. This is
  the League-era succession at Reims after the murder of Cardinal Louis de Guise (Dec. 1588), which ended with
  Cardinal Nicolas de Pellevé's appointment (10 May 1591). Date therefore c. 1589-91, not 1556. Jean de Piles, abbé
  d'Orbais (see `orbais/`), was Pellevé's man and the Nevers-Piles cipher's holder.

## Files

- `img/` (git-ignored): DECODE PNGs `p16170_P1.png`, `p16171_P2.png`, `p16172_P3.png`; Gallica `gf4.jpg`
  (the pasted 1556 key), `f4715_17.jpg` (fr. 4715 f. 2, same cipher with interlinear).
- `LABELS.md`: the ASCII label for each sign.
- `p1.txt`-`p3.txt`: first-pass transcription (superseded). `t1.txt`-`t3.txt`: second pass (page 1 by hand at 2x,
  pages 2-3 by two agents at 1.5-3x). Page 2 labels `W U q %`, page 3 `@`, all pages `Y` = ẋ.
- `key.json`: value set per label after hard-EM (`hardem.py`).
- Decoders: `beam.py` (letter 5-gram, polyphonic), `beams.py` (spaced), `wdec.py` (word Viterbi with a 30k-word
  lexicon and bigrams from `lang/corpora` fr-henri4 + fr-1520s-diplomatic + fr-rome-1600s), `hardem.py`.
- `check.py t1.txt,t2.txt,t3.txt <reading>`: aligns a reading to the signs and measures the fraction read.
- Readings: `read1.txt` (p. 1 ll. 1-18), `read13.txt` (p. 1 ll. 19-40, p. 3), `read2.txt` (p. 2).
- `steps.md`: log of solution steps for `profile.json`.

## State on 23 Sept 2026 (goal cleared; work in progress)

- Whole-letter reading: `reading.txt` (93 lines, all three pages). Measured with `KEY=key_v7.json python measure.py
  reading.txt`: **strict 3484/3920 = 88.9%** (sign agrees with the key), **sense 3598/3920 = 91.8%** (sign inside a real
  French word, slips read through). 107 `?` words remain. Words marked `*` were read under the half-the-signs rule
  (grade C).
- The letter: written from Reims "du dix neufiesme de iuin" [1589: the dean Frison is "maintenant a Rome", and orbais/ (Pellevé's secretary, Rome, 23 Aug 1589) says "le doien" will be dispatched in two days; after Cardinal Louis de Guise's death, Dec.
  1588, and Elbeuf's capture]. While the writer was still in Rome, someone "praticqua ici au chapitre une election ou
  postulation de deux personages et deux chanoines, l'ung le grand archidiacre Brulart qui i consentit en plourant … l'aultre
  esleu son postule est le doien Frison qui est maintenant a Rome … porteurs de l'acte de postulation". It names the
  Cardinal de Lorraine, Cardinal de Pellevé, the commandeur de Diou, Cardinal Allen ("alanus"), "Mr de Maine", the
  congregation in Rome, Brulart contenting himself with the revenue of the archbishopric and the abbey of Saint-Remi,
  the vidame and Robilard "mon hoste", Provins, 18,000 lansquenets and 8,000 reiters (one army for the Low Countries to
  hinder Parma), the Elbeuf ransom agreed at 50,000 écus, 150,000 écus the town excuses itself from contributing.
  Page 1 opens on a letter (code M = lettre) to the Pope presented in the chapter assembly, the need for a resident
  prelate, "plustost que ung estranger", and a letter to be carried to Rome.
- Sender: probably Jean de Piles, abbé d'Orbais ("pendant que iestoie encores a Rome"; Orbais is near Reims; the cipher
  is the Nevers-Piles one). Addressee: unknown; a patron who "l'a eu agreable" (approved the postulation), distinct from
  Mayenne.
- Key: `key_v7.json` (reading key); `key_v8.json` adds the fr. 4715 f. 2 values (⊞ = parle; ẋ = vous or null, never i;
  swash g = que; ꝺ mostly t in that hand; b also "cest"). Codes found here: `3Z` cardinal, `bb` leur, `3` le/du/d,
  `e`/`C` pour, `O` faire, `I` ie, `Y` vous, `Ml` lettre, `_` null, `^` s.
- fr. 4715 f. 2 fully aligned: `fr4715_aligned.txt`, `fr4715_values.json` (~1,050 pairs). Also usable for `orbais/`.

## Next step (if the work is resumed)

Re-read the 107 `?` words with key_v8 (the fr. 4715 values: in particular every `Y` read as i must be re-checked as
vous/null, and `N` = parle at t1.21 "ouy parle[r]" and t1.36). Then the writeup (site crops ready in img/snip_*.jpg).
The folder was renamed from `guise1556` (the wrong catalogue date) to `r2276` at write-up. `lex.json` / `bigr.json`
(word lists for wdec.py) are git-ignored; rebuild them from `lang/corpora` fr-henri4, fr-1520s-diplomatic and
fr-rome-1600s (word counts >= 2; bigrams >= 2). Page images stay in the original session's img/ (git-ignored).

## Remaining gaps
- torn right edge of p. 1 ll. 1-4 and 16-31, and the left margin of p. 2 ll. 1-2, 15-28, 39-40 (about 700 px of text) - blocker: illegible; paper lost, no other copy of the letter
- ink blot on p. 3 l. 2 (`d F z v - v m H z`) and the stained start of p. 3 l. 3 - blocker: illegible; signs under the stain cannot be told apart on the only image
- about 25 single-sign `?` in running text (e.g. t1.9 `u`, t1.11 `t`, t1.18 `3`, t1.35 `R`, t1.38 `Y`/`P`, t2.3 `x`/`m`, t2.4 `u`, t2.32 `3`, t2.36 `D`, t3.4 `Z`, t3.7 `3`) - blocker: too-short; one sign each, the sentence reads without it, no value can be proved
- the boxed cross ⊞ (`N`) at t1.21 and t1.36 - blocker: open-codes; = "parle" in BnF fr. 4715 f. 2, which fits t1.21 ("ouy parler") but not t1.36 ("de ? Bardin", probably a title); two occurrences
- about 80 unread words of two or more signs (listed as `?` in reading.txt; worst lines t1.16, t1.22-26, t1.33, t1.38-39, t2.2-3, t2.10, t2.13-16, t2.19, t2.21, t2.39, t3.1, t3.5, t3.9) - blocker: open-codes; no French word fits both the signs and the sentence after six reading rounds, a full alignment of the sibling fr. 4715 f. 2 and candidate search over a 30k-word lexicon; several contain signs with no attested value (Z with overline, 8 with superscript t, U, W, q, k)

## Escalation
- [x] siblings: BnF fr. 4715 f. 2 (Cardinal de Guise to Nevers, 1586, same cipher, interlinear decipherment) fully aligned, ~1,050 sign=value pairs (fr4715_aligned.txt); orbais/ (fr. 3413 no. 62, same cipher) read; fr. 20974 f4 is the letter's own verso with a different (1556) key pasted on; fr. 3612 (Piles's letters and Tomokiyo's key source) is not digitised
- [x] clear-pages: none; the letter is cipher throughout and p. 4 carries a key of another correspondence
- [x] known-keys: Tomokiyo's Nevers-Piles table (fits, partial), Nevers-Pelleve and Nevers-Guise tables (orbais/: do not fit), the 1556 Albany key on p. 4 (does not fit)
- [x] print: Tomokiyo guise.htm and unsolved.htm (Biermann 2021 identification, no text); web search for the Reims postulation, Brulart, Frison, Elbeuf ransom: no edition of the letter found
- [x] key-rebuild: hard-EM over a word Viterbi decoder (hardem.py), value counts from aligned readings (keyest.py), codes rebuilt from context (cardinal, leur, pour, faire, ie, vous, lettre, le/du) and from fr. 4715 (parle); key_v2 to key_v8
- [x] retry: every `?` word re-run in two targeted rounds with the extended key and candidate search (seg.py, cand.py); 60 -> 57 on pp. 1 and 3, 61 -> 53 on p. 2
