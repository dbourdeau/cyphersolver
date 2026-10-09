# Lope Hurtado de Mendoza (Rome) to Charles V, 1522 — RAH Salazar 9/26, DECODE R9634–R9656

Status: in progress (key being rebuilt from a contemporary decipherment; first values fixed)

Catalogue entry 144 ("Lope Hurtado de Mendoza (Rome) to unknown recipient, 8 ciphertexts",
RAH Signatura 9/26). Opened 2026-09-20, after the sanchez1522 session established that these letters
are **not** in Alonso Sánchez's cipher.

## Why this is a separate target

The nine Lope Hurtado records are bound in Salazar 9/26 among Sánchez's, were catalogued with them,
and look at first like more of the same: same months, same recipient, cipher mixed with clear inside
the sentence, code groups of the same shape. They are in a different cipher. Sánchez's codes end
strictly in `b c d f g h l m n`; Hurtado's take finals `p` and `z` (`tep`, `tap`, and groups ending
`-z`). See `../sanchez1522/NOTES.md`.

## Prior art: none

Tomokiyo's *Correspondence in Cipher of Imperial Ambassadors Alonso Sanchez and Juan Manuel (1522)*
(Cryptiana, 6 Sept 2025) reconstructs **Sánchez's** and **Juan Manuel's** ciphers. It does not mention
Lope Hurtado, and his records R9634–R9656 fall outside both ranges it lists. A web search for a
decipherment of his cipher returns nothing. **This key has not been published.**

## The records

| DECODE | 9/26 ff. | date 1522 | pp | DECODE status |
|---|---|---|---|---|
| R9634 | 14–16 | 13 Sept (Genoa) | 6 | Non-decrypted; **read in part 73%** (`read_r9634.md`, 2026-10-02) |
| R9644 | 237–243 | 1 Nov | 14 | **Decrypted** |
| R9645 | 243–244 | Nov | 4 | Non-decrypted; **read in part 75%** (`read_r9645.md`, 2026-10-03) |
| R9646 | 252 | [Nov] | 2 | Non-decrypted; **read in part 80%** (`read_r9646.md`) |
| R9648 | 260–265 | 9 Nov | 12 | Non-decrypted |
| R9649 | 266–268 | 9 Nov | 6 | Non-decrypted; **read 100%** from its own clear f. 268 (`read_r9649.md`) |
| R9650 | 269–272 | — | 10 | **Decrypted** |
| R9652 | 295–296 | Nov | 2 | Partially decrypted |
| R9656 | 334–335 | 23 Nov | 4 | Non-decrypted; **read in part 79%** (`read_r9656.md`, re-transcribed 2026-10-03) |

Images in `img/` (git-ignored; RAH material, fetched from DECODE 2026-09-20).

## The crib: R9644 carries its own decipherment

R9644 is the way in. The record holds **both** the ciphered letter (ff. 238–239) **and a full clear
version of it** (f. 242), the clear headed and closed with *Claro* section by section, and keyed to
the cipher by **marginal letters A, B, C** written against the matching passages on both.

So the attack is a straight crib: align the cipher against the clerk's own plaintext, token by token,
wherever the word counts match exactly.

## First values, fixed against the clear

The clear (f. 242) reads:

> … y que los que le tienen por frances veen si sus officios y fortalezas y servicio de su casa lo
> haze con franceses o castellanos. Su Sa[ntidad], a lo que yo pienso, espera lo que hara el
> arçobispo de Bari, y no gastar nada si ser pudiesse, porque esta tan escasso **que nunca hombre lo
> fue mas**; hasta que el arçobispo venga creo que sera mejor **no apretallo mucho**.

The cipher (f. 238) runs, with *hasta que el arçobispo venga creo que sera mejor* standing in the
clear on the cipher page itself:

```
… ton  tab    xud     xul  ɣm   xon  │ hasta q el arçobispo venga creo q sera mejor │ tu  ᵷʒ℔ʒ ʒ7 ∞ʒ ɸeɋ
    que nunca hombre  lo   fue  mas                                                    no  a-p-r-e-t-a-ll-o  mucho
```

Six tokens against six words, in a sentence with no room for slippage:

| code | value |
|---|---|
| `ton` | **que** |
| `tab` | **nunca** |
| `xud` | **hombre** |
| `xul` | **lo** |
| `ɣm` | **fue** |
| `xon` | **mas** |
| `tu` | **no** |

`ton` = *que* settles the point that this is not Sánchez's key, where *que* is `ho`.

Carried in `key_codes.tsv`.

## A second anchor, on the same leaf

Lower on f. 238 the cipher runs `… ɣof ∞7∞ᵷLʒ#8ʃ3m zun top │ descargo de los q │ …`, with
*descargo de los q* standing in the clear on the cipher page. The plaintext at that point (f. 242)
reads:

> … las obras ningun servidor de v. ma la esta satisfecho; **da por descargo** de lo que dexa de
> fazer la obligacion que tiene a procurar la paz …

So `zun top` = **da por**, which

- **confirms `top` = *por*** in a second, independent context (the first was `top ton` = *porque*);
- gives **`zun` = *da***;
- and shows the ten-sign run `∞7∞ᵷLʒ#8ʃ3m` standing where *satisfecho* must be, and the eight-sign
  run `Ɉ℔ɸʒx℔4` where *servidor* must be — so long words are spelled out letter by letter between the
  codes, as in Sánchez's cipher.

Nine values are now confirmed against the clerk's own plaintext, twelve more probable. The
`key_codes.tsv` file keeps the two apart in a `confidence` column; nothing probable is being used to
derive anything else.

## The key is shared across his letters

R9650 (9/26 ff. 269–272, the other *Decrypted* record) carries the same forms. On f. 270:

> `ᵹᵹʒ` **`ton` `tab` `xud`** `ɣifLᵹ` `zil` `tod` · **`tu`** `ʃʃ℔℔ᵹLᵷ9ʒ7` `zun℔` `xil` `to7` **`top`** ·
> *disimular en este caso v. Mt.*

`ton tab xud` stands there in identical forms, and `top` again immediately precedes clear words in a
slot that reads *por disimular en este caso* — a **third** independent context for `top` = *por*.
`tu` and `zun` recur too.

So Hurtado used one key across these letters, and values won on R9644 carry to the rest. That is what
makes the six non-decrypted records reachable once the key is far enough along.

