# Vetting wave 20, batch b04 (16 Nov 2026)

Claude Code session (Claude Opus 5.5), script access only (curl / Python / WebFetch / WebSearch), about one request a
second. Proposals only: `proposals.json` (keyed by lead id), built from `snip/p1.py`-`p4.py` (shared strings in
`snip/common.py`) and merged by `add.py`. Nothing in `research/leads.json` or `catalogue.json` was edited.
Helpers: `prior.py` (known.py plus Tomokiyo/Lasry greps for every lead, output in `prior_out.txt`), `bnp.py` (BNP
Horizon catalogue search and full record by curl), `manu.py` (Manuscriptorium castor search). Downloads in `img/raw/`
(git-ignored): Yale GEN MSS MISC finding aid (946.pdf), Urkunden und Actenstücke IX and XII OCR, BNP record texts.

Tomokiyo `unsolved.htm` and Lasry `GL.htm` (fetched 15 Nov 2026) were grepped for every name and shelfmark: no hit for
any lead (the GL "Ivernois" and "Jacobi" hits are "Nivernois" and "Jacobite").

## Results

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2513 | open | medium | UA XII p. 637 n. 1: Brandt's relation of 8/18 Oct 1666 "fast ganz in Chiffern geschrieben und nicht dechiffriert"; GStA unit still unidentified |
| 2514 | open | medium | UA IX p. 352: Hoverbeck's relation of 26 May 1662 "meist unaufgelöste Chiffern"; unresolved lines also at pp. 330, 351 |
| 2515 | open | medium | UA IX: relation of 20 May 1661 "meist in unaufgelösten Chiffern"; correction: Weiman's London diaries are missing and his journal ends 1659, so no clear crib |
| 1239 | open | medium | BNP 2083038, MSS. 14 n. 4: original signed letter, "Carta em liguagem cifrada", 1 f.; MSS. 14 n. 120 is a clear copy (drop it) |
| 1238 | open | medium | BNP: three autograph "Carta cifrada" letters; only doc. 46a (1731) has a topic sketch in another hand; docs 66 and 84 bare |
| 1237 | open | medium | narrowed to MSS. 99 n. 251 (Severino Gomes, Madrid 17 Apr 1828, "Em cifra"), partly ciphered siblings listed |
| 1242 | open | low | COD. 4417 pp. 33-37 (copy, 1740-42) "mensagem cifrada"; corrections: COD. 1750 is Cunha at The Hague 1728-36 (split), COD. 4419/6441 decipher Cunha Brochado 1712-13, not these |
| 1241 | open | low | PBA. 636 f. 320, 326 "parte final cifrada" in copies of Aires de Sá e Melo's 1766 Madrid dispatches made for Pombal, who had the key |
| 2781 | read | medium | the only ciphertext named (Jacobi-Kloest 1807-08, Ms. suppl. 976) is filed "avec déchiffrement de la main de d'Ivernois"; the rest are keys |
| 2780 | read | medium | Tronchin 148/56 holds keys, clear letters and a minute with numbers written over its clear words; no undeciphered ciphertext |
| 2270 | read | low | Saraiva's diary was printed (Imprensa Nacional 1915-17, BNP 416080) and its key is bound with it; no ciphertext described |
| 2274 | read | low | the BNP record summarises the invented-alphabet notebook's content in three parts: it has been read |
| 2271 | not_cipher | low | BNP record shows a clear 1873 letter with single capitals (Z, O) for a place and a person |
| 2113 | none | - | Yale finding aid confirms "mostly in cipher" (box 30), but Bible-commentator notes are likely shorthand; Yale viewers bot-checked |
| 2106 | none | - | ArchiveGrid Cloudflare 403, Yale 202/404 to scripts; "some appear in code" may be shorthand |
| 2782 | none | - | BGE behind Anubis proof-of-work; record calls the letter almost wholly ciphered yet summarises its content |
| 2275 | none | - | blocker stands: bundle-level "Parte do texto em cifra", no document named |
| 1847 | none | - | blocker stands: Calames series-level only; Des Noyers keys held in targets/desnoyers1659 noted |

## Access notes

- archives.bge-geneve.ch: Anubis proof-of-work page to curl (bot check, not passed).
- researchworks.oclc.org (ArchiveGrid): Cloudflare 403. collections.library.yale.edu: empty HTTP 202. Google Books API: 429.
- GStA PK ACTApro: not tried (needs a browser session, per research/vetting_2026-11-14_gsta_deep/README.md).
- BNP Horizon catalogue: plain curl works; the search page's record links are URL-encoded (`full%3D3100024%7E%21<bib>`).
- PARES not needed for this batch.
