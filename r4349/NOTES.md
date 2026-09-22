# Ciphered colophon of the Strängnäs Sequentiarium, 1517 (Uppsala UB C 513 f. 19v; DECODE R4349) — NOTES

**Verdict: the manuscript holds two ciphered pieces. The long one is read in full (already in print). The six-sign one,
which is what DECODE's note describes, is not read: it is too short.**

1. f. 19v, the scribe's dated colophon (1517): 125 letters in a vowel-shift cipher, set under chant notation. The Uppsala
   manuscript catalogue (1992) gives the rule and the reading. Transcribed here and checked; read in full.
2. f. 1r, a slip pasted in: a short private letter in Old Swedish (the catalogue says only "Anders Larsson receives
   medicines"). It closes "...til liff oth sel" followed by **six signs**, `ÿ ɑ M ÿ u ꝺ`. This is DECODE's "short
   ciphertext of six symbols out in a note" and its "unknown sender to unknown recipient". Not read: six signs, no key,
   no sibling. Probably a concealed signature.

A first pass took DECODE's note to be a garbled description of the colophon. A check of all 175 Alvin images (prompted
by the stop hook) found the slip. Worked in one session on 2026-09-22.

## Sources

- DECODE R4349, "Carolina-Rediviva-Uppsala-C513-Sequentiarium" (Non-decrypted, 1 p., graphic signs, public). Page
  saved as `rec4349.htm`. Its one "image" (`IMG_R4349_I26043_P.png`) is a 100×100 clock placeholder icon. Its document
  `DOC_4349_2023-Mar-15-08-56-53_11117.pdf` is two scanned pages (pp. 275-276) of the catalogue entry below. Both were
  fetched with the shared cookie into `img/` (git-ignored). DECODE's note, "A short ciphertext of six symbols out in
  a note", is wrong: the cipher is four lines of Latin letters, 125 letters in 19 words.
- M. Andersson-Schmitt, H. Hallberg, M. Hedlund, *Mittelalterliche Handschriften der Universitätsbibliothek Uppsala.
  Katalog über die C-Sammlung*, Bd. 5: *Handschriften C 401-550* (Stockholm 1992; Acta Bibl. R. Univ. Upsaliensis
  XXVI:5), pp. 275-276, C 513. It reads: "Die Hs. ist 19v in Geheimschrift datiert. Man hat den Vokal jeweils mit dem
  folgenden Konsonanten ersetzt: *Annp dpmknk* ist also als *Anno domini* zu lesen." It prints the full reading and
  says that the inscription is "mit Noten versehen" (set to music). The same page records the book's other facts:
  84 paper leaves, Strängnäs 1517, one early-16th-c. cursive hand, and an owner's entry *Liber conuentus insulensis
  ordinis predicatorum* (the Västerås Dominicans). A later hand in Västerås, "who evidently could not interpret the
  ciphered dating", ascribed the book on f. 20v to Frater Gudmundus Benedicti, c. 1520.
- The catalogue's literature: Collijn, NTBB 4 (1917) pp. 71-72; Moberg, *Sequenzen* (1927) pp. 17-19 (plate of
  f. 11r); Hedlund, *Katalog der datierten Handschriften* I (1977) p. 56, pl. 165; Frithz 1968. Not checked here for
  the decipherment. The catalogue reading is enough to settle the prior-art question.
- Scans: Alvin, `alvin-record:193385` (Public Domain Mark). **f. 19v is attachment 42** and f. 18v is attachment 40.
  The full-size TIFF is `https://www.alvin-portal.org/alvin/attachment/document/alvin-record:193385/ATTACHMENT-0042`
  (3618×4771, 35 MB). Plain curl works; the browser meets an Anubis check first. Copies are in `img/alvin/` (ignored).

## The folio

f. 19v ends the sequence *Benedicta sit celorum regina* ("...det nobis paratum in celesti patria Amen"). Then comes
the colophon, in the same hand, on four text lines under four staves of square notation, so the scribe wrote the date
into the book as though it were a chant. A red catchword *Corda manibus* follows, the next sequence (f. 21r).

## Transcription (`ciphertext.txt`)

```
Annp dpmknk mkllfskmp qxkngfntfsk-
mp dfckmp sfptkmp prfsfns lkbfr sf-
qxfnckpnbrkxs fst scrkptxs kn cpnxfntx
strfngfnfnsk prp cpnxfntx knsxlfnsk
```

- The initial A is a rubricated capital (red stroke) and is **not** enciphered. It is the only plain vowel.
- The minims after it could be read m or nn. The rule needs `nn` (Anno), which is also the catalogue's reading.
- In the first `cpnxfntx` (l. 3) the n is carried by a macron over *cp*. The second (l. 4) is written out.
- The letter the scribe uses for `k` is a tall form joined to the next letter. It is still a k: it is the only
  letter where the rule predicts k, and it never occurs where plain i is impossible.

