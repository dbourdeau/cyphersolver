# neufville1779: Jean de Neufville's syllabic code with Baudouin, Sartine's secretary (Amsterdam-Paris, 1779-1780)

Status: read in part; written up 24 Nov 2026 (docs/neufville1779.html). The open numbers were retried on every glossed page of the file; the rest needs the Paris archives (see Remaining gaps).

## What it is

The papers of the Amsterdam merchant Jean de Neufville (Jean de Neufville & fils), bound in the Department of State and now
in the Papers of the Continental Congress (National Archives, Record Group 360, microfilm M332 roll 4; free images in the
National Archives Catalog, file unit 464816476; see sources.md), hold a private correspondence in a numeric code:

- **de Neufville's drafts, April-May 1779** (pp.591-609), headed "Mad. d'Arras" or "Chaumont": plain French with code
  numbers written over the syllables (pp.599-603, 606, 608, 609), and one enciphered fair draft (pp.604-606) of the
  letter of 19 April 1779 whose plain text is on p.599;
- **letters from Paris, February 1779 to November 1781** (pp.487-590), addressed to "Monsieur Van Temmel chez Monsieur
  Jean de Neufville, négociant à Amsterdam", signed "Baudouin" and later "Dunoyer", with code groups inside clear
  French; de Neufville wrote the French over many of the groups (pp.516-548, 579), but not over all.

The code: numbers 1 to about 550, one number per letter, syllable, common word or name, with several numbers for common
units (re = 30, 229, 310; que = 22, 23, 278; les = 427, 428, 429). Names include 5 and 106 Le Ray de Chaumont, 529
Vergennes, 328 the Minister of Marine (Sartine), 444, 511 and 213 the Pensionary of Amsterdam, 508 the Stadholder, 500
Mr York (Sir Joseph Yorke), 550 the Ambassador and 417 La Vauguyon, 531 the Spaniards, 464 the States General, 103 the
Amsterdammers, 174 and 169 America, 346 and 347 France, 368 Martinique. key/key_entries.tsv gives every entry and its
source.

## Who read what

- **Who made which table.** On 7 March 1779 (p.499) Baudouin wrote: "je me depesche de faire le chiffre pour vous
  l'envoyer, en attendant, je vous en joins un petit icy, que vous entendrez aisement, ce n'est qu'un changement de
  noms", and that he would sign with "un des noms que je prends dans le petit chiffre cy joint". On 30 March 1779
  (p.516) he acknowledges "la lettre ... avec le chiffre qui y étoit joint et que j'ay trouvé à merveille".
  - So there were two tables: Baudouin's "petit chiffre", a list of cover names (not in the file), and a "chiffre" that
    reached Baudouin from de Neufville by 30 March.
  - The evidence makes it likely that the numeric code of the drafts is the one de Neufville sent. It does not show
    who composed it: Baudouin had said he was making one, and de Neufville may have sent his own instead or as well.
  - Neither table survives as a table; the numeric code is rebuilt here from its use.
- **Jean de Neufville** enciphered his own letters from his plain drafts, and wrote the plain French over many of
  Baudouin's groups. Those parts were read by him in 1779-1780.
- **Baudouin** read de Neufville's letters in the code (the sent letters are not in this file).
- **The Department of State's clerk** who bound and indexed the volume in the 19th century made the identification:
  his index (p.3) lists the correspondent as "Du Noyer, Bowdoin or Mad. D. Arras".
- **The Franklin Papers editors** cite the letter of 23 February 1779 (p.495) as "a cryptic note from Baudouin to an
  unknown recipient" (Papers of Benjamin Franklin 28:354 n.9). Fold3's indexers listed the drafts as "Letters from William Lee to John de Neufville and Son ...
  in French with cipher".
- **What this folder adds** (Andrew Beling, with AI agents, 13-14 Nov 2026):
  - the reconstruction of the code from de Neufville's drafts and the glosses;
  - the evidence on the leaves for the index-maker's identification of "Dunoyer" as Baudouin (the hand, the 7 March
    letter, the 30 March letter);
  - the reading of the bare passages that no one glossed (B573, B491, B492), each transcribed in two passes by the
    same agent (top-down and from the end backward).
  A second AI agent of ours, not a person, checked the folder independently on 13-14 Nov 2026. Its corrections are
  applied (key/corrections_post_test.tsv and below).

## Identification of the correspondent (made by the volume's index; the evidence on the leaves)

- pp.495-497, Paris 23 February 1779, and pp.498-499, Paris Monday 7 March 1779, are signed **"Baudouin"**. The second ends:
  "à l'avenir je signeray un des noms que je prends dans le petit chiffre cy joint".
- From 30 March 1779 the letters in the same hand are signed "Dunoyer"; the covers to "Van Temmel" are docketed "Baudouin".
- The volume's index (p.3, 19th-century hand) already makes the identification. It reads: "12. Thirty-five . . . Du Noyer, Bowdoin or Mad. D. Arras (Private
  news from Paris, for use U.S. 1779-81.)", folio 148.
