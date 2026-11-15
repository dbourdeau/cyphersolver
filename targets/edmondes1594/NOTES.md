# Thomas Edmondes to an unnamed lord, camp before Laon, 9 July 1594: the cipher printed undeciphered in HMC Salisbury IV, pp. 559-560

Status: in progress (folder only, no page). Read in part: the cipher is read from the 1892 print, with the manuscript
unseen. 636 of the 651 printed cipher letters are read (97.7%); by words, 130 of 135 cipher words, or 130 of 147 when the
12 occurrences of the undeciphered person signs and figures count as holes (0.884, the figure in profile.json). Key
recovered from the ciphertext alone, frozen and tested on held-out letters; a second agent solved it independently.
Contributed by Andrew Beling, with AI agents (14 Nov 2026). Nothing has been checked by a person.

## 1. What it is

The Historical Manuscripts Commission's *Calendar of the Manuscripts of the Marquis of Salisbury*, part IV (1892),
pp. 559-560, prints a letter headed "[Thomas Edmondes] to ——", dated "From the Camp before Laon, 9 July 1594",
"Unsigned. Endorsed:—'Mr. Edmunds.' 2¼ pp." It is in the Cecil Papers at Hatfield House (the calendar gives no
volume or folio). Edmondes was the Queen's agent with Henri IV. The letter is in clear English except for 16 runs of
cipher letters, 651 letters in all, which the editor printed as letters and left undeciphered, and several signs for
persons, which the editor printed as cuts (facsimiles) or figures. The volume's index has "Cipher letters
undeciphered; 484, 559" and "Cipher used by Mr. Edmunds; 559". The letter speaks of "yor L." commandment, so it is
addressed to a lord, who is not named. Lord Burghley remains possible (the letter is in the Cecil Papers, and its lord
is to sound the Queen), but he is no longer "very probable": that rested on The National Archives' catalogue entry
"Edmondes to Burghley" of the same day, which belongs to a different letter (section 6), and Edmondes's cipher passages
to Burghley of 13 and 23 July 1594 (SP 78/33 ff. 349v and 366) are in signs and figures, not this letter cipher.

Images: Internet Archive, item [11576077bsb](https://archive.org/details/11576077bsb) (Bayerische Staatsbibliothek
copy), leaves 581-582. `images/p559_cipher.jpg` and `images/p560_cipher.jpg` are crops of the cipher passages from those
leaves, kept as the evidence for the printed cipher letters (250 KB and 136 KB). Rights: the volume was printed in 1892
(Historical Manuscripts Commission, *Calendar of the Manuscripts of the Marquis of Salisbury*, part IV) and is in the
public domain; the crops show only the printed page. No other image is committed.

Not to be confused with catalogue 1003, the anonymous French cipher letter of 28 Feb 1594 on p. 484 of the same volume,
whose cipher is not printed; or with [`targets/stowe166/`](../stowe166/), Edmondes's own papers in the British Library,
whose cipher is a different sign alphabet.

## 2. Transcription

- `transcription/calendar_entry.txt`: the whole printed entry, clear text and cipher in place, with the person signs as
  the calendar prints them: {55} (a cut like a handwritten "55", twice), {m_} (a cut like a script m with a hooked
  underline, twice), {ho} (a barred "ho", once), {oo} (a different looped cut, once), and the figures 4s (once), 300
  (twice) and 26 (three times) set in ordinary type.
- `transcription/pass1.txt` and `pass2.txt`: the first agent's two passes (top down, then from the end), identical.
- `transcription/verifier_blind.txt`: a second agent's transcription, made from the same images before it opened the
  first agent's files. **The two transcriptions are identical on all 651 cipher letters.**
- `transcription/cipher_letters.txt`: the 651 letters by segment (labels A1-A12 on p. 559, B1-B2 on p. 560).
- The roman "to" in "m a p m a to b d d" (p. 559) is set like an English word; it reads as two cipher letters (t = e,
  o = w: "that he will"). It is not in the 651. (The second agent's report says its 651 includes this "to"; its
  transcription file does not, and the two files are equal letter for letter without it.)
