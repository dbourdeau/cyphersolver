# Vincenzo Gonzaga (Mantua) to Louis de Gonzague, duc de Nevers, 17 Sept 1590 — BnF fr. 3979 ff. 92–93, DECODE R4176

Status: read (878 of 923 cipher tokens, 95.1%, measured in reading.md; key complete from the archive)

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
conversion to Catholicism) "…**chiaramente aperta alla** … **grandezza**…". The blind 4x re-read (21 Sept, `blind_92r.md`) added "…far risolvere a favor loro **contro cotesto
Regno di Francia**, la conservatione del quale è desiderata da tutti i buoni **Italiani**, conoscendosi P. che,
**anichilata** cotesta potenza, li medesimi Spagnoli procureranno di **sottoporsi** [as written] a ognuno…" and "…il che
seguendo, **si vede** chiaramente aperta alla via della grandezza…". Hand traps: 3/9 and 0/8 look alike; `beam.py`
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
28 (u/v) looks like 27 (servitio, potuto, verso). The blind 4x re-read (`blind_93r.md`) read "la priego **far riverenza** per me" (32 for 31, 27 for
28) and "ho [..] **in quello** per ho potuto".

In sum: Mantua reports the rumour that Sixtus V was poisoned by the Spaniards, welcomes Henri IV's expected conversion,
and assures Nevers (for the King) of his devotion to the French crown against the "common enemy", a guarded pro-Bourbon
declaration of September 1590.

Gallica pass (21 Sept): on f. 93r the q-like sign is the key's ♀ = non and the following ● = che, and the
microfilm gives 14 35 31 38 "hora": "…al servitio di che, **sì come non hò mancato in quello che hò potuto sin hora**
di darne c[..] parte…" (digits 14 35 11 13 16 36 38 23 33 35, one stray 33, a writer's slip).

## Signs and code words read from the key (f. 64, upper right)

θ-with-bar per · ●— che · ♀ non · Y V.A. · ⊡ S. Ecc.za · ⊕ S. M.tà · ⊙ S. S. Ill.ma · flag-Γ S. A. · ⌊ et · S-sign quello ·
↓ quali · ‡ quanti · T mille · + conto · ※ lettere · Γ di · 7 il. Titles 41–63: 42 Mons. di, 43 Gran Duca di, 45 Papa,
47 Re di, 55 Cardinale di, 58 Duca di, 60 Legato … (overbarred 96 Mercœur, 97 Nemours; plain 96 Spagnoli, 97 Roma).
So on f. 93r "{box-sign}" = et ("a tempo et luogo conveniente", "corona et parimente"), "{bar-circle}" = per,
"{circle-plus}" = S. M.tà ("si assicuri la S. M.tà per…", "con S. M.tà gli interessi"); on f. 92v "{●} ti il [60]" = "che
il Legato ha scritto in Italia", "{T} Monsignor" = "Di Monsignor" (flag-Γ).

## Remaining gaps

The full working reading and the token count are in `reading.md` (878 of 923 tokens read, 95.1%, measured; nulls
count as read). Each stretch below was re-read independently at 4x twice (retry pass, then the blind re-read), and
again on the second image, the BnF microfilm on Gallica (btv1b9060544v, canvases 160-162), and run through the beam
with any-digit substitution.

- f. 92r l5 tail (~10): "la nda a a di" before ⊡ - blocker: illegible; writer's slips, no other copy
- f. 92r l8 middle (~27): writer's enciphering slips; digits agree on both images; re-read twice and run through the beam with any-digit substitution, no Italian - blocker: illegible
- f. 92v "la mondezza a me" (~6) - blocker: illegible; digits identical on both images and give no sense (the signs {0Δ}, {4-sign}, {9} there are nulls on the key's "Seguitano le Nulle" list)
- f. 93r l8 (~2): looped, dotted code group before "comune nemico" - blocker: illegible; figures uncertain

## Escalation
- [n/a] siblings: DECODE holds no other Mantua 1590 letter in this cipher; Tomokiyo's no. 35 entry names the use (Duke of Mantua, 1590) but lists no other letters, so none was opened
- [x] clear-pages: none; the clear passages on ff. 92-93 are the letter's own clear text, no decipherment on the record
- [x] known-keys: Tomokiyo's Nevers no. 35 (fr. 3995 f. 64) fits and was applied unchanged
- [x] print: Tomokiyo nevers.htm and DECODE: no decipherment or edition of this letter
- [n/a] key-rebuild: the key is complete from the archive sheet; the unread stretches are transcription or writer's slips, not missing key values
- [x] retry: doubtful lines re-read at 3x by a subagent with 3/9, 0/8, 7/8 and 27/28 alternatives in beam.py; 92v and 93r mostly recovered, the stretches above remain
- [x] retry: second independent blind re-read at 4x of every unread stretch, +56 tokens (blind_92r.md, blind_93r.md)
- [x] siblings/second image: Gallica microfilm btv1b9060544v re-read of every unread stretch, +15 tokens (93r l4 "sì come non hò mancato in quello che", l5 "sin hora"); the four stretches above remain

## Route

Written "Di Malceseno sul Lago di Garda a 17 di Settembre 1590" (f. 93r, Gallica btv1b9060544v canvas 163). The address leaf (f. 94) names no place; Nevers signed two commissions at Château-Thierry on 23 and 24 Sept 1590 (BnF fr. 3983 nos. 46-47), so the atlas routes the letter Malcesine -> Château-Thierry.