- Baudouin is Sartine's secretary at the Ministry of Marine: Papers of Benjamin Franklin 29:5-7, note 4 to Dumas's letter of
  1 March 1779 ("'Baud——' for Sartine's secretary Baudouin"); Baudouin's own notes to Franklin, 5 and 25 May 1779 (PBF 29:438).
- "Mad. d'Arras" as a cover for the same man is an inference, from the index and from the same code being used in both
  directions. It is not stated on any leaf.

## The tests

The keys are in key/FREEZE.txt and the test plans in TEST_PLAN.md. Two limits on what the files can show:
- Each test script builds its key by majority vote from a pair file written earlier and scores it in the same run, so
  the file times cannot show that a key was frozen before its test. What is fixed beforehand is the pair file, not the
  key file.
- The full key key_full_r3.json was built after p.573 had already been decoded once with an earlier key. The entries it
  added for p.573 (158 aux, 100 ent, 136 au, 224) come from glosses and drafts on other pages, so the reading is not
  circular, but the key was not frozen before the first look at the passage.
- T2 is weak as a test, because its ten held-out pairs were chosen so that each number also occurs among the training
  pairs.

A second agent of ours took 183 pairs from the drafts pp.599 and 601 before seeing the key. It agreed on 87 of 94
numbers, confirmed 38 of 39 further key entries on the images, and reran the three tests with identical results.

| Test | Key | Result | 200 shuffled keys |
|---|---|---|---|
| T1: predict pp.604-605 from drafts pp.600-603, 609 only | K1, 139 numbers | 139 of 146 covered groups as in the writer's draft p.599 | mean 1.8, max 15 |
| T2: ten p.599 pairs held out | K1 + other p.599 pairs | 8 of 10 | mean 0.21, max 3 |
| T3: the whole 6 May 1779 draft (p.608) held out | K2, 170 numbers | 64 of 65 covered groups (the miss: 106 "Chaumont" for "M. de Ch.") | mean 0.6, max 7 |

The misses in T1 and T2 are the writer's own variants (86 ne/na, 263 i/j, and the word "ménagera", which p.599 glosses
96 86 36 92 = mé na ge ra while his other drafts use 36 = ra, 92 = la).

Corrections after the tests are in key/corrections_post_test.tsv; the frozen keys are unchanged. Each was checked
on the image: 224 is m in "compter" (p.600) and n in "l'emprunt" (p.573), so it is m/n; 381 "passe" is a misreading of 384;
9 is "deux" (p.600) and "da" (p.599); 71 is "on" (p.535 gloss) and "mme" (p.601). No reading in this folder changes.

Statistical validation (docs/_validate.py, validation.tsv: the drafts' own plain units plus the bare passages read with
key_full_r3): pass, z 9.1 against random keys, 4.1 against refits to shuffled text.

## Integration check (14 Nov 2026)

Done for the project at integration of pull request #587; the contributor's text above and below is unchanged.

| Claim | Contributor | At integration | How |
|---|---|---|---|
| T1, pp.604-605 from K1 | 139 of 146, shuffles max 15 | 139 of 146; 200 shuffles max 15; own 2,000 shuffles max 23 | scripts rerun; own scorer |
| T2, ten held-out pairs | 8 of 10, max 3 | 8 of 10, max 3 | script rerun |
| T3, p.608 held out | 64 of 65, max 7 | 64 of 65, max 7 | script rerun |
| Key hashes | key/FREEZE.txt | all three equal | sha256 |
| Full key | 204 numbers | 204, identical | own build from the pair files |
| Bare passages, numbers | 43 + 18 + 7 | 68 of 68 agree with the images | frames 0428, 0363, 0364a |
| B573 read share | 39 of 43 numbers, 91% | 13 of 18 words, 72% | strict rule, below |
| B491 read share | 12 of 18 numbers, 67% (86% without four nulls) | 10 of 16 units, 62% | strict rule |
| B492 read share | 5 of 7 numbers, 71% | 1 of 4 words, 25% | strict rule |

- **Tests.** All three reproduce, and the key files rebuild byte for byte. Each passes the bar its plan sets (T2 exactly
  at the bar). The order of events (plans written before the runs, keys frozen before scoring) is by the contributor's
  record; the contributor says the same above.
  - T1: K1 covers 146 of the 179 groups that have a unit in the draft, so 139 is 77.7% of all of them.
  - T3: the truth file holds 69 pairs. On the image of p.608 at least 13 further groups stand over the French and are
    not in it (313 in "connoisse", 32 290 85 60, 204 before "envie", 261 310 133, 88 74 61 230 248 164). T3 therefore
    scores the pairs that were aligned, not the whole page. One of the groups left out, 204 for "l'", would be a miss.
- **Second decoder.** A decoder written here from the pair files gives the same key and the same four decodes. One
  difference: 136 has one vote for "à" and one for "au"; the frozen key holds "à", and letters/B573_decode.txt prints
  "au". The reading needs "au", which the gloss on p.516 gives.
