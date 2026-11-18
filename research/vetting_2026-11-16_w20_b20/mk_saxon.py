import json
BY = "claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting"
TOMO = "Tomokiyo's unsolved.htm (fetched 15 Nov 2026) searched for %s: no entry."
LAS = "Lasry's GL.htm (fetched 15 Nov 2026) searched for %s: no entry."
def w(i, d): json.dump(d, open('parts/%s.json' % i, 'w', encoding='utf8'), ensure_ascii=False, indent=1)

w('2657', {
 "verdict": "read", "confidence": "high",
 "note": "The archive's own title (archiv.sachsen.de and DDB record, 16 Nov 2026) is 'Dechiffrierte Briefe, meist aus der Zeit des Siebenjaehrigen Krieges, unter anderm vom Feldwachtmeister de Vela an den saechsischen Kurprinzen': the file is the contemporary decipherments themselves. Whether cipher originals lie beside them is not stated, but the texts were read at the time.",
 "access": "archive",
 "access_note": "Saechsisches Hauptstaatsarchiv Dresden, 10026 Geheimes Kabinett, Loc. 03447/28 (Gliederung 039.303 Vela, de), 1758-1759; no digital copy (digitalisatExists false on archiv.sachsen.de).",
 "vetting": {"date": "2026-11-16", "by": BY,
  "seen": {"kind": "not online",
   "where": "Archive record https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=ac907a36-1640-4778-9e23-f5acc2b07e80 fetched by curl 16 Nov 2026 and the DDB Solr record id DSKEZ6L4SSQ7S7RLO7SBXAFZ5TMYRBUM (both saved in src/); no digital copy.",
   "extent": "One file, 1758-1759, of several letters ('Briefe ... unter anderm vom Feldwachtmeister de Vela'); leaf count not given.",
   "cipher": "Archive title, verbatim: 'Dechiffrierte Briefe, meist aus der Zeit des Siebenjaehrigen Krieges, unter anderm vom Feldwachtmeister de Vela an den saechsischen Kurprinzen'. The letters are described as deciphered; not seen."},
  "prior_art": {"decode": "known.py on '03447/28' and 'Vela' (16 Nov 2026): only this lead and its sweep row; 'Vela' otherwise hits Velada/Velasco rows of other archives. No DECODE record.",
   "tomokiyo": TOMO % "Vela, Saxon, Saxony",
   "lasry": LAS % "Vela, Saxony (one 'Vela' hit is Velasco in a BnF list)",
   "edition": "The decipherment is the file itself (contemporary deciphered copies), so no printed edition is needed to establish that the letters were read; no edition was searched.",
   "literature": "No web search: the archive's title states the letters are deciphered, which decides the verdict."},
  "key_check": "No key for de Vela's correspondence with the Saxon Electoral Prince is held in the repo; the deciphered copies would give one if the cipher originals survive. Not tested.",
  "duplicates": "known.py on the shelfmark: no other lead or catalogue entry.",
  "verdict": "read",
  "closed": "The archive titles the file 'Dechiffrierte Briefe': the letters are present as contemporary decipherments, so they were read at the time."}})

