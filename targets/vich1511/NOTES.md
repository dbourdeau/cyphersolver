# Ferdinand the Catholic → Jerónimo de Vich (Rome), AHN Estado 8714/8715

PARES search "Vich cifrada" lists the ciphered letters in the Vich family archive (AHN, Archivos privados):

| Signature | Date | PARES id | State |
|---|---|---|---|
| 8714 N.12 | 1508-09-30 | 12751356 | cipher + contemporary decipherment |
| 8714 N.26 | 1509-07-28 | 12751370 | cipher + decipherment |
| 8714 N.39 | 1510-05-13 | 12751383 | cipher + decipherment |
| 8715 N.41 | 1510-05-22 | 12751386 | cipher + decipherment |
| **8715 N.45** | **1511-04-04** | 12751390 | cipher only — **read here** (Seville) |
| 8715 N.46 | 1511-07-05 | 12751391 | cipher + decipherment (key source) |
| 8715 N.52BIS | 1512-03-01 | 12760824 | cipher + decipherment (key source) |
| **8715 N.57** | **1512-06-05** | 12751402 | cipher only — **read here** (Burgos) |
| **8715 N.60** | **1512-09-01** | 12751405 | cipher only — **read here** (Logroño) |
| 8715 N.73 | 1515-10-26 | 12751418 | cipher only — **different key, not read** (Pedrezuela) |
| 8715 N.74 | 1519-01-30 | 12751419 | Charles I, cipher + decipherment, another system |
| 8715 N.79 | "1500" | 12751424 | "Clave de cifra": a plain letter→sign table, not the key to any of these |

**Caveat on prior work.** The Barón de Terrateig, *Política en Italia del Rey Católico 1507–1516.
Correspondencia inédita con el embajador Vich* (CSIC, Madrid 1963, 2 vols.) edits this correspondence.
I could not consult it (the one online review returns HTTP 403), so whether he printed texts for
N.45/N.57/N.60 is unverified. PARES itself records no decipherment for them, and no text of them was
found online.

## The 1511–12 cipher

One key serves N.41, N.45, N.46, N.52BIS, N.57 and N.60. It is a nomenclator:

- **A homophonic alphabet** of figures and marked letters — `40` r, `4h`/`3` e, `ah`/`T` o,
  `to`/`7`/`b` a, `ch` c, `oo` d, `11`/`W` n, `X`/`g`/`9` t, `d`/`eh` s, `q` m, `o` g, `O` h,
  `mt`/`SS`/`P` p, `tt` r. Words not in the code are spelled out with these.
- **Code groups**, three letters, for words *and* for syllables: `pef` que, `diz` de, `dih` con,
  `fak` el, `hor` la, `has` lo, `raf` por, `rif` porque, `mix`/`mye` papa, `fef` emperador,
  `sap` venecianos, `fio` ferrara, `fuq` francia, `dur`/`dox` duque, `hib` guerra — and syllabic
  ones like `pob` si (in *si-t-io*), `flart` me (in *pri-me-ras*), `mik` no (in *me-no-r*).
- Full list: `key.md`; machine-readable in `decode.py`; 153 groups recovered.

**How it was recovered.** N.46 and N.52BIS carry the clerk's decipherment on the following leaves.
Lining the two up word by word gives the alphabet and the common groups; the readings of N.45, N.57
and N.60 then supplied the rest. Two traps: `fug` (señor) and `fuq` (Francia) are near-identical, as
are `plart` (mi) and `plort` (al); and the barred q is m in most places but a in a few, so there are
probably two similar signs that this transcription merges. The transcribers of N.45 and N.60 also read
`plort` differently (al / mi), so that group and its neighbours `plart`, `flart`, `flort` need one
careful pass against the images before they are trusted.

## What the three letters say