- The second figure on p. 559 is **300**, not 800 ("he desireth me to advise and resolve him how 300 doth affect"):
  checked on the image here; the same type form as the first 300. An earlier draft and the Internet Archive text had 800.
- What the print loses (inferred from the reading, not seen on the manuscript): any mark that told the homophones
  apart; word division (the tight groups are typesetting and cut across words); a few misreadings of a secretary hand
  (g and q confused both ways, n printed as u, u as v).

## 3. The key

- Alphabet: the 24 letters a-z without j and v. **Base: the alphabet shifted 7 places**, cipher a = plain h, b = i,
  ... m = t, s = a, x = e ("the" = m a x or m a w). 490 of the 636 read letters take the base value.
- **Extra equivalents** for frequent plain letters come from the same alphabet shifted 8 and 10 places, occasionally
  11 and 20: e is written x, w, t, s or i; a is s, p, r, o or e; d is w, s, h, r or v; c is v, r, g; f is y, k, x, v.
- So several printed letters carry two or three values, chosen by context: s = a, d or e; r = a, c or d; o = w or a;
  p = a or b; t = e or b; w = e or d; x = e or f; k = r or f; g = o or c; e = m or a; h = p or d; v = c, f or d.
  Printed i is e in all 17 places, never its base q. Full counts per printed letter, with the shift each value
  needs: `keys/key_table.tsv`.
- Printed u is read as cipher n (except once, in "comandinge"), printed v as cipher u.
- Single values off the scheme, probably misprints: printed g = y in "by" (read as a misprinted q), printed q = o in
  "gouuernor" (a misprinted g), printed c = m in "some", printed e = e once, printed r = r once.
- Nomenclator: the cuts and figures above stand for persons or states; none is deciphered.
- Stafford's cipher with Burghley "allowed for three different options of alphabet" (Tomokiyo, Cryptiana, citing
  Daybell); this looks like the same family. That is a parallel, not evidence about this key.

## 4. Frozen key and held-out tests

Written before the run: `tests/PREREGISTRATION.md`. Scripts in `scripts/`, outputs in `tests/`.

1. **The first agent's test.** Training: segments A1-A9 (350 letters); held out: A10-B2 (301 letters). The three shifts
   were chosen on the training letters only, by scoring all 2,024 sets of three shifts with a quadgram model of 1590s
   English: (7, 8, 10), -4.082 against the runner-up (4, 7, 10) at -4.092 (`tests/heldout_freeze.txt`). Frozen as
   `keys/frozen_key.json`, **sha256 70077576e3a9d501cb088b07203d26ccdb9e45f1136fb64d8c107a61fab3ce6f**, before the
   test. Result (`tests/heldout_test.txt`): held-out score **-4.0950** per letter; 200 keys made by shuffling the
   frozen key's value-sets among the cipher letters: maximum -4.6513, median -5.1542; **0 of 200 as good**. The
   held-out machine reading, with no hand help, has declare, profession, relligion, cause, assure, assistance,
   army, under, byron.
2. **The second agent's stricter variant** (`scripts/stricter_heldout.py`, `tests/stricter_heldout.txt`). The first
   test's controls destroy the shift-7 base, and that base was first noticed on the whole text. So all three shifts,
   base included, were chosen blind on one half: on the first 350 letters the choice is (7, 8, 10), which then **ranks
   1 of 2,024** sets on the last 301 letters; chosen on the last 301, the choice is again (7, 8, 10), and it ranks 1
   of 2,024 on the first 350. With base 7 fixed, the extra pair (8, 10) is chosen on either half and ranks **1 of 231**
   pairs on the other (held-out -4.0950 against a median pair at -4.7047; reversed -4.0820 against -4.4512).
