# Van Reede's despatches from Berlin in the Grand Chiffre, 1787–1788 (DECODE R1026, R1027)

Status: read (re-read 23 Oct 2026, b24: R1026 and R1027 read on the figures with the Grand Chiffre R1024; DECODE's J+ is the writer's hooked 1, the key's untranscribed blocks are nulls). Was: not read (reading audit, 22 Oct 2026: decoded, not read); before that read in part.

**23 Oct 2026, re-read (REREAD_BRIEF, b24).** Both despatches **read in full** (`R1026_reading.md`, `R1027_reading.md`,
English `*_en.md`; log `R1026-R1027_reread_log.md`). No contemporary decipherment or print exists (DECODE records and
the Van de Spiegel prints checked). The garble of 21 Sept came from `resolve_j.py`, which picked a digit per `J+` group
with a language model: the `J+` sign is one glyph, the writer's 1 with a hooked foot, and J=1 gives a fitting key word
at all 101 places. The key's DECODE transcription leaves out six blocks, which on the key images are **"Nonvaleurs"
(nulls)**: 1-50, 331-370, 1201-1250, 2751-2800, 3131-3160, 3621-3660, so the "open codes" 1250, 331, 2800, 3160, 3660,
3153, 2751, 50, 1201 are padding; 2637 is "cependant" (mis-numbered 3637); four word slips read on the key images (54
est, 2142 paroit, 2143 paroitre, 4910 que). Eight labels corrected on the letter images. The bars above and below
groups are inflection signs (a bar above cuts letters, below adds the ending). Body scores 0.735 (R1026) and 0.867
(R1027) clean sentences. What R1026 says: Hertzberg motivated his own view in the report; article seven struck out as
disagreeable to England at Finckenstein's request; the treaty made temporary, twenty years; the conference agreed to
promise aid against a European attack without naming the overseas possessions. R1027: Ségur and Cobenzl dismayed that
the Empress refused the triple alliance; Keller (Prussian envoy) waits on Vienna and London.
Helpers: `research/reading_audit/b24_vr_*.py`, `reread_b24_vanreede.py`.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **R1026 and R1027 are
decoded, not read**. The Grand Chiffre R1024 fits (the R1028 control decodes word for word), but the decodes of these
two letters have garbled runs from DECODE's digit misreads and open codes in most sentences: the gist follows (the
alliance, the King's refusal to guarantee the overseas possessions), the sentences do not. Class now not read, method
not solved; 447/471 groups with a value is withdrawn as a reading figure.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. This entry joined R1026/R1027
(William V's 1782 Grand Chiffre) with R1893 (1793), which is in a different marked three-digit code. R1893 is a
different cipher, with its own page ([`targets/vanreede1793/`](../vanreede1793/), docs/vanreede1793.html); its files
(`ciphertext_R1893.txt`, `analyze_1893.py` and the key-bundle scripts) moved there. The DECODE downloads (`decode/`,
git-ignored, main checkout) and `fetch_decode.py` stay here.

Target: DECODE R1026, R1027 and R1893, seven pages described as numerical
nomenclator ciphertexts sent by Arend Willem van Reede from Berlin to Laurens
Pieter van de Spiegel, Hendrik Fagel Jr and the Secret Committee of the States
General (29 Dec. 1787–24 Mar. 1793). DECODE suggests the code is likely the
“Grand Chiffre” of Stadholder William V.

The repository's existing authorized DECODE cookie is used only as a request
header to de-crypt.org by `fetch_decode.py`; it is never reproduced here.

## Work log

- 2026-09-20: target opened; authenticated acquisition begun. No prior reading
  or key has yet been established.
- 2026-09-21: **R1026 and R1027 read with DECODE key R1024** (the 1782 "Grand Chiffre"
  of William V, KHA A29 inv. 301, French, 1–5000). Control first: the R1028 undated
  Van Reede despatch (DECODE gives its plaintext) decodes word for word with R1024
  (`la reponse à donner au Roi à la communication que S.M. vient de faire...`), so the
  key is the right one. The earlier garble came from the transcription, not the key:
  DECODE's `J+` is a catch-all for a sign the transcriber could not place, and it does
  not stand for one digit (275J = 2750 *dites*, matching the interlinear gloss, but
  JJ8J = 1181 *le Roi*, 375J = 3751 *dix* in "à dix heures"). `resolve_j.py` tries every
  digit for each J+ and picks the reading with a 6-gram French model built on
  targets/hellen1752/corpus_fr.txt (beam 40). 105 J+ groups resolved this way (79 + 26).
  Output: `reading_R1026.txt`, `reading_R1027.txt`, `resolved_R*.txt`.

## Reading (gist)

**R1026, Berlin 29 Dec. 1787, to Van de Spiegel.** The day before yesterday the two
ministers (Finckenstein and Hertzberg) put to the King the project of the alliance as
Van de Spiegel had sent it. There is to be a conference this morning at ten between the
King and his two ministers; Van Reede hopes for no change. "The only point so far is
that the King said he could not guarantee our possessions overseas"; Van Reede did not
press it, only that if they were attacked in Europe the King would furnish help in
money or subsistence. Mentions the Prince of Anhalt-Schaumburg, England, Finckenstein
and Hertzberg, the treaty. After the clear passage (the conference has been held): the
article is kept without the words *possessions outre-mer*, saying simply that if the
Republic were attacked by a European power the King would furnish the aid. (Cf. the
Prusso-Dutch defensive treaty of 15 Apr. 1788.)

**R1027, Berlin 4 Mar. 1788.** News from Russia; the Russian ministers are anxious
about the triple alliance; the Russian envoy has had no answer yet and does not expect
one until the Empress has the one she awaits from Vienna to her demand; the Emperor's
declaration of war on Turkey (Joseph II, Feb. 1788); a courier sent to London, followed
by two others, before (Prussia) explains itself on the proposals.

## What stays open

- Some passages remain garbled where the DECODE transcription misreads plain digits
  (not only J+): e.g. "comme ils mauvais oyent A differer", "Monsieur de L L nr" (the
  Russian envoy, probably Alopeus). A fresh transcription from better images would
  clear them.
- Unread groups (not in R1024 or damaged): R1026 1250, 21423068 (two run-together
  groups), 4 4 3 8 (corrected above to 4433), 331, 308J9, 2637, 2800, 3160; R1027 3660
  (x2), 2800, 3J089, 2637, 1J1021, 50, 3153, 2751. 2637/2800/3660 recur and are
  probably names absent from the 1782 key.
- R1893 (24 Mar. 1793, to the Secret Committee, Dutch) is a different system and now its
  own entry (vanreede1793, attempted, not solved).
- Follow-up: catalogue 217 (DECODE R1057, Van Reede to William V, 4 Feb 1792) is
  also Grand Chiffre but written as unseparated digit runs with an interlinear
  decipherment; not attempted here.

Write-up: [docs/vanreede1787.html](../../docs/vanreede1787.html).

- 2026-10-14: split; `fraction_read` on this key's letters only: 447/471 (94.9 %).

## R1893 and the 1789-92 code
- 25 Oct 2026: R1893 tested against Van Reede's 1789-92 marked code to Wilhelmina (target reede1789, rebuilt from
  KHA A32-545-547 interlinear glosses): coverage at chance level, French values in a Dutch letter, and R1893's marks
  sit above the digits where the 1789-92 code underlines them. Not R1893's code. R1893's DECODE image is stored
  upside down; turned, it is headed "Wel Edele Gestrenge Heer", 24 Mar 1793.

## Read share over cipher words only (16 Nov 2026)

README Conventions (16 Nov 2026): the read share counts the words written in cipher only. The readings do not mark
the clear, but the decodes do (`[clear: ...]` lines in `R1026_decode_b24.txt`, `R1027_decode_b24.txt`): in R1026 the
head, the paragraph "Depuis que ceci a été chiffré ... diner à sa table" and the close are clear; in R1027 the head and
the close. The cipher words are the remaining paragraphs of the readings.

- R1026: 0.986 (whole letter) -> **0.990** (283 of 286 cipher words; holes [?soit], [?fournit], [?énonçoit]). The
  four faint [?word]s are in the clear passage and drop out.
- [?énonçoit] (group 163 *ois* where the sense wants 164 *oit*, a one-digit difference under the surviving Grand
  Chiffre) is a candidate for the README one-digit-slip rule, pending an image check that the slip is the writer's;
  until then it stays a hole (with it read, R1026 would be 284 of 286).
- R1027: 0.994 (whole letter) -> **0.992** (122 of 123; hole [?decidement]).
- Class unchanged: **read** (both documents). A code group read as several words (*Monsieur de Herzberg*) is counted
  by its words; as one word the shares are the same to three places. Whole letter, clear included, not the measure:
  0.986 and 0.994.

## Remaining gaps
- R1026 [?soit], [?fournit], [?énonçoit] and R1027 [?decidement]: groups and bar marks spell a slip - blocker: no-key-material; the key has no instruction for the bar marks
- R1026 clear passage, four faint words ('je [?vois] le plus [?estimé] d'[?ici]', 'le jour [?la]') - blocker: illegible; 1240-px DECODE image
- closed 23 Oct 2026 (b24): R1026 and R1027 decoded, not read (read in full); the open codes 2637 (= cependant, key mis-numbered) and 1250, 331, 2800, 3160, 3660, 3153, 2751, 50 (nulls, 'Nonvaleurs'); the garbled passages (J+ = hooked 1, labels corrected on the images)

## Escalation
- [x] siblings: R1028 and R1029 opened as controls (R1028 decodes word for word); R1057 noted
- [x] clear-pages: 23 Oct 2026 — images and DECODE records checked: only the 'dites' gloss over the first (null) group; no clear copy or decipherment
- [x] known-keys: R1024 Grand Chiffre fits R1026/R1027
- [x] print: 23 Oct 2026 — Brieven en negotiatien i-iii and Vreede's Van de Spiegel grepped: not printed; Colenbrander not searched (letters read on the figures)
- [x] key-rebuild: 23 Oct 2026 — not needed: 2637 is in the key (mis-numbered 3637), 2800/3660 etc. are nulls; four key slips read on the key images
- [x] retry: 23 Oct 2026 — digits re-read on the images (J+ = hooked 1, eight labels corrected); resolve_j.py's per-group digit choice withdrawn
