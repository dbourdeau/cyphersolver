# Henry of Navarre to Ségur, BnF 500 de Colbert 401 ff. 233, 239, 288v (1585–86) — SOLVED 2026-09-16

Lasry review (25 Sept 2026): In private communications, Lasry wrote that he independently solved it in 2024 but his solution has not been published. Kept in the ciphertext-only list (outcome.first_break = 'unpublished prior').

**Status: the key is recovered and the three ciphered letters of 1585–86 are read in substance.** The alphabet, the
syllabary and the double-letter signs are fixed; a dozen word-signs written in letters (*pi*, *na*, *gne*, *H*, *L* …) and
three nomenclature numbers (180, 215?, 900) are glossed from context or left open. The 1583 letter at f. 143 is in a different
cipher and is not read. Tracker item #12; short-list candidate 4 of 2026-09-16.

## Corrections to the catalogue entry

- **Sender.** Tomokiyo's page lists these as letters of *Henry III*. They are signed *Henry* at Montauban (f. 239, 1586) and
  La Rochelle (f. 321, 11 June 1586), close "vostre affectionné maistre et parfait amy", and speak of "mon frere Mons.r le
  Prince" (Condé), "mon cousin le duc de Montmorency", the levy of reiters by the duke Casimir and Clervant: they are letters of
  **Henry of Navarre**, whose envoy to the German princes Ségur-Pardaillan was (the volume is titled *Négociation de M. de Ségur
  … pour le roi de Navarre avec les Princes protestans d'Allemagne, 1584–1588*). The f. 321 key Tomokiyo reconstructed is
  therefore also a Navarre cipher.
- **f. 143** (Beaupréau, July 1583) is not from the king either: it is *to* Ségur from a correspondent signing "vostre tres
  humble et tres … serviteur", and its clear text is about the cipher itself: *"Il me semble qu'il n'est point besoin d'autre
  alphabet, vous y avez toutes choses tellement dispersées en lettres, syllabes, doubles, nulles et tout le reste qu'il est
  impossible de le descouvrir … Les noms sont en lettres et syllabes."* That sentence is a description of the design found
  below (letters, syllables, doubles, nulls; names written with letter-signs), in a different key.

## Sources and access

- Gallica, ark:/12148/btv1b10035574w, 440 canvases, labels all "NP". IIIF manifest and images answer a script with a browser
  User-Agent (`fetch_gallica.py`; the 15 Sept block was transient). Canvas ≈ folio + 11 at f. 139, + 23 at f. 227, + 38 at f. 294.
  Cipher folios: f. 143 = canvas 154; f. 233 = 257; f. 239 = 263; f. 288v = 325 (left page); f. 321 = 359; f. 333 ≈ 370.
  Full-resolution images are 7749 × 6057 px; not committed (`img/`, `probe/`, `crops/` are git-ignored).
- Transcriptions: `ct_233.txt` (220 tokens), `ct_239.txt` (70), `ct_288.txt` (196), `ct_143.txt` (63, different key). Clear text
  in brackets. Re-read at 2× zoom for every digit the reading disputed (`crops/`).

## The design (recovered)

The numbers 1–53 are letters, doubles and a null in **alphabetical order with two or three homophones per letter**; 54–123 are
**seventy syllables, fourteen consonants × five vowels in alphabetical order**; word-signs written in letters and a few numbers
above 123 are names and words.

| numbers | value | evidence (words read) |
|---|---|---|
| 1 | *ee* / *ée* (double) | la lev**ée**, fortifi**ée**s |
| 2 | *ll* (double) | mi**ll**e |
| 3 | unread double (not in the 1585–86 letters) | — |
| 4 5 6 | a | **a**vec, **a**ucun, c**a**s |
| 7 8 | b | o**b**ligé |
| 9 10 | c | con**c**lure, **c**eux, du**c**, **c**hemin |
| 11 12 | d | **d**ix, gran**d**e |
| 13 14 15 | e | passim |
| 16 17 | f | (no plain *f* occurs; the syllables carry it) |
| 18 | g | **g**rande |
| 19 20 21 | h | mar**ch**er, **ch**emin, Daul**ph**iné |
| 22 23 24 | i / j | d**i**x, **j**e ne sçay, fa**i**re |
| 25 26 | l | mi**l**, qu'i**l**, **l**a |
| 27 28 | m | pro**m**ptement |
| 29 30 | n | passim |
| 31 32 33 | o | **o**bligé, **o**u |
| 34 35 | p | **p**romptement, **p**lus |
| 36 37 | q | (none in clear; *que/qui* are syllables 100/101) |
| 38 39 | r | passim |
| 40 41 42 | s | passim |
| 43 44 | t | passim |
| 45 46 47 | u / v | a**v**ec, **v**ous, Vi**v**arès |
| 48 (49) | x | di**x**, ceu**x**, deu**x** (49 once, else 49 = y) |
| 49 50 | y | mo**y**en, sça**y**, a**y**t |
| 51 | z | advisere**z**, oblige**z** |
| 52 | *et* | capituler **et** conclure, consentement **et** faire |
| 53 | null / word end | after *adviserez*, *obligé*, *Eglises*; between *H* and *L* |
| 54–58 | ba be bi bo bu | **bi**en, o**b**ligé (7), **bu**? |
| 59–63 | ca ce ci co cu | **Ca**simir, **ce**ux, en **ce** **ca**s, **co**nclure, se**co**urs |
| 64–68 | da de di do du | **Da**ulphiné, **de**ux, **di**ligence, a**du**iserez |
| 69–73 | fa fe fi fo fu | **fa**ite, **fe**i-re (faire), forti**fi**ées, **fo**urnir |
| 74–78 | ga ge gi go gu | obli**gé** |
| 79–83 | la le li lo lu | **la**, **le**, ob**li**gé, p**lu**s |
| 84–88 | ma me mi mo mu | **ma**rcher, prompte**me**nt, **mi**lle, **mo**yen, re**mu**ez |
| 89–93 | na ne ni no nu | **ne**cessaire, four**ni**r, **no**s |
| 94–98 | pa pe pi po pu | **pa**r, **pi**eces, **po**ssible, de**pu**is |
| 99–103 | qua que qui quo quu | **que**, **qui** |
| 104–108 | ra re ri ro ru | cont**ra**cte, **re**istres, esc**ri**re, p**ro**mptement |
| 109–113 | sa se si so su | **se**cours, Ca**si**mir, **so**nt, **su**is |
| 114–118 | ta te ti to tu | consen**te**ment, for**ti**fiées, **to**ut, capi**tu**ler |
| 119–123 | va ve vi vo vu | Cler**va**nt, le**ve**e, **vo**s |
| □ (square glyph) | *ss* (double) | nece**ss**aire (twice) |
| pi | *est* | s'il vous **est** possible, qui ayt **est**é faite, Clervant **est** obligé |
| Ra | *faictes* / *faire* | **Faictes** s'il vous est possible la plus grande levée |
| qu | *vous* | s'il **vous** est possible |
| na | *affaires* or *nouvelles* | de vos **na** depuis …; en quel estat sont nos **na** |
| gne (f. 288v) | *Je* | **Je** suis en extreme peine |
| gne gna (f. 239), pe pu, e, X, gla, H, L, Ne, qua, 180, 900 | word-signs, unread | see `reading.md` |

Alphabetical homophone counts (3 for a e h i o u, 2 for b c d f l m n p q r s t, 1 for g x z) are exactly the design of the
f. 321 key that Tomokiyo reconstructed (a 12–14, e 20–23, i 30–32, …, syllables ba–vu 63–142 consecutively, nomenclature from
162): the same chancery pattern with different offsets. In this key the syllable table starts at 54 and has fourteen
consonants (b c d f g l m n p q r s t v; no h, j, x, z rows), and the doubles and the null sit at 1–3 and 53.

## How it was solved

1. **Statistics.** 461 numeric tokens over 102 distinct values, 25 letter-written glyphs. Values 1–53: 311 tokens; 54–123:
   146; above 123: 3 (recounted later on the final transcriptions: 294 / 165 / 3). The frequencies of 64–123 taken mod 5 are 60 / 30 / 22 / 20 / 14 for one alignment and nearly flat for
   the other four: **blocks of five with one dominant slot**, the a-e-i-o-u signature of an alphabetical syllabary (e most
   frequent). That fixed the syllable structure before any letter was known. (The alignment is right; the start was first
   put at 64 and corrected to 54 from the reading, see step 4.)
2. **Structured annealer** (`solve.py`): numbers below the block start are free homophones (22 letters + null, null capped at
   8 symbols with a 3-nat penalty per dropped letter); each block of five is one consonant plus the fixed vowel; letter-glyphs
   and numbers above the table are skipped; the surrounding **clear French is kept as fixed context** for a 5-gram model
   (du Croc corpus: Catherine de Médicis, Teulet, Labanoff, 9.4 M letters, u=v, i=j, no spaces). Moves: reassign or swap a
   letter symbol, reassign or swap a block consonant. 300 000 steps, 12 seeds: 5 of 12 converge on one key at −6223.3.
3. **Controls** (`control.py`, `eval_control.py`): Catherine de Médicis' letters enciphered with random keys of the same
   shape, same token counts and the same clear-text interleaving. With the 64-start model: control 1 recovered 47 % of letter
   tokens and 4/12 blocks, control 2 90 % and 10/12. With the 54-start, 14-block model (control 3): **96.6 % of letter tokens
   and 12 of 14 blocks** (the two missed are *x* and *f*, one token each). So the method reads a text of this size when the
   structure is right, and not always when it is not.
4. **Reading.** The blind key already gave *capituler et conclure promptement avec ceux que vous adviserez … le duc Casimir …
   faire la levée … la faire marcher le plus tost, quelque prompt secours, deux mille reistres, dix mil escus, chemin, Vivarès,
   Daulphiné, n'espargner aucun moyen … secourir en toute diligence, la plus grande levée qui ayt esté faite, Monsieur de
   Clervant est obligé fournir, nos places sont bien fortifiées*. Against the final key it had **86 % of the letter tokens
   right (241/280) and 77 % of the syllable tokens (127/165)** despite the wrong block start; the letter part came out
   alphabetical on its own (a 4–6, b 7, c 9–10, d 11–12, e 13–15, g 18, h 20–21, i 22–24, l 26, m 27–28, n 29–30, o 31,
   p 34–35, r 38–39, s 40–42, t 43–44, u 45–47), which is the independent check. Reading *et conclure* (52 62 29 9 83 105),
   *secours* (110 62 46 39 42) and *le duc Casimir* (80 68 9 59 111 86 38) forced 62 = *co*, 59 = *ca*, 65 = *de*, 56 = *bi*
   → the table starts at 54 with b c d …; *que vous* (100 47 …) and *qu'il* (101 25) fixed 99 = *qu*; *Clervant* fixed
   119 = *va*. Rerun blind with the corrected structure (start 54, 14 blocks; `run_target14.log`), 6 of 8 seeds agree at −6201.9 and the key has **88.9 % of the letter tokens (249/280), 90.9 % of the syllable tokens (150/165) and 11 of 14 blocks** right against the final key; its only null is 52 (*et*), and the three blocks it misses are *b*, *qu* and *v* (the model writes *v* as *u*, and *qu* is a two-letter consonant it cannot represent).
5. **Digits disputed by the French were re-read at 2× zoom.** Confirmed as written: 20 in *a-v-i-h* (avec), *contra-h-te*
   and *Valen-h* (20 = h everywhere else; the encipherer's slip for 10 = c, or the key really doubles c at 20 — the three
   *ch* words read with 9/10 + 20 exclude that); 46 in *e-v-c-ri-re*. Corrected by re-reading: line 5 of f. 288v ends
   `80 40 65 45` (*les deux*, not 90); the interlinear insertion is `… 65 9 80 38 119 29 44` (*de Clervant*, not 63) and its
   caret sits after 111 in line 6, so *mon-si-[eur de Clervant]-est obligé*; `1579` at line 9 of f. 233 is *15 79* or the year.

## What the letters say

Navarre, October 1585 (a month after the bull of excommunication and the loss of his Guyenne places to Mayenne's army), tells
Ségur in Germany to conclude promptly with whoever he judges fit, if possible with Duke [John] Casimir or with his consent, to
raise the largest levy he can and to march it at once; he is writing to Clervant to raise the two thousand reiters he is
bound to furnish under the contract with the Churches, or part of them, using the ten thousand écus from [180] if he has no
other means; and he wants to know the route the army will take — the Vivarais or Dauphiné roads would suit. In February 1586
from Montauban: spare no means, succour us in all diligence, set every piece in motion, commit everything to it. On 1 April
1586 (slip): he is in extreme anxiety at having no news since [e], does not know where or to whom to write nor how their
affairs stand; make, if you can, the greatest levy ever made; the two thousand reiters Clervant is bound to furnish are very
necessary to us, and even more [H] [L]; assistance and succour are very necessary; our places are well fortified; we have
sent [someone] to … of whom we have long had no news. The postscript hand *D.* on f. 239 adds Drake's "very great prize" (the
sack of Santo Domingo, January 1586) — *le premier homme de marine … qui soit au monde*. All consistent with the German levy
of 1586–87 that Ségur, Clervant and Casimir were negotiating (Segesser, *Ludwig Pfyffer*; de Thou; the Ségur négociation
volumes themselves), which marched in 1587 to the disaster of Auneau. *Inferences, not readings: 180 = the Queen of England
(Elizabeth's subsidy for the levy); H, L = Hollande, Lorraine or similar.*

## Not done / open

- The word-signs (X, gla, gne, gna, pe, pu, e, H, L, Ne, qua, Ra, and now gu) and numbers 180, 215?, 900: the sweep below found
  no further secretary letter in this key, so a gloss must come from the key sheet (not in this volume) or from the second
  volume of the Ségur négociation (500 Colbert 402, not fetched).
- f. 143 (1583): 58 numeric tokens in a different key of the same design; not attackable at this length.
- f. 366 (below): 24 tokens in Navarre's own hand, probably this key; two of the three lines do not read as French.
- f. 321: not re-transcribed token by token (struck-through figures, see below); f. 333 is read with Tomokiyo's key and
  extends it.
- Misreadings I may have made: 93 (*nuine* for *peine*, 95), 66 (*pie-bes* for *pieces*, 60/61), 28 (*emlises* for
  *Eglises*, 18), the 20/10 question. All flagged in `reading.md`.

## Sweep of the volume, ff. 321/333, f. 366 (2026-09-16, later)

**Sweep.** All 440 canvases of 500 Colbert 401 were fetched at 1400 px (`fetch_sweep.py`, `sweep/`, git-ignored) and read
two to a contact sheet at 900 px (`mksheets.py`, `fixsheets.py`, `sheets/`). Cipher occurs on exactly six leaves: the four
on Tomokiyo's list (ff. 143, 233, 239, 288v), his two Henry-III items (ff. 321, 333), and **one leaf he does not list,
f. 366 (canvas 406)**, an autograph letter of Navarre to Ségur with three short cipher lines at the foot. Everything else
in the volume is clear text: Ségur's Latin and French memorials to the princes, letters of Walsingham, Casimir, the
Landgrave, the Hanse towns, Duplessis-Mornay, Clervant, Turenne, Catherine de Bourbon, Pallavicino, and nine further
autograph or secretary letters of Navarre in clear (ff. 88–89, 113, 160, 170, 343, 367–370, 375). The figures on f. 227 are
sums of money; the *8 8 8* on f. 158 is Duplessis's sigla. So there is no fourth secretary letter in the ff. 233 key in this
volume, and the word-signs cannot be glossed from it.

**f. 333 (canvas 369) read with Tomokiyo's f. 321 key.** Transcribed at 2× (`ct_333.txt`, 121 tokens, superscript 31 after
52 in line 4). Tomokiyo's table (`key_321.json`: a 12–14 … u 53–55, et 62, syllables ba–vu 63–142 in sixteen rows b c d f g
h j l m n p q r s t v) reads it almost completely: *[162] desire fort d'avoir des nouvelles de [204] de [189] [190] … et
leur advis sur le chemin [qu'i]l doit tenir et comment. … [167] assurer qu'aussi tost que les reistres marcheront il montera
à cheval; [166] et son frere sont de bonne volonté; il fault avancer la levée et la faire marcher le plustost qu'on pourra.*
The reading forces three values Tomokiyo left blank, **24 = f** (*frere*), **34 = l** (*il*, *montera*), **36 = m**
(*comment*), and shows 61 = et as well as 62. With those the f. 321 key is the ff. 233 key shifted: letters +8 (a 12–14, b
15–16, c 17–18, d 19–20, e 21–23 …, u 53–55, x y z 56–59, et 60–62) with three of Tomokiyo's assignments (19 = d, 20 = e,
26 = f) sitting one place off that pattern, and a syllabary that adds *h* and *j* rows. Five figures in f. 333 disagree
with the French and were confirmed at 2× as written (55 in *advis*, 19 and 31 in *à cheval*, 88 in *fault*, 20 in
*marcher*): the encipherer's slips, or homophones the pattern does not predict. f. 333 is a news-sheet in the third person
(*Le Roy de Navarre a envoyé … le Sr de Vesin de la Marsilliere à Berne*) signed *Henry* at La Rochelle, 10 July 1586 and
countersigned; 162 = *Le Roy de Navarre* is the king's own sign in his own cipher.

