"""Rows of the 11 Nov 2026 Nordic sweep. python3 build_candidates.py -> candidates.json, key_leads.json"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
D = "2026-11-11"; BY = "claude cloud sweep 11 Nov nordic"
rows = []
rows.append({
 "year": 1657, "date": "17 Jan to about May 1657",
 "title": "Christoffer Sehested (Danish envoy in Vienna) → Frederik III and chancellor Christen Thomesen Sehested: wholly enciphered relations",
 "correspondents": "Christoffer Sehested → Frederik III of Denmark; Christoffer Sehested → Christen Thomesen Sehested",
 "place": "Vienna", "language": "German", "region": "Scandinavia", "period": "1651-1700",
 "shelfmark": "Rigsarkivet (Copenhagen), Tyske Kancelli, Udenrigske Afdeling (TKUA), Speciel del, Kejseren: Gesandtskabsrelationer med bilag, pakke 1630-58, læg \"Relationer fra Christoffer Sehested 1657\" (cited by Fridericia as Østrig 46)",
 "folio_note": "Arkivalieronline unit 260651 (434 images, microfilm scans), images 108 to about 170: some 40 pages of cipher (letters dated 17/1, 10/2?, 14/2, 7-17/2, March 1657 ...). Seen at full size: image 126 (14 Feb 1657, 'Sire', 24 lines).",
 "cls": "A",
 "status": "Viewed 11 Nov 2026. The letters are written entirely in a number cipher: one- and two-digit numbers divided by colons, a t-shaped word divider, and nomenclator signs (Σ, Ψ, GG, XX, X, H, ♀, Ω, 7000, mm). No decipherment is written on the cipher leaves. Loose slips in a 19th-century hand (images 124, 125, 137, 138) carry a German decipherment of the letter to Chr. Thomesen Sehested of 7/17 Feb 1657 and its postscript, with the nomenclator signs left unresolved; older-hand plaintext leaves stand at images 112-115 and 157-158. Fridericia, Adelsvældens sidste Dage (1894), note 62 to p. 242, cites the letters and thanks Dr E. Gigas for 'a decipherment of Sehested's letters': so the letters were deciphered in the 1880s, but no text of the decipherment is printed and the slips in the volume cover only part. Not on DECODE (search 'Sehested': 0).",
 "why": "Denmark's secret alliance talks with the Emperor on the eve of the 1657 war with Sweden; the plaintext has never been printed, and the code signs for persons are unresolved even on the archivist's slips.",
 "importance": 4, "solvability": 5, "difficulty": 2,
 "score_note": "Scored from the scans during the 11 Nov 2026 Nordic sweep (research/sweep_2026-11-11_nordic/); image 126 read at full size, images 101-170 on thumbnails",
 "verify": "Not vetted as open: Gigas's decipherment (used by Fridericia 1894, and Gigas, Grev Bernardino de Rebolledo, 1883, pp. 283 f.) is prior art of unknown extent. Match each decipherment slip to its letter, list the letters with no plaintext in the volume, and ask Rigsarkivet whether Gigas's full decipherment survives. The archive also holds 'Christoffer Sehested keys 1650-70' (Daisy heid 1449582, see research/scandinavia).",
 "links": [{"label": "Arkivalieronline viewer (unit 1630-58, image 126)", "href": "https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=19852211#260651,48703417"},
           {"label": "Daisy series record", "href": "https://daisy.rigsarkivet.dk/arkivserie_detaljer?heid=11623887"},
           {"label": "Fridericia 1894 (full text)", "href": "https://archive.org/details/adelsvaeldenssid00frid"}],
 "seen": "image", "source": "Rigsarkivet Arkivalieronline sweep (TKUA envoy reports)",
 "prior_art": "partly read: E. Gigas deciphered Sehested's letters for Fridericia (Adelsvældens sidste Dage, 1894, note 62; archive.org full text opened 11 Nov 2026); slips with part of it lie in the volume. No printed plaintext found; DECODE search 'Sehested', 'Wien 1657': no record of it; not in Tomokiyo's unsolved.htm",
 "needs_archive_scan": "no", "access_note": "free on Arkivalieronline, no login; images also at api.rigsarkivet.dk/ao/v1/images/<id> (ao.py)"})
rows.append({
 "year": 1863, "date": "1863-1864 and 1869-1873",
 "title": "Johan Peter Carlsson: diary notes written mainly in cipher, two volumes",
 "correspondents": "Johan Peter Carlsson (1844-1915), diarist", "place": "unknown (Sweden; held in Linköping)", "language": "Swedish",
 "region": "Scandinavia", "period": "1801-1900",
 "shelfmark": "Linköpings stadsbibliotek (Stiftsbiblioteket), B 168",
 "folio_note": "Vol. 1: 551 pages, 16 x 11 cm; vol. 2: 1,135 pages, 17.4 x 13 cm; 'mainly written in cipher'",
 "cls": "C",
 "status": "Alvin record 371545 (read through Alvin's OAI-PMH feed, 11 Nov 2026): 'Dagboksanteckningar 1863-1864 och 1869-73, huvudsakligen skrivna med chiffer', subject headings Dagböcker and Chiffer. The record lists no digital copy and names no decipherment. Not on DECODE.",
 "why": "About 1,700 pages of a private diary of a young Swede of the 1860s in an unread cipher: a long text, so a personal substitution system should give way quickly once scanned.",
 "importance": 2, "solvability": 1, "difficulty": 2,
 "score_note": "Scored from the catalogue description during the 11 Nov 2026 Nordic sweep (research/sweep_2026-11-11_nordic/); not viewed",
 "verify": "Ask Linköpings stadsbibliotek (Stiftsbiblioteket) for sample pages of B 168 and whether a key or transcription is filed with it; identify the diarist.",
 "links": [{"label": "Alvin record 371545", "href": "http://urn.kb.se/resolve?urn=urn:nbn:se:alvin:portal:record-371545"},
           {"label": "Alvin OAI record", "href": "https://www.alvin-portal.org/oai/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:ALVIN.org:371545"}],
 "seen": "catalogue", "source": "Alvin OAI-PMH sweep",
 "prior_art": "open (checked 11 Nov 2026: DECODE search, Tomokiyo unsolved.htm, three web searches; nothing on this diary)",
 "needs_archive_scan": "yes", "access_note": "not digitised; reading room or scan order at Linköpings stadsbibliotek",
 "vetting": {"date": D, "by": BY,
  "seen": {"kind": "not online", "where": "Alvin record 371545 via https://www.alvin-portal.org/oai/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:ALVIN.org:371545 (the HTML record page is behind Anubis)",
           "extent": "two volumes, 551 and 1,135 pages, diary entries 1863-1864 and 1869-1873",
           "cipher": "Alvin description: \"Dagboksanteckningar 1863-1864 och 1869-73, huvudsakligen skrivna med chiffer.\" (diary notes, mainly written in cipher); subject heading \"Chiffer\". No decipherment, key or transcription is mentioned in the record."},
  "prior_art": {"decode": "de-crypt.org RecordsList searched for 'Carlsson', 'dagbok' and 'Linköping' on 11 Nov 2026: no records for any of the three",
                "tomokiyo": "repo copy of Tomokiyo's unsolved.htm grepped for Carlsson and Linköping: no mention; Cryptiana has no article on Swedish private diaries that the web searches surfaced",
                "lasry": "no Lasry paper concerns a 19th-century Swedish diary; the web searches for the diarist and shelfmark returned none of his work",
                "edition": "no edition known: web searches for the diarist with 'dagbok chiffer' and for 'B 168' Linköping found no printed diary or transcription",
                "literature": "HistoCrypt proceedings appeared in one search result list but with nothing on this diary; no article on a Linköping cipher diary found"},
  "key_check": "no key is recorded with the volumes in Alvin and none is held here; nothing could be tried without images",
  "duplicates": "known.py 'Johan Peter Carlsson' and 'B 168': no hit for this item (B 168 hits are other shelfmarks); not in catalogue.json or leads.json",
  "verdict": "open",
  "searches": [
   {"query": "\"Johan Peter Carlsson\" 1844-1915 dagbok chiffer Linköpings stadsbibliotek", "result": "no page on the diarist or the diary; only unrelated Carlssons and Linköping council minutes"},
   {"query": "Linköpings stadsbibliotek handskrift \"B 168\" Carlsson dagboksanteckningar chiffer 1863 ... chifferskrift tolkad", "result": "nothing on B 168 or a deciphered Carlsson diary"},
   {"query": "dagbok skriven med chiffer 1860-talet Linköping stiftsbibliotek Carlsson dechiffrerad dagbok", "result": "only the Copiale cipher news and unrelated farm diaries; no decipherment of this diary"},
   {"query": "de-crypt.org/decrypt-web/RecordsList?search=Carlsson / dagbok / Linköping", "result": "0 records each"}]}})
rows.append({
 "year": 1832, "date": "1832",
 "title": "Zacharias Topelius (aged 14): \"Chifferskrift 1832\", a piece of cipher writing among his childhood manuscripts",
 "correspondents": "Zacharias Topelius (1818-1898), author", "place": "unknown (Nykarleby or Uleåborg)", "language": "Swedish",
 "region": "Scandinavia", "period": "1801-1900",
 "shelfmark": "Kansalliskirjasto / National Library of Finland, Topelius archive, Coll. 244.182 (HCaa Barndoms- och ungdomsproduktion)",
 "folio_note": "one file; extent not stated",
 "cls": "C",
 "status": "Finna record fonte.168242480766500_172896282619400: title 'Chifferskrift 1832', genre 'kertomukset' (stories), Swedish; no images, no note of a reading. Whether it is ciphertext or a description of a cipher is not stated.",
 "why": "A cipher text by the boy who became Finland's national storyteller; small but datable and personal.",
 "importance": 2, "solvability": 1, "difficulty": 1,
 "score_note": "Scored from the archive description during the 11 Nov 2026 Nordic sweep (research/sweep_2026-11-11_nordic/); not viewed",
 "verify": "Lead only, no vetting block: the SLS edition Zacharias Topelius Skrifter (topelius.sls.fi) and its volume of early writings were not opened, and the title alone does not show ciphertext. Check the edition, then ask the library for a scan.",
 "links": [{"label": "Finna record", "href": "https://kansalliskirjasto.finna.fi/Record/fonte.168242480766500_172896282619400"}],
 "seen": "catalogue", "source": "Finna API sweep",
 "prior_art": "not established (one web search 11 Nov 2026, 'Topelius Chifferskrift 1832': nothing; SLS edition not checked)",
 "needs_archive_scan": "yes", "access_note": "special reading room of the National Library of Finland, or a scan order"})
rows.append({
 "year": 1913, "date": "1913-1918 (file dates)",
 "title": "Finnish Gendarme Administration: a letter to the Governor-General's deputies containing the gendarmerie's cipher",
 "correspondents": "Finland Gendarme Administration (Russian Corps of Gendarmes) → deputies of the Governor-General of Finland", "place": "Helsinki", "language": "Russian",
 "region": "Scandinavia", "period": "1901-1950",
 "shelfmark": "Kansallisarkisto (National Archives of Finland), Suomenmaalaisen santarmihallinnon arkisto, 6:1, unit 2906 (VAKKA-2268779.KA)",
 "folio_note": "one letter",
 "cls": "C",
 "status": "Finna/Vakka title: 'Kenraalikuvernöörin apulaisille osoitettu santarmiston salakirjoitusta sisältävä kirje' (a letter addressed to the Governor-General's deputies containing the gendarmerie's cipher), 1913-1918. No images; whether it holds ciphertext or the cipher key itself is not clear from the title.",
 "why": "Russian political police cipher practice in Finland just before 1917.",
 "importance": 2, "solvability": 1, "difficulty": 3,
 "score_note": "Scored from the archive description during the 11 Nov 2026 Nordic sweep (research/sweep_2026-11-11_nordic/); not viewed",
 "verify": "Lead only, no vetting block: the title may mean a key sent by letter (then it is a key lead). Order the unit in Astia and look.",
 "links": [{"label": "Finna record", "href": "https://www.finna.fi/Record/narc.VAKKA-319312.KA_VAKKA-2268779.KA"}],
 "seen": "catalogue", "source": "Finna API sweep",
 "prior_art": "not established (one Finnish web search 11 Nov 2026 found nothing on this letter; DECODE search 'gendarm', 'Helsinki': 0)",
 "needs_archive_scan": "yes", "access_note": "Astia order at Kansallisarkisto, Helsinki"})
EXTRA = os.path.join(HERE, "rows_extra.json")
if os.path.exists(EXTRA): rows += json.load(open(EXTRA, encoding="utf-8"))
keys = [
 {"title": "Key to the cipher in Magnus Stenbock's letters from captivity (c. 1713-17)", "shelfmark": "Lunds universitetsbibliotek, 'Strödda historiska handlingar' (3 capsules, c. 1619-1818; Alvin record 261485)", "note": "Alvin: 'Nyckel till chiffer i Magnus Stenbocks brev från fångenskapen'. A second copy of the Stenbock/Malmberg key noted in research/scandinavia (Riksarkivet E 4698); serves the Stenbock captivity letters lead.", "href": "http://urn.kb.se/resolve?urn=urn:nbn:se:alvin:portal:record-261485"},
 {"title": "Förborgad skrifkonst. Konst- och Underbook (manual of secret writing, cryptograms and inks)", "shelfmark": "Uppsala universitetsbibliotek, D 1601 a (Alvin record 468469)", "note": "Four quires, a loose leaf in mirror writing; a treatise, not a ciphertext.", "href": "http://urn.kb.se/resolve?urn=urn:nbn:se:alvin:portal:record-468469"},
 {"title": "Fortress staff of Sveaborg: cipher keys 1916 and papers on cipher 1913", "shelfmark": "Kansallisarkisto, Suomenlinnan linnoituksen esikunnan arkisto, 10033 (VAKKA-2267404.KA) and 10006 (VAKKA-2267192.KA)", "note": "Russian military keys; Finna titles 'Salakirjoitusavaimet (1916)' and 'Salakirjoitusta koskevat asiakirjat (1913)'.", "href": "https://www.finna.fi/Record/narc.VAKKA-215608.KA_VAKKA-2267404.KA"}]
KX = os.path.join(HERE, "keys_extra.json")
if os.path.exists(KX): keys += json.load(open(KX, encoding="utf-8"))
REQ = "year date title correspondents place language region period shelfmark folio_note cls status why importance solvability difficulty score_note verify links seen source prior_art needs_archive_scan access_note".split()
for r in rows:
    miss = [k for k in REQ if k not in r]; assert not miss, miss
    assert isinstance(r["year"], int) and r["cls"] in "ABC" and r["needs_archive_scan"] in ("yes", "no", "partly", "unknown")
json.dump(rows, open(os.path.join(HERE, "candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(keys, open(os.path.join(HERE, "key_leads.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), "rows;", sum(1 for r in rows if r.get("vetting", {}).get("verdict") == "open"), "open blocks;", len(keys), "key leads")
