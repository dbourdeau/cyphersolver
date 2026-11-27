# PRIOR_ART: VOC cipher letters of 1623 and 1634 (Track B, 26 Nov 2026 AEST; searches 25 Nov UTC)

| # | where / query | result | quote (under 15 words) |
|---|---|---|---|
| 1 | Coolhaas, Generale Missiven I (Huygens online, retroboeken/generalemissiven), list of missives p. XVIII-XIX | Both letters are in the edition: III, 25 Dec 1623 (p. 129); VII, 20 Feb 1634 (p. 435) [sourced] | "III. De Carpentier, De Houtman, Dedel en Specx, 25 dec. 1623 129" |
| 2 | GM I p. 129 (html + page image saved, prior/gm1/0129.*) | Edition NOTES the cipher and a marginal decipherment made in the Netherlands; does not print the deciphered text [sourced] | "Scheepsbeweging deels in cijferschrift, de verklaring is in margine in patria bijgeschreven" |
| 3 | GM I p. 130 | Second cipher passage noted (ship cargoes), same remark [sourced] | "scheepsladingen, dit laatste weer deels in cijferschrift, met de verklaring in margine" |
| 4 | GM I p. 435-436 (20 Feb 1634, "Copie. 1023, f. 258-271") | Summarised and partly printed; no mention of cipher; the cipher passages (inv. 1108 fol. 184v-185) are not printed [sourced; checked pp. 435-437 only] | n/a |
| 5 | GM I full-text search (vol. 1): Hase, Spiritu, cijfers, cijferen, Leyden, Aquapulco, embocadero, notemuscaten | Spiritu: p. 327 only (Cabo Spiritu Santo, an earlier missive); no printed decipherment [sourced] | "omtrent Cabo Spiritu Santo ofte de craecken van Portugael" |
| 6 | Colenbrander, Coen Bescheiden VII pt 1 and 2 (archive.org djvu text): cijfer, Hase, Wapen en Leyden, 28.000 sacken | No print of either cipher passage [measured: text search; OCR, not read page by page] | n/a |
| 7 | Cyphersolver local clone (a536957, 14 Nov 2026) and hunts40 snapshot (catalogue, leads, DECODE Dutch and batches 1-8): 1.04.02, Batavia, Carpentier, Brouwer | Nothing for these letters; only VOC item in DECODE lists is Ramanacoil 1674 [measured] | n/a |
| 8 | web: "VOC cijferschrift 1623 Carpentier ..." | No hit on these ciphers | n/a |
| 9 | web: "Dutch East India Company cipher 1620s 1630s homophonic ... DECODE Lasry Tomokiyo" | HistoCrypt papers: Ramanacoil 1674 (Dinnissen and Kopal), Dutch Brazil 1646, cipher-key survey; none mentions VOC ciphers of the 1620s-30s [measured: text search of the 3 PDFs] | n/a |
| 10 | web: "cryptiana Tomokiyo Dutch VOC cipher seventeenth century Japan Hirado Batavia" | No Cryptiana page on VOC ciphers found | n/a |

## In the archive itself (not print)
- inv. 1079 scan 129 (copy of the 1623 letter): margin beside block A holds a clear-text version, matching our decode word for word [image viewed after the decode].
- inv. 1079 scan 133: margin beside block B holds the clear text of the cargo passage, matching word for word [image viewed after the decode].
- inv. 1108 scans 1154-1155: margin glosses a to o give the sense of the 1634 passages (the basis of our key).
So both letters were deciphered by contemporaries, and Coolhaas (1960) printed the fact for 1623.

## Verdict
- 1623: NOT FIRST to read it. A contemporary decipherment survives in the 1079 margins and is recorded in print (GM I p. 129-130).
  The printed edition does not give the deciphered words, so the reading (as text) has not been printed as far as checked. What is new
  here: the key is recovered from the 1634 glosses, the same system is shown to run 1623-1634, and the 1623 text is decoded
  independently with that key. Lasry category for 1623: read after matching with an external key (the 1634-derived key), checked
  against an existing (archival) decipherment.
- 1634: read from existing decipherment (the margin glosses); key rebuilt from them. Not printed in GM I as far as checked.
- Gaps: Daghregister Batavia 1631-34 and 1624-29 (Colenbrander) not searched for the plain content; Coen VII p. 1086 (ship movements
  cited by Coolhaas) not read page by page; DECODE live site not searched (snapshot only); Lasry's publications not searched beyond the web query.
- 1696 (inv. 1575): not worked this session (lower priority); prior-art gaps as in sweep/lead_1575/LEAD.md.

