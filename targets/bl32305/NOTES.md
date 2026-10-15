# BL Add MS 32305: the Paris 1719 code letters, R2964 and R2965 (catalogue #78)

Status: attempted, open. Worked 21 Sept 2026.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This entry is the Paris 1719 code (R2964,
R2965). The Carré letters of 1742-45 (R2968, R2970, R2972), filed here until then, are another code and are now
[`targets/carre1742/`](../carre1742/NOTES.md) (a different cipher, with its own page). The other records of the volume
(table below) were read at the time in their own ciphers and are context, not documents of this entry.

## The volume

BL Add MS 32305 is catalogued as 39 folios of "unidentified cipher keys". The DECODE records R2963–R2981 show that it is a
codebreaker's working file of intercepted letters, most of them deciphered between the lines at the time. Catalogue
entry #78 grouped six records (R2963, R2964, R2965, R2968, R2972, R2974) under "Unknown sender (Paris)". They are not one
correspondence. All nineteen records R2963–R2981 were viewed (R2975–R2981 on 21 Sept, key hunt) (images via the DECODE cookie, git-ignored in `img/`):

| Record | Folio | What it is | State |
|---|---|---|---|
| R2963 | f. 5 | German letter to a "Marquis", 28 Jan [1719?], figures for names and words (1203 = London, 1439 = Theophili…) | deciphered interlinear at the time: **read** |
| R2964 | f. 6 | "A Mr [struck out]", Paris 7 Feb 1719, *Extrait*, French, clear with a 3-figure code | **open**: ~a dozen values glossed |
| R2965 | f. 7 | Paris 10 Feb 1719, *Extrait*, same code, same writer ("Vos Parens", "votre Cousin") | **open**: same glosses |
| R2966 | f. 8 | French letter, 2-figure letter cipher (20 = a, 97 = s…) | deciphered interlinear: read (not in #78) |
| R2967 | f. 10 | London 4 and 11 July 1740, French, a few code groups (0813 = le Sr Walpole) | glossed: read (not in #78) |
| R2968 | ff. 11–12 | "Anonyme à Monsr Carré en Pellmall à Londres", March 1742, all figures (3-figure, ≤ ~800) | **attempted, closed**: transcribed, two-part code, nothing glossed |
| R2969 | f. 13 | "Carré 1742": a frequency count of R2968 + R2970's groups (686 ×20, 212 ×19…; tentative 686/106 = de, 121 = la) | not a key |
| R2970 | ff. 14–17 | "Copie d'une Lettre en Chiffre, sans date", to Mr Carré, Palmal, under cover to Mr Chevening(?), jeweller near Charing Cross; same code as R2968; endorsed "R Aug. 22 1742" | **attempted, closed**: two-part code, transcribed (merged into #78) |
| R2971 | ff. 18–21 | French, 4-figure code (≤ ~4600), Queen of Hungary; pencil "Carré 1742" | deciphered interlinear: read (not in #78) |
| R2972 | ff. 22–23 | "Lond. 19 Janv. 1745", all figures, same code as R2968 (212, 771, 283, 606…) | **attempted, closed**: transcribed |
| R2973 | f. 24 | 6 March 1749, Vienna/Petersburg accession, code groups | glossed: read (not in #78) |
| R2974 | ff. 25–28 | "L. 17/28 Nov. 1749", 2-figure letter cipher | deciphered letter by letter: **read** |
| R2975–R2978 | ff. 29–33 | Dec 1749 – Jan 1750 (some Dresden), French, 2-figure letter cipher | deciphered interlinear: read (R2978 = #79) |
| R2979 | f. 34 | Hague 9 Aug 1753, "Hanau to Fer.", 4-figure code in a clear letter | decipherer's working copy, glossed in part: read in part at the time (#79) |
| R2980 | ff. 35–36 | "A Mr de H.", London 8–12 Dec 1758, continuous 2-digit cipher | deciphered: read (not in #78) |
| R2981 | ff. 37–39 | L. 12/23 Jan 1759, 2-figure letter cipher | deciphered: read (not in #78) |

So of the six catalogued items, R2963 and R2974 were read at the time, and R2964, R2965, R2968 and R2972 are open (R2968/R2970/R2972 now carre1742).

## The Paris 1719 code (R2964, R2965)

A letter from Paris, written a few days after Lord Stair's formal entry (5 Feb 1719 NS), to a correspondent in England
who is told he will stay there "jusqu'au retour de S. M. Brit." The tone ("vos Parens", "votre Cousin", "le caractère des
esprits de votre Famille") is that of a cover vocabulary, probably Jacobite or Spanish-side (Alberoni is named).
`R2964_transcription.txt` gives the whole of f. 6: **354 figure groups, 191 distinct, 116 seen once, highest 900.**
The decipherer's glosses (both letters): 36 = re, 88 = pas, 95 = le, 184 = que, 243 = vous, 347 = a, 531 = pour,
652 = qu'il, 786 = s; crosses mark 27, 258, 285, 611 as persons.

The glosses are not in alphabetical order (re 36 < pas 88 < le 95 < que 184 < vous 243 < a 347), so this is a two-part
code, and its order cannot be used. With about 700 groups in the two letters for a code of about 900 entries, most
values occur once. A ciphertext-only break is not feasible from this material; the decipherer of the time stopped at the
same place. What would move it: the key, a clear copy, or more letters in the same code elsewhere in the BL/SP 107 files.

## The Carré code (R2968, R2970, R2972): split off

The three letters to Mr Carré in Pall Mall (1742-45) are a different two-part code (~800 entries, 1,323 groups, no
gloss). Their transcriptions, statistics, solver runs and key hunt are now in
[`targets/carre1742/`](../carre1742/NOTES.md) (a different cipher, with its own page), with the `carre/` folder, since
14 Oct 2026.

## Prior art

Checked: the BL catalogue description (unidentified cipher keys) and a web search for the shelfmark; no edition or
study of these letters found. DECODE has no transcription files for any of the records.

## Catalogue #79: R2978 and R2979 (checked 21 Sept 2026)

The rule scorer made "Unknown sender (Dresden) to unknown recipient, 2 ciphertexts, 25 Jan 1750 – 9 Aug 1753" out of
the last two records of the file. Both were viewed at full resolution. They are two unrelated items, and neither is open:

- **R2978, f. 32 (4 pp.)**, "Dresde 25. Janv. 1750", French, a 2-figure letter cipher (e.g. 93 = s, 24 = t, 54 = d,
  12 = n). The contemporary decipherer wrote the plaintext letter by letter over every line ("…que l'on ignore pas les
  dangers auxquels notre position nous expose… les insinuations de Mr de Guydickens…"). Read at the time.
- **R2979, f. 34 (2 pp.)**, "Hanau to Fer.", "Hague, 9 Aout 1753". This is not the intercepted letter itself. It is the
  decipherer's working copy: the clear syllables written out, the unread 4-figure groups (up to about 3300) left as
  figures, with glosses over the groups he had worked out (1688 = si in "con-si-derable", 3227 = Devonshire, 1560 = roi,
  1808 = Lor…). The second page ends "Ici on parle du mariage de 3245 avec 3263" and a column of question marks. Read in
  part at the time. The code is syllabic and word-level; from one working sheet, most of the unglossed groups occur once,
  so no new reading was attempted.

Catalogue #79 was removed as read at the time.

## Remaining gaps
- R2964 and R2965, the code groups not glossed at the time (321 of 354 groups in f. 6; R2965 not transcribed) - blocker: no-key-material; a two-part code of ~900 entries whose order gives nothing, about 700 groups in all and most values seen once; no key, clear copy or other letter in the code found

## Escalation
- [x] siblings: all of Add MS 32305 on DECODE viewed (R2963-R2981); no other letter in the 1719 code, no key sheet
- [x] clear-pages: the letters are clear French with code runs; the clear text is the context, not a decipherment; the interlinear glosses (36 re, 88 pas, 95 le, 184 que, 243 vous, 347 a, 531 pour, 652 qu'il, 786 s) are transcribed
- [x] known-keys: none known for 1719 Paris; the volume's other codes (R2963's figures, Carré 1742-45, R2971) are different systems
- [x] print: BL catalogue and a web search for the shelfmark: no edition or study
- [n/a] key-rebuild: the glosses are not alphabetical, so a two-part code; its order cannot bracket the rest, and with ~700 groups for ~900 entries most values occur once
- [n/a] retry: nothing beyond the contemporary glosses was read
