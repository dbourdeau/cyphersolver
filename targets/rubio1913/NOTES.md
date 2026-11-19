# Rubio Navarrete 1913-14: three telegrams to the Minister of War in "Clave núm. 109" (CEHM DLXXIII)

Status: read, by the floor for short texts (19 Nov 2026; recounted 18 Nov 2026 over cipher words, sure words only: 24 of 24, 12 of 13 and 28 of 30 per telegram). Before the recount: read (Brice Dudout, 29 Oct 2026; 67 of 67 cipher words read in their sense, 64 certain, 3 probable, 0 restored, 0 unresolved; Daniel Bourdeau's 95% rule). Catalogue 1468 read in part: the other "en clave" pieces use other tables (see below).

Contributed by Brice Dudout (Europe chiffrée), 29 Oct 2026. Write-up (to be published when the account is restored):
https://bdudout.github.io/europe-chiffree/en/documents.html#rubio-1913

## Documents

Centro de Estudios de Historia de México (CEHM-Carso, Fundación Carlos Slim), fondo DLXXIII (Manuscritos del General Guillermo Rubio Navarrete), DLXXIII.1.30.16-49, 2.41.9-41 and 2.41.13-41. The key: DLXXIII.1.28.14-23.
18 July 1913, 13 March 1914, 18 March 1914; signed drafts, the first incomplete. Lampazos (Nuevo León) → Mexico City; Zacatecas → Mexico City.
Sender: Guillermo Rubio Navarrete, general of the federal army. Recipient: the Minister (Secretary) of War and Navy, Mexico City.
Images: CEHM public viewer (no explicit licence; not copied here). Records: https://www.cehm.org.mx/Buscador/FichaBasica/137859?Tipo=A, https://www.cehm.org.mx/Buscador/FichaBasica/137995?Tipo=A, https://www.cehm.org.mx/Buscador/FichaBasica/137999?Tipo=A.

Mexico, 1913–1914. After the coup of February 1913, General Victoriano Huerta’s federal army fought Venustiano Carranza’s Constitutionalists. General Guillermo Rubio Navarrete commanded first in the Northeast (Lampazos, Nuevo León, summer 1913), against Pablo González’s troops, then at Zacatecas in the spring of 1914, as Villa marched on Torreón. His drafts of telegrams to the Minister of War are partly in cipher, in the “Clave núm. 109” that the Secretaría de Guerra y Marina had issued to him; the key sheet stayed among his papers. The cipher passages carry what he would not entrust to the telegraph clerks: the Laredo garrison courted by the Carrancistas, an old federal general in touch with the revolutionaries at San Antonio, Texas, and the lack of material and men to reopen the railway to Torreón.

## System and key

“Clave núm. 109. Secretaría de Guerra y Marina, con el General Guillermo Rubio Navarrete”: a printed table of 160 numbers. Letters (1–3 u, 13–15 o, 25–27 i, 37–39 e, 49–51 a, then 61 d to 93 z), syllables (pa, pe… ta, te, ti) and military words (98 Gobernador, 106 tropa, 107 fuerza, 112 vía, 132 General…). The numbers are set in the plain text, joined by dashes.
`key.tsv` is a transcription of the printed key sheet filed with the telegrams (DLXXIII.1.28.14-23); nothing added.

## Validation

Contemporary pair: typed telegram DLXXIII.2.41.18-41 (Zacatecas, 30 Mar 1914) and its pencil draft DLXXIII.1.29.9-30,
where Rubio wrote the plain text above the cipher numbers. Key frozen (SHA-256 9adb1190...) and protocol hashed before
the measurement; the first ten groups (checked by eye before the protocol) excluded. Held-out part (9 words):
1.000 characters / 1.000 words; 200 control keys (table values permuted, seed 1913) at most -0.021 / 0.111.
Thresholds 0.85 / 0.75: met. The rest of that telegram, with no contemporary plain text, reads
"para poder seguir mis trabajos al norte".

## Reading

First published decipherment, to our knowledge: nothing in the cyphersolver repository, in Cryptiana or in Roberto Narváez’s open-access articles; his book Criptografía diplomática, política y militar en México 1813-1926 (SRE, 2019) could not be consulted. Rule applied: Daniel Bourdeau’s, 95% of the words read from the sense. Cipher parts of the three telegrams: 67 words; certain 64 (95.5%), probable {x} 3 (4.5%), restored [x] 0, unresolved 0; read from the sense: 67/67 = 100%.

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`.

## Notes

- The key. The printed sheet of “Clave núm. 109”, in Rubio Navarrete’s name, is filed with his telegrams (DLXXIII.1.28.14-23). Every number of the three telegrams is on it; no value was added or corrected.
- Validation by a contemporary pair. The typed telegram of 30 March 1914 (DLXXIII.2.41.18-41) has its pencil draft (DLXXIII.1.29.9-30), on which Rubio wrote the plain text above the numbers: “… la ha dado guarnición de dicha plaza por conferencia tenida hoy. Espero fuerzas”. The key, frozen before the measurement, gives back this plain text 100% (see Method). The rest of the cipher in the same telegram, with no contemporary plain text, reads “para poder seguir mis trabajos al norte”.
- {material} (13 March 1914): the second 159 (te) is badly formed; the value is required by “ma-te-ri-a-l”.
- {plza} (18 March 1914): group 93 (z) is written over another figure; the cipher gives “p-l-z-a” without the second a, which we do not restore.
- {destruirla}: the middle figure of 153 (ru) is under the CEHM watermark; “de-s-t-ru-i-r-la” is required by the sense.
- Spelling. “teellez” (te-e-ll-e-z: Téllez), “sobemanera” (the r of sobre omitted), “envia” (en + vía, for envío): we keep the spelling of the cipher.
- The people. General Joaquín Téllez commanded the federal forces in the Northeast; the elderly “General Treviño” at San Antonio is probably Gerónimo Treviño (born 1836), former military chief of the Northeast under Porfirio Díaz (identification not checked in the sources).
- The rest of the fonds. The other “en clave” pieces of no. 1468 use other tables: an alphabetical numerical syllabary from 1 to 255 for the traffic with Téllez and the División del Bravo (a draft of 19 July 1913, DLXXIII.1.30.17-49, carries a pencil interlinear decipherment), a two-figure code (DLXXIII.1.30.5-49, 1.30.27-49), a presidential code (1.31.29-30, 2.41.17-41, 2.41.19-41) and a “Clave nº 99” (2.41.1-41). These tables are not in the file; those pieces are not read here.

## Read share over cipher words only, sure words only (18 Nov 2026)

Rule applied as written in PR #728 (owner's decision of 16 Nov 2026, README Conventions "The read share counts cipher words only"): the share is counted over the words written in cipher, sure words only; a word marked probable {x}, restored [x] or unresolved ‹x›, or carrying one such letter, is a hole; holes are counted by words.

Counted per telegram on `reading.md`, the plain text marked <…> left out: 18 July 1913 **24 of 24**; 13 March 1914
**12 of 13 (92.3%)**, {material} a hole; 18 March 1914 **28 of 30 (93.3%)**, {plza} and {destruirla} holes. In all 64
of 67 (95.5%), but the bar is judged per document: the two 1914 telegrams and the target go **read -> read in part** (superseded on 19 Nov 2026 by the floor for short texts, below).
One probable word decides each short telegram. No image re-read. `research/reading_audit/v10_relabel.py` (PR #728 branch) does not reproduce this count: it does not treat {x} or ‹x› as holes, and this reading declares no cipher or clear markup.

## Floor for short texts (19 Nov 2026)

README rule of 19 Nov 2026 (owner's decision): a document of fewer than 40 cipher words is read when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more; never for 40 words or more. Applied to the counts of 18 Nov above, nothing recounted, for the documents under 95%:

- cehm-dlxxiii-2-41-9-41: 13 cipher words, 1 hole -> **read** (floor used)
- cehm-dlxxiii-2-41-13-41: 30 cipher words, 2 holes -> **read** (floor used)

Every document is now read: the class is **read** (no change from before the recount of 18 Nov).
