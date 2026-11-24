# Puente Nacional parte, 6 June 1832 (catalogue 1466)

Outcome: read in part, key recovered from the ciphertext alone. 124 of 149 cipher words read (83.2%, recounted 16 Nov 2026; was about 86%, 127 of 147).

CEHM-Carso, Fondo I-2 (Manuscritos de Luis Gutiérrez Cañedo), I-2.5.340.1: one page, 22 cipher lines and a dateline,
"Puente Nacional, 6 junio 1832, a las siete de la noche", unsigned (CEHM: "En clave", "Parte manuscrito").
Image: https://visor.cehm.org.mx/assets/docx/fondos/jzd/I-2/5/340/1/I-2.5.340.1.0001.jpg (1290x2278; curl needs
`Referer: https://www.cehm.org.mx/`; the older `/jzd/...` path in the catalogue 404s). The image is git-ignored
(`img/`); the crops used are described in the profile.

## System
Spanish, consonants written plain, vowels replaced by marks: a = dash, e = i, i = x, o = dot, u = u (see `decode.py`).
Found from word shapes alone (comunicacion = c.munxc-cx.n, recibido = ricxbxd., Jalapa = J-l-p-, cinco o seis dias =
cxnc. . sixs dx-s). A written x and a real letter x look alike (proximo is pr.Xxm.). The dateline is in clear.
No key or decipherment is known; none was used.

## Files
`transcription.txt` (signs as read), `decode.py` + `decode_out.txt` (mechanical decode), `reading.txt` (sentences),
`translation.txt` (English), `fuzzy.py` (skeleton lookup against the Spanish corpora in `lang/`).

## Reading
A report to a general ("V.E."): the enclosed note will say that at daybreak next day the section he commands was to
leave; V.E.'s notes of the 2nd arrived this evening; no movement has been made or planned on the road, he hopes V.E.
will combine his force with those leaving Jalapa so as to act with decision; the enemy's sudden movement makes the
retreat difficult; supplies for only five or six days.

## Read share over cipher words only (16 Nov 2026)

Old figure 0.86 (127 of 147 words of `transcription.txt` without a [?]). Recounted by hand and with `v10_relabel.py` on
`reading.txt`: the 22 lines are all cipher; the dateline ("Puente Nacional, 6 de junio de 1832 ...") is in clear and is
now marked with angle brackets in the file (markup only, no word changed; entry declares `clear_markup` as ⟨⟩) so that it stays
out of both numerator and denominator. Holes by words, as `v10_relabel.py` counts them: 15 bare [?] (one word each; line 4 shows five), five part-words
(oc[?], c[?], pr[?], [?]s, and c[?]m[?], which has two holes) and four supplied letters (S[r], dificulta[d], d[a], r[ecurs]os) = 25 holes; "149 words" is v10's unit (read words plus hole count); **0.86 -> 0.832 (124 of 149)**.
The class stays read in part. Remaining gaps and Escalation unchanged.

## Remaining gaps
- line 4 (five words) and the end of line 3 ("que oc...") - blocker: illegible; cursive vowel marks run together, single scan
- words in lines 5, 8, 10, 14, 17, 19 and the Sr. named in line 10 - blocker: illegible; single scan
- lines 18-22 (several words) and the signature - blocker: illegible; single scan

## Escalation
- [x] siblings: CEHM 33468-33472 opened; I-2.5.339.1 and I-2.5.341.1 (Facio, 15 June 1832) are clear documents, no sibling cipher in the legajo's neighbours
- [x] clear-pages: none; the neighbours are clear letters
- [n/a] known-keys: no keys are known for Mexican 1832 military correspondence (Narvaez's cases are 1860 and later)
- [x] print: one web search (Plan of Veracruz 1832, Jalapa, Facio): no cipher literature; Narvaez 2008/2022 not accessible here
- [n/a] key-rebuild: the key is a five-vowel substitution already fixed; nothing to anneal
- [x] retry: every gap re-looked at in 2x crops; the unread words stayed ambiguous

## Next
A second scan or a higher-resolution image from CEHM; a Spanish palaeographer for lines 4, 10 and 18-22; the
correspondent: the Facio letter of 15 June 1832 in the same legajo suggests government officers on the Veracruz road.
