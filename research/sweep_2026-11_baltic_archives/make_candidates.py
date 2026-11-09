import json
rows=[{"year":1907,"date":"1907","title":"Mihkel Sild's account of the 1905 events at Avinurme, written in secret writing (19 leaves)",
"correspondents":"Mihkel Sild (peasant-craftsman, Avinurme), account, no addressee","place":"Avinurme, Estonia (Governorate of Livonia)","language":"Estonian (presumed)",
"region":"Other","period":"1901-1950" if False else "1901-1950","shelfmark":"Eesti Ajaloomuuseum fonds, Rahvusarhiiv AIS AM.272.1.97","folio_note":"19 leaves; series 5 of fonds AM.272 (indictment of 31 Oct 1905 and Sild's descriptions of the 1905 events)",
"cls":"B","status":"AIS title: 'Ajalugu. Ulestahend. M. Sild. 1905-1906 Avinurmes (salakirjas)'; no decipherment or transcription mentioned in the record.",
"why":"Personal secret-script narrative of a 1905 revolution episode (breaking of the Tsar's portrait in the Avinurme parish house); a short, single-writer private cipher in a vernacular language, probably a simple substitution or invented alphabet.",
"importance":2,"solvability":3,"difficulty":2,"verify":"Order scans from the Estonian History Museum / Rahvusarhiiv (reading room: Ajaloomuuseum); check whether the 'salakiri' is a cipher or merely shorthand or Gothic script; look in AM.272.1.10 notebooks (series 10) and diaries (series 2) for the same hand.",
"links":[{"href":"https://ais.ra.ee/et/description-unit/view?id=126000102885","label":"AIS record"}],
"access_note":"description only on AIS; no digital object on the record; 'Uurimissaal: Ajaloomuuseum'",
"source":"Baltic archives sweep (AIS term sweep), 9 Nov 2026","score_note":"Scored from the AIS description; not viewed",
"prior_art":"open as far as checked (9 Nov 2026): known.py finds nothing on the shelfmark, Sild or Avinurme; one web search found no decipherment or study. Date is after 1900 (1907) and the content is not diplomatic: a weak lead.",
"seen":"catalogue","needs_archive_scan":"yes"}]
json.dump(rows,open('candidates.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
json.dump([{"note":"EAA.29.2.5365 (1881): file on introducing a new secret telegraph cipher key by the Ministry of the Interior; administration, no key text seen"}],open('key_leads.json','w'),indent=1)
