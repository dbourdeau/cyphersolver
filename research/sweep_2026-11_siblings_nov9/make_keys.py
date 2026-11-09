import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
H = 'https://hetutrechtsarchief.nl/collectie/'
keys = [
 {"year": 1837, "date": "Nov 1837 - 1838", "title": "Spanish army 'Cifra de Música' (a musical-notation cipher) and other keys for reserved correspondence, Army of Reserve of Andalusia, with 59 reserved letters",
  "shelfmark": "Madrid, AHN, DIVERSOS-COLECCIONES,167,N.19 (PARES 3899002)",
  "note": "Description: 'comunicaciones reservadas ... relativas a claves para documentos cifrados'. Viewed images 1-8: a 'Clave de Escritura' folder, a letter of 30 Nov 1837 from the Direccion General del Cuerpo de E.M. enclosing a key, and image 5, a leaf with three music staves showing a note-to-letter table (a to m on the first staff, n to z with note heads below, and an example 'amigo mio vendra'), followed by a second letter of 30 Nov 1837 saying the music cipher can be used without 'travesanos'. Sampled images 9-135: all plain letters (Seville, Cadiz, Andalusia reports). No ciphertext in the sample, but the 134 pages were not all paged. Key-only (check whether any of the 59 letters uses the music cipher).",
  "links": [{"href": "https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3899002", "label": "PARES record"}]},
 {"year": 1671, "date": "1671, 1685", "title": "Letter, number and figure codes for the political correspondence of Godard Adriaan van Reede (Huis Amerongen); marked digitised",
  "shelfmark": "Het Utrechts Archief, toegang 1001 Huis Amerongen, inv. nr. 2883 (old ref. I, 132, 194)",
  "note": "Inventory title: 'Letter-, cijfer- en figuurcodes ten behoeve van de politieke correspondentie, 1671, 1685'; 1 folder, 'Het stuk is digitaal beschikbaar'. Key-only. Ciphered letters to Godard Adriaan van Reede (series 2722-2760) were not flagged in the inventory.",
  "links": [{"href": H + "609C5B995BC54642E0534701000A17FD", "label": "Het Utrechts Archief record"}]},
 {"year": 1780, "date": "1780", "title": "Alphabetical number code of place names, personal names and titles for diplomatic correspondence of G.J. van Hardenbroek, for the States-General, with B. Lesteve(nom)",
  "shelfmark": "Het Utrechts Archief, toegang 1010 Huis Hardenbroek, inv. nr. 1191",
  "note": "Key-only item (EAD OAI-PMH harvest). Related unflagged letters: inv. 995 and 1933 (Mattheus Lestevenon van Berkenrode, Paris, 1771, 1778).",
  "links": [{"href": "https://hetutrechtsarchief.nl/collectie/8734590C08912977E053CA00A8C00B24", "label": "Het Utrechts Archief, 1010 Huis Hardenbroek (fonds record)"}]},
 {"year": 1762, "date": "[1762]", "title": "Key of the number code for the diplomatic correspondence of François Doublet van Groenevelt, Dutch envoy in Sweden",
  "shelfmark": "Het Utrechts Archief, toegang 1010 Huis Hardenbroek, inv. nr. 4515",
  "note": "Key-only. Doublet's letters as envoy in Sweden 1760-62 (inv. 989, 45 letters) and Spain 1762-66 (inv. 990, 72 letters) are in the same fonds with no cipher flag in the inventory: check them for number passages.",
  "links": [{"href": "https://hetutrechtsarchief.nl/collectie/8734590C08912977E053CA00A8C00B24", "label": "Het Utrechts Archief, 1010 Huis Hardenbroek (fonds record)"}]},
]
json.dump(keys, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(keys))
