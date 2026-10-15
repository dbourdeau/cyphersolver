# Archbishop of Bremen to Johan Adler Salvius, 1631 (Riksarkivet, DECODE R4330-R4331; from catalogue #207)

Outcome (21 Sept 2026): **key recovered from the interlinear glosses (adjacent plaintext); both letters deciphered in
full.** Write-up: docs/riksarkivet1628.html.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). Until then this folder was the whole of
catalogue entry 207, which bundled 14 DECODE records from Riksarkivet Stockholm under "Unknown sender → unknown
recipient, Stockholm, Latin, 1628–1646". Viewed here on 21 Sept 2026 they are four unrelated groups in different
ciphers. This entry now keeps only the Bremen letters (R4330, R4331) and their band key. The others are different
ciphers, each with its own page:

- R4282 (låda II:113, Latin letter cipher): deciphered by George Lasry with CTTS, entry
  [`targets/decode4282/`](../decode4282/NOTES.md). This folder's own attempt of 21 Sept 2026 (blind annealing, failed)
  is kept as history in `r4282_transcription.txt` and `r4282_codes.txt`; decode4282 is the canonical entry.
- R4284 (låda II:114, Latin numbers, 1628): [`targets/riksarkivet4284/`](../riksarkivet4284/NOTES.md), attempted, open.
- R4306 (låda II:133, to Amsterdam, 1632?): [`targets/riksarkivet4306/`](../riksarkivet4306/NOTES.md), attempted, open.
- R4333-R4337 (Rusdorff → Oxenstierna 1628): [`targets/rusdorff1628/`](../rusdorff1628/NOTES.md), surveyed only.
- R4338-R4341 (E 708, June 1633): [`targets/oxenstierna1633/`](../oxenstierna1633/NOTES.md), surveyed only.

The survey table of 21 Sept 2026 (the state column is as of that day; R4282 has since been deciphered by Lasry):

| records | what it is | system | state |
|---|---|---|---|
| R4282 (Chifferklaver låda II:113) | Latin letter, ~2 pp., sender/recipient not given | letter cipher of ~40 signs (Latin letters, digits 3 4 5 7 8, λ Δ φ ε α ⊡), with Latin words in clear | open |
| R4284 (låda II:114) | Latin letter, 1628, archival note "Legat … till L. Camerarius bref för 1628" | homophonic numbers (108 values) with Latin words in clear; plus a key-test leaf (effusorem sanguinis / pestem patriae / praeter naturalem / disturbatorem religionis) | open |
| R4306 (låda II:133, wrapper II:104) | letter to "Mr ?ilick" in Amsterdam, "1632?" | numbers 5–203, colon-separated; IoC 0.078 | open |
| R4330–R4331 | Johann Friedrich, archbishop of Bremen, to Johan Adler Salvius at Hamburg (not Åke Tott), 27 Nov. and 2? Dec. 1631 (German) | two-digit numbers inside clear German: homophonic, four consecutive numbers per letter; one-/two-number nomenclator (4 = wir, 5 = H. Christian, 7 = H. Georg, 32 = Bistum Minden, 59 = Salvius) | **read** (≈80% glossed at the time; all groups read here) |
| R4333–R4337 | J. J. von Rusdorff to Axel Oxenstierna, The Hague 1628 (German/Latin) | two- and three-digit numbers inside clear text; archive: "in many cases annotated as unsolved cipher" | open |
| R4338–R4341 (Oxenstiernska saml. E 708) | Swedish letters to Oxenstierna, June 1633 (DECODE's 1646 is wrong; the leaves are dated 8/18 and 27 June 1633) | two-digit letter code, four-digit nomenclator (1564, 3143, 3319 …) and letter-pair codes (rr, mm, aa, tt); interlinear decipherments at the time on some groups | read in part at the time |

## Images and access
`decode/` (git-ignored, not in this checkout) held the record pages and images (DECODE public records; cookie from
`targets/bordeaux/decode/cookie.txt`). The Bremen letters are DECODE phone photographs, 2448 x 3264.

`solve_num.py` and `qg.py` (the numeric annealer used on R4284 and R4306) stay here as shared tooling for those two
entries; `mk_validation.py` writes the Bremen `validation.tsv`.

## Bremen 1631 (R4330, R4331): read
Transcribed with the interlinear glosses (`bremen_transcription.txt`). Aligning glossed words to their numbers gave a
band key: each letter has four consecutive numbers, the bands in a scrambled order:

8–11 a · 12–15 g · 16–19 n · 20–23 t · 24–27 b · 28–31 h · 32–35 o · 36–39 u · 40–43 c · 44–47 i · 48–51 p ·
52–55 w · 56–59 d · 60–63 k · 64–67 [q] · 68–71 [x] · 72–75 e · 76–79 l · 80–83 r · 84–87 y · 88–91 f · 92–95 m ·
96–99 s · 100–103 z.

The band order is the alphabet written in a six-column grid (a b c d e f / g h i k l m / n o p q r s / t u w x y z)
and read down the columns; that places the unseen q and x and makes 84–87 y (weyter, Reuterey).

k, z, m, w and y were not glossed; they were fixed from the unglossed groups (sinken, schantze,
kommen / dem accord mitbegriffen / umbgriffen, etwas / wir / westphälisch, weiter / Reuterei). Every group then reads
(`bremen_decoded.txt`); the residue is transcription slips (e.g. `occupireh`, `feldlsihen`).

Content: the archbishop (Johann Friedrich of Holstein-Gottorp) presses Salvius, Swedish resident at Hamburg, for
Swedish succour — foot, dragoons, "etliche tausend" — against the imperial/League troops of Gronsfeld and
Bönninghausen in Westphalia; his men have taken the Burg and are attacking the schantze; he fears the enemy will
ravage the Lüneburg country and asks that the Stift be included in the accord if the Neuenburg garrison marches out.

## Remaining gaps

None for the Bremen letters: every group has a value; the residue is transcription slips from the phone photographs
(`occupireh`, `feldlsihen`), and the statistical validation (11 Oct 2026, `validation.tsv`) passes.

## Escalation
- [x] siblings: all 14 records of catalogue 207 opened and sorted; the others are separate entries (above)
- [x] clear-pages: the interlinear glosses are the decipherment of the time, used to rebuild the key
- [n/a] known-keys: key rebuilt from the glosses; no outside key needed
- [n/a] print: the letters read in full from the key; no edition needed for the reading
- [x] key-rebuild: band key from glosses, completed from unglossed words and the six-column grid
- [x] retry: every group of both letters decoded (bremen_decoded.txt)

## Assumptions for George's review
- R4282 belongs to George Lasry's entry `decode4282`; its outcome (key recovered from ciphertext-only, read) is left as
  he filed it, and nothing of this folder's failed 21 Sept attempt is credited to or subtracted from it.
- The Rusdorff letters (R4333-R4337) and the E 708 letters (R4338-R4341) are each kept as one entry by correspondence;
  no shared key is claimed for either group, and they are not worked.
