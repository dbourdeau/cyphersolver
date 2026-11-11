# lee1813: William Lee to James Monroe, Paris, 1, 2 and 6 February 1813: a numerical keyword cipher (WINCHESTER) and three letters read

Status: new cipher with its solution, contributed. Key: keyword WINCHESTER over a 25-letter alphabet, numerals 1-25,
restarted at each coded stretch, with Lee's frequent slips. 1 February read (8 stretches, 110 numerals, no
contemporary decipherment known); 2 February read in part (41 stretches, 1,097 numerals; seven passages the 1813 clerk
did not read are read here, one of them, J, as a proposal); 6 February read in part (74 stretches, 1,456
numerals; the last 32 stretches, 603 numerals, carry no decipherment on this copy, none was found elsewhere, and
they are deciphered here). "In part" is
the README read bar applied strictly: every word in which we supply a letter Lee mis-enciphered counts as a hole.

Contributed by Andrew Beling, with AI agents (Claude Fable 5.2 and Claude Opus 5.5 subagents, run by Andrew Beling),
10-11 November 2026. Not in `catalogue.json`, `research/leads*.json` or `targets/` (searched for William Lee,
Bordeaux 1813, WINCHESTER, T164 on main ebb365f).

William Lee (1772-1840), US consul at Bordeaux, had acted for some months as secretary to Joel Barlow, US minister to
France. Barlow died in Poland on 26 December 1812, on his way back from Vilna, where he had gone to meet Napoleon to
conclude a treaty. Lee came to Paris, and with Barlow's nephew Thomas Barlow and his widow Ruth disputed the charge of the legation and
its papers and cipher with David Bailie Warden, the consul at Paris. These three letters to the Secretary of State
were written from the legation in those weeks, partly in a cipher of Lee's own ("I use my own Cipher and not that of
the Government, in corresponding with the Secretary of State": Lee to Warden, 18 February 1813, NARA T1 roll 4 frames
0347-0348, certified copy).

## 1. Documents

| date | frames (T164 roll 3) | pages | cipher | clerk's decipherment of 1813 | printed |
|---|---|---|---|---|---|
| 1 Feb 1813, "private", Hotel of the Legation | 0099-0102 (cipher on 0099-0101), docket 0103 | 7 | 8 stretches, 110 numerals | none on the film (frames 0095-0115) | not in *Papers of James Monroe* 6 (cited in a note) |
| 2 Feb 1813, "Copy of Dispatch C" | 0106-0107 | 3 | 41 stretches, 1,097 numerals | separate sheets, frames 0104-0105, with gaps marked | *Papers of James Monroe* 6:366-367, from the clerk's copy |
| 6 Feb 1813, "Second Copy", Hotel of the Legation | 0108-0110 | 5 | 74 stretches, 1,456 numerals | pencilled between the lines of pages 1-3 only, to F6-42 | not printed |

Not to be confused with Lee's other letter of 1 February (frames 0097-0098, "private", "duplicate"), wholly in
clear, in which he regrets that he has "not the Cypher". Frame map of 0095-0115: Lee's 29 and 30 January letters,
the dockets, the Warden-Lee exchange of 17-18 February, and a Bordeaux letter of 19 February; none of these hold
numerals.

## 2. Sources and images

- NARA, RG 59, Despatches from U.S. Consuls in Bordeaux, France, 1783-1906, item "Despatches: March 30, 1810 -
  November 14, 1824", NAID [211586337](https://catalog.archives.gov/id/211586337), microfilm T164 roll 3.
- Frame images (public domain, NARA catalogue; not copied here), pattern
  `https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-NNNN.jpg`:
  [0099](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0099.jpg),
  [0100](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0100.jpg),
  [0101](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0101.jpg),
  [0102](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0102.jpg), docket
  [0103](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0103.jpg) (1 Feb);
  [0104](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0104.jpg),
  [0105](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0105.jpg) (clerk's
  decipherment of 2 Feb);
  [0106](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0106.jpg),
  [0107](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0107.jpg) (2 Feb);
  [0108](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0108.jpg),
  [0109](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0109.jpg),
  [0110](https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-0110.jpg) (6 Feb).
  The left edge of the left-hand page is cut on 0101 and 0107.
