# Heusner von Wandersleben to Axel Oxenstierna, Kassel, 15 May 1637 (Riksarkivet, DECODE R4332 = R3816) — NOTES

Status: written up (docs/heusner1637.html)

**Verdict: already READ, by Michelle Waldispühl and Nils Kopal (HistoCrypt 2024, pp. 249–253), whose key and
plaintext are on DECODE R4332.** Catalogue entries 208 (R4332) and 209 (R3816) are resolved and removed. Added
here: R3816, catalogued separately as "not solved", is the same letter, with the same three scans in a different
order; the letter's own date is 15 May 1637, not 15 March as both DECODE records have it; and an independent check
of the key on a fresh transcription of one page. Session 2026-09-21.

## Sources

- DECODE R4332 `Riksarkivet_Wandersleben_Oxenstierna_1637` (status Partially decrypted, homophonic, numerical, 5
  pp.): three page images `IMG_R4332_I25971_P1–P3.jpg`, three 5 KB placeholder PNGs, the key
  `DOC_4332_2024-Mar-26…txt` (letter homophones, a list of sixteen three-digit codes left as themselves, and
  three clear date phrases) and the plaintext `DOC_4332_2026-Jul-15…doc`. Fetched with the shared cookie by
  `decode/get.py` into the git-ignored `targets/heusner1637/decode/`.
- DECODE R3816 `Oxenstierna` (status Non-decrypted, 3 pp., "March 1637, encipher letter, not solved"): images
  `IMG_R3816_I23156_P1–P3.jpg`. MD5 check: R3816 P1 = R4332 P1, R3816 P2 = R4332 P3, R3816 P3 = R4332 P2.
  **The same scans, so the same letter.**
- Waldispühl, M. & Kopal, N. 2024. "Decipherment of a German encrypted letter sent from Sigismund Heusner von
  Wandersleben to Axel Oxenstierna in 1637". HistoCrypt 2024 Proceedings, 249–253.
  https://doi.org/10.58009/aere-perennius0116

## The system

Clear German with enciphered words and phrases set inside it. One- to three-digit numbers: a homophonic alphabet
of 22 letters with 1 to 8 values each (E: 8, 30, 31, 61, 100, 110, 120, 200; H: 5, 29, 55, 85, 102, 202; K and P
one value each), no word division inside the cipher runs, and three-digit numbers (147–808) for names and places,
which the solvers left as numbers. The key file lists 47 under both O and U.

## The reading (Waldispühl & Kopal)

Heusner reports from Kassel that he fled Banér's displeasure and the Saxon side (Franz Heinrich of Saxe-Lauenburg,
"wegen der Hamburger sache") to 164; the court there has turned: "HERR UND KNECHT SEHR GEENDERT UND AM GANZEN HOFE
AUSSER DER 503 NICHT EINER MEHR UFFRECHT SCHWEDISCH", 628 favours those who opposed 503 and wanted to hand over 764;
a campaign is talked of, "WOHIN IST STILL", the force is not there; 385 hundredweight of metal secretly melted
down and taken covered to 147 to be cast into guns ("STUCKE"); JOHAN VON UFFELN to be commandant of 571, GUNTEROT
to take the field. Ends "CASSEL den 15. May 1637".

## Check made here

`transcription_p2.txt`: the figures of DECODE image P1 (letter page 2), transcribed from the scan here: 259 tokens,
75 distinct including separators (`_check_profile.py --measure`). The published homophone table applied to it
gives ZUWIEDER GEWESEN … UBERGEBEN … NEGOCIIREN … FORCE … BASTANT … AUS DEM LANDT ZU TREIBEN … BESTALLUNG …
GELDER … GROSSES HERANTZ … RECHT IM DIRECTORIO FASSEN, identical to the published plaintext except for three
slips in this transcription (SOHL/SOLL, FEOD/FELD, CLAM/CLAR).

## Open

The three-digit codes: 147, 164, 184, 255, 289, 321, 384, 385, 503, 571, 617, 628, 703, 708, 747, 764, 808 (747
is in the plaintext but not in the key file's list). Context only: 164 is where Heusner withdrew to (Kassel
itself? the letter is dated there); 503 is the one person at court still Swedish-minded and "SOLL IN DAS FELD",
most likely Landgrave Wilhelm V of Hesse-Kassel (grade M); 147 is where the guns are cast. Not pursued: the
Hessian correspondence would settle them.

## DECODE update queued

`decode_updates/queue.json` (heusner1637): R4332 date 15 March → 15 May 1637, key re-check, 747 missing from the key file; R3816 marked as a duplicate of R4332 (proposed Partially decrypted, date and place filled). Not sent: needs write access.

## Brice Dudout: shelfmark of the original (credit added 4 Nov 2026)

Brice Dudout's report of 2 Nov 2026 (issue #208) gives the location of the original letter. It is in the Riksarkivet, Oxenstiernska
samlingen, Axel Oxenstierna, letters received, vol. E 622 A "Henckell-Heydt" (SE/RA/720701/II/01/B/I/E 622 A). The
volume is catalogued "1637 mars, i oupplöst chiffer", which is probably where DECODE's "not solved" comes from. It
is not digitised on the Riksarkivet portal (an analog copy only). Credited `dudout`, role "pointer".
