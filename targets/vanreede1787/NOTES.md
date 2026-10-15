# Van Reede's despatches from Berlin in the Grand Chiffre, 1787–1788 (DECODE R1026, R1027)

Status: read in part (R1026, R1027 read with the Grand Chiffre R1024; open codes and transcription misreads remain).

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

## Remaining gaps
- R1026/R1027 groups 2637, 2800, 3660, 1250, 331, 3160, 3153, 2751, 50 and damaged groups - blocker: open-codes; not in the 1782 R1024 key; 2637/2800/3660 recur, probably names
- R1026/R1027 garbled passages from DECODE digit misreads - blocker: not-attempted; NOTES say a fresh transcription from the images would clear them; not done

## Escalation
- [x] siblings: R1028 and R1029 opened as controls (R1028 decodes word for word); R1057 noted
- [ ] clear-pages: not done — check the R1026/R1027 images for interlinear glosses beyond the 275J one and for a clear copy
- [x] known-keys: R1024 Grand Chiffre fits R1026/R1027
- [ ] print: not done — Colenbrander Gedenkstukken and Vreede, Van de Spiegel en zijne tijdgenooten, for these despatches
- [ ] key-rebuild: not done — bracket 2637/2800/3660 alphabetically inside the R1024 code order and by LM context
- [ ] retry: not done — re-transcribe the digits from the images and rerun resolve_j.py
