# fuerstenberg1659: Wilhelm von Fürstenberg to Jobst Edmund von Brabeck, Vienna, 10 July 1659 (catalogue 1645)

## Document

- Landesarchiv NRW Abt. Westfalen, W 004 (Manuskripte VI) Nr. 52. Finding aid: "chiffrierter Brief mit Schlüssel des
  Wilhelm von Fürstenberg an Edmund von Brabeck, 1659". Record: https://www.archivportal-d.de/item/I6NURLTMG3SYAWTBLDWQDF4QNEUTPEAT
- Images (LAV NRW, METS https://www.landesarchiv-nrw.de/digitalisate/Abt_Westfalen/Msc_VI/00052/mets.xml), fetched
  12 Nov 2026, one at a time:
  - 084: wrapper "Geheime Schrift nebst Schlüssel";
  - 085: letter, page 1 (https://www.landesarchiv-nrw.de/data01/Abt_Westfalen/Msc_VI/00052/MSC_VI_00052_085.jpg);
  - 086: letter, page 2, signed "Wilhelm von Fürstenberg", dated "Wien di 10 Julij 1659"; on the facing leaf the
    "Schlüssel zur Ziffer-Schrift" (..._086.jpg);
  - 087: address leaf, "A Monsieur Monsieur Jodoc Edmund de Brabeck, Doien de Munster et Signeur de ... , Munster in
    Westphalen", with the seal (..._087.jpg).
- The letter is in German with Latin phrases. Five passages (runs P1-P5, 345 letters in all, 54 words) are written
  in cipher in a separate round script, each flagged by a mark in the margin. No decipherment is written on or near
  them.

## System

The filed key is **not** the key of this letter. It is a plain-letter-to-number table (A 10, B 12, C 16 ... Z 56,
transcribed in `key_sheet_086.tsv`), while the letter's cipher is written in letters, not numbers. A search for a
letter-to-digit mapping that turns letter pairs into the table's numbers (`scripts/solve_digits.py`) finds nothing.
So this was not a lookup.

The letter cipher is a period-2 polyalphabetic substitution on the 24-letter alphabet a-z without j and v: at the
1st, 3rd, 5th ... letter of a run the plain letter is the cipher letter moved back 1; at the 2nd, 4th ... it is moved
back 8 (a Vigenère with the key "bi" on this alphabet). The count restarts at each run. Found ciphertext-only:

- the index of coincidence of all 345 letters is 0.052, but of the odd and the even places separately 0.065 and
  0.080, which points to two alternating alphabets;
- a Caesar fit of each set against German/Latin letter frequencies gives shift 1 and shift 8 (`scripts/vig2.py`),
  and the decryption reads at once.

Runs P1-P3 have even length and P4 odd; P5 decrypts only if the count restarts, which confirms the restart.

## Held-out test

The key was first found on all five runs. As a test, the two shifts were fitted blind again (letter frequencies, no
cribs) on runs P1-P3 only and applied to P4-P5, which took no part in that fit: 159 of 159 letters (100%) agree
with the reading. The reverse fold (fit on P4-P5, test on P1-P3) also gives shifts 1 and 8; 185 of 186 letters
(99.5%) agree, the one miss being the encipherer's slip in "quob" (below). `scripts/heldout.py`. The key has only
two parameters and the margins of the fits are wide (26-49 log units over the next shift), so the test is strong for
the key; it says nothing about transcription slips.

Dan's statistical validation (`docs/_validate.py`, model de-1640s) on `validation.tsv`, written by
`scripts/validation_pairs.py`: each token is a sign with its place parity (x1, x2), since the two alphabets
alternate. 345 tokens, 41 types: the reading scores -2.349 per letter, random keys -6.685 (z 10.2), a key annealed
onto the shuffled ciphertext at best -3.613 (z 20.5). Verdict: pass.

## Reading

All five runs read as sentences or clauses in their German-Latin context (reading_fuerstenberg1659.md,
translation_fuerstenberg1659.md):

- P1: a praesidente comite de Ottingen verstanden
- P2: sein wor{t?}, so Caesar von Franckfort aus in scriptis gegeben, halten wolle
- P3: princeps Aursbergius quo{b/d} princeps sit habiturus sententiam pro se sine ulla konditione doctoris Batz
- P4: dem referenten von Lindenspur versprochne siebenhundert reichsdalers uberwexelen
- P5: alles ist heut in consilio secreto in fauorem principis nulla adiecta conditione concludiret worden

In short: the president of the Imperial Aulic Council, Count Oettingen, and Prince Auersperg told Fürstenberg that
the Prince (the Prince-Bishop of Münster, Christoph Bernhard von Galen) would have the judgement in his favour
without any condition; 700 Reichstaler promised to the referent von Lindenspür were to be transferred; and in the
postscript, that everything had been concluded that day in the secret council in the Prince's favour, with no
condition attached. This may concern Galen's dispute with the city of Münster at the imperial court (not checked;
the next file in the volume, image 087 right, has a wrapper on the "Executions Sache wider die Stadt Münster",
1660).

Word counts (`scripts/reading.py check`): 54 cipher words; 53 verbatim from the signs (98.1%), one of them (wor{t?})
resting on an uncertain sign (85.4, fourth sign, written c?; if it is e, the word becomes the repair wor{w/t} and the
count 52 verbatim and 2 repaired, 96.3%); 1 with one marked
repaired letter (quo{b/d}: the sign is an open c, which gives b; the sense needs e, so most likely the encipherer's
slip); 0 from a gloss; 0 holes. Proper names and spellings are kept as the signs give them (Ottingen, Aursbergius,
konditione beside conditione in P5, Lindenspur, reichsdalers, uberwexelen). `scripts/check_marks.py` rebuilds the
decryption from transcription and frozen key and fails on any unmarked departure; it passes.

State: **read**. Strict count (README read bar): 52 of 54 words verbatim from the signs (96.3%), because the word on
an uncertain sign (wor{t?}) and the repaired word (quo{b/d}) are not counted as read signs. The contributor's own count
was 53 of 54 (98.1%), with wor{t?} counted as verbatim; it is theirs and is not used for the headline.

Dan's reading checker (docs/_check_reading.py, origin/main 54c4ecc65), recorded as it is:

- reading_fuerstenberg1659.md (whole file, with the English notes): clean share 0.48 (24 of 50 sentences; 0.45, 18 of 40, before the review notes were added);
- the five marked runs alone, one sentence each: clean share 0.40 (2 of 5). The checker judges each sentence in one
  language, and these runs are mixed German and Latin; its unknown words are names (ottingen, aursbergius, batz,
  lindenspur), period spellings (konditione, reichsdalers, uberwexelen, concludiret, siebenhundert) and, per
  language, the words of the other language. With the German and Latin word lists joined and the four names left
  aside, 4 of 5 runs are clean (P4 fails on siebenhundert, reichsdalers, uberwexelen). This variant is our own and
  is given only to explain the figure;
- translation_fuerstenberg1659.md: 0.727 (8 of 11);
- decryption_fuerstenberg1659.txt (unspaced mechanical output): 0.083.

## Transcription

Sign conventions first (SIGN_CONVENTIONS.md), then two passes by shape before any key: pass 1 on 2x crops, pass 2
on fresh 3x crops with other boundaries. They differ at two signs, settled on the image (85.8 k, 85.9 e). After the
decryption, three places were looked at again on 4x crops (work/crops/Z.png, Zb.png): the second sign of 85.2 and
the fourth of 85.4, read e in both passes, are open c's with no loop, and were changed to c (this check was made with
the decryption in mind; please look at these two signs); the third sign of "wxcys" in 85.7 is also an open c and was
left as c although it gives b for d (marked repair). In 85.7 the writer struck out a sign after "pk" and wrote d
above it; transcribed as d. After the independent review (below) the fourth sign of 85.4 is written `c?`: the
reviewer read it e at 2x and, at 4x, as a c with a small tick at the top, fainter than its neighbours. The '?' does
not count as a sign; `decrypt.py` copies it into the decryption and `reading.py` requires the mark {t?} at that
place.