- **Images** (National Archives Catalog, `.../M332/004/<frame>.jp2`, fetched by plain download). Frames for the drafts:
  p.599 = 0449, p.600 = 0450, p.601 = 0451a, p.603 = 0452, p.604 = 0453, p.608 = 0455b.
  - The three bare passages: every number agrees with letters/B*_groups.txt (68 of 68). The last number of p.573 looks
    like 369.
  - Key sources: about 60 of the 69 pairs of p.608, 35 pairs of p.600 and 40 pairs of p.599 were compared with the
    numbers standing over the French; all agree. p.599 does carry the numbers over de Neufville's own words, and its
    lower block spells the units out under the numbers, so T1 is scored against pairs that are on the leaf.
  - On p.599 the number 30 stands over "re" in "encore" (47 30). "g" for 30 in "ar{g}ent" (B573) and "{G}rand" (B492) is
    therefore against the key in both places. Both words are counted as holes.
- **Identification.** Seen on the images: the index entry on p.3 ("12. Thirty-five ... Du Noyer, Bowdoin or Mad. D. Arras
  (Private news from Paris, for use U.S. 1779-81.)", folio 148); the letter of 23 February 1779 signed "Baudouin" (frames
  0366-0367b); the letter headed "A Paris le Lundy 7 mars 1779" (frames 0368-0369a) with "je me depesche de faire le
  chiffre ... je vous en joins un petit icy ... ce n'est qu'un changement de noms", signed "Baudouin", and "à l'avenir je
  signeray un des noms que je prends dans le petit chiffre cy joint"; the cover to "Monsieur Van Temmel chez Mr Jean de
  Neufville negociant à Amsterdam". The hand of these letters and of the letters of January 1780 looks the same; that
  was judged by eye, by an AI model, not by a person. 7 March 1779 was a Sunday, so "Lundy 7" is the writer's slip or
  the letter is of the 8th.
  - (Superseded: checked later in Founders Online via Chrome, 14 Nov 2026; see below.) Not checked here at first: that Baudouin was Sartine's secretary, and the Franklin Papers notes (28:354 n.9; 29:5-7 n.4;
    29:438). Founders Online answered scripted requests with an empty response on 14 Nov 2026 (a bot check); it needs a
    browser.
- **Strict read shares** (sure words only; an open number, an unread number and a unit set by the word against the key
  are holes; counted in words carried by code numbers):
  - B573: 13 of 18. Read: les, États, Généraux, a, retiré, aux, l'emprunt, un, emprunt, son, au, crédit, du. Holes: [3],
    [58]rands, [227]er, ar{g}ent, [369/349]. "l'emprunt" reads exactly with 38 = ru (the p.526 gloss); "un emprunt"
    needs 352 and 394 as "un" where the key has "une", and 224 = m (key/corrections_post_test.tsv).
  - B491: 10 of 16. Read: Stadhouder (twice), à, la, cour, Monsieur, le, Pensionnaire, de, Amsterdammois. Not read: 507,
    501, 405, 387, 390, 447. That the last four are nulls is the contributor's suggestion, not shown.
  - B492: 1 of 4 ("ce"; [143], [162] and "{G}rand" are holes).
  - Together 24 of 38 = 63%. The contributor's figure, in numbers with a key value, is 56 of 68 = 83%.
- **Prior art and duplicates.** No entry for this file, de Neufville or Baudouin in `catalogue.json`, `research/leads.json`,
  the ledgers or any other target (the other "Neufville" entries are Villeroy and Bordeaux-Neufville). The contributor's
  searches were not repeated, except Founders Online, which was blocked as above. Not a DECODE record.
- **Corrections made in profile.json:** the three bare passages are "read in part" with the strict shares (they were
  "read" with 0.91, 0.67 and 0.71); the pooled share is 0.63; the system summary and one credit note no longer say that
  de Neufville made the code (who composed it is not shown, as stated above).
