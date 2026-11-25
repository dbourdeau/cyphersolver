# Mountflorence → Madison, Paris, 18 March 1801 (catalogue 480)

Status: read in part (16 Nov 2026, recounted over cipher words: 12 of 16 words, 75.0%; was read, counted over code groups)

## Result: key recovered from the ciphertext alone; all 39 code groups decoded (26 Oct 2026, one session)

> I have it from very good Authority, DUPONT, that Spain has ceded to France, not Florida, but[?] the[?]
> Mississippi[?], with all its Dependencies. This was done by some of the secret Articles at[?] LUNEVILLE, as
> Compensation for TUSCANY, given by France to PARMA.

Reproduce: `python decode.py` (reading), `python decode.py check` (alphabetical order of the key), `python decode.py tsv`.
Key with grades: `key.tsv`. Group-by-group reading: `reading.txt`. Transcription: `ciphertext.txt`.

## The document

- James Cole Mountflorence (American consular agent and chancellor at Paris) to the Secretary of State, Paris,
  18 March 1801. Addressed to John Marshall, received under Madison (docketed by Jacob Wagner, received 12 June).
- NARA, RG 59, Despatches from US Consuls in Paris (microfilm T1), roll 1, **frame 0097** (catalog NAID 211302912,
  `https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T1/T1-01/T1-01-0097.jpg`). The 6 March 1801 letter
  is frame 0093. One page; two sentences in code, then clear text on the Council of Prizes and six US ships in
  quarantine at Malaga.
