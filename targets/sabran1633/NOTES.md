# The Louis XIII–Sabran cipher, 1631–1635: Baluze 155 f. 79, fr. 4134, fr. 4135 — NOTES

Status: read in part (22 Oct 2026). George Lasry's key reads all 43 imaged pages (PR 84). The eight leaves Tomokiyo
lists beside them were checked on the image the same day: seven carry no cipher outside Lasry's images, f. 218r has
a 17-sign marginal run he missed, and Baluze 156 f. 157 (1636) is in another key, too short to break alone.
**23 Oct 2026, re-read (REREAD_BRIEF batch b34):** Baluze 156 f. 157r kept *decoded, not read*: its neighbouring leaves (ff. 155-161 opened, ff. 140-190 surveyed on Gallica) carry no decipherment, copy or sibling in the same key, and a hand crib on the repeated run `g 7 4 t o` does not hold (`baluze156/f157r_reread_log.md`).

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): Baluze 156 f. 157r (two crib values only) is marked *decoded, not read* and the two-word f. 218r margin *not prose* in profile.json. Claim unchanged.


**Outcome: key recovered from ciphertext-only by George Lasry, read in part (contributed, PR 84).** He recovered
the key with CTTS's built-in cryptanalysis in 2022 on the King's letter of 1631, and in October 2026, with Claude
Opus 5.5 and OpenAI Codex, completed the transcription of 43 images and the nomenclator, and edited and translated
18 letters (`lasry2022/READING.md`). Write-up: `docs/sabran1633.html`.

**One key, one entry (22 Oct 2026).** Two former entries are folded in here:
- `sabran1631` (Louis XIII to Sabran, Baluze 155 f. 79, DECODE R2748; "read from existing decipherment",
  Lasry 2022): its notes are `notes_former_sabran1631.md`; `docs/sabran1631.html` is now a "moved" page.
- the fr. 4134 entry built on Harumi-Matsuba's partial AI reading of nine leaves (issue #56, 20 Oct 2026): its
  notes are `notes_issue56_fr4134.md`, its data and code `contributed/`, the earlier checks `measure.py`,
  `measure.txt`, `spotcheck.md`.

## Documents (all three in one cipher)

| source | images | cipher signs | letters |
|---|---|---|---|
| BnF Baluze 155 f. 79r–v: Louis XIII to Sabran, Dijon, 28 Mar 1631 (DECODE R2748; Gallica btv1b9001401d) | a1, a2 | 528 | 1 |
| BnF fr. 4134 ff. 46v–73v, Sabran's "Troisième livre des negotiations … à Gennes" (1633), to Bouthillier (Gallica btv1b9060193z) | 14 | 1,061 | 8 |
| BnF fr. 4135 ff. 132–252, "Le quatrième livre …" (1634–35), to Bouthillier (Gallica btv1b9060194c) | 27 | 1,764 | 9 |

Melchior de Sabran was the French resident at Genoa from late 1629 to about 1638. The letter-books are his copies of
his despatches to Claude Bouthillier (or his son Léon, Chavigny, secretary of state from March 1632: which one
received each letter is open). Most images show only part of a letter; dates in brackets come from the leaf order
and the BnF catalogue (Lasry's READING.md, letter by letter).

## The key (Lasry, `lasry2022/ctts/key.txt`)

Homophonic substitution of 22 letters with 51 signs (up to four for S; digits 7 = A, 8 = E, 9 = I, 10 = O,
11 = V); 41 two-digit codes for words and syllables in first-letter order (17 bon, 24 ce, 26 de, 35 Genes,
47 monsieur, 59 que, 68 vous, 95 ou); ten name signs read from context ([France?], [Espagne?], [Republique?],
[Savoie?] …); three doubling signs. The clerks' hands differ from leaf to leaf, so one sign can look different
(the clerk of ff. 57 and 242v–245v writes H with a straight stem and F as a script L).

## Checks made here (22 Oct 2026)

- `decode.py` applies key.txt to the CTTS transcription and reproduces Lasry's counts exactly: 3,353 signs,
  2,853 letter signs, 287 firm and 212 tentative code readings ([Traicte] counted as tentative), one unknown
  (code 46). Per source 528 / 1,061 / 1,764; 108 distinct sign labels (hand variants included).
- `docs/_validate.py` (fr-1600-letters, letter signs only, codes and clear text as breaks): reading −2.125 per
  letter; random keys −5.728 (z 7.8); key fitted to shuffled text −3.255 (z 94.3); annealer on the real text
  −2.916. Verdict: pass.
- `coherence.py` → `coherence.txt` (word cover, fr-henri4 vocabulary, early spelling normalised): 83.7% of the
  deciphered text lies in French words of 3+ letters; Baluze 155, which Lasry deciphered in full in 2022, gives
  91.6%, the measure's ceiling on a clean letter; fr. 4134 84.5%, fr. 4135 80.8%; shuffled keys median 36.9%,
  max 44.9%.
- Against the independent reading of issue #56 (Harumi-Matsuba, nine fr. 4134 leaves): 761 of their 865 decoded
  letters align with Lasry's (88%; f. 73v 100%, f. 66v 98%, f. 46v 96%, f. 50v 77%, the leaf where theirs formed no
  words). Their unlisted codes 35, 12, 33 are Lasry's Genes, [Agent?], [Guerre?].
