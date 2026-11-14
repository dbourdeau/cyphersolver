"""Build candidates.json and key_leads.json from the saved hits/details (hand-vetted specs below)."""
import json, pathlib
H = pathlib.Path(__file__).parent
det = {}
for l in open(H/"details.jsonl", encoding="utf8"):
    d = json.loads(l); det[d["ref"]] = d
hits = {}
for f in ("hits_AHU.jsonl", "hits_ALL.jsonl"):
    for l in open(H/f, encoding="utf8"):
        r = json.loads(l); hits[r["ref"]] = r
def link(ref, label):
    i = (det.get(ref) or hits.get(ref))["id"]
    return {"label": label, "href": "https://digitarq.arquivos.pt/documentDetails/" + i}
PA = "open (checked 14 Nov 2026: DECODE keyword search, known.py, Tomokiyo unsolved.htm snapshot, two web searches; no decipherment or edition found; Lasry/HistoCrypt not searched beyond the web query)"
common = {"language": "Portuguese", "region": "Other", "cls": "C", "seen": "catalogue", "source": "Arquivo Histórico Ultramarino / Torre do Tombo (DigitArq) sweep",
          "prior_art": PA, "needs_archive_scan": "yes", "decode_ids": []}
common.pop("decode_ids")
sc = "Scored from the DigitArq description during the 14 Nov 2026 Portuguese Africa sweep (research/sweep_2026-11-14_africa_portugal/); not viewed"
rows = [
 dict(year=1897, date="1897", title="Lourenço Marques railway, documents on the Berne arbitration, with enciphered documents",
  correspondents="Portuguese Ministry of the Navy and Overseas / railway arbitration papers", place="Lisbon / Lourenço Marques / Berne",
  period="1801-1900", shelfmark="AHU, Iconografia/Obras Públicas, PT/AHU/ID-OP/OP16696 («1897. Caminho-de-Ferro de Lourenço Marques. Documentos relativos à arbitragem de Berne»)",
  folio_note="folder of reports; DigitArq: 'Contém relatórios, e documentação cifrada'; amount of cipher unknown", 
  status="DigitArq description says the folder contains enciphered documentation; no images online (0 files); no decipherment noted; not on DECODE (searched Lourenço Marques, Delagoa, Angola: 0 records)",
  why="Portugal's side of the Delagoa Bay railway arbitration (Berne convention 1891, award 1900), a great-power dispute over the Transvaal's sea outlet.",
  importance=3, solvability=1, difficulty=4, score_note=sc,
  verify="Order scans or consult at AHU Lisbon; check whether the cipher is Portuguese ministerial or a British/US copy",
  links=[link("PT/AHU/ID-OP/OP16696","DigitArq record")], access_note="no images online; AHU reading room or reproduction order"),
 dict(year=1896, date="1891; 1896-1898", title="Lourenço Marques railway and harbour works files containing cipher telegrams (four folders)",
  correspondents="Direcção das Obras Públicas, Lourenço Marques / Ministry in Lisbon", place="Lourenço Marques / Lisbon",
  period="1801-1900", shelfmark="AHU, ID-OP: OP16752 (1891, Caminho-de-Ferro diversos assuntos); OP16773 (1896, pasta 1); OP16774 (1897, pasta 2); OP16775 (1898, pasta 3), Obras Públicas de Lourenço Marques, Caixa H",
  folio_note="each description lists 'telegramas cifrados' among other papers; counts unknown", 
  status="DigitArq descriptions: 'telegramas cifrados' in each folder; no images online; no decipherment noted; not on DECODE",
  why="Official telegrams of the Mozambique public works direction during the Delagoa Bay railway and port contracts (Sivewright-Verloop agreement of Dec 1891, Schneider and Winby port proposals).",
  importance=2, solvability=1, difficulty=4, score_note=sc, verify="Order scans; look for a telegraph code book in the same fonds (SEMU/GM/004 cifrantes of 1888 are the Ministry's own)",
  links=[link("PT/AHU/ID-OP/OP16752","OP16752 (1891)"),link("PT/AHU/ID-OP/OP16773","OP16773 (1896)"),link("PT/AHU/ID-OP/OP16774","OP16774 (1897)"),link("PT/AHU/ID-OP/OP16775","OP16775 (1898)")],
  access_note="no images online; AHU reading room or reproduction order"),
 dict(year=1891, date="1891-1892", title="Mozambique, telegrams received and sent 1891-1892, foreign affairs, with enciphered telegrams",
  correspondents="Governor-General of Mozambique / Lisbon", place="Mozambique / Lisbon",
  period="1801-1900", shelfmark="AHU, ID-OP, PT/AHU/ID-OP/OP19560 («Moçambique. Telegramas recebidos e expedidos. 1891-1892»)",
  folio_note="DigitArq: 'Referentes a negócios estrangeiros. Contém cifrados'", 
  status="DigitArq description only; no images online; no decipherment noted; not on DECODE",
  why="Telegrams on foreign affairs between Lisbon and Mozambique in the year after the 1890 British Ultimatum and the Anglo-Portuguese treaty of 1891.",
  importance=3, solvability=1, difficulty=4, score_note=sc, verify="Order scans; BNP MSS. 146 n. 840 (Serpa Pinto on the telegraph ciphers, 1890) may hold the system",
  links=[link("PT/AHU/ID-OP/OP19560","DigitArq record")], access_note="no images online; AHU reading room or reproduction order"),
 dict(year=1898, date="1898", title="Conference on the railways at the Cape, 1898, correspondence containing one cipher telegram",
  correspondents="Portuguese delegation / Lisbon", place="Cape Town / Lisbon",
  period="1801-1900", shelfmark="AHU, ID-OP, PT/AHU/ID-OP/OP17197 («Conferência sobre os caminhos-de-Ferro no Cabo» 1898)",
  folio_note="DigitArq: 'Correspondência, contém telegrama cifrado' (one telegram)", 
  status="DigitArq description only; no images online; no decipherment noted; not on DECODE",
  why="Portuguese position on the Transvaal-Mozambique railway tariffs in the Cape conference of 1898, before the South African War.",
  importance=2, solvability=1, difficulty=4, score_note=sc, verify="Order scans", links=[link("PT/AHU/ID-OP/OP17197","DigitArq record")],
  access_note="no images online; AHU reading room or reproduction order"),
 dict(year=1900, date="undated (José Luciano de Castro papers cover 1852-1918)", title="Cipher telegrams of the Governo Geral de Moçambique to an unidentified addressee, in the José Luciano de Castro papers",
  correspondents="Governo Geral de Moçambique → unknown", place="Mozambique",
  period="unknown", shelfmark="ANTT, José Luciano de Castro, Correspondência, caixa 7, PT/TT/JLC/007/00007",
  folio_note="item filed between 'J. Milícia' and Mo- names in an alphabetical box; telegrams in cipher, number unknown; 'year' 1900 is a placeholder for an undated item",
  status="DigitArq title 'Telegramas em cifra do governo geral de Moçambique para destinatário não identificado'; undated; no images; the Oct 2026 Torre do Tombo sweep harvested the record (hits.jsonl) but did not row it; no decipherment noted; sibling lead JLC/008/00083 (Pindela) is in the catalogue",
  why="Colonial government telegrams in cipher that reached a Progressive Party prime minister (1886-90, 1897-1900, 1904-06), probably during a Mozambique crisis.",
  importance=2, solvability=1, difficulty=4, score_note=sc, verify="Ask ANTT for the box 7 item; the date will fix the period and the likely telegraph code",
  links=[link("PT/TT/JLC/007/00007","DigitArq record"),{"label":"Parent: caixa 7","href":"https://digitarq.arquivos.pt/documentDetails/0fa937c76e1a436890846d1875d28257"}],
  access_note="no images online; ANTT reading room or reproduction order"),
 dict(year=1947, date="1947-1950", title="Ministry of the Overseas 'Telegramas cifrados' for Angola, Mozambique, Guinea, Cabo Verde and São Tomé, 1947-1950",
  correspondents="Ministério das Colónias/Ultramar ↔ governors of Angola, Mozambique, Guinea, Cabo Verde, São Tomé e Príncipe", place="Lisbon / Portuguese Africa",
  period="1901-1950", shelfmark="AHU, Ministério do Ultramar, Gabinete do Ministro, Telegramas cifrados recebidos/expedidos: MU-GM/111/Teleg00011, 00014, 00015 (Angola 1947); MU-GM/116/Teleg00401-00404 (Mozambique 1947); MU-GM/113/Teleg00918-00919 (Guinea 1947); MU-GM/112/Teleg01082-01092 (Cabo Verde 1947-50); MU-GM/117/Teleg01371-01372 (São Tomé 1947)",
  folio_note="about 17 folders of 1947-50; the series continues to 1976 (not rowed, after 1950)", 
  status="DigitArq titles only, 0 files online; ministerial cipher telegrams of the late colonial period, probably machine or one-time-pad systems; no decipherment noted; not on DECODE",
  why="Governor-level telegrams of the post-war colonial administration; low odds of a reading without the key books.",
  importance=2, solvability=1, difficulty=5, score_note=sc, verify="Find out whether the AHU also holds the cipher books (SEMU/GM/004 holds only 1888 cifrantes); order one folder",
  links=[link("PT/AHU/MU-GM/116/Teleg00401","Mozambique 1947 (1st pasta)"),link("PT/AHU/MU-GM/111/Teleg00014","Angola 1947 (1st pasta)"),link("PT/AHU/MU-GM/112/Teleg01082","Cabo Verde 1947")],
  access_note="no images online; AHU reading room or reproduction order"),
]
for r in rows:
    r.update(common)