## The clear version begins on f. 241, and gives the opening of the letter

`IMG_R9644_I45411_P1.jpg` shows f. 241: *Al Rey — de Lope Hurtado, de Roma, del primero de
noviembre*, then **Claro**, then the plaintext in lettered sections (A …). So the clear runs
ff. 241–242 and covers the cipher of ff. 238–239 from its start.

Its third paragraph is the crib for the top of the cipher page:

> **Es muy bien lo que v. ma dize que lo que hoviere de hazerse con** los criados de su Sa
> **primero los sepa, pero hasta que v. ma les de lo que fuere servido, si algo se le dixesse**
> pensaria que era para no les dar nada …

(bold = what stands in the clear on the *cipher* page too; the rest is enciphered there.)

Aligning the enciphered stretch after *si algo se le dixesse*:

| cipher | plaintext |
|---|---|
| `⊃84∞7ʒ∞7` | **pensaria** — eight signs for eight letters |
| `ton` | **que** (again) |
| `ᵷʒ7` | **era** |
| `teɡ` | **para** |
| later, `zun`+`ʒ` | **dar** |

New confirmed values: **`ᵷʒ7` = *era***, **`teɡ` = *para***, and the letter **`ʒ` = r** — the last
attested twice over, in the *r* of the spelled *pensaria* and in `zun`+`ʒ` = *dar*, which in turn
re-confirms `zun` = *da*.

**A retraction.** The earlier probable `zar` = *Bari* was wrong. `zar` is frequent, and here it falls
in the slot *los criados **de su** Sa*; it is now carried as *de* or *su*, still probable. This is why
the probable values are kept out of any derivation.

### The next line aligns end to end

The following line of cipher matches the plaintext token for token with nothing left over:

| `ta` | `xil`+s | `zun`+`ʒ` | `xur` `zun` | `ɋ` | `x∞ʒ∞7` | `ton` | `tu` | `ton`+`℔∞7` | `ton` | `xul` |
|---|---|---|---|---|---|---|---|---|---|---|
| no | les | dar | **na·da** | y | diria | que | no | **que·ria** | que | lo |

Three things come out of it.

1. **Two codes for *no*.** `ta` and `tu` both stand for it, in the same line — the cipher has
   homophones at the code level, not only in the alphabet.
2. **Codes carry syllables.** `xur`+`zun` = *na*+*da*, and `ton`+`℔∞7` = *que*+*ria*. `zun` is the
   same *da* confirmed earlier in *da por*; here it is the second syllable of *nada*. Word boundaries
   go both ways in this cipher exactly as they do in Sánchez's.
3. `x∞ʒ∞7` is five signs for the five letters of *diria*, consistent with `ʒ` = r.

### Three codes chained into one word

The next line gives `… ɋ xul h℔∞ ℔ xᵹ∞ **ton zun ℔∞74** ᵷard zilᵹ84 …` against the plaintext
*… y los criados **quedarian** descontentos …*:

> `ton` + `zun` + `℔∞74` = *que* + *da* + *rian* = **quedarian**

`zun` = *da* is now confirmed a third time, in a third role: a whole word in *da por*, the second
syllable of *na·da*, and the middle syllable of *que·da·rian*. The ending `℔∞74` is `℔∞7` (*-ria*)
plus `4`, which gives the letter **`4` = n** — the same sign as the *n* of the spelled *pensaria*.

### The letter alphabet starts to come out

The end of the same paragraph aligns exactly — four cipher units for four words:

| `∞L84℔ɋ` | `⊃8ʒxL67` | `xuɡ` | `ɣufɋ` |
|---|---|---|---|
| tiene | **perdida** | la | esperança |

*perdida* is spelled out, seven signs for seven letters, and that hands over a first slice of the
**substitution alphabet**:

| sign | `⊃` | `8` | `ʒ` | `x` | `6` | `L` | `7` | `4` |
|---|---|---|---|---|---|---|---|---|
| letter | p | e | r | **d** | **d** | i | a | n |

Two signs for **d** in one word — homophones in the alphabet as well as in the codes. The values
cross-check against the spelled *pensaria* earlier in the paragraph (same `⊃`, `8`, `7`, `4`) and
against `ʒ` = r, already confirmed twice.

### A name spelled out

Further down, between *a v. Mt.* and the clear words *es el principal*, the cipher carries the
plaintext **El camarero Pedro**. *Pedro* is spelled `⊃ 8 x ʒ m` — five signs for five letters, of
which p, e, d and r are already confirmed, so the last one falls out: **`m` = o**.

The alphabet so far: `⊃`=p, `8`=e, `ʒ`=r, `x`/`6`=d, `L`=i, `7`=a, `4`=n, `m`=o.

Thirty-three values confirmed, fourteen probable.

*One caution:* the sign transcribed `∞` reads as **t** in *tiene* but seemed to be **s** in
*pensaria*. One of the two transcriptions is wrong. It is left unassigned rather than guessed.

## The key reads a record DECODE calls non-decrypted

R9648 (9/26 ff. 260–265, 9 Nov 1522, **Non-decrypted**) turns out to carry the same matter as
R9644's clear — *pregunte a su S.* and *le avia embiado la carta de v. Mt y q esperava saber lo de
Yngalaterra* stand in the clear on its leaves, answering to section **C** of the R9644 plaintext.
Hurtado sent his despatches in duplicate, so one clear version serves both.

That makes R9644's plaintext a crib for R9648 as well, and the key built on it reads there. On
f. 262, nine cipher tokens against nine plaintext words, with nothing left over:

| `ɋ` | `ton` | `ɣub` | `taf` | `tu` | `ɣof` | `ɣuc` | `ton` | `L84ℇ℔` |
|---|---|---|---|---|---|---|---|---|
| y | que | el | papa | no | esta | en | que | venga |

and immediately after the clear words *pregunte a su S.*:

| `ton` | `teʒ` | `ᵹʒ4∞` | `7zar` | `ɣon` |
|---|---|---|---|---|
| que | nueva | tenia | de | Francia |

`ɋ`, `ton` and `tu` are values won on R9644 and reappearing here correctly, which is the check that
matters. Seven new values come out of it — **`taf` = *papa***, **`ɣof` = *esta***, **`ɣuc` = *en***,
**`teʒ` = *nueva***, **`ᵹʒ4∞` = *tenia***, **`ɣon` = *Francia***, and the spelled *venga* — plus
`ɣub` = *el* promoted from probable, and support for `zar` = *de*.

