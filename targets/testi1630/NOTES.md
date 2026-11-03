# 1567 Francesco I d'Este / Fulvio Testi to Ottavio Bolognesi, 1630-1636: read in part

Status: read in part (3 Nov 2026). Of the 13 letters in entry 1567, 7 are read, c. 13r is read in part (8 lines), 5 are
unread. "Read" means the cipher of that letter. cc. 20 rests on a one-word margin. cc. 73-74 is read, provisional. The key
was got from a later clear copy, c. 22, not by cryptanalysis. Prior art is open: we do not claim that any of this is new.

Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents viewing the images.
No human palaeographer has checked it.

Entry 1567 has 13 letters. Seven in Lettera T (1630) were opened first. Six in Lettera F (1634-1647) were located later;
one of them, cc. 73-74, falls to the same key. The full clear text is given for the letters marked read, but it is a first
transcription.

| Document | Date | Cipher signs | Job | Words | A sense | B no slips | C no restored letter | Status |
|---|---|---|---|---|---|---|---|---|
| c. 7r | 7 Feb 1630 | 546 | no decipherment in the file | 108 | 107 (99.1%) | 107 (99.1%) | 104 (96.3%) | read |
| cc. 9r-9v | 15 Feb 1630 | 1275 | no decipherment in the file | 252 | 251 (99.6%) | 250 (99.2%) | 245 (97.2%) | read |
| c. 11r | 15 Feb 1630 | 287 | no decipherment in the file | 62 | 62 (100%) | 61 (98.4%) | 61 (98.4%) | read |
| cc. 16r-16v | 22 Feb 1630 | 1056 | no decipherment in the file | 211 | 210 (99.5%) | 209 (99.1%) | 197 (93.4%) | read |
| cc. 20r-20v | 1 Mar 1630 | 287 | no decipherment in the file | 50 | 50 (100%) | 48 (96.0%) | 42 (84.0%) | read, one-word margin |
| c. 23r | 14 Mar 1630 | 404 | transcription job, c. 22 covers it | 68 | 68 (100%) | 68 (100%) | 68 (100%) | read |
| c. 13r, 8 lines | 22 Feb 1630 | 287 + 2 lost | transcription job, c. 15 covers it | 58 | 58 (100%) | 58 (100%) | 55 (94.8%) | read in part |
| cc. 73r-74r | 2 Feb 1636 | 716 | no decipherment in the file | 154 | 153 (99.4%) | 147 (95.5%) | 136 (88.3%) | read, provisional, no margin |

Words are counted in the ciphered passages only, with elided forms split and the editor's own labels removed.
`scripts/readings_final.py` prints these counts.

- A: words reading as sense, doubtful words out.
- B: A, also without writer's slips and changed readings (no[n], circo[s]tanze, confiden[t]i, qualco). Lost or blotted signs
  stay in. So do the closed a and open c, a shape variant seen in several letters, and a single letter for a double.
- C: A without any word holding a restored or changed letter.

"Read" rests on B, not on A. The 95% rule asks for words reading as sense, and a marked hole does not stop a word reading,
but the rule means little if every slip can be corrected and then counted. On B, cc. 20 needs 48 of 50 and has 48. cc. 73-74
needs 147 of 154 and has 147. One word less in either falls under 95%. On C, cc. 16, cc. 20 and cc. 73-74 are below 95%, and
Dan may prefer to mark those three "read in part".

c. 7r stands at 108 words, not the 107 of the final check, because the final pass found a dropped word on the page (below).

Sense settles these calls, so they are not independent evidence. All 117 places where the key-free reader took n for h stay n:
the shapes have the n form or do not decide. In the H-like hand tailed t and g are close. In some places a is written closed
like D, or c open like A. See `key.tsv`.

Not read: the rest of c. 13r, c. 13v, the cipher of c. 14r (c. 15 covers them); c. 53, c. 54, c. 72, c. 4, cc. 5-6 of Lettera F.

## What the documents are

Ducal letters of Francesco I d'Este from Modena. The 1630 letters are countersigned Don Fulvio Testi. They mix clear Italian
with cipher inside the same sentences, and the most sensitive words are in cipher. The addressee stands at the foot only as
Bolognesi (c. 7r, c. 9r, c. 11r, c. 16r, and c. 73r for 1636). "At Vienna" rests on c. 22 alone, which is a later hand. The
manifests title cc. 7-24 and cc. 73-74 to Bolognesi; the catalogue marks cc. 13-15 "Destinatario incerto".