json.dump(rows, open(H/"candidates.json","w",encoding="utf8"), ensure_ascii=False, indent=1)
keys = [
 {"title":"Jesuit alphabet cipher 'enviada de N.P. Claudio Aquaviva aos vinte e tres de Março de 1587', with the rules for nulls and a second cipher, copied in an Angolan despatch of 1760",
  "shelfmark":"AHU, Conselho Ultramarino, Angola, cx. 47, doc. 4298, PT/AHU/CU/001/0047/04298 (1760-10-08)",
  "seen":"image (32 scans, DigitArq /api/rdigital; table seen at m0007, m0015 and m0027, with show-through on the following leaf, several copies of the same table)",
  "what":"A 26-letter plaintext alphabet over a row of symbols and a row of digits (duplicate signs with numerals for the vowels, nulls any sign with a dot above or below), copied by António de Vasconcelos, governor of Angola, to Oeiras (Pombal) with Fr. João de Paiva's letter of 1666 and the note that the cipher was reformed by Provincial João Correia. A table only, no ciphertext on these leaves.",
  "links":[{"label":"DigitArq record","href":"https://digitarq.arquivos.pt/documentDetails/20b0b55ced384c238de7d34bb6f0b6fe"}],
  "use":"Candidate key for Jesuit ciphertexts of the 1580s-1759; compare with the Pombal-era PBA. 614 f. 33-34v lead (BNP sweep) and COD. 10566//3 'Cifra de nomes antigos'."},
 {"title":"Cifrantes for the Minister's official and confidential correspondence, 1888","shelfmark":"AHU, Secretaria de Estado da Marinha e Ultramar, Gabinete do Ministro, PT/AHU/SEMU/GM/004 (items 0001, 0002; 'Lv. s/n')",
  "seen":"catalogue only (0 files)","what":"Two code books (cifrantes) of 1888 for the Ministry's confidential and official correspondence; the key to the Ministry's telegrams of the period.",
  "links":[{"label":"DigitArq record","href":"https://digitarq.arquivos.pt/documentDetails/01fd0007257245e28a4dc322fc33c7d7"}],"use":"Possible key for the 1891-98 Mozambique telegram rows if the system carried over."},
 {"title":"Conselho Ultramarino consultas of 1644 on a new cipher for the Viceroy of India and Goa's request for one","shelfmark":"AHU, CU, Índia, PT/AHU/CU/034/0211/00028 and /00015 (1644)","seen":"catalogue only",
  "what":"Titles only: 'se haver de mandar nova cifra'; no cipher text.","links":[{"label":"00028","href":"https://digitarq.arquivos.pt/documentDetails/d6288f16742240cab935f09b1a112d52"},{"label":"00015","href":"https://digitarq.arquivos.pt/documentDetails/a290ca9e271547af957c4d506f6f3b5f"}],"use":"Dates the introduction of a Portuguese India cipher (not Africa)."},
]
json.dump(keys, open(H/"key_leads.json","w",encoding="utf8"), ensure_ascii=False, indent=1)
print(len(rows), len(keys))