3. **Rerun at packaging** (`tests/rerun_packaging.txt`): both tests rerun from this folder give the same numbers to
   the last digit. The language model is rebuilt by `scripts/lm.py` from `corpus/` (Stevenson's *Correspondence of
   Sir Henry Unton*, Roxburghe Club 1847, Internet Archive `cu31924027964471`, and Edmondes's clear letters in Butler
   1913, pp. 141-147); the rebuilt `lm4.json` is byte-identical to the one used (sha256 9513a2ab...cf26). Run
   `python3 -I scripts/lm.py` first (the model files are not committed), then `python3 -I scripts/heldout.py test`
   and `python3 -I scripts/stricter_heldout.py scripts`. Do not run `heldout.py freeze`: it rewrites the frozen key.
4. The score cannot choose the occasional shifts 11 and 20 (a fourth or fifth shift helps any set about equally:
   `tests/scan_quads.txt`, `tests/scan_fivesets.txt`); they rest on whole words read by hand ("neighbourhoode",
   "places", "Poictou", "anie necessitie", "towardes", "being").
5. `docs/_validate.py`: verdict **not applicable** (12% of read letters differ from their printed letter's commonest
   value, over the validator's 10% limit for a polyphonic reading; reading -2.986 per letter, en-1640s). The cipher is
   polyphonic by design, so this test does not apply; the held-out tests above are the statistical check.
   `validation.tsv` is the token-by-token alignment.

The model in `scripts/lm.py` is this target's own and not one of the repository's `lang/` models: the tests were run and
frozen with it, so it is kept as it was.

## 5. The reading

`reading/reading.md` (the whole letter, cipher reading in bold), `reading/decryption.txt` (letter by letter),
`reading/modernized.md` (modern English of the cipher passages in context), `reading/reading_hand.tsv` and
`reading/reading_words.tsv` (the reading aligned letter for letter; checked by `scripts/check_hand.py`). Marks:
° the word rests on a value chosen by sense (67 of 130 words: the printed letter has more than one value and here takes
a less common one, or has no dominant value); † weak (4 words and "he will"); ? a letter not read (15).

**Unread**: A2 "a d m" and "g k l" (6 letters), A11 one letter and five letters (6), B1 "goo" (3). **Weak**: "by"
(needs printed g to be q), "gouuernor" (printed q for g), the "relligion" of the governor's sentence (printed r = r),
"some" (printed c = m), "that he will" (takes the roman "to" as cipher), "(v)ehement" (from "ehement"; the second
agent offered "adhement" from the same letters; neither is secure).

The second agent's own reading agrees word for word with this one outside the spans both mark weak or unread
(A2, A9 "by", A11's opening). Its corrections are applied here (section 7).

### What the letter says

Kept apart: what the clear text says, what the cipher adds, and what is inference.

- **Clear text.** The Duke of Montpensier, ordered back to Brittany after Sir Roger Williams's negotiation, "hath used
  earnest instance towards 55 to accompany him thither to assist him in that service". Montpensier pressing 55 to go
  to Brittany is in the clear text, not the cipher.
- **Cipher, Montpensier's reason.** Because of "the many occasions [needing his presence in Normandie]" he "shall not be
  able also [to hould ??? gouuerment ???]", so he would "[only make a iourney thither to install him therin]". The
  Normandy reason is Montpensier's own, not 55's.
- **Cipher, 55's case for Brittany** ("for argument of utility"): Brittany could "[hould correspondencie wth us]"; it
  has 4s on one side and on the other "[those of the relligion of Poictou]"; once planted there he could "[gett some
  porttownes into his handes to geiue us footing]" and hoped for "[places uppon the riuer]".
- **Cipher, "inducements of facility"**: he is desired by the country; "the gouuernor of Rhenes hath promised him as
  soon as he shall be arrived there [that he will declare himselfor the relligion, wherof he hath long since made
  seceret profession]" (the cipher letters give "himselfor", one f for "himself for"; "will" depends on the printed
  "to" being cipher); some have given him assurance; he can count on "[the succors of Poictou in anie necessitie]".