**This is the first previously-unread text of Hurtado's read here.** It is short, and it leans on the
duplicate's plaintext rather than standing on the key alone, so it is a foothold rather than a
reading. But the mechanism now works end to end: crib → key → a record nobody had read.

### And it keeps reading

Further down the same leaf of R9648, against section C of the R9644 plaintext:

> `ton` `ɣub` `zed` │ *le avia embiado la carta de v. Mt* │ = **que el arçobispo** …

giving **`zed` = *arçobispo*** — a name-code for the man who runs through this whole
correspondence, the archbishop of Bari.

And a few words on:

| `ton` | … | `xuɡ` | `tef` | `top` | `xul`+s | `ᵹʒ℔ʒℇᵹʒᵹ` | `ɋ` | `top` | `xuɡ` | … |
|---|---|---|---|---|---|---|---|---|---|---|
| que | desseava mucho | **la** | **paz** | **por** | **los** | infieles | **y** | **por** | **la** | necessidad |

Everything in bold is a value won earlier and reappearing correctly; `tef` = *paz* is new. The run
*la paz por los infieles y por la necessidad* is continuous previously-unread text — Hurtado
reporting that the Pope wanted peace because of the Turks and because of the Emperor's need.

### The alphabet decodes a word on its own

On f. 264 of R9648, between the clear words *antes de agora* and *si se oviera hecho*:

> ‖ `tu` `ʃu` `ᵹ…7` **`℔ᵹ8ʒxL6m`** **`xur zun`**
> = no se [h]uviera **perdido** **nada**

`℔ᵹ8ʒxL6m` spells out p-e-r-d-i-d-o. Six of those signs — `8`=e, `ʒ`=r, `x`=d, `L`=i, `6`=d, `m`=o —
were derived on R9644 from *perdida*, *pensaria* and *Pedro*, and every one of them is correct here in
a word decoded without being looked for. `xur zun` = *na*+*da* likewise reappears intact.

The whole sentence then runs: *y antes de agora **no se huviera perdido nada**, si se oviera hecho
como muchas vezes yo lo escrevi a v. Mt* — Hurtado telling the Emperor that nothing would have been
lost had his advice been taken earlier.

R9644 carries this same sentence in the clear, being the duplicate, so the reading is corroborated
rather than unsupported; but the **decoding** was done from the key, not read off the crib, and that
is the test the key needed to pass.

### The key stands on its own: R9656, an independent letter

Everything so far leaned, somewhere, on R9644's plaintext — R9648 being its duplicate. **R9656**
(9/26 ff. 334–335) is not. It is headed *Al Rey — De Lope Hurtado, de xx de noviembre*: a different
despatch, three weeks later, with **no clear version and no duplicate**. If the key is real it must
read there unaided.

It does. On f. 334, after the clear words *las cartas traxo don Correo q vino con la valante*:

> ‖ `tu` `n7` `Lᵹʒᵹ` `∞∞` **`ɣub`** **`taf`**
> = no … **el papa**

`ɣub` = *el* and `taf` = *papa* were both won on R9648 against R9644's crib, and both read correctly
here in a letter that crib does not cover. Elsewhere on the same leaf `ton` (*que*), `zar` (*de*),
`ɣof` (*esta*), `sub` (*si*) and `tu` (*no*) all fall in slots that make sense.

**This is the validation that matters.** The key was built on one letter's crib and reads in another
letter that has none.

The three unresolved units between *no* and *el papa* are left blank rather than guessed; the sense
wants something like "no ha querido ver", but wanting is not evidence.

### One more from the crib

R9648 f. 264, after the clear words *A lo q he entendido*:

> ‖ `ɣʒ` `ʃta` **`zil`** **`ɣub`** **`zed`** **`zar`** `ɣᵹᵹ84ɣ` │ *trata de algunas cosas su S.*
> = … **con el arçobispo de** Cosenza …

against section B of the R9644 plaintext. That gives **`zil` = *con***, re-confirms `zed` =
*arçobispo* in a second context, and promotes **`zar` = *de*** — now attested three times over
(*de su Sa*, *de Francia*, *de Cosenza*), which matters because `zar` is one of the commonest groups
on every leaf.

### The commonest group of all

A little further on the same leaf, against section C of the plaintext (*… por la necessidad de v. ma,
pues queda de la guerra honrrado y approvechado. Yo dixe a su Sa …*):

> … `zar` **`rab`** … `ᵹᵹ497xm` `ɋ` `7℔℔…xm` │ *yo dixe a su S. q v. Mt.*
> = … de **v. ma** … **honrrado** **y** **approvechado** …

`zar rab` falls exactly on *de v. ma*, and `rab` is one of the commonest groups on every leaf of
every letter — which is what *vuestra magestad* ought to be in despatches addressed to the Emperor.
**`rab` = *vuestra magestad***.

The two spelled words either side check the alphabet again: *honrrado* and *approvechado* both end
`…7 x m` = a-d-o, with `4` = n inside the first. Every one of those signs came from R9644.

Fifty values confirmed, ten probable.

## Section A confirms the spine

f. 237 carries the head of the ciphered letter, with **A** in the margin against the passage the
clear (f. 241) gives as:

> Ha sido muy bien que v. ma **prevenga a su Sa** de lo que conviene a su servicio, porque aunque
> **no haga lo que es obligado, no se disculpe despues con dezir que v. ma** no le mando prevenir…

The cipher runs, with the unbolded parts standing in the clear on the cipher page itself:

> *ha seido muy bien q v. Mt* │ `℔ᵹʒʒLℇ7` `ℇ7` **`ʃʃ`** **`ʃid`** │ *de lo que conviene a su servicio,
> por q aunq* │ ‖ `ɣʒ` **`tu`** `xLʒ` `ℇ7` **`xul`** **`ton`** **`ɣaf`** `tad` `xᵹ` **`tu`** `ʃu`
> `xᵹᵹɡLʒʒx℔` `ɣ7` **`zil`** `ɣʒʒ` **`ton`** **`rab`** │ *no le mando prevenir*

Six values already fixed — `tu` *no*, `xul` *lo*, `ton` *que*, `ɣaf` *es*, `zil` *con*, `rab`
*vuestra magestad* — all fall in their right places across a long sentence. That is the densest
single check the key has had.

