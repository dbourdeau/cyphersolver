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
- **1206** Kerlérec, October 1755: `unvetted`. Pusch, *Louisiana History* 49 (2008), reconstructs Kerlérec's code and
  is behind a JSTOR login; Villiers du Terrage (1904) p. 71 already summarises the 9 October 1755 cipher despatch.
  Very probably read.
- **1207** Kerlérec, 1759-60: `unvetted`. Same Pusch question; ANOM C13A is microfilm only.
- **1299** Kerlérec, 1758-59: `unvetted`. The Ministère des Armées inventory does not answer this network either.
- **1257** Whitworth and Wich, 1712: `unvetted`. The two Rawl. C. 392 copies are Whitworth's despatches to St John of
  March to June 1712, and *Sbornik RIO* vol. 61 (1888; HathiTrust coo.31924112547348, full view) prints that series in
  English (No. 42 of 4/15 March to No. 54 of 8/19 June 1712 and on). The Rawl. A. 286 private letters to Bishop
  Robinson are not printed there and not digitised.
- **1300** Obregón, 1825: `unvetted`. Narváez's *Historia Mexicana* 231 article stays behind Cloudflare even in a normal
  browser; the despatches are in the SRE archive, not online.
- **1301** Torrens, 1826: `unvetted`. Narváez (*EHMCM* 38, 2009, p. 142) says notes 2 and 3 are wholly in Torrens's
  10 x 7 matrix cipher, whose key sheet survives and is printed there, and (*Documenta & Instrumenta* 6, 2008, n. 25)
  that several messages in this cipher are already printed. The cipher part is almost certainly read; the *Memorias*
  49 article and the notes themselves are not online.
- **1437** Sinclair-Zevely telegrams, 1916-24: `unvetted`. Portal to Texas History shows an "I'm not a robot" check.

Count: open 1, not_cipher 1, unvetted 8.

No lead in the online waiting list is a United States diplomatic document with free images (`vet.py --list --online`,
filtered on United States, Madison, Monroe, Jefferson, minister, envoy and the like): 1437 was taken as the tenth
instead.

## Routes and logins

| Route | Result from this network |
|---|---|
| Harvard (hollisarchives, nrs, mps IIIF) | works with curl and Chrome (it refused the cloud on 11 Nov) |
| gilderlehrman.org | Cloudflare passes in Chrome; item pages and 400 px previews are public, full scans need a Collection subscription |
| jstor.org | page-1 preview only; full text needs a login |
| historiamexicana.colmex.mx | Cloudflare check does not clear, curl 403 |
| moderna.historicas.unam.mx, revistas.ucm.es, redalyc.org | open PDFs, downloaded |
| babel.hathitrust.org | Cloudflare passes in Chrome; catalogue API works with curl |
| archives.bodleian.ox.ac.uk | Anubis proof-of-work page to curl; passes in Chrome |
| texashistory.unt.edu | "I'm not a robot" check, left for the contributor |
| bibliotheques-numeriques.defense.gouv.fr | no connection |
| de-crypt.org (DECODE), cryptiana.web.fc2.com, archive.org | work with curl |

## What is left

- 1285: TNA SP 94/205 (the received original of No. 35) and BL Add MS 24157-24179 (Grantham's papers) for a
  decipherment or a clear draft.
- 2051: full scans of GLC02414.229, .339, .341, .344 and .114 (Gilder Lehrman subscription or PDF order); then split.
- 1206, 1207, 1299: Pusch 2008 in full (JSTOR); the Ministère des Armées inventory from another network.
- 1257: Rawl. A. 286 ff. 60-153 (Bodleian reading room or a scan order).
- 1300, 1301: Narváez in *Historia Mexicana* 231 and *Memorias* 49 (library or interlibrary loan).
- 1437: the robot check on Portal to Texas History.