The Reggio Emilia State Archive inventory, seen only as a search-engine extract, describes papers of Ottavio di Stefano
Bolognesi (1580-1646) on affairs handled for the princes of Correggio and the dukes of Mirandola, Savoy and Modena:
https://archiviodistatoreggioemilia.beniculturali.it/getFile.php?id=810 . That explains "vostro principe naturale" (c. 7r)
and the reproach in c. 20.

c. 9r is marked Duplicato, and c. 11r seems to carry the same word, overwritten. The clear text of c. 20r says the Venice
courier was robbed at the Gradisca border, that dispatches may have been intercepted and that duplicates are enclosed. So
c. 9 is probably one of those duplicates, which is independent support for the reading.

Date of the 1636 letter: the page reads "Di Mod.na li 2. feb.o 1636" on an enlarged crop, and c. 73r has "1636" pencilled at
top left. 1 Feb 1636 is c. 72, to Forni, a different letter. Bolognesi's post in February 1636 is unproved: nothing opened
places him. The letter speaks of S. M., ministers and "stati imperiali", which fits an imperial court, but Vienna in 1636 is
not shown. The entry of the troops at Castelnovo di Sotto was not found in any source opened. Hanlon's account of Modenese
incursions against Parma in winter and spring 1636 fits the setting only in general.

## System

Simple substitution of Italian. 20 signs for 20 letters (a b c d e f g h i l m n o p q r s t u/v z). No word breaks, no nulls,
no homophones, no code groups in any page read. Balls and dots on strokes are pen style. u and v share one sign. See `key.tsv`.

Hands. The zigzag o with a ball and plain t: c. 9, c. 11, c. 20, c. 23r. The H-like o, alpha-like s and tailed t: c. 7r,
c. 13r, c. 16. The values are the same. cc. 73-74 is a third hand, and it adds one device: a small caret above a sign doubles
the letter.

## How the key was obtained

The key came from a later clear copy, not from cryptanalysis. c. 22 is that copy, and it covers the cipher of c. 23r.

1. c. 23r was cut into strips at full resolution and transcribed sign by sign (404 signs).
2. Checked by machine shape reading with no language: clusters 338/360 agree, k-fold classifier 326/399. All 73 disagreements
   were viewed as crops; none changed a sign.
3. The clear text of c. 22 was aligned with the signs. c. 22 has "premere molto nel" where the cipher has no "molto"; with that
   word removed every sign has one value. c. 22 also has a struck "sito" and a closing "e Dio vi contenti", both outside the
   cipher.
4. Frozen on 2 Nov 2026 before c. 13r was transcribed. No value has changed since, including for 1636.

## Held-out test

Cipher of c. 13r, first 8 lines (289 sign positions), against the clear text of c. 15r. Neither was used for the key.

| Reading of c. 13r | Agreement with c. 15r | Shuffled table, mean | Shuffled, best |
|---|---|---|---|
| Visual transcription, key known | 286/289 = 99.0% | 26.7% | 39.8% (200 runs) |
| Machine, classifier not trained on this page, no language | 232/289 = 80.3% | 35.4% | 43.6% (100 runs) |
| Machine, k-fold on the same page, no language | 208/289 = 72.0% | 32.5% | 42.9% (100 runs) |

The machine lines are the fairer proof. Agreement is a longest-common-subsequence count. Of the 3 visual misses, 2 signs are
lost at a blot and 1 is real: cipher "quindecimila", c. 15 "quindicimila". c. 15 speaks of "quel tal ministro" and "Dottor
Genuino", and c. 9r has the same two in cipher. cc. 73-74 is a test six years later: below.

## Independent checks

Two independent AI readers checked the work. `VERIFY.md` and `FINAL_VERIFY.md` are their reports, unchanged. They describe the
text before the final fixes.

First check (529 signs of cc. 9, 16, 20). It disagreed with the solver on 3.0% of signs in its own read and on 6.8% in a key-free
read. That key-free read gave Italian through `key.tsv`.

Final check. The reader saved its signs before opening any solver text. It was not key-free: it used the sign chart and
recognised Italian as it went.

