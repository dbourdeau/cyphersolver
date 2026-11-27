# Two Pancho Villa telegrams, March and June 1914

**Status:** in progress. Both telegrams are read in part, and the gaps are still workable from online scans. Next step: transcribe the two-digit groups of the 1914 sibling telegrams in the same fonds, CEHM CMXV.35.3433.1-2 (Guadalajara to the Governor of Chihuahua, 27 Jul 1914) and CMXV.35.3492.2-3 (Ciudad Juárez to González Garza, 24 Aug 1914), from the CEHM visor images, and test the March and June keys on them, aiming to fix groups 33, 37, 69 and 99. Catalogue 1462 covers additional telegrams that remain open.

Ashton Allen reconstructed and applied the key with OpenAI Codex and Python. This filing uses the revised [contributor evidence](https://github.com/ashtonwallen/pancho-villa-telegram-decipherment/tree/0dc067a460fc66a9e36eb6c796ab7a4ba86d4779) and the [project review](https://github.com/dbourdeau/cyphersolver/issues/845). The CEHM manuscript images are linked.

## March 3, CEHM CMXV.31.3092.3-6

Villa tells Federico Gonzalez Garza what to say and record about Gustav Bauch. The text records Villa's instructions. It does not establish what happened to Bauch. The numeral replay covers 86 positions and supports 17 of 18 cipher-bearing words with contextual 69=CH, or 16 of 18 with that group open. The manuscript has DA in a place that provisionally reads d[e]. The March-fitted key gives a consistency check because the March text supplied some values.

[CEHM record](https://www.cehm.org.mx/Buscador/FichaCompleta/13105?tipo=A) | [Front](https://visor.cehm.org.mx/assets/docx/fondos/jzd/CMXV/31/3092/3-6/CMXV.31.3092.3-6.0001.jpg) | [Spanish](march-reading.md) | [English](march-translation.md)

## June 15, CEHM CMXV.34.3344.1

The reverse pencil reading supplies the starting values. The preferred 99=C agrees with pencilled DICHO and leaves CHAO incomplete. The alternative 99=CH gives CHAO and DICHHO. The key assigns 49 of 51 groups. Seven of ten cipher-bearing words are sure with 99=C and six of ten across both values. The pencil supplies the end of the word for campaign. The wholly supplied connecting words in brackets fall outside the count.

[CEHM record](https://www.cehm.org.mx/Buscador/FichaBasica/13195?Tipo=A) | [Front](https://visor.cehm.org.mx/assets/docx/fondos/jzd/CMXV/34/3344/1/CMXV.34.3344.1.0001.jpg) | [Reverse](https://visor.cehm.org.mx/assets/docx/fondos/jzd/CMXV/34/3344/1/CMXV.34.3344.1.0002.jpg) | [Spanish](june-reading.md) | [English](june-translation.md)

## Transcription doubts

- March first numeral of the date is overwritten. The reply supports March 3. Both occurrences of 16 in the first run are visible. The first DA remains literal in the replay.
- March 69=CH rests on the contextual Bauch identification and remains provisional.
- June 33 and 37 remain unresolved. The proposed surname and the competing values for 99 are shown in the contributor evidence.

## Replay

Join the group values in [key.tsv](key.tsv) in written order, preserving unassigned groups as brackets. A dash marks an unavailable assignment in that key state. The March and June assignments are shown in separate columns. The [contributor evidence](https://github.com/ashtonwallen/pancho-villa-telegram-decipherment/tree/0dc067a460fc66a9e36eb6c796ab7a4ba86d4779) files the alternative June result and the evidence behind each assignment.

## Remaining gaps

- March group 69 (CH) and the first DA - blocker: not-attempted; 69=CH rests on the contextual Bauch identification, and a sibling telegram in the same key could confirm it.
- June groups 33 and 37 (unassigned) and 99 (C or CH) - blocker: not-attempted; the sibling telegrams under Escalation are online and untried.

## Escalation

- [ ] siblings: CEHM CMXV.35.3433.1-2 (27 Jul 1914, 0001.jpg, about 130 two-digit groups with clear words between) and CMXV.35.3492.2-3 (24 Aug 1914, about 70 groups, ticked as if checked at the time) are online at visor.cehm.org.mx in a two-digit system like this one. Not transcribed (26 Nov 2026). A glance at the first line of 3433.1-2 with the June values gave no Spanish, so the key may differ by telegram; that was not a test. CMXV.35.3464.1 (2 Aug 1914, to Carbajal) is a plain-word code telegram, not this system.
- [ ] clear-pages: the pencil reading on the June reverse is used; the March reply cited under Transcription doubts not yet checked for more plaintext.
- [ ] known-keys: CMXV.16.1557.1 holds 21 manuscript keys (1911, including a División del Norte alphabet; catalogue 1462 status), not compared with key.tsv.
- [ ] print: not searched.
- [ ] key-rebuild: not done beyond the contributor's key.
- [ ] retry: waits on the steps above.