**N.45 — Seville, 4 April 1511** (378 lines, ~5% still unread; `n45_pp*`). A long complaint against
Julius II and a set of instructions. Ferdinand is angry at the publication of the new cardinals, at the
Pope absolving the Venetians and treating with them "sin dezirme ni comunicarme", at the priory of San
Juan, and at the Pope's refusal to follow his counsel, from which followed *la rota* of the papal army.
Then the business: press the **Emperor–Venice concord** (with draft terms — Padua and Treviso to stay
with Venice in fief against tribute; Verona, Vicenza, Riva, Rovereto, Peschiera to the Emperor), settle
**Ferrara**, keep the Pope's army in a safe place, and deliver orders to **Fabrizio Colonna** under an
enclosed letter of credence. He warns that France is offering him a separate perpetual alliance without
the Emperor and that he will not take it, and that a rupture would wreck his crusade against the Moors.

**N.57 — Burgos, 5 June 1512** (35 lines, ~7% unread; `n57_*`). The aftermath of **Ravenna**
(11 April 1512). Ferdinand reconstructs how his army was pushed into battle: Vich's own letters, and
the papal side, pressed the viceroy Ramón de Cardona, saying that **if they did not fight, the Pope
would not meet the pay and would come to terms with France** — against Ferdinand's repeated written
orders not to risk a battle. "Las cosas de guerra es muy peligroso [para] los que están ausentes
dellas; siempre se ha de remitir a los que las tienen presentes." Do not do it again, he says, or it
would be *echar la soga tras el caldero*. Then: get the Pope and the Venetians to pay their share, push
the Emperor's business to a conclusion, and **treat the Ferrara business secretly, "sin que la sienta
el Papa"**, reporting back so he can give orders.

**N.60 — Logroño, 1 September 1512** (432 lines, ~14% unread; `n60_pp*`). Written from the Navarre
campaign, and the weightiest of the three.

- **Reproach to Julius II** (pp. 3–5). The bulls Vich had sent; the Pope acting "en quebrantamiento de
  lo que tiene asentado"; Ferdinand's account of what he has spent "por tierra y por mar" to rescue the
  Pope, the Church and Italy, and of the Pope's ingratitude in not paying his troops as the League
  requires. He traces it to the Pope's suspicion "que el Emperador y yo nos [hemos de apoderar] de
  Italia, no siendo assí la verdad", and tells Vich to remove that suspicion; he will persevere
  "constantíssimamente" all the same.
