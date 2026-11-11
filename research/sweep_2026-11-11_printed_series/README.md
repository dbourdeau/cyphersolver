# Printed series sweep, 11 Nov 2026 (cloud session)

Brief: `research/_nov11/BRIEF.md`. Area: the "Printed series" row of `research/COVERAGE.md` (Hardwicke State Papers,
Journals of the Continental Congress, Official Records of the War of the Rebellion, Calendar of Home Office Papers after
1775), then other printed editions that note cipher left undeciphered.

Output: `candidates.json`, **10 rows** (built by `build.py`): 4 with a complete `open` vetting block, 6 leads without one.
No key leads worth a `key_leads.json` (two notes below). Nothing outside this folder was edited.

## Result in one paragraph

The four series named in COVERAGE.md are closed with **no rows**: they print cipher resolved, or only note garbled
telegrams. The finds came from the second half of the brief: two German-language editions that were never searched,
Pribram's edition of Lisola's reports (Archiv für österreichische Geschichte 70, 1887) and the 23 volumes of *Urkunden und
Actenstücke zur Geschichte des Kurfürsten Friedrich Wilhelm von Brandenburg*. Both editors worked from the originals and say
where a leaf carries cipher with no decipherment.

## Rows

| # | Item | Shelfmark | Vetting |
|---|---|---|---|
| 1 | Lisola, Dankow, 3 Jun 1657 (Pribram LX): about 1.5 pages and two lines not deciphered | HHStA StAbt Polen I 69 | open |
| 2 | Lisola, Königsberg, 4 Sep 1657 (LXXV): 2.5 pages not deciphered | HHStA StAbt Polen I 70 | open |
| 3 | Lisola, Königsberg, 11 Sep 1657 (LXXVI): one page not deciphered | HHStA StAbt Polen I 70 | open |
| 4 | Lisola, Warsaw, 3 Mar 1656 (note to XXIX): whole report not deciphered | HHStA StAbt Polen I 66 | open |
| 5 | Lisola, Danzig, 6 Feb 1660 (CLX): one passage | HHStA StAbt Polen I 74 | lead (length unknown, no searches run) |
| 6 | Chr. von Brandt, London, 8/18 Oct 1666: relation almost all cipher, not deciphered (UA XII p. 637) | GStA PK I. HA Rep. 11 England | lead |
| 7 | Hoverbeck, Warsaw, 26 May 1662: "meist unaufgelöste Chiffern" (UA IX p. 352) | GStA PK I. HA Rep. 9 Polen | lead |
| 8 | Nassau and Weiman, London, 20 May 1661: "meist in unaufgelösten Chiffern" (UA IX) | GStA PK I. HA Rep. 11 England | lead |
| 9 | Fridag to Leopold I, Berlin, 17 Sep 1685: "längerer nicht dechiffrirter Passus" (UA XIV/2 p. 1186) | HHStA StAbt Brandenburgica | lead |
| 10 | Millet to Lionne, Berlin, 27 Jul and 24 Aug 1667: mostly not deciphered (UA II) | AAE CP Brandebourg 1667 | lead |

Caveats that the merge session should read:

- **Shelfmarks of rows 1-5 are at Karton level and assigned by date.** The AIS describes HHStA StAbt Polen I by Karton only
  (IDs 227463-227553, walked with `ais_walk.py`, log in `ais_polen.log`); Pribram cites "St.-A. (Pol.)" for this
  correspondence but gives no folio per report. The Königsberg reports (rows 2-3) could be filed in Brandenburgica, the
  Warsaw report of 1656 in Suecica. Each row says so in `verify`.
- **Rows 1-4 are `seen.kind` "not online".** `seen.cipher` quotes the editor's note, not an archive description, because no
  item-level archive description exists. If the gate wants the archive's own words, these four go back to leads.
- **The GStA rows (6-8) have no unit number**: the edition gives none and the GStA database was not searched. They carry no
  vetting block. Row 10's AAE volume number was not looked up; French incoming despatches were normally deciphered in the
  office, so a decipherment may sit in the volume.
- Lisola's sibling reports are printed with their cipher passages resolved (between asterisks), so the key is recoverable
  from the same Kartons once images exist. No key under his name on DECODE or in the AIS.