## DECODE live check (signed-in Mac Chrome, 26 Nov 2026 ~07:05 AEST) [measured]
Searches (DECODE RecordsList text search): VOC, 1.04.02, Oost-Indische, Compagnie, Batavia, Hooghly, Coromandel, Pondicherry, Surat, Jacatra, Heeren, "inv.nr 1292".
- HIT: DECODE record 1564, "NA_1.04.02_VOC_inv.nr.1292_anonymous_to_HeerenXVII_without date". Author and sender Rijcklof van Goens; receiver Heeren XVII; region Ceylon (Ramanacoil); homophonic substitution, graphic signs; 46 pages; Status: Decrypted; key_CT2 and decryption_CT2 files attached; created 2020-07-09; public. https://de-crypt.org/decrypt-web/RecordsView/1564
- No other VOC (1.04.02) cipher record seen: Batavia, Pondicherry and Heeren hits are non-VOC collections (KHA, Fagel, BuZa, BL Add MS 32263 Dupleix 1745). Hooghly, Coromandel, Surat, Jacatra, Oost-Indische: 0.
Effect on the pitch: VOC cipher letters are NOT new to DECODE as a class. A 1674 van Goens letter is already decrypted there. Our claim must be narrower: the 1620s-30s letters (inv. 1080, 1108, 1575) and the rebuilt key from that period, with DECODE 1564 cited. Next: compare key_CT2 of record 1564 with KEY_v2 (different period; a match would be a strong control or a NOT FIRST risk). Martin 1696 (inv. 1575 scan 38): no DECODE record found.
- DECODE 1564 key_CT2: the document viewer returned "Insufficient permissions to see the full image" (this Chrome is not signed in to DECODE: the header shows "Login") [measured]. The record lists its symbol set as "Graphic signs". Our 1620s-30s VOC key is numeric (KEY_v2, 60 number values), so the two are different cipher systems on the record's own description [derived]. A direct key comparison needs a DECODE login. Not a blocker for the period claim; cite 1564 as related prior art.
- RESOLVED without DECODE access (26 Nov 07:40 AEST) [sourced]: Dinnissen & Kopal, "Island Ramanacoil a Bridge too Far. A Dutch Ciphertext from 1674", Proc. HistoCrypt 2021 pp.48-57, open access PDF https://ecp.ep.liu.se/index.php/histocrypt/article/download/156/112 (saved prior_dl/ramanacoil_2021.pdf). The paper reproduces the 1674 key: "The key consists of 36 graphical signs" (Table 5, Fig. 1) with seven nomenclature elements. Van Goens made the key himself in 1674. So the 1674 system is a graphic-sign substitution, not our 1623-1640 numeric cipher [derived]. No key comparison is needed. Cite as related VOC prior art: VOC ciphers known as a class; our number cipher and its key are a different system.

# PRIOR_ART: Batavia letter of 9 Sep 1640 (NA 1.04.02 inv. 1134), cipher postscript (searched 25-26 Nov 2026)

| # | where / query | result | quote (under 15 words) |
|---|---|---|---|
| 1 | Coolhaas, Generale Missiven II (Huygens online), heading p. 101 [sourced] | Letter in the edition: Van Diemen and Council, 9 Sep 1640, KA 1043 fol. 235-253, copy 1043 fol. 255v-270 | "zending van deze brief met het Engelse schip Caesar" |
| 2 | GM II pp. 101-108 (opened only AFTER the score was fixed) | Printed in extracts; the extract ends at the closing prayer "... amen. Fol. 252v-253v." The cipher postscript that follows is NOT printed, and the edition does not mention cipher [sourced] | "tot de schaepscoye Christi gevoeght, amen." |
| 3 | GM I and II full-text grep of all 1,676 pages for cijfer/cyffer/ciffer/in margine/cursief | Cipher noted only for 25 Dec 1623 (GM I 129-130) and 7 Mar 1643 (GM II 197 n. 6); nothing for 9 Sep 1640 [measured] | n/a |
| 4 | In the archive: copy inv. 1134 scan 617 | Contemporary interlinear letter-by-letter decipherment over the number cipher (h e t d u b b e l d e s e r ...) and partial gloss over the letter-cipher words [seen after the score] | n/a |
| 5 | Cyphersolver local clone (a536957, 14 Nov 2026) and hunts40 snapshot of DECODE lists | No VOC item before Ramanacoil 1674 (trackB search, 25 Nov) [measured] | n/a |
| 6 | web: "VOC brief Batavia 9 september 1640 cijferschrift Malakka" | No hit on this cipher | n/a |
| 7 | web: "Dutch East India Company enciphered letter 1640 number cipher Heren XVII homophonic" | HistoCrypt papers on Ramanacoil 1674 and others; nothing on a 1640 VOC cipher | n/a |
| 8 | web: "Sybertsen" pastijbacker Nieuwendijk Amsterdam 1640 Caesar Batavia | No hit on the passage | n/a |