- **State.** Folder only, `Status: in progress`, as the contributor filed it. The open numbers have steps not yet tried
  (the glossed letters pp.516-548 in full, the rest of Baudouin's letters pp.487-590 for the numbers 3, 58, 143, 162,
  227, 501 and 507, and the value of 30 in Baudouin's own use), so no page is written yet.

## Follow-up to the integration check (14 Nov 2026)

Andrew Beling, with AI agents, answering the seven points of the review of pull request #587. Images are the local copies
of the National Archives Catalog frames; "on the image" below means read on a full-resolution crop by an AI agent, not by
a person.

| Point | What was done | Result |
|---|---|---|
| Read shares | retry of every open number with the enlarged key | B573 13 of 18 (unchanged), B491 10 of 16 (unchanged), B492 2 of 4 (was 1 of 4); together 25 of 38 = 66% |
| 30 | p.599 and p.605 seen on the image | 30 = "re" ("encore" = 47 30, on p.599 and in the fair copy p.605 line 4); that is its only source, a draft, not a gloss. No gloss of 30 in pp.516-548. "ar{g}ent" and "{G}rand" stay holes |
| p.608 truth | whole leaf re-read, two passes | key/p608_truth_complete.tsv: 92 groups, 23 more than the 69 of T3 (list below) |
| 136 | four more glosses | "au" on pp.516, 527, 530 and 535 against "à" once (p.599, "à Mr v. Berkel"); the key now holds "au" |
| "Lundy 7 mars" | heading of p.498 seen on the image | it reads "A Paris le Lundy 7. mars 1779" (see below); not emended |
| Dunoyer is Baudouin | Founders Online in Chrome | Baudouin as Sartine's secretary is in print; Dunoyer = Baudouin is not (below) |
| Glossed letters | pp.516-548 transcribed in full | transcriptions/glossed_pp516-548.tsv, 386 rows (310 G, 25 D after the p.529 correction of 15 Nov); held-out test 64 of 66 |

**The glossed letters in full.** Code groups occur on pp.516, 526-531, 534-535 and 547-548 only; the other pages of
516-548 were checked on the images and carry none. transcriptions/glossed_pp516-548.tsv gives every group in order, the
gloss as written, the unit, a status (G glossed, D doubtful, U unglossed, X struck) and the word. Pass 1 top-down; pass 2
on a second, larger crop of every doubtful gloss. Only G rows enter the key.
- Corrections to key/key_pairs_classB_glosses.tsv (kept unchanged as the round-3 source): the number glossed "Declaré" on
  p.516 is 474, not 574; 271 on p.526 is glossed "le" ("et le Pens."), not "la".
- New or confirmed by the glosses: 400 = oi ("d-oi[t] ordonner", "de v-oir", "l'écri-r-oi[t]-il"; three clear glosses);
  143 = vaisseau(x) (p.534, faint; read the same in both passes, and "aux vaisseaux et troupes qu'ils ont envoyés à la
  Martinique" fits); 98 = en (p.528; p.526 has "en" or "est"); 237 = y; 39 = le Roi d'Espagne; 6 = the numeral 3
  (p.529, "que dans [?] ou 3 mois": the gloss "3" stands over the figure 6; corrected on the image on 15 Nov 2026 after an
  independent verifier's check, the first transcription had "3 ou 6"; the figure before 488, first read as 3, is a tall sign
  like a long-tailed z with a small similar sign above it, not a clear 3, and is left doubtful); 43 = à; 188 = d/de; 55 = é in "l'écriroit"; 5 = M. de Chaumont.
- Unglossed groups inside glossed letters (status U): p.526 "soit [17 399 444 74]"; p.527 "[327 441 19 54 60 133] sucre
  brut" (B527 line 1), "la cause commune [204 91 133 327]" and B527 line 2; p.529 "[22 18 92 501 531] sur trois
  bâtiments"; p.530 "[100 36 85]". 501 is unglossed here too; 507 occurs only struck through (p.527).
- p.516: "si [207 66 158] & Compagnie sont chargés en tout ou en partie de cette affaire" (the supply business), glossed
  "fo/fi se aux & Compagnie". Reading it as Fizeaux & Cie of Amsterdam is inference. Papers of Benjamin Franklin 28:354 n.8
  says Georges Grand was a partner in Horneca, Fizeaux & Cie, then handling the commissioners' attempted loan. That makes
  "Grands" a natural reading of "[58]rands" in B573 ("[3] a retiré aux [58]rands l'affaire de l'emprunt"), but it is
  context, not a gloss, and 58 stays open.

**Held-out test T4** (plan in TEST_PLAN.md, written before the run; keys in key/FREEZE.txt): all glossed groups of the
letter of 10 April 1779 (pp.529-531) held out, fixed by page before any key was built. The transcriber had read those
glosses while transcribing. K4 (205 numbers) predicts 64 of the 66 covered groups (97%); 200 shuffled keys: mean 0.6,
maximum 6, none reaches 64. The two misses are word forms (474 déclaré/déclarer, 384 passe/passez). Not covered: 3, 6, 100.
After the p.529 correction (15 Nov) the held-out set is 68 glossed groups, not 69 (the doubtful sign drops out); K4 is
unchanged and still predicts 64 of 66 covered; not covered: 6 (= 3) and 100 (`results/test_round4_output_p529corrected.txt`).

**Retry of the open numbers** with the full key key_full_r4.json (208 numbers, frozen first):
- B492: 143 = vaisseau. "On a déjà proposé plusieurs fois à ma tante d'acheter son vaisseau". New word read.
- 136 = au in B573 is now the key's value, not a choice.
- No change for 3 (no gloss: the "numeral 3" of p.529 was a misplaced reading, corrected 15 Nov; it stays a hole in
  "Il y a longtemps que [3] a retiré"), 58, 227,
  369/349, 30 as "g", 162, 507, 501 and the B527 lines. The retry read nothing else new.

**p.608 truth file.** Groups on the leaf missing from heldout_p608_truth.tsv: 313 (no, "connoisse"), 60 (s, "dessous"),
11 38 141 over "écrit" (not aligned; 38 is "ru" elsewhere), 138 355 537 and 455 ("soit par vous Monsieur"), 32 290 85 60
("fermerons", partly aligned), 204 ("l'envie"), 261 310 133 ("préviendrez"), 88 74 61 230 248 164 ("je me trouve"). The
old file is kept, since it is what T3 scored. Re-scored on the whole leaf, the frozen K2 gets 81 of 83 covered groups; the
misses are 106 (Chaumont for "M. de Ch.") and 204 = "le" for "l'".

**"Lundy 7 mars 1779"** (p.498, frame 0368). On the image the heading reads "A Paris le Lundy 7. mars 1779": the day
word begins with this hand's L; the numeral has the form of the 7s in "1779"; "mars" is clear. 7 March 1779 was a
Sunday and the Monday was the 8th. The same writer's postscript of 30 March 1779 ("aujourd'huy mardy", p.516) is correct
for its date. So either the writer slipped in the day or the weekday; the image does not decide which.

**Dunoyer and Baudouin.** Checked in Founders Online (Chrome, 14 Nov 2026): Papers of Benjamin Franklin 28:353-354,
nn.8-9 (Dumas to Franklin, 5 January 1779) names "Sartine's associate Chaumont and secretary Baudouin" and cites this
file's 23 February 1779 letter; 25:366-367 n.9 calls Baudouin "Sartine's agent". A search for "Dunoyer" finds nothing on
this correspondence. So Baudouin's post is checked in print, and that "Dunoyer" is Baudouin rests on the file alone (the
index, the signatures "Baudouin" on pp.497 and 499 and the announced change of name, the same hand). Not checked: what
would settle it is a person comparing the Dunoyer hand with Baudouin's signed notes to Franklin (American Philosophical
Society, 25 December 1777, 5 and 25 May 1779) or with his office papers in the Archives nationales, Marine series B4 and B7.

