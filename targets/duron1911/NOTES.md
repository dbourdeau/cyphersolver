# duron1911: Manuel Durón to W. Olliphant, México to El Paso, 20 May 1911, read in part with a shift on a 29-sign alphabet (CEHM-Carso CMXV.18.1777.1-6)

Status: read in part (Brice Dudout, 12 Nov 2026; 15 sure + 3 probable of 19 words, strict 78.9 %, 94.7 % with the probable words). The key is recovered from the ciphertext and **not validated**: the text has 107 signs, and the contributor's protocol declared before decoding that no reading of so short a text can be validated (`dudout/VALIDATION.md`).

A different key from every other entry of this traffic: the Clave G.A. card (`../mccarty1911/`), the turning grille (`../nuevaclave1911/`), the Hernández card (`../hernandez1911/`), the signer's card of `../mexico1911/`, and the shift of the sister telegram 1777.2-6 ("Elisa"). One key, one entry.

## The document

Centro de Estudios de Historia de México (CEHM), Fundación Carlos Slim, Archivo Federico González Garza (Fondo CMXV), CMXV.18.1777.1-6: a received telegram, Manuel Durón, México, to W. Olliphant (alias of Federico González Garza), El Paso, 20 May 1911, 9:10 pm, no. 428. Catalogue 1462 lists it as undeciphered. There is no gloss on the sheet, and it is not in the typed list of period decipherments CMXV.18.1795.1. The CEHM holds the original; its image was viewed on the public viewer for study and is not redistributed here.

It is not the same telegram as its neighbour CMXV.18.1777.2-6 (signed "Elisa", 4:21 pm the same day, 97 signs): the times, numbers and lengths differ. That one was deciphered at the time.

## The key

A simple shift on a Spanish alphabet of **29 signs, with ch, ll, ñ and w**: a b c ch d e f g h i j k l ll m n ñ o p q r s t u v w x y z; cipher = plain + 22 (mod 29). Details in `dudout/key.txt`.

- The first two signs (GM, plain "m s") are a header, like the two signs "PH" of the sister telegram.
- The telegraph has no ñ: the cipher sign ñ (plain u) is typed "n", so a cipher "n" reads t or u. Five cases (cuídese, muchísimo, retana, particípamelo, detalles; the contributor counts four), all settled by the sense.
- How it was found: a general substitution anneal with no shift assumed gave "...madero de licenciado... reyes retana y compañeros... correo detalles", and the table it found was a shift. A sweep of every shift on six alphabets (26, 27, 28, 28 without w, 27 with ch-ll, 29) then gave one reading only: 29 signs, +22 (score -10.1 against at best -13.2 for any other).
- Before this, a preregistered single measure tried every key of the fonds as is, including the Elisa shift (+-10 on 28 signs) and the cards CMXV.16.1557.1. None applies (best 0.259 against a best control of 0.365; `dudout/MESURE-C06.txt`).
- Observed after the reading, **not counted**: the shift equals header sign 1 minus header sign 2 in both telegrams of 20 May. Durón: G (7) - M (14) = -7 = +22 (mod 29). Elisa: P (17) - H (7) = +10 (mod 28).

## The reading

> Cuídese muchísimo Madero de licenciado {Daniel} Reyes Retana y compañeros. Salieron a ésa. Particípamelo {a} {la} [?dak]. Correo detalles.
>
> Let Madero be very much on his guard against Licenciado {Daniel} Reyes Retana and companions. They have left for your city. Let me know of it {at the} [?dak]. Details by mail.

- "danlel" has one wrong sign, so {Daniel} is only probable. The sister telegram names **Ismael** Reyes Retana: the first name is doubtful (an error of the encipherer or the telegraph, or another person).
- "VJLLL LYJXY": the space falls inside "ll ll"; joined, it reads "correo de-".
- "ladak": "a la" plus an unresolved "dak", perhaps a transmission error. No repair is forced.
- Count by words, header excluded (`dudout/reading.md`): 19 words, 15 sure, 3 probable, 0 restored, 1 unresolved. Strict 15/19 = 78.9 %; with the probable words 18/19 = 94.7 %. Under 95 % either way: read in part.

