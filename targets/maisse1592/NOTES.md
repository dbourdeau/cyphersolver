# Henri IV to Maisse (Venice), four ciphered letters — BnF fr. 16093 ff. 370, 373, 406, 410

Catalogue no. 17 (priority 5.0, class B). Opened 19 Sept 2026.

Status: read (23 Oct 2026, r2l: f. 373's cipher transcribed group by group and aligned with its copy, so both letters
are measured; before: in progress).

23 Oct 2026, r2l (REREAD_BRIEF): **f. 373's figures transcribed and aligned with the copy.** f. 373r-v fetched again at
full size (openapi.bnf.fr views 422-423), deskewed, every line cut in four quarters (`research/reading_audit/r2l_lines373.py`,
`r2l_q373.py`) and read figure by figure against the Brienne copy enciphered with `key1.tsv` (`r2l_pred373.py`),
recording the figures where they differ: `texts/f373_figures.txt` (built by `r2l_fig373.py` from the line spec
`texts/f373_figures_spec.txt`), **3,958 groups in 66 lines** (recto ll. 3-53, verso ll. 1-15; b29 had counted about 42 + 11
lines), 36 doubtful, 3 struck. Aligned with the copy by `research/reading_audit/r2l_align373.py` ->
`texts/f373_figures_vs_copy.md`: **3,972 of the 4,062 copy letters of the cipher passage agree (97.8%)**, 29 substituted,
48 missing from the figures, 13 in code 24 (Roy d'Espagne, f. 373r l. 14). The figures differ from the copy in wording at
*vous pouvez tascher de* (copy *pourrez tascher a*), *fort bon* (*tres bon*), *asseurer ce faisant* (*en ce faisant*),
*Verac sa partialité* (no *et*), *combien qui* (*qu'il*), *par faulte d'estre* (*d'y estre*), *le moien que j'ay*
(*que j'y ay*), and in spelling throughout (*atendre, moiens, devoir, amys, ruine, reduit, acabler, cheute, flaterie,
ceste, cogneues, oultre, laquele, cele, ceulx, aider, contraint, commancement, infaliblement ...*); the reading
`texts/f373_reading.md` now follows the figures there (v2_score 0.913 plain, 0.957 explicit holes). Caveat: the figures
were read against the enciphered copy, so agreement is partly by construction; the 77 differing words are what the image
shows. fraction_read 0.99 (estimated) -> **0.999 measured** (6,250 of 6,251 visible cipher groups: f. 370 2,293, f. 373
3,958; group 90 unread). Class read in part -> **read**.

23 Oct 2026, independent second reader (sr): **blind re-transcription of a sample of f. 373.** Six lines drawn with
`random.seed(373)` from recto ll. 3-53 and verso ll. 1-15 (**r07, r15, r17, r18, r48, v13**, 366 groups) read group by
group from Gallica views 422-423 at full size (openapi.bnf.fr IIIF; crops in the session scratchpad only), decoded with
`key1.tsv`, without opening `texts/f373_figures.txt`, the Brienne copy or its enciphered form. Compared group by group
(`texts/f373_sr_blind.txt`): **342 groups agree, 94.1% independent agreement** (Dice on 366 vs 361 groups; per line
r07 95.4%, r15 92.7%, r17 97.5%, r18 97.6%, r48 95.7%, v13 84.7%). Every difference re-checked on the image falls on the
blind reader's side (v13 "par deca que vous" skipped, r48 "aduiserez" read as "aduisement", r15 "faire", r18
"pourueu", two crop-overlap repeats), so the figures file stands and the 97.8% agreement with the copy is not only by
construction. The reading still rests on the copy for the wording; the sample confirms the figures carry it.

23 Oct 2026, r2f (REREAD_BRIEF): **f. 370's figures aligned with the copy.** The whole cipher passage of f. 370r-v
transcribed group by group from openapi.bnf.fr views 419-420 (`texts/f370_figures.txt`, 2,293 figure groups measured,
63 lines), decoded with `key1.tsv` and aligned letter by letter with the Brienne 13 copy (now kept separately as
`texts/f370_brienne_copy.txt`) by `research/reading_audit/r2f_align370.py` -> `texts/f370_figures_vs_copy.md`. The
alignment spans the whole copy, so the copy is this letter, and the key holds: **2,255 of the 2,310 covered copy letters
agree (97.6%)**; 147 copy letters lie where the verso line ends run into the binding gutter. The reading
(`texts/f370_reading.md`) now follows the figures where they differ in wording (*vouldriez* for *vouldrez*, *ou
restraigniez* for *et retranchiez*, *concernans* for *qui concernent*, *traictees*, *lesquelz* for *desquelz*, *si
c'estoit* for *s'il estoit*, *vengez* for the copy's doubtful *vangez*) or spelling (*besoing, habandonnées, suyvy,
affin, connoissance, ceste ...*), and keeps the copy over evident enciphering slips (*sois parsz sisost* for *soit
passé sitost*, *seulerent*, a doubled *apres*). v2_score 0.979 plain, 1.0 explicit holes; English `texts/f370_en.md`.
Key extended (`key1.tsv`): 71 = rr, **73 = tt** (was entered as uu; *a 73 endant*), codes 23 = pape, 24 = Roy d'Espagne,
48 = ambassadeur, 49 = guerre; 90 (once) unidentified. f. 373: the copy's doubtful words checked on the figures:
*Vivac* = **Verac**, *chauvez* = **charmez**, *sainement* confirmed. Neighbouring leaves ff. 367-369, 371-372 are clear
despatches (no second-route duplicate of f. 370). profile: key recovered (key_file key1.tsv), fraction_read about 0.99
(f. 370 measured, f. 373 estimated). Class stays read in part only because f. 373's group count is estimated (its cipher
is not transcribed group by group); every remaining gap has an outside blocker.

23 Oct 2026, re-read (REREAD_BRIEF, batch b29): **f. 373 read** from the contemporary clear copy. Brienne 13 fol.
104v-106v (Gallica btv1b100904592 views 109-112) transcribed in full (`texts/f373_brienne_copy.txt`); f. 373r-v fetched at
full size (views 422-423) and the copy checked against the figures with `key1.tsv` at five places, no disagreement; the
original's clear close and a clear postscript the copy omits (Joyeuse's defeat and death at Villemur, Oct 1592) read from
the original. Reading `texts/f373_reading.md` (0.924 clean sentences; explicit holes 0.978), English `texts/f373_en.md`,
log `texts/f373_reread_log.md`. fraction_read about 0.06 -> about 0.87 (estimated); class stays read in part (the rest of
f. 370 is still not transcribed).

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read**: the transcribed
opening of f. 370 (80 groups, identical with Brienne 13 fol. 102v). **Not read**: the rest of f. 370 (about 550 groups)
and all of f. 373, neither transcribed, and neither Brienne clear copy is transcribed (f. 373 marked "decoded, not
read" in profile.json). This answers the open question below: 1.0 does not stand; class read -> read in part,
fraction_read about 0.06 (estimated).

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. This entry now keeps
**ff. 370 and 373, Maisse's Cipher (1592)**. ff. 406 and 410 (with f. 404, f. 412) are in Maisse's Cipher (1592-1593),
a different cipher, with its own page ([`targets/maisse1593/`](../maisse1593/), docs/maisse1593.html); Tomokiyo's key
image for it (`src/henryiv_Maisse2.png`) moved there. The notes below cover the whole catalogue item and stay here as
the record; the fetch scripts and the git-ignored images (`img/`, `br/`, `src/`) serve both entries.

Open question (22 Sept 2026, site review): profile.json has class read, fraction_read 1.0, but the key was checked
letter for letter on f. 370 only (81 characters); ff. 373, 406 and 410 were read from the Brienne clear copy, not
deciphered from the cipher. Decide next time whether 1.0 should stand, or whether the other three leaves should be
deciphered with the key and measured. Written up as `docs/maisse1592.html`.

## 1. What the catalogue said, and why it was wrong

`catalogue.json` scored this "these four use a different key with no sibling found yet" and classed it **B**.
Both halves of that are wrong, and the error came from reading Tomokiyo's list as one group of four.

Tomokiyo's Henri IV page (`../../research/gallica_sweep/src/henryiv.txt`, lines 127-177) splits fr. 16093 into cipher
periods. The four "undeciphered" leaves fall in **two different sections**:

| leaf | date | Tomokiyo's section | siblings in the same volume |
|---|---|---|---|
| f. 370 | 3 Nov 1592 | *Maisse's Cipher (1592)*, ll. 127-143 | ff. 304, 307, 317, 323, 327, 328 |
| f. 373 | Nov 1592 | *Maisse's Cipher (1592)* | idem |
| f. 406 | Feb 1593 | *Maisse's Cipher (1592-1593)*, ll. 144-177 | ff. 344-444, incl. **ff. 398, 401, 402, 404 with partial interlined decipherings** |
| f. 410 | Apr 1593 | *Maisse's Cipher (1592-1593)* | idem; **f. 412 is a duplicate of f. 410** |

So each target has siblings in its own volume, and the 1592-93 group has sibling leaves that carry a
contemporary decipherment between the lines. This is class **A** (key recoverable by alignment), not B.

Confirmed on the images: f. 370 is a **pure figure cipher** (two-digit numbers, 1-99); f. 404 (same family as
ff. 406, 410) mixes figures with letter-shaped symbols. Two distinct systems, as Tomokiyo says.

## 2. Shelfmark, ark, and the folio -> canvas map

fr. 16093 = **ark btv1b90074656** (`Dépêches originales de la Cour à André Hurault de Maisse`), 558 canvases,
originally **Harlay ms. 1024**. The catalogue entry had no ark; resolved by Gallica SRU
(`dc.type all "manuscrit"` + `gallica all "Francais 16093"`).

Canvas labels are all `NP`, so the folio map was calibrated by reading folio numbers off the leaves.
**Each canvas is an opening**: canvas *N* shows f.(N-offset) recto on the right and the preceding verso on the left.
The offset is not constant (unfoliated leaves intervene):

| folio | canvas | offset | |
|---|---|---|---|
| f. 362 | 410 | +48 | Tomokiyo's f.362, "A Champs 30 Sept. 1592" |
| f. 369 | 418 | +49 | |
| **f. 370** | **419** | +49 | target 1 |
| **f. 373** | **422** | +49 | target 2 |
| f. 404 | 455 | +51 | crib, partial interlinear decipherment |
| f. 405 | 456 | +51 | continuation, cipher block |
| **f. 406** | **457** | +51 | target 3 |
| **f. 410** | **461** | +51 | target 4 |

`fetch.py` takes canvas indices; `fetchr.py` takes the same and crops a page region (`REG=pct:48,0,52,100`
is the right-hand page).

## 3. The break: the old pièce numbers are the edition's citation key

Every leaf carries, top right, an **old Harlay pièce number** above the modern folio number. Berger de Xivrey,
*Recueil des lettres missives de Henri IV*, cites letters by exactly that number
("B. R. Fonds Saint-Germain-Harlay, Ms. 1024, pièce N"), and for most of them also gives
**"Cop. — Fonds Brienne, Ms. 13, fol. N"**. Read off the images:

| leaf | pièce | Xivrey's clear copy |
|---|---|---|
| f. 370 | **224** | Brienne Ms. 13, fol. **102 verso** |
| f. 373 | **226** | Brienne Ms. 13, fol. **104 verso** |
| f. 404 | 247 | Brienne Ms. 13, fol. 171 recto |
| f. 398 | 244 | Brienne Ms. 13, fol. 156 recto (letter printed in full, t. III p. 719) |

Tome III is Internet Archive `recueildeslettre03henr` (`src/lm3.txt`). Its appendix
"Table de plusieurs lettres non imprimées dans ce volume" (from line ~43390) lists the despatches Xivrey did
*not* print, each with its Harlay pièce and Brienne folio; that is where ff. 370 and 373 appear.
For the letter he did print (p. 719 = f. 398) he notes: *"La partie en italique est chiffrée dans l'original
et déchiffrée dans la copie du fonds Brienne."*

**Fonds Brienne Ms. 13 = BnF NAF 6984 = ark btv1b100904592**, `COLLECTION DE BRIENNE. 11-13 ... 13 III.
Années 1592, juin-1594, avril`, 335 canvases. It is a clean 17th-century clerk's copy, fully legible, and it
copies these despatches **in clear, including the passages the originals encipher**.
Brienne 11 = NAF 6982 (btv1b525122596), Brienne 12 = NAF 6983 (btv1b525122611).

Brienne folio -> canvas: canvas *N* right page = fol. (N-5) recto, left page = fol. (N-6) verso.
So **fol. 102v = left page of canvas 108** and **fol. 104v = left page of canvas 110**. `fetchb.py` fetches them.

### Confirmed match for f. 370

Brienne 13, fol. 102v (canvas 108, left) is headed

> *Autre coppie de lettre du Roy audict sieur du troisiesme 9bre par ledict Lambert.*

and opens with the same words as the clear preamble of f. 370:

> *Mons.r de Maisse, En mesme temps qui n'est que depuis trois jours, j'ay receu les duplicatas de vos
> depesches du mois d'aoust, et celles des six et dixneufiesme septembre par trois divers messagers que le
> maire de Langres m'a envoiez...*

f. 370 breaks into cipher at *"...ou la plus part des lettres se perdent."* The Brienne copy runs straight on
in clear: *"Le Cardinal de Bondy aura passé près de vous... suivy par le marquis de Pisany pour aller vers le
Pape au nom des Catholiques de ce royaume mes serviteurs..."*

That is a full known-plaintext for the 1592 cipher.

## 4. Plan

1. Transcribe the ciphertext of f. 370 and the Brienne clear text of fol. 102v-103r. Align -> key.
2. Verify the key on f. 373 against Brienne fol. 104v, and read it.
3. Locate the Brienne copies of ff. 406 and 410 (Feb and Apr 1593) and repeat for the 1592-93 cipher,
   cross-checked against the interlinear decipherments on ff. 398-404 and against the f. 412 duplicate of f. 410.
4. Grade every group (H/C/M/I per the repo convention) and write up.


## 5. Result: all four letters are read

Every one of the four "undeciphered" leaves has a **contemporary deciphered clear copy in Brienne 13**
(NAF 6984, ark btv1b100904592). Each was located from its Harlay pièce number via Xivrey's table and then
confirmed on the image by heading and by the wording of the clear preamble shared with the original.

| target | date on the original | pièce | Brienne 13 | canvas / page | confirmed by |
|---|---|---|---|---|---|
| **f. 370** | S. Denys, 3 Nov 1592 | 224 | fol. **102v** | 108 left | heading *"Autre coppie de lettre du Roy audict sieur du troisiesme 9bre par ledict Lambert"*; preamble identical |
| **f. 373** | 7 Nov 1592 | 226 | fol. **104v** | 110 left | heading on fol. 104r *"Autre lettre du Roy du sept.e novembre mil cinq cens quatre vingtz douze"* |
| **f. 406** | Chartres, 8 Feb 1593 | 247 | fol. **171r** | 176 right | heading *"Coppie de lettre du Roy audict sieur de Maisse de Chartres le huictiesme febvrier 1593, receue le viii.e d'Avril"*; preamble identical |
| **f. 410** | Mantes, 27 Apr 1593 | 251 | fol. **193v** | 199 left | heading *"Mante le vingt huictiesme Avril 1593, receue le vingt douxiesme May"* |

### A correction to Tomokiyo's list

Tomokiyo lists f. 404 (*"only partial interlined deciphering"*) and f. 406 (*"undeciphered"*) as two letters.
They are **the same despatch**: Chartres, 8 February 1593. f. 406 is the duplicate sent by the second route —
Henri IV routinely sent these by *"double voye"*, and f. 404 says so in clear. The two leaves open with the
same words, carry the same date, and Brienne 13 copies the letter once, at fol. 171r, under pièce 247.
So f. 406's plaintext is attested twice over: by the Brienne copy and by the interlinear decipherment on f. 404.
Likewise f. 412 is the duplicate of f. 410, as Tomokiyo notes.

The four "undeciphered" leaves are therefore **four despatches** in two ciphers (f. 404 is not one of the four); what the duplicate changes is that f. 406 was deciphered at the time, on f. 404, so only three of the four were without a contemporary decipherment. (Corrected 22 Sept 2026: this line earlier said "three distinct despatches".)

### What the letters say

- **f. 370** (3 Nov 1592, S. Denis). Cardinal de Gondi has passed near Venice, shortly to be followed by the
  **marquis de Pisany**, going to the Pope in the name of the Catholics of the kingdom — the embassy that
  prepared Henri's absolution. The King presses Maisse not to leave his post; the house of Austria; the King
  of Spain's ambition "qui se desborde"; Mayenne, having broken up his army, has slipped into Paris with a
  handful of horse and found the people "si las et ennuyé de la guerre et de la vanité des promesses passées"
  that they are in "grand garbuge", inclining to peace and against "l'introduction de l'Espagnol".
- **f. 373** (7 Nov 1592). Acknowledges Maisse's letter of 4 October; the King will suspend final judgement
  until he sees what comes of the Gondi and Pisany missions; appeals to his Catholic friends' own interest,
  against the ruin the length of the war and the King of Spain's efforts have brought.
- **f. 406 / f. 404** (8 Feb 1593, Chartres). The King has answered every despatch and docketed the dates so
  Maisse can tell what is lost; the Spanish insolence and the Pope; Pisany and Cardinal Gondi should not leave
  Rome; their going would be of importance, and their entry among those of the League could breed division.
  Contains in clear the sentence about **"le double du chiffre que j'ay envoyé aud. de Brèves"** — the same key
  Savary de Brèves used, which is why the 1592-93 cipher recurs in the Brèves correspondence.
- **f. 410** (27/28 Apr 1593, Mantes). Acknowledges Maisse's letters of 20 Feb, 7 and 23 Mar; the duc de Nevers
  held one courier in Champagne; warm assurance that Maisse's absence will cost him nothing in the King's
  favour; and that experience has proved Maisse's long-standing judgement of "les affaires de Rome" right.

## 6. The two cipher systems, and what is still open

Observed on the leaves at native resolution (fr. 16093 is scanned at 7029 x 6142):

- **Maisse's Cipher (1592)** — ff. 370, 373. A **pure figure cipher**: one- and two-digit numbers, values
  observed from 2 to 97, written with light spacing and occasional separating dots and short overbars.
  f. 370 carries ~25 lines of it. Frequent groups in the opening lines are 11, 19, 10, 7, 16, 13, 17, 5, so
  the system is homophonic rather than a plain 1:1 alphabet. Tomokiyo notes the overbar marks the usual
  scribal abbreviation inside the *plaintext* spelling (l[ett]res, occa[si]on, v[ost]re), not a cipher value.
  Savasse (1997) reconstructed this key independently from Maisse's own 1590 letters in the "Manuscrit Revol",
  recording code elements 23 = *votre Majesté / le roi*, 24 = *le roi d'Espagne*, 74 = *le grand-duc de
  Florence / Toscane*, plus nulls. Savasse's edition was not available here (marked * in the catalogue).
- **Maisse's Cipher (1592-1593)** — ff. 404/406, 410. A **mixed system**: letter-shaped symbols
  (w, d, l, p, b, y, g, z, long-s, and others) carry the letters, while two-digit figures carry the
  nomenclator; 27, 10, 26, 23, 19, 21, 22, 24 and 8 are the commonest figures on f. 404. This is the key
  Henri IV calls "le double du chiffre que j'ay envoyé aud. de Brèves" in the clear text of f. 404 itself,
  which is why Tomokiyo finds the same cipher in the Savary de Brèves correspondence of 1593-1596 and again
  between Brèves and Beaumont in 1602.

### The keys were already published - and they read these leaves

The catalogue entry said what to do first: *"Verify first. Savasse 1997; Tomokiyo's Maisse keys as a first
test."* That step was skipped at the start of this session because `research/gallica_sweep/src/henryiv.txt` is a **text
dump** of Tomokiyo's page and his key tables are **images**, so they were invisible in it. Fetching the page
itself (`src/henryiv.htm`, SHIFT_JIS) shows 62 `<img>` tags, two of them the keys:

- `henryiv_Maisse1.png` - *"Cipher used in BnF fr.16093 f.317"* = **Maisse's Cipher (1592)** = ff. 370, 373
- `henryiv_Maisse2.png` - *"Maisse' Cipher 2 (BnF fr.16093, f.344 etc.)"* = **Maisse's Cipher (1592-1593)** = ff. 406, 410

Both are in `src/`. Tomokiyo reconstructed the keys from the sibling letters but never applied them to the four
leaves he marked undeciphered. Applying them is what was missing.

### Maisse's Cipher (1592): the key, and the verified reading of f. 370

A simple substitution on a 22-letter alphabet (i=j, u=v), copied to `key1.tsv`:

```
a 7   b 8   c 9   d 10  e 11  f 1   g 2   h 3   i 4   l 5   m 6
n 12  o 13  p 14  q 15  r 16  s 17  t 18  u 19  x 20  y 21  z 22
ff 66   mm 67   nn 68   ss 72   uu 73
```

This is exactly the structure the blind frequency analysis had already found before the key turned up: 94 % of
groups in a near-contiguous band 1-22, commonest value at 14.5 % (= *e*, which is 11), a sparse nomenclator
above the band. That analysis stands as an independent confirmation of the key's shape.

`ct370.txt` is the hand transcription of the opening of f. 370 and `decode.py` applies the key:

```
5 11 9 7 16 10 4 12 7 5 | w 11 2 13 12 10 21 | 7 19 16 7 | 14 7 72 11 | 14 16 11 17 | 10 11 | 19 13 19 17
-> lecardinal d egondy   aura        passe      pres       de          uous
```

Decoded in full, the 81 characters transcribed give

> lecardinaldegondyaurapassepresdeuousilypeultiaauoirquelqueiourslequeluousaurafait

and Brienne 13 fol. 102v, normalised the same way (v->u, j->i, spaces dropped), gives

> lecardinaldegondyaurapassepresdeuousilypeultiaauoirquelqueiourslequeluousaurafait

**Identical, 81 of 81 characters.** The decipherment is therefore confirmed against a source independent of
the key: *"Le Cardinal de Gondy aura passé prés de vous, il y peult ja avoir quelque jours, lequel vous aura
fait [entendre de mes nouvelles]"*. Grade **H** for the groups in `ct370.txt` (read from a primary key source
and confirmed on a known-plaintext copy).

