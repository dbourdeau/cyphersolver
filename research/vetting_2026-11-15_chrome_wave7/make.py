"""Vetting of leads 2843-2853 (sweep_2026-11-15_chrome_wave7, Arxius en linia): writes vetting.json and applies it to
research/leads.json. Promotion is done afterwards with docs/_check_catalogue.py --promote."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BY = "claude session 15 Nov 2026 (Claude Sonnet 5.5), Chrome wave 7 vetting"
D = "2026-11-15"
DEC = ("known.py plus the DECODE dumps (research/catalogue_harvest/decode views.jsonl, views_b, views_c: about 2,450 records) and the Cryptoole snapshot, 15 Nov 2026: "
       "no record for this shelfmark, writer, fonds or correspondent (the dumps are partial, so 'not on DECODE' is as far as they go).")
TOM = ("Tomokiyo's Cryptiana: a web search for the names and the archive returned nothing (15 Nov 2026), and the live code/GL.htm (Lasry's AI-assisted list) was "
       "searched for the shelfmark and names: no entry; no page on this item in the repo holdings (known.py).")
LAS = "GL.htm (Lasry's list, 15 Nov 2026): searched for this shelfmark, fonds and the names, no entry. Lasry's papers: nothing found."
ARCH = ("Arxius en linia record read in Chrome 15 Nov 2026 (arxiusenlinia.cultura.gencat.cat, detallunitat/{ref}); its object list is empty (backend unitat/objects returns no image), "
        "so no facsimile is online: archive item, reading room of the Arxiu Nacional de Catalunya (Sant Cugat del Valles).")
out = {}


def lead(num, **kw):
    out[str(num)] = kw


# 1873 telegrams: image viewed
for num, ref, cipher, extent in [
    (2843, "ANC1-700-T-412",
     "Viewed on the 1,184 x 1,696 px image 15 Nov 2026: printed 'Despacho telegrafico' form, Zaragoza to Castellon 23 Apr 1873, manuscript; the text starts in clear ('Me dicen de Madrid'), then about 60 two-digit groups in blue ink, with a clear 'tambien' inside. No decipherment on or with the sheet; the record holds 1 image.",
     "one leaf, one image, about 60 groups"),
    (2844, "ANC1-700-T-420",
     "Viewed on the image 15 Nov 2026: Madrid to Tarragona, Ministro Gobernacion to the Governor, headed 'Clave L. 13'; about 30 two-digit groups, then clear text (the message is partly in cipher, as the record says). No decipherment on or with the sheet; 1 image.",
     "one leaf, one image, about 30 groups"),
    (2845, "ANC1-700-T-429",
     "Viewed on the image 15 Nov 2026: Madrid to Tarragona 10 Dec 1873, Jefe Seccion politica Gobernacion, headed 'Clave N. 34'; about 190 two-digit groups with a few clear words ('de gobernador desde', 'de V.L. hasta'). No decipherment on or with the sheet; 1 image.",
     "one leaf, one image, about 190 groups")]:
    lead(num, date=D, by=BY,
         seen={"kind": "scan",
               "where": f"Arxius en linia, {ref}: image at static.arxiusenlinia.cultura.gencat.cat/active/GANC/TEXTUAL/1/700/0/{ref.rsplit('-', 1)[1]}/, opened in Chrome 15 Nov 2026.",
               "extent": extent, "cipher": cipher},
         prior_art={"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
                    "edition": "None known: the Josep Anselm Clave papers (ANC1-700) have no published edition of the telegrams that this pass found; the Gaceta de Madrid (BOE) prints the clear telegram traffic of 1873 and not these cipher sheets (web search 15 Nov 2026).",
                    "literature": "Web search 15 Nov 2026 (telegrama cifrado 1873 Gobernacion clave gobernador): nothing on a cipher of the Ministry of the Interior of the First Republic or on these telegrams."},
         searches=[{"query": "known.py 'ANC1-700', 'Clave', 'Zaragoza 1873' and the Arxius en linia cipher terms (xifrat, xifrada, cifrado, 38 terms)", "result": "only the sweep rows and the three Clave telegrams"},
                   {"query": "web: telegrama cifrado 1873 Ministro de la Gobernacion clave gobernador civil Tarragona", "result": "BOE Gaceta pages of plain telegram traffic; no cipher"}],
         key_check="No key held. The two later sheets name their key ('Clave L. 13', 'Clave N. 34'), which implies a numbered family of keys at the Interior Ministry; no table is known. The clear fragments inside the groups ('tambien', 'de gobernador desde') are cribs.",
         duplicates="known.py 'ANC1-700', 'Clave', 'Anselm' (15 Nov 2026): no hit in the ledgers; the other Clave telegrams are the siblings 2843-2845 of this wave. One cipher per sheet is possible; they may share a family.",
         verdict="open",
         lead_updates={"seen": "image"})

# Carlist letters, Saavedra, Castelldosrius, Carreras: not online
CARL_ED = ("None found: the Rocaberti-Dameto papers in the ANC collection on the Carlist wars have no edition or study of their cipher letters in a web search (15 Nov 2026); "
           "an auction lot of 25 Rocaberti drafts to Metternich 1840-47 is the only outside trace of the correspondence.")
for num, ref, extent, cipher, key in [
    (2846, "ANC1-1391-T-92", "2 units; one of them 'una carta xifrada'",
     "Archive text: 'conte una carta on es tracten diversos aspectes del viatge, allotjament, correspondencia, financament i sospites sobre traidoria de dirigents carlins. Tambe conte una carta xifrada.' Draft letters, Modena 7 Jul 1842, Spanish. No decipherment is mentioned.",
     "Key probably the Alcudia cipher tables of 16 Jun 1840 in the same collection (ANC1-1391-T-14, 'taules i instruccions per desxifrar els missatges codificats. Inclou les taules.'), also not online and not tested. A key in the collection does not block the lead."),
    (2847, "ANC1-1391-T-115", "1 unit, 'carta xifrada'",
     "Archive text: 'Volum: 1 unitat. Abast i contingut: carta xifrada. Llengua: castella. Tecnica: manuscrit.' Draft letter, Vienna 30 Dec 1842, to Carlos Maria Isidro. No decipherment is mentioned.",
     "As 2846: the Alcudia tables of 1840 (ANC1-1391-T-14) are the likely key, not online and not tested.")]:
    lead(num, date=D, by=BY,
         seen={"kind": "not online", "where": f"Arxius en linia, {ref}. " + ARCH.format(ref=ref), "extent": extent, "cipher": cipher},
         prior_art={"decode": DEC, "tomokiyo": TOM, "lasry": LAS, "edition": CARL_ED,
                    "literature": "Web search 15 Nov 2026 (Rocaberti-Dameto cifra carta xifrada guerres carlines): nothing on cipher in the correspondence; the Alcudia-Rocaberti letter of 11 Jun 1840 appears on the Generalitat's patrimoni portal as a letter about finance, not as cipher."},
         searches=[{"query": "known.py 'Rocabert', 'ANC1-1391', 'guerres carlines'", "result": "no hit before this wave"},
                   {"query": "web: Rocaberti-Dameto carlista cifra carta xifrada Arxiu Nacional de Catalunya", "result": "nothing on the cipher"}],
         key_check=key,
         duplicates="known.py 'Rocabert', 'ANC1-1391', 'Alcudia' (15 Nov 2026): no hit in catalogue.json, leads.json or the sweeps before this wave. Siblings in this wave: 2846/2847/2848 (T-92, T-115, T-421); T-87 (7 Apr 1842, 'carta parcialment encriptada' that also reports a deciphered Metternich message) and T-113 are left out as the description mentions a decipherment.",
         verdict="open",
         lead_updates={"access_note": ARCH.format(ref=ref), "seen": "catalogue"})

lead(2848, date=D, by=BY,
     seen={"kind": "not online", "where": "Arxius en linia, ANC1-1391-T-421. " + ARCH.format(ref="ANC1-1391-T-421"),
           "extent": "1 unit, a letter partly in cipher",
           "cipher": "Archive text: 'carta parcialment encriptada referent a la recepcio d'informes i a realitzar operacions de batuda a la Catalunya Central.' Pere Nolasc Bassa (Cardona) to Manuel Llauder, 22 Feb 1835, Spanish, manuscript. No decipherment is mentioned."},
     prior_art={"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
                "edition": "None found for this letter (web search 15 Nov 2026); Llauder's papers are cited in Carlist-war histories, none of them for a cipher.",
                "literature": "Web search 15 Nov 2026 (Bassa Llauder 1835 carta encriptada): nothing."},
     searches=[{"query": "known.py 'Llauder', 'Nolasc', 'ANC1-1391'", "result": "no hit before this wave"}],
     key_check="No key held. The Carlist cipher tables in the same collection are of 1840 (a different system, other correspondents); no key for a Cardona officer of 1835 is known.",
     duplicates="known.py 'Llauder', 'Bassa', 'ANC1-1391-T-421' (15 Nov 2026): no hit.",
     verdict="open", lead_updates={"access_note": ARCH.format(ref="ANC1-1391-T-421"), "seen": "catalogue"})

lead(2849, date=D, by=BY,
     seen={"kind": "not online", "where": "Arxius en linia, ANC1-53-T-702. " + ARCH.format(ref="ANC1-53-T-702"),
           "extent": "156 folios (ff. 174-329) of a 534-folio parchment book; 55 letters signed by the king, mostly 1644",
           "cipher": "Archive text: 'Cartes xifrades relacionades amb les negociacions de pau (1640-1646): folis 174 a 329. Hi ha 55 cartes signades pel rei catolic (la majoria pertanyen al 1644).' The record lists the other sections of the 'especul d'escriptures' (titles, safe-conducts, Munster papers) with no mention of a decipherment, and says the book needs restoration."},
     prior_art={"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
                "edition": "Not found: web search 15 Nov 2026 turned up Saavedra Fajardo's Munster letters in the literature (Boadas, Saez, Gonzalez Canal) and ANC fonds Blanes-Centelles i Saavedra n. 65 (Philip IV to Saavedra, Zaragoza 24 Sep 1644, ff. 244-245), but no source that prints or deciphers the 'cartes xifrades' of this book.",
                "literature": "Web search 15 Nov 2026 (Saavedra Fajardo cartas cifradas Munster 1644): nothing on cipher in this book. The ledger holds a Sarmiento/Saavedra Fajardo cipher lead of 1638-39 from the RAH (leads 1086-1088) that is a different series."},
     searches=[{"query": "known.py 'Saavedra Fajardo', 'Blanes-Centelles', 'ANC1-53'", "result": "only the RAH/Sarmiento leads (1086-1088), the Belgian AGATHA Saavedra row and Dudout's Sarmiento ms 2093; none is this book"},
               {"query": "web: Saavedra Fajardo cartas cifradas Munster 1644 Felipe IV descifradas", "result": "context only; nothing on this cipher"}],
     key_check="No key held. Philip IV's cipher to his Munster plenipotentiary is not known to survive; the Spanish general ciphers of the 1640s (Simancas Estado) may be the family. Decipherments may exist in the volume itself, which the description does not say.",
     duplicates="known.py 'Saavedra Fajardo', 'ANC1-53', 'Blanes-Centelles' (15 Nov 2026): only different series. Not the Sarmiento/Cardinal-Infante leads.",
     verdict="open", lead_updates={"access_note": ARCH.format(ref="ANC1-53-T-702"), "seen": "catalogue"})

lead(2850, date=D, by=BY,
     seen={"kind": "not online", "where": "Arxius en linia, ANC1-167-T-3773. " + ARCH.format(ref="ANC1-167-T-3773"),
           "extent": "two cipher letters inside a composite unit of 478 documents (1681-1700)",
           "cipher": "Archive text: 'conte una carta autografa de Carles II sobre la successio al tron d'Espanya i dues cartes xifrades.' Volume: 478 units, Spanish, manuscript, old sig. 1242.19. Which two letters, their length and their writers are not stated; no decipherment is mentioned."},
     prior_art={"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
                "edition": "None found: the Castelldosrius correspondence is used in studies (Gomez Mesas, Burgos Lejonagoitia on the marquis's agents of 1709, Saenz-Rico on the viceroy of Peru), none of which prints a cipher letter of 1681-1700 from this unit (web search 15 Nov 2026).",
                "literature": "Web search 15 Nov 2026 (Castelldosrius cartes xifrades Carles II): nothing on cipher in the unit."},
     searches=[{"query": "known.py 'Castelldosrius', 'Sentmenat', 'ANC1-167'", "result": "no hit before this wave"},
               {"query": "web: marques de Castelldosrius cartes xifrades Carles II", "result": "background only"}],
     key_check="No key held. Castelldosrius was ambassador to Louis XIV from 1698; a cipher between him and Madrid is plausible but no table is known.",
     duplicates="known.py 'Castelldosrius', 'Sentmenat', 'ANC1-167-T-3773' (15 Nov 2026): no hit.",
     verdict="open", lead_updates={"access_note": ARCH.format(ref="ANC1-167-T-3773"), "seen": "catalogue"})

lead(2851, date=D, by=BY,
     seen={"kind": "not online", "where": "Arxius en linia, ANC1-171-T-183. " + ARCH.format(ref="ANC1-171-T-183"),
           "extent": "10 documents, typescript, 11-18 Jul 1936",
           "cipher": "Archive text: 'Telegrames xifrats. Volum: 10 unitats documentals. Llengua(es): frances. Tecnica: mecanoscrit. Cronologia 11.07.1936 - 18.07.1936. Observacions: Inclou claus.' No decipherment is mentioned; the keys are filed with them."},
     prior_art={"decode": DEC, "tomokiyo": TOM, "lasry": LAS,
                "edition": "None found (web search 15 Nov 2026).",
                "literature": "Web search 15 Nov 2026 (Narcis de Carreras telegrames xifrats juliol 1936): nothing."},
     searches=[{"query": "known.py 'Carreras i Guiteras', 'ANC1-171'", "result": "no hit before this wave"}],
     key_check="'Inclou claus': keys are filed in the unit, in the archive (not online, not tested). A key in the unit does not block the lead; whether it is a code book or a key to these ten telegrams is not stated.",
     duplicates="known.py 'Narcis de Carreras', 'Carreras i Guiteras', 'ANC1-171' (15 Nov 2026): no hit.",
     verdict="open", lead_updates={"access_note": ARCH.format(ref="ANC1-171-T-183"), "seen": "catalogue"})

N = {
    "2852": "ANC1-408-T-1891 (Andreu i Abello, about 150 'copies de telegrames, cablegrames i radiogrames xifrats', Spanish Embassy in Mexico 1937): the record says the unit holds copies, but not whether they show ciphertext or clear text; not promoted until that is known. Not online.",
    "2853": "ANC1-1-T-7519 (Generalitat 1937 file, 96 images online): the images were not paged through, so no cipher telegram was seen and none is cited; not promoted.",
}
for i, s in N.items():
    out.setdefault(i, {"unvetted": "Vetting pass 15 Nov 2026 (Chrome wave 7): " + s})

json.dump(out, open(os.path.join(HERE, "vetting.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
sys.path.insert(0, os.path.join(ROOT, "docs"))
import _check_catalogue as C
d, leads = C.load(C.LEADS, "leads")
byid = {str(l["id"]): l for l in leads}
for i, b in out.items():
    l = byid[i]
    if "unvetted" in b:
        l["vetting_note"] = b["unvetted"]
        continue
    b = dict(b)
    l.update(b.pop("lead_updates", {}))
    l["vetting"] = b
C.save(C.LEADS, d)
print("applied", len(out))