| Document | Signs read | Differences | Rate |
|---|---|---|---|
| c. 7r | 381 | 9 | 2.4% |
| cc. 9 | 286 | 3 | 1.0% |
| c. 11r | 258 | 2 | 0.8% |
| c. 13r | 220 | 6 | 2.7% |
| cc. 16 | 279 | 5 | 1.8% |
| cc. 20 | 212 | 1 | 0.5% |
| c. 23r | 232 | 2 | 0.9% |
| cc. 73-74 | 472 | 8 | 1.7% |
| All | 2340 | 36 | 1.5% |

After zoom most of the 36 were the reader's own errors, unreadable signs or weak pairs. About 4 places were solver errors.
A second run of the key over all transcriptions gave 0 differences in 4858 positions, which shows consistency only.

## Sign-first retranscription

The first files for cc. 9, 11, 16 and 20 were re-encoded from a reading made with the key known. They carried whole-word
repairs. They have been replaced.

1. Every cipher line was cut into numbered strips. Readers with no key and no text copied the signs against a shuffled sheet
   S01-S20, and were told not to use language.
2. The copy was then passed through the key and compared with the earlier signs: 2904 signs, 246 differences, 112 of them n
   read as h.
3. 100 disputed places were viewed on enlarged crops. A sign was changed only where the crop supported it. The changes are in
   `retranscription_log.tsv`, 39 entries with the earlier and present signs.
4. After correction the copy differs from the final text in 62 of 2905 signs (2.1%), plus 117 n/h and 27 signs the reader could
   not read. By letter: cc. 9 2.6%, c. 11r 0.3%, cc. 16 2.5%, cc. 20 0.7%. Differences outside the viewed list were not
   re-examined.

Main results: "lo stato" (c. 16r l. 16) is "l'angustia"; "vedendone" (c. 9r l. 15) is "vegnendone"; "per" (c. 16r l. 6) and "e"
(c. 16r l. 19) are not on the page; "no scemarlo" (c. 11r) is "o scemarlo"; "che qui sia" is "che vi sia"; "sono stati" is "sono
restati"; "da favorir" is "di favorir"; "munizioni" at c. 16r l. 7 is "munitioni".

c. 13r and c. 23r were typed sign by sign in the first pass and were not redone.

## Final pass, 3 Nov 2026

One agent, who had taken no part in the solving, read c. 7r whole and c. 74r rows 8-15 sign by sign on full-resolution strips
recut to the true paper edge (`scripts/recut.py`). This reader had seen the transcription and knew the key. So it is a fresh
sign-first read, not a blind one, and it is not a human check.

- c. 74r rows 8-15, 233 signs, the part the final check did not sample: no difference in any sign. Together with the final
  check's 472 signs and the two short rows (c. 74r row 0, c. 73v row 11), this gives cc. 73-74 a second reader throughout, but
  only the 472 were saved before the solver's text was opened.
- c. 73v and c. 74r: the old strips stopped at x = 4993 and the paper runs on past that. Row 8 `A`, row 4 `N` and row 10 `V` are
  whole on the page and are now unbracketed. "a Milano" stands on the page. No sign is lost at the edge in any row, and none
  stays illegible. c. 74r row 0, sign 4, has vertical sides unlike the clean triangle six signs on, so it is the box:
  prometterci, still doubtful in sense. The log is `retranscription_log_1636.tsv`.
- c. 7r had not had a sign-first pass. It gave 5 changes, in `retranscription_log_c7r.tsv`. l. 8 is g V, "strigne", silently
  swapped before. l. 4 has one g in "Corre[g]gio"; the second was a repair. l. 15 has an a sign that had been dropped, "cooperare
  a nostri interessi", which adds one word. The last signs of l. 14 and l. 15 are damaged at the edge and are now marked.
- No correction on the final check's list was found wrong on the image. The three `c 2 A` differences in its c. 7r read were its
  own error, as it says: the dotted d is followed by a alone.
- Clear text: c. 13r l. 5 is `[?fermo]`, not "ferro"; "by the sword" is dropped. c. 73r has "questa notte", not "[?questa passata]".
- The 1636 reading now brackets every restored letter. It had printed six plain, so its earlier strict count was too high.
- The earlier word totals counted the editor's English. The counter is fixed.