## Independent review (12 Nov 2026)

An AI language-model agent that took no part in the solution looked at the images before it read the transcription,
then re-ran the scripts and Dan's reading checker and read the text as sentences against the translation.

- Blind sign spot-check, six cipher lines (85.2, 85.4, 85.7, 85.8, 86.2, 86.4): 201 of 202 signs agree. The one
  difference is the fourth sign of 85.4 (e or c; now `c?`). The reviewer read the second sign of 85.2 as c blind,
  and the third sign of "wxcys" in 85.7 as c blind too.
- `scripts/check_marks.py` and `scripts/heldout.py` reproduced (159/159 and 185/186); the held-out fit uses the
  training runs only.
- Reading: 5 of 5 runs read clean as German-Latin clauses, no holes; every word is a real word, a name or a period
  spelling; the translation matches. State **read**, grade **A**.
- Changes made from the review: 85.4 fourth sign written `c?` and marked {t?} in the reading; the P1 translation
  now brackets the supplied words ("[I have] understood [this]").

## Integration check (12 Nov 2026)

By a second AI language-model reader that is not the contributor; no human palaeographer.

- `decrypt.py`, `check_marks.py`, `heldout.py` re-run (159/159 and 185/186 reproduce); an own decoder from the two shifts
  gives the same text on all five runs.
