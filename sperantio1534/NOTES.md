# Two ciphered letters in the Sperantio file, BayHStA KAA 4591 ff.248, 250–251 (DECODE R9411, R9412)

Status: read in part (R9411 read; R9412 read in part, gaps illegible)

Catalogue entry 163, "Cornelio Sperantio to …, 2 ciphertexts". DECODE R9411 (f.248r–v, 2 pp. of cipher) and
R9412 (ff.250r–251r, 3 pp. of cipher, cover f.251v). Same key volume as `kaa4591/` (catalogue 161) and
`kaa4591b/` (catalogue 162); kept apart because the catalogue lists it apart.

Images: DECODE, login only. DECODE's rights line: "The image is not in the public domain. Publishing it is only
possible with the permission of the Archive"; no permission asked, so the JPEGs stay in the untracked `img/` and
the site page carries no image figures.

This folder merges two sessions of 22 Sept 2026 that worked on the target independently: one inside
`kaa4591/r9411/` (now `r9411/` here: the gloss-based key, both readings, all passes on R9412), one as
`sperantio1534/` (the identification with System L of R9415, a second full transcription and a word-fitting
reading). The first session's readings are the ones kept; the second is recorded as a control.

## What the two records are

DECODE has the direction wrong. The cover (f.251v) reads "Cornelio Sperantio etc. domino observandissimo":
Sperantio, the dukes' man at Buda, received the packet. Neither letter is his.

| Record | Folios | Date | Language | What | State |
|---|---|---|---|---|---|
| R9411 | 248r–248v | Buda, 6 Feb 1534 ("Bude sexta Februarii, anno etc. xxxiiii", in cipher, glossed) | Latin | King John (Zápolya) of Hungary to the dukes of Bavaria | **read**, 96% of words (357 read, 13 gaps) |
| R9412 | 250r–251r | Ofen (Buda), 8 Feb [1534] ("Datum Ofen, des achten Februarii") | German, Latin passages in clear | an agent at Buda to a duke of Bavaria | **read in part**, 95.0% of words with 37 editorial supplies, 89% without |

The second session dated R9412 "22 December [1533]" from the "xxii Decembris" in line 1. That date belongs to
the earlier letter it repeats ("des xxii Decembris hab ich Eurn G. dergleichen newe zeittung geschriben"); the
letter's own date is at the foot, l.63–64.

## The cipher and key

Homophonic substitution on the graphic sign set of the volume (↓ ω π 4 8 ÿ …), no word division, clear Latin
passages left standing ("quod negocio", "Ceterum", "Misimus nunc", "Et primo", "Secundo", "Tertio", "Quarto",
"Sed tamen per maximos suos conatus…", "Tantum de isto negocio…").

R9411 carries a contemporary interlinear Latin decipherment over every cipher line (checked on the image,
f.248r). The key was fixed from it by constrained annealing (`r9411/solve.py`, `r9411/run7.txt`), then applied to
R9412 and refitted on German (`r9411/run_r9412_R6.txt`):
w/4 e, q n, v r, x/L s, 5 a, 3 u, y t, 7 m, m i, c c, 9 o, d l, 6 d, 8 n, D f, P z (up-arrow cross), b h
(lollipop), A b, K rr, S g/q, Y ll; polyphones π b/w/o, 4 e/i, ∃ d/ch, double stem H u/v/k/g; word and pair
signs 2o = et/und, oo = q(u), r+ = sch, ro = h, a+ = der; ‡ before :: is a paragraph null. Language decides the
pair signs (et in Latin, und in German).

This is the key the second session called **System L**, rebuilt in `kaa4591b/` for R9415 (18 April 1533, King
John's side to the dukes): its values agree sign for sign on the common signs (w e, x s, 3 u, v r, y t, q n,
5 a, 7 m, 9 o, 8 n, d l, 6 d, D f, c c). The Sperantio file and R9415 are one correspondence, in one cipher.

## R9411 (f.248r–v), King John to the dukes of Bavaria, Buda 6 Feb 1534 — read

Reading: `r9411/reading_r9411.txt`. He will do whatever he can for the dukes, "fratres et amicos"; their request
must first go to "illustri domino regni nostri gubernatore" (Lodovico Gritti), expected shortly, rather than be
tried abruptly with the Turkish emperor; the news his adversaries spread is false. Through his captain and
councillor he has begun on the gold and silver mines, "quae res nobis vehementissime fuit cordi", and sends his
servant **Nicolaus Freiberger** to the dukes; he invites them to take on the labour and working of such mines,
asks for masters skilled in them, and asks for the Bavarian mining ordinance ("ordinacionem rerum montanarum")
by a sure messenger. "Datum ut supra."

