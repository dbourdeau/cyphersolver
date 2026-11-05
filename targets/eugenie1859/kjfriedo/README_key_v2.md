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

## Status
- **Values not yet checked against the images by a second reader.** Tier A values from f7, f10, f11F and r11 are my reading of the interlinear decipherments in the images above.
- f12 groups 87–97 (Lucques … littoral … Massa): uncertain. Groups 78 and 110: unexplained.
- Conflicts: 799 (Luc-/lit-) unresolved; 1149 (l'A-/al-) weak; 1150 at f12:24 read as 1150 or 1140.
- 133 vs 135: the alignment needs all 135 groups.
- f11r nouveau (27 groups) does not fit the text of no. 785 and probably belongs to another telegram. f11r ancien is a different codebook.
