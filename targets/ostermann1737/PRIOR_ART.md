# PRIOR_ART: cat 1247 ostermann1737 (24 Nov 2026)

Verdict: **no key, decipherment, gloss or printed reading of this leaf found.** One flag for the main session (item 6).

1. Cyphersolver issues and PRs (`issues_index.tsv`, `issues_bodies.tsv`): grep for ostermann, kalushkin, astrakhan, остерман, калушкин = 0 lines in each file [measured]. Gate row 12: PASS.
2. Cyphersolver repo (`git -c gc.auto=0 grep -i kalushkin upstream/main -- research`): only the sweep and vetting records of this lead; no target folder, no key [measured].
3. DECODE public: gate recorded Ostermann 0, Kalushkin 0, Astrakhan 0 [sourced: GATE_20.md row 12]. Not re-run.
4. Commons file page (https://commons.wikimedia.org/wiki/File:Шифрованное_письмо_вице-канцлера_Остермана_резиденту_в_Персии_Калушкину,_1737.jpg): description "Рескрипт вице-канцлера ... Остермана русскому резиденту в Персии И. П. Калушкину, 17 апреля 1737 г." Source: archive.astrobl.ru virtual exhibition. No transcription or decipherment on the page [measured].
5. Source publication (Astrakhan archive exhibition page and PNG): NOT reached. curl: tunnel closed 5 times; WebFetch: robots unreachable; Wayback: tunnel closed. So whether the exhibition caption prints a reading is **not checked** [measured].
6. FLAG. SPbII RAN fond 178 op. 3 finding aid (https://spbiiran.ru/wp-content/uploads/2025/04/fond-178.-opis-3.-astrahanskaya-prikaznaya-palata.pdf), read through WebFetch's summary only: 1739 rescripts to Kalushkin are listed as "Шифр и дешифрант" and "Частично зашифрован, и дешифрант" (units 178-3-6, -7, -10). These are other documents, two years later, unpublished, and the finding aid has no 1737 entry and no key ("ключ", "цифирная азбука": none). Whether the 1739 cipher is the same alphabet is unknown. Not a reading of this leaf; recorded because contemporary decipherments of sibling rescripts exist in an archive [sourced, unverified at the page level].
7. Web searches (Russian and English), all without a hit on this rescript, its text or a key:
   - рескрипт Остермана резиденту Калушкину 1737 шифр цифирь расшифровка
   - Соболева "Тайнопись в истории России" Остерман шифры 1730-х ... Персия резидент
   - "Калушкин" резидент Персия 1737 рескрипт "цифирью" / "шифрованный" ... АВПРИ
   - Астраханский архив виртуальная выставка "быть особо" ... рескрипт Остермана Калушкину
   - Ostermann Kalushkin 1737 cipher rescript ... Soboleva
   - after the decode, two plaintext phrases: "Калушкину" 1737 "Абдул Баки" ...; "бденно смотреть и прилежно разведывать" / "что между шаха и турок происходит": no hit.
8. Soboleva, Тайнопись в истории России / История шифровального дела в России: not opened in full text (not online to this sandbox). General histories; search snippets show nothing on Kalushkin or Persia. **Not checked at page level.**
9. Cryptiana/Tomokiyo, Lasry, Turner (NoAutopilot/cipher-lab), Dudout: nothing surfaced in the searches above; the Nov 2026 vetting block in catalogue.json records the same. Not re-fetched site by site.
10. Not searchable here: AVPRI f. 77 "Сношения России с Персией" (the Collegium's clear draft of this rescript should be there), HathiTrust and Google Books full text. For Malcolm's prior-art sheet: "бденно смотрѣть и прилѣжно развѣдывать", "Абдулъ Бакы ханъ", "Калушкину" 1737.


## Later prior art (27 Nov 2026): an earlier independent solution exists

[sourced] Mark Vladimir Prizmic (Anaheim, CA) published "An independent solution of Vice-Chancellor A. I. Ostermann's cipher rescript to I. P. Kalushkin, Russian resident in Persia, 17 April 1737" as a Zenodo working paper on **14 Nov 2026** (v1, CC BY 4.0, https://doi.org/10.5281/zenodo.24234135). Its record says it works from the public web image, identifies a monoalphabetic substitution with a few homophones and a line-end continuation mark, gives the key and reads all 144 cipher words; it discloses AI assistance (Claude) and says the archive's file includes a decipherment the author has not seen.

[derived] That is ten days before this project's reading (key frozen 24 Nov 2026 10:55Z; Sectigo and FreeTSA stamps 24 Nov 11:01:35Z). **This entry is therefore not the first solution.** Our 24 Nov prior-art search covered Cyphersolver, DECODE, the Commons page and web searches but not Zenodo; that was a gap, and the paper was found on 27 Nov by a search for later work. It was not seen or used before or during our reading, so the two solutions are independent of each other.

[unverified] The two keys and readings have not yet been compared sign by sign (the paper's PDF could not be read from the sandbox). Agreement would corroborate both; any difference should be listed here. Credit for the first solution goes to Prizmic; this entry stays as an independent second reading with its frozen files, controls and stamps.

The checks were done with AI tools and no person checked each record by hand.

## Key comparison with Prizmic (27 Nov 2026)

[derived] Prizmic's paper (Zenodo 10.5281/zenodo.24234135, v1, 14 Nov 2026) was read on 27 Nov and compared with our frozen KEY.tsv, TRANSCRIPTION.tsv and DECODE.txt (hashes unchanged). His sign labels differ from ours, so the mapping was made by aligning his raw sign-by-sign decode with our 787 transcribed tokens (same sign count on 14 of 20 lines, within one on the rest) [measured].

- [derived] Same system (monoalphabetic substitution, invented signs and digits, word division kept, final ъ). 29 of our 31 letter signs have the same value in both keys. Differences: S28 (2 tokens) ours ѿ "от", his у ("у себя", "управить"); S22 ours ю, his key и/й (his text prints ю in 3 of its 5 places).
- [derived] He merges look-alike pairs we keep apart (S01/S02, S08/S09, S30/S31, S27/S28), has two м signs where we have one, and treats our S26 as the conjunction и inside a line and as a hyphen-like continuation mark at line ends; he reads our S33 as и in 3 of 5 places. We read S26 and S33 as non-letter marks.
- [derived] About 20 of 787 sign tokens (2.5%) are read differently, in 16 places; most come from S26/S33. Examples: L01 "иного" (ours) against "и того"; L15 "разведыъа" (ours) against "разведывать" (his is the better sense there). None changes the content of the rescript.
- [unverified] Neither reading has been checked by a Russian reader or against the archive's decipherment (GAAO f. 394, op. 1 dop., d. 11). Credit for the first solution stays with Prizmic; the comparison corroborates both solutions.

The checks were done with AI tools and no person checked each record by hand.