New from it: **`ʃʃ` = *su*** and **`ʃid` = *Sa*** (Su Santidad, the Pope), from `ʃʃ ʃid` = *su Sa*.
Three more are probable — `tad` *obligado*, `xLʒ` *haga*, `ɣʒʒ` *dezir* — sitting in slots the sense
fixes but the counts do not.

The paragraph after it does the same. Clear: *Assi mesmo fue bien escrivir largo, **porque su Sa
tenia tanta passion que no conocia lo que** don Joan le havia servido*. Cipher:

> … **`top`** **`ton`** **`ʃid`** `ᵹ847` `ʃuf` `ʒ7xʒᵹᵹ4` **`ton`** **`tu`** **`zil`**+`mɡᵹᵹ`
> **`xul`** **`ton`** `xᵹ4` `LL741` …
> = **por** **que** **su Sa** tenia tanta passion **que** **no** **con**·ocia **lo** **que** don Joan

Seven fixed values in a row, and one more instance of the stem-plus-ending pattern: **`zil` (*con*)
+ a spelled *ocia* = *conocia***, which is the third construction `zil` has been seen in.

`ʃid` is worth a note. In section A it stood beside `ʃʃ` (*su*) as *su Sa*; here it carries *su Sa*
on its own. Either it means *Sa* and the *su* is sometimes coded separately, or it means the whole
title and section A wrote *su* twice. Not settled, and recorded as *Sa / su Sa*.

### The end of f. 237, and a second sign for o

The last two lines of the leaf run against *Yo he preguntado a su Sa lo que le parece **del duque**,
y me dixo que estava contento, **lo que no quedo de don Joan** segun dizen todos*:

> *yo he preguntado a su S. lo q le parece* │ ‖ **`zarᵹ`** **`ɣᵹb`** │ *y me dixo q estava contento*
> │ **`xul`** **`ton`** **`tu`** **`ton`·`x`·`m`** **`zar`** **`x`·`ᵹ`·`4`** `ʒLʃʃ4` `ʃob` `ɣL4`

- **`ɣᵹb` = *duque*** — the Duke of Sessa, the imperial ambassador at Rome, who with the Pope and
  the archbishop makes three of the four men these letters are about.
- **`zarᵹ` = *del***, `zar` (*de*) plus one sign.
- **`ton`·`x`·`m` = *que*+d+o = *quedo***, a code finished with two alphabet signs.
- **`x`·`ᵹ`·`4` = d-o-n = *don***, spelled outright — and that fixes **`ᵹ` = o**, a second sign for
  o beside `m`.

That last one matters beyond the word: `ᵹ` was one of the signs whose readings contradicted each
other, and it turns out to be a homophone of `m`. Part of the alphabet tangle recorded above was a
missing homophone rather than a bad transcription.

Fifty-five values confirmed, thirteen probable.

## A second complete crib: R9650 f. 272

R9650 has its own clear version, on **f. 272**, headed *Al Rey — De Lope Hurtado de …* exactly as
R9644's does. It is a full letter, and a rich one:

> Ayer vino posta **del arçobispo de Bari**; scrivieme de [xxiii] … dize que antes de seys dias
> enbiaria aqui uno suyo con quien avisaria largo … En substancia me dize que **los franceses son
> determinados de venir en Italia, y enbian gran suma de dinero a Leon**, y que es menester que se
> entienda en la defensa, y que **el papa** haga lo que pudiere, pues le va mas que a nadie. Y he
> dicho a su Sa que de **Hieronymo Adorno** me ha venido este aviso de unas cartas que ha tomado por
> amor de v. ma … por servicio de Dios y remedio de la yglesia y de su estado deve pensar lo que ha
> de hazer sin dilatar mas, porque despues no havra tiempo … trabajare de saber lo que el arçobispo
> scrive y vere la respuesta de su Sa. Y luego avisare a v. ma, que agora no puede ser, porque **el
> duque** me ha scrito que oy partira la posta … Yo le he avisado desto y a **don Joan Manuel** y al
> **visorey de Napoles** …

So there are **two complete cribs**, not one, covering two different letters — and this one brings
new vocabulary the first does not have: *franceses*, *Italia*, *dinero*, *Leon*, *yglesia*,
*Hieronymo Adorno*, *don Joan Manuel*, *visorey de Napoles*, *posta*. Those are exactly the content
nouns the key is short of.

It also tells us what the letters are *about*, independently of the cipher: the French are
determined to come into Italy and are sending a great sum of money to Lyon; the Pope must do what he
can; Adorno has intercepted letters; the archbishop of Bari is the channel to the Emperor.

### The second crib starts paying

R9650 f. 269 is the ciphered letter whose clear is f. 272, and it opens with the same words *ayer
vino posta del arçobispo de Bari* standing in the clear on the cipher page itself. A few lines down,
against *En substancia me dize que **los franceses son determinados de venir en Italia, y enbian gran
suma de dinero a Leon, y que es** menester…*:

> ‖ `ʃta` │B│ **`ton`** `xul`+s `ɣunʒᵹ` `ᵹᵹ4` **`zar`** `ᵹ8ʒ…xmᵹ` **`zar`** `Lᵹtip` **`ɣuc`** `xLɡ`
> **`ɋ`** `ɣuc`·`ᵹᵹ74` `xᵹb` `ʃed℔` **`zar`** `ɣab` `ʃʃ` `xiLᵹ4` **`ɋ`** **`ton`** **`ɣaf`** …

`ton`, `zar` (×3), `ɣuc`, `ɋ` (×2), `ɣaf` and `xul` all land correctly — eight placements of
already-fixed values in one sentence of a letter the first crib does not cover.

And the slots give the **content nouns the key was short of**, recorded as probable since the
token counts are not exact: `ɣunʒᵹ` *franceses*, `xLɡ` *Italia*, `ɣab` *dinero*, `xiLᵹ4` *Leon*,
`xᵹb` *gran*, `ʃed℔` *suma*.

A few words on, against *y que **el papa haga lo que** pudiere, pues le va mas que a nadie*:

> **`ɋ`** **`ton`** **`ɣub`** **`taf`** `xLᵹ7` **`xul`** **`ton`** `⊃Lxᵹᵹ℔ᵹᵹ` │ *pues le va mas q a
> nadie*
> = **y** **que** **el** **papa** haga **lo** **que** pudiere

