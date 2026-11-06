# Ludwig von Ompteda to Count Münster, Berlin, 24 July 1811: the "undeciphered" part is in print since 1869

Status: no write-up (contents printed in 1869 from Ompteda's papers; nothing added here beyond locating the print
and checking it against the cipher. Outcome method: read from existing decipherment. Catalogue 2012 removed 6 Nov 2026 as
found in print.)

Catalogue 2012 (class A): "Count Münster's papers on the war between Russia and France ... part ciphered and part
never deciphered", NLA Hannover, Dep. 110 A Nr. 111 (Archiv Derneburg), 277 images.
Arcinsys record: https://www.arcinsys.niedersachsen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=3411488
Images: `https://arcinsys-digitalisate.niedersachsen.de/nla_ha/dep._110/a_nr._111/m_ha_dep._110_a_nr._111_aufn_NNNN.jpg`
(curl works; all 277 downloaded to `images/`, git-ignored).

## What the volume holds (all 277 images surveyed, 5-6 Nov 2026)

| aufn | folios | what | cipher state |
|---|---|---|---|
| 0001-0079 | 1-76 | Münster's drafts to Ompteda (Berlin) and others, 1811, several marked "in Chiffre"; English extracts | clear drafts |
| 0080-0150 | 77-133 | Dörnberg's German letters, Kolberg and St Petersburg 1812; *The Times* cuttings; reports | clear |
| **0151 R** | **134** | **"B. den 24 Juli 1811", sheet "1."**: undivided 4-digit code, German decipherment between the lines | deciphered at the time |
| **0152-0165 L, 0166, 0167** | **134v-147, 148v-150** | sheets II ff.: undivided digits, nothing written over them (about 27 pages, ~26,000 digits) | **the "nicht dechiffriert" part** |
| **0165 R** | **148** | "B. den 24ten Juli 1811", the P.S.: same code, German between the lines | deciphered at the time |
| 0168-0172 | 151-155 | "Vienne 15 Juin": 3-digit code with French between the lines | deciphered |
| 0173-0205 | 156-184 | French reports from Göteborg/Sweden, 1812 (e.g. "No 14", 25 Apr 1812, f. 177 = aufn_0198): 4-digit groups marked off with dots, French between every line | deciphered |
| 0206-0276 | 185-250 | German and French clear letters and memoranda, 1812-13 | clear |

So the only numeric text in the volume without a decipherment is the run ff. 134v-150. The catalogue's ff. 141-143
(aufn_0158-0160) lie inside it.

## The cipher

Ompteda says it himself on f. 134 (deciphered line 8-10): he has no French cipher, "sondern nur den deutschen Chiffre
von 1790 ... dessen ich mich auch jetzt bedienen muß". A 4-digit code written as one unbroken stream, wrapped across
lines without regard to groups; the 1811 decipherer put dots under some group boundaries. Groups are counted from
the start of the letter (verified: "Graf Hardenberg" = 2656 2964 on f. 134 lines 3 and 4, both at group
boundaries once the running digit count is carried over the line breaks). Two-part (not alphabetical) code with
homophones: den 3178, der 1697, König 3900, Graf 2656, Hardenberg 2964, "von" with at least two values.

## Prior art: the full text is printed

*Politischer Nachlaß des hannoverschen Staats- und Cabinets-Ministers Ludwig von Ompteda aus den Jahren 1804 bis
1813*, ed. F. von Ompteda, vol. 2 (Jena 1869), Dritter Abschnitt 1811:

- **No. 21, "Ompteda an Münster, Berlin, den 24. July 1811"**, pp. 51-59 (about 3,360 words): opens "Euer Excellenz
  sehr geehrtes Schreiben vom 27. März erhielt ich in Dresden erst am 22. Juny mit einer sichern Gelegenheit durch
  den Grafen Hardenberg", word for word the interlinear of f. 134, and goes on through the meeting with the Duke of
  Mecklenburg-Strelitz at Potsdam and the secret talks with the Prussian chancellor Hardenberg.
- **No. 22, the P.S. of the same day**, pp. 59-60 (about 410 words): "Meiner gehorsamsten Anzeige zufolge, hatte
  meine Reise nach Potsdam hauptsächlich zur Absicht ...", the interlinear of f. 148. It ends: the courier will not
  wait, so the rest follows by another occasion with a duplicate of the whole report.

Copy: archive.org `11005674bsb` (BSB scan), https://archive.org/details/11005674bsb ; OCR of both pieces in
`texts/ompteda_nachlass2_1869_nr21-22_ocr.txt` (public domain, raw OCR with long-s errors).

The edition printed Ompteda's own text, not a decipherment of these sheets, but it is the plaintext of this cipher:
the report's length (3,770 words for ~6,500 groups, about the f. 134 ratio of 1.6 groups a word plus spelled names
and numbers) and its words fit the sheets. Checked on the first undeciphered page (aufn_0152 L, f. 134v, which
continues the f. 134 sentence "um mich bei demselben des mir ertheilten Auftrages zu entledigen ..."): line 5 reads
4440 3761 2961 **3061 3178** 3519 4554 **1697 3900** 2591 5930 ... at group boundaries, i.e. "durch den Herzog,
den der König von Preußen" (print p. 51), with 3061 3178 = "durch den" and 3900 = König as on f. 134; line 14 has
2964 (Hardenberg) at a boundary where the print has "Staatskanzler von Hardenberg". Not checked further.

The 1811 decipherer of f. 134 wrote "Julii" where the print has "Juny" (22 June) and the heading "B." = Berlin,
not Dresden.

## Remaining gaps

None in the contents: the whole report and P.S. are in print. What was not done here:
- the undeciphered sheets were not transcribed beyond aufn_0152 L (`transcription/aufn_0152_L.txt`, 17 lines,
  893 digits, by a transcription agent, unchecked);
- f. 134 transcribed in draft (`transcription/f134_digits_draft.txt`, 907 digits); the running count is off by one
  digit somewhere in lines 9-16 (line 17's dots put it on a group boundary, the count does not), not yet found;
- the 1790 codebook was not rebuilt. It could be, by aligning the ~6,500 groups with the printed text ("key from
  external plaintext"), which would also show whether the 1869 editor abridged the report.

## Escalation

Not needed for the contents (printed). If the code itself is wanted: transcribe aufn_0152-0167, align each sheet with
pp. 51-60 of the print, collect the code table, and look for the "deutscher Chiffre von 1790" itself in the Hanoverian
chancery files (NLA HA Hann. 92 / Cal. Br.; Ompteda's Dresden reports are Hann. 92 Nr. 1349).

## Open

- Catalogue 2012 removed from `catalogue.json` on 6 Nov 2026 (record kept in
  `research/vetting_2026-10/removed_2026-11-02.json`, verdict read; listed in SOLVED_CATALOGUE.md section 4).
- Not on DECODE (no hit on 10,106 records); a new-record proposal is in `decode_updates/queue.json` (skip entry,
  as for labbe1582).
