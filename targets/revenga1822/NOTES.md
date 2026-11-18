# Revenga's undated intercepted letter from Madrid (1821 proposed): the cipher passages of the "paper in fragments" (catalogue 641)

Status: in progress. Contributed by WAINUT (27 Oct 2026). Key recovered from the ciphertext alone; the text is
deciphered in part on a first-pass transcription (a dozen holes and doubtful words, about 110 slips corrected from the
sense and listed in corrections.md). The next step is a full second transcription pass on the four frames and a test
of the z sign. The site page and the ledger rows are left to the maintainer.

**Reading status (17 Nov 2026).** The profile now records decoded, not read: no accepted
`reading_review` exists for this document. The earlier 0.82 cipher-passage estimate and 0.868
mixed-text estimate remain documented as unreviewed historical figures, not accepted sure-word
read shares. No review stamp is added. The existing decode, proposed reading and frozen tests
are unchanged; a maintainer must review the sentences before the result is counted as a reading.

Catalogue 641. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the cipher was transcribed from the NARA frames with a vision-capable language model. An independent agent re-read
seven passages on the film, decrypted them with its own code and ran the controls. A second pass for this
contribution re-read three more groups, and a review re-read three more (C26, C38, C42).

## 1. The document

- **Source.** NARA RG 59, Despatches from US Ministers to Colombia, vol. 3 = microfilm T33 roll 3,
  [naId 189273979](https://catalog.archives.gov/id/189273979) (535 frames, "Apr. 14, 1823-May 1, 1826").
  Richard C. Anderson to John Quincy Adams, No. 7, Bogota, 19 Jan 1824, frames T33-03-0044 to -0047. The enclosure
  **No. 4**, "the paper (in fragments) and written partially in Cypher", is on frames
  [0055](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/T33/T33-03/T33-03-0055.jpg),
  [0056](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/T33/T33-03/T33-03-0056.jpg),
  [0057](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/T33/T33-03/T33-03-0057.jpg) and
  [0058](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/T33/T33-03/T33-03-0058.jpg).
  Frame 0057 right is headed "2o. duplicado / Al Sr. Ministro de Estado y Relacs. Exters. de Colombia", with the
  marginal "4". The text runs 0057 right, 0058 left, 0056 left, 0056 right, 0055 right. Frame 0057 left is a clear
  fragment, not transcribed here.
- **Contemporary translation.** Frames 0058 right to 0061 hold an English translation signed "W. B. H." of the
  clear parts only, with the cipher parts left blank.
- **Manning.** Manning, *Diplomatic Correspondence of the United States concerning the Independence of the
  Latin-American Nations* (1925), vol. 2, doc. 641, p. 1272. The despatch calls the item "a Duplicate of a letter
  written by Mr. Ravenga at Madrid, sent by him through France ... intercepted and opened by order of the Authorities
  there; he says that the letter of which this was a duplicate was sent through another channel and arrived in due
  time". Footnote: "Not printed. A postscript to Anderson's letter explains that no key to the cipher was furnished.
  The portions not in cipher are, alone, unintelligible." The catalogue adds that Count Landos, a French agent at
  Cartagena, handed it over in 1822.
- **Writers.** Manning names only "Mr. Ravenga". The letter says "nosotros" throughout, which fits the joint mission
  of José Rafael Revenga and José Tiburcio Echeverría in Madrid. The second name is our inference.
- **Addressee.** The Colombian Secretary of Foreign Affairs (Pedro Gual, per the catalogue).

## 2. The system and the key

The letter is in Spanish. Clear text alternates with 56 cipher groups written in ordinary lowercase letters, with no
spaces inside a group. The system is a **monoalphabetic substitution**:

- the cipher letter `a` stands for the space between words;
- the digraph `ll` is one sign and stands for plain s; `lll` is ll + l (s + t) in every case checked;
- `c` stands for plain ll (millones, millón, aquellas, vellón), because ll was taken;
- `ñ` stands for plain l.

The full table with counts is in `key.txt`. The main values (a, t, v, p, g, ll, m, e, z, b, y, l, ñ, d, o, n) rest on
dozens of occurrences. The rare values u = f, r = h, i = x and f = ñ rest on 3 to 6 occurrences each. Open: the
sign for plain z (the first pass reads g in Cádiz, pobreza, diez and forzoso), the sign for plain j (consejo,
aconsejó, ejecutivo), and whether a final z or k after a word is a stop.

**How the key was found.** No key was given and none was used. A quadgram hill-climb against Spanish statistics (a
Cervantes text) on the cipher groups, with `ll` merged into one symbol and cipher `a` removed, gave
"los dos grandes partidos republicano y realista constitucional" at once. That made `a` the space, and the rest of the
key followed. That solver script was not kept; `decrypt.py` applies the key. For the review the solver was rewritten
as `solve.py` (swap annealing from random keys against the repository's es-modern 4-gram model, word space and commas
left out, nothing taken from the key). With seed 641 and four restarts, three reach -2.87 per character and agree
with the key on 97.5-97.7 % of sign occurrences; they differ only on the rare c, f, k, n, u. The key itself scores
-2.834, above the annealer's best.

## 3. The transcription

`transcription.txt` gives the 56 groups with the clear text that follows each one. It is a **first pass**. The hand
confuses g/y/q, n/ñ, e/c, p/t and b/ll, and the first pass drops letters here and there. That explains the
misspellings in the mechanical output (`decryption.txt`). Twelve groups were re-read on the film and corrected: seven
by the independent verifier (C01, C05, C06, C07, C42, C52, C53), three in the second pass (C39 nulidad, C40 por
España, the comma after republicanos in C10) and three in the review of this contribution (C26 Argüelles with c,
C38 a line break that had been typed as a space, C42 one l too many in Prusia). The list is at the head of the file.

- **The comma-like mark.** A mark that looks like x stands where a comma belongs, after "distinguido", "republicanos"
  and "España". It is written `,` in the transcription. True x (plain b) occurs in republicano, absoluta and obrar.
- **The writers' own spelling.** "virey", "La Torre" with one r, "Argüelles" with c for ll: these are kept apart from
  misreadings.
- 2,294 sign places in all (ll counted as one sign), counted with `decrypt.signs`: 335 are the word space `a`, 3 are
  the comma-like mark and 8 are unread places. There are 28 distinct signs: 26 letter signs with a value (k doubtful), one q
  without a value (C41), and the comma-like mark.
- **gg next to c.** Next to plain c the first pass often has gg where plain i stands: every -ción comes out as
  "-ciion", and there are "ciivil", "diice", "deciidirse" (about 15 places). This may be a second i-like sign, the
  open sign for z, or a habit of the first reading. It is not settled; the reading gives the word with one i.

## 4. The reading

The text as sentences is in `reading.md` (Spanish), with the deciphered parts in «guillemets», and in
`translation.md` (English). Slips of the first pass (a dropped, added or confused letter or two, where the word is
certain from the sense and the clear text) are corrected there and each is listed in `corrections.md`; `decryption.txt` keeps the raw output. Anything
beyond that is marked `[?word]`, and what cannot be read is `[...]`.

What the letter says (five fragments):

1. **Spanish politics.** The two great parties, republican (exaltado) and constitutional royalist, are at odds; the
   republicans prepare a revolution "sangrienta y desastrosa" in Cádiz, Barcelona and on the coast. Riego's
   banishment, his later "puesto distinguido", the fall of the ministers, the Cortes' democratic measures, an
   anti-constitutional plot reported to the Cortes in secret session, and schisms in the secret society.
2. **The treasury.** The Treasury could raise only seven million reales de vellón in a week; nobody dares propose
   a new loan after the ten million duros that ruined Canga Argüelles; national bankruptcy is spoken of openly. Each
   party fears to back American independence. The Colombians try to unite the American deputies in the Cortes and,
   through an independent European deputy, to get a motion on extraordinary Cortes.
3. **The case for treating.** Fear that no one would recognise Colombia without Spain, and the view of French
   politicians and a "Madame Orloff" that Russia, Austria and Prussia had divided America among themselves, pushed
   someone towards accepting a proposal. The writers argue the opposite: the nullity of the Spanish government only
   strengthens Colombia's right, and the three powers are no real threat. They visit a man close to the ministry.
4. **Recognition and Mexico.** They hope the present Cortes will authorise the Executive to treat with them before
   they dissolve. Apodaca writes in public that there is nothing to fear, but privately that he will probably be "el
   último virey"; his wife, aunt of the Minister of Marine, says it is better to lose it single than double.
5. **Venezuela.** General La Torre (holding Puerto Cabello) asks for four thousand men and a million duros; the
   Council of State advises ships for troops; fifty thousand pesos a month are to go to him from Havana.

**Dating.** The first solver dated the letter to about September-November 1822. Two details point earlier: "acercándose
el día de San Fernando" (Ferdinand VII's saint's day, 30 May), and "antes de disolverse las presentes [Cortes]" (the
ordinary Cortes of 1822 closed at the end of June). Riego was President of the Cortes from March 1822, and La Torre
held Puerto Cabello until mid-1822. About May-June 1822 seems likelier. This is our inference; it was not checked
against the dated correspondence of the mission.

