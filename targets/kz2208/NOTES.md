# Admiralstab telephone message K.Z. 2208, 19 October 1914

The **Schieber I setting is 376**. A contemporary typewritten decipherment in the German Admiralty Staff’s aviation files confirms all four paragraphs of the telegram. The manuscript is in National Archives microfilm publication T1022, roll 1061, frame 35. The typewritten copy is on roll 1056, frame 800. [Original ciphertext](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-1061/T1022-1061.pdf#page=35) · [Complete contemporary decipherment](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-1056/T1022-1056.pdf#page=800)

## German plaintext

This transcription follows the typewritten copy with line breaks joined and the dispatch time reference normalized.

1. Bei Hochseechef anregen, bei Unternehmungen gegen Firth of Forth ein Unterseeboot mitgeben oder entsprechend ansetzen.
2. Für Hochseechef. Es wird angestrebt in den nächsten Tagen die Einnahme von Dünkirchen und später Boulogne. Es ist zu erwarten Teilnahme feindlicher Seestreitkräfte an der Verteidigung. Daher U-Boote bereithalten zu dortiger Verwendung, sobald jetzt im Kanal befindliche U-Boote zurück sind.
3. Halte auch U-Boote in Ostsee für englisch. Seine Majestät der Kaiser ist einverstanden mit der Verwendung der VIII. Flottille in der Ostsee, bis Unterseeboot-Gefahr abgewendet. Spätere Regelung im Sinne des Fernspruchs vom 19. X., 3h30 nachm., Ziffer 5, ist genehmigt. Hochseechef und Ostseebefehlshaber benachrichtigen. Gez. v. Pohl.
4. Armee gebraucht die in Namur aufgestellten Ballon-Abwehrkanonen. Ersuche sofort festzustellen, ob und wann wir die dortigen Luftschiffhallen in Schutz nehmen können.

## How the key was checked

The forwarding draft for K.Z. 2219 restates the submarine proposal with *Firth of Forth*, *Unternehmungen* and *ein Unterseeboot*. The known *Verkehrsbuch* (VB) group for *Unterseeboot* is `65873`. Setting the three strips to `376` turns it into `67683`, as in the manuscript. It also gives `37013 → 35343` for *Chef der Hochseeverbände*, `67485 → 65775` for *Unternehmung*, and `39887 → 37477` for *ein, eine*. The same setting appears in an independently deciphered Admiralty Staff message of 28 October. [Forwarding draft](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-1061/T1022-1061.pdf#page=33) · [Schieber I](https://www.ww1ciphers.com/chapter/verkehrsbuch-substitution-with-sliders) · [28 October comparison](https://www.ww1ciphers.com/message/nara-rg242-t1022-r1122-0764-vb)

The High Seas Fleet’s 20 October war diary reproduces sections 1 and 2 as forwarded in K.Z. 2219. It gives *Von da aus später Boulogne* and uses *daß teilnehmen*. The incoming manuscript and the complete decipherment have *und später Boulogne*, and the latter confirms *Teilnahme*. The separate Great Headquarters copy of section 3 confirms the Kaiser’s assent, the condition about the submarine danger, and the reference to point 5 of the 3:30 p.m. dispatch. The complete decipherment gives the ordinal VIII, obscured in the bound headquarters copy. The Baltic commander’s war diary independently records the VIII Flotilla’s temporary assignment. [Fleet war diary](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-0141/T1022-0141.pdf#page=380) · [Great Headquarters plaintext](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-1202/T1022-1202.pdf#page=25) · [Baltic command war diary](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-0147/T1022-0147.pdf#page=766)

## Ciphertext readings

The [group worksheet](reading.tsv) records 43 group occurrences, including 26 exact matches from independently deciphered VB telegrams. Faded digits are restored where the group and plaintext agree, including `43532 → 40282` (*feindlich*), `40693 → 46853` (*Kanal*) and `14335 → 14185` (*englisch*). The full copy confirms the parallel readings `45736 → 41086` (*VIII. Flottille*) and `63596 → 60256` (*in Schutz nehmen*). [Original TIFF](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-1061/T1022-1061-00035.tif) · [Complete contemporary decipherment](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-1056/T1022-1056.pdf#page=800)

- The Namur group appears to read `02942`, which yields `08692` outside the VB range. Changing the initial digit gives `22942 → 28692`, the independently attested group for *Abwehr*. The typewritten copy confirms *Ballon-Abwehrkanonen*. [Independent *Abwehr* example](https://www.ww1ciphers.com/message/nara-rg242-t1022-r0447-0718-vb)
- The apparent manuscript readings `69485 → 67775` and `39306 → 37166` are outside the expected alphabetical positions for *Verteidigung* and *bereithalten*. Both plaintext readings are clear in the typewritten copy and the fleet’s forwarded version. The intended numerical groups remain unverified. [Complete contemporary decipherment](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-1056/T1022-1056.pdf#page=800) · [Fleet war diary](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-0141/T1022-0141.pdf#page=380)

Run `python deslide.py` from this directory to check the group worksheet. The script checks both directions and includes a worked example using setting 718 as a control. A headquarters telegram dated 16 October refers explicitly to the third edition of the *Verkehrsbuch* and reports that frequently used aviation terms were missing. The National Archives at Kew lists a physical copy of the 1908 codebook under ADM 137/4374. [K.Z. 2062](https://catalog.archives.gov/medialz/dc-metro/rg-242/315246058/T1022/T1022-1044/T1022-1044.pdf#page=362) · [Kew catalogue](https://discovery.nationalarchives.gov.uk/details/r/C4116045)

## Transcription doubts

- 1?677 (§2, Dünkirchen) - read: 11677; checked: image, decode, transcription; the second digit appears to be 1 on the TIFF, the published reading has 4, and the resulting VB entry is between Dover and Durban.
- 4?532 (§2, feindlicher) - read: 43532; checked: image, decode, transcription; the faint second digit fits 3 and gives independently attested VB 40282. The plaintext copy reads feindlicher.
- 4?6?3 (§2, Kanal) - read: 40693 by reconstruction; checked: image, decode, transcription; digits 2 and 4 are indistinct, and attested VB 46853 plus the contemporary readings identify Kanal.
- 14??? (§3, englisch) - read: 14335 by reconstruction; checked: image, decode, transcription; the opening digits are visible and independently attested VB 14185 supplies the rest at setting 376.
- 02942 (§4, Abwehr) - read: 22942 by emendation; checked: image, decode, transcription; the pencil first digit appears to be 0. Substituting 2 yields the attested Abwehr, as in the typewritten compound.
- 69485 and 39306 (§2) - read: unresolved numerical correspondence; checked: image, decode, transcription; the apparent groups yield VB positions outside the expected alphabetical ranges, while the typewritten copy and the forwarded order agree on Verteidigung and bereithalten.
