# Vetting, ajbeling (13 Nov 2026)

Run by Andrew Beling (GitHub ajbeling) with AI agents: a Claude Code agent, model claude-opus-5-5, working from his
own computer and network, with his Chrome for pages behind Cloudflare. Ten leads, chosen for blockers his access might
lift. Before starting, open issues and pull requests were searched for each id and correspondent (`gh api search/issues`,
13 Nov 2026) and issue #542 was read: none of the ten is named. Leads 1136 and 1137 were left alone (another of our
sessions has them). `python research/vet.py --check research/vetting_2026-11-13_ajbeling/vetting.json` prints
`result: pass`.

## Leads

- **1285** Grantham (Aranjuez) to Weymouth, 18 June 1778, duplicate of No. 35: `open`. Harvard's IIIF images were
  opened at 2000 px: about 64 numeric code groups (120 to 3709) inside a clear despatch, nothing written between the
  lines. The lead's addressee is better given as Lord Viscount Weymouth (Thomas Thynne, later Marquess of Bath). The
  received original ("rec'd 6 July") should be in The National Archives SP 94/205 and may carry a decipherment; it was
  not seen.
- **2050** Ingalls to Nesmith, 12 Dec 1862: `not_cipher`. The "Union cipher letter" is Chinook Jargon in plain script
  ("nesika", "tum-tum", "tomolloh", "klahowya mika"). Read on the 400 px public preview; the hand is large and every
  word is legible, but a subscriber view of the full scan would confirm it.
- **2051** "Graham" telegrams to Scammon's command, 1-3 July 1863: `unvetted`. Real Union route cipher (plain words
  transposed, with code words and nulls), but only 400 px previews are free. GLC02414.114 in the same collection is the
  period decipherment of GLC02414.341 ("Graham" is Colonel Carr B. White, 12th Ohio, per the docket). No decipherment
  found for .229, .339 and .344. Suggest splitting the lead.
- **1206** Kerlérec, 9, 10 and 18 October 1755: `read`. Pusch, "Kerlérec's Cipher", *Louisiana History* 49 (2008)
  463-480, read in full after Andrew's JSTOR login (copy in `sources/raw/kerlerec_pusch_2026-11-13/`), decodes these
  three (his nos. 86, 87, 91) and corrects the ministry's readings of two of them. The ministry's own decipherment is
  written above every code line: seen on ANOM C13A 39 f. 60, which is digitised on the ANOM site.
- **1207** Kerlérec, 1759-60: `partly_read`. ANOM C13A 41 is digitised in full (302 images, 2150 x 3110 px). Nos. 194
  (10 Nov copy) and 228 (12 Jun 1760) have the ministry's plaintext; nos. 206 (3 Jul 1759, about 650 groups) and 215
  (17 Sep 1759, about 370 groups) are bare on the leaf and Pusch decoded them without printing the text. Pusch prints
  the code book (547 of 700 entries). The 1736 item in C13A 21 was not examined.
- **1299** Kerlérec, 1758-59: `unvetted`. The Ministère des Armées inventory still does not open, by curl or in Chrome.
  Pusch decodes the two ANOM cipher despatches of these dates (12/23 Aug 1758 and 6 May 1759); whether the inventory's
  items are copies of them is the open question.
- **1257** Whitworth and Wich, 1712: `unvetted`. The two Rawl. C. 392 copies are Whitworth's despatches to St John of
  March to June 1712, and *Sbornik RIO* vol. 61 (1888; HathiTrust coo.31924112547348, full view) prints that series in
  English (No. 42 of 4/15 March to No. 54 of 8/19 June 1712 and on). The Rawl. A. 286 private letters to Bishop
  Robinson are not printed there and not digitised.
- **1300** Obregón, 1825: `read`. Narváez, *Historia Mexicana* 231 (2009) 1093-1153, read in full once Andrew cleared
  Cloudflare: the ministry decoded Obregón's coded despatches on receipt (printed by Chávez Orozco 1930 and in *México
  y Cuba* 1982); the only two left undecoded, reserved nos. 3 and 14 of 1825, Narváez decodes and prints in full, with
  the code book (figure 5). The despatches are in the SRE archive, not online.