### One sign not in the published table

Between *cardinal* and *egondy* the leaf carries an **omega-shaped sign**, not a figure. It is not the pair
1-0, which occurs separately and repeatedly on the same lines. In context it can only be **d**, giving
*cardinal-d-e-gondy*; d also appears as the figure 10 seven words later, in *gondy* itself. So d has two
signs in this cipher, the figure 10 and the omega, and **the omega is absent from Tomokiyo's table**. That is
the one addition this session makes to the published key. Grade **C** (established from the known-plaintext
copy, not from a key source).

### What is not transcribed

f. 370 carries about 21 lines of cipher on the recto, roughly 630 groups by the segmentation in `seg2.py`;
81 characters of it are transcribed here. The rest reads with the same key - spot decoding of the next line
gives *auoir quelque iours lequel uous aura fait* against Brienne's *"avoir quelque jours lequel vous aura
fait"* - but it is not transcribed group by group, and neither is f. 373. For ff. 406 and 410 the key
(`henryiv_Maisse2.png`) is in hand but not applied: that cipher is homophonic, mixes letter-shaped symbols
with figures and carries word codes (*vous, ceulx, est, faict, de, des, fort, par, pour, que, qui, advis, ces,
comme, bon, avec, et, jay, les, luy, moy*), so transcribing it is a much larger job than Cipher 1.
The content of all four letters is in any case settled by the Brienne copies (section 5).