**Blind annealer on f. 333** (`run_333.log`, BLOCK0 = 63, NBLK = 16, 12 seeds × 300 000 steps, clear French as context):
58 letter tokens over 27 symbols and 44 syllable tokens. No two seeds agree (best −1125.2, scores spread over 14 nats);
the best key has 35 of 58 letter tokens and 3 of 16 blocks right against `key_321.json`. Seed 8 alone produced *son frere
sont de bonne volonté* and *doit tenir*. So f. 333 on its own is below unicity for this method, as the du Croc and Moray
items were at that size; the key stands on the f. 321 interlinear (Tomokiyo) and on the French it produces in f. 333.

**f. 321 (canvas 359).** Every cipher figure is struck through by the decipherer's pen and glossed between the lines. At
2.4× the strike-through swaps 4/9 and 3/8 systematically (*le chemin* came out 44 17 84 105 98 where the key wants 99 17
89 105 38), so a figure-level transcription would only be the interlinear reading fed back to itself. Not re-derived;
recorded as Tomokiyo's ground truth. The letter is addressed to Clervant, Buhy(?) and Ségur as *conseillers en mon conseil
d'estat et surintendans de ma maison et finances*, i.e. Navarre's council, which settles the sender question for that
pair of letters as well.

**f. 366 (canvas 406), the new item.** Autograph letter of Navarre (*Mons.r de Segur, j'ay fait tout ce que j'ay peu
suivant l'avis que m'avez donné pour essayer de retenir ou prolonger la paix … on a fait avancer l'armée et les forces
contre moy pour donner plus de moyen et authorité aux estrangers contre les enfans de la maison … d'user de toute la
diligence que vous pourrez pour effectuer ce dont je vous ay chargé*; undated, the peace talks and the advancing royal army
put it in the autumn of 1586). Three cipher lines at the foot, each with a marginal mark (+, +, n):