## Second pass: Baudouin's other letters, pp.487-515 and 549-590 (14 Nov 2026)

Andrew Beling, with AI agents. Every page was looked at on the local images by an AI agent, not by a person; the page list
is transcriptions/survey_pp487-515_549-590.tsv.

- **What the pages hold.** 34 letters and covers from Baudouin ("Baudouin", later "Dunoyer" or a flourish), 23 February
  1779 to 13 November 1781, in clear French, plus de Neufville's drafts of 22 March 1779 (p.503) and two short drafts
  (pp.514-515), his list of signal numbers (p.504) and blank versos. Code numbers stand on three pages only: the bare
  passages already transcribed (pp.491-492, 573) and p.579, the only glossed page.
- **p.579** (letter "Ce 25", after 29 December 1780): two groups, both glossed by de Neufville, "L'approvisionnement
  [p.] la Hollande" over 68 499 473 202 226, and "par les Danois" over 537 428 326. All eight groups are in
  transcriptions/glossed_p579.tsv, a file of their own. Four of them (537, 428, 326, 68) were already in the key, from round 2
  (`key_additions_round2.tsv`) and round 3.
- **Neighbours.** The leaves before and after each bare passage (pp.487-490 and 493-494; 569-572 and 574-578) are in
  clear and carry no decipherment, draft or fair copy of the bare groups. pp.491-492 and 573 stay bare.
- **Other finds on these pages** (clear text, not readings of code):
  - p.502, 15 March 1779, same hand: "je vous adresseray ces jours cy par Dunkerque le chiffre que je vous ay promis", and
    p.507, 21 March: "lorsque vous aurez reçu le paquet que je vous ay envoyé par Dunkerque vous pourrez m'écrire plus
    librement". Baudouin says he sent a cipher by Dunkirk. Whether it is the numeric code is still not shown (it would
    point to Baudouin as its maker; see "Who made which table").
  - p.510, 28 March 1779: de Neufville glossed cover names written in clear, not numbers: "No. 14" as "de la paix
    générale" (the signal list of p.504), "la maison de commerce" as "l'Amérique", and "les parents du bon ami" as what
    looks like "l'Angl[eterre]" (doubtful).
  - p.487 (30 September 1779): "M. V. Vort ... la sortie du navire ... le vaisseau pourrira où il est". This is context for
    143 = vaisseau in B492, which rests on the p.534 gloss.
  - p.498 ("le Sr grand, qui ... sortoit de chez le ministre") and p.551 ("le Seigneur grand d'Amsterdam") name Grand in
    clear. That is context for "[58]rands" in B573, not a value for 58.
- **Held-out test T5** (plan in TEST_PLAN.md, round 5, written before the run; output results/test_round5_output.txt). The
  frozen key_full_r4.json (sha256 146207b0...f460, checked by the script) was scored on the five p.579 groups never used to
  build it (glossed and legible; 473 is doubtful and left out). It predicts 4 of 5: 68 l', 499 approvisionnement, 202 la,
  428 les. The miss is 226, glossed "Hollande" here and "même" once on p.606. 200 shuffled keys: mean 0.04, at most 1.
  Five groups are too few for a pass bar; the result is reported as it came out. **Correction (15 Nov 2026):** two of the five
  (68, 428) were already in the key from round 2 (`key_additions_round2.tsv`), so the plan's held-out set was wrong. Of the
  three pairs new to the key (499, 202, 226) it predicts 2 (226 missed); re-scored on those three, shuffles mean 0.03, at most 1
  (`results/test_round5_output_rerun_2026-11-15.txt`). Three pairs are too few to carry weight either way.