**Context.** 20 May 1911 is the eve of the Treaty of Ciudad Juárez (21 May). That afternoon, the Elisa telegram (deciphered at the time) reported Ismael Reyes Retana, of Blanco's staff, as the head of a plot to kill Madero. In the evening, this telegram from Mexico City, by another sender and in another key, warns Madero against a Licenciado Reyes Retana and his companions, who "have left for your city".

## Remaining gaps

- Validation of the key by a held-out test - blocker: too-short; 107 signs, and a held-out measure needs 300 letters. A second telegram in this key, or a period decipherment, would validate it; none is known among the 136 coded pieces of the fonds harvested.
- The first name "danlel" ({Daniel}) - blocker: needs-physical-access; one wrong sign, and the sister telegram has Ismael. The telegraph form or a period source would settle it.
- "dak" after "particípamelo a la" - blocker: too-short; three signs, perhaps a transmission error.
- A human palaeographer's check of the transcription against the CEHM image - blocker: needs-physical-access; the integration check compared all 24 typed groups with the public image (24 of 24 agree), but no human reader has.

## Escalation

- [x] siblings: the dossier CMXV.18.1777 opened (2-6 Elisa, a different telegram; 3-6 a notice of non-delivery; 4-6 and 5-6 Herrera Moreno); none is a decipherment of 1-6
- [x] clear-pages: no gloss on the sheet; the typed list of period decipherments CMXV.18.1795.1 (45 pp., OCR) searched: on 20 May only Elisa, Herrera Moreno x2 and Miranda/Herrera Moreno; no "Retana" outside Elisa
- [x] known-keys: every key of the fonds as is (Elisa +-10, the .tsv cards and the tables of CMXV.16.1557.1 incl. the Clave G.A.), one preregistered run: none applies
- [x] print: no edition of this telegram known; Narváez 2011 (Documenta & Instrumenta 9, full text, checked for catalogue 1462) has nothing on it; Narváez 2019 (SRE book, ch. VII-VIII) not available to the contributor, so it could not be checked
- [x] key-rebuild: free substitution anneal, then every shift on six alphabets: one key only (29 signs, +22); two methods on the same 107 signs, not two tests
- [x] retry: the doubtful groups (danlel, ladak, the spacing of VJLLL LYJXY, the four cipher n) retried against the key and the sense, and regraded

## Credits

Brice Dudout's project (AI agents, directed by Brice Dudout): transcription, the preregistered protocol and measure, key recovery, reading and translation. Catalogue 1462 and the pointer to the key cards CMXV.16.1557.1 and the typed list 1795.1: Daniel Bourdeau. The CEHM (Fundación Carlos Slim) holds the original.

## Files

| File | Content |
|---|---|
| `dudout/README.md` | status line and file list of the contributor's folder |
| `dudout/transcription.txt` | the cipher text as typed |
| `dudout/key.txt` | the key |
| `dudout/decryption.txt` | group by group: cipher signs and plain signs |
| `dudout/reading.md`, `dudout/translation.md` | the reading with S/P/R/I marks and the count; the English translation |
| `dudout/VALIDATION.md` | the declared impossibility of validation and the single archive-key measure |
| `dudout/PREREG-C06.md`, `dudout/MESURE-C06.txt` | the frozen protocol (French, verbatim) and the raw output of its one run |
| `profile.json` | the target profile |

## Contributor's note (dudout, 12 Nov 2026)

We send this as **read in part, not validated**, and we said so before decoding. The protocol (`dudout/PREREG-C06.md`, SHA-256 e2dcfc2a...) was frozen at 16:12 CET on 12 Nov 2026, with the transcription (100db048...) and the measure script (e99f7c57...), before any decoding of this telegram in the session. It states that 107 signs leave no room for a held-out portion of 300 letters, so the best possible status is "read in part" without validation. Two independent routes give the same key: a free anneal with no shift assumed, and a sweep of every shift on six alphabets. The header rule (shift = header 1 - header 2) was seen afterwards and is not counted. The first name is doubtful: Daniel here, Ismael in the Elisa telegram. Narváez 2019 (ch. VII-VIII) could not be checked. No CEHM image or crop is included.