```
106 13 9 20 4 47 16 70 30
105 65 68 96 30 gu 79 100
15 41 10 106
```

The figures 4, 9, 10, 13, 15, 16 sit below 12 and so exclude the f. 321 key (where 1–11 are doubles and nulls); the
letter-written sign *gu* belongs with *pi, na, gne, gna, gla, qu, qua* of the ff. 233 key. With that key line 3 reads
**escri** and lines 1–2 read *ri-e-c-h-a-v-f-fe-n* and *re-de-du-pi-n {gu} la-que*: not French, most likely proper
names in the king's phonetic spelling (a German place or captain? *Riechauffen*), or a memorandum of nomenclature for the
marginal signs. Both keys' renderings come from `decode.py` on `ct_366.txt`. Left open; 24 tokens.

**Design-constrained annealer: f. 333 re-derived blind** (`solve_mono.py`, `eval_mono.py`; logs `run_mono333.log`,
`run_mono_control5.log`, `run_mono233.log`). The free homophonic annealer fails at f. 333's size (above), but the two keys
share a design, and the design can be built into the search: if the letter figures LO…HI are homophones **in
alphabetical order**, the letter key is nothing but a vector of homophone counts (0–4 per letter, a leading and a trailing
null slot capped at MAXNULL figures together, an *et* slot), and the moves shift one figure from one slot to the next.
The syllable blocks stay as before; the clear French stays as context; a dropped letter costs 6 nats.

