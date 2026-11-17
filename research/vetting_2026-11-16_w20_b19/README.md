# Vetting wave 20, batch b19 (16 Nov 2026)

Leads: 2697 (Dordrecht lodge), 1880-1883 (RGAVMF), 1858, 1860, 1862, 1863, 1865-1867, 1869-1871, 1876, 1877, 1879 (RGIA).
Proposals are in `proposals.json` (written by `make_props.py`). Script access only. Downloads are kept under `img/raw/` (git-ignored).

| id | verdict | confidence | deciding fact |
|---|---|---|---|
| 2697 | open | low | EAD: inv. 847 'Aantekeningen in geheimschrift', no scans, no decipherment named; inv. 803 (papers on the Masonic cipher) may be the key |
| 1882 | none (probably read) | medium | RGAVMF: 'копия шифрованной депеши' whose content is summarised; 2 leaves, no scans |
| 1881 | none | medium | RGAVMF record opens by curl now; letters and ciphered telegrams to Glazenap 1867, 39 pp., no scans |
| 1880 | none (probably read) | medium | RGAVMF: a journal 'с подробной записью шифрованных депеш', most probably a clear register |
| 1883 | read | medium | RGAVMF title: 'Шифрованные телеграммы расшифровки и письма': the decipherments are filed with the telegrams; dated 1904, not WWI |
| 1858, 1860, 1862, 1863, 1865, 1866, 1869, 1877, 1871 | none | medium | RGIA, no scans; the title does not show ciphertext rather than decoded copies |
| 1867, 1870, 1876, 1879 | none (probably read) | medium | RGIA titles call the pieces copies or give their content |

## Routes
- rgavmf.ru answers curl (16 Nov): all four RGAVMF records were read in full (fond, opis, section, dates, page count). Earlier notes said
  Chrome could not open 1880 and 1881; curl works.
- fgurgia.ru (RGIA KAISA): the object API used in batch C, `/ajax/obj/<id>/286525?children=false`, answered HTTP 500 for every id
  today, batch C's own id 3646513 included (the 286525 search index seems to have expired). The object page is a JS shell. The RGIA
  record texts already quoted in the leads (11 Nov) were not re-read.
- Dordrecht: the archieven.nl OAI EAD of toegang 383 has no `<dao>` at all, so nothing in the lodge archive is digitised.

## Prior art
- known.py on toegang 383 and Flamboyante, Ф. 315 and Gorchakov/Bludov, Glazenap, Butakov, Cromariot and Ф. 417, Pokotilov and Ф. 560,
  Timiryazev, Tashkent, Tolstoy, Grube, Davydov and Linevich, Goltsinger, Ф. 468, the economic conference: only the leads themselves and
  their sweep files (`known_out.txt`).
- cryptiana unsolved.htm and GL.htm (fetched 15 Nov) grepped for all names and for Russia/RGIA/RGAVMF/Masonic: no relevant entry.
- Web searches: Cromariot (nothing); La Flamboyante + geheimschrift (only an 1815 lodge song in the Vrijmetselarij Museum catalogue).

## Record errors
- 1883: the RGAVMF record dates the file 1904 (Военно-морской ученый отдел, раздел 1904, делопр. № 26577), not the First World War.
- 1867: the case runs 1903-1904 (from the record quoted in the lead), not 1903 alone.