Six fixed values round a single unknown, which the sense then fixes: **`xLᵹ7` = *haga***, promoted
from probable — it was in the same slot in R9644's section A (*no haga lo que es obligado*), and a
value that turns up twice in the same construction across two letters is not a coincidence.

And at the end of the line `zar rab` = *de v. ma* again.

And again in the next sentence, against *y **por lo que** deve, **no se** ponga **en** esto*:

> **`ɋ`** **`top`** **`xul`** **`ton`** `xiL` **`zar`** … **`tu`** **`ʃu`** `ᵹᵹq℔℔` **`ɣuc`** `ɣif`
> = **y por lo que** deve **de** … **no se** ponga **en** esto

Seven fixed values in one short clause. New probables from the gaps: `xiL` *deve*, `ᵹᵹq℔℔` *ponga*,
`ɣif` *esto*, and `ᵹeɡʒ` *cartas* from the phrase before (*de unas cartas que ha tomado por amor de
v. ma*).

Sixty-five entries now, fifty-six of them confirmed.

## A measured coverage number

`decode.py` resolves a transcribed token string against `key_codes.tsv`. It applies **only the
confirmed values**; probable ones print in `<angle brackets>` so they can never be mistaken for
evidence, and unknown tokens print as `?tok` with a coverage figure.

Run on two lines picked from records the key was *not* built on:

| line | result | coverage |
|---|---|---|
| R9650 f. 270 | `?` que nunca hombre `?` con otros no `?` `?` les `?` por | **8/13 = 62%** |
| R9648 f. 262 | que nueva tenia `?` Francia `?` `?` que el arçobispo | **7/10 = 70%** |

So roughly **two tokens in three** now resolve on sight, in letters the crib does not cover. The
misses are of two kinds: a few nomenclator codes not yet met, and the spelled runs, which need the
alphabet. That is the honest state of the key — good enough to follow the sense of a passage, not
good enough to edit one.

## f. 239: sections B, C and D

The third ciphered leaf carries the rest of the letter, marked **B**, **C** and **D** in the margin.

Section **B**, against *… que **sin el no hay nada, y con el** por lo de aqui esta perdido …*:

> `ton` **`ʃubʒ`** **`ɣub`** **`tu`** … **`xur zun`** **`ɋ`** **`zil`** **`ɣub`** …
> = que **sin** **el** **no** … **na·da** **y** **con** **el** …

**`ʃubʒ` = *sin*** — `sub` (*si*) plus one sign — and `xur`+`zun` = *nada* turns up yet again.

Section **C**, against *… que su Sa **da señal de paz**, y que **el Rey de Francia** pedia salvo
conducto por enbiar **embaxador** a su Sa … **pues queda de la** guerra honrrado y approvechado*:

> **`zun`** `ᵹ847ᵹ` **`zar`** **`tef`** **`ɋ`** **`ton`** **`ɣub`** `taʒ` … **`zil`** … **`teɡ`**
> **`ɣuc`** … `ɣed` **`ʃʃ`** … / **`tel`** **`ton`**·**`zun`** **`zar`** …
> = **da** señal **de** **paz**, **y** **que** **el** Rey … **con** … **para** **en** … embaxador
> **su** … / **pues** **que·da** **de** …

**`tel` = *pues*** is new and confirmed by an exact slot, and it is immediately followed by
`ton`+`zun` = *que*+*da* = **queda**, which confirms both of those a further time. `taʒ` = *Rey* and
`ɣed` = *embaxador* are recorded as probable.

Sixty-nine entries, forty-nine confirmed code values.

## The records with no crib: measured, not guessed