w('2658', {
 "verdict": "partly_read", "confidence": "medium",
 "note": "Loc. 00694/10 is Dr. Krauske's 1893 work 'Chiffren in Schreiben Manteuffels an Flemming', containing 'Einige Chiffre-Aufloesungen zu den Berichten Manteuffels an Flemming 1712 und 1713 (Loc. 694/08 und 694/09)', and the 14 Nov viewing found a reconstructed code table (numbers with French words). So the 1712-13 reports were partly deciphered in 1893 and the rest reads by lookup in Krauske's table; the ciphered passages in 694/08-09 were never located. Not an open cipher.",
 "access": "online",
 "access_note": "Loc. 00694/10 is digitised (7 microfilm frames, archiv.sachsen.de viewer, seen in Chrome 14 Nov 2026); the report volumes Loc. 694/08 (digitised microfilm) and 694/09 were not paged for the ciphered passages.",
 "vetting": {"date": "2026-11-16", "by": BY,
  "seen": {"kind": "scan",
   "where": "Saxon digital copy of 10026 Geheimes Kabinett Loc. 00694/10 (archiv.sachsen.de, guid 96698908-5fa7-4fb6-ae66-bf4617f6e401), viewed 14 Nov 2026 in the German state databases vetting (research/vetting_2026-11-14_german_state_dbs/README.md); record re-read by curl and the DDB Solr record HJGLVTUASTOYY3PNBCB5D6WNXF3AIXO6 on 16 Nov 2026.",
   "extent": "Seven microfilm frames: Krauske's 1893 title sheet and a table of code numbers with French words (persons and places). The reports themselves (Loc. 694/08, 1712, and 694/09, 1713) were not paged; the first 12 frames of 694/08 were clear French letters.",
   "cipher": "Archive description, verbatim: 'Chiffren in Schreiben Manteuffels an Flemming (angefertigt von Dr. Krauske, 1893). Enthaelt u. a.: Einige Chiffre-Aufloesungen zu den Berichten Manteuffels an Flemming 1712 und 1713, (Loc. 694/08 und Loc. 694/09)'. A numerical code with French plaintext, reconstructed by Krauske."},
  "prior_art": {"decode": "known.py on '694/08' and 'Manteuffel' (16 Nov 2026): only this lead, its sweep row and the vetting note of 14 Nov; research/archivportal_d lists Flemming key volumes, not this one. No DECODE record.",
   "tomokiyo": TOMO % "Manteuffel, Flemming, Saxon, Saxony",
   "lasry": LAS % "Manteuffel, Flemming, Saxony",
   "edition": "Krauske's 1893 resolutions are themselves the modern decipherment (manuscript, filed as Loc. 694/10); no printed edition of the 1712-13 reports was searched.",
   "literature": "No web search: the archive record of the 1893 decipherment decides the verdict."},
  "key_check": "Krauske's 1893 reconstructed code table (numbers to French words) is Loc. 694/10 itself, digitised; it was not applied to the reports in 694/08-09, whose ciphered passages were not located.",
  "duplicates": "known.py on the shelfmarks and Manteuffel: no catalogue entry; the 'Graefl. Flemmingsche Chiffres' key volumes in the Saxon sweeps are other files.",
  "verdict": "partly_read",
  "closed": "Krauske deciphered parts of Manteuffel's 1712-13 reports to Flemming in 1893 and reconstructed the code table, so the cipher is keyed and partly read; what remains is lookup, not an open cipher."}})

w('2659', {
 "verdict": "read", "confidence": "medium",
 "note": "The archive's own content note for the Hitzschold police file (archiv.sachsen.de and DDB, 16 Nov 2026) is 'Enthaelt u. a.: Entschluesselung chiffrierter Schreiben': the police decipherment of the ciphered letters is filed in it. The 6-frame digital copy seen on 14 Nov shows no cipher leaf, so neither the cipher nor the decipherment has been seen; the verdict rests on the archive's description.",
 "access": "archive",
 "access_note": "Saechsisches Hauptstaatsarchiv Dresden, 10736 Ministerium des Innern, Nr. 00457/02 (09.02.06 Ueberwachung von Einzelpersonen), 1850; a partial digital copy of 6 frames on archiv.sachsen.de (cover and clear leaves only).",
 "vetting": {"date": "2026-11-16", "by": BY,
  "seen": {"kind": "not online",
   "where": "Archive record https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=955476c9-0978-4861-b8a9-a274c7c13b53 fetched by curl 16 Nov 2026 and DDB Solr record NA6LUEJGWYPVG7662QNN5Z2QOWIXK447; its 6-frame digital copy was viewed in Chrome on 14 Nov 2026 (research/vetting_2026-11-14_german_state_dbs/README.md) and shows no cipher sheet.",
   "extent": "One police surveillance file of 1850 on Carl Heinrich Hitzschold, former Justizamtmann at Wolkenstein; the number of ciphered letters is not given.",
   "cipher": "Archive content note, verbatim: 'Enthaelt u. a.: Entschluesselung chiffrierter Schreiben' (contains, among other things, the decryption of ciphered letters). Neither the cipher nor the decryption leaf is in the 6 frames online."},
  "prior_art": {"decode": "known.py on 'Hitzschold' and '00457/02' (16 Nov 2026): only this lead, its sweep row and the 14 Nov vetting note. No DECODE record.",
   "tomokiyo": TOMO % "Hitzschold, Saxon, Saxony",
   "lasry": LAS % "Hitzschold, Saxony",
   "edition": "No edition; the decryption is filed in the police file itself per the archive, so no print was searched.",
   "literature": "No web search: the archive's note that the file contains the decryption decides the verdict."},
  "key_check": "No key held; the police decryption in the file would give it. Not tested.",
  "duplicates": "known.py on the shelfmark and name: no other lead or catalogue entry.",
  "verdict": "read",
  "closed": "The archive describes the file as containing the decryption of the ciphered letters, so the Saxon police read them in 1850."}})