- *The Papers of James Monroe*, vol. 6, ed. Daniel Preston and Robert Karachuk (Charlottesville: University of
  Virginia Press, Rotunda digital edition), "From William Lee, Paris Feby 2d 1813", MONR-01-06-02-0283, pp. 366-367.
  It prints the clerk's decipherment with his bracketed remarks ("here there is some error", "here follows a sentence
  which from some error must remain in obscurity", "an error") and italics for the coded words. Cited, not copied.

## 3. The system and the key

See `key.md` (rule, tableau, slips, how the key was obtained) and `key.tsv` (tableau). In short: a Vigenère-type
cipher with numerals, alphabet `ABCDEFGHIKLMNOPQRSTUVWXYZ`, keyword WINCHESTER, plaintext index = (numeral - 1 + key
letter index) mod 25, key restarted at W for every coded stretch. The keyword is pencilled by the 1813 clerk above
the numerals of 6 February; the earliest record of it in our project files is 6 November 2026, when the rule was
checked against two of the clerk's pencilled words. Our files do not record how or when the keyword was first
noticed.

Lee broke his own rule often: 25 of the 123 stretches read only under a changed key position (a letter left out
while the key advances, a key letter used twice, the key run on from the stretch before, a few larger jumps), and
single wrong letters are frequent (section 9).

## 4. Transcription

- **2 February** (`transcription_1813-02-02.txt`): transcribed 6 November 2026 from the frame images, 41 stretches,
  1,098 numerals, a first pass with overwritten and struck groups noted. Source corrections since: Y numeral 37 is
  4, not 21 (enlarged crop, 6 Nov); on 11 November 2026, at zoom, J numeral 17 is 4 followed by a comma (was 14), Z
  numeral 5 is 19 (was 14), AN numeral 7 is 17 (was 7), and N's "9231", written with no dots, is 9 23 1 (was 9 2 3
  1), so the letter has 1,097 numerals. The clear words were checked on frames 0106-0107 on 10 November 2026 and four
  corrected ("Mrs B.", "told her", "asked her if she", "She answered"; the working file had the masculine forms).
- **1 and 6 February** (`transcription_1813-02-01.txt`, `transcription_1813-02-06.txt`): transcribed 10 November 2026
  from full-resolution strips, five to six lines each, with Lee's colons and line ends kept. Then the baseline and
  the decoder were run, and only then the clerk's pencil was read. Limits stated by the transcriber: pages 1-3 of
  6 February (F6-01 to F6-42) were read with the clerk's pencil in view; after the first decode about 100 crops at
  2x zoom were re-read where the text was off, and six numerals changed on the image evidence (6 Feb: F6-20 no. 18,
  F6-14 no. 12, F6-11 no. 14, F6-65 no. 9; 1 Feb: F1-H nos. 21 and 23 from 16 to 10). Each is marked doubtful in the
  transcription with the first reading.
- The 10 and 16 of this hand are the easiest pair to confuse; every 10 or 16 that mattered to a word was looked at
  again, the ones in clean words were not.
- F1-H nos. 21 and 23 ("offend"): Andrew Beling compared them on frame 0101 with Lee's other 10s and 16s on
  11 November 2026 and reads both as 10. As 16 they give UFMEND; as 10 they give a word that fits the key and the
  sentence.

## 5. Decryption and the decoder

`decryption_<date>.txt` gives, for every stretch, the numerals, the baseline (key restarted at W, no slip), the
decoder's offset path and text, z against 200 shuffled-numeral controls and whether it beats them all, the path used
for the reading with the key letter under each numeral, the mechanical text unrepaired, and the words of the reading.
`python decode.py` re-derives every baseline and used text from the transcriptions (result: ok, 123 stretches).

The decoder (project script `lee_phase_slip_decoder_2026_11_10.py`, and a copy with paths changed for 1 and 6 Feb)
chooses for each stretch the offset path that maximises a letter 4-gram score minus 9.0 nats per offset change, by
exact dynamic programming. The penalty was fixed before the first run and not tuned. The model was built from about
2.0 million letters of English prose (13 files of period and modern text in the project, including *Naval Documents
Related to the United States Wars with the Barbary Powers* vol. 2 part 2; nothing from Lee). Each stretch is decoded
200 more times with its numerals shuffled. 104 of the 123 stretches beat all 200 controls (1 Feb 6 of 8, 2 Feb 33 of
41, 6 Feb 65 of 74); the others are short (5-15 numerals, where the test has little power) or are the weak places
named in section 12 (F6-26, F6-47, F6-62, 2 Feb J and V). The decoder is not included here: it needs the corpus,
which is not in this repository. Re-running it on 10 November 2026 reproduced every saved path and z exactly; z for
the three 2 Feb stretches of 7 numerals (A, M, W), which the 2 Feb run skipped, were computed then with the same code.
The decoder lines and z of 2 Feb J, N, Z and AN were computed on the transcription before the re-reads of 11 November
(section 4), as their notes say; `decode.py` checks the baseline and used lines on the current transcription.