- **Cipher, the request for help** is 55's, not the governor's: "and hopeth that I will for the love they bear him
  [extend themselfes also to som assistance towardes him]". The clear text goes on: "But yet for that 300 that is only
  capable to preserve that country ... he desireth me to advise and resolve him how 300 doth affect and will yield to
  embrace the succouring thereof".
- **Cipher, p. 560.** Asked whether he would serve in the coming war in Artois and Hainault instead, 55 answered that
  "[the the mareshal of Byron] hath taken such a possession [??? gouuerninge the army under] 26" that 26 will not cross
  him, and would rather employ 55 in Luxembourg; Edmondes finds he will not stay at court "so long as the other hath
  the vogue of [comandinge the army]". "the the mareshal of Byron" needs no extra values at all.

### Sign 55 and the other signs (inference)

- **55: probably the duc de Bouillon** (Henri de La Tour d'Auvergne, Marshal of France, a Protestant), by content
  only: a Protestant grandee courting "those of the relligion" and a secretly Protestant governor, a rival of Biron for
  the command of the army, offered employment in Luxembourg. The second agent puts it at about four chances in five,
  against the comte de Soissons (Catholic, no Poitou following), Marshal d'Aumont (already the King's commander in
  Brittany, Catholic) and Claude de La Trémoille (Protestant, Poitou, but no Luxembourg role or rivalry with Biron).
  Sign 55 occurs nowhere else in the volume. It is printed [55] in the reading, not replaced by a name.
- 26 is probably the King (Biron governs the army "under 26"; "26 careth not to contradict his humour"). 300 is
  probably England or the Queen ("only capable to preserve that country"). 4s is Normandy or Montpensier's
  government, or a person (the one side of Brittany, Poitou the other). The m-sign, ho-sign and oo-sign are not
  identified. All of this is inference from content.

## 6. Who read it before, and what we add

