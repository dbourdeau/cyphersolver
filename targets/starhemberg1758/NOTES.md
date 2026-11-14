# Georg Adam Starhemberg (Paris) to the Austrian envoy at Madrid [Rosenberg?], 23 May 1758: NOTES

Status: in progress. Read in part by a contributor (GitHub issue #555, aaymeloglu), strict 170/188 words = 90.4 %, with the
1752 Austrian Prima/Secunda tables (DECODE R1695/R1698). The key tables and the five digits added from the manuscript
photographs were not checked here (DECODE login; photographs not shareable), so the folder has no page yet.

## The document

A letter of Georg Adam, Count Starhemberg, imperial ambassador at Paris, dated "Paris den 23ten May 1758". German, with a clear
opening and closing and a numeric cipher passage between them. Satoshi Tomokiyo published it on Cryptiana ("Adam Starhemberg
(1758)", https://cryptiana.web.fc2.com/code/variable2.htm#Starhemberg, listed "Non-decrypted, German"). He had the image from
Alexandre Pillon and transcribed 1,721 digits. Tomokiyo noted that the figures are written without break, that 310-314 are very
frequent and look like groups of three, and that some digits may be missing at the right edge of his image. No archive shelfmark is known
(Pillon's collection). The address does not name the recipient. The contributor's reading is addressed to the envoy at
Madrid, which fits Count Rosenberg; that identification rests on context only.

Not in catalogue.json or research/leads.json; catalogue.json mentions the item only in passing (the Palm 1727 entry: "only an
unsolved Adam Starhemberg 1758"). Not the key of targets/starhemberg1721 (the Riva letters, 1720-27). No other target uses
the 1752 tables (R1695-R1698). One key, one entry: a new folder.

## 14 Nov 2026: issue #555 (aaymeloglu), integration check

Claim (issue #555; the contributor's public repository aaymeloglu/unsolved-ciphers, folder starhemberg-1758, CC0). Copied into
`aaymeloglu/`: `manuscript-lines.json` (transcription), `manuscript-tokens.json` (graded parse), `alignment.tsv`,
`emendations.json`, `emended-tokens.json`, `key-evidence.json`, `working-prima-v4.tsv` and `working-secunda.tsv` (their excerpt
of the 1752 tables), `source-transcription.txt` (their copy of Tomokiyo's), and the edition as `edition.md` (German and English).
Their notes are in `NOTES_aaymeloglu.md`.
- Key: the surviving 1752 Austrian Clavis Prima / Secunda (DECODE R1695 and R1698, with the instructions and worked
  examples R1696/R1697), applied as it stands. There are two tables: 2-digit and 5-digit (31xxx) units, with switch and control units. No
  language model was used. Secunda 31183 is Farinelli in the key's proper-name section.
- Transcription: Tomokiyo's 1,721 digits plus five digits at line ends from the manuscript photographs. Tomokiyo sent the photographs to the
  contributor on 21 Sept 2026 with Pillon's permission. They are not redistributable, and the contributor asks that Pillon be approached
  for them.
- Parse: 413 units, 398 from the key, 12 uncertain, 3 inferred. Emended: 404 units, 378 / 8 / 18. Eleven conjectural digit repairs,
  four contextual readings of 99 as g, 883 at start and end read as framing, a defective 119 at the recto/verso join.
- Reading: Starhemberg praises the memorandum handed to Wall and hopes Spain can be brought into the war or towards an
  honourable peace. He reads the closely agreeing statements of Farinelli (to the recipient) and of Wall (to the French ambassador) as a sign
  that ceding Minorca would bring Spain in against England and Prussia. He tells the recipient to keep working on Wall while he
  waits for the courier Zinner. German and English in `aaymeloglu/edition.md`.
- The contributor's words: "Small local doubts, no unread passages". "Not a claim of first decipherment." Tools: OpenAI Codex.

Checked here:
- Transcription against Tomokiyo's: his page was fetched today. His digits (1,721) and the contributor's (1,726) differ only by
  three insertions at line ends, of 1, 2 and 2 digits (difflib), as the contributor says. The five digits themselves rest on the photographs: **not checked**.
- Own script `own_check.py`. The 413 units concatenate to the 1,726-digit stream exactly. 389 ordinary/null units agree with
  the contributor's tables. 14 do not, all documented by the contributor: secunda 8 (null, 8 times), 50 die, 31133 l/ll, prima 28 (marked
  uncertain), 31183 Farinelli (from the name section, not the syllable value "no"), and 31010/31126 "gege" (a handwritten longer
  variant, key-evidence.json).
- The key tables themselves against DECODE R1695/R1698: **not checked** (images need a login; none in this session).
- Strict count over the German of the encrypted passage in `edition.md`: 188 words, 18 holes = 90.4 %, read in part. Holes:
  [stattlich?], Hoffnun[g] (twice), [es], Stat[s]secretario, vor[sich]ti[g], [bis zu] (2), erspr[ieß]lichen, the defective 119,
  [bereit?], un[d], [en]tschließen, [engländischen], setz[en], Ver[langen?], Be[s]eres, [g]schicktes. The contributor gives no
  percentage.
- Prior art: Tomokiyo lists it as not deciphered; one web search (14 Nov 2026) found nothing. Pillon contributes to this
  repository and may know more.
- Outcome: read after matching with key from external sources (the 1752 tables), by the contributor (provenance contributed).

## Remaining gaps
- The five digits added from the photographs and the eleven digit repairs: - blocker: needs-physical-access; the photographs are Pillon's
  and not shareable. Ask Pillon (or Tomokiyo) for a check, as the contributor suggests.
- The 1752 key tables as transcribed by the contributor (handwritten alternatives: stat?, bereit?, Verlangen?, gege): - blocker: not-attempted;
  check on DECODE R1695/R1698 with a login, which is workable.
- The defective 119 at the recto/verso join: - blocker: illegible; a writer's error, no second copy known.

## Escalation
- [ ] siblings: other Starhemberg-Madrid letters of 1757-58 in the 1752 key (HHStA Staatskanzlei; not searched).
- [x] clear-pages: the clear opening and closing are read (contributor).
- [x] known-keys: the 1752 Prima/Secunda tables (contributor).
- [ ] print: the Starhemberg-Kaunitz-Madrid correspondence of 1758 in print (not searched here).
- [ ] retry: check the tables on DECODE and the photographs with Pillon, then recount.