## Integration check (12 Nov 2026, round 4)

Reproduced with my own decoder from the key rule (not the contributor's files): 107 signs; plain = cipher + 7 on the 29-sign alphabet gives, group for group, the text of `dudout/decryption.txt`. My own sweep of 166 (alphabet, shift) pairs over seven alphabet variants (26, 27, 27 with ch and ll, 28 with ll, 28 with ch, 29, 28 without w), scored with a 4-gram Don Quijote model, ranks the contributor's key first at -2.36 per character against -3.32 for the best other. Strict count recounted by hand: 15 of 19 words (78.9 %); five of the sure words (cuídese, muchísimo, retana, particípamelo, detalles) contain a cipher `n` that stands for t or u (the telegraph has no ñ), settled by the sense (the contributor writes four cases; `decryption.txt` marks five); he counts strictly and keeps his figure.

**Image.** www.cehm.org.mx answers with the project's CA bundle (CEHM record 12916 for CMXV.18.1777.1-6, 12917 for 2-6); the image host visor.cehm.org.mx still fails TLS verification, but the public image URL over plain http answers (`http://visor.cehm.org.mx/assets/docx/fondos/jzd/CMXV/18/1777/1-6/CMXV.18.1777.1-6.0001.jpg`, 1847 x 1272, found through the viewer page `Buscador/VisorArchivoDigital?jzd=...`). All 24 typed cipher groups of `dudout/transcription.txt` agree with it. The form types the addressee "Mr. William **Ollifhant**" (f for p; the sister telegram has "Olliphant"), carries "148-G. HM. 24 Via. Galveston." and the stamped number 428; no pencil gloss on this sheet. A telegraph slip in the addressee line shows that such slips occur, which fits the contributor's reading of `danlel` and `dak` as transmission errors but does not settle either.

**The sister telegram** (CMXV.18.1777.2-6, image fetched): a continuous string of 97 letters, signed Elisa, "Via Galveston", 4:21 pm, with a pencil decipherment of the time ("Dícème Ing. Rivera Balatayud urge sepan Ismael Reyes Retana, Estado Mayor Blanco, es jefe complot asesinar Madero"). My decoder gives a shift of **28** signs (a-z with ll and ñ, no ch), plain = cipher + 18 (cipher = plain + 10): `hx dicemeingoriveracalatayud urgespan ysmael reyes retana estado mayor blanco es jefe complot asesinar madero`. So its key is a different alphabet and shift from this telegram's (29 signs, +22), as the contributor says. The observation that the shift equals header sign 1 minus header sign 2 holds in both by my count (P 17 - H 7 = 10 on 28 signs; G 7 - M 14 = -7 = +22 on 29), but two cases, noticed after the reading, are an observation to test on other telegrams of the fonds, not evidence. CEHM record 12916 gives this telegram's subject as "Blanco, es jefe de un complot para asesinar a Francisco I. Madero"; records 12917 (2-6) and 12918 (3-6) carry the same subject line, so it is the legajo's subject, taken from the Elisa gloss, not a reading of this telegram.

**One key, one entry.** The other 1911 targets use other keys (`../mexico1911/`: the "Herrera. Moreno." card, 26 signs; `../hernandez1911/`: five letter swaps; `../mccarty1911/`: the Clave G.A. digraphic card; `../nuevaclave1911/`: a turning grille), so this is its own entry. No other target, lead or open pull request of this round holds CMXV.18.1777.1-6.

**Corrections made.** The credits line says AI agents. The SHA-256 of the frozen transcription quoted in `dudout/VALIDATION.md` and above (100db048...) is that of the batch file `T-sanantonio-duron-v1.txt`, which is not in the pull request; the `transcription.txt` here is a commented excerpt (90c1f7e9...), and `measure_c06.py` (e99f7c57...) is not included, so the archive-key measure is not reproduced; `PREREG-C06.md` matches its hash. The order of events (protocol frozen at 16:12 CET before decoding) is by the contributor's record. The name `Daniel` against `Ismael` is not resolved. Narváez 2019 was not checked.
