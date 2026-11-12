# klogesoren1858: "Kloge Søren" (Søren Christensen), his Cyprianus, a book of charms in his own cipher, c. 1858 (catalogue 2525)

Status: read in part (Brice Dudout, 11 Nov 2026; integration check 12 Nov 2026). The key is right: the writer's own alphabet table on
image 091 left gives the same values. Measured share, certain words only, on the one sample graded word by word on the image (the
held-out images 030-031, about 2% of the book): **130 of 176 words = 73.9%**; with the probable words 172 of 176. The contributor classed
169 of his 179 words there as certain or probable (94.41%); eight of those were misread, so 161 stood. No whole-book share is given
(see "Claims review by a second reader"). 136 of the 148 pages have no sign-level transcription: their reading (the contributor's classification, 95.4%)
cannot be re-derived from the files. Open: those 136 pages unchecked, seven doubtful words on the first nine pages, the seals.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents (transcription, key, protocol and measurement, reading,
write-up). Catalogue entry **2525**, found and vetted by Daniel Bourdeau on 11 Nov 2026 (KB Copenhagen Primo sweep, Nordic sweep of
11 Nov), who pointed to the book, to its "lønskrift" (secret writing) and to the KB images.

## Document

Copenhagen, Det Kgl. Bibliotek, Dansk Folkemindesamling, **DFS 1997/020** (Kloge Sørens samling). One octavo volume, 109 images
on KB Digitale samlinger (object392246, https://digitalesamlinger.kb.dk/manus/musman/2010/dec/viser/object392246/da/; IIIF
DFS_1997_020_4_000a to _107 on kb-images.kb.dk). **Each image has its own folder** on the image server and the folder numbers are
not regular (003 is .../OnlineMasterArkiv/0000/392/251/DFS_1997_020_4_003/, 030 is .../392/278/DFS_1997_020_4_030/, 091 is
.../392/232/DFS_1997_020_4_091/, and 007 and 008 are 256 and 255): take each info.json URL from the HTML of the viewer page. The
path .../392/246/... given in an earlier version of this note and in the catalogue entry returns 404. The KB marks the material as
out of copyright ("Materialet er fri af ophavsret"). The contributor's folder holds no image, crop or derivative; the site page
carries two crops made at the integration (image 003 right and the table on 091 left), credited to the KB.
Credit: Det Kgl. Bibliotek / Dansk Folkemindesamling, DFS 1997/020.

Søren Christensen, "Kloge Søren" (1843-1925), a cunning man of Funen, wrote this Cyprianus (a book of charms and cures) from 1858,
as a boy, almost wholly in his own cipher, in red ink, under headings in clear Danish. The cipher text runs from image 003 right
to 079 right; images 080 to 093 are blank leaves, pastedowns and binding; image 091 left carries the writer's table of the cipher
alphabet. Two loose leaves carry cipher in the same signs: 098 (a charm, two copies) and 104 (a circular seal, not read). A private
piece of the 20th century, not part of the grimoire, is excluded from this write-up.

## System and key (`key.tsv`)

A simple substitution, one sign per letter, with **word spaces kept** (the catalogue scan at 1,700 px did not show them; at full
size they are clear). About 27 signs made of chevrons, bars under 1-3 dots (u, n, m), strokes with dots placed above, beside or
below (s, k, h, b, p), hooks (d, g, r, i/j), a cross (t, also f), an arch (v), dots (o, ø). Homophonies and confusions declared:
t/f, o/ø, i/j. Ligatures (aa, tt, nn, mm) and variants are listed in `key.tsv`, section D.

How the key was found (training portion only, images 003 right to 007 left, 1,591 signs transcribed at low resolution): probable
words from the clear marginal "3 gange", the closing formula "i Navnet Gud Fader, Gud Søn og Gud den Hellige Aand. Amen" and the
cipher ordinals of the headings ("Andet / Tredie Begreb"); then a **blind** simulated annealing (simple substitution, Danish
quadrigrams with the space from Project Gutenberg texts, only the space fixed) found by itself "saa sandt ... dette blod ei mere
flyde i navnet gud fader gud søn og gud den hellige aand amen" (6 of 10 restarts converge).

`key.tsv` sections: A = the key as measured (frozen/KEY.json); B = separation of the stroke-and-dot signs at full resolution,
after the measurement; C = the writer's table on image 091 left; D = ligatures and variants of the second session. License CC BY 4.0.

## Validation (`frozen/`)

**Key validated (the contributor's run; see the Integration check for the re-run and what the figures measure).** One measurement; by the contributor's record it was pre-registered and hashed before the held-out portion was looked at:
`frozen/PROTOCOLE.md` SHA-256 106f10c69168ee2aa1c5a1390c040351b512f40bb461b426f3984fd2292a7329, `frozen/KEY.json` 40bf4b2d...,
scorer `mesure.py` 530a86e5..., Danish word list 5c295d99... (`frozen/FREEZE.sha256`; the scorer and the word list are not
included: the scorer holds a local path, the list is built from Gutenberg texts). Held-out portion = image 030, then image 031
added by the protocol's rule because 030 has fewer than 300 signs; by the same record both were transcribed and hashed before any decoding
(`frozen/RESERVE-p030.txt` d56aef4d..., `frozen/RESERVE-p031.txt` d2d93503...). Result (`frozen/MESURE.out`), on 790 signs
(185 words): lexical cover **COV 0.4025** (C1 >= 0.40: met, narrowly); best of 200 permuted keys 0.1089 (C2 threshold 0.359: met);
best of 200 shuffles of the signs 0.1038 (C3 threshold 0.354: met); S (two consecutive lines read as Danish without correction):
met. Declared bias: the held-out portion was transcribed by an agent who already knew the key; C1 passed with a small margin.

**A second, independent confirmation, after the measurement:** image 091 left (found at the end of the volume during the second
session) is a **table of the cipher alphabet in the writer's own hand**, a to ø, one sign per letter in alphabetical order, without
the letters. Every value of the measured key found in the table falls at its place (19 letters: a, b, c, d, e, f, g, h, i, k, l,
m, n, o, p, r, t, u, v), and it adds q, s (a straight dotted stroke, opposed to the curved dotted i), z, æ, ø. A second form of g is written above
the g, probably added by a later user.

## Reading (`reading.md`, `translation.md`, `decryption.txt`)

This section is the contributor's account and figures as delivered on 11 Nov 2026; the Integration check below corrects the
held-out pages and the first nine pages and says what the percentages are worth. `translation.md` is a summary table of every
charm with full translations of a few of them, not a full translation.

The contributor's counting rule: read = certain + probable words; restored and unresolved words are holes. Clear headings, arabic numerals,
apothecary units and seals are not counted; cipher headings ("Ottende Begreb") are counted.

| part | pages | certain / probable / restored / unresolved | words | read |
|---|---|---|---|---|
| held-out portion (030, 031) after the blind sheet K1, result B (**retained**) | 3 | 133 / 36 / 1 / 9 | 179 | **94.41%** |
| same, result A (the hashed integration rule taken literally) | 3 | 133 / 37 / 1 / 8 | 179 | 94.97% |
| first session, low resolution (003 R - 008 L, except 007 R) | 9 | 292 / 93 / 0 / 40 | 425 | 90.6% |
| second session, full resolution (007 R, 008 R - 079 R, 098), after the blind sheet K3, result B (retained) | 136 | 6,441 / 668 / 76 / 266 | 7,451 | 95.4% |
| **whole book, indicative only**, after K3, result B (retained) | 148 | 6,866 / 797 / 77 / 315 | 8,055 | **95.1%** |
| same, result A (rule as written) | 148 | 6,866 / 796 / 77 / 316 | 8,055 | 95.1% |
| whole book before K3 | 148 | 6,863 / 802 / 77 / 313 | 8,055 | 95.2% |

- The figure we declare is the **held-out portion, 94.41%** (result B, retained at Brice Dudout's request; result A 94.97%). Both
  are under 95%, hence "read in part". See `BLIND-REREADING.md`.
- The whole-book figure, **95.1%** (95.13%, result B; A 95.12%; 95.16% before K3), is given **as an indication only**: the second
  session was checked blind on nine targeted signs only (sheet K3: three probable words became certain, two became
  unresolved, three by the rule as written; see `BLIND-REREADING.md`), and on the held-out portion the blind sheet K1 took the share down by 1.7 points (96.1% -> 94.41%). We do
  not claim 95%. The held-out portion was not touched by K3.
- **Nine pages of the first session were read at low resolution (4,115 px) and are still to be re-read at full resolution**: 003 R,
  004 L, 004 R, 005 L, 005 R, 006 L, 006 R, 007 L, 008 L (90.6%; 005 R 69.4% and 005 L 79.2% are the weakest).
- Weakest pages of the second session: **064 L 61.4%** (a list of conjuration words, stained and faded), **010 R 77.2%** (end of a
  fever litany), then 011 R 82.1%, 019 R 82.5%, 064 R 84.4%, 034 L 86.6%, 010 L 87.1%.
- The 136 full-resolution pages were read by 16 sub-agents (one batch each), each writing a fiche per page with a class per line
  and a list of doubtful sign shapes (1,122 in all). A random draw of them (sheet K2) was pre-registered and abandoned before it was shown; the targeted sheet K3 took 9 of them,
  chosen for the words whose class depends on the answer (`BLIND-REREADING.md`).

Content: about a hundred charms and recipes of a Danish cunning man (summary of each in `translation.md`, section 1). Cures
(bleeding, wounds, colic, toothache, fever, chilblains, childbirth, warts, scrofula, rickets, bed-wetting, consumption), protection
of cattle, horses, poultry, geese, butter and milk against witchcraft, pests summoned to the Thing (caterpillars, rats and mice),
dogs and bulls held at bay, guns bound and men made proof against shot and blades, fire conjured (Mary's cloak; the SATOR square),
winning at cards, and a long series against thieves (to make one stand still, bring back what he took, or suffer). The charm types
are the classic ones of Danish tradition (Ohrt's "Danmarks Trylleformler": the Longinus charm, "Gud sætter sin Stav for Flod",
the impossible condition "førend Jomfru Maria føder en Søn"); what this book holds is their text, and above all the written
directions for use, which only the cipher held.

Numbering: the cipher Begreb numbers run 1 to 23, the 23rd twice (031 R and 036 L, "Treogtyvende"); the 24th is never read; one
Begreb (butter, 020 R) has no number read; no Begreb number appears after 036 L.

## Integration check (12 Nov 2026)

PR #419 was checked by an independent verifier before integration; this section applies that report and adds a re-reading of
twelve pages on the full-size KB images.

**What reproduced.** The four frozen hashes match (`PROTOCOLE.md`, `KEY.json`, `RESERVE-p030.txt`, `RESERVE-p031.txt`); the scorer
`mesure.py` and the word list are not in the PR. The later commits touched no frozen file. An independent decoder gives the same
DECODE line as `frozen/MESURE.out`. Held-out size: 790 signs plus the numeral 3, 185 words.

| figure | contributor's run | verifier's re-run (own lexicon: 25,681 forms from the repository's `da-gutenberg` corpus, same tolerances) |
|---|---|---|
| lexical cover of the held-out portion | 0.4025 | 0.404 |
| best of 200 permuted keys | 0.1089 | 0.157 (mean 0.053) |
| best of 200 sign shuffles | 0.1038 | 0.117 (mean 0.078) |
| cover of the training portion | 0.575 | 0.555 |

The protocol asked for a margin of +0.25 over the best control. The contributor's run has 0.294 over the permuted keys and 0.299
over the shuffles: met. With the verifier's lexicon the margin over the best permuted key is 0.247, so the declared margin of 0.25 is not met
in the re-run (it is met, at 0.294, in the contributor's pre-registered run); over the shuffles it is 0.287, met. Both runs are reported; a cover of 0.40 against 0.16 or less is not chance either way. The annealing
script is not in the PR: the verifier's own crude blind annealer on the training transcription reached 19 of 29 sign values in the
best of 6 restarts, which supports a ciphertext-only attack but does not reproduce "6 of 10 restarts converge".

**The strongest evidence is the writer's table.** Image 091 left, seen at full size: 26 signs in three rows (10 + 11 + 5), which in
alphabetical order are a-k, l-v and x y z æ ø. The values of the measured key fall at their places. The key is therefore in the
volume (`key_in_volume`). **By the contributor's record** the table was found during the second session, after the key had been
recovered and measured; all three commits are from the same evening, so that order rests on the contributor's account.

**What 0.4025 and 94.41% measure.** They are different things. 0.4025 is the share of signs falling in word-list words when the
frozen key is applied mechanically to the frozen transcription. 94.41% is the share of words a reader classed certain or probable
after correcting by sense and re-reading. Only 49 of 182 held-out reading words (27%) equal a mechanically decoded word; at
character level 85% agree, 93% if a and e are merged (verifier's measurement). So **the frozen held-out transcription is wrong in
roughly one sign in ten** (missed dots for a/e and b/h, word spacing; the transcriber knew the key), and **94.41% is a reader's
classification, not a measured accuracy**: words classed certain or probable include wrong words.

**Held-out pages corrected on the image.** Images 030 and 031 were re-read at full size (8,230 x 6,804 px per opening) against the
writer's table. Eight of the 169 words the contributor counted as read were misread:

| place | contributor | on the page |
|---|---|---|
| 030 left, l. 2 | hold[t] | beholdt (b e h o l d t) |
| 030 left, l. 4 | holdt | beholdt |
| 030 right, ll. 3-4 | for Bøssen dig (two words) | for bestan-dig = bestandig, for ever |
| 031 left, l. 1 | saae | seer |
| 031 left, l. 9 | skal | skeer |
| 031 left, l. 4 | paa Verden | a single sign p before Verden: "paa" is supplied |
| 031 right, end of the heading | Den som stjæler fra [dig] | Dem som stjæler fra |

Also: "Mari[a]" (030 l. 3) was counted restored, but the final a is on the page; "[?ra]" (030, second charm) is not on the page
(a doubling in the frozen transcription); "Artila / [?sia]" is one word across a line break, Artilasia; "Jom-fru" and
"Kir-kegaard", left unresolved by the blind sheet K1, are written across line breaks with the writer's hyphen mark and are plain
at full size; "[?ssyon]" is "skjøn" (the two dots of k stand over the next sign), which gives the rhyme "Jomfru skjøn / een Søn".
"beholdt", "bestandig", "seer", "skeer" and "skjøn" appear nowhere in the PR.

So, on the held-out pages: 161 of the contributor's 179 words stood as delivered (89.9%, a figure that counts his probable words).
After correction the pages hold 176 words (030: 63; 031 left: 52; 031 right: 61): 130 certain, 42 probable, 1 supplied (paa) and 3
doubtful (Kabbe, for Kaabe; karlegravet; søn). **Certain words only: 130 of 176 = 73.9%**, the figure used as the headline since the
claims review; with the probable words 172 of 176. That second figure is the integration reader's classification, made with the key and the table in hand: it is
not blind and not an independent measurement. The frozen files are unchanged; the corrected signs are in `transcription.txt`,
Part 2b, and `decryption.txt`, Part 2.

**The first nine pages re-read.** Pages 003 right to 008 left (the contributor's low-resolution session, 385 of 425 words classed
read, 90.6%, delivered as a summary with gaps) were re-read on the full-size images; the complete text is in `reading.md`, Part 1.
Counted by the rule of the held-out pages (see the claims review; the first count here, 447 words and 437 read, did not follow it):
459 words, 9 doubtful (Aanmanden; saa Blodet staar; vaadne, badne, kølne; blødne; vaade), 1 supplied (i), 449 without a doubt mark, of
which 4 have one letter supplied (ell[er], di[n], svig[e], de[r]for). The re-reading was not graded certain or probable. Same caveat: one reader, with the key. Words changed include "bløde" (was flyde), "denne Mand" (was
"den [?]"), "svige" (was [?værke]), "træskelig bedrog" (was "[?fræselig] bed"), "de[r]for vover" (was "det [?orv] over"). The cipher
heading at the top of 003 right, "Første Begreb", was not in the first transcription.

**What cannot be re-derived.** For the 136 pages of the second session (7,451 of the book's words, about 92%) there is no
sign-level transcription: the agents read the images straight into letters. A second decoder has nothing to decode, so the
contributor's 95.4% for these pages, and the whole-book 95.1%, are his classification only and are not a headline figure. The
only outside check on these pages is the verifier's sample of image 013 (about 75 signs: left lines 1-2 and right line 1 decode by
the writer's table to exactly the claimed text). On the two held-out pages first read from a low-resolution transcription, 8 of 169
words classed read were wrong; how far that carries to pages read at full size is not known.

**Counts in the files.** `decryption.txt` carried the pre-K3 counts: its Part 3 header and the page lines of 035 left, 052 left,
027 left, 064 left, 019 right and 016 right now carry the K3 result B (6,441/668/76/266 of 7,451). On four pages (015 left,
044 left, 065 left, 067 right) the page header differs from the sum of its lines by one word; the headers are the declared totals.

**Method and class.** Class: read in part. Method: key recovered from ciphertext-only. The probable words were guessed formulas
and ordinals, not plaintext at hand, and the clear headings give only the subject of each charm; the profile now records the attack
as ciphertext-only with the clear headings as context (it said "known plaintext" and "crib"). This is an independent re-solution:
Ferdinand Ohrt's unpublished copy and decipherment is prior work.

**Not checked.** fynhistorie.dk returned 403 to curl again on 12 Nov and no browser route was available, so the quotation
"Afskrevet og tydet af Ohrt. = kop 79.4" is the contributor's and was not seen here. Whether Ohrt printed these charms in *Danmarks
Trylleformler* was not checked; that matters, because the agents read 136 pages into charm formulas that may be in print (the
verifier's sample of 013 agreed sign by sign, and the errors found on 030 run against memorised formulas). Items 3 and 47 of the
1977 inventory (other key material) were not seen.

## Claims review by a second reader (12 Nov 2026)

An independent reader checked the page against these notes and the profile. What changed:

1. **The headline counts certain words only.** `decryption.txt` says read = s + p (certain + probable), and the figures "161 of 179
   (89.9%)", "172 of 176" and "437 of 447" all counted probable words as read. By the read bar as applied in this round the headline
   is the certain words of the one sample graded on the image: **130 of 176 = 73.9%** on the held-out images 030-031. The figures with
   the probable words are given once, labelled: 172 of 176 (97.7%) after correction; 161 of the contributor's 179 stood (89.9%).
   "Probable" here means a word whose signs give a period or irregular spelling, or whose word spacing or one sign is in doubt, read by
   the sense.
2. **One counting rule.** Each cipher word is one word ("I" and "Navnet" are two; each cipher "gange" is one); numerals and clear
   headings are not counted; cipher headings are. The held-out pages were already counted so (63 + 52 + 61 = 176, recounted from
   `reading.md`). Part 1 of `reading.md` holds 459 words by that rule (43, 65, 65, 43, 40, 43, 53, 58, 49 on the nine pages), not 447:
   9 doubtful, 1 supplied, 449 without a doubt mark (97.8%), 4 of these with one letter supplied. That re-reading was not graded
   certain or probable, so it gives no certain-only figure; 445 of 459 (the words with no bracket at all) is an upper bound for one.
   The contributor's own low-resolution grading of these pages had 292 certain of 425 words (68.7%).
3. **No whole-book percentage.** `outcome.fraction_read` was 0.899 "measured", which the site printed as "partial (90% of the
   cipher)". It was a figure for two images, about 2% of the book. It is now "unknown"; the sample figure 0.739 stays in the text
   entry's `read_share`, and the entry's summary says what it covers.
4. **Order of events.** That the protocol was written and hashed before the held-out pages were looked at, and that these were
   transcribed and hashed before decoding, is by the contributor's record (commits of one evening); said so here and on the page.
5. **The margin.** In the verifier's re-run the margin over the best permuted key is 0.247: the declared 0.25 is not met in the
   re-run. It is met, at 0.294, in the contributor's pre-registered run. "A hair under" is gone.
6. **The table.** Not "every value of the recovered key": the 19 letter values of the measured key that the table carries fall at
   their places; the table adds q, s, z, æ and ø.
7. **Page details.** The clear heading on image 030 is "dölge en Bösse" (no "at"); the line-break mark is called the writer's
   hyphen mark throughout; Sources now name image 013 (the verifier's sample) among the images used.

## Prior art

**An earlier decipherment exists, in the archive (found on 11 Nov 2026, after our reading).** The inventory of Kloge Søren's
collection made in 1977 by Gustav Henningsen, quoted by Hans Nørgaard (comment of 6 Nov 2008 on fynhistorie.dk,
https://fynhistorie.dk/node/16123), describes item no. 4, "Et Ulæg af 9de, 10de og 11te Bøger i Cyprianus ... 1858" (the title
of this volume in the KB record; images DFS_1997_020_4_*; "Ohrt Hskr. 4"), as **"Afskrevet og tydet af Ohrt. = kop 79.4"**:
copied and deciphered by the folklorist Ferdinand Ohrt (1873-1938). **That copy has not been consulted**, and whether Ohrt
published any of it (for instance in *Danmarks Trylleformler* I-II, 1917-1921) has not been checked. **Our reading is
independent**: it was made from the KB images alone, without Ohrt's copy, and the key was validated on our own held-out portion.
What we add is the key, its validation and the probable text, published. An earlier version of this note said that Ohrt could
not have seen a manuscript that entered the DFS in 1997: that was wrong (Ohrt listed Kloge Søren's manuscripts, DFS 1909/3b).

Also known before this reading: the existence of the book, its author and its "kodeskrift" (lex.dk, article "folkemedicin" by B.
Rørbye; heuschkel.dk, "Cyprianus: De sorte bøger", reproduces an opening without reading it); the KB description "Størstedelen i
lønskrift". Daniel Bourdeau's vetting (11 Nov 2026) found nothing on DECODE ("Cyprianus", "Kloge", "lønskrift": 0 records), in
Tomokiyo or Lasry, and no edition. The same 1977 inventory lists other key material in the collection (item 3, "tavle med
opløsning af kodeskrift"; item 47, "et blad med en kode og alfabetisk opløsning heraf"), not seen. **Not verified on paper:**
B. Rørbye, *Kloge folk og skidtfolk. Kvaksalveriets epoke i Danmark* (1976), which deals with cypriani.

## Remaining gaps

- the 136 pages of the second session (007 R, 008 R - 079 R, 098; the contributor classes 266 words unresolved and 76 restored, worst on 064 L and 010 R) - blocker: illegible; stained and faded passages by the contributor's account; no sign-level transcription exists, so neither the holes nor the words classed read can be checked from the files, and the pages were not re-read at the integration
- the shapes flagged by the blind sheet K3 (chevron with a foot on 034 R, closed loop on 073 R, 074 L, 075 L, the star-like sign of 064 L, dot confusions; "fer / før" on 033 L) - blocker: illegible; the contributor's rule forbids a further sheet on the same signs; a declared re-reading is his next step
- held-out pages: Kabbe (031 left), karlegravet and søn (031 right) - blocker: illegible; the signs are plain (k a b b e; k a r l e g r a v e d t; s o n) but the word or its division is not settled by them
- first nine pages: Aanmanden and "saa Blodet staar" (004 left), vaadne, badne, kølne (005 right), blødne, vaade (006 right) - blocker: illegible; dots and word division doubtful at full size; a comparison with Ohrt's copy would settle them
- circular seals (018 R, 019 R, 104) - blocker: illegible; the same signs written round a circle; not read
- prior art on paper: Ohrt's copy and decipherment ("kop 79.4", DFS), whether he printed these charms in *Danmarks Trylleformler*, Rørbye, *Kloge folk og skidtfolk* (1976), items 3 and 47 of the 1977 inventory, and the DFS accession record of 1997/020 - blocker: needs-physical-access; not online, and fynhistorie.dk answered 403 to scripts on 11 and 12 Nov 2026

## Escalation

- [x] siblings: all 109 images of DFS 1997/020 opened (contact sheet, then 173 half-openings at full resolution); cipher on 003 R - 079 R, 091 L (alphabet table), 098 and 104 (loose leaves); the other leaves are blank or binding
- [x] clear-pages: clear headings used as cribs; no clear copy of the charms in the volume; the table on 091 L is a key, not a decipherment
- [x] known-keys: no key on DECODE or in print (Daniel's vetting); the writer's own table (091 L, a key in the volume) confirms ours; an unpublished decipherment by F. Ohrt is recorded in the archive (1977 inventory, 'kop 79.4'), not consulted
- [x] print: lex.dk / Rørbye, heuschkel.dk, KB record, fynhistorie.dk (1977 inventory: Ohrt's decipherment), Ohrt (charm types only, not compared); Rørbye 1976 not seen (not online)
- [x] key-rebuild: stroke-and-dot signs separated at full resolution; ligatures aa, tt, nn, mm and variants added (key.tsv B, D); table 091 L adds q, s, z, æ, ø
- [x] retry: image 031 right lines 16-26 re-read at full resolution (85.8% -> 96.1% on the held-out portion before the blind sheet, 94.41% after); at the integration (12 Nov 2026) images 030-031 and the nine first-session pages re-read at full size against the writer's table (eight misread words corrected on 030-031; 449 of 459 words without a doubt mark on 003 R - 008 L)