- **Rebuild and retry.** Adding the p.579 pairs left the key unchanged on 14 Nov: key_full_r5.json was byte for byte
  key_full_r4.json, because 226 ties (me 1, Hollande 1) and the tie keeps "me". That run added 68 and 428 a second time (they
  already voted through key_additions_round2.tsv; no value changed). Rebuilt on 15 Nov with the corrected files (68 and 428
  counted once, p.529 corrected): 207 numbers, sha256 ee29e9f7...2e87, differing from key_full_r4 only in 6 = 3 and no value
  for 3. None of the p.579 numbers occurs in the bare passages.
  Read shares (strict rule, as before) are unchanged: B573 13 of 18, B491 10 of 16, B492 2 of 4, together 25 of 38. No open
  number is settled: 3, 58, 227, 369/349, 162, 507, 501, 30 as "g" and the two lines of p.527 stay open. "Grands" for
  [58]rands and "Congrès" for [369/349] remain guesses from context and are not counted.

## The bare passages

Decoded with key/key_full_r3.json (204 numbers). In the readings, [n] marks a hole and {x} a unit settled by the word, not
by the key.

**B573, "Dunoyer" (Baudouin) to "Van Temmel" (de Neufville), 24 January 1780 (p.573).** 43 numbers, 39 read (91%; 38 by the key as written, the 39th being 30 = g).
The last number is 369 or 349: the middle digit could be this hand's 6 or its looped 4 (our first pass and the second
agent read 369). Either way it is a hole.
"Il est certain que le patriarche et la bande joyeuse feront tous leurs efforts pour faire avaler la dernière pilule,
mais ... cela couvrira **les États Généraux** d'opprobre et de ridicule. Il y a longtemps que [3] **a retiré aux
[58]rands** l'affaire de **l'emprunt** ... d'ouvrir **un emprunt** où personne ne se soucie de **[227]er son ar{g}ent**,
cela ne peut que faire beaucoup de tort **au crédit du [369/349]**." He then advises de Neufville to speak to "M. du Fresne".
- In English, as close as the French allows: the patriarch and the merry band will do all they can to make [them]
  swallow the last pill, but this will cover the States General with shame and ridicule. It is long since [3] took "the
  loan business" away from the [58]rands, and he has given it up since de Neufville met obstacles there. To open a loan
  in which nobody cares to [227] his money can only do much harm to the credit of the [369/349].
  - That "the loan" is the American loan de Neufville was trying to raise is inference; the letter says only "l'affaire
    de l'emprunt".
- Open numbers and candidates (holes in the text):
  - 3: a person. 3 has no gloss: the "numeral 3" once taken for its gloss (p.529) stands over the figure 6 (corrected
    15 Nov 2026).
  - 58: an initial. "Grands" fits if 58 = G, and so does 30 = g in B492 "{G}rand". The Grand family of bankers is
    meant if so; Dumas calls Georges Grand "le ch—— G——" (PBF 29:5-7 n.4).
  - 227: "plac-", "hasard-" or "risqu-".
  - 369/349: "Congrès" (context only).
- 30 is read "g" here because the word "argent" forces it; in de Neufville's drafts 30 is "re". So 30 is either a homophone
  or a writer's slip; a slip for 33 (= ge) is the simpler explanation.

**B491, the same to the same, 18 January [1780] (p.491).** 18 numbers, 12 read (67%; 86% if the four likely nulls are left out).
"Je pense absolument comme M. Leerding sur le compte du **Stadhouder** [507] [501] [405 387 390 447] **Stadhouder** ...
il se pare **à la cour** de son savoir-faire et de ses succès, qu'il ne doit qu'à **Monsieur le Pensionnaire des
Amsterdammois**."
- Pass 2 (from the end backward) corrected one number of pass 1 (206 to 204, "le").
- 405, 387, 390 and 447 are probably nulls. Each occurs in de Neufville's fair draft pp.604-605 only at places where his
  cipher has a number with no counterpart in his own plain draft, and none has a reading anywhere in the file. This is
  evidence, not proof.
- 507 also heads both unglossed lines of p.527, struck through by the writer each time, and 501 is unglossed on p.529.
  Both are open.

**B492, second page of the same letter (p.492).** 7 numbers, 5 read (71%; one unit by the word only).
"On a déjà proposé plusieurs fois à ma tante d'acheter son [143] ... il y a certainement du tripotage au sujet de **ce**
[162] entre V. Vort et **{G}rand**."
- The gloss over 143 on p.534 reads "vaisseau(x)". It was first judged too faint to enter; in the follow-up of 14 Nov 2026
  it was read the same way in two passes and entered (see above), so 143 = vaisseau: "d'acheter son vaisseau".