- **1301** Torrens, 1826: `unvetted`. Narváez (*EHMCM* 38, 2009, p. 142) says notes 2 and 3 are wholly in Torrens's
  10 x 7 matrix cipher, whose key sheet survives and is printed there, and (*Documenta & Instrumenta* 6, 2008, n. 25)
  that several messages in this cipher are already printed. The cipher part is almost certainly read; the *Memorias*
  49 article and the notes themselves are not online. *Historia Mexicana* 231 adds (n. 52) that *Memorias* 49 holds a
  "precarious" decoding of a code manuscript presumed Torrens's, and (p. 1133) that Torrens's and Obregón's codes look
  like versions of one book.
- **1437** Sinclair-Zevely telegrams, 1916-24: `open`. Andrew cleared the robot check; all nine items the Portal tags
  "telegraphic commercial code" were seen at 1800 px. Only three carry code (metapth1891750, 29 Apr 1922; 1891738,
  1 Oct 1923; 1891736, 21 Jan 1924); 1891648 has two code names glossed in pencil; five are plain English. No
  decoding on the leaves, in three volumes of the 1923-24 Senate oil-lease hearings, or in print. The 1923-24 code
  words come from the 1901 Berne official vocabulary, so the book is not identified. The catalogue entry should be
  narrowed to the three coded telegrams.

Count: open 2, read 2, partly_read 1, not_cipher 1, unvetted 4.

### Second pass, 13 Nov 2026 (late evening)

Andrew cleared the JSTOR login, the Historia Mexicana Cloudflare check and the Portal to Texas History robot check in
his Chrome; this pass reread 1206, 1207, 1299, 1300, 1301 and 1437 and replaced their blocks. Each replaced block says
so in `supersedes`.

No lead in the online waiting list is a United States diplomatic document with free images (`vet.py --list --online`,
filtered on United States, Madison, Monroe, Jefferson, minister, envoy and the like): 1437 was taken as the tenth
instead.

## Routes and logins

| Route | Result from this network |
|---|---|
| Harvard (hollisarchives, nrs, mps IIIF) | works with curl and Chrome (it refused the cloud on 11 Nov) |
| gilderlehrman.org | Cloudflare passes in Chrome; item pages and 400 px previews are public, full scans need a Collection subscription |
| jstor.org | through the University of Maryland proxy after Andrew's login: full PDF |
| historiamexicana.colmex.mx | curl 403; in Chrome after Andrew cleared Cloudflare, the PDF viewer's text was read |
| recherche-anom.culture.gouv.fr | COL C13 A 39, 41 and 42 are digitised; page images open with curl from the IIP server |
| moderna.historicas.unam.mx, revistas.ucm.es, redalyc.org | open PDFs, downloaded |
| babel.hathitrust.org | Cloudflare passes in Chrome; catalogue API works with curl |
| archives.bodleian.ox.ac.uk | Anubis proof-of-work page to curl; passes in Chrome |
| texashistory.unt.edu | after Andrew cleared the robot check in Chrome: item pages, IIIF manifests and images |
| bibliotheques-numeriques.defense.gouv.fr | no connection, curl or Chrome |
| de-crypt.org (DECODE), cryptiana.web.fc2.com, archive.org | work with curl |

## What is left

- 1285: TNA SP 94/205 (the received original of No. 35) and BL Add MS 24157-24179 (Grantham's papers) for a
  decipherment or a clear draft.
- 2051: full scans of GLC02414.229, .339, .341, .344 and .114 (Gilder Lehrman subscription or PDF order); then split.
- 1207: Kerlérec nos. 206 and 215 (and the coded passage of no. 207 on C13A 41 f. 97) can be read with Pusch's
  printed code book from the ANOM images; the C13A 21 item of 1736 is unexamined.
- 1299: the Ministère des Armées inventory from another network.
- 1257: Rawl. A. 286 ff. 60-153 (Bodleian reading room or a scan order).
- 1301: Narváez in *Memorias* 49 (library or interlibrary loan).
- 1437: the remaining volumes of the Senate oil-lease hearings, and the code book behind the three coded telegrams.
