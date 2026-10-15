# Frederick II (ministerial rescript) to Louis Michell, Berlin, 28 December 1751 (KHA, Prins Willem V inv. 198; DECODE R1955)

Catalogue item 36 (class C, scored by rule). Split on 14 Oct 2026 from `targets/michell1751/` under the one-key rule
(George Lasry, 14 Oct 2026). The King's immediate letter of the same day, DECODE R1957, is in Frederick's cabinet code and
stays in `targets/michell1751/` (michell1751.html): a different cipher, with its own page. This entry is R1955 alone,
in the code Michell used for his own reports.

**Outcome: read after matching with a key from external sources, read in part.** WAINUT (PR #29, 11 Oct 2026) found
that R1955 is in Michell's envoy code and decoded 95 of its 360 groups (26.4%, re-counted 14 Oct 2026 from
`R1955_reading_line.txt`) with a table taken from the contemporary Dutch decipherments of two of Michell's reports
(DECODE R1050, R1051). Fragments only; the subject cannot be stated with confidence. The result is WAINUT's; this
project transcribed the letter (19 Sept), compared the two transcriptions and re-counted the fraction.

Files: `transcription_r1955.txt` (Bourdeau, 362 groups, one line per manuscript line), `R1955_tx.txt` (WAINUT, 360
groups, with a palaeographic header), `R1955_reading_line.txt` (WAINUT's decode, '·' for no value),
`circular_scores.tsv` (circular-letter test). The scripts are in `targets/michell1751/key1751/scripts/`, shared with
the cabinet-code work (`circular.py` reads `R1955_tx.txt` here). Images: the main checkout's
`targets/michell1751/decode/IMG_R1955_*` (P2 = first page), git-ignored.

## The letter (Bourdeau, 19 Sept 2026)

Worked 19 Sept 2026 (catalogue entry 36, DECODE R1955), in `targets/michell1751/` until the split. Transcribed in full in `transcription_r1955.txt`.

- The Dutch copy is headed *Lettre du Roi de Prusse au Secrétaire Michell du 28 Decemb. 1751* and signed *Féderic*, but
  the *Politische Correspondenz* prints only one letter to Michell of that date (no. 5263 = R1957). This one is the
  ministerial rescript, issued in the King's name and not printed.
- The clear opening is *Toutes vos dépêches m'ont été bien rendues et la dernière est du 14e de ce mois*. Then come 362
  code groups (2 to 5346, most under 3600, with half-groups 1½, 10½, 40½, 150½, 180½, 660½) and the date.
- It shares no code with R1957: only 19 of their distinct groups coincide, and those are chance collisions.
- 295 of the 362 groups are distinct, and the commonest (2, 230) occurs 5 times. That is a large two-part code with
  homophones even for *de* and *que*, so ciphertext-only analysis has nothing to work with. The pair 1487 50 recurs 3×.
- No printed or online decipherment was found. What could open it: the Prussian ministerial code of 1751 (GStA PK, I. HA
  Rep. 96 / Rep. 9 Chiffres), Pierre Lyonet's decipherments for the States General (see K. de Leeuw, *Diplomacy &
  Statecraft* 10, 1999), British decyphers of Michell's correspondence (BL Add MS Newcastle papers; TNA SP 107), or
  other rescripts to Michell in the same code with known content. DECODE R1953 (von der Hellen to the King, 4 Jan 1752,
  KHA inv. 196) was checked the same day and is in a different, smaller code (groups under ~1650, frequent repeats), so it is no sibling of R1955.

## Contributed by WAINUT, 11 Oct 2026: R1955 in Michell's envoy code

