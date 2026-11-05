# BVPB sweep (3 Nov 2026)

Biblioteca Virtual del Patrimonio Bibliografico (bvpb.mcu.es), user's Chrome, own tab, UK-exit VPN. **Not blocked**: every
request answered 200, no 429, no check. Searches were same-origin `fetch` POSTs, one request every 2.2-2.5 s.
`/es/consulta/busqueda_general.do` does not exist (the search form is on the home page); fields `busq_general`, `general_ocr=on`.

## Method
1. Full-text (OCR) POST to `/es/consulta/resultados_ocr.do`, 15 terms: cifra, cifrado, cifrada, cifrados, cifradas,
   descifrado, descifrada, descifrar, escritura cifrada, cifrario, zifra, clave, en cifra, cifras, carta cifrada.
   Totals are dominated by printed books (e.g. cifrada 885: Libros 877, Mapas 1; Seccion "Libro impreso" 870,
   "Manuscrito antiguo hasta s. XIX" 4, Documentos 1). For each term the facet links Manuscritos, Manuscrito antiguo,
   Manuscrito moderno, Epistolario and Documentos were followed (first page of 50 only; none reached 50).
2. Catalogue (metadata) POST to `/es/consulta/resultados_busqueda.do`, 12 terms: cifrada, cifrado, escritura cifrada,
   descifrado, cifrario, zifra, carta cifrada, criptografia: 0 hits each; cifra 242 (first 50: books, 48 photos, maps);
   cifras 19; nomenclator 30 (printed gazetteers).

## Result: 0 rows
84 distinct records from the OCR facets, 25 typed Manuscritos. Every hit is "cifra" in the sense of number/sum/signature,
"clave" in the sense of key/keystone, or OCR garbage. Looked at the hit snippets of all 25 manuscripts: Huesca ceremonial 1786,
Tractus isagogicus, Genealogias de Casas Ilustres de Aragon T. II (S. XVI; narrative about a "cifra" correspondence
between named men, not a ciphertext), Fuero de Navarra 1595, 20th-century Basque studies, Idea sucinta del comercio del Peru
1794, Misioneros 1895 (printed), Expositio libri Geneseos 1594, legal and sermon volumes, a benedictine missal, Denis the
Carthusian, Ragionamento di Carlo V (18th c.), religious texts. None is a letter or document in cipher; no record carries
a cipher description. The BVPB holds heritage books and a few manuscripts, not diplomatic correspondence.

## Not reached
Only the first page (50) of each facet; OCR hits depend on the OCR quality of handwriting, so a ciphered manuscript whose
catalogue record does not say so would not appear; Genealogias de Casas Ilustres de Aragon was not opened beyond the
snippet; no known.py or web searches were run because there are no rows. BVPB adds nothing to Spanish cipher coverage;
Hispana and BNE remain the routes. Note: result pages are about 0.8 MB, so run one term per call (45 s limit in the tool).
