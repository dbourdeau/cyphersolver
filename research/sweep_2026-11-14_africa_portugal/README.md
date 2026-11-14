# Portuguese Africa sweep (14 Nov 2026)

Run by a Claude Code sweep agent (Sonnet 5.5) for the African-focused archive sweeps, 14 Nov 2026, 05:20-06:20 UTC. Area: Portuguese Africa through DigitArq
(Arquivo Histórico Ultramarino, Torre do Tombo), plus the BNP and the other Portuguese-language hosts. Nothing was solved.

**Result: 6 candidate rows (all catalogue-level, `needs_archive_scan: yes`, no `vetting` block), 3 key leads.** Africa in Portuguese holdings is
thin at catalogue level: the AHU's digital catalogue rarely says "cifra" in its descriptions, and the cipher series it does name are telegrams,
none of them digitised.

## Routes
| host | route | result |
|---|---|---|
| digitarq.arquivos.pt | `/api/docs/search?query=<q>&archiveCode=AHU|ANTT&fromIndex=&max=100` (omit archiveCode for all archives), `/api/docs/details/<id>`, `/api/rdigital/<id>`, `/rdigital/dissemination?fileId=` (see `research/torre_do_tombo/README.md`) | worked from plain urllib/curl, 2 s between requests, no 429/403. AHU is `archiveCode=AHU` (not swept before). The search is fuzzy (cifra also returns Ciera, Cafra, "se cifra em" = amounts) and indexes the title and description only; an AHU Conselho Ultramarino record carries its summary in the *title*, the description field is empty. Scripts: `harvest.py`, `details.py` |
| BNP Horizon (catalogo.bnportugal.gov.pt) | keyword search | answers, but a two-word query ("cifr* angola") returns 0 for every combination, and the BNP raw harvest of Nov 2026 is not in the checkout, so a re-filter on African words was not possible; `bnp_africa.py` records the attempt (`bnp_africa.log`). The BNP sweep's README already lists MSS. 146 n. 840 (Serpa Pinto, telegraph ciphers to Mozambique, 1890) |
| actd.iict.pt (Arquivo Científico Tropical, IICT) | `/list/?query=` | answers, ignores the query (always the 11 top communities); no cipher search possible. Scientific mission papers, low prior |
| ahu.dglab.gov.pt | front page | "Sítio em manutenção" |
| arquivonacional.cv (Cabo Verde) | front page | answers; no catalogue search found (not explored) |
| Angola archive, Arquivo Histórico Militar, arquivos.pt, CPLP archive | | no answer (connect failure) |
No bot checks were met. Claude in Chrome was not available; none was needed.

## Terms (archive, term, hits)
AHU hits are fuzzy: the "cifrado/cifrados/telegrama(s) cifrado(s)" family returns about 444 each (the 1947-1976 `Telegramas cifrados` series, post-1950 mostly), "decifração" 857, "chave" 984, "números" 2,533 (capped at 2,000; noise).

