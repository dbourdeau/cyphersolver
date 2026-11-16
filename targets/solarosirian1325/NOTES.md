# solarosirian1325: Enigmatic Book of the Solar-Osirian Unity (Tutankhamun's second shrine; tomb of Ramesses IX)

**Status: read in part (README read rule: under 95 % of words read as sense), and only in a small part; on the
schema's sentence test our own output is "decoded, not read". The texts were read and published long before us
(Darnell 2004; Darnell & Darnell 2018). Our one pre-registered measurement FAILED its threshold.**

## What this is (and what it is not)

**This is not a cipher in the usual sense, and it is not classical hieroglyphic writing either.** It is Egyptian
*enigmatic* (often called *cryptographic*) writing: a learned sign-substitution convention used by New Kingdom
scribes for some netherworld books. The language underneath is ordinary Egyptian. There is no secret key held by a
sender and a receiver; why the scribes wrote this way is a question for Egyptologists, and we make no claim about it.

How it works, as far as this project saw it: most signs keep their ordinary hieroglyphic value; a minority are
replaced by other signs under scribal rules. The rules we met are acrophony (the sign of a word stands for that
word's first consonant, e.g. "hills", *ḫꜣst*, for *ḫ*), substitution of look-alike signs, and rare spellings. On the
Ramesses IX line we counted about one sign in four substituted (session C11).

Why it is in a cipher catalogue anyway: it is a sign-for-sign substitution layer over a known language, so the
catalogue's tools apply (a substitution table, held-out measurement, permutation controls). How it differs from a
cipher: the "key" is a shared scribal convention, not a secret; it is partial (most signs are plain); it is
homophonic and not fully systematic (one value can have several signs, and the choice varies between monuments and
even between registers); and there is no clear text to recover, only a reading that Egyptologists already publish.

### Not every plate is the same kind of writing

The monuments mix ordinary and enigmatic texts. We only measured the enigmatic ones.

| Plate / zone | Kind of writing | Used here |
|---|---|---|
| Shrine 2, Piankoff pl. IV (right side) and pl. II (left side): legends and column texts | enigmatic | learning block (pl. IV, 17-column text) and tests |
| Shrine 2, Piankoff pl. III (back): Book of the Dead chapters | ordinary hieroglyphs | no |
| Ramesses IX (KV 6), third corridor, right wall: register 2 line and snake legends; register 3 annotation columns (Darnell 1–24) and legends; right section, scene 1, five-column annotation | enigmatic | tests and the C13 measurement |
| Same wall: register 3 annotation columns Darnell 25–49, the line above register 3, the legends of right section scene 2, the band above the right section (Guilmant pl. LXXVIII–LXXIX) | ordinary hieroglyphs (Darnell describes the band as written mainly in normal orthography) | no |

Even inside the enigmatic zones, ordinary signs seem to be the majority: on the one Ramesses IX line we counted
(C11), about three signs in four kept their ordinary value. We did not count this elsewhere.

## Result

Earlier sessions (C01–C12, October 2026) built a substitution table from an exposed block (shrine pl. IV, 17-column
text, aligned on Piankoff's published reading) and tried it on other passages of the shrine and of Ramesses IX. Those
sessions were exploratory: some were blind and frozen before comparison, some were not (C07 knew Darnell's general
translation; C05 and C08–C09 were re-readings with known values in context). We do not use them as evidence of
success here.

The only decisive test is **C13 (16 Nov 2026)**:

- **Frozen before reading:** protocol, table v5 (learned on the shrine and Ramesses IX in C03–C12), and the
  measuring script, each frozen by SHA-256. One addendum, also frozen before transcription, added zone F.
- **Held-out portion:** 428 signs no session had read (exposure declared: C12 had described four shapes of legends
  2–6, without values; C03 had seen the openings of the pl. II legends in Piankoff's transliteration). Zone F was
  added by the addendum after the table was frozen, chosen from a thumbnail, before any transcription: 269 from Ramesses IX (Guilmant pl. LXXXI legends 2–9 and 48–58,
  pl. LXXX legends 15–21, pl. LXXVII cols. 1–5) and 159 from the shrine (pl. II, lower register).
- **Reference:** the value of each sign in the published reading, aligned after our blind reading was frozen, from
  Darnell & Darnell 2018, by a separate model run (Claude Opus 5.5 via the API) that did not see the table. It is
  the same model family that built the table, and it knows Egyptian; this is a limit of the reference, not an
  independent check.
- **Measure:** M = share of reference signs with a phonetic value (or the plural strokes) whose value the table
  predicts. Pass bar, fixed in advance: M ≥ 0.70 **and** M ≥ best of 200 permuted tables + 0.30.

| | |
|---|---|
| M | **27/65 = 0.415** |
| 200 permuted tables | mean 0.018, best 0.154 |
| Bar | 0.70 and best + 0.30 = 0.454 |
| Verdict | **FAILED** (0.415 < 0.70; margin over best control 0.26 < 0.30) |

The table beats all 200 permuted controls (27 right against a mean of about 1.2; no control above 10/65; p < 0.005
with 200 permutations), but it does not read the new portion to the standard we set. Secondary figures, which played no part in the verdict:

- substitution entries of the table: 18/26 = 0.69 right; ordinary values: 9/39 = 0.23;
- Ramesses IX zones alone: 27/58 = 0.466; shrine zone: 0/7.

What the secondary figures suggest, without decision value (the split was not pre-registered): the substitution
part of the convention learned on earlier passages carries over to a passage never read before better than the
ordinary-value part does, as our table holds it.

### Reading (Daniel Bourdeau's read rule)

Classed after comparison with the publication. Units are the labels and column groups of the portion (37 units):

| Class | Units | Which |
|---|---|---|
| sure (read from the table and the shapes, confirmed) | 1 | *ḫpr* (Khepri), Ramesses IX |
| probable (read from the table, consistent with the publication, at least one sign uncertain) | 3 | *ḫprw* "manifestations"; *ḥr* "face" (in "Evil of Face", *ḏw* restored); *Rʿ … nb* "Re … lord" |
| restored (known only from the publication) | 12 | e.g. the five snake legends ("One Who Is Shot" in Darnell & Darnell 2018) |
| unresolved (neither read nor restored) | 21 | including all 6 shrine units |

Read by sense: 4 of 37 units, about 11 %, far below 95 %: **read in part**, and only in a small part. One blind
prediction came true at the level of structure: we predicted that snake legends 3–7 carry one repeated name, and they
do; but the word itself was restored from the publication, not read from the table. Any translation quoted is
Darnell & Darnell's.

### Reading review

No `reading_review` grade is recorded, and no `outcome.texts` entry. The schema's grades (A, B) are for decryptions
that read as coherent sentences. Ours does not: on the repository's own definitions our table-only output is
"decoded, not read", and the coherent text of these monuments is the published one, which is not ours to reprint.
The review of the C13 reading against the unit sheet (fiche) was done by Claude (Opus 5.5), which is **not
independent of the contributor's project**; it found the counts above and saw no basis for grade B. Brice Dudout has
not graded it (he does not read hieroglyphs). The outcome is therefore recorded as `already solved` (by Darnell) with
method `not solved` (by us), as for other targets where the project's own attempt did not obtain the text.

## Limits

- **Poor reference.** 85 % of the portion's signs (351 of 428) have no value in the reference, and 12 more are
  determinatives. Darnell & Darnell 2018 gives an English translation without transliteration, so most signs could not be aligned.
  The denominator (65) is small and leans toward short labels. Darnell 2004 (OBO 198), the sign-by-sign edition, was
  **not consulted**: we found no copy we could open.
- **Misaligned reference in zone F.** The reference run aligned zone F with the register 3 annotation; F is in fact
  the enigmatic annotation of the right section, scene 1. Part of its values for F are therefore wrong. We did not
  re-run it: the protocol allowed two model runs and both were used.
- **Missing values found after the measure.** Four shape classes had no value in the frozen table: a knob sign = *p*
  (5 cases, in *pn*), a slanted flagpole = *nṯr*, an inverted hill sign = *ḏw*, and V6 = *š* by acrophony (the
  table had the biliteral *šs*). A coding mismatch between two forms of the ayin (ꜥ / ʿ) would raise M to 29/65 =
  0.446 if fixed. Both are declared after the fact and do not change the verdict.
- **Shrine zone unreadable.** The only copy of the shrine plates we used gives about 15 px per sign. Both
  transcription passes were guesses there; no reading is claimed for the shrine part (0/7).
- **Transcription by models, not by a person.** Sign shapes were transcribed by Claude models from the plates: a Claude
  Opus 5.5 sub-agent, and a second pass by Claude Opus 5.5 through the API, arbitrated on the image by the
  sub-agent. The two passes are not independent in the way two human epigraphers would be. Fourteen disputed shapes
  were put on a blind shape-choice sheet for Brice Dudout; it has not been answered. No Egyptologist checked the
  transcription. Earlier sessions: Claude Opus (C01–C04, C06–C07, C10–C12), Claude Fable 5.1 (C05 re-reading, same
  session, partly dependent), and Codex (C08–C09 re-readings, as recorded in the project log). The C13 API runs cost
  1.19 USD.
- **Burnt portions.** Every passage measured or read in C03–C13 is spent and cannot be used for a new test of this
  table or its successors.
- **No follow-up measurement.** A table v6 (with the four values above) was frozen in C14, but no unused enigmatic
  portion of 300 signs remains on the Ramesses IX wall in Guilmant's plates: the only unread text there (pl.
  LXXVIII–LXXIX, about 120 signs) is in ordinary hieroglyphs. C14 therefore made no measurement.
- **Plate number corrected.** Zone F is Guilmant **pl. LXXVII** (PDF page 86), not pl. LXXVI as the frozen C13 files
  say; the frozen files are left unchanged.
- **What would settle it:** Darnell 2004 (OBO 198) as a sign-by-sign reference; the Ramesses VI version of the same
  book (KV 9, ceiling of corridor G; Piankoff & Rambova 1954, pl. 179–182) as fresh, unread material; and better
  photographs of the shrine (Harry Burton's photographs at the Griffith Institute, in high resolution).

## Credits

This work builds on, and checks itself against, published Egyptology. It does not replace it.

- **John Coleman Darnell**, *The Enigmatic Netherworld Books of the Solar-Osirian Unity: Cryptographic Compositions in
  the Tombs of Tutankhamun, Ramesses VI and Ramesses IX*, OBO 198 (Fribourg / Göttingen 2004): the scholarly edition
  and reading of these texts. Credited as the prior solution; not consulted by us (see Limits).
- **John Coleman Darnell and Colleen Manassa Darnell**, *The Ancient Egyptian Netherworld Books*, Writings from the
  Ancient World 39 (SBL Press 2018), ch. 7: the translation our reference was aligned from, and the reading we
  checked our results against.
- **Alexandre Piankoff**, *Les chapelles de Tout-Ankh-Amon*, MIFAO 72 (IFAO 1951–1952): the plates of the shrine
  (fasc. 2, line drawings by IFAO draughtsmen) and his transliterations (fasc. 1), used to align the learning block.
- **Félix Guilmant**, *Le tombeau de Ramsès IX*, MIFAO 15 (IFAO 1907): the line drawings of the Ramesses IX wall,
  from which the held-out portion was transcribed.
- **Étienne Drioton**, "La cryptographie de la chapelle de Toutânkhamon", *JEA* 35 (1949): an early published study
  of the shrine's cryptography. Credited as prior work; not opened by this project.
- Not consulted, named only as further literature: A. Piankoff with N. Rambova (ed.), *The Shrines of Tut-Ankh-Amon*
  (1955) and *The Tomb of Ramesses VI* (1954); work on the netherworld books and on enigmatic writing by Erik
  Hornung, Friedrich Abitz and Joshua Roberson. Nothing here depends on them.
- **Contributor:** Brice Dudout, who brought the target and set the protocol rules (pre-registration frozen by
  SHA-256, one held-out measurement, thresholds fixed in advance). He does not read hieroglyphs. The transcription,
  table, measurement and reading were done by Claude agents (Claude Opus 5.5; earlier Claude Opus, Claude Fable 5.1,
  and Codex, see Limits).

## Images and rights

No image, crop or derivative of any plate is in this repository. The Piankoff plates are IFAO publications, in
copyright until 2036; we used them for private study only. The Guilmant volume is on archive.org (`MIFAO15`); we have
not checked its reuse status, so no crop is included either. Darnell & Darnell 2018 is © the authors and SBL Press;
only a few words are quoted. Our working files (pre-registration, frozen table, transcription, measurement, unit
sheet) are kept outside the repository and are available on request.