## The rule

The alphabet is a b c d e f g h i k l m n o p q r s t u x y z (i/j and u/v one letter each). Each vowel is replaced
by the letter after it:

| plain | a | e | i | o | u |
|---|---|---|---|---|---|
| cipher | b | f | k | p | x |

Consonants are unchanged, and word division and doubled letters are kept. So the cipher is two-valued where a vowel's
substitute is also a consonant of the text: cipher **b** = a or b (*lkbfr* = liber), **p** = o or p (*scrkptxs* =
scriptus, *prfsfns* = presens, *prp* = pro), **f** = e or f (no plain f occurs). k and x are never plain consonants
here. This is the old scribal "vowel to next letter" trick, known from early medieval manuscripts. It needs no key.

## Reading (`decode.py` → `reading.txt`)

`decode.py` fixes k=i and x=u and chooses b/f/p by a beam search over the whole colophon under the shared Latin model
(`lang` model `la`). A word-by-word first pass misread k (the model folds k into c) and gave *oro* for *prp*. With
sentence context, every word matches the catalogue:

> Anno domini millesimo quingentesimo decimo septimo presens liber sequencionarius est scriptus in conuentu
> strengenensi pro conuentu insulensi.

"In the year of the Lord 1517 the present sequentiary was written in the convent of Strängnäs for the convent of
Västerås" (*insulensis* = the Dominican house of Västerås; the catalogue glosses "sc. Dominikanerkonvent in
Västerås"). 125 of 125 cipher letters have a value (100%), and all 19 words read as sense. Nothing is open.

## DECODE corrections (queued)

Status Non-decrypted → Partially decrypted: the colophon is read (in print), the six signs are not. Date 1517 for the
book; the slip is later, undated. Place: Strängnäs Dominican convent, written for Västerås. Language: Latin
(colophon), Old Swedish (slip). Symbols: alphabet. Cipher type: simple substitution (vowel shift) for the colophon.
The six-symbol note is the pasted slip on f. 1r (Alvin attachment 3), a letter to Anders Larsson, and the colophon on
f. 19v (attachment 42) is a second cipher on the same manuscript. The only image on the record is a placeholder.

## The slip on f. 1r (Alvin attachment 3) and its six signs (`slip.txt`, `signs.txt`)

A strip of paper pasted over the top of f. 1r (it hides part of the first staves), in a post-medieval cursive. It is a
private letter in Old Swedish, a first transcription (`?` = uncertain):

```
thetta skal wal[?] larens?+ andhers hess? / lass son wara andhers y brygghe stuffuan  [+ skriffue interlined]
kære hertans brodher andhers larsson h[elsa]? / sändher yagh edher littit örther til edher / brysth kanelbark men
yak ffruchthar ath / han är gammal kære brodher edhra / [w]älgärningar? är yak ffor ringa til at betala / hwilket yak
tager then effuige gudh / til help then yak edher beffaller til / liff oth sel  ÿ ɑ M ÿ u ꝺ
```

"...[to] Anders Larsson in the brewhouse. Dear heart's brother Anders Larsson, I send you a few herbs for your chest,
cinnamon bark, but I fear it is old. Dear brother, your kindnesses I am too poor to repay, which I leave to the eternal
God, to whom I commend you in life and soul." Then the six signs, where a signature would stand. They look like
cursive letters of the same hand (ÿ as in *yagh*; ꝺ is the hand's looped d, as in *edher*), in two groups of three,
each group opening with ÿ.

Tried, all without a reading: the colophon's vowel shift (none of b f k p x occurs); all 23 shifts of the alphabet on
five readings of the signs (yamyud, yamymd, yanyud, yamynd, iamiud); a plain abbreviation (initials of a name, a closing
formula). Six signs with two repeats cannot fix a substitution, and nothing else in the book is in the same hand.

## Remaining gaps
- the six signs closing the f. 1r slip (ÿ ɑ M ÿ u ꝺ) - blocker: too-short; six signs, no key, no sibling in the same hand, no crib beyond "a signature stands here"

## Escalation
- [x] siblings: DECODE has no other record from this manuscript or from Carolina Rediviva in this group; all 175 Alvin images of C 513 checked; the only other writing is pen trials on the back pastedown (an alphabet, "Thögmersdage Thögbane"?), clear
- [x] clear-pages: the slip's own clear text read; it gives the context (a signature) but no crib for the letters
- [x] known-keys: the colophon's vowel shift applied; no b/f/k/p/x among the signs, so it does not fit
- [x] print: the Uppsala catalogue (1992) describes the slip without the signs; Collijn 1917 not checked
- [x] key-rebuild: all 23 alphabet shifts on five readings of the signs; nothing
- [n/a] retry: nothing reads, so nothing to regrade; six signs cannot be retried to a unique reading