| archive | term | hits |
|---|---|---|
| AHU | cifra | 47 |
| AHU | cifras | 29 |
| AHU | cifrada | 2 |
| AHU | cifrado | 445 |
| AHU | cifrados | 444 |
| AHU | em cifra | 11 |
| AHU | decifrar | 0 |
| AHU | decifrada | 0 |
| AHU | decifrado | 0 |
| AHU | decifra | 0 |
| AHU | descifrado | 0 |
| AHU | sifra | 54 |
| AHU | zifra | 24 |
| AHU | cyfra | 25 |
| AHU | letra de cifra | 0 |
| AHU | por cifra | 45 |
| AHU | escrita secreta | 4 |
| AHU | letra secreta | 0 |
| AHU | contracifra | 3 |
| AHU | chave da cifra | 0 |
| AHU | chave de cifra | 0 |
| AHU | cifrar | 29 |
| AHU | caracteres | 21 |
| AHU | algarismos | 1 |
| AHU | cifra de | 44 |
| AHU | carta em cifra | 3 |
| AHU | ofício em cifra | 8 |
| AHU | carta cifrada | 0 |
| AHU | cartas em cifra | 2 |
| AHU | parte em cifra | 2 |
| AHU | números | 2533 |
| AHU | decifração | 857 |
| AHU | decifrada pelo | 0 |
| AHU | em cifras | 4 |
| AHU | alfabeto | 77 |
| AHU | sinais | 110 |
| AHU | hieróglifos | 0 |
| AHU | ininteligível | 1 |
| AHU | escrita enigmática | 0 |
| AHU | criptografia | 0 |
| AHU | código secreto | 13 |
| AHU | telegrama cifrado | 444 |
| AHU | telegramas cifrados | 444 |
| AHU | não decifrado | 0 |
| AHU | não decifrada | 0 |
| AHU | chave | 984 |
| AHU | papel em cifra | 1 |
| AHU | tinta simpática | 0 |
| AHU | linguagem cifrada | 0 |
| AHU | linguagem secreta | 0 |
| AHU | escrita árabe | 1 |
| AHU | caracteres árabes | 0 |
| AHU | caracteres arábicos | 0 |
| AHU | em árabe | 6 |
| AHU | cifra usada | 1 |
| AHU | numeração cifrada | 0 |
| AHU | nomenclatura | 16 |
| AHU | cifra secreta | 0 |
| ALL | cifra Angola | 49 |
| ALL | cifra Moçambique | 19 |
| ALL | cifra Cabo Verde | 4 |
| ALL | cifra Guiné | 7 |
| ALL | cifra São Tomé | 15 |
| ALL | cifra Mombaça | 0 |
| ALL | cifra Etiópia | 0 |
| ALL | cifra Abissínia | 0 |
| ALL | cifra Congo | 1 |
| ALL | carta em cifra Angola | 5 |
| ALL | em cifra Moçambique | 13 |
| ALL | decifrada Angola | 1 |
| ALL | cifra Zambézia | 0 |
| ALL | cifra Benguela | 0 |
| ALL | cifra Luanda | 13 |
| ALL | cifra Sofala | 1 |
| ALL | cifra Ilha de Moçambique | 0 |
| ALL | cifra Fortaleza de Jesus | 0 |
| ALL | cifra Melinde | 1 |
| ALL | cifra Zanzibar | 0 |
| ALL | cifra Macuas | 0 |
| ALL | cifra Monomotapa | 0 |
| ALL | cifra Quiloa | 0 |
| ALL | cifra Bissau | 3 |
| ALL | cifra Cacheu | 1 |
| AHU | código telegráfico | 0 |
| AHU | telegrama em código | 2 |
| AHU | convencional | 9 |
| AHU | linguagem convencional | 0 |
| AHU | sinais convencionais | 0 |
| AHU | estenografia | 447 |
| AHU | carta em árabe | 2 |
| AHU | suaíli | 0 |
| AHU | língua suaíli | 0 |
| AHU | ajami | 1 |
| AHU | carta em língua | 29 |
| AHU | escrita indígena | 4 |
| AHU | papel em branco | 29 |
| AHU | tinta invisível | 0 |
| AHU | letras de cifra | 0 |
| AHU | cifra da | 30 |
| AHU | cifra para | 18 |
| AHU | cifras para | 10 |
| AHU | cifras de | 28 |
| AHU | chaves | 960 |
| AHU | livro de cifra | 12 |
| AHU | caderno de cifra | 0 |

Not run: "segredo" (the run was stopped to avoid two streams on the host). The ANTT-only term list was not repeated; `research/torre_do_tombo/hits.jsonl`
(1,677 records) was re-filtered for African place words instead. Unique AHU records harvested: 2,894 (hits_AHU.jsonl); all-archive African-combination
records: 84 (hits_ALL.jsonl); 28 full records fetched (details.jsonl).

