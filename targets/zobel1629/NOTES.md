# zobel1629: Johan Zobel to Christian IV, Paris, 20 Sept 1629 (catalogue 2540, Rigsarkivet TKUA Frankrig B.31, unit 261292, images 241-242)

Status: read in part (Malcolm McBratney with Claude, 12 Nov 2026, issue #456; integration check 12 Nov 2026). 15 of 19 cipher words read without emendation = 78.9% by the README read bar; the other 4 each need one figure added, doubtful or supplied. Key partial: two of the four number alphabets are rule-fixed, the other two have values only for letters seen. Open: the cover letters D., H., G., B., Bp., Bo. and the transcription's doubtful figures.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic), as GitHub issue #456 with two comments (a second and a blind third transcription). The issue carried the key, the word table with all 134 letter figures, the reading, translation and counts, but no files; the files here were laid out from the issue text at integration. Catalogue entry **2540** (Daniel Bourdeau, Rigsarkivet TKUA sweep, 11 Nov 2026).

## Document

Copenhagen, Rigsarkivet, TKUA Speciel del, Frankrig, Gesandtskabsrelationer fra Johan Zobel 1627-31 (B.31), unit 261292 (Arkivalieronline epid 19852643), image 241 (right page, 21 lines) and 242 (left page, 17 lines, signature; the address is on the outside). German letter of Johan Zobel, Danish resident in Paris, to Christian IV, with 19 words replaced by runs of numbers; the pencil date at the foot of 241 is "1629 20/9". Persons and states appear as single capital letters in the clear (D., H., G., B., Bp., Bo.). No decipherment on or beside the leaves. Images: api.rigsarkivet.dk/ao/v1/images/48879224 and 48879225 (plain curl works; 4550 x 3436 px).

## System and key (`key.tsv`)

Each cipher word is `index, f.f.f.f`: the index number 28-39 selects one of four alphabets for the 24 letters a b c d e f g h i k l m n o p q r s t u w x y z (i = j, u = v); the letters are the figures 4-27.
- 28-30: a=4 ... z=27 (straight), rule-fixed; 31-33: a=27 ... z=4 (reversed), rule-fixed. The contributor tested all 48 straight and reversed alphabets: a=4 straight is the only one giving words for the 28-30 words, reversed a=27 the only one for 31-33.
- 34-36: a b e g f h l m n = 15 16 19 20 21 22 25 26 27 (rising, with f and g changed over), o r s t u = 12 10 9 8 7 (falling), z = 14. Not seen: c d i k p q w x y. The values g=20 and f=21 were fitted to figures a hypothesis wanted otherwise (declared).
- 37-39: e g = 25 27; i k l n = 8 7 6 4; r = 14. Seen in three words only; the rest of this table is open.
- Found by the contributor from the ciphertext alone: cribs seen while transcribing (WAFFEN, ZOBELN, WALLENSTEINS, FRIDRICHEN) gave the straight table; the reversed table from the test of all alphabets; the third and fourth from word fits. The key was found while reading, before the transcription was frozen (his own account).

## Reading (`reading.md`, `translation.md`)

The 19 cipher words decode, with the key, to waffen, protec(tion), stas stralsunt (STA[T]), krieg, zobeln, zobel, einge#il (EINGE[W]IL), auf, zobel, krieg, vornembsten, friden, investitur, wallensteins, meklen, herzog, fridrichen, stifter, stll (ST[A]LL): `decryption.txt`. Zobel tells Christian IV that "D." has an eye on "H." whose arms are fortunate, that he handed over the letters on the protection of Stralsund, that the king should call him home, that Wallenstein's investiture with Mecklenburg cannot please the king, and that good people would risk a black eye to put Duke Frederick back in his bishoprics (the English is the contributor's). The reading of the clear text is the contributor's from the scan.

## Count

| Rule | Read | Of | Share |
|---|---|---|---|
| README bar (the contributor's strict count, identical): a word is read only if every figure gives the letter it needs | 15 | 19 | 78.9% |
| Contributor's harder count (also auf, krieg, vornembsten, herzog hold a value fitted from a single word) | 11 | 19 | 57.9% (his figure) |

Emended words (holes): word 3 STAS for STAT (the figure written above the line is 9 = s, the key wants 8 = t), word 4 KRIEG (third figure 4 or 8), word 7 EINGE#IL (ink blot), word 19 STLL (an a missing, third figure overwritten). 134 letter figures in 19 words, 131 give a letter. A pointer: the third reader of the issue comments decoded his own transcription with the key unchanged at 16 of 19 words (84.2%); the second reader's 14 of 19 (73.7%): the contributor's figures.

## Integration check (12 Nov 2026)

- Decoder written here from the four alphabet rules and the word table: all 19 words and the 134-figure count reproduce.
- Images 241 and 242 compared at full size: the 19 index figures and all letter figures agree with the table, including the added 9 above the line in word 3, the blot in word 7 and the overwritten figure in word 19. The clear German of lines 1-6 of 241 and of the cipher lines of 242 agrees with the contributor's reading.
- Control: German language model (`lang`, de-modern) puts German first; the decode scores -3.87 per letter, and 0 of 2,000 random letter relabellings reach it (best -6.62). The contributor's own: 0 of 5,000 shuffled and 0 of 5,000 random keys (best -3.5974, true -2.9761). `docs/_validate.py` (133 read tokens, 1.5 per type) gives "underdetermined": too few tokens per type for its overfitting test, so the test neither confirms nor refutes the key; the key rests on the rule-fixed tables and on words that read.
- Order of events, by the contributor's record: md5 5f3df4a8bf2142faef091c1cf373d316 for the frozen first transcription (12 Nov 04:05:57 UTC) and an RFC 3161 time of 04:14:03 UTC for his manifest are stated in the issue; no files were sent, so neither was recomputed.
- Not checked: the clear text beyond the cipher lines against the images, the contributor's shuffle scorer, Fridericia and the other printed sources.

## Remaining gaps
- letters not seen in tables 34-36 (c d i k p q w x y) and 37-39 (all but e g i k l n r) - blocker: no-key-material; only 19 cipher words are known in this cipher
- four emended words (STA[T], KR[I]EG, EINGE[W]IL, ST[A]LL) - blocker: illegible; single figures doubtful, blotted or overwritten on the images
- cover letters D., H., G., B., Bp., Bo. - blocker: no-key-material; G. = Christian IV from context, the others the contributor's guesses; the clear letters of 16-19 Sept 1629 (images 231-240) may settle it
- three clear words after "ZOBEL hette bey wehrendem KRIEG dem G." and clear words marked (?) - blocker: illegible; read from the scan only
- priority and the printed record (Danmark-Norges Traktater, Opel, Lindenfels, Franksen, the packet "Chiffer" no. 112) - blocker: needs-physical-access; not reached by the contributor

## Escalation
- [x] siblings: neighbouring leaves 239, 240 and 243 viewed by the contributor for the catalogue: no gloss; the packet "Chiffer" (no. 112) not examined
- [x] clear-pages: no decipherment on or beside the leaves (images 234-250 viewed by the catalogue sweep)
- [x] known-keys: Haxthausen cipher of 1819 (Cryptiana): same index-switching family, a different key
- [x] print: Fridericia 1876, Bippen, Danske Magazin, Danske Samlinger, Historisk Tidsskrift, DECODE, Cryptiana searched by the contributor: nothing
- [x] key-rebuild: tables 34-36 and 37-39 built from word fits; no further values can be reached from 19 words
- [n/a] retry: all 19 words were decoded with the final key; the four emended words stay as the images allow