`transcription_<doc>.txt` holds the signs as they stand. `decryption_<doc>.txt` is letter for letter. `reading_<doc>.md` gives the
whole letter with clear and cipher marked apart and an editorial note for every departure from the signs; `translation_<doc>.md`
gives the English. `scripts/readings_final.py` compares each reading with its decryption and lists every departure; each one has
its note. `scripts/check_decryption.py` reruns the key.

## Reading

- **c. 7r:** the prince of Correggio is held prisoner in his own town by the Germans, under order to appear at Sabbioneta within
  25 days. The agent is told to move first, and that once the prince's ruin is beyond repair he must serve Modena.
- **cc. 9r-9v:** the duke suspects the court of feeding him hopes in order to use him. Rumour says the Germans have taken the fief
  of the prince of Castiglione for favouring the Venetians. The agent is to propose Correggio for Modena and Castiglione for the
  duke of Guastalla, and to watch Mirandola.
- **c. 11r:** the duke of Mirandola is at risk of a trial too. Warn His Excellency, and enlarge the danger.
- **cc. 16r-16v:** the marchese di Villafranca's offers may bring requests for money and munitions. The arguments for refusing:
  fortresses to supply, the sum paid to Collalto, over 400,000 scudi gone on grain, an exhausted population. The agent is to renew
  the hope of a match with Princess Margarita, the duke's sister.
- **cc. 20r-20v:** the agent cannot serve Modena and also handle business for Mirandola and Correggio.
- **c. 23r:** inform Carnevale, in general terms only.
- **cc. 73r-74r (1636):** French and Savoyard troops enter Modenese land while their envoys are still in the city. The duke will show
  his front and hold the main strongholds. Postscripts: His Majesty must attend to Italy or lose his imperial states; 200,000 scudi
  have reached the legate at Bologna to raise troops, and Cardinal Antonio Barberini is expected there.

Writer's slips, kept in the decryption and marked in the reading: "aongiunture", "oaulato", "confidenui" (c. 9r); "proaessi", "qualco"
(c. 11r); "c all|alloggio" (c. 16r); "Corregio" with one g (c. 7r, c. 16v); "coni" (c. 16v, left doubtful); "quclificati",
"circontanze", "qrincipe", the repeated "del principe del" (c. 20r); "crepcnti dc nostri cicscuno" (c. 20v). For 1636 see the notes in
its reading file.

## Lettera F (located 2 Nov 2026 by the public result pages of Lodovico)

| Letter | Date | To | Cipher | Result |
|---|---|---|---|---|
| cc. 73-74 | 2 Feb 1636 | Ottavio Bolognesi | 716 signs | **same key** |
| c. 53 | 22 Jul 1634 | Paolo Francesco Forni | about 570 signs in 17 lines | separate key, not solved |
| c. 54 | 25 Jul 1634 | Forni to the duke, reply | clear and cipher | not transcribed; mixed Latin-like signs |
| c. 72 | 1 Feb 1636 | Forni | about 4 lines | not transcribed; looks like the c. 53 signs |
| c. 4 | 25 Oct 1642 | Francesco Ottonelli | digits and letters | not transcribed; not this system by eye |
| cc. 5-6 | 25 Oct 1647 | Ottonelli | digits and letters | not transcribed; not this system by eye |

Test on cc. 73-74. One key-free reader copied all the cipher against the 1630 sheet, in a hand it had not seen. The copy went through
`key.tsv` unchanged and gave Italian at once, for example `noisiamorisolutidimostrarelafronte` and `cardinalantoniobarberino`. Every one
of the 20 values holds. The base text is that copy, with 17 corrections made on enlarged strips and logged in
`retranscription_log_1636.tsv`.

So the same table served this correspondent from 1630 to at least 1636. That fits the Este practice of one cipher per correspondent:
the letters to Forni use another table.

c. 53 is a separate key: other shapes (phi, epsilon, xi, omega). A key-free copy at reduced size gave 573 signs and 21 labels. That
looked like a simple substitution, so a ciphertext-only attack was run: annealing against Italian trigrams, 40 restarts. It gave no
Italian. A control on 573 letters of known Italian with a shuffled key and the same solver recovered 429 letters and was plainly
readable. So either the copy is too rough or c. 53 is not a plain substitution. The copy has a flat frequency profile, hardly any
doubled signs and small marks over the signs that were ignored. Treat c. 53 as unsolved. Next step would be a full-resolution copy.

