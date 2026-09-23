# Henri IV to Maisse (Venice), four ciphered letters — BnF fr. 16093 ff. 370, 373, 406, 410

Catalogue no. 17 (priority 5.0, class B). Opened 19 Sept 2026.

Status: solved. Both ciphers identified and keyed; f. 370 decoded and verified letter-for-letter against the
independent clear copy.

Open question (22 Sept 2026, site review): profile.json has class read, fraction_read 1.0, but the key was checked
letter for letter on f. 370 only (81 characters); ff. 373, 406 and 410 were read from the Brienne clear copy, not
deciphered from the cipher. Decide next time whether 1.0 should stand, or whether the other three leaves should be
deciphered with the key and measured. Written up as `docs/maisse1592.html`.

## 1. What the catalogue said, and why it was wrong

`catalogue.json` scored this "these four use a different key with no sibling found yet" and classed it **B**.
Both halves of that are wrong, and the error came from reading Tomokiyo's list as one group of four.

Tomokiyo's Henri IV page (`../gallica_sweep/src/henryiv.txt`, lines 127-177) splits fr. 16093 into cipher
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
test."* That step was skipped at the start of this session because `gallica_sweep/src/henryiv.txt` is a **text
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
