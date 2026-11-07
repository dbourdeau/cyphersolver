# More letters, same key

AGAD zesp. 338, catalogue 1579. The archive card calls 1398 to 1400 "List cyfrowany, nierozwiązany" (cipher letter, unsolved).

The key from `../key.tsv`, found on the Branicki letter 446, reads these with no change. They read as French.

| Letter | Scans | Files |
| --- | --- | --- |
| 1/338/0/1/1398 | https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/28225111 | `1398/` |
| 1/338/0/1/1399 | https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/28225112 | `1399/` |
| 1/338/0/1/1400 | https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/28225113 | `1400/` |

`numbers.md` gives the number code, with the evidence for each value.

## What they say, in short

**1398, dated 24 July, probably 1757.** Matusewic writes on the Russian army under Apraxin at the frontier of Prussia. Town deputies come to submit, carts and men are taken without pay, and a rumour says flour and bread were poisoned. The letter puts the army at sixty thousand men.

**1399, probably June or July 1756.** An insider's report on the party of Hetman Radziwiłł in Lithuania. It plans for the Tribunal of 1757, so it comes before that Tribunal's dietines. After a congress at Iwie, the party agrees a fund of 146,000 francs to buy the coming dietines. Five lords take shares. The writer also sets up a new correspondence at Mitau.

**1400, from Nieśwież, 11 September 1756.** The year is in the number code: 824 811 823 818 810 reads "mil sept cent cinquante six". A bloody election assembly at Brest, with massacred gentlemen, brother against brother, and a rival party spreading two hundred thousand francs across Lithuania. Signed Boeven.

## Outside checks

**The sum in 1399.** The letter gives the total in words: "cent quarante et six mille francs". The shares come later: 53,000 + 25,000 + 50,000 + 10,000 + 8,000. They add up to exactly 146,000. The letter also says "[809] seigneurs", which the number block reads as five, and it lists five.

**The matcher.** My count-matching algorithm reads 1399 and 1400 from the ciphertext alone. Its key agrees with the 446 key on 99.4% and 98.9% of tokens.

**The people are in print.** Władysław Konopczyński, *Polska w dobie wojny siedmioletniej* (1909): https://archive.org/details/polskawdobiewoj7v8kono

I searched its OCR, and I did not read all of it. Pages marked "about" are near an OCR page mark.

| The letter says | The book says |
| --- | --- |
| 1399: "Mr le Palatin de Trok", with "Mr le Strasznik de Lithuanie son fils" | p. 126: Aleksander Pociej, palatine of Troki, with his son Ludwik, strażnik of Lithuania |
| 1399: a share from "Mr Pociei, strasznik de Lithuanie" | The same Ludwik Pociej |
| 1399: a share from "le Prince Grand Général" | About p. 125: Prince Michał Radziwiłł, grand hetman of Lithuania, lord of Nieśwież |
| 1399: a share from "le Prince grand enseigne" | About p. 125: his brother Hieronim Radziwiłł, chorąży of Lithuania |
| 1399: a share from "Mr Sottohub, général d'artillerie" | P. 219: Sołłohub, general of the Lithuanian artillery |
| 1399: "la Princesse Palatine Douairière de Nowogrod", at Zdzięcioł | About p. 153: the Radziwiłł palatine's widow of Nowogród lives at Zdzięcioł |
| 1399: "Mr Zabiello", marshal of Kowno | P. 137: Zabiełło, and the marshal of Kowno |
| 1400: "Mrs Oziemblowski et Suzin", deputies for Brest | P. 507, list for the Diet of 1758, Brest: Ludwik Suzin and Ignacy Oziębłowski |
| 1400: "Suzin, lieutenant de Mr Sosnowski" | P. 408: lieutenant Suzin acts for "his rotmistrz", Sosnowski |
| 1400: the "Prince Grand Général", and a sentence on Suzin | P. 405: the prince hetman refuses to free Sosnowski and Suzin from his courts |
| 1400: signed Boeven, at Nieśwież | P. 352: in 1756 the French minister Durand opens a correspondence with Radziwiłł's secretary, Boeyen |
| 1400: Boeven | P. 433: "Boevenowi 200", on the French embassy's payment list |
| 1400: Boeven | P. 475, a report of 28 November: the Lithuanian hetman has his secretary Boeyen arrested, for sending Apraxin's manifestos to the Prince of Moldavia |
| 1398: "monsieur Siruc", castellan of Witebsk, near Kowno | About p. 127: Siruć, castellan of Witebsk. About p. 466: Sz. Siruć writes from near Kowno |
| 446: "Mr le [?Stolnik] [de] Lithuanie", on a mission | "Stolnik lit." is the book's title for Stanisław Poniatowski, who was in St Petersburg |
| 446: "Mr Delachinal" | P. 352: La Chinal, secretary of Rzewuski. He may be the same man. |

## What I read from this

**Who wrote 1399 and 1400.** Boeven signs 1400. 1399 is unsigned, but its hand looks the same. Its writer reports on "mon maître", and asks to write directly to "le ministre de [?France]".

The book has the French minister writing to Radziwiłł's secretary in 1756. So I read Boeven as the hetman's secretary, reporting on his own master, for French money.

**Whom 446 attacks.** 720 fits Stolnik in the alphabetical table. Stanisław Poniatowski held that title, and he became King of Poland in 1764. So Branicki's manifesto of 1757 is probably aimed at his mission to Russia.

**What this does not show.** These identifications are my reading, and no historian has checked them. The Brest list is for 1758, and 1400 dates itself 1756, so both men would have stood twice. I found no copy of these letters in the book.

## Corrections, 7 November 2026

A check against the scans found errors in my first transcriptions. The files here now carry these fixes.

- 1399 and 1400: 820, 822 and 823 are 620, 622 and 623. The hand writes 6 with a tall stem, and I read it as 8.
- 1400: 840 is 640, "la République".
- 1399: 635 is 655, "Russie".
- 1398: 815 is 215, "Castellan".
- 1400: "Subin" is Suzin, and "Sobiemblowski" is Oziemblowski. This hand's g and q look alike.
- 1399: "Abramski" is Trabiwski, and "Tiesenhausen" is Tiezenaus, as written. Two unread names are Pociei and Sottohub.
- 1398: "Cirur" is Siruc, and "Witezehk" is Witebsk.
- 1399: I first dated it to 1757. It is probably 1756.

## Files

Each folder has `reading.md` (French), `translation.md` (English), the transcription and the line-by-line decryption.

- `1399/` and `1400/`: `transcription_all.txt` and `decryption_all.txt`.
- `1398/`: `transcription_p1.txt` and `transcription_p2.txt` come from one pass, with their decryptions.
- `1398/`: `transcription_consensus.txt` joins two passes. Where they differ, the key and a French character model settled the sign, not the scan.

## Status

Published 7 November 2026. 1399 and 1400 come from two transcription passes, reconciled on the scan. Page 2 of 1398 is still rough. `[?word]` marks a doubtful reading.

© 2026 Prabal Gupta. Released under CC BY 4.0: reuse it, and credit me.
