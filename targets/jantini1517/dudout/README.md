# Fantini 1518 (R1126): the key, and the contemporary plaintext copy on pp. 3-4 (Brice Dudout)

Status: read; contemporary plaintext copy identified on pp. 3–4 (Brice Dudout, 28 Oct 2026; 469 of 492 words read by sense, 95.3%, of which 290 sure; probable and restored words rest on that copy).

## What is new

The text itself is not new: pp. 3-4 of the same letter give it in clear. The contribution is the key (identical in
system to Caprile 1519), validated blind against that contemporary copy, and the identification of the copy.


1. **The cipher is the Caprile 1519 family.** Our Caprile 1519 key (C05a, rebuilt from R1129-R1133 against the 1882
   decipherments and validated on held-out R1135/10b, 0.736) was applied unchanged to this folder's transcription
   (`c_v6` / `t1126_p1c` + `t1126_p2final`). On a portion designated in advance (p. 2 lines 13-26) it ranks 1st of 201
   against 200 shuffled keys, both on characters (4-gram log-prob per letter -2.17 vs best control -2.92) and on words
   (letters in Italian words 0.38 vs 0.25). "7 9" (bare 7, then 9) = 9/7 = c, so "7 9 m^b" = "che" (30 times).
   NOTES.md's conclusion that "Caprile's 1519 key does not fit" came from the 20 or so values tried (R1130/4c), not from a full key.
2. **Pages 3-6 are not only the continuation of the letter: pp. 3-4 give the ciphered passage in clear.** P. 3 begins
   "de la quale dubito assai assai essendo passato il tempo …", the first words of the cipher, and the parallel runs to p. 4
   l. 19 ("… in tempo che … li nostri"). Transcription: `R1126_pp3-4_period_cleartext.txt` (Vestigia 1849 images 3-4).
3. **Blind validation against that clear copy.** Key K2 (`key_K2_blind.json` = C05a + 14 cells set by sense on p. 1 and
   p. 2 lines 1-12) was frozen (SHA-256) BEFORE the clear copy was opened. Monotone alignment of its decryption with the clear
   copy: p. 1 0.765, p. 2 0.667 letters right, against 200 shuffled keys at most 0.349 / 0.335 (mean 0.33 / 0.32).
   The Caprile key alone already gives 0.681 on p. 1. Control on R1127 (5 faded lines, never decrypted before): rank 1/201 on
   both measures, but too short to be conclusive.
4. **Reading key** `key_K3v2_reading.json`: K2 + cells learnt from the alignment with the clear copy (not a validation).
   Signs merged: "-/X -/9" -> X+9 (n+9 = fa/sa), "-/X -/y" -> X+y (n+y = ge, 7+y = i). Four bracket signs relabelled
   after checking the Vestigia images ([o] round = ro vs [ɔ] = tu; [9] = sa vs [b9]), see `R1126_transcription_v2.txt`.
   f/x at the end of a line is a nomenclator sign for "Re (de Ungaria)" (cf. the 1882 note on Caprile 6c: "X^t = Re d'Hungheria").

## Reading and count (Daniel's rule)

`R1126_reading.md`: 492 words, sure 290 (58.9%), probable 125 (25.4%), restored by sense 54 (11.0%), unresolved 23 (4.7%)
-> 95.3% read by sense. Each probable/restored word rests on the contemporary plaintext copy at the same place; the line notes say
what the key gives. An automatic word-by-word comparison with the clear copy (no judgement) gives 91.4%. Caveats: one
reader; the margin over 95% is thin; the sure class alone is 59%; the transcription was checked on the images only for the
bracket signs [o], [9], [t] (the rest is this folder's transcription).

Content: the Hungarian diet of 1518, the eight lords appointed to govern for the young Louis II, the Cardinal of Esztergom
(Bakócz) and the palatine (Perényi) keeping power, a one-ducat hearth tax refused by the counties, a planned meeting at the
feast of St James, and Fantini's opposition to sending the nobles' troops on raids against the Turks.
English translation: `R1126_translation.md`. Decryption line by line: `R1126_decryption.txt`.

Files: `R1126_transcription_v2.txt`, `R1126_pp3-4_period_cleartext.txt`, `key_K2_blind.json`, `key_K3v2_reading.json`,
`R1126_decryption.txt`, `R1126_reading.md`, `R1126_translation.md`. No archive images are included.
