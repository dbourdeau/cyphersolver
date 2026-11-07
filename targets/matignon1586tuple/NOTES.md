# Matignon's tuple cipher: despatch to Henri III, May 1586 (BnF fr. 15572 ff. 234r-238v)

Status: read in part. Contributed by Michael Brackx (issue #86, 22-23 Oct 2026), taken in 24 Oct 2026. F. 234r read
(glosses recorded group by group, issue #95), eight pages read in part, f. 236v decoded, not read. Page: [`docs/matignon1586tuple.html`](../../docs/matignon1586tuple.html).

## The document

- BnF fr. 15572 ff. 234r-238v (Gallica ark `btv1b9061879d`, canvases 241 right to 247 left; canvas 243 duplicates
  242). Cover on canvas 240 right, *Au Roy*, endorsed May 1586 (Tomokiyo has March). Ten pages, 220 lines, wholly in
  cipher: no clear text, signature or date. No leaf is missing before f. 234r (canvas 241 left is the cover of a
  different letter, Forget to Villeroy).
- Writer: Jacques de Matignon, the King's lieutenant in Guyenne, to Henri III (the cipher is Tomokiyo's
  "Matignon's Tuple Cipher", cryptiana, *Henry III's Cipher with Ambassadors*, which he calls the only letter known
  to him in it, with no key or reading).
- **One key, one entry.** This is a different cipher from Matignon's Cipher-3 ([`matignon1586c3`](../matignon1586c3/NOTES.md))
  and from the Mayenne-Forget Cipher-1 ([`matignon1586`](../matignon1586/NOTES.md)). The names overlap with the
  Cipher-3 note f. 276 (Jehan Durant, La Roussière, La Guiolle, La Saussaie): the same affair in another cipher.

## The cipher

Each plaintext letter is a group of two to four signs (`ξ.ur` = e, `ỹop` = a, `aỹ` = t, `bɿ` = s); figure groups
for letters and syllables (14ʓ = p, 20 = la, 18 = le/de, 237 = g, 30∂ = m, 15 = mm); word signs (⁘ = qui/que,
ſq̄ = par, 60 = faire, C•ꝺ = sieur, 8 = Monsieur); nulls between groups. Groups may run across a line break. A
contemporary decipherer drew bars between groups and wrote a letter or syllable over most of them (whole phrases on
ff. 236-238).

## Files

- `transcription/f<page>.txt`: one label per group, one line per cipher line (Brackx).
- `legend.md`: the 120 labels used, value(s), sign shape, kind (shape / gloss / null / open), first locations.
- `key.json`: the 136-label key as posted (a few labels unused in the final transcription).
- `decryption/f<page>.txt`: decode per line with label = value per group.
- `texts/f<page>_reading.md`: the reading in the decrypted spelling (no accents), holes sized: `[?]` one unread
  group, `[?word]` doubtful, `[word]` supplied, bracketed letters inside a word supplied.
- `texts/f<page>_en.md`: Brackx's English with the same holes.

## How it was done (Brackx, with Claude Code / Claude Opus 5.5)

Full-size Gallica canvases deskewed and flattened (mirrored-verso subtraction on f. 237; it failed to register on
ff. 236 and 238). Every line transcribed group by group with the glosses; beam search over each label's allowed
values under a French character 5-gram; seven rounds of image checks. Coverage 80.8% of decoded letters in French
corpus words with the model rebuilt from the *Essais* I-III (posted 83.0% with a model partly built from the wrong
Gutenberg texts); shuffled keys 28-30%.

## Measured here (24 Oct 2026)

read_share = 1 - (holes + doubtful) / (words + holes), `research/reading_audit/v10_relabel.measure` on
`texts/f<page>_reading.md`; in-word bracket expansions (`i[l]`, `l[e]ur`) count as holes, which is why some pages
come out a point or two under Brackx's own figures.

| page | groups | read_share | state |
|---|---|---|---|
| 234r | 251 | 0.974 | **read** (23 Oct, issue #95) |
| 234v | 251 | 0.622 | read in part |
| 235r | 183 | 0.962 | read in part |
| 235v | 255 | 0.954 | read in part |
| 236r | 271 | 0.723 | read in part |
| 236v | 231 | 0.431 | decoded, not read |
| 237r | 190 | 0.940 | read in part |
| 237v | 201 | 0.929 | read in part |
| 238r | 202 | 0.836 | read in part |
| 238v | 117 | 0.756 | read in part |

Word-weighted over all ten pages: 0.818 (`outcome.fraction_read`). Groups: 2,152 (`_check_profile.py --measure`).

**Why the other pages are not read, even over 95%.** On every page 8-14% of groups belong to labels with two or more values
(E2 c/e, M30 m/n/mm/nn, QUI qui/que, N18 le/de, DA de/d ...) where the decoder chose the value in context. That is
over the 3% look-alike limit in README Conventions. The glosses would confirm most choices, but they were not
recorded group by group, so the confirmation cannot be shown token by token. Reading review: grade B, Claude Opus
5.5, 24 Oct 2026 (coherent but raw: decrypted spelling, the decoder's choices unconfirmed).

**The glosses recorded (issue #95, 23 Oct 2026).** Brackx then recorded the contemporary gloss over every
multi-valued group on the five pages nearest the bar, 107 groups, in `glosses_multivalued.tsv`:

| page | multi-valued | gloss agrees | contradicts | unclear | no gloss |
|---|---|---|---|---|---|
| 234r | 24 | 20 | 1 | 3 | 0 |
| 235r | 23 | 5 | 0 | 0 | 18 |
| 235v | 21 | 2 | 0 | 1 | 18 |
| 237r | 17 | 6 | 1 | 0 | 10 |
| 237v | 22 | 3 | 2 | 3 | 14 |

- **f. 234r is glossed group by group**, so its choices can be shown: 3 of 251 groups stay unconfirmed (1.2%), under
  the 3% limit, at read_share 0.974. It is **read**.
- **Four contradictions, all taken into the readings:** 234r l. 7 the gloss has *qui* over the group decoded *que*
  (*les affaires qui ce presente[nt]*); 237r l. 1 *de* over `DA` decoded *d*; 237v ll. 3-4 *mons[ieu]r* twice over
  the `SR` groups decoded *sieur*.
- 235r-v and 237r-v carry glosses only on some lines or phrases, so most of their choices stay unconfirmed.

**The other five pages (issue #99, 25 Oct 2026).** Brackx recorded the glosses on 234v, 236r, 236v, 238r and 238v
the same way (109 more rows in `glosses_multivalued.tsv`):

| page | multi-valued | agrees | contradicts | unclear | no gloss | unconfirmed share |
|---|---|---|---|---|---|---|
| 234v | 22 | 20 | 0 | 0 | 2 | 0.8% |
| 236r | 36 | 20 | 2 | 5 | 9 | 6.0% |
| 236v | 19 | 6 | 3 | 3 | 7 | 5.7% |
| 238r | 18 | 12 | 1 | 0 | 5 | 3.0% |
| 238v | 14 | 8 | 0 | 1 | 5 | 5.3% |

- All ten pages now have every multi-valued group checked against the glosses: 216 groups, 114 of 2,152 groups
  (5.3%) unconfirmed. No page changes class: 238r is inside the 3% limit and 234v nearly fully confirmed, but both are
  under 95%.
- Six contradictions, the reading following the gloss: 238r l. 20 *m* for *n*, so *m'a dit auoir charge* is now read
  (0.803 to 0.836); 236v ll. 4-5 *cure remo[ns]trant*; 236v l. 11 *pour*, l. 7 *que*; 236r l. 22 *m* (a name, open)
  and l. 25 *ss*. The last four fall in unread or doubtful words and change the decode, not the counts.

## Content

A report to the King from Guyenne, spring 1586: the Garonne trade cut by the Protestants of Caumont; the Gascon
captains' discontent and their talk of a league; the people ruined by Huguenot contributions; 500 horse to be kept
with the army beyond the Garonne; *maistre Jehan Durant*'s order to attack Castillon-sur-Dordogne, which drove the
Gascon captains away. The second half: La Saussaie, the sieur de la Fontaine, the baron de Vaillac (to be rewarded
with 2,000 muids of salt or three Huguenot councillors' offices), Alincourt and Gouffiers, the friends of La
Roussière and of la Magdaleine.

## Remaining gaps
- multi-valued labels on the nine pages other than 234r (E2, M30, QUI, N18, DA and others) - blocker: no-key-material; every multi-valued group on all ten pages checked against the glosses (issues #95, #99): 114 of 2,152 groups are not confirmed by a gloss (104 none or unclear, 10 contradicted and followed in the readings), and nothing else on the leaves settles them
- f. 236v, most of the page (read share 0.431) - blocker: illegible; show-through and faded ink, fragmentary glosses, verso subtraction failed to register
- 234v l. 13 ('Cadarran(?)') and ll. 21-24; 236r l. 15, ll. 22-25; 238r ll. 20-22 ('la crois lartie'); 238v ll. 7-10 ('Bourg(?)') - blocker: illegible; re-read at full and upscaled resolution in the contributor's round 7
- 41 rare 'open' labels (79 groups, 3.7%) with no shape recorded - blocker: no-key-material; once or twice each
- single-use values (19 = sa on 236v, QUAND, trouppes, X = paix, code 13) - blocker: too-short; one occurrence each

## Escalation
- [x] siblings: neighbouring Matignon letters checked by Brackx (Cipher-2 ff. 218-219, Cipher-3 f. 276, fr. 15573 ff. 379-381): different ciphers; no other letter in this key known (Tomokiyo)
- [x] clear-pages: no clear copy or decipherment leaf in the volume around ff. 234-240; the interlinear glosses are the decipherment and were used
- [x] known-keys: Cipher-1 (matignon1586), Cipher-2 (mayenne1586c2), Cipher-3 (matignon1586c3) are different systems
- [x] print: Tomokiyo describes the letter with no key or reading; no edition found by web search
- [x] key-rebuild: Brackx completed the glossed key from the language (beam search under a French 5-gram), one-off values kept as single-use labels
- [x] retry: seven rounds of image checks, round 7 aimed at every open spot; no further gain recorded