## Finds, ranked (candidates.json)
1. **AHU ID-OP/OP19560, Mozambique telegrams received and sent 1891-92, foreign affairs, "Contém cifrados"**: the year after the Ultimatum. No images.
2. **AHU ID-OP/OP16696, Lourenço Marques railway, Berne arbitration documents 1897, "documentação cifrada"**: Delagoa Bay arbitration. No images.
3. **Four Lourenço Marques railway/harbour folders, 1891, 1896, 1897, 1898, "telegramas cifrados"** (OP16752, 16773, 16774, 16775). No images.
4. **ANTT PT/TT/JLC/007/00007, cipher telegrams of the governo geral de Moçambique, undated** (José Luciano de Castro papers). Harvested by the Oct 2026 Torre do Tombo sweep but not rowed; the year in the row (1900) is a placeholder.
5. **AHU MU-GM "Telegramas cifrados" 1947-50 for Angola, Mozambique, Guinea, Cabo Verde, São Tomé** (about 17 folders; the series runs on to 1976). Machine-era; difficulty 5.
Also the Cape railway conference 1898 (OP17197, one cipher telegram).

Prior art for all rows: `known.py` (Lourenço Marques, Mozambique, Delagoa, Luciano de Castro: no hit for these items), `decode_search.py` (0 records for Lourenço Marques, Angola, Delagoa, Moçambique), Tomokiyo `unsolved.htm` snapshot (no mention), two web searches (Jesuit/Aquaviva; Berne arbitration cipher telegrams: nothing). Lasry/HistoCrypt and printed editions were not searched beyond those web queries. No row is viewed, so none can be vetted.

## Key leads (key_leads.json)
- **AHU CU Angola cx. 47 doc. 4298 (PT/AHU/CU/001/0047/04298), 8 Oct 1760: the Jesuit alphabet cipher "enviada de N.P. Claudio Aquaviva ... 1587"** copied by the governor of Angola António de Vasconcelos for Oeiras (Pombal). **Scans viewed (32 images, three clear copies of the table: m0007, m0015, m0027):** 26 letters over a row of symbols and a row of digits, duplicate signs "com numeros" for the vowels, nulls any sign with a dot, a second cipher "nao aparece". A table only, no ciphertext. It may read the Jesuit PBA. 614 lead (BNP sweep, 1759) and other Jesuit letters; the same file holds João de Paiva's letter of 1666.
- AHU SEMU/GM/004, two cifrantes of 1888 for the Minister's correspondence (catalogue only).
- AHU CU Índia 1644 consultas on a new cipher for the Viceroy (title only; India, not Africa).

## Excluded
- All `Telegramas cifrados` folders of 1951-1976 (after 1950) and the Secção de Expediente e Cifra files (MU-GM/SEC, 1947-60 personnel books).
- Fuzzy noise: Ciera/Cafra/Carceres name hits, "cifra" meaning an amount (Inhambane 1787 wine harvest), "sifra" = Brazilian sugar-harvest forms, Alfabeto dos Requerimentos (indexes), UIT "Nomenclatura" radio lists, Brazilian ofícios that mention a "cifra" only as figures or as a departmental cipher (Gomes Freire 1753-56, conde das Galveias 1811: Brazil, not Africa; not opened).
- Torre do Tombo hits on Angola/Moçambique that are 1974-86 Foreign Ministry cipher-section telegrams or Inquisition processes (fuzzy matches); PT/TT/AMC/012-1560/000039 "texto cifrado sobre acontecimentos em Bissau" has no date and sits in a post-1960 context, not opened.
- Angola 1760 ofício itself: its text is clear; only the enclosed key table is cipher material.

## What is left
- AHU catalogue is title/description only; ciphers described as "carta ... em cifra" inside long CU summaries would be found by the terms run, but the fuzzy index may drop long descriptions. A page-through of the Moçambique (CU/064) and Angola (CU/001) series by leaf was not attempted (tens of thousands of documents).
- The Jesuit Ethiopia mission, Fort Jesus/Mombasa and Kongo returned nothing in DigitArq ("cifra Etiópia/Abissínia/Mombaça/Congo": 0-1 hits); the Jesuítas na Ásia collection is at the Biblioteca da Ajuda (not reached).
- BNP: African-word re-filter needs the raw harvest of the BNP sweep (not in the checkout).
- Arquivo Nacional de Cabo Verde, Angola's and Mozambique's national archives, Arquivo Histórico Militar and ACTD: no usable search from this network.
- "segredo" and the Ethiopia-specific Jesuit series were not run.