## Verdict
- The deciphered words have NOT been printed as far as checked (GM II stops at "amen"). A contemporary decipherment exists in the archive
  (interlinear gloss in inv. 1134 scan 617), so the content was known to the Company in 1640-41: NOT FIRST to know it, first in print as far as checked.
- Gaps: Daghregister Batavia 1640-41 not searched; live DECODE site not searched (snapshot only); HathiTrust/Google Books phrase search not done
  (for Malcolm's prior-art sheet: "Pastijbacker", "Cornelis Sybertsen", "schip Caesar 1640").

# PRIOR_ART: VOC number cipher 1623-1643, extension (searches 25 Nov 2026 UTC = 26 Nov AEST)

source | query | UTC | result | URL | quotation (page)
---|---|---|---|---|---
Cyphersolver GitHub issues + PRs (REST search) | VOC; Batavia; 1.04.02; East India Company; Oost-Indische, each is:issue and is:pull-request | 21:35:24-21:35:52 | 0 hits on VOC; Batavia hits are #363 (pointers) and PR #360 batavia1800 (NA 2.01.27, 1800), unrelated | gh_search.txt | n/a
Cyphersolver catalogue.json (sparse clone 77a77f49, 25 Nov 21:27 UTC) | regex 1.04.02 / Oost-Indische / Dutch East India / VOC over 2,170 entries | ~21:33 | 0 entries | github.com/dbourdeau/cyphersolver | n/a
Dinnissen and Kopal 2021, HistoCrypt (Ramanacoil) | read in full text | 21:21 | VOC letters of 1674 in a graphic-sign cipher (36 signs, 7 nomenclature elements); nothing on 1620s-1640s number ciphers | https://doi.org/10.3384/ecp183156 | "The key consists of 36 graphical signs" (p. 6 of PDF)
Dinnissen and Araujo, HistoCrypt (Dutch Brazil 1646); Dinnissen (Portuguese 1649) | text grep VOC, Batavia | 21:21 | Portuguese ciphers; no VOC cipher | ecp.ep.liu.se/.../download/392/350 and 693/599 | n/a
web search | "Island Ramanacoil" HistoCrypt VOC cipher van Goens | 21:20 | paper found (above) | ecp.ep.liu.se/index.php/histocrypt/article/view/156 | n/a
web search | VOC cijferschrift 1643 Tartarien goud zilver eilanden Vries brief Heren XVII cijfer | 21:21 | no hit on the cipher | n/a | n/a
web search | Dutch East India Company seventeenth century cipher key homophonic numbers letters Batavia Heren XVII decipherment study | 21:22 | only HistoCrypt papers above | n/a | n/a
web search | Tomokiyo cryptiana Dutch cipher VOC OR "East India Company" 1640s | 21:22 | no Cryptiana page on VOC ciphers | n/a | n/a
web search | Van Meersbergen "In goede en vertroude handen" VOC communicatie cijfer | 21:23 | article (De Zeventiende Eeuw 27, 2011, 80-101) on VOC communication 1672-78 cited by Dinnissen; not opened; period is later | n/a | INCOMPLETE: not read
Dagh-Register Batavia 1643-1644 (ed. Van der Chijs, 1902), archive.org daghregistergeh01indgoog OCR | Tartar, Castricum, Breskens, eylanden | 21:24 | PRINTS the purpose of the Vries voyage in clear: "tot ontdeckinge van Tartaria ende de eijlanden achter Japan gelegen" and "goudt ende silverrijcke eijlanden" | https://archive.org/details/daghregistergeh01indgoog | "tot ontdeckinge van Tartaria ende de eijlanden achter Japan gelegen" (OCR line 20503)
Dagh-Register 1640-1641 (archive.org daghregistergeh03kologoog OCR) | Caesar; pastij/Sybert/Egbertsen; vijftich tonnen | 21:25 | Caesar's departure noted; the 1640 cipher content (Sybertsen, 50 tonnen for Japan) not found | https://archive.org/details/daghregistergeh03kologoog | n/a
Coolhaas, Generale Missiven II (1964), pp. 194-195, read after the 1643 score | 23 Jan 1643 letter | 21:30 | prints only the Van Twist / Malacca passage and a China junk (copy fol. 388v-389r); cipher passages NOT printed | resources.huygens.knaw.nl/vocgeneralemissiven | "Brief verzonden met de Engelse Ulysses" (p. 194)
DECODE (from trackB check 26 Nov 07:05 AEST by Chrome) | VOC, 1.04.02 ... | earlier | only record 1564 (Ramanacoil 1674) | de-crypt.org/decrypt-web/RecordsView/1564 | n/a

## Full references
- Dinnissen, Jorgen, and Nils Kopal. 2021. "Island Ramanacoil a Bridge too Far. A Dutch Ciphertext from 1674." In Proceedings of the 4th International Conference on Historical Cryptology, HistoCrypt 2021, 48-57. Linkoping Electronic Conference Proceedings 183. Linkoping: Linkoping University Electronic Press. doi:10.3384/ecp183156.
- Coolhaas, W. Ph., ed. 1964. Generale Missiven van Gouverneurs-Generaal en Raden aan Heren XVII der Verenigde Oostindische Compagnie, Deel II: 1639-1655. Rijks Geschiedkundige Publicatien, Grote Serie 112. 's-Gravenhage: Martinus Nijhoff. pp. 101-108, 194-199. Online: resources.huygens.knaw.nl/retroboeken/generalemissiven.
- Chijs, J. A. van der, ed. 1902. Dagh-Register gehouden int Casteel Batavia ... Anno 1643-1644. Batavia / 's-Gravenhage: Landsdrukkerij / Nijhoff. archive.org daghregistergeh01indgoog. INCOMPLETE: page number for the Vries passage not taken from the OCR.
- Chijs, J. A. van der, ed. 1887. Dagh-Register ... Anno 1640-1641. Batavia / 's-Gravenhage. archive.org daghregistergeh03kologoog. INCOMPLETE: page not checked by hand.
- Meersbergen, Guido van. 2011. "'In goede en vertroude handen': Communicatie en beleid bij de VOC tijdens de Hollandse Oorlog (1672-1678)." De Zeventiende Eeuw 27 (1): 80-101. (not read)
- Archive: Nationaal Archief, 1.04.02 (VOC), inv. 1134 scans 570, 583, 605, 617; inv. 1141 scans 886, 890, 897-908. Images via GLOBALISE IIIF manifests (data.globalise.huygens.knaw.nl/manifests/inventories/<inv>.json).

## Verdicts
- 1643 letter (23 Jan 1643): CLEAR as far as checked for the deciphered WORDS (GM II prints none of the cipher passages); RISK on CONTENT:
  the Vries voyage's purpose (Tartary, gold and silver islands behind Japan) is printed in the Dagh-Register 1643-44 and is well known.
  NOT FIRST to know it: contemporary interlinear decipherment in copy 1 (inv. 1141 scans 886, 890).
- 1640 letter body (inv. 1134 scans 570/605): CLEAR as far as checked; contemporary gloss in copy B (605).
- The key(s): no printed or online VOC key for 1623-1643 found; KEY_v2 and KEY_B_v1 appear new as reconstructions [as far as checked].
- Gaps: HathiTrust / Google Books phrases (sheet below); Van Meersbergen 2009/2011 not read; DECODE logged-in key comparison for 1564; Lasry's publications beyond web search;
  NA inventory descriptions of 1.04.02 for "cijfer" not searched; Leupe (1858) and Hesselink on the Vries voyage not checked for cipher remarks.

# Filing summary (26 Nov 2026 AEST, for the pull request)
- VOC ciphers are known as a class. DECODE record 1564 (https://de-crypt.org/decrypt-web/RecordsView/1564; NA 1.04.02 inv. 1292, Rijcklof
  van Goens to the Heren XVII, 1674, status Decrypted) and Dinnissen, Jorgen, and Nils Kopal. 2021. "Island Ramanacoil a Bridge too Far.
  A Dutch Ciphertext from 1674." Proc. HistoCrypt 2021, 48-57, LECP 183, doi:10.3384/ecp183156, describe a 1674 VOC cipher. That is a
  graphic-sign substitution ("The key consists of 36 graphical signs", Table 5), a different system from the 1623-1643 number cipher here.
- Content risk: the purpose of the 1643 Vries voyage (Tartary, the gold and silver islands east of Japan) is printed in clear in the
  Dagh-Register 1643-44 (Van der Chijs 1902, archive.org daghregistergeh01indgoog): "tot ontdeckinge van Tartaria ende de eijlanden achter
  Japan gelegen". The deciphered words of the 23 Jan 1643 letter are not printed in Coolhaas, Generale Missiven II (pp. 194-195) as far as checked.
- Contemporary decipherments survive in the archive: interlinear glosses in the 1640 copy (inv. 1134 scan 617) and the 1643 copy 1
  (inv. 1141 scans 0886, 0890), margins in 1623 (inv. 1079) and glosses in 1634 (inv. 1108). Each was opened only after the score it checks.
- So we are NOT first to the content. The find is the key (KEY_v2, rebuilt from the 1634 glosses, run unchanged 1623-1643) and the two
  blind tests on unseen letters (1640 postscript, 1643 letter), with their controls and two independent blind second readings.

## Update 27 Nov 2026 (AEST): external blind package and Leupe 1858
The checks were done with AI tools and no person checked each record by hand. Sources: the non-Anthropic package report
(`blind_external_2026-11-26/VOC-independent-reading-and-prior-art.md`, with its search logs) and one check of our own (Leupe OCR, below).

| # | source | finding | quote (under 15 words) |
|---|---|---|---|
| U1 | Leupe, P. A., ed. 1858. *Reize van Maarten Gerritsz. Vries in 1643 ...* Amsterdam: Muller. Introduction (package: p. 6) and note (2). archive.org reizevanmaarten01siebgoog (OCR read 27 Nov 2026 00:2x UTC) | **CHANGES OUR 1643 VERDICT.** Leupe prints the cipher passage of the 23 Jan 1643 letter as it stands (letter-cipher words, XXI/IV, and the numbers of our runs 905.3, 905.9, 905.10) and, in note (2), the explanation of the cipher words: Tartarie(n), Goud en Zilver Eylanden, Oosten, Japan, noort. So the meaning of the page 905 cipher words has been in print since 1858 [sourced]. Our 1643 test did not use it (found after reading). His numbers agree with ours for 905.9 (11 9 16 10 2) and 905.10 (2 25 20 72 22); for 905.3 the OCR gives 24 89 17 30 16 6 50 20 against our frozen 24 39 17 30 16 5 50 20 (OCR or witness difference; to check on the page image; not applied) [measured on OCR] | "Verklaring der cijfers en letters in dezen brief voorkomende" |
| U2 | Coolhaas GM I p. 129-130 (already row 2 above) | Confirmed by the package: the 1623 letter is Coolhaas no. III, old inv. 991 ff. 124-126 (copy ff. 61-63) = modern **1079**, not 1080; Coolhaas does not print the explanations or a key [sourced, package] | "de verklaring is in margine in patria bijgeschreven" |
| U3 | De Jonge, J. K. J. 1870. *De opkomst van het Nederlandsch gezag in Oost-Indië* V, doc. V, pp. 22-24 | Prints a passage of the same 1623 letter about the English; not the cipher blocks or a key [sourced, package; not read by us] | n/a |
| U4 | Cheng, Shaogang. 1995. *De VOC en Formosa 1624-1662*. Leiden dissertation, vol. II, appendix p. 27 (cited by Andrade, "Pride and Prejudice", Itinerario, n. 8, for this letter) | **[unverified]** whether p. 27 prints the cipher lines or their reading. Open check; on Malcolm's prior-art sheet (page image needed) | n/a |
| U5 | Colenbrander/Coolhaas, *Jan Pietersz. Coen: Bescheiden* I and VII (public OCR) | no ciphertext, decipherment or key found; II-VI not checked [sourced, package] | n/a |
| U6 | Dagh-Register (first vol. starts 1 Jan 1624); de Leeuw 2000 *Cryptology and Statecraft in the Dutch Republic* ch. 2 | no 1623 witness; no identification of this key [sourced, package] | n/a |
| U7 | Dinnissen & Kopal 2021 (HistoCrypt), already above | Ramanacoil 1674: VOC 1292 ff. 544-563 (cipher and key), clear copies VOC 1298; no basis to equate with our system [sourced, package] | n/a |

Revised verdicts: 1623: not first (contemporary margin reading in inv. 1079, reported by Coolhaas); a printed reading is not known, Cheng II p. 27
open. 1643: **not first, in print since 1858** for the meaning of the page 905 cipher words (Leupe); the page 901/902/906 runs not checked in Leupe
beyond this passage. Key: Leupe gives word meanings, not a number table; KEY_v2 as a table is still not found in print [as far as checked].