## The four named series (closed, no rows)

| Series | What was read | Result |
|---|---|---|
| Official Records, Armies | 119 Cornell volumes (`cu319240...`) and 69 `warofrebellion...rootrich` volumes, OCR downloaded and searched (`ex_note.py`, `ex_gib.py`). The two sets overlap; not every one of the 128 serials was confirmed present. | Three editor's notes only (below). Confederate and Union cipher telegrams are printed in clear. |
| Official Records, Navies | 111 of 114 listed copies (all 30 volumes several times over) | Ser. II vol. 3 prints Slidell's Paris despatches of 1863-64 with the Vigenère ciphertext in brackets **after the clear text** of each passage: read, and a ready-made plaintext/ciphertext pair set. No unread cipher. |
| Journals of the Continental Congress | all 34 volumes (`dl_jcc.py`; the text file name differs from the identifier) | No cipher note at all (one "undecipherable" is a struck-out word in a draft). |
| Hardwicke, Miscellaneous State Papers 1501-1726 | 9 copies of the 2 volumes | Cipher letters are printed deciphered; no note. |
| Calendar of Home Office Papers | The printed calendar stops at 1775 (4 volumes, 1760-1775; `ia_pass2_b` already read them). **There is no volume after 1775**, so that COVERAGE item is void. | none |
| Wharton, Revolutionary Diplomatic Correspondence | 23 of 36 listed copies, all six volumes at least once | One editor's note (Arthur Lee's dictionary cipher explanation, "now unintelligible": a key description, not ciphertext); the rest are the writers' own complaints (Adams on Lovell's cipher, Jay and Livingston on missing ciphers), covered by cryptiana `adams3.htm`. The series is catalogue 784 already. |

Official Records notes found, **not made rows** (no manuscript shelfmark established, and each is a word or a phrase):

- OR I/44 p. 869: R. E. Lee to Jefferson Davis, Petersburg, 19 Nov 1864, two gaps footnoted "Cipher unintelligible"
  ("nor do I know of a ...", "It would be extremely hazardous and ..."). Not in Freeman's *Lee's Dispatches* (opened), not
  on cryptiana's Civil War pages. The original telegram (Confederate War Department or Davis papers) was not located. Worth
  a NARA RG 109 look by whoever holds the `nara_*` notes: a garbled Vigenère fragment in a known keyword period.
- OR I/47/3 p. 791: Archer Anderson to Johnston or Davis, Raleigh, 12 Apr 1865: one word printed "g.t.l.r.t.y",
  "Unintelligible cipher word".
- OR I/48/1 p. 1370: Maj. W. F. Mastin's report on the District of Texas, Feb 1865: "An unintelligible cipher is here
  omitted" (the effective strength figure).

The other "cipher unintelligible" hits are the generals' own complaints about garbled telegrams (Polk 19 Feb 1864, Johnston
11 Apr 1865, Meade 3 Jul 1863), which Tomokiyo's `civilwar4.htm` already discusses.

## Other editions checked, no rows

