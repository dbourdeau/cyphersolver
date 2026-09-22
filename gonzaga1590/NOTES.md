# Vincenzo Gonzaga (Mantua) to Louis de Gonzague, duc de Nevers, 17 Sept 1590 — BnF fr. 3979 ff. 92–93, DECODE R4176

Status: in progress

Session of 21 September 2026. Catalogue entry "Vincenzo Gonzaga, duke of Nevers → Louis Gonzaga". The sender is
Vincenzo I Gonzaga, **Duke of Mantua** (DECODE's "duke of Nevers" for him is a slip), writing to his uncle Nevers.
Italian clear letter with long passages in unseparated two-digit figures, 3 written pages (DECODE images P1–P14:
P1/P5/P9/P12 are 1024-px page overviews, the rest high-resolution strips). Images git-ignored in `img/`.

## Key

Tomokiyo's Nevers cipher **no. 35**, BnF fr. 3995 f. 64 ("Per Cavare 1590"), Gallica `btv1b525085665` canvas 131
(7348 × 6032, fetch with a browser User-Agent; canvas 130 is the blank verso). Figures 11–40 letters with homophones:
11 m 12 f 13 a 14 h 15 e 16 n 17 p 18 g 19 b 20 z 21 d 22 a 23 t 24 u 25 o 28 u 30 l 31 r 32 i 33 c 34 t 35 o 36 e
37 i 38 a 39 o 40 s (26 Inglesi, 27 Venetia, 29 Consiglio); 41–99 words and names (80 Francesi, 81 Spagna, 84 Francia,
96 Spagnoli, 97 Roma …); overbarred figures and signs for names and words (● che, ⊡ S. Ecc.za, ⊕ S. Alt.a …).
An overbar on a letter figure doubles it. No prior decipherment found (DECODE: Non-decrypted; Tomokiyo lists the key,
not this letter).

## Reading so far (f. 92r, `ct_92r.txt`, `beam.py`)

The key fits at once. On the death of Sixtus V (27 Aug 1590): "…che la morte del Papa **sia stata procurata con veleno
da [Spagnoli]**…", "…**la conservatione** …", "…**desiderata da tutti i buoni**…", "…**cotesta potenza, li medesimi
[Spagnoli]**…", "…**mi spiace** per i molti buoni **effetti che mi prometto che ne debbano seguire**…" (on the King's
conversion to Catholicism) "…**chiaramente aperta alla** … **grandezza**…". Hand traps: 3/9 and 0/8 look alike; `beam.py`
resolves them with `it-cinquecento`.

## f. 92v (`ct_92v.txt`, 8 cipher lines)

"…[l'] interesse di stato la devono far risolvere a correre la fortuna … come fanno [Venetia] e sì tutti gli altri
principi e nobiltà francese … dubitando … la sua conscienza … in così universal concorso se le possa opporre mancamento
alcuno {sign} conto della religione." Short passages: "{●} … [60]" before "ha scritto in Italia"; "{T} Monsignor" before
"sia stato menzognero". Reader's note: the ω-loop after 1 is 8 (18 = g: "gli", "religione").

## f. 93r (`ct_93r.txt`, 11 cipher lines)

About half reads: "…certificarlo della ottima … volontà verso il suo Re al servitio {Γ}… si assicuri la {⊕}{⊖} oltre la
mia particolar inclinatione e verso cotesta corona … parimente … gli interessi contro il … comune nemico me le renderà
sempre devotissimo servitore come a tempo e luogo conveniente {●} conoscerà chiaramente da gli effetti." Here the writer's
28 (u/v) looks like 27 (servitio, potuto, verso).

In sum: Mantua reports the rumour that Sixtus V was poisoned by the Spaniards, welcomes Henri IV's expected conversion,
and assures Nevers (for the King) of his devotion to the French crown against the "common enemy", a guarded pro-Bourbon
declaration of September 1590.

## Signs and code words read from the key (f. 64, upper right)

θ-with-bar per · ●— che · ♀ non · Y V.A. · ⊡ S. Ecc.za · ⊕ S. M.tà · ⊙ S. S. Ill.ma · flag-Γ S. A. · ⌊ et · S-sign quello ·
↓ quali · ‡ quanti · T mille · + conto · ※ lettere · Γ di · 7 il. Titles 41–63: 42 Mons. di, 43 Gran Duca di, 45 Papa,
47 Re di, 55 Cardinale di, 58 Duca di, 60 Legato … (overbarred 96 Mercœur, 97 Nemours; plain 96 Spagnoli, 97 Roma).
So on f. 93r "{box-sign}" = et ("a tempo et luogo conveniente", "corona et parimente"), "{bar-circle}" = per,
"{circle-plus}" = S. M.tà ("si assicuri la S. M.tà per…", "con S. M.tà gli interessi"); on f. 92v "{●} ti il [60]" = "che
il Legato ha scritto in Italia", "{T} Monsignor" = "Di Monsignor" (flag-Γ).

## Remaining gaps

- f. 92r lines 5 and 8: transcription errors, only part decoded — blocker: not-attempted (retranscribe).
- f. 93r l1–l5, l8: stretches that decode to nonsense (transcription slips; 27/28 and 3/9) — blocker: not-attempted (retry with the 27→28 alternative added to `beam.py`).
