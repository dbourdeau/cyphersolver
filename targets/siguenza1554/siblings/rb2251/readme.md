# Siblings: Real Biblioteca II/2251, Pacheco's letters of 1554 to the bishop of Arras

Siblings of catalogue #855. Pedro Pacheco, viceroy of Naples, writes to Antoine Perrenot de Granvelle, bishop of
Arras. The letters are in Madrid, Real Biblioteca, II/2251 ("Cartas espaniolas a Antoine Perrenot de Granvelle"),
images through the library's IIIF server. Openings are about 2700 x 1975 px; opening *n* shows ff. (*n*-4)v and
(*n*-3)r. Transcribed 2 Nov 2026.

## Which letters carry cipher

II/2251 holds thirteen Pacheco letters (H15Corpus GRANVELA-H-0032 to 0044). All their openings were viewed. Four
have cipher, each with a decipherment of the time in the margin or between the lines:

| H15 id | folios | date | cipher | lines here |
|---|---|---|---|---|
| GRANVELA-H-0032 | 22r-24v | Naples, 5 Jan 1554 | f. 22r (1 line), 22v (4), 23r (3), 24r (6), 24v (1) | H32a-H32l |
| GRANVELA-H-0033 | 72v-73r | Naples, 17 Jan 1554 | f. 72v (4 lines), 73r (1) | H33a-H33e |
| GRANVELA-H-0036 | 110r | Naples, Feb 1554 | f. 110r (6 lines) | H36a-H36f |
| GRANVELA-H-0044 | 243r-244v | Naples, 30 Mar 1554 | f. 243r (5 lines), 243v (8), 244v (5) | H44a-H44m |

H-0044 is dated "xxx de março 1554" at its end (f. 244v); H15Corpus lists it under 1556. The other nine letters
(H-0034 to 0043 without 0036) show no cipher. The volume also holds a letter of the viceroy of Sicily (f. 182r,
March 1554) that is almost wholly in cipher, in a different correspondence; it was not worked.

The decipherments of the time were taken from the H15Corpus TEI (`<add place="margen|interlineado">`) and checked
against the images. The second column of the lines files gives them, with words lost in the gutter in brackets.
The H15Corpus marks each cipher passage only as "[mensaje cifrado]"; the cipher itself is transcribed here for
the first time.

## Files

- `h32_transcription.md`, `h33_transcription.md`, `h36_transcription.md`, `h44_transcription.md`: 37 lines, 626
  cipher signs (dots and clear words excluded), in the sign names of the BNE transcriptions (`../../transcription/`).
- `hNN_decode.txt`: `python3 ../../dec1554.py hNN_transcription.md`, with the key of `../../key_1554.md`.

## What the siblings show

**Same key.** Before these letters were read, the BNE key gave a value to 509 of the 590 signs then transcribed (86%). Its decode followed the
decipherments over long runs:
- `fu e su co s … y e s … si ra … e n tra`: *fue su costumbre y es y sera mientras*;
- `e s ta a que e l … tro … ni o`: *hasta que el [ma]trimonio*;
- `que/vo que/vo n ga se/si gu ta y`: *que venga seguro y*.

**Values confirmed by second and later occurrences:**
- `ụʒ` *Sena*: twice more (H32e, H44d), three times in all;
- `ιos` *su Magestad*: four more times (H32h, H32l, H44c, H44g), five in all;
- `de` *aqui*: twice more (H36c, H36g);
- `ɀ` *do*: *dos* twice (H32f, H32g);
- `ʒ` *yo*: *yo toda via* (H33a), the large Ʒ;
- `4` *y*, `o-o` *no*, `ȯ-o` *ni*, `n°` *gu*, `c .` *que*, `6` *l* (`tt 6` *el*), `tt oʒ` *en/em*, `aꝶ̶ ∇ t` *llos*,
  `8ſ` *ca*, `◻` *tra/tre*, plain `∇` *o*.

**The vowel-mark model predicts new signs that the decipherments confirm:**
- `ꝺ°` *tu* (*costumbre*), the *t* sign with the *u* mark;
- `-d` *mi* (*mientras*, *mil*), the *m* sign with the *i* bar;
- `dꝶ` *ma* (*matrimonio*, *mal*, *Roma*), the *m* sign with the *a* tail;
- `◻̇` *tri* (*matrimonio*), the *tr* sign with the *i* dot;
- `nꝶ` *ga* (*venga*, *holgaria*), as `n̄ꝶ`;
- `fꝶ` *pa* (*parte*), as `f°` *pu*;
- `ꞃꝶ`/`ɼꝶ` *da*, the *d* sign of `ɼ` with the tail.

**Plain `ꝗ` is not separable.** As transcribed, it stands for *que* in some places (*y que ninguno*, *y que no*,
*porque*, *que venga*) and for *r*, *vo* or *lo* in others. A side-by-side comparison on these images found that the
*v* syllables are mostly the barred `ꝗ̶`, which is a separate sign. But the plain two-storey `ꝗ` has the same shape as
*que* and as *r*, both in H32a. A small 9-like q (*lo*, H36f) had also been written `ꝗ`. The decoder prints
*que/vo*.

**New code groups:**

| group | value | where |
|---|---|---|
| `42` | duque | H32g *el duque es timido*, H44h *animo al duque* |
| `36` | (el) duque de Florencia | H32j, H32f |
| `ιoz` | su Santidad | H44h *como lo tomara su Santidad*, H44l *la voluntad de su Santidad*; differs from `ιos` *su Magestad* only by the final z |
| `iz` | cardenal | H33a *el cardenal Polo* |
| `ꝗz` | Ingalaterra | H33b |
| `5ı`, `ge` | españoles, alemanes | H32f, once each |
| `25` | (ca)vallos | H32f, `8ſ 25` *cavallos*; once (what was first read as `26` is `ꝸ 6` *al*) |

`T . ∇` is *creo* twice (H32h, H44j), and `T` is *cre* again in *secreto* (H36g), and `Ƶ̊ ∇ dꝶ` is *Roma* twice (H36d, H36f).

**After the additions** (`hNN_decode.txt`) the key gives a value to 608 of the 626 signs (97%); 118 of them keep two
values, most of them plain `ꝗ` (*que/vo*).

## Limits

- The lines were read on strips at 1.5-3x of the 2700 px openings. Sign names follow the BNE transcription; a
  few shapes were matched to the nearest BNE sign by eye.
- Some decipherments are partly lost in the gutter (H32a, H36). They were completed from the H15Corpus where it
  reads further, and are otherwise marked in brackets.

## Licence note: the decipherment column is not under CC BY 4.0

The cipher transcriptions, the decodes and the key values in these files are the contributor's work and fall under the
project licence (CC BY 4.0 for text and data, MIT for code). **The decipherment-of-the-time column in
`h32_transcription.md`, `h33_transcription.md`, `h36_transcription.md` and `h44_transcription.md` is a different matter.**
It largely follows the H15Corpus transcriptions of these letters, checked on the images. The H15Corpus states no
licence, so that column is **not covered by the project's CC BY 4.0 licence**, and the maintainer has not obtained
permission to reuse it. It is kept here for checking the key and is credited below; it is not offered for reuse. If the
corpus's directors object or ask for it to be removed, cut that column to the key words and leave the cipher and its
values (decided by the maintainer, 2 Nov 2026).

Source of the decipherment transcriptions: Lola Pons y Eva Bravo-García (dirs.): H15Corpus, disponible en línea:
<http://historia15.us.es/H15corpus/> [fecha de consulta: 02/11/2026], documents GRANVELA-H-0032, 0033, 0036, 0044. The
site states no licence; its citation form is used here.