## R9412 (ff.250r–251r), Ofen 8 Feb [1534] — read in part

Reading: `r9411/reading_r9412.txt`. Repeats news sent by an unsure messenger on 22 December: what the chancellor
Stephan Werbőczy obtained at the Porte. *Et primo*: an everlasting peace between Hungary and the Turk.
*Secundo*: towns and places to be handed over, "als nemlich Peterwardein … Titil, Salankamen". *Tertio*: the
quarrels over the kings' titles and the frontier towns. *Quarto*: the Sultan's letter; "Sed tamen per maximos
suos conatus nihil aliud impetrare potuit quam illud quod". Then plans against Siebenbürgen; the mines:
Fridrich Schmalcz, his factor at Nuremberg, "berckverstendig, zu Pest", "herr Caesar" at Vienna; a bishop's
greetings in clear Latin. The b/w and d/t pairs are not separated by the cipher (beczi = Werbeczi).

Outcome: **read in part**. R9411 read (96%); R9412 95.0% of words with 37 editorial supplies, 89% counting only
what the cipher yields. Over both letters, 915 of 996 words read from the cipher (92%). Key recovered.

## The second session (control)

`transcription.txt` (4,745 signs, both letters), `key.txt` (System L seed), `dec.py`, `fit.py` (Viterbi fit of
corpus words to the sign stream), `fit248*.txt`, `fit250*.txt`, `reading248.txt`. It reached R9411 at 91% without
using the gloss, and R9412 as running German with local errors. Its hill-climbs (`solve.py`) failed twice. It
confirms the key independently of the gloss; its readings are superseded by `r9411/`.

## Remaining gaps

- R9412 clean reading - blocker: illegible; 31 words unread and 37 supplied: the second Danube fortress (l.10),
  "Caiianer" (l.44), the bishop (l.56), Schmalz's factor's name (l.51), the signature (l.65), about twenty single
  words at blotted signs. Three transcription passes, a 2.4x zoom pass on the names, a gap-level sign search
  (`r9411/gapfix.py`), two look-alike repairs (`confuse.py`) and two lexicon optimisers (`lexopt*.py`) were tried;
  the automated ones raise their objective while making the German worse and were rejected. A second, independent
  transcription (the control above) does not read these places either. What is left needs better images.
- R9411 13 short gaps - blocker: illegible; single words at blotted signs, and the captain's name on l.19, where
  the gloss is also faint.

## Escalation

- [x] siblings: R9415 (System L, kaa4591b) has the same key; System A′ letters R9408–R9413 used as parallel text
  for R9412 (they read worse, no help); R9413 key compared (16 signs agree, a different key).
- [x] clear-pages: R9411's own interlinear gloss gave the key; the only other gloss (f.251r) is the dating clause.
- [x] known-keys: System L (R9415) and System A′ (R9427 gloss key) tried; System L fits unchanged.
- [x] print: web search for KAA 4591 / Sperantio / Zápolya 1534 cipher letters, a printed Bavarian-Hungarian
  mining correspondence and Nicolaus Freiberger: no edition, no prior decipherment.
- [x] key-rebuild: constrained annealing from the gloss (Latin), refits on German (free, joint, seeded with
  ch/sch); hill-climbs from the System L seed (failed twice, seed kept).
- [x] retry: three transcription passes over R9412, gap-level sign search, look-alike repair, lexicon optimisers,
  an interpretive pass (84% → 89% → 95.0%), and an independent second transcription with a Viterbi word fit.

## Steps

- 2026-09-22 (session A, in `kaa4591/r9411/`): transcribed both letters from line crops; key from the R9411
  gloss; R9411 read 96%; R9412 84%, then five further passes to 95.0% (commits ddb522cd4 … b3f7649ea).
- 2026-09-22 (session B, as `sperantio1534/`): System L of R9415 applied unchanged; full second transcription;
  hill-climbs failed; Viterbi word fit; R9411 91% (commit e65051696).
- 2026-09-22: the two merged here; R9412 redated to 8 Feb 1534; gloss on f.248r confirmed on the image.
