# jablonski1705: Daniel Ernst Jablonski to Pál Ráday, enciphering drafts 1705 and 1706-07 (SBB Berlin, Nachl. Francke 11,2/15 and 11,2/16), key of the numeric syllabary

Status: read (the drafts carry their own Latin plaintext under the numbers); key rebuilt from the figure/plaintext pairs and validated on a held-out draft (Brice Dudout, 10 Nov 2026; 0.930 of characters vs 0.247 for the best shuffled key). Our role is the key and its verification, not a solution.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Leads 2169 and 2170, found in Daniel Bourdeau's
Staatsbibliothek zu Berlin (Kalliope) sweep of 3 Nov 2026 (leads 2168-2171) and vetted in leads review batch c26 (4 Nov 2026),
which marked both "read": these are enciphering drafts, clear Latin with the red number groups written above it, so "a table
could be built from the number-over-word pairs, but this was not done". This target supplies that table.

## Documents

Staatsbibliothek zu Berlin - Preußischer Kulturbesitz, Nachlass August Hermann Francke, Jablonski's letter-draft books
(Digitalisierte Sammlungen, licence in the METS: Public Domain Mark 1.0). No images are included here (CONTRIBUTING: images
stay out of git); they are public at the links below. Credit: "Staatsbibliothek zu Berlin - PK, Nachl. Francke 11,2/15"
(resp. 11,2/16), PDM 1.0.

| draft | date | SBB scans | role here |
|---|---|---|---|
| 11,2/15 no 8 (lead 2169) | 13 Mar 1705 | PPN1853543950, 23-24 (25 has no figures) | training pairs |
| 11,2/15 no 13 (lead 2169) | 18 Apr 1705 | PPN1853543950, 37-39 | training pairs |
| 11,2/15 no 33 (lead 2169) | 11 Sep 1705 | PPN1853543950, 71-72 | training pairs; two unglossed runs (see below) |
| 11,2/16 no 42 (lead 2170) | 7 Dec 1706 | PPN1853544159, 86-87 | training pairs |
| 11,2/16 no 44 (lead 2170) | 14 Feb 1707 | PPN1853544159, 91-92 | held out: all 541 groups, measured once |

Viewer: https://digital.staatsbibliothek-berlin.de/werkansicht?PPN=PPN1853543950 and ?PPN=PPN1853544159.

## System and key (`key.tsv`, CC BY 4.0)

A one-part numeric syllabary in alphabetical order, the same in 1705 and in 1706-07 (the "R I" of the Kalliope record for no 42
is not a second cipher):
- single letters with homophones, 30-70 (30 a, 31 b, 32 c, 33 d, 34 e, 35 a ... 64 t ... 70 u), plus round numbers 110 u,
  120 t, 130 s, 140 r, 160 p, 180 n, 190 m, 210 l, 220 i, 250 f, 260 e, 270 d, 280 c, 290 b, 300 a;
- syllables VC/CV in alphabetical order, 84 ab, 85 ac, 86 ad ... 97 ba, 98 be ... 185 qua ... 201 ta ... 223 ut;
- code words 225 imperator/Caesar, 226 Hungaria, 227 Prussia, 228 Polonia, 229 Suecia, 231 Anglia, 232 and 237 Gallia,
  233 Hispania, 234 Italia, 236 Elector, 241 Rex;
- nulls below 30 and 301-310, 390, 401.

Built from 350 figure/plaintext pairs (1,368 groups, `pairs.tsv`) by an iterated segmentation (`frozen/scripts/solve_key.py`)
then hand corrections along the alphabetical order (`frozen/scripts/make_key.py`), frozen as `frozen/03_KEY.json`. 213 groups:
146 sure (seen twice or more), 38 probable (seen once), 29 nulls. 171 and 278 are unresolved and left out.

## Validation (`validation.txt`, `frozen/`)

