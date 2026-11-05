# Balkans and Greece sweep (2 Nov 2026): 0 rows

`candidates.json` is empty on purpose. Nothing found met the bar (unread, pre-1950 letter or document with a real
shelfmark and a record link, not already tracked). I did not pad it.

## What was reached
- **Europeana API** (`api2demo` key, `eu.py`, one request per 2.5 s, TYPE:TEXT, country filter). 44 terms (Croatian/Serbian
  šifra, šifrirano, šifrovano, tajnopis; Cyrillic шифра, шифр, шифрован, шифър, тайнопис; Albanian cifër; Italian cifra, cifrata;
  English, French, German; Greek κρυπτογραφ-*, κώδικας) x 10 countries (Croatia, Serbia, Slovenia, Greece, Bulgaria, Bosnia,
  Montenegro, Albania, North Macedonia, Kosovo). 363 distinct records, raw in `europeana_raw.json`. Almost all noise:
  computer-science papers (Serbian NL), Bulgarian newspaper articles, Hebrew "Sifra", Venizelos-archive telegrams of the 1910s-30s
  (SearchCulture/NHRF, telegram noise, skipped), a Philatelic Postal Museum telegram, an undated Academy of Athens "Κρυπτογραφημένο
  σημείωμα" (no writer, date or addressee; not a letter).
- **Web searches** (Ragusa/Dubrovnik ciphers, HDA Zagreb, Greek GAK, Filiki Eteria): nothing citable beyond the Vrančić literature.

## Excluded as already read
- **Vasil Levski, BIA fonds 85, II A 8108 (accounts and committee cipher, 29 Apr 1872) and the southern Bulgaria tour notes
  (Europeana 9200368/BibliographicResource_3000113715906 and ...715394)**: both printed with the decipherment in *Vasil Levski.
  Documents* (2000 facsimile, 2009 "разчетен текст", nos. 150 and 231); the second has a later red-pencil decipherment by
  Strashimirov on the sheet. Not in the repo. Worth a target if the user wants "read in print, re-derive the key".
- **Vrančić (Antun, Paris 1546; Mihovil, Šibenik 1558-59, four letters; five code books in the Széchényi Library)**:
  Lončar and Sorić (Colloquia Maruliana XXII, XXIII, 25; Antun's passage solved in Lončar's later part II). Already read;
  catalogue 501 and the Ferducci/Ragusa rows already cover the HHStA Türkei side.

## What blocked
- Hosts that did not resolve or reset from this machine: arhinet.arhiv.hr (HDA), pavs.sik.gov.si, arhiv.gov.si, arhiv.rs,
  gak.gov.gr catalogue, archive.benaki.org, archives.gr, arhivdubrovnik.hr. Network level, not a bot check, so Chrome was not used.
- dad.hr (Dubrovnik State Archives) is a WordPress site with no online catalogue to search.
- Bot checks: hrcak.srce.hr file downloads (HTTP 418) and doaj.org (Cloudflare). Article abstract pages loaded; full texts did not.
  Per instructions I stopped rather than opening Chrome tabs for a literature source.
- SearchCulture.gr (Greek aggregator) form needs a CSRF POST; two GET attempts returned the whole-collection count or HTTP 500.
  Not swept directly; only reached through Europeana.

## Not reached
Dubrovnik State Archives (Lettere di Levante, Secreta Rogatorum cipher keys), HDA Zagreb, Arhiv Srbije, Arhiv Jugoslavije, Slovenian
archives portal, GAK, Gennadius, Benaki, Filiki Eteria archive (Academy of Athens repo). Next step: a Chrome pass on
arhinet.arhiv.hr, the DADU finding aid and repo.academyofathens.gr, or a different network for the unresolved hosts. Ragusan
material abroad is better swept from the holders (HHStA Türkei I, ASVe, Simancas, Vatican), which other sweeps cover.