- **Groen van Prinsterer, Archives de la maison d'Orange-Nassau**: 25 volumes downloaded (all five series). Only footnotes
  "chiffre inconnu / incertain / inlisible" on single names in Morillon's letters to Granvelle (1566-68), and Count Johann's
  letter of 21 Nov 1573, which the Supplement prints "déchiffré par un Hollandois" (Bezold's remark that it is "nicht
  dechiffrirt" is out of date).
- **Forst, Politische Correspondenz des Grafen Franz Wilhelm von Wartenberg 1621-31**: four notes "Chiffrirt, ohne
  Auflösung", each a name or a few words (St.-A. Osnabrück Abschn. 1 Nr. 43, the unit of catalogue 601). Not rows.
- **Landtagsakten von Jülich-Berg I**: one cipher group of 1540, resolved by the editor from Harst's alphabet.
- **Urkunden und Actenstücke**, single unresolved groups (not rows): UA I (two), UA V p. 21 Sept 1655 Johann Moritz ("für
  beide Chiffern waren die Schlüssel nicht aufzufinden"), UA VI, UA VII (Weiman, The Hague, Dec 1655: "mehrere chiffrirte
  Zeilen ohne Auflösung" and four unresolved name groups), UA IX pp. 330, 351 (Hoverbeck, several lines), UA XII (three),
  UA XV, UA XIX, UA XXIII/2. Weiman's lines of Dec 1655 and Hoverbeck's of 1662 belong with rows 7-8 if those units are
  ever ordered.
- **Calendar of the Papers of Benjamin Franklin (APS)**: "In untranslated cipher", VII 87: already a lead
  (`sweep_2026-11_us_blocked`).
- **Archiv des Vereins für Siebenbürgische Landeskunde 28**: "Unaufgelöste Chiffern; Auflösung vom Herausgeber": read.

## Routes

- archive.org from this network: `advancedsearch.php` (identifier discovery, `find.py`), `download/<id>/<id>_djvu.txt`
  (`dl.py`, `dl1.py`), `metadata/<id>/files`, and the full-text endpoint
  `services/search/beta/page_production/?service_backend=fts` (`fts.py`, `q.py`) all answer. About 1 volume per 20-60 s
  when two downloads run at once. No 429.
- archivinformationssystem.at: answers the `research/aut_hhsta/ais_search.py` session POST (`ais.py`) and plain
  `detail.aspx?ID=` GETs; slow (5-20 s a page).
- de-crypt.org `RecordsList?cmd=search` (`decode_search.py`, copied from `sweep_2026-11-11_german`): answers.
- cryptiana.web.fc2.com: answers over https (http gives a 302).
- Nothing was blocked. The container restarted once mid-run; scratch files survived, background jobs did not.

## Full-text phrase queries (`hits1.json`, `hits2.json`)

72 phrase queries, up to 3 pages of 50 (`q2.log` has the hit count per query). The endpoint ranks loosely and most hits are
novels, dictionaries and periodicals; the earlier sweeps had already taken the English, French, Spanish and Italian
phrases. The productive ones were all German: "unaufgelöste Chiffern" (4 hits), "chiffrirt" + "ohne Auflösung" (6),
"chiffrirt" + "nicht dechiffrirt" (7), "Chiffern" + "nicht aufgelöst" (89, one useful). Zero or noise: all Dutch,
Swedish, Danish, Portuguese phrases; "en cifra" + "sin descifrar" (30, literary); "in cifra" + "non decifrato" (18, the
Documenti diplomatici italiani 1908-14 "gruppo non decifrato" telegram notes, 20th-century single groups).

## Method for the series

`ex_note.py`: a cipher word within 160 characters of an "unread" phrase, over every downloaded volume. `ex_gib.py`: printed
ciphertext detector (runs of five or more tokens that occur at most twice in the whole corpus, or twelve or more number
groups, with a cipher word nearby); this is what found the Slidell passages and nothing else. `ex_de.py`, `ex_fr.py`:
readers for the German and French editions. Every row was read in context by hand.

## Not done

- The OR serial-by-serial completeness check.
- GStA database lookup for rows 6-8, AIS Brandenburgica Karton for row 9, AAE volume for row 10; web searches for rows 5-10.
- Other unsearched editions of the same kind, in the order I would take them: Pribram's other HHStA editions (Venetian
  despatches from Vienna, FRA II), Fiedler's Relationen, Hirsch/Meinardus Protokolle und Relationen des Brandenburgischen
  Geheimen Rathes, Briefe und Akten zur Geschichte des Dreissigjährigen Krieges, Erdmannsdörffer's UA volumes in the Google
  copies (only the Toronto set was read: vols 1-13, 14/1-2, 15, 16/1-2, 17-19, 21, 23/1-2; **20 and 22 are missing**).
- Rows 1-4 need the leaf from HHStA before anything else can be said about the cipher system.

## Files

`build.py` (rows), `candidates.json`; `find.py`, `ids*.json`, `ua_ids.txt`, `groen_ids.txt` (identifiers); `dl.py`, `dl1.py`,
`dl_jcc.py`, `dl*.log`; `fts.py`, `q.py`, `view.py`, `hits1.json`, `hits2.json`, `q2.log`; `ex_note.py`, `ex_gib.py`,
`ex_de.py`, `ex_fr.py`, `notes*.json`, `gib.json`; `ais.py`, `ais_walk.py`, `ais_polen.log`; `decode_search.py`.
OCR texts are in the session scratch directory only.