- **The Sforza restoration in Milan** (pp. 6–8), the core of the letter. The Emperor and Ferdinand agree
  that **Massimiliano, son of Duke Ludovico**, be put into the state by the Emperor's hand, precisely so
  that Pope and Venice lose the suspicion that Milan is being taken for the Emperor; the essential
  article is that possession of the state and its fortresses be taken "sin dilación". A marriage for the
  infante **don Fernando** with "la fija de la duquesa de Milan" (so the decode; the notes earlier said
  the duke's daughter) is in view.
- **Venice and the papal claims** (p. 9). Venice should not be barred from recovering its old terraferma
  towns, or it will not pay; the Pope, however, is trying to appropriate **Parma, Piacenza, Modena and
  Reggio** against the capitulation of the League — "ninguno de los de la liga haga cosa en perjuizio de
  otra".
- **Spiritual war on Louis XII** (pp. 10–11). Ferdinand wants "las armas espirituales": the king
  deprived of his crown and of **Guyenne and Normandy** — assigned to England — as a "príncipe fautor y
  receptador de cismáticos y heréticos", his subjects absolved of obedience, crusade granted against
  him, citing precedents against the Emperor Frederick and King Pedro. Send me the bull, he says.
- **Money, and Milan before Ferrara** (pp. 12–15). Pensions of fifty thousand ducats a year in all to
  hold an Italian power steady, "y no se olvide de aqueste artículo, que es muy sustancial"; and if the
  Pope insists on starting with Ferrara, Vich is to insist on finishing the French in the state of Milan
  first, plus a mutual-defence arrangement securing each member of the League in its Italian state.

**Checks.** The key was built from N.46 and N.52BIS alone and then read three letters it was not built
from. Each letter's place and date come out of the clear-text subscription and match the catalogue
(Seville, Burgos, Logroño). The contents fit their dates independently: the March 1511 cardinal
promotion, Ravenna, the Navarre bulls. In N.57 the proverb *echar la soga tras el caldero* is mostly
spelled out letter by letter (it does use `fak` el and `plort` al in c-al-dero, which supports `plort` = al
against the N.60 transcriber's mi).

## N.73 (1515) — not read

`n73_transcription.txt` (124 lines, 3,177 tokens, 197 distinct) and `n73_freq.txt`. It is a different
system: mostly three-letter code groups (`sin` 151, `sud` 97, `no` 93, `zre` 89, `xed` 68) with a
smaller set of signs (`X` 171, `TH` 170, `PHI` 163, `RH` 151). No deciphered sibling exists for it:
the nearest, N.74 of 1519, is Charles I's and is a third system (its `sex` = papa, `mod` = tiene,
`sin` = de). Attacks tried and failed (`solve73.py`, `solve73g.py`): annealing against the repo's
Spanish 5-gram model with the lowercase groups split into letters, as whole units, and as context
breaks around symbol runs. All gave ~-2.7 to -3.5 per character with seeds disagreeing — no solution.
Symbol runs are short (median 3), so there is little for an n-gram model to hold onto; this one needs a
crib or a sibling. Its clear text: docket "a 26 de octubre 1515", opening "videlicet iterum", ending
"en Pedrezuela a xxvj de otubre de dxv".

## Files

- `pares.py` search/image client; `lines.py`, `half.py` page-to-strip cutters.
- `n45_pp03-09.txt`, `n45_pp10-15.txt`, `n57_transcription.txt`, `n60_pp03-09.txt`,
  `n60_pp10-15.txt` — transcriptions in ASCII glyph labels (legend at the head of each).
- `*_decoded.txt`, `n57_decode_v3.txt` — decodes; unread groups print in [brackets].
- `decode.py` the key, `key.md` the human-readable key.
- Images are not committed; re-fetch with `python pares.py img <pares-id> <prefix>`.

## Open

- ~5–15% of groups per letter still unread; the untouched decipherments (N.41 and the three in 8714)
  would close most of them.
- The q = m/a sign split, and `plart`/`plort`, want a careful re-reading against the images.
- N.73 (1515) needs a different approach.
- Whether Terrateig 1963 already printed any of this. Search of 18 Sept 2026 (snippets only): vol. II prints
  Ferdinand's letters to Vich from AHN Estado as numbered documents, with plates of ciphered letters and their
  decipherments; no snippet or citation names 4 Apr 1511, 5 June 1512 or 1 Sept 1512. Unresolved: assume it
  may print them until the book is seen.

## 5 Oct 2026: siblings N.41, N.39, N.12 aligned

- **N.41** (22 May 1510): cipher transcribed (`n41_transcription.txt`, 2,758 tokens) and its clerk decipherment
  (`n41_clear.txt`); alignment in `n41_align.tsv`.
- **8714 N.39** (13 May 1510): pp. 5-6 cipher (1,365 tokens), pp. 1-4 the clerk decipherment; `n39_*`.
- **8714 N.12** (30 Sep 1508): p. 3 cipher (720 tokens), p. 1 its decipherment; `n12_*`.
- **8714 N.26**: PARES serves one image, a clear letter; no cipher online.
- All three use the 1511-12 key unchanged (no sign or group contradicts decode.py). Added ~85 groups (poi rey de
  francia, pum Roma, plirt ni, sol todos, gue alla, mox principes, pep remedio, fil ellos, sul tambien, oto qu ...)
  and signs `q1` a (single-barred q, distinct from barred `q` m: this is the "barred q = a" puzzle),
  `11h` l, `6h` u, `qto` l, `B8` b, `pi` m; `N`, `/`, `9to` are sentence marks. Doubtful values left out
  (flort, dux, hiz/nos, rof/pero, fub/fuerças).
- Measured (`measure.py` token coverage, `measure_sense.py` attested-word share):

| letter | tokens covered before | after | sense words |
|---|---|---|---|
| N.45 | 0.974 | 0.983 | 0.855 |
| N.57 | 0.965 | 0.974 | 0.860 |
| N.60 | 0.925 | 0.940 | 0.802 |
| N.41 / N.39 / N.12 | - | 0.971 / 0.948 / 0.992 | 0.871 / 0.821 / 0.831 |
| all incl. N.73 | 0.83 | 0.862 | |

  The sense measure undercounts letter-spelled words (the clean N.12 decode scores 0.83), so it is a floor.
- What did not move: N.60's open groups (`2` x101, `flort` 56, `gz` 37, `phi` 36, `reg`, `fiy`, `mat`, `goi`)
  occur in none of the deciphered siblings. `flort` conflicts (N.12: pro-flort-tido = me, and "aquella flort delos
  quatro" = confe[deración]); in N.60 "por la [flort] es [mat]" reads naturally as "por la liga es obligado", but
  that is a context guess and is not counted. N.60 also has letter-level garbles (ma[flort]nte, nauallbt) that
  need a re-transcription against the images, with q1 separated from q.
- N.73 (3,177 tokens, other key) alone caps the target at ~0.90 even with every 1511-12 token read.

## 5 Oct 2026 (second pass): N.60 re-transcribed, q/q1 split in N.45 and N.57

- **N.60 v2** (`n60_transcription_v2.txt`, 433 lines, 11,592 tokens, 97 doubtful): a new reading from the images.
  Pages 3-6 were read at 4-5x, pages 7-15 only at 2x. About 52 B labels were carried over from the old file.
  It has 108 q1 and 77 q.
  - Old `2` is the y-sign `&` (179 in all).
  - The old `&` is a different sign, `ang`, a clause mark (not given a value).
  - `&2` = x (ma-x-imiliano, about 12 times).
  - Values forced by context and added to decode.py: flort liga, fiy favor, fuy exercito, mat obligado.
  - Still open: gz (77 tokens, clause-final, perhaps a mark), phi (68), reg, goi (aquel? medium), sid (son? medium).
  - Several old garbles survive unchanged (nauallbt, brantbt; some "por la [flart] me" where flort/liga is meant).
    A 4-5x pass over pp. 7-15, and over the flart/flort spots, is still owed.
- **q/q1 split** (`n45_pp*_v2.txt`, `n57_transcription_v2.txt`, `qwork/q_decisions.tsv`): all 151 q checked on the
  images, 69 relabelled q1. Image and sense never disagreed. There are 8 no-bar cases, and 2 q1 are missing from the
  transcription (L0426, L0429).

| letter | tokens covered, start of day | after both passes | sense words, first pass | after |
|---|---|---|---|---|
| N.45 | 0.974 | 0.984 | 0.855 | 0.858 |
| N.57 | 0.965 | 0.976 | 0.860 | 0.865 |
| N.60 | 0.925 | 0.948 (v2) | 0.802 | 0.824 |
| all incl. N.73 | 0.83 | 0.865 | | |

## Remaining gaps
- N.73 (26 Oct 1515, 3,177 tokens) - blocker: no-key-material; different system, no deciphered sibling (N.74 is a third system); annealing with Spanish 5-grams failed
- N.60 open groups gz, phi, reg, goi, sid and surviving garbles - blocker: not-attempted; groups absent from every deciphered sibling; v2 pp. 7-15 read at 2x only, a 4-5x pass is owed
- 8 no-bar q tokens in N.45, 2 q1 missing from the transcription - blocker: illegible; q/q1 split otherwise done (qwork/q_decisions.tsv)

## Escalation
- [x] siblings: N.46, N.52BIS, N.41, 8714 N.39 and N.12 aligned with their decipherments (5 Oct 2026); N.26 has no cipher online
- [x] clear-pages: the clerk's decipherments on the leaves after N.46 and N.52BIS aligned word by word
- [x] known-keys: N.74 (1519) system and the N.79 table compared; neither fits N.73
- [ ] print: not done — Terrateig, Politica en Italia del Rey Catolico (1963) vol. II not seen
- [x] key-rebuild: 153 groups recovered from the sibling crib and context readings
- [x] retry: N.45/N.57/N.60 re-decoded with the extended key (5 Oct 2026); token coverage 0.983/0.974/0.940