Context on frame 0055 right, read once from the frame at reduced size, not transcribed in full: before the last cipher
group the clear text describes an audience with the ministers, then visits to "el Capitán general de esta Provincia
Conde de Cartagena" (Pablo Morillo held that title; our identification) and to "el digno Arzobispo de Caracas".

## 5. Controls (`python decrypt.py --controls`)

Share of decrypted words (three letters or more) found in the repository's Spanish word list
(`lang/lexicons/es.json.gz`), over the 56 groups as transcribed:

- the key: **0.427** (on the first-pass transcription, misspellings included);
- 2,000 random permutations of the key: maximum 0.092, mean 0.003;
- 2,000 shuffles of the signs inside each group, with the true key: maximum 0.091, mean 0.040;
- the key rotated by one place, space kept: 0.042.

The independent verifier ran similar controls with its own code and word list (41.2 % against at most 10.2 % and
11.7 %).

`python docs/_validate.py revenga1822` on `validation.tsv` (es-modern, order 4): the key -2.836 per letter; 200 random
keys -7.61 (max -5.70); a key annealed onto the shuffled ciphertext at best -4.50; verdict pass.

**How much is read.** These figures show the key is right; they do not measure the reading. 2,282 of the 2,294 sign
places have a value, but that is not a share read as sense. Measured on the reading: the deciphered passages of
`reading.md` score hole rate 0.18 on `docs/_check_reading.py --file` (share read 0.82, the profile's fraction_read),
and that share includes about 110 first-pass slips corrected from the sense (`corrections.md`), not yet checked on
the film. The checker scores the whole of `reading.md` 0.586 of sentences clean. This is short of the 95 % read bar.

## 6. Prior work

- Manning (1925) prints neither the cipher, nor the clear text, nor a decipherment (checked on the archive.org text
  of `diplomaticcorres02mann`).
- One web search with Spanish key phrases (with Revenga, Echeverría, Madame Orloff, La Torre, Apodaca) found no
  printed text.
- **Not checked:** Bogotá received the original by another channel and must have read it with its own key. The
  plain text may therefore be in the Archivo General de la Nación, Bogotá (Sección República), in the Archivo
  Santander, in Blanco and Azpurúa, or in Zubieta, *Apuntaciones sobre las primeras misiones diplomáticas de Colombia*
  (1924). We claim only the decipherment of this intercepted NARA copy, not that the content is new.

## 7. Second transcription pass (Andrew Beling, with AI agents; work of 12 November 2026, added 17 November 2026)

This is the next step named at the head of these notes: a full second transcription of the cipher on frames
0055-0058 and a test of the z sign. Files in `second_pass/` (its README lists them). The sections above, and
`transcription.txt`, `reading.md`, `corrections.md`, `decryption.txt` and `key.txt`, are left as they were; where this
pass disagrees with them, it is said here.

**How it was done, and what is blind.** An AI agent transcribed all the cipher and the clear text from the four
frames without sight of any key, decryption or earlier transcription; its files were hashed when it finished and are
copied unchanged (`second_pass/blind/`). Then one AI agent, which could see both transcriptions and the key, went
through every place where they differ and settled each on the frame. **The transcription was blind; the settling of
the differences was not.** No person has checked any of it.

**Result.**

- The two transcriptions agree on 2,261 of 2,532 alignment columns (0.893; reproducible recount below). The earlier collation separately lists 231 entries: 200 where they
  differ and 31 where they agree only on a doubtful or alternative reading. 112 were settled on enlargements of 3 to
  6 times, 119 on line strips at about 1.5 times (the weaker settlements, mostly 0056 left lines 5-17, 0056 right and
  0055 right). By method: 171 by the letter shape, 45 from the sense, 15 left open. In 5 further places both
  transcriptions read alike and the frame shows otherwise (a third l in costa, e not a in presentes, a third stroke
  in ministros, n not m in porque, a tilde-marked sign read as ñ in sólo). Each place, with frame, line, both
  readings and what the frame shows: `second_pass/collation.tsv`. The settled text: `second_pass/transcription_settled.tsv`.
- **The 108 corrections of `corrections.md`, checked on the frames** (`second_pass/corrections_check.tsv`): **44
  confirmed** (the frame has the corrected letter; the first pass misread it); **35 are the writer's own slips** (the
  frame has what the first pass read, e.g. sangrienta written `blvesmgpelv`, sesión as `sasion`, secreta as `sireta`;
  the correction stands as an emendation of the writer, not as a reading of the frame); **29 mixed** (about 14 partly
  confirmed with a writer's slip left, about 11 other writer's slips, 4 now holes or open: al primero, bancarrota in
  C34, cincuenta, sobre).