Of the nine, four are read complete as to content (`read_r9644.md`, `read_r9650.md`,
`read_r9652.md`, and R9648 as R9644's duplicate). The other five have no clear version anywhere,
and there the key has to work alone. Measured with `decode.py`, which applies confirmed values only:

| record | date | measured coverage |
|---|---|---|
| R9648 f. 262 (duplicate of R9644) | 9 Nov | 70% |
| R9650 f. 270 | Nov | 62% |
| **R9645 f. 243** (no crib) | Nov | **57%** |
| **R9656 f. 334** (no crib) | 20 Nov | **42%** |

R9645 decodes to *… se si no con […] con vuestra magestad, que no […] en […] esta[do] […] de
vuestra magestad …* — the shape of the sentence and its subject, with the content words missing.

**A correction to an earlier claim in this file.** I had written that the five uncribbed records
"read in substance". Measured, they do not. R9656 comes out at **42%**, and what it yields is

> `?` `?` `?` **no** `?` `?` `?` **el papa** `?` **la** `?` `?` `?` **que** `?` **su** **el papa**

— fragments, not substance. The subject can sometimes be identified (this stretch is plainly about
the Pope) and the parties can be named, but the letters do not read.

The honest ceiling of the present key on an **uncribbed** letter is therefore: **roughly half the
tokens, concentrated in the function words and the names; the content words are the misses.** That is
enough to say what a passage is about when the surrounding clear text helps, and not enough to read
one. R9648 and R9650 score higher (70%, 62%) partly because their cribs were walked.

## Correction: the alphabet signs are downgraded to probable

An 8× zoom on the spelled *perdido* in R9648 f. 264 settles a doubt the other way from the hoped-for
one. At that magnification the word resolves into seven distinct glyphs, as it should — but the
signs in positions 2 and 6, which must be **e** and **d**, look near-identical. They were read as
different letters at the zoom the alphabet values were taken at.

The conclusion is uncomfortable and is recorded rather than buried: **the nine alphabet values were
labelled `confirmed` on weaker evidence than that word implies**, and all ten sign entries are
**downgraded to `probable`**, with the reason written into each row.

The distinction that matters, and that the audit should have drawn earlier:

- **Code groups are safe.** They are written as ordinary latin trigrams — `ton`, `zar`, `rab`,
  `xul` — legible without paleographic judgement, and they cross-check against each other across
  letters and constructions. Forty-seven of them stand.
- **Alphabet signs are not.** They rest on discriminating one cursive shape from another at the
  limit of what the scans carry. Any of them could be a homophone of a sign I have read as something
  else, and *perdido* shows exactly that failure mode.

`decode.py` now shows every alphabet value in angle brackets, so no reading can lean on one without
it being visible.

## Where the work is now limited: the alphabet, not the nomenclator

The two halves of this cipher are not equally tractable at the resolution DECODE serves.

**The nomenclator is easy.** The code groups are three-letter latin trigrams written plainly —
`ton`, `zar`, `rab`, `xul`, `top`, `zil`, `taf` — and they read off the page without difficulty.
Fifty of them are now fixed, including the high-frequency spine (*que, de, no, y, por, la, lo, los,
el, en, es, si, con, papa, arçobispo, vuestra magestad*), and they carry most of the content.

**The alphabet is hard.** The spelled runs between the codes need per-glyph discrimination that the
images do not reliably support. Nine signs are fixed — `⊃`=p, `8`=e, `ʒ`=r, `x`/`6`=d, `L`=i, `7`=a,
`4`=n, `m`=o — every one of them cross-checked on several words. Beyond that the transcriptions
start to contradict each other:

- *tiene* wants `∞` = t, but my reading of *pensaria* wants `∞` = s;
- *venga* as transcribed wants `L` = v, but *perdida* fixes `L` = i;
- *Cosenza* comes out as eight signs for seven letters, with `ɣ` apparently serving as both c and z
  and `ᵹ` as both o and s.

At least one transcription in each pair is wrong. Rather than pick whichever reading suits, those
signs are left unassigned. **This is the same wall the sanchez1522 work hit**: the codes read, the
letters need a picture-book built glyph by glyph against known plaintext, and that is slow work on
these scans.

The practical consequence is that Hurtado's letters will read *in substance* — subject, parties,
sums, the drift of the argument — well before they read word for word.

## The one thing that would finish this: better images

The blocker is measured, not guessed. DECODE serves these leaves at **3440 × 2465 for a two-page
opening** — about 1700 px across a folio, which is enough for the latin trigrams and not enough to
tell two similar cursive signs apart. That is why the code groups are confirmed and the alphabet is
not, and no amount of further crib-walking changes it.

**DECODE has been checked with the cookie, and has nothing better.** The logged-in session does
fetch the images (that is how `img/` was filled), but:

- the full-size file `IMG_R9644_I45410_P1.jpg` *is* what `filesrv` returns — 1.45 MB, 3440 × 2465
  for the two-page opening. There is no larger variant: `MASTER_`, `MS_`, `ORIG_` and `.tif` names
  all come back as the server's 5,244-byte not-found placeholder;
- the Image Manager (`/decrypt-web/ImagesList`) answers **"You do not have permission to access"**
  with this cookie. It is a viewer session, not an editor one, so its zoom view cannot be reached
  either.

So the ceiling is DECODE's stored copy, and it is a derivative. The volume is in the
**Colección Salazar y Castro**, which the Real Academia de la Historia has been
digitising at its own Biblioteca Digital (<https://bibliotecadigital.rah.es>). If Salazar 9/26 is
there, its images will be far better than DECODE's derivative copies, and the alphabet becomes
ordinary work rather than guesswork.

**This needs Daniel**, not the session: `bibliotecadigital.rah.es` returns HTTP 403 to automated
requests and puts a bot check in front of its search, exactly as DECODE's image server needs a
logged-in cookie ([[decode-access]]). Searching there for *Salazar y Castro, A-26* (the old
signature for 9/26) and pulling ff. 237–243, 260–272 and 334–335 at full resolution would unblock:

- the substitution alphabet, and with it a word-perfect edition of the ciphered leaves;
- the five records with no clear version (R9634, R9645, R9646, R9649, R9656; R9649 and R9656 later turned out to carry one), which currently read
  in substance only.

Until then the honest ceiling is the one recorded above: the nomenclator reads, the spelled runs do
not.

## Next

- Work the rest of the R9644 alignment section by section, using the marginal A/B/C keys.
- Then R9650 (also *Decrypted*) and R9652 (*Partially decrypted*) as further cribs.
- Then apply the rebuilt key to the six non-decrypted records.
- Test whether the key is Juan Manuel's: Tomokiyo's Juan Manuel table has `ton` unassigned, so the
  values above do not yet contradict it, and the question stays open.

## The 1524 alphabet applied back to 1522 (2026-09-21)

The 1522 transcriptions and `key_1524.tsv` use different names for the same glyphs (1522 `∞` = 1524 `ω`,
1522 `ɣ` = 1524 `y`, and so on), so the 1524 key cannot be run over the old token strings. R9656 f. 334
(20 Nov 1522, no crib, no duplicate) was re-read off the image in 1524 notation instead. Its cipher runs:

```
l.1-2  … nueva ∂6 ʃta zar ε7 ∠8ω / ti zun zar ε&∂ yun ʒ∂ │ ni a nadie sino a mi
l.4    ʃ6 tu n4 ∠α8ʒ oo yub taf
l.5    ɡ ʇʇ8 oo ʒ xuɡ ∠84αx7 zar ε&∂ yun ʒ∂ │ he preguntado
l.6    ʃʃ yuc n4∠α ʒt ʃub ∠α84oo ɡ ton xic ʒ ʃʃ
```

With the 1524 values unchanged (`zar` de, `xuɡ` la, `yun` fran-, `ε` l, `7` a, `8` e, `4` n, `ʇʇ` r):

- l.5 `xuɡ ∠84αx7 zar ε&∂ yun ʒ∂` = **la venida de los franceses**, exact count. It gives `∠` = v (a sign the
  1524 key does not have) and agrees with 1524 `α` = i; `x` = d, which the 1522 key already had.
- l.1-2 then reads *[el arçobispo de Bari no escrevio al papa] nueva … **de la ve·ni·da de los franceses**
  [ni a nadie sino a mi]*: `ε7` = la and `zun` = da, both 1524 values.
- l.6 `ʃub ∠α84oo` = **si vien-** (`sub` si), which the clear two lines later answers: *si vienen franceses
  sera por mal dellos*.

So the 1522 and 1524 alphabets are one alphabet: five 1524 letter values (a, e, n, l, i) and four
codes read correctly in a 1522 letter nobody has deciphered, and 1522 `L` = i is really `α`, not the 1524
`L` = r. The key-moved note on `L` is a transcription collision, not a key change.

Still open on this leaf: `∂6 ʃta`, `ʃ6 tu n4 ∠α8ʒ oo` (*no … el papa*), `ɡ ʇʇ8 oo ʒ`, `oo` (probably a
sign for s or an ending; not fixed from one context). R9634, R9645, R9646, R9649 re-read and R9656 regraded 2026-10-02 (next section).

## R9634, R9646, R9649 in 1524 notation (2026-10-02)

The claim above (and in the Remaining gaps until today) that these three were never attempted was out of date for
two of them: `read_r9646.md` and `read_r9649.md` already existed, from a session that did not update this file.

| record | date | crib | tokens | read as sense (measured) | file |
|---|---|---|---|---|---|
| R9634 ff. 14–16 | Genoa, 13 Sept 1522 | none | 1191 | **842 = 71%** | `read_r9634.md`, `r9634_cipher.txt`, `r9634_reading.tsv` |
| R9646 f. 252 | [Rome, Nov 1522] | none | 121 | **97 = 80%** | `read_r9646.md` |
| R9649 ff. 266–268 | Rome, 9 Nov 1522 | own clear, f. 268 | 89 | **89 = 100%** | `read_r9649.md` |

- **R9649 is not uncribbed**: f. 268 is the clerk's clear of the whole letter (*Al Rey — De Lope hurtado de ix de
  noviembre*). Read in full: Adrian VI asks Charles to urge him to keep the fortress of Ostia, which Cardinal Santa
  Cruz (Carvajal, as dean) claims; the licenciado Bernardino has landed from Barcelona and is hiding in Rome.
- **R9646**: Adrian VI's capitulation with the duke of Ferrara is signed; Charles's request (*la decima*, probable)
  meets papal fear; the archbishop advises offering money *al papa para sus necesidades … que creo que por dinero
  …*. Re-read today: *oviese* for *oyese*, and the run-opening groups are nulls.
- **R9634** (first transcription today, from the three DECODE openings): not a Rome letter. Written from **Genoa,
  13 Sept 1522**, it reports Geronimo Adorno's proposal that Charles V and Henry VIII invade France through
  **Provence**, *la tierra mas flaca que el tiene*, supplied by the Genoese galleys, with 600 men-at-arms, light
  horse and foot paid **70,000 ducats a month**, set for **March**, kept secret, *cosa segura, de poca costa e
  provechosa*, the Pope glad to see the troops leave his lands. An early form of the 1524 Provence campaign.
- **Key additions** (`key_1522_r9634.tsv`, read by `decode.py --letter`): `ɋ` = r (new sign); `z` after a code = plural
  s; `yob` ducado, `xep` mar, `xu` gente (conflicts 1524 `xu` = ha-), `zar∂` des-; `ʃil`, `ʃal`, `ʃop`, `xud`, `ʄ` (y)
  confirmed; **nulls after the opener `Ꮒ`**: `ʃta` confirmed (R9649 clear, R9634, R9646, R9656), `ɡʇo`/`ɣ̊ʇ`/`ʑto`,
  `ʆ∂`, `yt`, `yω` probable.
- `decode.py` gained a letter mode: `python decode.py --letter r9634` decodes `<letter>_cipher.txt` against this
  hand's key, the merged 1524 key and the 1522 codes, and prints confirmed/probable coverage and the unvalued tokens.

### Retry, same day: R9645 and R9656 with the extended key

| record | tokens | read as sense (measured) | before |
|---|---|---|---|
| R9645 ff. 243r-v | 489 | **358 = 73%** | 57% confirmed coverage / about 47% read (2026-09-21) |
| R9656 f. 334r-v | 214 | **131 = 61%** | about 47% (2026-09-21), 42% (2026-09-20) |
| R9634 (retry of its unread groups) | 1191 | **846 = 71%** | 842 |

- R9645 re-transcribed in the R9634 notation (`r9645_cipher.txt`); R9656 token file built from its 1524-notation tables
  (`r9656_cipher.txt`, not re-read from the image). `decode.py --letter` now also loads `key_1522_r9634.tsv` for every letter.
- The R9645 glosses confirm the null `ɣto` after `Ꮒ` (twice) and `xu` = gente (*la gente de v. mgd*); `yib` = duque is
  confirmed (*duque de Ferrara*, *duque de Albania*: the old yub = 'duque' conflict was a misread).
- R9645 f. 243r, which has no gloss, now reads as the terms of Adrian VI's capitulation with Ferrara (the feudo of
  Pope Alexander, a hundred men-at-arms for the Church, no league save with the Pope and the Emperor, no harbouring of
  their enemies in his state), matching R9646.