**Key material.** DECODE R1050 (Michell to Frederick II, London 5 Sep 1752) and R1051 (London 12 Nov 1751) are Hague
copies of Michell's own reports with the contemporary Dutch decipherment written over the numbers (attributed in our
notes to Pieter Lyonet; we have not compared the hand; on Lyonet's work for the States General see De Leeuw 1999,
cited in the letter section above). DECODE's transcriptions of them (March 2020) give each line of the decipherment above its cipher line.
Pairing them token by token gives 512 code-word pairs for 271 codes; 5 lines with unequal counts are skipped. The code
held over the ten months between the two reports: 40 codes occur in both, 32 with the same commonest value; 4 more
differ only by inflection or by a tie between variants (*continuer*/*continue*, *dernier*/*dernière*, *on*/*l'on*,
*d'*/*d*), and 4 disagree (800, 1005, 1805, 2341).
The table derives from DECODE's transcriptions, so neither it nor they are committed here. `targets/michell1751/key1751/scripts/envoy_key.py
<folder>` rebuilds it from DOC_R1050_*.txt and DOC_R1051_*.txt (DECODE login needed); `frozen_keys.sha256` holds the
hash of the table used on 11 Oct.

**R1955 is in that code.** The envoy table gives a value to 95 of R1955's 360 groups (26.4%), against 10 (2.8%) for
cabinet v1 and 20 (5.6%) for v2; on R1957 (`targets/michell1751/`) it gives 30 of 548 (5.5%). Adjacent decoded words in R1955 form attested
French word pairs more often than chance (`targets/michell1751/key1751/scripts/coherence.py`): 19 of 30 adjacent pairs, against a mean of 11.1 for
2000 permutations of the same values (p = 0.001), with word pairs taken from our corpus of 18th-c. diplomatic French
(French paragraphs of the Politische Correspondenz; the first 6 M characters used come from vols 8-13 only; spelling
partly archaised, e.g. -ait to -oit, at random; not included). With PC vols 8-9 alone as corpus the result is weaker:
14 of 30 against 9.5 (p = 0.046). The test has little power when the decoded values are mostly function words: the v1
decode of R1957, which the LCS test shows to be right, scores 26 of 44 against 23.7 (p = 0.28).

**Reading.** `R1955_reading_line.txt`, '·' for a group without a value. Legible fragments include "... avis ... sur
... negociation avec ... de Vienne ... les difficulte(s) ... article ... du ... Prince Stadhouder ... maison ... cet
avis et ... états ... depuis avis est ... ce projet ... nouvelle ... doit être ... des esperance(s) de ...". These are
fragments of a trial decoding with a table from two other letters; the subject cannot be stated with confidence beyond
Dutch affairs (the Prince Stadholder, a house, the States) and a negotiation that involves Vienna.

**Circular-letter test (negative).** Hypothesis: R1955 repeats the wording of a royal letter of the same days printed
in PC 8-9, which would then give its plaintext. The scoring rule was fixed before the results were seen
(`targets/michell1751/key1751/scripts/circular.py`): longest common subsequence of R1955's 77 decoded words with each French PC letter of vols
8-9, z against 100 shuffles; candidates are the letters of 22 Dec 1751 - 10 Jan 1752 (21), controls the other 1,329;
a candidate counts only with z >= 4 and above every control. Best candidate PC 5268 (to Michell, 4 Jan 1752), z =
2.69; highest control PC 5117, z = 4.85; no candidate qualifies. Our first run also scored five Dutch decipherments of
royal letters to von der Hellen of 3-24 Dec 1751 (Fagel 5177, our transcriptions, not included here): z from -2.01 to
0.57. Positive control (`--power`): a random 17% of the words of PC 5263 or 5262 scores z = 27.6 to 31.3 against its
source and 5.8 to 10.9 against a 50% paraphrase of it, with control maxima of 2.7 to 5.3. A shared wording would have
shown.

**Transcription of R1955 against `transcription_r1955.txt`** (`compare_tx.py R1955_tx.txt transcription_r1955.txt`): 352 of our 360 groups agree in sequence. Differences: the underlined run of nine digits
without separators on l. 16 is one unsplit group in our file (best split 2 2407 2398) and "2240? 7? 2398" there, hence
362 against 360; and 3356/3336, 194?/1949 (1949 is also our preferred reading), 247/227, 2?07/2407, 1401/1403,
1517/1857 (p. 2 l. 1), 1321/1821 (p. 2 l. 3), ours first. The envoy table has values for 247 (*me*) and 1401
(*depuis*) and none for 227, 1403, 1857 or 1821; that is weak support only.

**Against the 19 Sept notes.** We agree that R1955 is in another code than R1957, and we have nothing against its
identification as the ministerial rescript of that day. Its code is the one Michell used for his own reports to the
King (R1050, R1051); the King's immediate letters (R1957 and the six in Fagel 5177) use the cabinet code. Of the leads
listed above, the contemporary Dutch decipherments (the Lyonet lead) are the one that worked.

## Remaining gaps
- R1955, 265 of 360 groups without a value in the envoy table - blocker: no-key-material; the table comes from two decipherments of Michell's reports (R1050, R1051); further decipherments (probably KHA A31-1181) are not online, a contemporary decipherment of R1955 may be in Nationaal Archief 1.01.50 inv. 159 (not digitised), and ministerial rescripts are not in the Politische Correspondenz

## Escalation
- [x] siblings: R1953 (von der Hellen, 4 Jan 1752) checked 19 Sept, a different code; R1957 and the six Fagel 5177 letters are the cabinet code (2.8-5.6% coverage); R1050/R1051 (Michell's reports) are the envoy code and gave the table
- [x] clear-pages: the record has only the two cipher pages (P2 first); clear heading, opening and date only
- [x] known-keys: cabinet keys v1/v2 (WAINUT) tried and ruled out; the envoy table fits (26.4% against 5.5% on R1957)
- [x] print: Politische Correspondenz 8-9 searched; the ministerial rescripts are not printed; WAINUT's circular-letter test found no printed parallel text (best candidate z = 2.69, control maximum 4.85)
- [n/a] key-rebuild: a large two-part code with homophones even for de and que (296 distinct of 362 groups); the unread groups have no context to extend the table from
- [n/a] retry: no extended key exists to re-run; the trial decode is WAINUT's single pass with the full envoy table
