# NAF 11355: Prince Napoléon key (June 1859), f12 alignment and dictionary v2

Contributed by Jozef Krajčovič (kjfriedo) for issue #194, 5 Nov 2026. CC BY 4.0 for the alignment, dictionary and annotations.
The images are reproductions from the Archives nationales (Fonds Napoléon, 400AP). Reproduction is authorised under AN terms; credit "Archives nationales, 400AP/…".

## Files
| file | content |
|---|---|
| `f12_alignment_v2.tsv` | the 135 groups of f12r → plaintext unit, with tier. Columns `group code meaning tier`. The `code` column is identical, group for group, to the f12r rows of `prince_family_tokens_f7_f10_f11_f12.tsv`, which was checked by script. |
| `prince_key_dictionary_v2.tsv` | 149 codes: `code meaning tier occurrences note` |
| `images/` | the six AN pages the external values come from (greyscale, 1400 px) |

SHA-256 values:
- `f12_alignment_v2.tsv`: `9c94a0a2013d2795b28b388760593ccc5741c1fe019efaafd98af97be606b7ff`
- `prince_key_dictionary_v2.tsv`: `a23bdb3267fcb32545fa39cac83f7b83085820e740987ae7f3a57ed0a07218c3`

## Sources and images
The whole of 400AP is digitized and online in the AN Salle des inventaires virtuelle (inventory FRAN_IR_053754, "Consulter les archives numérisées associées").
Image n of a box = the microfilm frame given below. The frame can be fetched as Zoomify tiles from
`https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/<frame>/ImageProperties.xml`.

| image file | box / image / frame | content |
|---|---|---|
| `AN_400AP118_img140_f7_decipherment.jpg` | 400AP/118, img 140, `DAFANCH97_MIC027000430` | n° 42, received copy of **f7**, with values written above the groups |
| `AN_400AP118_img197_f12_minute_p1.jpg`, `…img198…p2.jpg` | 400AP/118, img 197–198, `DAFANCH97_MIC027000487`–`488` | n° 59, the prince's **minute of f12**, "(chiffré sauf ce qui est souligné)" |
| `AN_400AP144_img184_f10_received.jpg` | 400AP/144, img 184, `DAFANCH97_MIC032003599` | n° 92, Florence form of **f10**, with values |
| `AN_400AP144_img185_f11_received.jpg` | 400AP/144, img 185, `DAFANCH97_MIC032003600` | n° 93, **f11 (no. 785)** as received in Florence: 15 groups, with values |
| `AN_400AP144_img186_reply_11june.jpg` | 400AP/144, img 186, `DAFANCH97_MIC032003601` | n° 94, the Emperor's **reply to f12**, 11 June, 8.55 p.m., with values |

## Occurrence tags in the dictionary
- `f12:n`: f12r group n (alignment above).
- `f7:n`: f7r, from the decipherment written on the 400AP/118 copy.
- `f10:n`: f10r, from the Florence form.
- `f11F:n`: the Florence form of f11. These are **not** the NAF f11r ancien/nouveau groups.
- `r11:n`: the reply of 11 June.

## Tiers
- **A:** the code repeats with the same meaning, or its value is written on a contemporary decipherment (f7, f10, f11F, r11).
- **B:** single occurrence, placed by an exact group count between A anchors.
- **C:** syllable division or a guess inside a section.
- **X:** unresolved.

`~` marks a syllable fragment. `a | à` marks a homograph.