- The R9634 retry gained only two words (`xu` gente in 14v23, `yiL` hazer in 15r20): its remaining unread groups occur
  once and none of them recurs in R9645 or R9656 with a crib.

## Push toward a full reading, 2026-10-03

| letter | before (2026-10-02) | after (2026-10-03) |
|---|---|---|
| R9634 | 846/1191 = 71.0% | **872/1191 = 73.2%** |
| R9645 | 358/489 = 73.2% | **368/489 = 75.3%** |
| R9646 | 97/121 = 80% | **80%** (no change) |
| R9649 | 89/89 = 100% | 100% |
| R9656 | 131/214 = 61.2% | **177/225 = 78.7%** (re-transcribed from the image, below) |
| all five, token-weighted | 1521/2104 = 72% | **1603/2115 = 76%** |

What was tried, in order:
- **Better images: blocked.** DECODE re-checked with the logged-in cookie on 2026-10-03: the full-size `IMG_R9634_I45360_P1.jpg`
  (1,427,572 B, 3256 x 2365 for a two-page opening) is byte-identical to `img/`; `.png`, `.tif`, `ORIG_` and the
  page-less name return the 5,244-byte not-found placeholder. The RAH Biblioteca Digital now sits behind an Anubis
  proof-of-work bot check (`/.within.website/?redir=...`), which an automated session must not get past; a web search
  finds Salazar genealogy records there but no hit for 9/26 or A-26. **Daniel has to look in a browser**: search *Salazar
  y Castro A-26* or *9/26* and, if the volume is there, save ff. 14-16, 243-244, 252, 334-335 at full size into `img/`.
- **Codes pooled** across R9634, R9645, R9646, R9656 and the 1523-24 letters (`../lopehurtado1523/decode_merged.py --kwic`).
  Of the about 60 codes seen once, only `ze` (= el, four contexts), `zer` (= hazer), `yin` (= fue) and, weakly, `xer`
  (mucho?) and `zif` (capitan?) recur anywhere. The rest occur nowhere else in 21 letters.
- **Print cribs.** CSP Spain ii has no Hurtado letter for Sept-Nov 1522 (2026-09-21 search). Sanuto, *Diarii* t. XXXIII
  (archive.org `idiariidimarinos33sanu`, full text grepped for Provenza, Lion, Adorno, Urtado): no report of an
  Adorno/imperial plan to invade Provence in Sept 1522, so no crib for R9634. Not a word-level crib source.