Other leaves checked, no cipher: Lettera T cc. 5-6, 8, 10, 12, 17, 18-19, 21, 24, 27-28. Marks on c. 7v and c. 11v are show-through.
Lettera F cc. 5-6 is a different item from Lettera T cc. 5-6. The catalogue's vetting note needs correcting: the versos are not blank,
and c. 9 alone has 1275 signs.

## Historical context

The 1630 setting is the War of the Mantuan Succession, with Imperial troops under Rambaldo di Collalto in northern Italy. Britannica
confirms the Emperor's condemnation of Siro da Correggio in 1630. Later steps differ by source (1634, 1635, 1641). Unchecked, from
general reference: Guastalla under Ferrante II Gonzaga, Mirandola under Alessandro I Pico. If those hold, c. 9 shows Modena proposing
to acquire Correggio in February 1630. In c. 73v the clear text itself has the enemy aiming to put Signor Siro back in his State. All
of this needs a historian's check.

## The later hand

c. 15 and c. 22 look like one hand by eye. It is not contemporary; c. 22 is headed "Copia dall'autografo". On c. 15 the words that stand
in clear in c. 13r are underlined, so the writer had the cipher leaf in front of them and could read it. Someone before us knew this
key. Whether that person deciphered more, or published, is open. No evidence links the hand to Campori. "No decipherment in the file"
above means only that no clear copy of that letter is in the file.

c. 7r points the same way. Thin vertical strokes run through its cipher at l. 8-16 and fall at word divisions, in l. 14 on either side of
"compiamo", and in l. 15 after the dropped a. A small dark cross stands above "cose" at l. 9. These are a reader's marks, so someone who
could divide the words worked through this leaf. Whose they are, and whether other leaves carry them, was not checked.

## Prior art and collision (3 Nov 2026): open

We do not claim that any of this reading is new. Nothing found shows these letters printed, and nothing shows they are not.

- Collision: no target folder and no commit naming these documents in origin/main of the cyphersolver clone, rechecked at head
  47a53b8a2 on 3 Nov. The catalogue entry came from the Estense sweep merged on 29 Oct.
- Maria Luisa Doglio's edition exists: Fulvio Testi, *Lettere*, 3 vols (1609-33, 1634-37, 1638-46), Bari, Laterza, 1967, Scrittori
  d'Italia 236-238. It was not opened. No scan was found. Her "Intorno alle lettere edite e inedite di Fulvio Testi", *Lettere
  Italiane* 16 (1964), 425-444, was not opened either. Whether she prints ducal letters countersigned by Testi is not known.
  https://www.helveticarchives.admin.ch/detail.aspx?ID=730769
- B. A. Raviola (ed.), *Corti e diplomazia nell'Europa del Seicento. Correggio e Ottavio Bolognesi (1580-1646)*, Mantova 2014. It is
  the first place to look for his posts and his ciphers. Not opened.
- The 1843 *Memorie di Religione, di Morale e di Letteratura* XV-XVI, "Lettere inedite": not opened, to be checked first among the old
  editions. https://books.google.com/books?id=cMwaAAAAYAAJ&pg=RA1-PA333
- The Reggio inventory could not be opened (DNS failure). The extract says "I cifrari del cav. Ottavio Bolognesi si trovano uniti alle
  carte". The key may survive there, and his papers may hold clear copies.
- No Campori edition of Testi's letters was found.
- Other editions, none opened: *Opere scelte* II (Modena 1817), said to be open at HathiTrust; letters to Sassatelli (Modena 1841);
  Lazzari (Faenza 1872); De Castro, *Fulvio Testi e le corti italiane* (1875), said to be open at HathiTrust. Muratori, *Annali*, 1636:
  passage not found. Hanlon, *The Hero of Italy*: extract only.
- The Archivio di Stato di Modena keeps 8 buste of ciphers:
  https://www.filodiritto.com/la-parola-incognita-cifre-e-cifrari-alla-corte-estense . No link to these letters was found.
- The later hand of c. 15 and c. 22 could read the cipher (above).

## Remaining gaps