Pre-registered (`frozen/01_PREREG.md`, frozen before any view of the portion). Portion: every numeric group on scans 91-92 of
11,2/16 (no 44, 14 Feb 1707), letter body and P.S. The groups were transcribed blind from red-ink-only renderings (the Latin
under them masked), 541 groups; decoded with the frozen key; only then the Latin under the groups was read. One measurement:
**0.930 of characters** (958 decoded / 952 reference letters) against **0.247** for the best of 200 shuffled keys (mean 0.198),
margin 0.683; thresholds >= 0.85 and margin >= 0.30 fixed in advance: **validated**. Hashes of every step in `frozen/HASHES.txt`.
The portion is burnt; the key was not changed after the measurement.

Declared: the measuring script folds w->u and y->i besides the j->i, v->u that the protocol names. 9 groups decoded as "?"
(2 illegible, 7 outside the frozen key: 215, 15, 61, 178, 113, 53, 40) count as wrong.

Main differences: 225 gives "imperator" where the draft says "Caesar" (the code word serves both); 232 "gallia" for
Gallos/Galliae; 208.153 "uile" for "vina" (a clerk's slip, or 153/163); a few one-letter slips (paax, grandm, exse).

## Texts

`transcription.txt` = the 541 held-out groups (blind transcription, frozen copy `frozen/04_TRANSCRIPTION.txt`);
`decryption.txt` = our decode, word-divided, line by line beside the Latin of the draft; `reading.md` = the decode read as
sentences; `translation.md` = English. Count on the measured portion (Daniel's form): 541 groups; 532 decoded; 9 holes
(2 illegible, 7 outside the key), in 8 of about 176 words; 0 restored; read_share 0.955. The content is Jablonski's own Latin:
Ilgen's message in the King of Prussia's name that the Hungarians should make peace with the Emperor before the
Franco-Imperial peace, and a postscript on two casks of noble wine (from Ráday) passed on to the King and on sending more via Cracow or
Breslau.

## Open: the two "ex aliena Cifra" runs (scan 72)

On 11,2/15 no 33 (scan 72) Jablonski quotes two number runs from Ráday's incoming letter, unglossed, saying they seem to come
from another cipher ("ex aliena Cifra"):
`204.155.275.30.147.111.18.213.8.205.7` and `95.137.112.15.48.137.12.178.144.187.16.90.85.45` (25 groups).
They do **not** read with this key ("tolo?aipdo...", "athedu?ohe..."), which bears out Jablonski's remark. **Unresolved**;
not to be read with `key.tsv`. They may belong to Ráday's own key to Jablonski (Benda, Levéltári Közlemények 25, 1954, mentions a
clavis for the Jablonski correspondence in the Ráday archive; not seen).

Also not glossed: the two red heading lines of scan 23 (no 8), `310.144.156.130.120.193.63.28 / 27.111.29.159.164.302`, which
read "illustris domine" with the key (an enciphered address). Outside the measured portion, not tested.

## Verification against the received letter of 3 Aug 1705

Wikimedia Commons, "File:Partially encrypted letter 1705-08-03.jpg" (Jablonski -> Ráday, the letter as received, with Ráday's
glosses; scan by user Szilas from Révay 1974): its groups and Ráday's glosses agree with this key (191 ra, 208 vi, 203 ti, 170 o,
98.210.155.131.45.154.105 "bello gallico", 93.161.195.46 "armorum", 160.62.146.104.181.63 "principes"). Checked, not measured;
the letter is glossed and printed, so this is a verification only.

## Prior work

