# Koninklijke Bibliotheek (KB, The Hague) sweep, 5 Nov 2026

The KB, the national library of the Netherlands, had never been swept. The Nationaal Archief and the Koninklijk
Huisarchief were swept separately (`research/nationaal_archief/`), so this pass covers the KB's own manuscript
collection only.

**Result:** the KB manuscript catalogue describes almost nothing as ciphertext. **One row** went into
`candidates.json`: a trivial 1797 album inscription. No row has a vetting block, because no scan is online. The useful
finds are **two bare keys** (key leads below) and several items that turned out to be read already.

## Method

- **Search: KB SRU** (`https://jsru.kb.nl/sru/sru`, `x-collection=GGC`, `recordSchema=dc`). Adding
  `and type=handschrift` to the query restricts it to the 86,068 manuscript records. The search matches note
  fields as well as titles: album records were found through words that occur only in their MARC 500 notes. CQL
  truncation works (`cijf*`). Script: `harvest_sru.py`. Output: `mss.jsonl`, 4,040 manuscript records with their
  terms; `hits.jsonl` is the resume file and is git-ignored.
- **Full records: KB OAI-PMH**
  (`https://services.kb.nl/mdo/oai?verb=GetRecord&identifier=GGC:AC:<PPN>&metadataPrefix=marc21`). This route
  returns the full MARC21 record: notes (500), contents (505), provenance (541/561) and literature (510). It is the
  only working route to the notes (see "What blocked"). Script: `marc.py`. Records are cached in `raw/`
  (git-ignored).
- **Terms and manuscript hit counts:**

| Term | Hits |
|---|---|
| `geheimschrift` | 47 (all of them the systematic class "6/4 Schrift. Geheimschrift. Calligrafie") |
| `cijf*` | 35 |
| `ontcijf*` | 42 (album records that say a signature "dient nader ontcijferd", i.e. is illegible) |
| `sleutel*` | 21 |
| `cyf*` | 1 |
| `gecodeerd*` | 1 |
| `nomencla*` | 4 |
| `code*` | 105 (codices) |
| `geheim*` | 78 |
| `secreet` / `secrete` | 8 / 9 |
| `alfabet` | 10 |
| `raadsel*` | 15 |

  These terms returned **0** manuscripts: chiffre, chiffres, chiffr\*, déchiffrement, dechiffr\*, cijferschrift,
  cipher\*, cypher\*, ziffer\*, cifr\*, crypt\*, kryptograf\*, steganograf\*, geheimtaal, codebrief\*,
  cijferbrie\*, "geheim schrift", "notis arcanis". To list the diplomatic papers, these were added: gezant\*,
  ambassad\*, resident\*, envoy\*, briefwisseling, correspondentie, missiven, lettres, letters, brieven,
  kopieboek, brievenboek, Alva, Granvelle, Oranje, Spanje, Aerssen, KA, CdG, "Pieter de Groot", Witt,
  Wicquefort.
- **Reviewed:**
  - Every record of class 6/4 (47), read in full MARC.
  - Every record that hit a cipher term.
  - The diplomatic and political letter collections dated 1480-1830 (`diplo.txt`, 272 shelfmarks), with full
    MARC for about 60 of them.
  - The KA series (former KNAW collection, `ka.txt`).
  - The Cornets de Groot family archive (CdG).
- **Prior art:**
  - DECODE: `research/catalogue_harvest/decode/list.json` has **no** record held by the KB.
  - known.py: no hits on Koninklijke Bibliotheek, KB Den Haag or the KB shelfmarks.
  - Web searches (cryptiana, HistoCrypt, DBNL).
  - The DBNL edition of the *Briefwisseling van Hugo Grotius*, vols. 1-17 (XML, grepped with `bhg_grep.py`).

## Rows (`candidates.json`)

| # | Shelfmark | Date | What | Scores (imp/solv/diff) | Scans |
|---|---|---|---|---|---|
| 1 | 79 J 35 fol. 90v | 1797 | Album inscription, Caroline Geesteranus for S.C. Rochussen, "klinkers door cijfers vervangen" | 1/2/1 | not online |

There is nothing to rank in a top five: this is the only item that the KB catalogue describes as enciphered text and
that is not already read or shorthand.

## Key leads (bare keys, no ciphertext in the item)