- **1594.** No decipherment of 1594 is known. The National Archives' catalogue (Discovery, record C7318548) lists
  **SP 78/33 item 170, folio 345: "1594 July 9. Edmondes to Burghley, and copy."** An earlier state of these notes
  called it "very probably the same despatch" and its copy a decipherment. It is neither. SP 78/33 ff. 345-346 is **a
  different letter of the same day**, signed by Edmondes and addressed to Burghley, three pages wholly in clear (the
  siege, Mayenne's peace terms, general news), with no cipher, no sentence in common with this letter and no mention
  of it; ff. 347-348 is a clerk's copy of that clear letter, not a decipherment. So no word of this reading is
  confirmed or contradicted by a parallel text.
  How it was read: from the copy saved on site at the Library of Congress on 14 November 2026 in State Papers Online,
  by AI agents in two independent passes. No person has checked it. The images are licensed and are not included here.
- **Later.** No later reading of this cipher found in: HMC Salisbury IV (the letter itself; index), V, XIII and XIV
  (Internet Archive texts); Birch, *Memoirs of the Reign of Queen Elizabeth* (1754); Birch, *Historical View of the
  Negotiations* (1749; checked upstream in Sept 2026); G. G. Butler, *The Edmondes Papers* (Roxburghe Club, 1913), which
  prints Edmondes's letters of 4, 20 and 30 June and 23 July 1594 but none of 9 July; Tomokiyo, *Cryptiana*
  (Elizabethan ciphers page); DECODE (only the Stowe 166 records).
- **Print summary: none found.** The *List and Analysis of State Papers, Foreign Series, Elizabeth I*, vol. 5 (July
  1593 - December 1594, ed. R. B. Wernham, 1989) was read in part (the list entries for these letters and pp. 236-246,
  from pages saved at the Library of Congress on 14 November 2026; by an AI agent, not checked by a person): it does
  not summarize this letter. Its Brittany section was not seen.
- **What we add:** the reading of the cipher as the Cecil Papers text prints it, and its key (the base shift and the
  extra equivalents). This is a solution from the cipher alone; no decipherment or clear copy of this letter is known.

## 7. Corrections from the independent check (14 Nov 2026), applied here

- The second figure on p. 559 is 300, not 800.
- Montpensier pressing 55 to go to Brittany is in the clear text, not the cipher.
- The Normandy reason is Montpensier's ("only make a iourney thither to install him therin"), not 55's.
- The request for assistance ("extend themselfes also to som assistance towardes him") is 55's, not the governor of
  Rennes's.
- 55's identification is by content only and is printed [55].
- The person signs {ho} and {oo} are two different cuts (the first agent's description; the second had lumped them).

## 8. Context (references as checked; letter, history and inference kept apart)

- **The siege of Laon.** Henri IV besieged Laon, held for the League with a Spanish garrison, in the summer of 1594;
  the garrison capitulated on 22 July 1594 (French Wikipedia, "Laon", citing S. Martinet, *Le Siège de Laon sous Henri
  IV, 1594*). Edmondes dates in the English style, so 9 July is 19 July in the French calendar, before the capitulation;
  the letter speaks of "this siege ended" as still to come. His letters of 20 June and 23 July (Butler nos. LXIV, LXVI)
  frame this one.
- **Montpensier.** Henri de Bourbon, prince de Dombes, then duc de Montpensier (1573-1608), had commanded for the King
  in Brittany before 1592 and became governor of Normandy on his father's death in June 1592 (English Wikipedia, "Henri,
  Duke of Montpensier", citing Harding 1978). That fits the letter's "return ... into Brittany" and his "occasions
  needing his presence in Normandie".
- **Bouillon and Biron.** Henri de La Tour d'Auvergne, duc de Bouillon, Protestant, Marshal of France from 1592; Henri
  IV and the Dutch campaigned against Spanish Luxembourg in 1593 and 1595 (English Wikipedia, "Henri de La Tour
  d'Auvergne, Duke of Bouillon"). The "mareshal of Byron" in 1594 is Charles de Gontaut, duc de Biron (1562-1602),
  Admiral of France from 1592, who traded that title for Marshal two years later; his father, Marshal Armand de Biron,
  had been killed in 1592 (English Wikipedia, "Charles de Gontaut, duc de Biron", citing Jouanna 1998). Edmondes's
  20 June letter has Bouillon arriving at the camp with 500 horse (Butler).
- **Brittany.** The Duke of Mercoeur held most of the province for the League with Spanish help; Marshal Jean d'Aumont
  commanded for the King there from 1593 until killed in 1595 (English Wikipedia, "Jean VI d'Aumont", citing Harding
  1978); English troops under Sir John Norris served there from 1591 to 1594 (English Wikipedia, "John Norris
  (soldier)"). On 3 October 1594 the Queen was still waiting on Montpensier's going to Brittany (Wolley to Cecil, HMC
  Salisbury V, pp. 1-2).
- **The governor of Rennes in 1594: René Marec de Montbarot.** French Wikipedia's "Liste des gouverneurs de Rennes"
  gives him as captain and governor of Rennes from 1583 to 1605 (citing the *Bulletin* of the Société archéologique et
  historique de Nantes, vol. 24, 1885), and G. Py-Patinec, *L'armée royale en Bretagne* (master's thesis, HAL
  dumas-02176647, 2019, PDF p. 99), has him named lieutenant of the King for the bishopric of Rennes from 1593 and
  pushed out of Rennes when Mercoeur entered it at the start of the war. So the governor of the letter is very probably
  Montbarot. **His secret Protestantism is the letter's claim (from the cipher); no reference found here says he was a
  Protestant**, and none was looked for beyond these.
- **Why it was enciphered** (inference): a Huguenot duke's plan to take a command in Brittany with Protestant backing
  from Poitou, the promise of port towns to the English, a royal governor's secret religion, and an unflattering
  account of Biron's hold on the King's army were exactly what could not be risked in an intercepted packet.

## Reading review

Preliminary. `CONTRIBUTING.md` (14 Nov 2026): a reading merges only with a `reading_review` graded A or B,
"recorded by the reviewer, not by the author of the reading". The grades in `profile.json` (1 entry) were
written by Andrew Beling's own AI agents and are kept as preliminary grades: `by` is "Author's agents (Andrew
Beling, with AI agents)" and each note begins "PRELIMINARY: author's self-check, not a reviewer's grade. For a
maintainer to confirm or replace.", followed by the agents' own reading note. No grade letter was changed.

## 9. Limits, and what would finish it

- Read from the 1892 print; the manuscript in the Cecil Papers is not seen. The print may hide marks that separate the
  homophones, and the editor misread some letters (g/q, n/u).
- 15 letters unread; 67 words rest on a value chosen by sense and 5 are weak.
- The person signs are not deciphered; their identifications are inference.
- There is no second witness. SP 78/33 ff. 345-348 is a different letter of the same day, in clear, with its clerk's
  copy (section 6), and the *List and Analysis* vol. 5 (list and pp. 236-246 read) does not summarize this letter; its
  Brittany section was not seen.
- What would finish it: **only the Hatfield manuscript can check the reading**: the **Cecil Papers images** (ProQuest's
  Cecil Papers collection, or a copy ordered from Hatfield House) for the reading as a whole, the homophone marks and
  the 15 unread letters.

## Remaining gaps

- 15 printed cipher letters not read (A2 6, A11 6, B1 3) - blocker: needs-physical-access (the Hatfield manuscript; the print may misread them)
- person signs 55, the m-sign, ho-sign and oo-sign, and the figures 4s, 300, 26 (12 occurrences) - blocker: no-key-material (one letter, no key or decipherment seen)
- values chosen by sense, the printed "to" as cipher, and the assumed g/q and n/u misreadings - blocker: needs-physical-access (only the Hatfield manuscript can confirm them)

## Escalation

- [x] siblings: the volume's other Edmondes letters (pp. 371, 620, 622) have no cipher; p. 484 is a different, French cipher letter with no cipher printed; SP 78/33 has despatches of 13, 23 and 31 July 1594: the cipher passages of 13 and 23 July (ff. 349v, 366) were seen and are in signs and figures, a different cipher, so they are not siblings; 31 July not seen
- [x] clear-pages: the manuscript is not online; SP 78/33 ff. 345-348 was read (copy saved at the Library of Congress, 14 Nov 2026): a different letter of the same day, in clear, with its clerk's copy; no clear copy of this letter is known
- [x] known-keys: Stowe MS 166 (Edmondes's sign alphabet), Unton's 1591 cipher, and the upstream Maisse, Mornay, Champagne, Walsingham and Wotton keys compared; none fits (`keys/keys_tested.md`); the key is a shifted-alphabet letter cipher built here
- [x] print: HMC Salisbury IV, V, XIII, XIV; Birch 1749 and 1754; Butler 1913; Tomokiyo; DECODE; List and Analysis vol. 5, list and pp. 236-246 read (no summary of this letter; Brittany section not seen)
- [x] key-rebuild: all 2,024 three-shift sets scored; fourth and fifth shifts tested; shifts 11 and 20 added from whole words
- [x] retry: every unread span retried by two agents independently with the full key; the second agent's alternatives recorded (A11 "adhement")

## Files

- `transcription/`: `calendar_entry.txt` (whole entry), `pass1.txt`, `pass2.txt`, `verifier_blind.txt`, `cipher_letters.txt`.
- `keys/`: `frozen_key.json` (the frozen held-out key), `key_table.tsv` (values per printed letter with counts and shifts), `keys_tested.md` (outside keys compared; its paths `../scan_triples.txt` and `sources/raw/...` refer to the working folder: here `tests/scan_triples.txt` and `corpus/`).
- `tests/`: `PREREGISTRATION.md`, `heldout_freeze.txt`, `heldout_test.txt`, `stricter_heldout.txt`, `scan_*.txt`, `rerun_packaging.txt`.
- `reading/`: `reading.md`, `decryption.txt`, `modernized.md`, `reading_hand.tsv`, `reading_words.tsv`.
- `scripts/`: `lm.py`, `poly.py`, `multishift.py`, `scan_triples.py`, `heldout.py`, `stricter_heldout.py`, `check_hand.py`, `make_reading.py` (builds `key_table.tsv`, `decryption.txt`, `validation.tsv`).
- `corpus/`: the two public-domain texts the language model is built from.
- `images/`: crops of pp. 559 and 560 from the Internet Archive images (1892, public domain).

## Sources

- Historical Manuscripts Commission, *Calendar of the Manuscripts of the Most Hon. the Marquis of Salisbury ... at
  Hatfield House*, part IV (London, 1892), pp. 559-560 and index; Internet Archive 11576077bsb. Part V (1894),
  pp. 1-2: Internet Archive calendarofmanusc05grea_0.
- The National Archives, Discovery catalogue, SP 78/33/170 (record C7318548): "Folio 345: Edmondes to Burghley, and copy."
- The National Archives, SP 78/33 ff. 345-346 (Edmondes to Burghley, camp before Laon, 9 July 1594, in clear) and
  ff. 347-348 (clerk's copy of it): read in full from the copy saved on site at the Library of Congress on 14 November
  2026 in State Papers Online (Gale), by AI agents in two independent passes; no person has checked it; licensed images,
  not included. Ff. 349v and 366 (13 and 23 July 1594): the cipher passages looked at only, to identify the cipher.
- G. G. Butler (ed.), *The Edmondes Papers* (Roxburghe Club, 1913), nos. LXIII-LXVI, pp. 141-151 (HathiTrust mdp.39015083993017).
- J. Stevenson (ed.), *Correspondence of Sir Henry Unton* (Roxburghe Club, 1847), Internet Archive cu31924027964471 (language model only).
- S. Tomokiyo, *Cryptiana*, "Ciphers during the Reign of Queen Elizabeth I" (web page, read 14 Nov 2026).
- R. B. Wernham (ed.), *List and Analysis of State Papers, Foreign Series, Elizabeth I*, vol. 5 (1989): searched (HathiTrust mdp.39015015172375); the list entries and pp. 236-246 read from pages saved at the Library of Congress on 14 November 2026; the Brittany section not seen.
- G. Py-Patinec, *L'armée royale en Bretagne* (HAL dumas-02176647, 2019); French Wikipedia, "Liste des gouverneurs de
  Rennes" and "Laon"; English Wikipedia, "Henri, Duke of Montpensier", "Henri de La Tour d'Auvergne, Duke of Bouillon",
  "Charles de Gontaut, duc de Biron", "Jean VI d'Aumont", "John Norris (soldier)" (all read 14 Nov 2026).

## Log

- 2026-11-14: lead from a mining run over the Salisbury calendar; transcription, key, frozen held-out test and reading
  (first agent); independent blind transcription and solution, stricter test and content check (second agent);
  packaged here with the second agent's corrections, the governor of Rennes looked up, and both tests rerun.
- 2026-11-15: SP 78/33 ff. 345-348 collated with this letter, from the copy saved on site at the Library of Congress on
  14 November 2026 in State Papers Online (AI agents, two independent passes; no person has checked it; licensed images
  not included): a different letter of the same day, in clear, with its clerk's copy. Addressee changed from
  "[Lord Burghley]" to "an unnamed lord"; prior work and "not checked" corrected. No change to the reading, the key,
  the counts, the tests or the date.