- Rest of c. 13r, c. 13v and the cipher of c. 14r - blocker: not-attempted; the images are good and c. 15 covers them, so this is a transcription job.
- c. 53 (22 Jul 1634, to Forni) - blocker: no-key-material; a separate key; annealing on a rough copy gave no Italian; a full-resolution copy is the next step.
- c. 54 and c. 72 (1634, 1636, Forni) - blocker: not-attempted; they may share the c. 53 table.
- c. 4 and cc. 5-6 (1642, 1647, Ottonelli) - blocker: not-attempted; digits and letters, not this system by eye.
- c. 7r l. 14 `[?compiamo]` - blocker: too-short; signs certain, sense not; a slip for compatiamo or compiagniamo would fit; neither is adopted.
- c. 9v l. 8 `[?roliet]` - blocker: too-short; signs certain; perhaps a name followed by et; neither c. 15 nor c. 22 mentions it.
- c. 16v l. 2 `[?coni]` and c. 74r `[?prometterci]` - blocker: too-short; each occurs once; signs read, sense not settled.
- c. 16v: whose son is meant depends on the doubtful clear word before "la speranza" - blocker: not-attempted; needs a palaeographer on the clear hand.
- "Sua Eccellenza" (c. 11r), Carnevale (c. 23r), Genuino (c. 9r), S. M. (c. 74r) not identified - blocker: not-attempted; a historian's question.
- Clear passages are a first transcription, especially `[?Feudo]` (c. 9r), `[?Inviato predetto]` (c. 16v) and the place names of c. 73r - blocker: not-attempted.

## Escalation

- [x] siblings: all 13 letters of the entry located; neighbouring leaves of Lettera T opened (list above); the 1636 letter tested against the 1630 key and read
- [x] clear-pages: c. 15 and c. 22 are later clear copies, used for the held-out test and for the key
- [x] known-keys: c. 53 has other shapes, so this key does not apply to it; a grep of the repository's target notes found no Modenese key of this period; the Modena and Reggio cipher papers were not seen
- [x] print: searched and not settled; Doglio, Raviola, the 1843 Memorie and the Reggio inventory were not opened (see Prior art)
- [n/a] key-rebuild: every one of the 20 values is in use and the table is complete; c. 53 needs a new copy, not a rebuild
- [x] retry: the doubtful words were rechecked on enlarged crops; each stays doubtful in sense

## Image sources (links only; no scans in git; licence CC BY-NC-SA)

Lodovico IIIF manifests: `https://edl-jarvis.cultura.gov.it/meta/iiif/<uuid>/manifest`

Lettera T:

- `466c929f-5b41-4996-96f0-6d65429c75bb` cc. 7-8
- `3ac41f1e-cfa3-4f0e-bde9-2a91a418a341` cc. 9-10
- `4b2f1bef-0336-4adf-a960-1dfb03cb152e` cc. 11-12
- `1a595038-5b35-475f-ae2b-9e927b07d9d7` cc. 13-15
- `92cc5498-d423-4a05-ae2b-a3a723a4787c` cc. 16-17
- `122b0a36-7822-40ef-a2b5-879773f20d11` cc. 18-19
- `9f92e76e-7316-4139-ae70-564668947e1c` cc. 20-21
- `723cce42-473d-431e-97e4-295ddac6851a` cc. 22-24
- `112c6f62-e5da-4986-94f2-d2d18bba1157` cc. 5-6
- `f1bb842b-abfc-4b97-82be-9659656c7f1d` cc. 27-28

Lettera F:

- `5bb52515-109c-495f-b472-ffe341e2e472` cc. 73-74
- `702e1f5d-f8ee-4035-87ff-9a782712569e` c. 53
- `0c1244d5-6e7d-45f3-9656-fee0c0bb8d18` c. 54
- `040c52d4-0303-48f9-b895-2c8fec535793` c. 72
- `7cfec976-3e73-454f-b443-bfb6538e2ba8` c. 4
- `5bde0757-a1dc-4e7f-b24b-d57713d30579` cc. 5-6

Image server note: whole pages work only at fixed sizes (pct:25 is fine); regions work up to about 1800 px output width. Use the width
from info.json, not the manifest.

## Files

`key.tsv`; `transcription_<doc>.txt`, `decryption_<doc>.txt`, `reading_<doc>.md`, `translation_<doc>.md` for cc07r, cc09, cc11r, cc16, cc20,
cc23r, cc73-74 and cc13r lines 1-8; `retranscription_log.tsv`, `retranscription_log_1636.tsv`, `retranscription_log_c7r.tsv`; `VERIFY.md`,
`FINAL_VERIFY.md`, the independent checks, unchanged; `scripts/`. The images and working files are not in this folder.