- **Spelled words by lexicon** (`wordmatch.py`, new): each sign is expanded to every letter it has been read as in this
  hand (the 8/ϑ, ∂, ε, ɣ, 9 confusions included) and each expansion is looked up in a Spanish word list (Quijote,
  Vasto memorias, Gutenberg Spanish). Hits are accepted only when the sentence also takes them: *sostener*, *tenia*,
  *ser*, *vio*, *vivo* (R9634), *real*, *hara* (R9645). Nothing for R9646's or R9656's unread words.

**Why 95% is out of reach from here.** Of the 319 R9634 tokens still unread, about 60 are codes that occur once in the
whole corpus (no second context, no crib), and the rest are spelled words for which no expansion of the sign sets is a
Spanish word, i.e. at least one sign is misread at DECODE's resolution. Both need an outside input: the RAH images
(for the signs) or a clear copy / summary of these letters (for the codes). R9645 (f. 243r) and R9656 (ll. 13-18) are in
the same position; R9656 also needs re-transcribing from the image in the R9634 notation.

### R9656 re-transcribed (2026-10-03)

f. 334r and the f. 334v runs re-read from the images in the R9634 notation (`r9656_cipher.txt`): **78.7%** read as sense
(was 61.2%). The old `ʒ` was mostly `ɣ̊` = r, a "sign" closing l. 1 was a hyphen, and the f. 334v run now reads in full
against the faded copy: *que esta muy sospechoso el papa que de alla* (`zub`) *se le haya mandado lo que ha fecho*.
New values: `zub` = alla, `3` = h confirmed, `ʒ` = y and `⊤` = x probable. Details in `read_r9656.md`.

## Remaining gaps

- R9645 (75% read): tec, ʃen, the spelled words of f.243r ll. 5, 8, 14, 17 and f.243v ll. 1, 7, 10 - blocker: no-key-material; f. 243r and upper f. 243v have no gloss, codes seen once
- R9656 (79% read, re-transcribed 2026-10-03): ɲ4∠&ɣ̊ϑ (l. 6), ∂ɡ∂∂8 (l. 9), teɡ ∂ ϑ∠8ɣ̊oo (l. 13), ϙ8, 8x& (l. 14), ϯ7∂∂, ßϑ7, 30, f. 334v l. 1 tail, ∂∂8∂7 - blocker: illegible; no lexicon match under any reading of the signs; the f. 335r clear copy is legible only in its right half at DECODE resolution, and the spelled signs are at the scan's limit; RAH Biblioteca Digital blocked to automated requests
- R9634 (73% read, retried 2026-10-02 and 2026-10-03; codes pooled over 21 letters, Sanuto XXXIII and CSP ii searched): about 40 code groups seen once (ʃe, xer, zud, zac, ʃum, ʇudd, yat, zub, ʃof, zif yin, xen, zer, car ʒa, xas zɣ, yul ...) and yel (4x), ɣ̊e (4x), ʃun, ʃud - blocker: no-key-material; no clear version in the record and none in CSP Spain ii; one context each
- R9634 spelled words with every letter valued that give no word (14r12, 14v03 place names, 14v16, 15r11, 15v05, 15v12) and the force numerals of 15r05/15r09/15r10 - blocker: illegible; 8/ϑ (e/t), ∂ (s/p/t) and ε (l/g) not separable at DECODE resolution; no expansion of the sign sets is a Spanish word (wordmatch.py); DECODE has no larger file and the RAH Biblioteca Digital is behind a bot check (needs Daniel in a browser)
- R9646 (80% read): ʙ∠89&Ho, zip (run 4); zob, δ8ǝtoo, ʃof, ʙ∠47 ɣ?8δHo (run 5) - blocker: no-key-material; no crib, codes seen once; one misvalued sign in each spelled word
- Spelled runs in the ciphered leaves of R9644, R9648, R9650 (word-perfect edition) - blocker: illegible; same per-glyph limit; ten alphabet signs downgraded to probable
- Nomenclator codes not yet met in the uncribbed letters - blocker: no-key-material; no clear version for them; roughly half the tokens resolve

## Escalation

- [x] siblings: all nine records opened; R9648 is R9644's duplicate; R9652 is wholly clear; R9649 carries its own clear (f. 268), R9656 a faded one (f. 335)
- [x] clear-pages: R9644's clear (ff. 241-242, lettered sections), R9650 f. 272 and R9649 f. 268 aligned
- [x] known-keys (codes pooled over R9634, R9645, R9646, R9656 and the 21 letters of lopehurtado1523, 2026-10-03): the 1524 alphabet (targets/lopehurtado1523/key_1524.tsv, key_merged.tsv) applied back to R9656 f. 334 (2026-09-21) and to R9634, R9646, R9649 (2026-10-02); Juan Manuel's table (Tomokiyo 2025) still untested
- [x] print: Bergenroth CSP Spain ii (archive.org bub_gb_ZoY9AAAAcAAJ, full text) searched 2026-09-21: Hurtado letters calendared for 1522 are nos. 416, 422 (6 June), 454, 455 (26-27 July) only; nothing from Sept-Nov 1522 (Salazar A. 26 appears once, for Sánchez no. 488). The nine records here are not in print, so there is no CSP crib for R9634 (13 Sept, Genoa) or R9646. Sessa's 20 Nov despatch (no. 502) is the nearest contemporary context. 2026-10-03: Sanuto, Diarii t. XXXIII (archive.org idiariidimarinos33sanu) grepped for Provenza/Lion/Adorno/Urtado: no report of the Sept 1522 Provence plan, no crib
- [x] key-rebuild: crib alignment gave 49 confirmed code values and probable alphabet signs (key_codes.tsv), audited for conflicts; R9634 line-by-line reading added ɋ = r, plural z, yob/xep/xu and the null groups after Ꮒ (key_1522_r9634.tsv)
- [x] retry: R9656 f. 334 re-read in 1524 notation (2026-09-21) and regraded with the nulls and R9634 values (61%, 2026-10-02); R9634 transcribed and read, its unread groups retried against the R9645 values (71%); R9646 retried (nulls, oviese; 80%); R9649 measured (100%); R9645 re-transcribed in the R9634 notation and regraded (73%), all 2026-10-02
