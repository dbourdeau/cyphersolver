# Biermann to Marcus Gioë (England), Copenhagen 12 January 1675: cipher passage

Contributed by Tomáš Pavuk (issue #720), working with OpenAI GPT-6 (Codex) and Claude (Anthropic).

Source: Rigsarkivet, TKUA Almindelig del, Conrad Biermanns kopibog 1675 (S-1418), p. 12,
Arkivalieronline image 015 (right page; id 48573966); the letter ends in clear on p. 12v, image 016 (left page;
id 48573967).
Key: TKUA "Chiffer" 1670-1709, image 55 (`key.tsv`), unchanged. Transcription: `transcription_1675-01-12_gioe.txt`;
mechanical decipherment: `python decode.py transcription_1675-01-12_gioe.txt`, kept unedited in
`decryption_1675-01-12_gioe.txt`.

Clear text before the cipher: the news in Gioë's report of 29 December is of great weight and the King has given
it all the thought it needs. "Il faut neantmoins esperer que ..." After the cipher, in clear: the Swedish
ambassador had his audience on Friday, is paying his visits and has asked for commissioners; the resident la
Maire has orders to warn the Dutch ships in Swedish ports to leave; the allies have left Brisach for Strasbourg
on Turenne's arrival.

## Line by line

`<n>` is a group with no value on the sheet, as `decode.py` prints it.

| line | decipherment |
|---|---|
| 12.01 | {Staten General} fa |
| 12.02 | i sa n t s le u r po s si b |
| 12.03 | le po u r do n ne r co n te |
| 12.04 | n te me n t a u <123> i l ne |
| 12.05 | vo u d ra po s do n ne r |
| 12.06 | li e u pa u ne re so lu ti |
| 12.07 | o n de ce t te na tu re a u |
| 12.08 | ne no u ve l le <488> qui <sq> a |
| 12.09 | u ra de la <477> i ne a fa i |
| 12.10 | re a g re e r a so n pa r |
| 12.11 | le me n t le que l [apparemment] |
| 12.12 | [sera toujours plus porté a contribuer a] la f |
| 12.13 | fo i b li <31> se me n t de |
| 12.14 | la {Frankrig} qua so n a g ra n di |
| 12.15 | s se me n t [M. L'Ambassadeur de Suede ...] |

## Reading

Marks: `[123]`, `[488]` a code with no value; `[?word]` a word that holds a group with no value on the sheet or
a letter that is not written; `{+..}` a one-digit slip of the copyist (README Conventions, 14 Nov 2026). Every
letter or word that the key does not give for the groups as transcribed carries one of these marks.
Conventions, stated once and not marked word by word: accents, apostrophes, capitals, punctuation and word
division are added (`qui` + l is written *qu'il*, `la f` + `fo` *l'affo-*); the sheet labels its name codes in
Danish and they are given in French, 162 *Staten General* as *les États généraux* with the article French
needs, 212 *Frankrig* as *France*.

Il faut néanmoins espérer que les États généraux faisants leur possible pour donner contentement au [123], il ne
voudra {+pa}s donner lieu [?par] une résolution de cette nature à une nouvelle [488], qu'[?il] aura de la
{+pe}ine à faire agréer à son parlement, lequel apparemment sera toujours plus porté à contribuer à
l'[?affoiblissement] de la France qu'à son agrandissement.

(In English: It is to be hoped that, with the States General doing what they can to satisfy [123], he will not
wish to give rise [?through] a resolution of this kind to a new [488], which [?he] will have difficulty getting
his Parliament to approve; that Parliament will apparently always be more inclined to help the [?weakening] of
France than its growth. The translation with the same marks is in `reading_1675-01-12_gioe_en.md`.)

## Measure

- Cipher tokens: 132 (counted by `decode.py`). Resolved by `key.tsv` and the sign table: 127 (96.2%).
- By words: the cipher passage has 49 words; five are holes ([123], [488], [?par], [?il], [?affoiblissement]);
  44 are sure: 0.898, read in part. The project recounted the same figures on issue #720.
- One-digit slips, counted as read under the rule of 14 Nov 2026 (K55 is the surviving key; the other groups of
  each word are read from it; the slip is on the image):
  - 12.05 `579` (po) where the sense wants 576 (pa): "vo-u-d-ra po-s" for *voudra pas*. A clean 579 on the page.
  - 12.09 `477`, not on the sheet, where the sense wants 577 (pe): "477-i-ne" for *peine*. A clean 477 on the page.
- Holes, kept as holes:
  - 12.04 `123`: not on the sheet. `new_values.tsv` has it from the Høeg letter of 9 January as l'Angleterre or
    le Roy d'Angleterre; "au 123 ... il ne voudra ... son parlement" here fits the King. Not adopted.
  - 12.08 `488`: not on the sheet and not met in the Høeg and Meyercron letters; a feminine noun ("une nouvelle
    488 qu'il aura de la peine à faire agréer à son parlement").
  - 12.08 `sq`, the open square: `new_values.tsv` proposes l from four places; it gives *qu'il* here. Not adopted.
  - 12.13 `31`: `new_values.tsv` proposes s from the Høeg letter of the same day (*desesperent pas*); it gives
    *affoiblissement* here. Not adopted.
  - 12.06 "li-e-u pa u-ne": *par* wants an r that is not written. The last digit of 576 is overwritten on the
    page (576 or 579); neither supplies the r.
- On the image: 12.05 group 1 is 673 (vo) with the middle digit overwritten; 12.13 group 2 is 17 (i), where an
  earlier reading had 57, which is not a letter number on the sheet.
- Checks: read from the scan by two OpenAI GPT readers, one of them without the key (116 of 132 groups agreed
  at first, the rest settled on the scan); all 132 groups checked on the scan by Claude Fable 5.2, which had seen
  the transcription; the project read all 132 on image 15 in the review of #720 and all agree. No person has
  read the scan.
- The contributor's working files, review and report:
  <https://github.com/JOPPA5/hcsolve/tree/48e850e25723f701fed87fd7fec1f8c95861aee6/ciphers/gioe-1675-01-12>.