- Controls with the German model `de-1640s`, per letter: true shifts (1, 8) -3.90; best of the other 575 shift pairs
  -7.62; mean of those pairs -9.53 (sd 0.51); 500 random substitution-alphabet pairs, mean -9.53, max -7.87; 300 within-run
  shuffles of the ciphertext under the true key, max -8.09. The five runs are 38, 60, 88, 73 and 86 letters (345 in all,
  54 words); the key has two parameters, so there is no room to overfit.
- Image 085 (Landesarchiv NRW, public jpg): the ten cipher lines of the first page, read at reduced size, agree in line breaks and signs;
  full-resolution crops of 85.4 (the fourth sign is an open c with a small tick, as `c?`) and of 85.9-85.10 agree. Image
  086 (lines 86.1-86.5) not compared.
- The filed key sheet (image 086, a letter-to-number table) is another system: the letter contains no numbers, so the
  catalogue entry's wording "ciphered letter with its key" is misleading for this cipher; the entry is closed.
- Strict read share: 52 of 54 words (96.3%), see Reading.

## Prior art (checked 12 Nov 2026)

- Two web searches (Fürstenberg, Brabeck, 1659, Wien, Chiffre; Hüttenhain Geheimschriften Münster Fürstenberg
  Brabeck) found no edition or decipherment of this letter. The vetting of 4 Nov 2026 found no DECODE, Tomokiyo or
  Lasry record.
- Not excluded: E. Hüttenhain, *Die Geheimschriften des Fürstbistums Münster unter Christoph Bernhard von Galen
  1650-1678* (Münster 1974, 101 pp.), not online; its pp. 36-41 ("Beispiele aus der praktischen Anwendung") and
  42-99 ("Wiedergabe der Geheimschriften") may describe this system or print this letter. Interlibrary loan needed.
- Collision check (12 Nov 2026): no target folder, open PR or issue on Dan's repo for Brabeck, Fürstenberg 1659 or
  W 004 Nr. 52.

## Remaining gaps

- Hüttenhain 1974 not seen: it may already print this letter or this cipher.
- The clear German text of the letter was not transcribed; the runs are placed by position and a few clear words
  only. A full transcription would firm up the context (for example who "doctoris Batz" is).
- "doctoris Batz" not identified; "Lindenspur" taken as the Reichshofrat von Lindenspür without a source checked.
- The fourth sign of 85.4 (`c?`) is ambiguous on the image: e at 2x, a ticked c at 4x. As e, "wort" becomes the
  repair wor{w/t} (52 of 54 verbatim, 96.3%). The blind reviewer confirmed c for the second sign of 85.2 and for the
  slip in 85.7; a human reader of the original would settle 85.4.
- The number key on image 86 belongs to some other cipher; which letters of the Galen/Fürstenberg correspondence use
  it (the wrapper points to the "Registratur Fürstbischof Christoph Bernhards") was not looked for.
- No human palaeographer checked the reading.

## Method note

WAINUT set the task and the rules; AI language-model agents fetched the images, transcribed, found and tested the
key, read and checked. No target-specific human intervention.