## Update v3 (17 Nov 2026): f11r deciphered, dating corrected
Licence and credit for the v3 files: see `LICENCE_v3.md` (CC BY 4.0 for the tables; images credited "Archives nationales, 400AP/…").
New source: **400AP/144 img 181**, AN microfilm frame `DAFANCH97_MIC032003596`. To see the page, open the [AN viewer for the Fonds Napoléon](https://www.siv.archives-nationales.culture.gouv.fr/siv/IR/FRAN_IR_053754), go to 400AP/144, choose "Consulter les archives numérisées associées" and go to image 181. The image is not stored in this repository; see `LICENCE_v3.md`. This is the Florence telegraph office copy: "Firenze 4 giugno 1859, ore 4 pom. — Da Alessandria li 4, ore 11.45 ant. — L'Empereur au Prince Napoléon". It gives both the *ancien chiffre* and the *nouveau chiffre*, with the value written under every group.

- **NAF f11r is the telegram of 4 June 1859, 11.45 a.m., from Alessandria.** It is not the 10 June dispatch ("Suivant toutes les probabilités…"), which reached Florence as a separate, partly enciphered form (img 185, `f11F`). Everything earlier that assumed "f11r = the d'Hauterive/Comandini text" is withdrawn: the 616 = à position test, the la/no-la discussion, and the 2774 = null idea.
- Plaintext (the same in both keys): **"Ne comptez pas pour le moment sur la division d'Autemarre; je ne puis l'envoyer par mer; vous la recevrez plus tard par terre."**
- The groups on the copy match the f11r rows of `prince_family_tokens_f7_f10_f11_f12.tsv` exactly, ancien 31 and nouveau 27 (checked by script). The only exception: nouveau position 24 is 2162 on the copy, and the decipherer noted "(1162 tard)"; the NAF has 1162.
- **f11 nouveau = prince key.** It shares 11 codes with the f12 dictionary, and 10 agree: 135, 2079, 2218, 1308, 543, 1682, 1299, plus the newly confirmed **512 vous** (f12:19), **1040 compt-** (f12:48) and **2041 par** (f12:100). The one conflict is **1344 = pas** at f12:109 (v2 had guessed "ville"). f12:108–110 are reopened.
- **f11 ancien is a separate codebook**: `f11r_ancien_key.tsv` (31 groups with values; 616 = par, 2774 = -re).
- New files: `f12_alignment_v3.tsv` (SHA-256 `e013f548…d232`), `prince_key_dictionary_v3.tsv` (165 codes: A 88, B 42, C 31, X 4; SHA-256 `5e2646f9fcea…0ce0`; changed in the scan-check commit, where the note on code 1150 was updated), `f11r_ancien_key.tsv` (`5f2d13b7…c4d0`). New occurrence tag: `f11N:n` = f11r nouveau group n, from the img 181 decipherment. The v2 files are kept for reference.

## Status (updated 17 Nov 2026)
- **Second reader.** Dan Bourdeau's project check (PR #768) read f11r on img 181 (all 58 groups) and img 366 independently, and found agreement. The other tier A values from f7, f10, f11F and r11 are still my reading of the interlinear decipherments in the images above.
- **Gallica scan.** All 215 groups (f7r, f10r, f11r, f12r) were compared with the scan (`SCAN_CHECK_AND_HELDOUT.md`). The f12 readings 1150, 1255 and 1216 are now settled. **133 vs 135:** the scan has 135 groups, so the header "133 gro." is the clerk's miscount.
- **f11r** is the telegram of 4 June 1859 from Alessandria. *Ancien* and *nouveau* carry the same text ("Ne comptez pas pour le moment sur la division d'Autemarre …", see the v3 section above). *Nouveau* is the prince key; *ancien* is a separate codebook.
- **Held-out test** (`SCAN_CHECK_AND_HELDOUT.md` §2): 10 of the 11 overlapping codes are correct. Eight of the ten are tier A codes whose values come from other telegrams' decipherments, so they show that f11r nouveau uses this code. **The alignment itself is tested only by six codes** (1040, 1344, 1682, 1299, 2041, 512), and five of them are right. The script's matching is lenient: a value counts as correct if one string starts the other. The 1344 correction ("ville" → "pas") was made after the answer was seen.
- **Still open in f12:** groups 87–97 (Lucques … littoral … Massa), 78, 108 and 110; the conflict at 799 (Luc-/lit-); and 1149 (l'A-/al-, weak).