Which path the reading uses: the baseline when the decoder adds nothing or its slip is spurious (it sometimes
"repairs" the last letters of a stretch with a slip); the decoder's path where it gives the text; a hand-chosen path
in five stretches, labelled (2 Feb D and L, from the 6 November 2026 pass; 2 Feb J and N, 11 November 2026; 6 Feb
F6-01).

## 6. Readings

| letter | file | coded words (about) | words with a supplied letter | words guessed or unread | read_share (repo measure, whole reading) | read_share, cipher words only | state |
|---|---|---|---|---|---|---|---|
| 1 Feb | `reading_1813-02-01.md` | 19 | 0 | 0 | 0.994 | 1.000 | read |
| 2 Feb | `reading_1813-02-02.md` | 216 | 42 | 1 | 0.896 | 0.792 | read in part |
| 6 Feb | `reading_1813-02-06.md` | 293 | 53 | 6 | 0.928 | 0.802 | read in part |

The "repo measure" is `research/reading_audit/v10_relabel.py` `share()` on the `## Reading` section, which includes
Lee's clear text. The cipher-only share counts every word with a supplied or dropped letter as a hole, as the README
asks for supplied letters. If words whose sense is not in doubt (a wrong letter of Lee's in an otherwise certain
word) were counted as read, the cipher-only shares would be 0.995 (2 Feb) and 0.980 (6 Feb), counting as holes only
words guessed or unread; over all three letters that is `fraction_coherent` (0.987) in the profile. We mark the two letters "read in part" because the bar as written counts
supplied letters; Andrew Beling, reviewing on 11 Nov 2026, kept that label.

The readings mark, passage by passage, what the clerk read (italics), what he did not (bold italics, † failed,
‡ never attempted, ≠ differs), and what rests on a hypothesised slip or a proposed division of numerals (§); the
notes on each marked passage are in section 12. Each reading ends with a summary. The plaintext is English, so no
translation is needed. `docs/_check_reading.py lee1813` scores the readings 0.935, 0.846 and 0.811 clean sentences
(readable); the weak sentences in 2 and 6 February are those where a bracketed repair splits a word (CHECKS.txt).

## 7. What the 1813 clerk read and missed