- "Ma tante", "le saint homme", "V. Vort", "le patriarche", "l'ami du cœur" and "M. du Fresne" are covers used in clear.
  Du Fresne is Chaumont: de Neufville glossed "Mr de Fresne" with "Chaumont" on p.579. The others are not identified.

**B527, two unglossed lines in the letter of 9 April 1779 (p.527).** Decoded to syllables but not read.
- Line 1: "[327] [441] ca do s s", followed in clear by "sucre brut et blanc, caffé &c.". "cadeaux" is possible but not
  forced.
- Line 2: "Vergennes [400] fi su ca in in s ta", followed by "au surplus". It does not parse.

## Inventory of the file (all 808 images checked at readable size)

Code numbers occur only on pp.487-609. Classes:
- (a) de Neufville's drafts with numbers over the French: pp.599, 600-603, 604-606, 608, 609. About 1,100 numbers.
- (b) Baudouin's letters glossed by de Neufville: pp.516, 526-528, 529, 530-531, 534-535, 547-548, 579. About 380 numbers.
- (c) Bare: pp.491-492, the two lines on p.527, p.573. About 90 numbers.

What this folder contains of each:
- the (a) items as aligned pairs: transcriptions/p604-606_cipher_with_p599_draft.tsv, key/heldout_p608_truth.tsv,
  key/key_source_pairs_pp600-603_609.tsv;
- the (b) glosses as pairs: key/key_pairs_classB_glosses.tsv (round 3); from 14 Nov 2026 the glossed letters pp.516-548
  in full, every group with its gloss and a status: transcriptions/glossed_pp516-548.tsv;
- every (c) passage in full: letters/B*.

p.504 is de Neufville's list of four signal numbers. 7, 8, 14 and 15 mean "Spain will declare the independence of America",
"... will go to war with England", "... will make the general peace" and "Spain will stay quiet".

## History and significance

Kept apart: what the letters say; established history, with the reference checked in this work; and inference.

**What the letters say.**
- De Neufville was passing Paris news to the Pensionary of Amsterdam. Baudouin was asking about Spanish intentions, the
  Amsterdam Pensionary and the French ambassador, and he advised on de Neufville's dealings with Chaumont ("M. du Fresne").
- In January 1780 Baudouin wrote that opening a loan nobody would put money into could only harm "the credit of
  [369/349]". That this is the American loan is inference. He also wrote that the patriarch and the merry band would make
  [them] swallow the last pill, to the shame of the States General.
- De Neufville's draft of 19 April 1779 reports that he passed news of Spain to the Pensionary and could not yet sound
  him about a direct correspondence.

**Established history (checked here).**
- In September 1778, at Aix-la-Chapelle, de Neufville negotiated a plan of a treaty of amity and commerce with William Lee,
  acting for the Pensionary and burgomasters of Amsterdam. His 1792 petition to Congress for compensation was rejected on
  Jefferson's report of 26 November 1792 (Papers of Thomas Jefferson 24:664-667, which cites Schulte Nordholt, *The Dutch
  Republic and American Independence*, 1982, pp.64-69).
