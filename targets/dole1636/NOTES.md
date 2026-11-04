# Siege of Dole, June-July 1636: the "points" cipher of the Parlement and Antoine Brun (BM Besançon Ms 1594)

Status: in progress. Not yet written up: no site page or README row. Classed read (96.9%), so it is ready for the /writeup skill. The status below is the contributor's.

Status: read (Brice Dudout, 4 Nov 2026; key recovered and validated; fols. 191 + 127v 128 words, 113 certain, 11 probable, 4 unresolved = 96.9%; clear text already printed by Longin 1912, found after the reading).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Not in the catalogue; no DECODE record.
To be shown on https://bdudout.github.io/europe-chiffree/en/documents.html#girardot-1636 (if published).

## Documents

Besançon, Bibliothèque municipale, Ms 1594 (Ms 1591-1595 vol. IV, papers of Jean Girardot de Nozeroy, lord of Beauchemin):
letters from besieged Dole (siege by Condé, 27 May - 15 Aug 1636) to the relief army of the Marquis of Conflans and Girardot.
fol. 200 (22 July, two blocks glossed in the margin at the time), fol. 191 (Antoine Brun, [1 July], no gloss), fol. 127 (7 June,
recto glossed, verso not), fols. 181 and 183 (25 June, two ciphered copies) with the period clear copy fol. 182. Images:
Mémoire vive (Besançon); not reproduced here. The numbers are given as read.

## System and key

simple substitution, one number per letter (1-54), numbers separated by points, inside clear text; a = 35, b = 31 ... p = 1 going down by two, q = 36, r = 38 ... u = 44 going up; 20 is a second c. Full key (`key.tsv`): p=1 o=5 n=7 m=9 l=11 i=15 h=17 g=19 c=20 f=21 e=25 d=27 c=29 b=31 a=35 q=36 r=38 s=40 t=42 u=44 x=50 y=52 z=54. Learnt on fol. 200 block 1 (177 numbers aligned 1:1 with the
marginal gloss), frozen; 17, 21, 50 from the gloss of block 2 after the measurement; 20 = c from sense; 54 = z from fol. 182.
No number for k seen. fol. 106 (12 Aug) uses another cipher (not broken): the court had warned three times that "the enemy has
found the key of the cipher" (Longin nos. CCCXXI, CCCXXXII); Richelieu had sent Antoine Rossignol to Condé's camp with the
decipherment of the Dole letters (Longin no. CCLXXVIII).

## Validation

One pre-registered measurement on held-out fol. 200 block 2 (341 numbers) against its period gloss: letter agreement
0.9072 vs 0.229 at best for 200 shuffled keys (`validation.txt`). After the reading, the mechanical decryption
agrees with Longin's printed clear at 0.967 (fols. 191 + 127v) and fol. 183 matches fol. 182 apart from vous/nous, ou/a.

## Reading

`reading.md` (French, tagged, with the count and Longin's text under each line), `translation.md` (English), `decryption.txt`
(mechanical). Count by Daniel's rule, made mechanically on the published text: fols. 191 + 127v 128 words, 113 certain,
11 probable, 0 restored, 4 unresolved = 96.9%. fols. 181 + 183 (clear copy exists): 48 words,
35/9/2/2. Unresolved: a struck-out group, a word under a blot, "?atlons" (Longin: rations), "o..." (Longin: c'estoit).

## Prior work

The clear text is printed: É. Longin (ed.), "Le siège de Dole par le prince de Condé (27 mai - 15 août 1636). Documents inédits", Mémoires et documents inédits pour servir à l'histoire de la Franche-Comté, vol. X, Besançon, 1912 (archive.org mmoiresetdocum10acaduoft): nos. LIV (pp. 89-90), CXXXII (pp. 190-191), CLXXVIII (pp. 249-251), CCLXXXVII (p. 405), from Brun's drafts (Buthiers archives, Brun papers vol. VII), the words to be enciphered printed in brackets. Longin used Brun's drafts, not the letters received in Ms 1594, and gives no key.
Contribution here: the transcription of the cipher, the key, and a reading made from the numbers alone (before Longin was found).
Differences from the draft: "par son altesse" (draft "par S. A."), "à plain" (draft "à plein"); Longin also brackets
"de Mercy et de Forgats" and "accueillir", not read on fol. 191.