- The plaintext is on the leaves (Jablonski's own Latin under the numbers): credited `contemporary`, prior solution.
- Daniel Bourdeau, leads 2169/2170 (sweep 3 Nov 2026; review c26, 4 Nov 2026): verdict "read", key not built.
- **Révay Zoltán, *II. Rákóczi Ferenc és korának rejtjelezése (XVIII. század)*, Budapest: Magyar Néphadsereg Híradó Főnökség (MNHF),
  1974.** The Commons scan of the 3 Aug 1705 letter comes from this book, so Révay reproduces that letter (and is said to transcribe it; not checked).
  We searched (10 Nov 2026) for its contents: bibliographic records (Cryptologia reference lists; hu.wikipedia "Kuruc titkosírás",
  which cites it without page numbers and reproduces no key; Vámos & Vadai's critique of Révay on the Pázmány and Rákóczi I ciphers),
  the Commons file page (no statement on a key), and open full texts. **No open text, preview or table of contents was found**, so
  we could not check whether Révay prints the Jablonski-Ráday key. If he does, the key is his and our part is the verification
  (an independent rebuild from the Berlin drafts and the held-out test); we ask that the credit be adjusted then. Láng's open-access
  *Real Life Cryptology* (2018) covers the 16th-17th centuries; its PDF could not be fetched (connection reset), not checked.
- Benda, Levéltári Közlemények 25 (1954), cited in review c26: a clavis for the Jablonski correspondence in the Ráday archive
  (Budapest). Not seen; if it survives, it is the original key and this table a rebuild.
- In this repository: `targets/rakoczi1711` names "domino Jablonski" in R483, but R483's syllabic key (`R483_key_rebuilt.json`) is a
  different system: of 81 groups valued in both keys, 2 agree (160, 280). `rakoczi1704`/`rakoczi1707` (Rákóczi's French letters,
  key R639) are other systems too. No target, branch or PR on these drafts (GitHub, 10 Nov 2026). Not on DECODE (review c26).

## Related leads

- 2168 (11,2/14 nos 62, 71, 75; 1704): no 75 is partly in cipher; the 1704 numbers run lower than the 1705 ones (review c26), so
  the 1704 system may differ. Not compared here (scans not harvested: the SBB server answered HTTP 429, not retried).
- 2171 (11,2/17 no 91; 1712, Jablonski -> Rákóczi): a different system; not part of this target.

## Limits

- One reader (an agent), on the SBB "max" images; no human palaeographic check.
- 38 values seen once (probable); 171, 278 unresolved; groups 15, 40, 53, 61, 113, 178, 215 not in the table.
- The other drafts of 11,2/15-16 were not swept for further cipher.

## Remaining gaps

- the two "ex aliena Cifra" runs on 11,2/15 no 33, scan 72 (25 groups) - blocker: no-key-material; they do not read with this key, and Ráday's own key (the clavis in the Ráday archive, Benda 1954) has not been seen
- groups 171 and 278 unresolved; 15, 40, 53, 61, 113, 178, 215 not in the table; 38 values seen once - blocker: too-short; each occurs too rarely in the drafts to fix a value
- Révay 1974, whether it prints this key - blocker: needs-physical-access; no open text, preview or table of contents found (10 Nov 2026)

Out of scope (not gaps of this key): lead 2168 (the 1704 drafts, numbers in a lower range, perhaps another system) and lead 2171
(1712, a different system) are their own leads; the other drafts of 11,2/15-16 were not swept for further cipher. One reader (an
agent), no human palaeographic check (Limits).

## Escalation

- [x] siblings: all five cipher drafts of 11,2/15-16 used (four for training, one held out); the received letter of 3 Aug 1705 (Commons) checked against the key
- [x] clear-pages: the drafts are their own clear text (Latin under the numbers)
- [x] known-keys: R483's rebuilt key (rakoczi1711) and R639 (rakoczi1704/1707) compared; different systems (2 of 81 shared groups agree)
- [x] print: Révay 1974, hu.wikipedia "Kuruc titkosírás", Vámos & Vadai, Láng 2018 searched; no printed key found open
- [x] key-rebuild: iterated segmentation over 350 pairs plus hand corrections along the alphabetical order (213 groups)
- [x] retry: the scan-72 runs and the scan-23 heading run decoded with the frozen key; the heading reads "illustris domine", the scan-72 runs do not read
- [x] integration check (11 Nov 2026, PR #385): measure.py re-run on the frozen files gives 0.9296 vs 0.2468 (PASS), and all seven SHA-256 hashes in frozen/HASHES.txt match