- **The z sign** (`second_pass/z_sign_test.md`): plain z is written with `g`, the sign of plain i, in all four places
  (Cádiz, pobreza, diez, forzoso); both transcriptions read g there and no other sign is used for z. So "cadii",
  "diei", "pobreia" and "forioso" in `decryption.txt` are what the writer enciphered, not misreadings. **The j sign** is
  a w-like double loop (read `w` by the blind transcription in Ejecutivo and mejor), close to u = f; it is not in
  `key.txt`. A final z (often) and k (rarely) stand where a stop or comma belongs; inside words z is plain d. The
  doubled g before -ción is on the frame (8 of the 10 places): the writer's habit, not a misreading.
- **The fragments.** The last cipher run of 0057 right continues on the first line of 0058 left (B18 = C17 + C18):
  fragments 1 and 2 of `reading.md` are one text, and its "[page ends; continuation not on film]" does not hold. The
  end of 0058 left ("y concebimos ya esperanzas de que") runs on to the start of 0056 right ("se conseguirá que ...
  definitivamente con nosotros"): the contemporary English translation (frame 0060 right) puts the two clauses together,
  before the Apodaca paragraph. On that translation the order is 0057 right, 0058 left, 0056 right, 0055 right, then at
  least the second paragraph of 0056 left, against the order 0057R, 0058L, 0056L, 0056R, 0055R given above. Where the
  opening of 0056 left belongs is not settled. This order is the translator's; it is evidence, not proof of one
  continuous original.
- **The date.** The clear fragment on 0057 left (another, upright hand) has the Minister of State showing a letter of
  Zea's "fecha en Bayona el 3o. del corriente" (blind reading). The numeral is not secure: one figure, then a small
  raised circle and a dot; a second look read it as 5. Read it as "el [3/5?]º del corriente". It gives no month or
  year, and that the fragment belongs to this letter is not shown (it is not in the English translation). It does not
  date the letter.
- **Readings that change** against `reading.md` (from the settled letters unless marked "from the sense"): "continúan
  como antes" for "como an[...]" (from the sense; the end of B01 is ambiguous on the frame); B38 "se [?haga] la moción
  sobre Cortes extraordinarias; si la perdiere, [struck] propondrá" for "[...]" (from the sense); B42 "Madame Orlof",
  one f; B49 "una carta, en que [...]" for "una [...]" (`gvml` = carta with g for y; from the sense); B50 "obrará"
  without the query (from the sense); B55-B56 "se está pagando aún [...] un millón y medio de duros, que costó
  [?plantear] aquí el presente sistema" for "se está [?tratando] aún de [?preparar] ... que cos[...]"; in the clear
  text "nos es de suma entidad" for "utilidad" (blind reading, not looked at again). Unchanged and still from the sense:
  [?cuartel], [?Andalucía], the King's action in B23, B19 "de [...]", the holes in B54-B56.
- **Open: 15 places** (`second_pass/open_places.tsv`): signs under ink blots in B24, B29, B33, B34, B47, B49 and
  B55-B56; a struck-out passage in B42; signs that the shape does not decide, n or m (B23), c or e (B29), z or s
  (B42), eg or gz (B49), z or r and v or u (B55-B56); and the sheet edge cutting the end of B54. A second look at
  the full frames closed none of them; another exposure of the film or the original received in Bogotá would be
  needed.

**Prior print.** As section 6 says, Manning (1925) prints no text of the enclosure, and no printed decipherment is
recorded; this pass changes no reading against a printed text. It was not searched again.

**What this does not do.** It does not recompute `fraction_read`, the controls or the validation on the settled text,
and it does not change `transcription.txt` or `reading.md`. The later profile status correction above
withdraws the unreviewed reading claim; it does not rerun or revise the decipherment. The z and j signs are not added to
`key.txt`.

## Remaining gaps

- The transcription is a first pass (44 of the 56 groups read once; about a dozen words doubtful or open: an[...], cuartel, remoción, Andalucía, the end of C17, C18-C19, the King's action in C23, C36, C38, C43, C49, C50, the person addressed in C53, La Torre's verb in C54, C55-C56; about 110 slips corrected from the sense, listed in corrections.md) - blocker: not-attempted; the frames are public, and a full second pass on the four frames should settle most of them and confirm or undo the corrections.
- The signs for plain z and plain j, and the role of a final z or k - blocker: not-attempted; plain i stands where z is expected (cadii, diei, pobreia, forioso, uatoriien), so gg or g is the candidate z sign, and the key table runs in blocks (a b c d -> v x y z; m n ñ -> d e f; o p q r s t -> p o n m ll l; v x y -> j i h) that predict z -> g; to be tested on the film in the second pass.
- The clear fragment on 0057 left and the clear paragraphs of 0055 right and 0056 right are not transcribed - blocker: not-attempted; part of the second pass.

## Escalation

- [x] siblings: no other letter in this cipher has been found; Revenga's other letters (AGN Bogotá, Archivo Santander)
  are not online
- [x] clear-pages: the clear text frames every group, and Hodgson's English translation (0058-0061) confirms the clear
  parts; it leaves the cipher blank
- [x] known-keys: no Colombian key of 1822 is known in the repository (no Revenga entry); not needed, the key was
  recovered
- [x] print: Manning vol. 2 checked; Zubieta and the Colombian collections not checked
- [x] key-rebuild: the key is complete for the common letters; z and j open
- [ ] retry: a full second transcription pass on frames 0055-0058, with the z test (not yet done; the reason for "Status: in progress")

## Files

- `transcription.txt`: the 56 cipher groups with the clear text after each, frame by frame
- `decrypt.py`: the key, the decryption, the controls and the validation pairs (`--pairs` writes `validation.tsv`; standard library)
- `solve.py`: ciphertext-only key recovery (swap annealing against the repository's Spanish 4-gram model); rewritten for the review, as the first solver's script was not kept
- `validation.tsv`: one cipher sign per line with its value, for `docs/_validate.py` (verdict: pass)
- `decryption.txt`: output of `python decrypt.py`, group by group
- `reading.md`: the text as Spanish sentences
- `corrections.md`: every first-pass slip corrected in reading.md, group by group
- `translation.md`: English translation
- `key.txt`: the key with counts
- `second_pass/`: the second transcription pass of 17 November 2026 (section 7): the blind transcription, the
  collation of every difference settled on the frames, the settled transcription and its decryption, the check of
  corrections.md, the z-sign test and the open places

## 14 Nov 2026: reading review recorded

`reading.md` was read as sentences against `decryption.txt` and `corrections.md`, and `translation.md` against the reading
(Claude, session of 14 Nov 2026). The Spanish is coherent in all five fragments and the translation is complete with the
same holes. `reading_review` grade B recorded in `profile.json` (coherent, but the mechanical decode is raw and the
reading normalises about 110 words from the sense, listed in `corrections.md`, none checked on the film). State stays
read in part (read_share 0.868). The second transcription pass on the four frames (Remaining gaps) was not done.

## Reproducible agreement recount, 17 November 2026

The earlier 2,293/2,532 (0.906) figure did not preserve an executable counting rule and is withdrawn as a sure-agreement measure. The reproducible recount is 2,261/2,532 = 0.893. Each ll is two characters. Join B10+B11 against C10, B18 against C17+C18, and B55+B56 against C55+C56; otherwise use the documented B/C group correspondence. Within each joined group use minimum unit-cost edit distance; ties take diagonal, then deletion from the second sequence, then insertion. Align first-choice letters, but count a match only if both letters are unmarked and identical. A question mark makes its preceding letter doubtful; x|y is one doubtful position; a bracketed annotation is one unresolved placeholder (x in [x?] is a doubtful first choice); periods and spaces are excluded, comma-like cipher signs retained. Insertions, deletions, doubtful agreements and unresolved placeholders remain in the denominator. Unknown-length struck spans represented by one placeholder make this an operational alignment denominator, not a certified count of manuscript signs. The first-choice recount including doubtful equal letters is 2,288/2,532, also not the old 2,293. No key, decode, or settled transcription enters this recount.

The four words with expected z support the proposed g value; they are not an independent test. The z-sign hypothesis step is partial.

AI agents did this work; no person has checked it.

The earlier collation lists 231 entries (200 disagreements and 31 doubtful readings); that historical count is not the remainder of this new alignment. The new alignment has 271 non-sure columns: 244 unequal first choices and 27 doubtful equal choices.

## Dating correction proposed after Brice’s review

Brice’s comment on PR 764 (https://github.com/dbourdeau/cyphersolver/pull/764#issuecomment-6955975760) proposes May–June 1821 rather than 1822, citing the Madrid mission and the reference to Apodaca. The earlier May–June 1822 argument above is retained as the history of an unconfirmed inference, not an established date. The 1822 handover date does not itself date the intercepted letter. The profile now records the year as unknown and the 1821 proposal explicitly. No new archival dating evidence was obtained, and the historical target folder name is unchanged.

AI agents did this work; no person has checked it.
