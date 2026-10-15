# Galgano Borghesi to Leonardo Benvoglienti, Naples, 12 May 1456 (ASSi Concistoro 2308 fasc. 2 no. 4, DECODE R4793)

Status: read in part — key rebuilt from an alphabet fragment and the recipient's glosses on the letter; 114 of 144 cipher signs (79%) read.

Split on 14 Oct 2026 from `siena1421` under the one-key rule (George Lasry, 14 Oct 2026). The old entry grouped the
whole bundle of Sienese cipher letters (Concistoro 2308 fasc. 2), each in its own key. This letter has a key of its
own; the other letters with recovered keys are their own entries, each a different cipher with its own page: no. 25
([`targets/siena25/`](../siena25/NOTES.md)), no. 18 ([`targets/siena18/`](../siena18/NOTES.md)), no. 14
([`targets/siena14/`](../siena14/NOTES.md)), nos. 6 and 24 (George Lasry's [`targets/siena1431/`](../siena1431/NOTES.md)).
The unread pieces, the key index (with the transcribed 1450s keys `keys/R47xx.txt`) and the shared solvers stay in
[`targets/siena1421/`](../siena1421/NOTES.md). The work below was done on 24 Sept 2026 and is carried over from its NOTES.

Work date: 2026-09-24. From catalogue 336 (now narrowed to the unread pieces).

## The document

ASSi Concistoro 2308, fasc. 2, no. 4 (Meister's dated anchor: 1456), DECODE R4793 (`IMG_R4793_I27928_P2.jpg`, 2248 x
4000; ASSi, git-ignored). Galgano Borghesi, J.U. doctor and orator, at Naples to Leonardo Benvoglienti, 12 May 1456.
Senatore 2009 ("Callisto III nelle corrispondenze diplomatiche italiane", Revista Borja 2) cites "Concistoro 2308, c. 4,
da Napoli, 12 maggio". (The 24 Sept notes once wrote 17 May; the heading and Senatore give 12 May.)

## Cipher and key

- Clear Italian letter with 15 cipher runs (144 sign tokens) and 9 Latin code words; a second (recipient's) hand wrote
  interlinear glosses over some runs ("duca", "papa", "per la", "presto", "chercavano", "e cardinali", "pigliasse",
  "per parte del duca", "al re"): the contemporary partial decipherment behind the 1952 inventory's "solo parzialmente
  decifrate". Transcription: `transcripts/no04.txt` (agent G).
- None of the six 1450s keys filed in fasc. 1 (R4750, R4753, R4754, R4756, R4757, R4762; transcribed in
  `targets/siena1421/keys/`) gives the letter values, though R4757 shares sign shapes and the code word Calor (there =
  Florentini) and R4750 has 'storps'.
- A two-row **alphabet fragment written below the letter's text** (i o_tail, l longs, m 2, n a, o T, p M, q S, r g_ring,
  s y, t L_slant, u C; left part torn) plus the glosses rebuilt the key (`keys/no04_key.txt`): 114/144 sign tokens read
  securely (79%), 11 more from context, 19 unread (1, //, 8, F, x_slash, T_long, 4_hook, +, R, delta, B, b°). Code
  words: Calor = duca, storps = Lucca (per the gloss), cras = parte, Matto/Maffo = papa, toffe = papa?, vapor =
  cardinali?, pedesi = ?.

## Reading

Sense (tentative; `transcripts/no04_reading.txt`): Borghesi asks Benvoglienti to use the cipher; at his urging King
Alfonso wanted the settlement to include the promises made when Lucca was besieged by the Florentines ("al capitano ...
a Milano"); the King made light of it ("Tunc rex parvi fecisse"); Antonio d'Arezzo reports the Duke well disposed; the
Pope, the Florentine clergy ("chericato de Fiorentini") and the cardinals to contribute "contra lo Turcho"; the Duke's
message to be referred "al re".

## Validation

Not applicable (`docs/_validate.py borghesi1456 --na`): 144 signs in 15 short runs is too little for the shuffled-text
test; the key is attested by the fragment written on the letter.

## Remaining gaps
- 19 rare signs and the code words toffe, vapor, pedesi - blocker: too-short; each occurs once or twice; the fragment is torn on the left and no filed key fits

## Escalation
- [x] siblings: the whole busta opened; no other letter in this key found
- [x] clear-pages: the alphabet fragment below the text and the recipient's glosses used (they are the key)
- [x] known-keys: R4750, R4753, R4754, R4756, R4757, R4762 transcribed and tested sign by sign; none fits
- [x] print: Senatore 2009 identifies the letter; no printed decipherment found
- [x] key-rebuild: key rebuilt from the fragment and glosses, extended from context
- [x] retry: every run re-read with the extended key; doubtful readings marked in the reading file