### Working files

`seg.py`, `seg2.py`, `boxes.py`, `zoom.py` - segmentation and reading aids; `glyphs.py`, `digits.py`,
`cluster.py` - the glyph-clustering route, built before the keys were found and left unfinished;
`align.py`, `align2.py`, `control.py` - the blind known-plaintext alignment, which failed at the noise floor
(12 groups placed against a shuffled-cipher control of mean 8.2, p95 11) because the transcription mis-split
*9 7* (c,a) as a single group *97* and because homophony was wrongly assumed. Kept as the record of the
attempt and as the matched control the repository's conventions require.

## 7. Files

- `fetch.py` / `fetchr.py` — fr. 16093 canvases and page regions (ark btv1b90074656)
- `fetchb.py` — Brienne 13 / NAF 6984 canvases (ark btv1b100904592)
- `montage.py` — folio-number corner sheets used for the calibration above
- `src/lm3.txt` — Xivrey, *Lettres missives* t. III (IA `recueildeslettre03henr`), gitignored

## 23 Oct 2026: verification 3 (explicit-hole score): f. 370 read from the Brienne 13 copy

f. 370 had only its 81-letter opening read (`texts/f370_decryption.md`, 0.545 explicit-hole as scored with its header
and comparison strings). Its contemporary clear copy, Brienne 13 fol. 102v-103v (pièce 224), is now transcribed for the
whole cipher passage from openapi.bnf.fr views 108-109: `texts/f370_reading.md`, 0.979 explicit-hole, 0.936 plain. The
passage runs from "Le Cardinal de Gondy aura passé pres de vous" to "... a la conservation de cette Couronne": on f.
370v (view 420) the original returns to clear with "depuis le partement", which follows those words in the copy. So
the cipher is longer than the "about 550 groups" counted on the recto: 35 more lines of figures on the verso (about
2,200 groups in all). Content: Gondi has passed near Venice, Pisany follows to the Pope for the Catholic royalists;
Maisse is to stay at his post; Lambert goes back to the Levant with Brèves's despatch, which Maisse may amend; the
advice to the English ambassador and Brèves on the Spanish intrigue at the Porte; Lesdiguières's war in Piedmont; the
Pope's resolutions awaited. Beyond the opening the reading rests on the copy alone (figures not aligned). fraction_read
0.87 -> 0.98, estimated.