1. **KB KA 169**: "Sleutels van geheimschrift, gebruikt in brieven aan Alva e.a."
   - Record: PPN 310865956; 6 leaves, folio, Dutch; dated [early 17th c.]. Subject: Fernando Álvarez de Toledo, 3rd
     duke of Alba.
   - What it is: the keys used in letters to Alba and others, most likely a 17th-century copy of keys from 1567-73.
   - Not on DECODE. No description or edition found (web search on KA 169, cryptiana, the Alba/Margaret of Parma
     cipher literature).
   - Use: compare with the Alba-period keys of the Philip II reign (Tomokiyo, "Spanish ciphers during the reign of
     Philip II"; the 2025 Estudios Románicos study of Margaret of Parma's keys). It may read unread Alba-era letters
     in AGS Estado (Flandes) or the BL.
   - Needs a KB scan.
   - Already flagged by the US-blocked review pass (`sweep_2026-11_us_blocked/README.md`).
2. **KB 120 D 14**: "Sleutels voor het opstellen en ontcijferen van gecodeerde berichten".
   - Record: PPN 31084679X; 2 large sheets, about 400x530 mm, in French. Found loose in the KB in 1932.
   - It is a chiffrant and déchiffrant pair. The catalogue dates it by the names in the table: the marshals
     Villeroy, Villars, Tessé, Montrevel, Tallard and Berwick, plus Vaudémont, the duke of Mantua, Prince Louis of
     Baden, Prince Eugène and Marlborough.
   - Date: Berwick was made marshal in 1706, Louis of Baden died on 4 Jan 1707 and Charles III Ferdinand of Mantua
     in July 1708. So it is a French military key of **about 1706-07**. The catalogue says 1709 for Villars; he was
     made marshal in 1702.
   - Possible uses: French army or ministry letters of 1706-07, i.e. the Heinsius archive intercepts (NA 3.01.19),
     the Baden intercepts lead (Chamillart/Marsin/Tallard "chiffriert", Landesarchiv BW, in `research/leads.json`),
     and the French ministry keys used in `targets/geertruidenberg` and `targets/villars1710` (1710).
   - Needs a KB scan.
3. **KB GW A104556 [8]**: "Bericht over de geheime briefwisseling van Willem Bilderdijk".
   - Record: PPN 377311766; 19th century; on loan from the Letterkundig Museum since 2008.
   - It is a copy from the *Kronijk van het Historisch Genootschap* (1856) "with the key to the stamp Bilderdijk
     used on his letter paper, and an impression of the stamp".
   - This is a postal stamp or mark code, not a cipher table. Low priority.

## Read already, shorthand, or not cipher (not rows)

- **KA 53 and KA 54, journals of Constantijn Huygens jr (1649-50; 1688-96).**
  - Erotic passages are in a cipher that reads the even-positioned letters only.
  - Deciphered by J.F. Heijbroek, "Het geheimschrift van Huygens ontcijferd", in *Huygens herdacht* (KB, 1987),
    pp. 167-172. KA 53 cites that article; KA 54 is in the same hand and system.
  - Tomokiyo post: cryptiana.blogspot.com/2024/08/constantijn-huygens-jrs-secret-in.html. See also Dekker 2013
    and Joby 2014.
  - The 1876-77 and 1888 editions are expurgated, but the system is known.
- **128 B 3**: "Las Cartas que ... Don Juan de Austria y el secretario Joan Descobedo, **descifradas**, escribieron a
  Su Magd. y Antonio Perez", Saragossa, about 1591, 180 leaves.
  - These are plaintext decipherments, copied for the Antonio Pérez affair.
  - Useful only as cribs for the ciphered originals of 1576-78 (AGS).
- **78 C 4**: Petrus Scriverius' "Wonderbare vondt" (1618-19), a way to tell the imprisoned Oldenbarnevelt,
  Hogerbeets and De Groot what was happening.
  - The method is printed leaves of Secundus' *Itineraria* and *Opera* with swapped lines, underlined here.
  - This is steganography in clear text, not a cipher. Brandt printed it in 1710 (*Historie van de rechtspleging*,
    2nd ed., pp. 41-45).
- **76 H 6 fol. 20r**: Edmond Willis' inscription in the album of J. Montanus (London 1619), written in Willis'
  shorthand (*An abreviation of writing by character*, 1618). Shorthand, so excluded.
- **79 E 114**: Glijnis' name written "in cijfers" in a 1828 miscellany. Trivial, and the name is given in the record.
- **Hugo Grotius letters (CdG 14-28, and the Grotius letters elsewhere).**
  - The *Briefwisseling* edition resolves the cipher words of the Paris embassy letters in its footnotes ("staat in
    de tekst in cijfer: ...").
  - Only five isolated groups are left unresolved: nos. 3992, 4063, 4290, 4465 and 6048, values 321, 547, 161
    and two short runs.
  - Those originals are in UB Amsterdam (coll. RK) and NA coll. Hugo de Groot, not the KB. They are single name
    codes and not worth rows.
- **Album records with "ontcijferd"** (about 20): the word refers to illegible signatures ("Naam inscriptor dient
  nader ontcijferd te worden"), not to cipher.
- **The "geheimschrift" class hits**: calligraphy specimen books and writing-master sheets, for example 76 D 45
  (1446), 129 F 2-18, 132 E 2-7 and 135 L 2-7. The KB files secret writing and calligraphy under one systematic
  heading (6/4). None of these records mentions a cipher.

## Diplomatic papers that may hold cipher (catalogue silent; sample if scans are ever ordered)

None of these records mentions cipher, so none is a row. Where letters are copies the chance is low.

- **134 C 17**: Gideon van den Boetzelaer, Dutch ambassador in Paris, diplomatic correspondence, 1614. 163 leaves,
  originals and copies.
- **134 C 16**: letters of Dutch representatives abroad, 1664-71. 148 leaves; part records exist.
- **72 E 18**: Bolingbroke and Townshend at the Hague peace talks, 1710-11. 68 letters, autographs and copies;
  British despatches of these years often have cipher passages.
- **120 B 21-22**: correspondence of the marquis de Villarnoux, Prussian chamberlain, 1688-1727. 443 letters, from
  the Royer collection.
- **CdG 32-40**: letters to and from Pieter de Groot during his Swedish and French embassies, 1668-72.
  - Partly 19th-century copies.
  - The De Witt-De Groot letters are printed in *Brieven van Johan de Witt* with the cipher resolved, so check that
    edition first.
- **KA 132**: Justus de Huybert's letters from Paris, 1660-62. 487 leaves, copies and minutes.
- **71 H 18**: Helvetius' peace feelers, 1705-06. 176 leaves, copies.
- **135 D 29**: five letters to William Boswell, English resident at The Hague, 1633-34.

## What blocked

- **KB catalogue front ends.**
  - `opc-kb.oclc.org` resets the TLS connection.
  - `webggc.oclc.org` returns an empty body.
  - `kb.on.worldcat.org` (WorldCat Discovery) shows a Cloudflare "Verify you are human" page in the built-in
    browser. The page was not clicked through.
  - `www.kb.nl/zoeken` returns 403.
  - The SRU and OAI routes above make these front ends unnecessary.
- **No KB scans online for any item above.**
  - None of the MARC records has an 856 digitisation link, and none of the items is in Europeana.
  - The KB's online images are mainly medieval illuminated manuscripts and some alba amicorum (the EuropeanaTravel
    project); 79 J 35 is not among them.
  - So nothing could be viewed, and no vetting block could be completed. Every row and key lead needs a KB
    reproduction order.
- `data.bibliotheken.nl` SPARQL timed out (Gateway Timeout). Its linked-data record pages have less detail than
  OAI MARC.
- `mmdc.nl` (Medieval Manuscripts in Dutch Collections) is gone: it redirects to a KB page. Medieval KB manuscripts
  are in GGC anyway, and none is described as cipher apart from calligraphy-class items.

## Not reached

- Delpher full text, for printed KB catalogues and the annual *Verslag KB* acquisition notes ("in cijferschrift").
  The SRU book collections were not tried for this.
- The Literatuurmuseum archive catalogue beyond the GW records that are in GGC.
- An item-by-item look at the KB's diplomatic letter collections listed above; this needs scans.

## Files

- `harvest_sru.py`: SRU harvester for manuscripts.
- `marc.py`: OAI MARC21 fetcher and printer.
- `bhg_grep.py`: finds unresolved cipher notes in the Grotius edition XML (run against a scratch download).
- `mss.jsonl`: harvested records.
- `list.txt`, `diplo.txt`, `ka.txt`: triage lists.
- `raw/`, `hits.jsonl`: git-ignored caches.

## Merge (main session, 5 Nov 2026)

The single row (KB 79 J 35, album inscription, 1797) was merged as lead 2285. It has no vetting block (not online,
trivial), so it stays a lead. The key leads (KA 169 Alba keys, 120 D 14 French keys c. 1706-07) are best checked against the
Nationaal Archief Heinsius intercepts and the Baden intercepts already in `research/leads.json`.