- **f. 333 alone** (58 letter tokens 12–62, 44 syllable tokens, 16 blocks, 8 seeds × 150 000 steps): every finished seed
  converges on the same key at −1160.8: a 12–14, b 15–16, c 17–20, d 21, e 22–23, f 24, g 25–28, h 29, i 30–32, l 33–34,
  m 35–36, n 37–38, p 39–41, q 42–45, r 46–47, s 48–50, t 51–54, u 55, z 56–58, et 59–62. Against `key_321.json`
  (Tomokiyo's table plus the four values f. 333 forced) that is **54 of 58 letter tokens, 93.1 %**; the syllable side is
  weaker, 28 of 44 tokens and 7 of 16 blocks (l, m, s, r, h, c right; the *v* row comes out *t*, so *cheval*, *volonté*,
  *avancer*, *levée* read *chetai*, *tolonse*, *atancer*, *letee*). The text: *les reistres marcheront il mon[t]era a
  che[v]a[l] … et son frere sont [de] [b]on[n]e [v]olon[t]e il [f]aut a[v]ancer la le[v]ee et la faire marcher*. So the
  letter key of f. 321/333 is recovered from f. 333 alone once the chancery's alphabetical design is assumed, and it
  agrees with Tomokiyo's interlinear-based table; the blind run also fixes 20 as *c* (the *marcher* problem above) and
  puts *et* at 59–62, i.e. both 61 and 62.
- **Matched control of the same shape** (`control5.txt`, `control.py` with `ALPHA=1`: a Catherine de Médicis passage
  under a random alphabetical key on a random contiguous run of figures, same token counts as f. 333): 7 of 8 seeds
  agree, **36 of 40 letter tokens (90 %)**, 45 of 52 syllable tokens, 9 of 16 blocks. The method works at this size when
  the design assumption is right, and the f. 333 result is not a fluke.
- **Sanity on the ff. 233 set** (294 letter tokens 1–53, 14 blocks): the constrained run recovers the whole letter key
  from seed 0 (a 3–6, b 7–8, c 9–10, d 11–12, e 13–16, g 17–18, h 19–21, i 22–24, l 25–26, m 27–28, n 29–30, o 31–33,
  p 34–35, q 36–37, r 38–39, s 40–42, t 43–44, u 45–47, x 48, y 49–50, z 51, et 52–53), the only slips being *f* 16–17
  absorbed into *e* and *g*, and 3 and 53 mis-slotted: scored against `key_v4.json`, **287 of 290 letter tokens (99.0 %)**,
  150 of 165 syllable tokens, 11 of 14 blocks, two seeds agreeing at −6275.2 (the free annealer's blind key had 88.9 % /
  90.9 % / 11 of 14).

The order of attack for this cipher family is therefore: residue test for the syllabary → free structured annealer if the
text is long (≥ ~450 tokens) → alphabetical-count annealer if it is short (≥ ~100 tokens with clear context). f. 321 was
not run: its figures cannot be transcribed independently of the interlinear reading (see below).

**Word-signs ranked by the language model** (`gloss_signs.py`, `gloss_check.py`, outputs `glosses.txt`,
`gloss_check.txt`). For each letter-written sign every occurrence is rendered with a candidate word in place and scored by
the 5-gram model over 40 letters of context each side; the candidates' scores are summed over occurrences. Against the
600 most frequent corpus words nothing beats deleting the sign, which a no-space model always favours, so only the
like-for-like comparisons of the reading's own hypotheses mean anything, and there the margins are a few nats:

| sign | occurrences | hypotheses in order of likelihood (nats relative to deletion) |
|---|---|---|
| na | 3 | lettres −18.0, nouvelles −21.4, gens −21.8, affaires −23.9, forces −24.9 |
| gne | 2 | de −3.8, je −7.8 (the f. 288v occurrence opens a sentence, so *de* is excluded there and *je* stands) |
| gna | 1 | de −1.1, a −4.3, de nous −6.1, vous −6.2 |
| X | 1 | de −1.4, et −1.8, a −3.7, pour −4.1 |
| gla | 1 | de +1.3, et +0.4, a 0.0, pour −0.3, par −1.0, selon −5.9 |
| pe / pu | 1 | pe: que −0.1, quand −4.1, si −6.0, ou −11.9; pu: luy −2.4, vous −3.1, nous −5.8 |
| H, L | 1 | france −2.8, esté −4.0, espagne −4.9, angleterre −6.1, suisse −6.8, lorraine −8.3, allemagne −8.4, hollande −13.9 |
| qua | 1 | qui −2.4, me −6.1, nous −6.3, que vous −7.3 |
| Ne | 1 | en −4.8, nous −5.0, et −6.3 |
| 180 | 1 | catherine −1.1, la royne −4.1, la rochelle −6.3, angleterre −6.8, la reyne −7.5, casimir −10.9, elisabeth −12.8 |
| 900 | 1 | je −0.7, de −1.1, vous −3.2, nous −4.8 |
| e | 2 | six mois −16.4, decembre −17.0, novembre −17.1, longtemps −17.8, angleterre −18.6 |
| 215 | 1 | en −3.8, ne −4.0, il −6.6, l −7.0 |

What this supports: *na* is a plural noun of the *lettres / nouvelles / affaires* class (the model slightly prefers
*lettres*, which fits *n'avoir eu de vos [lettres]* twice but not *en quel estat sont nos [lettres]*, so the reading keeps
*affaires* / *nouvelles* as the pair); *X*, *gla*, *gna* are short function words (*de* leads each time); *pu* is a
pronoun (*luy* / *vous*); *H* and *L* are names, with nothing to choose between the countries; 180's top candidate is
*Catherine* only by 3 nats over *la royne* on a single occurrence, which is not evidence for either. The signs stay open;
the table records what the model can and cannot say.

**Matched control at f. 333's size** (`control4.txt`, `run_control4.log`; `control.py` now takes `CTFILES`): a Catherine
de Médicis passage enciphered with a random key of the sixteen-row shape, 59 letter tokens over 24 symbols and 44 syllable
tokens, the same clear-text interleaving as f. 333. Twelve seeds spread over 10 nats with no agreement; the best key has
37.3 % of the letter tokens and 3 of 16 blocks right, the same figures as the blind run on f. 333 itself (35/58, 3/16). So
the failure on f. 333 is the size, not the transcription; the method's floor for this design lies between 120 and 460
tokens.

**Other volumes.** 500 Colbert 402 (the second Ségur volume, 1587–88) is not on Gallica (SRU search on title and on
"Segur"/"Pardaillan", 2026-09-16). BnF fr. 17820, *Lettres du roi de Navarre envoyées en Allemagne aux princes protestans
de la Confession d'Ausbourg* (1583–85, 211 canvases, ark btv1b90620099), was fetched and its opening leaves read: it is an
eighteenth-century fair copy (Coislin collection) of the 1583–84 letters and instructions, all in clear, with a table of
contents of diplomatic texts only; a copyist would not have kept cipher figures, so it was not swept further. BnF
Dupuy 407, *Recueil de lettres … pour la plupart autographes ou originales, émanant de Henri IV* (btv1b10035037p, 320
canvases, `fetch_sweep3.py`, `sweep3/`, `sheets3/`), was fetched and read to canvas 46: it is chronological, the 1580s
occupy the first two dozen leaves (autographs of Navarre to Henry III, Catherine de Médicis and, at f. 13, **to Ségur,
Lectoure 26 June 1585, in clear**), and from f. 24 on it is the 1590s and Marie de Médicis; no cipher, download stopped.
Surfaced by the search and not yet looked at: fr. 3985, and the printed *Accort et capitulation faict entre le roy de Navarre et le duc de Cazimir pour la levee de l'armee des
reistres* (1587, bpt6k79516b), which is the contract the October 1585 letter refers to.

**f. 321 at 3×.** One segment is clean of strike-through and confirms the key against the interlinear *et s'il fault*:
`61 130 33 78 54 52` = et si l fa u t. Elsewhere the strike-through still turns 9 into 4 and 3 into 8 (*le chemin* read
44 17 84 105 98 for 99 17 89 105 38), so the leaf stays unretranscribed.

**f. 321, strike-through removal tried.** Long horizontal dark runs (≥ 45 px at full resolution) were detected and blanked in
the cipher block (`crops321/f321_destriked.png`, local). The decipherer's stroke runs through the middle of every figure,
so removing it removes the digit cores as well; only figures the stroke missed survive (162; *et s'il fault* = 130 33 78
54 52; 139 18 114 53; 50 24 55 12; 20 89 126 38 …). A figure-level transcription of f. 321 independent of the interlinear
reading is not obtainable from this image; a re-derivation of f. 321 would need the leaf itself or a raking-light scan.

**Correction to step 1 above.** The five "alignments" of the residue test are cyclic shifts of one count: the residue
classes of the figures 54–123 carry 27 / 67 / 31 / 26 / 14 tokens (165 in all), and the class with 67 (41 %) is the *e*
slot, which fixes the table start modulo five (54 ≡ 4 mod 5). The start itself (54 rather than 59 or 64) came from the
reading, as step 4 says.

**Checked:** every canvas of the volume at 900 px, with the even canvases of solo sheets re-paired (`fixsheets.py`); the
f. 333 figures at 2×; the f. 366 figures at 3×; Tomokiyo's table against f. 333 word by word. **Not checked:** 500 Colbert
402 (the second Ségur volume, not digitised) for further letters in this key; fr. 3985; Dupuy 407 beyond canvas 46 (1590s); Tomokiyo's f. 321 table figure by figure against the leaf;
the identity of 189/190/204/166/167 in f. 333. **User must verify:** the dating of f. 366 and the reading *escri* before
either is quoted.

## Files

- `ct_233.txt`, `ct_239.txt`, `ct_288.txt`, `ct_143.txt` — transcriptions with clear text in brackets.
- `key_v4.json` — the key (letters, blocks, glossed glyphs); `key_v1.json` the blind annealer's key; `decode.py key_v4.json`
  renders the letters; `decode_v4.txt` its output; `reading.md` the edited reading with token notes.
- `solve.py` (structured annealer; `BLOCK0`, `NBLK`, `NULLPEN`, `MAXNULL` env), `control.py`, `eval_control.py`, `load.py`,
  `crop.py`, `fetch_gallica.py`; logs `run_target.log`, `run_control1..3.log`, `run_target14.log`; `henryiii.htm/.txt` the
  cryptiana article as fetched.
- Sweep and siblings (2026-09-16, later): `fetch_sweep.py`, `mksheets.py`, `fixsheets.py` (contact sheets; `sweep/`,
  `sheets/`, `crops321/` git-ignored); `ct_333.txt`, `ct_366.txt`; `key_321.json` (Tomokiyo's f. 321 table plus 24 = f,
  34 = l, 36 = m, 61 = et); `run_333.log` (free annealer on f. 333, negative); `control4.txt`, `control5.txt` (matched
  controls, random and alphabetical keys); `solve_mono.py`, `eval_mono.py` (design-constrained annealer and its scorer;
  `run_mono333.log`, `run_mono_control5.log`, `run_mono233.log`); `gloss_signs.py`, `gloss_check.py`, `glosses.txt`,
  `gloss_check.txt` (word-sign likelihood ranking).

Checked: transcription of the three letters at full resolution and 2× re-reads of disputed digits; mod-5 structure; three
matched controls; convergence over seeds; alphabetical order of the recovered key; word-level French of every cipher span.
Not checked: the f. 321 key against Tomokiyo's table token by token; the identity of the word-signs; the historical glosses
(Casimir, Clervant, the 1579 contract, Drake). User must verify: the sender attribution before it is reported to Tomokiyo,
and the readings marked ? before they are quoted.
