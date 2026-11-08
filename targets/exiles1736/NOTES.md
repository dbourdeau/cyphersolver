# exiles1736: a letter of the Polish exiles on King Stanisław's abdication, 4 February 1736 (AGAD 1/338/0/1/1401)

Status: read (7 Nov 2026). Contributed by Prabal Gupta (issue #320; repository `prabal-rje/branicki-1757`, folder `agad-1401`, CC BY 4.0, commit f465095): a letter in Polish with long Latin stretches, in a cipher of one number per letter, with a dash between words and a few code groups for names, read from the ciphertext alone. Checked here against its own files only (`VERIFICATION.md`); the AGAD scans are not reachable from the project, so no transcription was compared with a scan here. The contributor settled the 23 differences of his two transcription passes on the scan.

## The document

AGAD Warsaw, Zbiór Anny z Potockich Ksawerowej Branickiej (zesp. 338), 1/338/0/1/1401, 7 scans (https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/28225114). Catalogue 1579 listed it with letters 1398 to 1400 ("List cyfrowany, częściowo po polsku, może do Branickiej"); those three use the reciprocal alphabet of `branicki1757`, this one a different cipher. An unsigned letter beginning "Monseigneur", the date line "D. 4. Feb:" with the year inferred as 1736 from the contents; the signature is a flourish. The card's guess that it is to Branicka looks wrong: the text addresses a man and asks what the Turkish power and the Khan plan.

`reading.md` (Polish and Latin, cipher in bold) and `translation.md` are the contributor's, `transcription.txt` the numbers and the clear parts line by line, `decryption.txt` the line-by-line decryption, `key.tsv` the letter key (30 signs), `contributor_notes.md` his own notes (how it was read, the limits of his checks, the code groups, the date and addressee, what was searched).

## What it says

France has agreed preliminary articles with Vienna and an armistice and says it cannot keep Stanisław Leszczyński on the Polish throne; the courier Orlik brings this as happy news and the exiles receive it in despair; they answer with two conditions: Europe must first recognise Stanisław as lawful king for life, and he must call a Diet, use the royal rights there and only then abdicate; a second courier left Versailles on 11 January and the reply says that Du Theil has gone to Vienna with the articles and Stanisław must abdicate at once; the confederated estates refuse and ask for some weeks; two lords leave for Warsaw with passports from Keyserling, the Russian envoy; the writer asks what the Turkish power and the Khan plan.

## The cipher

One number stands for one letter (30 signs: 0 ł, 1 e, 2 u, 3 a, 4 h, 5 m, 6 l, 7 c, 8 i, 9 b, 10 w, 11 ą, 12 x, 16 d, 18 g, 19 q, 20 k, 21 s, 22 ę, 33 æ, 37 f, 44 œ, 45 n, 53 j, 67 o, 79 y, 85 p, 100 r, 101 t, 120 z), with a dash between words; code groups written without dots stand for names (125 Stanisław, 455 Augustus III, 136 and 142 Warsaw, 675 [?Monti], 435 and 4345 the Khan, spelled in letters). It is not the key of letters 446 and 1398 to 1400.

## Remaining gaps

- Nine code groups unread (145, 156, 175, 195, 289, 505, 613, 715, 5455), "[?Monti]" for 675 a guess, and "cza[s]" written with 12 for 21 - blocker: open-codes; each occurs once or twice and no text fixes it (the contributor's table of what he tried is in `../branicki1757/numbers.md`)
- The signature (a flourish) and so the writer and the addressee - blocker: illegible; the scan shows no readable name, and the year digit "2" of 1736 looks like a 2 but is inferred from the contents
- A human check of the transcription against the AGAD scans - blocker: needs-physical-access; szukajwarchiwach.gov.pl is not reachable from the project and the images may not be redistributed

## Escalation

- [x] siblings: letters 446, 1398, 1399 and 1400 of the same fonds compared by the contributor (they share only stray phrases and use another cipher); the cards of 1397, 1402 and 1403 viewed
- [x] clear-pages: the clear Polish and Latin parts of the letter read and compared with the cipher around them; none is a decipherment
- [x] known-keys: no earlier key for this fonds or this correspondence is known to the contributor or the project
- [x] print: the contributor scanned Konopczyński (1909) for keywords and ran one web search on the names; no printed copy found; Polish editions of the 1733-36 correspondence not searched
- [x] key-rebuild: the key was found by the contributor's count-matching solver on Polish next-letter counts on this letter alone (98.2% of letter tokens), and settled by reading the numbers against the Polish; a solver on a Polish model agrees on 93.1% of tokens
- [x] retry: the doubtful groups were retried by the contributor against the scan; the project did not retry them