## Independent verification by Brice Dudout (PR #570, 14 Nov 2026)

Brice Dudout (`VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) decoded both figure files with `key1.tsv` alone
and aligned the letters with the readings: f. 370 2,291 of 2,355 decoded letters (97.3%), f. 373 4,015 of 4,026 (99.7%).
Re-run here: the same. No new disagreement; `research/reading_audit/v10_relabel.py` gives the recorded read shares
(1.0 and 0.987).

He also made the first blind sample of f. 370 (f. 373 had one): five lines drawn with `random.seed(370)` (r30, v09, v10,
v25, v29), 182 groups read from Gallica views 419-420 before comparison, 177 agreeing (97.3%). The order of the work is
by his record. Three points come out of it; view 420 was fetched here (openapi.bnf.fr, full-size bands of v25 and v29):

- **v29, *contrainct*: the figure is 8, not `9?`.** Seen here: a closed 8 like the 8 of the 18 that follows. The
  encipherer wrote b for c. `texts/f370_figures.txt` now has `8`, and the slip is in the list of
  `texts/f370_figures_vs_copy.md`. The reading keeps the copy's word, as for the other slips.
- **v29, one more group at the gutter** (21, *luy*) after the last 19: by his reading. The band fetched here ends at that
  place and shows the start of a figure; the group is not added to the file.
- **The code for *pape* may be 25, not 23** (v25 and r06). Seen here at v25: the second digit has a looped top and a
  tail turning left, like the 5 of 15, and unlike the flat-topped 3 of the 73 and the 3 nearby. r06 was not found again
  here. The value is not in doubt (the copy has *pape* at both places). `key1.tsv`, the figures and the page still call
  the code 23; renaming it wants both places seen, and is left open.

## Remaining gaps

- f. 370: read 23 Oct 2026; figures aligned with the copy (r2f). Line ends of f. 370v hidden in the binding gutter (about 147 copy letters, the copy is the only witness there) - blocker: needs-physical-access; group 90 at the end of f. 370r l. 1, probably a null - blocker: too-short
- f. 373: closed 23 Oct 2026 (r2l: all 3,958 cipher groups transcribed and aligned with the Brienne copy, 97.8%). Clear postscript ll. 2 and 5 (not cipher) - blocker: illegible

## Escalation

Added by the reading audit (22 Oct 2026), which relabelled the documents that do not build sentences as decoded,
not read. None of these steps has been redone since; each is open for those documents.

- [x] siblings: other letters of the same series or key, read or deciphered at the time (23 Oct, r2f: neighbouring leaves ff. 367-369, 371-372 are clear despatches, no duplicate of f. 370; the key's own sibling, f. 317, is Tomokiyo's source)
- [x] clear-pages: clear, cleartext or postscript pages checked for being the decipherment (23 Oct: f. 373v clear postscript read; Brienne 13 copy of f. 373 transcribed)
- [x] known-keys: other keys of the same correspondents tried (23 Oct, r2f: Tomokiyo's 1592 key fits, 97.6% on f. 370; his 1592-1593 key has letter-shaped signs that ff. 370/373 lack; Savasse's codes agree on 24, not on 23; Savasse 1997 not available)
- [x] print: printed editions and calendars searched for these letters (Xivrey t. III lists f. 373 = pièce 226 as not printed; the Brienne copy is the text)
- [x] key-rebuild: the key corrected against the documents that read (23 Oct, r2f: 71 = rr, 73 = tt, codes 23, 24, 48, 49 added to key1.tsv)
- [x] retry: every decoded-not-read document re-read sentence by sentence against the images (23 Oct: f. 373, b29; 23 Oct r2l: f. 373's cipher transcribed group by group and aligned, 97.8%)