- Image: the second cipher line of Baluze 155 f. 79r (DECODE R2748 P1) matches the transcription sign for sign
  (26 of 26: *monacho, l'avtre vostre seiovr a Genes*). Gallica refused scripted IIIF requests on 22 Oct 2026, so
  no fr. 4135 leaf was checked on the image here.
- No edition of the fr. 4134/4135 cipher passages found (web, Tomokiyo louisxiii.htm and GL.htm, the
  contributor's sources). Sabran's despatches of 1636–37 printed in the *Correspondance de Sourdis* are later.

## The eight listed leaves (checked 22 Oct 2026)

Images from openapi.bnf.fr IIIF (gallica.bnf.fr still refuses scripted requests). fr. 4134 has one page per Gallica
view (f. 51r = view 109); fr. 4135 one opening per view, view v = f.(v−9)v | f.(v−8)r, checked on the folio numbers
of views 220–256. Tomokiyo's fr. 4135 folio numbers name Gallica openings, so each was read as an opening.

| listed | what is there |
|---|---|
| fr. 4134 f. 51 | f. 51r–v all clear: the letter "A Monsieur Bouthillier du 2e Juillet 1633" begins on f. 51r; its cipher is on f. 52 (Lasry's image 52, his letter 4, dated "[1 Jul]": the heading gives 2 July) |
| fr. 4135 f. 217 | opening 216v \| 217r. f. 216v is Lasry's image "215v" (misnumbered, see below); f. 217r is clear, Sabran to the duc de Créquy, 7 Oct 1635. In the next opening, 217v \| 218r, f. 218r has a marginal cipher not in Lasry's image (below) |
| f. 226v | opening 226v \| 227r: 226v clear (letter of 25 Oct begins); 227r is Lasry's image 227 |
| f. 227v | opening 227v \| 228r: under the end of the letter (signed "S. de Sabran") is a faint cipher block, the show-through of f. 227r (its mirror image reads "… 8 59 43 45 …", f. 227r line 11); 228r clear |
| f. 231v | opening 231v \| 232r: 231v clear; 232r is Lasry's 232a/232b |
| f. 239v | opening 239v \| 240r: both clear (letter of 30 Nov 1635) |
| f. 243 | opening 242v \| 243r: 242v is Lasry's image 242v; 243r clear, to Créquy, 10 Dec 1635 |
| Baluze 156 f. 157 | view 161: "Coppie du 9e febvrier 1636", 15 cipher runs, 136 signs; ff. 157v–158 clear. Another key (below) |

Real f. 215v is clear too (end of a letter, the 4 Oct summary, the 8 Oct letter begins).

**Lasry's image "215v" is f. 216v.** Its first line ("incommodité que l'on souffrira par l'impuissance …") is the
left page of the 216v | 217r opening. Letter 11 therefore runs f. 216r (images 215a, 215b) → f. 216v and ends there
with "je demeure eternellement" and a summary of a later note. READING.md prints the 216v text first and says the
end on f. 216v is not imaged; the order should be reversed. Left in his files as contributed; noted here and on the
page.

**f. 218r margin (new, 17 signs, `baluze156/fr4135_f218r_margin.txt`).** At the "+" after "la raison que le Roy a
d'avoir", two lines in the left margin. Lasry's READING has only "[marg.: Cll]" (the "ell" after line 1). Read with
his key sheet: `o 7 h a S y 9 z` = c a d a v o i r, `# a n E 9 d 7 ŋ e` = s a n t i m a n t: "[c]a d'avoir /
[s]antimant", the words the clear text has at that place ("a d'avoir … [res]sentiment"). First sign of each line
doubtful.

**Baluze 156 f. 157r (`baluze156/f157r.txt`, `solve.py`).** Written at Genoa after Sabran had left for court
("Monsieur de Sabran est party de Gennes … pour se rendre a la Cour"): Duke Doria, at the Lérins islands under
pretext of fear of the French fleet, gathers the Spanish galleys of Naples and Sicily for a design on Marseille,
learnt from a Gascon who is sent to the maréchal de Vitry; Nice and Villefranche supply munitions; Florence and
Modena pressed by Don Francisco de Melo. The cipher (names and means) uses lower-case letters, digits and doubled
strokes; 136 signs, 33 types with codes 12, 36, 94.
- Lasry's table by sign shape gives no French (run 2 → "eroobliag?cm"); Tomokiyo's Servien–Sabran key of 1632
  (`cryptiana servien.htm`, also lower-case signs) neither (run 12 → "ag?la?agnq").
- Cribs: "munitions [g n 36 6 g tt g n b u]" = "en GALERES de genes" if 36 = galeres, Lasry's code (g=e n=n 6=d tt=g
  b=e u=s); "faire [d o 4 n g ff] audit" = "donner" (d=d o=o 4=n ff=r). g is the commonest sign (21/136).
- Anneal inside the clear context (fr-1600-letters), free and with the ten crib values fixed: degenerate both ways.
  4.9 signs per letter type is below what a homophonic solve needs; a sibling letter in the same key is the way in.

## Verification 3, 23 Oct 2026

The v3 sweep flagged the 43-image entry at 0.0: it scored `lasry2022/ctts/decryption/all.txt`, CTTS's raw output
(spaced letters and `[plaintext]` placeholders), which is not a reading. The reading is `lasry2022/READING.md`. Its
18 "French" sections, clear and cipher together, score **0.721 on explicit holes** (0.536 plain, the manuscript's v
for u being unknown to the word list), hole rate 0.086; the cipher runs alone (the 401 bold stretches) score 0.84 on
explicit holes and 0.712 plain. The 212 tentative name-code readings count as holes. Kept read, grade B; the entry's
`reading` now names `lasry2022/READING.md`.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: rescored the 18 French sections of lasry2022/READING.md: plain 0.519, explicit 0.715, hole rate 0.088. The writer spells by ear (secretere, trete, afaire, eloignemant) and the tentatively read name codes count as holes; the rest builds sentences. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

## Read share over cipher words only (16 Nov 2026)

README Conventions (16 Nov 2026): the read share counts the words written in cipher only. `lasry2022/READING.md`
marks the cipher in **bold** and the clear in roman; the count takes the bold words of the 18 "### French" sections
(image markers cut), a bracketed code reading counting as one word. Holes, sure words only: the 209 tentative code
readings (`[Savoie?]`, `[France?]`, `[Republique?]`, `[Name1?]` ...), 3 doubtful readings (`dessein[?]`, `[r?]`,
`pie[r?]`), the blotted `se[blot]s`, and 13 words with a supplied letter (`Ros[s]y`, `re[s]idant`, `[d]e` ...: the key
is rebuilt, so no slip rule applies). Firm code readings count as read.

- The 43-image entry: 0.929 (24 Oct, v2_score over clear and cipher together) -> **0.790** (850 of 1,076 cipher words).
  Whole letter, clear included, not the measure: 0.929.
- Class unchanged: **read in part**. Only letter 1 (the King's letter, Baluze 155) is over the bar on its own.
  `outcome.fraction_read` (0.9609) is the share of cipher signs that carry a value and is left as it is.

| Letter | cipher words | holes | share |
|---|---|---|---|
| Letter 1 — Baluze 155, f. 79r–v | 144 | 2 | 0.986 |
| Letter 2 — fr. 4134, f. 46v–47 | 25 | 2 | 0.920 |
| Letter 3 — fr. 4134, f. 50v | 78 | 19 | 0.756 |
| Letter 4 — fr. 4134, f. 52 | 32 | 6 | 0.812 |
| Letter 5 — fr. 4134, f. 54 | 28 | 19 | 0.321 |
| Letter 6 — fr. 4134, f. 57r–v | 56 | 8 | 0.857 |
| Letter 7 — fr. 4134, f. 66r–v | 53 | 6 | 0.887 |
| Letter 8 — fr. 4134, f. 69v | 15 | 2 | 0.867 |
| Letter 9 — fr. 4134, f. 73v | 5 | 0 | 1.000 |
| Letter 10 — fr. 4135, f. 132r–v | 36 | 8 | 0.778 |
| Letter 11 — fr. 4135, ff. 215v–216r | 96 | 13 | 0.865 |
| Letter 12 — fr. 4135, ff. 218r–220r | 154 | 38 | 0.753 |
| Letter 13 — fr. 4135, f. 224v | 12 | 3 | 0.750 |
| Letter 14 — fr. 4135, ff. 227–229v | 127 | 36 | 0.717 |
| Letter 15 — fr. 4135, ff. 232r–233r | 124 | 49 | 0.605 |
| Letter 16 — fr. 4135, ff. 241r–242v | 31 | 6 | 0.806 |
| Letter 17 — fr. 4135, f. 245v | 25 | 3 | 0.880 |
| Letter 18 — fr. 4135, ff. 251v–252r | 35 | 6 | 0.829 |
| **All 18** | **1,076** | **226** | **0.790** |

## Remaining gaps
- code 46 (fr. 4135 f. 219, once) - blocker: no-key-material; "d'une [46] de l'armée navale", context does not fix it
- 212 tentative name-sign readings - blocker: no-key-material; read from context only; o- and o-- may be confused in the ff. 215v–216 hand
- cipher runs that do not read (f. 50v "veraivre", "fevitga", "tmineli…"; f. 215b "parico"; f. 228v "duc de s / vop"; "Vbr[?]" on 54b, 57b) - blocker: illegible; reviewed against the images by the contributor, probably clerks' slips in the copies
- Baluze 156 f. 157r (9 Feb 1636 copy, 136 signs) - blocker: too-short; not Lasry's letter table nor the Servien key; two cribs give ten values, the anneal is degenerate at 4.9 signs per type; needs a sibling in the same key (none on the Baluze 156 leaves opened 23 Oct 2026, b34: `baluze156/f157r_reread_log.md`)
- f. 218r margin, first sign of each line - blocker: illegible; against the gutter, matches no sign of the key sheet
- the originals as received (Archives diplomatiques, Correspondance politique, Gênes) - blocker: needs-physical-access; not digitised

## Escalation
- [x] siblings: Baluze 155, fr. 4134 and fr. 4135 in one key; the issue #56 reading compared (88% agreement); the eight listed leaves read on the image 22 Oct 2026 (seven have no further cipher; f. 218r margin added; Baluze 156 f. 157 another key)
- [x] clear-pages: no decipherment on the letter-book leaves; Baluze 155 f. 80 blank
- [x] known-keys: the key is Lasry's own, recovered ciphertext-only; on Baluze 156 f. 157 Lasry's table and Tomokiyo's Servien–Sabran key (1632) both tried, neither fits
- [x] print: no edition of these passages; Sourdis correspondence covers 1636–37 only
- [x] key-rebuild: nomenclator completed from context and first-letter order; code 46 stays open
- [x] retry: 23 Oct 2026 (b34) Baluze 156 neighbouring leaves searched for a decipherment or sibling (none), crib on the repeated run tried (fails)
- [x] retry: the eight listed leaves opened and read with the key (22 Oct 2026): f. 218r margin read, Baluze 156 f. 157 cribbed and annealed (`baluze156/solve.py`); code 46 and the slips on Lasry's images were not re-read this session (contributor reviewed them on the images)

## Files
- `baluze156/` — the 22 Oct 2026 check of the listed leaves: `f157r.txt` (Baluze 156 transcription), `solve.py`, `fr4135_f218r_margin.txt`, `README.md`.
- `lasry2022/` — George Lasry's contribution (PR 84): CONTRIBUTION.md, READING.md, CTTS project, key and overlay images.
- `decode.py`, `coherence.py` (+ `coherence.txt`), `validation.tsv` — the checks above.
- `notes_former_sabran1631.md`, `notes_issue56_fr4134.md`, `contributed/`, `measure.py`, `measure.txt`,
  `spotcheck.md`, `build_reveal.py` — the two former entries.
- `profile.json`