- **2 February.** The clerk read most of it, and the edition prints his text. Seven passages are in neither: the
  qualification "except that part relating to indemnities" (D), "would not only have indemnities through" (J, a
  proposal; clerk "here there is some error"), the sentence he marked obscure ("their game now is to spin out the
  negotiations still farther", L), "injudicious letter of his to Latrobe" (U, V), "Mr Barlow's correspondence with
  the Dukes of Bassano and Dalberg" (Y), "proves favorable [?to] their policy" (Q; clerk "favorable news [to
  france]"), "last correspondence" (AN; clerk "communication").
- **6 February.** The clerk's pencil reads 42 stretches with gaps: he gave up in F6-01/02, F6-11, F6-26, F6-29,
  wrote "(an error here)" at F6-39, took F6-28 as "lost his cause" (the cipher gives "left his capital fearing"),
  read only the start of F6-21, F6-27, F6-42, and stopped. The 32 stretches after that were never touched:
  forced donations of men and money as "the last effort of the nation", the Concordat, the dread of an "emprunt
  forcé", terms of peace offered to England if she abandons Russia, Dalberg's report of Austria "firm on the
  principle of an armed neutrality, negotiating as mediatrix", and the closing "on this rests the hopes of his court,
  his crown and his fame".
- **1 February.** No decipherment found; all eight passages are new readings: the Irish Brigade, Marshal Sérurier,
  Barlow's letter to Latrobe, toasts to the "success of Clinton" and Emmet, the United Irishmen as "a distinct party"
  so strong that "the President dares not offend" them.
- The clerk repaired Lee's single wrong letters silently where the word was obvious, so his copy reads more smoothly
  than the numerals; we keep each repair visible.

## 8. Second-reader check (6 February, the part never deciphered)

An independent agent, with no access to our files, the decode or the clerk's text, re-read the numerals of F6-43 to
F6-74 from the frames in two passes (strips at 1.5x, then thirds at 2.3x, with 4.5x crops of doubtful places)
(project file `lee_feb6_bare_second_reading.json`). It read 589 numerals in 30 stretches; aligned with ours, 588 are
identical. The one difference is F6-65 numeral 9: we read a re-inked 1, the second reader 17 (or 11, or a blotted
1); "Duke Dalberg" needs 1. It skipped one written line, F6-51 numerals 20-33 (14 numerals), which so have one
reading only. It divided two pairs of stretches differently (F6-61/62 and F6-73/74 as one each), which changes no
numeral. Pages 1-3 (F6-01 to F6-42) and the 1 and 2 February letters have had no second reading of the numerals,
apart from Andrew Beling's check of F1-H numerals 21 and 23 on frame 0101 (section 4).

## 9. Lee's own enciphering errors

Counted from the alignment of the mechanical text with the reading, outside the passages given only as proposals:
60 letters supplied and 2 dropped in 6 February, 53 supplied and 1 dropped in 2 February, none in 1 February (recounted on
11 November 2026 from the "read as" lines, after the new readings of J, L and N). The
transcriber's earlier count for 6 February, "at least 47", was made over letters that align one to one and left out
the omissions. Wherever a numeral behind a wrong letter was looked at again at zoom it was clear on the page, so
these are Lee's slips, not ours; but the single wrong letters in F6-15, F6-21, F6-22, F6-25, F6-30, F6-69 and F6-73
rest on the strip reading alone and some may turn out to be ours.

**How the mistakes arise** (`errors.py`, output in `error_accounts.txt`, 11 November 2026). The script enciphers each
reading with WINCHESTER and finds the cheapest set of mistakes that turns it into the numerals Lee wrote. The kinds of
mistake allowed, and their costs, are set by judgement and listed in the script. The accounts are explanations that fit
the numerals; they do not prove what Lee did. Across the three letters it finds:

- **Key steps**: a key letter skipped (8) or used twice (5). This is what the decoder's "slips" are. A step forward is
  also what happens when Lee leaves a letter out but its key letter is still used up (9 cases, e.g. the R of "their"
  in 2 Feb L). Three larger jumps remain (2 Feb Y -3, AN +4, 1 Feb F1-H -2); F1-H is a restart at W after PRESIDENT, the other
  two have no mechanism found.
- **Dots between figures**: two figures run together with no dot (5: 2 Feb J "17" for 1 7, L "13" for 1 3, AB "23"
  for 2 3, AM "14" for 1 4, 6 Feb F6-02 "11" for 1 1) and one figure split by a stray dot (2: 6 Feb F6-01 "1.2" for
  12, and 2 Feb Q "1.5" for 15, in the doubtful words before "their policy"). 2 Feb N, where Lee wrote "9231" with no
  dots at all, is not counted: the transcription already divides it 9 23 1. Lee's dots are irregular, so this kind of mistake is easy to
  make and easy for a reader to miss. It is why the clerk failed at J and at the opening of 6 Feb.
- **Single wrong figures**: off by one place (22), a tens figure added or lost, e.g. 17 for 7 (6), look-alike figures
  that may be our misreading (8), and 52 others.
- **The keyword's first letter, W.** 27 of the single wrong figures fall under W, 8.7% of the 310 figures enciphered with
  it, against 0.4-2.4% for I, N, H, E, S and R (C 6.4%, T 5.6%). Most fall where the keyword comes round to W again:
  13 at figure 11 of a stretch, 3 at figure 21, 5 at figure 1. In five of them (2 Feb D, V, X; 6 Feb F6-13, F6-29)
  Lee wrote the letter's place in the plain alphabet (E as 5, B as 2, I as 9, S as 18), as if he did not apply the key
  when it came back to W. Under no other key letter does this happen. In 6 Feb, seven figures under W are two too
  high, as if he counted from U. One reading of this (ours, not proved): the W row is where the count from the key
  letter must wrap past Z after four letters, and Lee lost his place there.

## 10. Prior work

Searched 10-11 November 2026 (project file `prior_art_663_king_lee_2026-11-11.md`, question D): Weber, *United
States Diplomatic Codes and Ciphers 1775-1938* (1979) and *Masked Dispatches*: nothing on Lee, Bordeaux 1813 or a
WINCHESTER keyword. Cryptiana (Tomokiyo), 293 pages: "Winchester" only on Civil War pages, "William Lee" only the
Revolutionary-era Lee. This repository: no Lee, Bordeaux 1813 or WINCHESTER target, issue or pull request. Web
searches for the keyword and for the letters of 1 and 6 February: nothing. *Papers of James Monroe* 6 prints 2
February from the clerk's copy and neither of the others (the 1 February coded letter is cited in a note only).
The Madison Papers print Lee to Dolley Madison, 20 March 1813, which mentions the legation's "Papers seal & Cypher"
but not this cipher. Mary Lee Mann (ed.), *A Yankee Jeffersonian* (1958), a selection of Lee's diary and letters, is open at
HathiTrust (uc1.b4437374); all 354 pages were searched on 11 November 2026: it prints Lee to Monroe of 20 January 1813
and 4 March 1814, but not the letters of 1, 2 or 6 February 1813, and never mentions a cipher of Lee's or WINCHESTER. So: no earlier identification of the
keyword and no earlier reading of the passages the clerk left was found; the 1 and 6 February letters are "not found
in print", not proven unpublished.

## 11. Method and tools

AI agents (Claude Fable 5.2 and Claude Opus 5.5 subagents), run by Andrew Beling, located the frames (20 October
2026), transcribed the numerals from the NARA images, wrote and ran the decoders, compared the clerk's pencil and
copy, read the passages as sentences and wrote these files; a further agent made the blind second reading. Andrew
Beling set the tasks and rules (numerals before the clerk's text, nothing repaired silently, nothing posted), read the
three readings against the images (reading_review) and checked F1-H on frame 0101 himself (human_check). No professional
palaeographer has checked the numerals. Scripts: `decode.py` and `errors.py` here (standard library); the decoder and the
full-pass scripts stay in the contributor's project folder (they need a corpus not in this repository) and can be
supplied.

`viewer/` is a static page (open `viewer/index.html`; no build step) that shows each NARA frame beside the reading,
passage by passage, with what was in cipher, what the 1813 clerk deciphered and what was first read now marked, and the
figure-by-figure decipherment under the key. Frames load from the National Archives catalog; no images are stored here.
`viewer/reveal_lee1813.json` is a draft for the site's "watch it decipher" widget (the opening of 6 Feb), offered for
the write-up. `viewer/README.md` says how `viewer/data.js` is generated.

## 12. Notes on the passages

The readings mark passages with †, ≠, ‡ and § (legend in each reading). The detail:

**1 February.** All eight are new readings: no contemporary decipherment is known.

- F1-A Irish Brigade: Irish officers in French service, whom Lee counts as Warden's friends (Warden was Irish-born).
- F1-B Marshal Serrurier: probably Jean-Mathieu-Philibert Sérurier, Marshal of France; Lee's spelling, mechanical and exact.
- F1-C Latrobe: Barlow's letter of 1812 to Benjamin Henry Latrobe, also meant in the 2 February letter (U, V).
  7 numerals: the baseline is exact, the control test means little at this length (z 0.5).
- F1-D success of Clinton: DeWitt Clinton, Madison's opponent in the presidential election of 1812.
- F1-E Emmet: Thomas Addis Emmet, United Irishman in New York. 5 numerals, baseline exact.
- F1-H the President dares not offend: the key restarts at W after PRESIDENT (decoder path 1-12:0 13-26:8, z 6.8);
  "offend" rests on numerals 21 and 23 read 10, not 16 (as 16: UFMEND), as Andrew Beling confirmed on frame 0101. §

**2 February.**

- D: after "sanctioned" the clerk's copy and the edition stop. The numerals go on, under the key stepped back one
  place from numeral 62 (hand path 1-61:0 62-98:9, from the 6 Nov 2026 pass; the decoder's own path ends 95-98:8 and
  gives a worse tail): "except that part relating to indemnities", with four wrong letters. †§
- J (17 numerals, after "would not only have"): read 11 Nov 2026 as "indem[ni]ties through". The clerk wrote "here
  there is some error". The key runs on from stretch I (27 numerals, so J starts at key letter T), which gives INDEM.
  Numeral 6 is written 17: taken as 1 and 7 run together (N, I), Lee's numerals then match a correct encipherment of
  INDEMNITIESTHRO figure for figure, and UGH sits one key letter on. Lee's colon after the tenth figure falls at the
  end of "indemnities". The last figure is 4 (a re-read at zoom; first transcribed 14). The words are the cipher's;
  the sense is presumably "would not only have carried the indemnities through". †§
- L (47 numerals, the head of page 2): the clerk marked the whole sentence as obscure. Under two hand-chosen key
  steps (1-4:6 5-25:7 26-47:8) it reads "thei[r] game now is to spin out the negotiations still farther"; the
  decoder's own path (1-26:7 27-47:8) gives the same from "game" on. The step at numeral 5 is the R of "their" left
  out with its key letter used up, which settles the first word (11 Nov 2026). †§
- N: "now", as the clerk read it. Lee wrote "9231" with no dots; read as 9, 23, 1 (first transcribed 9, 2, 3, 1) the
  stretch gives NOW and reads with one key step, after "making" (path 1-27:0 28-57:1), where the old reading needed
  three and still failed at "now" (11 Nov 2026).
- Q: the clerk has "proves favorable news [to france]"; the cipher gives "proves favorab[l]e", then, with the key
  stepped from numeral 15, "... their policy", with the word between not clean. ≠§
- U, V: the clerk has "injudicious" and a bracketed gap. The cipher gives "injudicious letter" (key one place on from
  numeral 12) and then, after the clear "of", "his to Latro[b]e" (baseline; numeral 11 reads 2 where B needs 6;
  12 numerals, z 0.8). The 1 February letter has the same phrase in cipher, "that unfortunate & injudicious letter
  to LATROBE", and Warden to Jefferson, 21 January 1813, and Lee to Dolley Madison, 20 March 1813, discuss Barlow's
  letter to Latrobe. †§
- Y: the clerk has "Mr Barlow's [an error]". From numeral 10 the key is seven places on, and 45 of 45 letters read
  "correspondence with the Dukes of Bassano and Dalberg" (numeral 37 is 4, re-read on the frame on 6 Nov 2026; the
  first transcription had 21). The first nine letters give MRSARLOWS: S for B (numeral 3 reads 6). †§
- AN: the clerk has "the ministers last communication"; the cipher gives "correspondence" (key stepped at numeral
  17). ≠§
- AD: the clerk's manuscript has "as equivalent", as the cipher does; the printed edition has "an equivalent" (corrected 11 Nov 2026; earlier marked ≠).
- X: the clerk has "indemnities" where the cipher gives "indemnity" (≠, added 11 Nov 2026).
- Z, AN: numerals re-read on frame 0107 on 11 Nov 2026 (Z 5 = 19, AN 7 = 17); "declarations" and "ministers" now read without a supplied letter.
- AJ: small difference only: the cipher has "to these
  arrangements" (clerk "to the arrangement"). ≠
- Paths with a slip that the clerk also read through (G, N, O, AB, AM) are not marked §: his copy confirms the words.

**6 February.**

- F6-01, F6-02: the clerk read "purpose of commerce" and stopped. The rest rests on two of Lee's mistakes of the kind
  set out in section 9. "I established": Lee used the key letter T twice (figures 18 and 19), which steps the key back
  one place, and he wrote the last figures 1.2.25 with a stray dot: as 12 and 25 they give ED, as three figures 1, 2,
  25 they give TFQ. "a [c]ipher, a copy": the fifth figure of F6-02 is written 11 with no dot and is two figures 1
  and 1; then the stretch reads AIIPHERACOPY under the plain key, with one wrong figure (I for C). If right, WINCHESTER is a cipher Lee set up for commerce with C. D., S. S. L
  and C. W., not a State Department cipher, which fits his "I use my own Cipher and not that of the Government". The
  three are not identified, nothing found ties the word WINCHESTER to Lee, and no other text in his cipher was found
  on T164 roll 3; on 26 May 1813 (frame 0151) he asked Monroe for the legation's old cipher (project file
  `research/lee_cipher_partners_2026-11-11.md`). †§
- F6-11: the clerk pencilled key letters only. "[a]n account of such a disastrous campaign" (C for A; a stray C in
  DISASTRCOUS; "such" rests on numeral 14 read as 1 with a blotted second digit). †
- F6-19: the clerk has "patriotic"; the cipher has PATRIOT (7 numerals). ≠
- F6-21, F6-27, F6-42: the clerk read the first part only. "it is feared" needs the key to step one place after
  CONTINENT; "for a general peace are operating" is the baseline with five wrong letters; "depression of the nation"
  needs the key to step back one place after DEPRESS (the clerk carried it straight on and wrote nonsense). †§
- F6-26: a proposal. The numerals give OFALARMERKEUTRATITY (all confirmed at zoom; z 3.5, does not beat all
  controls); "of an armed neutrality" needs four wrong letters and a key restart. F6-70, which is clean, says "an
  armed neutrality" of Austria. The clerk wrote the same letters and gave up. †§
- F6-28, F6-29: the clerk has "lost(?) his cause" and nothing more; the cipher gives "left his capital fearing" and
  "approach of the Russian[s]". ≠ †
- F6-39: the clerk wrote "(an error here)". Lee enciphered H, dropped the I and went on with the key one place ahead;
  the decoder holds offset 1 throughout, so the first letter comes out U. †§
- F6-43 to F6-74: never attempted by the clerk (‡). § on F6-47 (E of EFFECT not enciphered, key one place on; the last
  six numerals, 2 3 4 23 6 1, do not read; "but on" if the first two are one numeral 23, but the page has a dot
  between them), F6-51 and F6-52 (letters left out while the key advances), F6-62 and F6-74 (key carried on from the
  stretch before, offsets 8 and 9).
- F6-62 "A Mr de Bassagne(?)": thirteen letters, exact under the key run on from F6-61, but z 3.0, not clear of all
  controls, and the man is not identified.
- F6-65 "Duk[e] Dalberg told me" reads only if a thick, re-inked 1 (numeral 9) is kept; first taken for a deletion.
  The second reader read 17 there.
- F6-56 "emprunt forcé": a forced loan, in French in the cipher.

## Integration check (11 Nov 2026)

Done by the project on merging pull request #397 (the contributor's files are otherwise as sent).

- **The key decrypts the 603 numerals.** A decoder written separately from `decode.py` (same rule, from `key.md`)
  was run on `transcription_1813-02-06.txt`: F6-43 to F6-74 are 32 stretches and 603 numerals; 27 of the 32 give
  English under the key restarted at W with no change of position (RECOURSE, TOFORCEDDONATIONS, MENANDMONEY,
  BUTITISTHELASTEFFORTOFTHENATION, EMPRUNTFORCE, OFFEREDTOENGLANDIFSHEWILLABANDONRUSSIA,
  ANARMEDNEUTRALITYNEGOTIATINGASMEDIATRIX, ATTHEEXPENSEOFPOLAND ...), and in five the key position changes inside the
  stretch or runs on from the stretch before (F6-47, F6-51, F6-52, F6-62, F6-74), as section 12 says. `python decode.py`: result ok, 123 stretches, 110 + 1,097
  + 1,456 numerals. The three readings were read here as sentences; they hold.
- **Numerals checked on the frames.** NARA frames 0108-0110 were fetched and these stretches compared with the
  transcription at full resolution: F6-15, F6-21, F6-22, F6-25, F6-30, F6-51 (second line, numerals 20-33), F6-65 to
  F6-69, F6-70 (first 13 numerals), F6-73 (second and third lines) and F6-74. Every numeral agrees with the
  transcription (about 300 numerals). So the single wrong letters in F6-15, F6-21, F6-22, F6-25, F6-30 and F6-69 are on the page (Lee's,
  not the transcriber's); in F6-73 numeral 14 was seen here and numeral 8 rests on the transcriber's zoom note. F6-51
  numerals 20-33, skipped by the second reader, now have a second reading.
- **"Never deciphered at the time" is narrowed.** What the frames show: the clerk's pencil (key letters above, words
  below) runs on frame 0108 and 0109 to "depression of the" (F6-42) and stops; from "recourse" (F6-43) to the end of
  frame 0110 there is no pencil. The contributor found no separate decipherment on frames 0095-0115 and no printing.
  But the letter is headed "Second Copy": another copy was sent, it was not looked for (for example among the
  despatches from the legation in France), and a decipherment could exist on it. The statement supported by the
  sources is: no contemporary decipherment of these 603 numerals is on this copy, and none was found. The Status
  line, the profile title, the 6 Feb summary and the head of `reading_1813-02-06.md` were reworded to say that; the
  phrase "never attempted by the clerk" in section 12 is about this copy.
- **Gaps.** Three items were listed with the blocker "not-attempted". The zoom re-read of the seven single wrong
  letters and the second reading of F6-51 numerals 20-33 were done (above) and the items removed. "Mr de Bassagne" is
  a reading with exact letters whose doubt is its length (13 numerals, z 3.0), now listed as too short. The missing
  second reading of the numerals of 1 Feb, 2 Feb and 6 Feb F6-01 to F6-42 is a limit of the verification, not an
  unread piece: it stays stated in section 8 and on the page.
- **Method.** The keyword is the clerk's, read off his pencil; the alphabet, the numeral rule, the restart and the
  slips were worked out here against his pencilled words. That is "key recovered based on adjacent plaintext" in the
  project's categories, kept as the contributor set it.
- Checkers: `docs/_check_profile.py lee1813` valid; `docs/_check_reading.py lee1813` 0.935 / 0.846 / 0.811, as in
  CHECKS.txt; `docs/_check_terms.py lee1813` 0 hits. Not in `catalogue.json` or `research/leads.json`; not on DECODE.
- `viewer/` loads only its own `data.js` and frame images from catalog.archives.gov. It also carries a URL pattern
  for another NARA film (M30 roll 4) that no document in `data.js` uses.

## Remaining gaps

One line per open piece (detail in sections 4, 8, 9 and 12):

- 6 Feb F6-47, last six numerals (2 3 4 23 6 1) - blocker: illegible; "but on" only if 2 and 3 are one numeral 23, and the page has a dot between them.
- 6 Feb F6-26 "of an armed neutrality" - blocker: illegible; a proposal: the numerals, confirmed at zoom, give OFALARMERKEUTRATITY (four letters off and a key restart; z 3.5).
- 6 Feb F6-01/F6-02 "I established ... a cipher, a copy", and 2 Feb J "indemnities through" - blocker: illegible; proposals: each rests on taking Lee's dots between figures as mistakes (1.2 as 12; 11 as 1 1; 17 as 1 7).
- "Mr de Bassagne" (F6-62) - blocker: too-short; 13 numerals, letters exact under the key run on from F6-61, but z 3.0 does not clear all controls at this length, and the man is not identified.
- 2 Feb Q, the word before "their policy" - blocker: illegible; "[?to]" is supplied from the sense, the figures between "favorable" and "their policy" do not give a clean word.

Not gaps in the text, but limits of the checking: the numerals of 1 Feb, 2 Feb and 6 Feb F6-01 to F6-42 have one
reader each (section 8), apart from the stretches compared on the frames in the integration check; the words in which
a letter is supplied for one of Lee's wrong figures (60 letters supplied and 2 dropped in 6 Feb, 53 and 1 in 2 Feb)
are counted as holes in the measure (section 6).

## Escalation

- [x] clear-pages: the clerk's pencilled keyword letters and plaintext (6 Feb) gave the keyword and the check; his separate copy (2 Feb) and the edition used for comparison only, after our decode
- [x] siblings: the three coded letters of 1, 2 and 6 Feb in T164 roll 3 frames 0095-0115 all read; in the NARA OCR of the whole roll (1810-1824) runs of numerals occur only in these three letters (OCR can miss faint numerals)
- [n/a] known-keys: the keyword is written on the 6 Feb letter by the clerk and reads all three letters; no other key is needed
- [x] print: *Papers of James Monroe* 6 (2 Feb only); Weber 1979 and Masked Dispatches; Cryptiana; this repository; web. Mann (1958), searched in full 11 Nov 2026
- [x] key-rebuild: the key is complete; Lee's slips are modelled per stretch by the phase-slip decoder (one rule, fixed penalty, controls) over all 123 stretches
- [x] retry: J under all ten offsets and the decoder, then read on 11 Nov 2026 with the key run on from I; four cancellation branches of L at all offsets (6 Nov 2026); the doubtful numerals of 1 and 6 Feb re-read at zoom where a word depended on them
