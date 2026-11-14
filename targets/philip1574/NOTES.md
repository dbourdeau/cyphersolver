# Philip II to Don Juan of Austria, Madrid, 28 Aug 1574 (KHA G016-A0204)

Status: read (from the clear version on the same item; key rebuilt from the pair and checked line by line, 24 Oct 2026)

## Source

- Koninklijk Huisarchief, The Hague, Collectie Handschriften 2e serie, G016-A0204 ("Brief in cijferschrift van
  Filips II ... aan Don Juan van Oostenrijk", 2 stukken), 6 scans via koninklijkeverzamelingen.nl; fetched full size
  from `cms.koninklijkeverzamelingen.nl/api/images/rendition/<id>/original/` (ids in `scans.json`; `img/` git-ignored).
- Found by the Nationaal Archief sweep, second pass (KHA lead K1).
- The catalogue calls Don Juan "stadhouder van de Nederlanden"; in Aug 1574 he was Captain General of the Sea, as
  the address says ("Al Ill.mo Don Juan de Austria mi muy caro y muy amado hermano, mi Capitan General de la Mar").

## What the scans hold

- s1: the original, opening in clear ("Ill.mo don Juan de Austria mi muy caro y muy amado hermano mio Capitan general
  de la mar"), then about 30 lines of numeric cipher with a few clear words ("de lo qual los he querido avisar").
- s2 left / s3: the end of the original, signed "Yo el Rey", countersigned "Ant. Perez", "Madrid xxviii de agosto
  1574"; s5-s6 the address leaf with seal.
- s2 right / s3 left: a **clear version** in another hand headed "G16-A204": the alférez Diego de Esquivia, captive of
  the Moors since the Count of Alcaudete's expedition of 1558, slave of Hasan Pasha in Constantinople, freed in 1573,
  came to Naples to inform Don Juan; the King recommends him (15 escudos ...). It ends "Madrid xxviii de agosto 1574".

## Prior work

- Not in Gachard's *Correspondance de Philippe II* (Netherlands affairs; Don Juan only from 1576). No web hit for
  Esquivia; not on DECODE (23 Oct 2026).

## Key and check (24 Oct 2026)

- `clear_version.md`: the clear version transcribed. `key.md`: the key rebuilt by aligning it with the cipher.
  Letters on one- and two-digit numbers near alphabetical order, vowel marks on the preceding sign (cross = e,
  dot = i, stroke above = u), a few code groups (pe *como*, co *año*, Lo *carta*), y written g, numbers in clear.
- Checked against the cipher on scan 1 with the key, line by line on about 14 of the ~30 cipher lines (both
  paragraphs, beginning, middle and end): every word agrees except
  - end of paragraph 1: the cipher has *que lo podra hazer* (9 ρ X+ 19), the clear version *saber*;
  - the interpreter's name: the cipher spells *15 19 ρ 13+ g* (Oram bey), the clear version *[?]oran vey*. This
    is Hürrem Bey, the Porte's chief dragoman, a known contact of Philip II's agents.
- The cipher writes *de lo qual los he querido avisar* in clear where the clear version has *os*; the clear version's
  doubled phrase (*de lo qual os he querido avisar* twice) is in the cipher too.

## What it says

Philip II recommends to Don Juan the alférez Diego de Esquivia, captured at Mostaganem in 1558, a slave of Hasan
Pasha in Constantinople, free since 1573, with 15 escudos a month to serve near Don Juan. Esquivia brought a
letter from Hürrem Bey, chief interpreter of the Sultan; the King answers encouraging him to continue in Spanish
service and offering him refuge in Spain, and a second letter goes to Mostafa, a Milanese renegade engineer who had
been at La Goleta and now sailed with Uluç Ali in the Turkish fleet. Esquivia carries both letters; Don Juan is to
decide how to use them. The letter is dated a week before La Goleta fell (13 Sept 1574).

## Independent verification by Brice Dudout (PR #570, 14 Nov 2026)

Brice Dudout (`VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) recounted the read bar on `clear_version.md`.
`research/reading_audit/v10_relabel.py` gives 433 words and 37 holes, 0.921, under the bar; but the 37 holes are the
abbreviation expansions written in brackets (r[elaci]on, q[ue], v[uest]ra ...), not unread words. Counted on the
Spanish body with the expansions as read words: 406 words and one hole, *[?]oran*, the interpreter's name, whose first
letter is not read on the clear sheet (the cipher spells it Oram): **0.998**. Re-run here (the script takes the checkout
root as its argument): the same figures. `read_share` is now 0.998 (was 1.0); the class stays read. Running
`v10_relabel.py --apply` on this target as the file stands would wrongly move it to read in part.

The scans: the rendition address in Source now answers 410 Gone (checked here too, 14 Nov 2026) and, by his report, the
deepzoom paths of `scans.json` answer 404. The lines not compared with the key (below) therefore cannot be checked from
this route at present.

## Remaining gaps

- code groups 161 (*turco*?) and g 90 (*Porque*?) - blocker: open-codes; one context each, read from the clear version
- Verification, not reading: about 16 cipher lines on scan 1 and the cipher end on scan 2 left were not compared sign
  by sign with the key; the clear version covers them and every compared line agreed. The image route used in October
  no longer answers (410 Gone, 14 Nov 2026), so this needs the scans again.

## Escalation

- [x] clear-pages: the separate sheet is the decipherment
- [x] key-rebuild: key rebuilt from the pair
- [x] print: Gachard (Netherlands), web, DECODE: nothing
- [n/a] siblings: no other Philip II - Don Juan cipher letter found online yet