- The pro-American Pensionary of Amsterdam was Engelbert François van Berckel ("notre ami" in Dumas's letters). The
  French ambassador at The Hague was the duc de La Vauguyon, the British ambassador Sir Joseph Yorke, and the Stadholder
  William V was generally pro-British (PBF 29:5-7 n.4).
- John Paul Jones's squadron lay in the Texel in October-December 1779. Yorke demanded the Serapis, and de Neufville & fils
  supplied the squadron. This file holds the letters (pp.127-345, among them Yorke's memorial of 8 October 1779 at p.299).

**Background not checked in this work.**
- Spain entered the war in June 1779.
- The British seizure of the Dutch convoy under Bylandt on 31 December 1779 - 1 January 1780 is very probably the "last
  pill" of B573.
- De Neufville's loan for Congress in 1780-81 failed. Van Winter's *American Finance and Dutch Investment* was not
  consulted.

**Inference.** A merchant's private code channel into the office of the Minister of Marine shows the French ministry
using an Amsterdam banker to work on the Amsterdam regents beside, and perhaps around, its ambassador. The letters'
worry about La Vauguyon's "confidences" (p.526 glosses) points that way. This is a reading of a few letters, not a
finding of the literature.

## Provenance (how the papers reached the government)

- **Documented:** the volume, with the index page "Diplomatic Letters" cross-referenced to "Dep. Correspondence Vol. II", was
  bound with the Continental Congress papers in the Department of State. Jefferson's 1792 report says he "examined the
  records of the Department of State". The National Archives Catalog gives no accession note. Butler's *Index to the
  Papers of the Continental Congress* (1978) indexes "Van Temmel".
- **Conjecture:** the papers came in with de Neufville's own claims, his 1792 petition or his widow's of 1797. They may
  also have been handed over earlier as intelligence "for use U.S.", as the index puts it. Neither route is documented
  here. The Journals of Congress and the American State Papers (Claims) were not searched.

## In print

One letter is cited, none is printed:
- Papers of Benjamin Franklin 28:354, note 9 (Founders Online, Franklin/01-28-02-0286) cites "a cryptic note from Baudouin
  to an unknown recipient, Feb. 23, 1779, mentioning that Stürler had arrived in Paris and had been in contact with
  someone named Montaigu. National Archives." That is p.495 of this file. The editors did not identify the recipient and
  do not mention the code.
- Nothing was found that prints the letters' text, their content or the code.

Searches made:
- Founders Online: "Neufville Baudouin" finds only Dumas's letters with the abbreviation note; "Dunoyer" and "Temmel" find
  nothing relevant.
- HathiTrust full text: "Van Temmel" Neufville finds only Butler's index. Wharton's *Revolutionary Diplomatic
  Correspondence* is full text there, and it does not match.
- Schulte Nordholt, *The Dutch Republic and American Independence*, and van Winter, *American Finance and Dutch
  Investment*: no hits for Baudouin, Dunoyer, Van Temmel or Sartine in HathiTrust's search-only view. One hit for
  "Arras" in van Winter vol. 2, probably the town, was not seen.
- Cryptiana: nothing found.

## Transcription doubts

Every number of the three bare passages was checked against the National Archives Catalog frames at integration (68 of
68 agree, frames 0428, 0363, 0364a); B491 and B573 were each transcribed in two passes (top-down and from the end).
- last number of p.573 (B573) - read: 369 or 349; checked: image, decode, second agent's transcription; the middle digit is this hand's 6 or its looped 4; both agents read 369; a hole either way
- 30 in "ar{g}ent" (B573) and "{G}rand" (B492) - read: 30 as written; checked: image, decode; 30 is clear, but its only key value is "re" (p.599, p.605); the unit is set by the word and counted as a hole
- 206 or 204 (B491) - read: 204 = le; checked: image, decode, second pass; pass 2 corrected pass 1's 206
- 224 (B573) - read: 224 as written; checked: image, decode; m in "compter" (p.600), n in "l'emprunt" (p.573), so m/n (key/corrections_post_test.tsv)
- gloss over 143 (p.534) - read: vaisseau(x); checked: image, decode, two passes; faint, read the same in both passes; carries "vaisseau" in B492
- figure before 488 (p.529) - read: left doubtful; checked: image, decode (not in any decoded passage; the key holds no value from it); a tall sign like a long-tailed z with a small sign above, not a clear 3; the gloss "3" there stands over the figure 6 (corrected 15 Nov 2026)
- 473 (p.579) - read: left out; checked: image, decode (gloss under "L'approvisionnement la Hollande"; not used by any reading); doubtful, left out of test T5

## Remaining gaps

- Numbers 3, 58, 227, 369/349, 30 as "g", 507, 501 and 162, the two lines of p.527, and the likely nulls 405, 387, 390 and 447 - blocker: open-codes; retried on 14 Nov 2026 with the glossed letters pp.516-548 transcribed in full: none is glossed with a value that fits (3 has no gloss, the p.529 "numeral 3" being the gloss of 6; 501 and 507 only unglossed or struck).
- A glossed or deciphered copy of the bare groups (pp.491-492, 573) - blocker: needs-physical-access; none is in this file (all 808 images paged; Baudouin's letters pp.487-515 and 549-590 surveyed page by page on 14 Nov 2026, the neighbours of the bare pages read, p.579 transcribed in full); Baudouin's office copies or de Neufville's sent letters may survive in the Archives nationales, Marine B4/B7, not seen. The clear text of pp.487-515 and 549-590 is not transcribed; it carries no code.
- That "Dunoyer" is Baudouin is not confirmed outside the file - blocker: needs-physical-access; needs a comparison of hands with Baudouin's signed notes (American Philosophical Society) or his office papers (Archives nationales, Marine B4, B7).

## Escalation

Checklist added at integration (14 Nov 2026), from the contributor's list below:
- [x] siblings: all 808 images of the file paged; code numbers only on pp.487-609
- [x] clear-pages: de Neufville's plain drafts and glosses are the key source; no plain text of the bare passages found
- [x] known-keys: neither table survives as a table; no other key of this correspondence is known
- [x] print: Founders Online, HathiTrust full text, Cryptiana (see "In print")
- [x] key-rebuild: three rounds (K1, K2, full key), each from more drafts and glosses
- [x] retry: the glossed letters pp.516-548 transcribed in full and every open number retried with key_full_r4 (14 Nov 2026); one new word (143 = vaisseau); second pass the same day: pp.487-515 and 549-590 surveyed, p.579 transcribed in full, held-out test T5 4 of 5, key unchanged, no open number settled

Tried for the open numbers:
- every glossed letter and draft in the file (all 808 images paged);
- the code's own thematic neighbours (names sit at 500-550, but there is no alphabetical run that settles 3, 58, 227 or 369/349);
- Founders Online, HathiTrust full text and Cryptiana.

Not tried:
- the Archives nationales Marine series (B4, B7) or Sartine's papers, where Baudouin's office copies or de Neufville's
  sent letters may survive;
- Dutch archives (the Stadsarchief Amsterdam's van Berckel papers).