- Printed: Papers of James Madison, Secretary of State series, vol. 1, p. 27 (abstract: "Partly in code; key not
  found. Coded section apparently discusses Louisiana cession"); full transcription with the code numbers undecoded
  on Founders Online, Madison/02-91-02-0009 (added 2015).

## Transcription

39 code groups (measured, `ciphertext.txt`), 25 distinct, range 207-756. The groups were checked one by one against
frame 0097. **One correction to Founders:** the fourth group after "Compensation for" is **251**, not 250. Every
other group agrees.

Separators carry the structure: groups joined by full stops spell one word letter by letter (four runs: 6, 9, 7 and
5 groups); groups separated by commas are whole words.

## The system

A small one-part code: the numbers rise with the alphabet. Single letters stand at the head of their section
(A 207, C 251, D 357, E 377, I 460, L 475, M 500, N 529, O 544, P 640, R 660, S 664, T 684, U/V 723, Y 756), and
words follow their initial letter in order (at 228, but 249, by 250, Florida 432, France 434, Mississippi 521,
secret 666, Spain 679, the 688, to 719). All 25 values in use keep strict alphabetical order (`decode.py check`).
About 550 numbers between A and Y, so a code of some 600 groups. Not the Armstrong THE=972 code
(`targets/armstrong/`), where 'the' is 972.

## How the key was found

1. The 9-group run `475.723.529.377.723.460.475.475.377` has the pattern ABCDBEAAD. LUNEVILLE fits with U and V one
   letter, and the treaty of Lunéville (9 Feb 1801) is five weeks old and disposes of Tuscany.
2. The 5-group run ending the letter, `640.207.660.500.207`, is ABCDB: PARMA. The 7-group run after "Compensation
   for" shares 207 (A) and 529 (N) with these: TUSCANY. The 6-group name after "Authority" then reads
   D-U-P-O-N-T from letters already fixed (U, P, N, T) plus two new ones.
3. The letters come out in rising numerical order, which shows the code is one-part, and every word group is then
   bracketed by the letters around it: 679 between S 664 and T 684 = Spain ("679 has ceded"); 434 between E and I
   = France; 666 between S and Spain = secret ("some of the 666 Articles"); 432 just before France = Florida;
   521 between M and N = Mississippi; 688 and 719 between T and U = the, to; 228, 249, 250 between A and C = at,
   but, by.
4. The decipherment, made from the Founders text, needed 250 to be both C (TUSCANY) and "by" (given by France),
   so the reading predicted that one of them was a slip and that C ought to be 251. Frame 0097 shows 251 in TUSCANY
   and 250 for "by": the prediction held and the Founders transcription has a misprint.

Method: **key recovered from ciphertext-only** (pattern words, the order of the key, and probable words from the
known terms of the 1800-1801 treaties). No plaintext of the letter and no existing key were used.

## Grades and doubts

- Fixed by spelling (S, cross-checked between names): the 15 letter values, 27 of the 39 tokens.
- Inferred (I) from the alphabetical slot and the sense: 10 word groups, 12 tokens. Spain, France, secret and
  Florida are narrow (slot plus sense). Weaker: 521 Mississippi (any word from Mi- to My- fits the slot; "the
  Mississippi with all its Dependencies" is the sense), 249 but, 228 at, 688 the (common words, chosen from the
  slot and grammar). These are marked [?] in the reading.
- "Dupont": the informant is not identified. Pierre-Samuel du Pont de Nemours was in America in March 1801; another
  Dupont in Paris is meant, or the name is used loosely.

## Historical sense

Spain retroceded Louisiana to France by the secret treaty of San Ildefonso (1 Oct 1800), in exchange for a kingdom in
Italy for the Duke of Parma's son; the treaty of Lunéville (Art. 5) gave Tuscany to the Duke of Parma's house, and the
convention of Aranjuez (21 March 1801, three days after this letter) settled it. Spain refused to give up the Floridas.
Mountflorence's report matches all three points: Louisiana ("the Mississippi with all its Dependencies"), not Florida,
in compensation for Tuscany. His attribution to "secret articles at Lunéville" is his informant's version.

## Prior work

- Madison Papers editors (1986): key not found, sense guessed (Louisiana cession).
- David Humphreys to Madison, 10 April 1801 (abstract): could not decode a Mountflorence message with the key State
  had given him, so the code is not Humphreys's.
- Web search 26 Oct 2026 (correspondents, date, Founders, Tomokiyo's American list): no decipherment found. First
  decipherment, so far as known.

## Read share over cipher words only (16 Nov 2026)

README Conventions now count the read share over the words written in cipher, holes by words, sure words only. The
coded part of the letter is two sentences standing among clear words (the clear words of the same sentences, and then
the news on prizes and Malaga, which `reading.txt` does not hold). Separated by hand from `decryption.txt`, which lists
the coded words group by group: 16 cipher words (DUPONT, LUNEVILLE, TUSCANY and PARMA spelled letter by letter; Spain,
to France, Florida, but, the, Mississippi, secret, at, by France to: 12 words read from their alphabetical slots). The
four marked [?] in the reading (but, the, Mississippi, at) are holes: **1.0 -> 0.750 (12 of 16 words)**. The old 1.0
was 39 of 39 code groups given a value, a count of tokens. Class **read -> read in part**; the key stays recovered.
The measure cannot be declared: the reading file sets the coded words inside clear words without a mark, so
`v10_relabel.py` reports the whole file (0.918, not split).

## Remaining gaps

- 521 (Mississippi), 249 (but), 228 (at), 688 (the) - blocker: too-short; each occurs once in a 39-group message in a one-part code of some 600 numbers, only the alphabetical slot and the sense fix them, and no second message in this code has been found

## Escalation

- [x] siblings: frames 0082-0099 of T1 roll 1 viewed on a contact sheet (with the 6 March 1801 Mountflorence letter,
  frame 0093); no other coded page seen there
- [x] clear-pages: none; the clear text of the letter is on other subjects
- [x] known-keys: the Armstrong THE=972 code (1806-10) is a different code ('the' is 972 there, 688 here); Humphreys's
  State key is ruled out by his 1801 letter
- [x] print: Madison Papers SS 1 and Founders: undecoded; nothing else found
- [x] key-rebuild: whole key rebuilt from the four spelled names and the alphabetical order
- [n/a] retry: nothing to retry the four weak word values against, since each occurs once and no second message in this code exists; all 39 groups have a value
