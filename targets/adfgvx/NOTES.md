# The unsolved ADFGVX messages of 1918 — a working decoder, and page 100 reproduced

Twenty-two ADFGVX radio messages from the Eastern Front sit on Klaus Schmeh's Top 50 as unsolved.
They are not unbroken ciphers. George Lasry, Ingo Niebel, Nils Kopal and Arno Wacker broke the James
Rives Childs corpus and **published the keys** — fourteen three-day periods, 618 cryptograms
recovered. What defeats these twenty-two is mutilation in transmission, and ADFGVX is unforgiving
about length: the columnar stage splits the stream by the key length, so one lost letter moves every
column boundary after it.

In the comment thread under Schmeh's 2017 post, readers solved twelve or thirteen of the twenty-two.
Schmeh announced a consolidating article and never wrote it, so those readings exist only as
scattered comments and no table has ever been published.

## What this session built

**The keys, machine-readable.** `keys.json` has all fourteen. Three of them do not survive a naive
read of Lasry's PDF: their substitution squares contain runs of hyphens for unrecovered cells, and the
PDF text layer collapses those runs into en- and em-dashes, leaving squares of 34 or 35 characters
instead of 36. Expanding the dashes back to the length that makes 36 recovers all three.

**The transposition convention, settled.** Two readings of the key numbers are possible: `perm[i]` is
the column emitted i-th, or `perm[i]` is the position at which column i is emitted. Both round-trip
self-consistently, so a round-trip test cannot tell them apart. Decrypting a real message can, and it
is the **second**.

**Page 100, reproduced from scratch.** The published reading is

> KEINE STOERUNG DURCH FEIND X MITTAGS 2 FEINDL X DIV X IM MARSCH AUF BELGRAD X

That is 62 characters, so 124 ADFGVX letters, but only 122 were received. Searching every way of
inserting two placeholders, against all fourteen keys, returns it at a score of 140.7 against a field
where nothing else clears 7:

```
KEINESTOER?NGDURCHFEINDXMITTAGS2FEINDLXDIVXIMMARSCH?UFBELGRAD?
```

Key: **Nov 1–3, length 19**. The placeholders land on the three characters shown as `?`. This
validates the whole pipeline end to end.

## What it found

Running all twenty-two against all fourteen keys, allowing up to two insertions or one deletion:

| page | letters | key | reading |
|---|---|---|---|
| **100** | 122 | Nov 1–3, len 19 | **solved**, as above, score 140.7 |
| **132** | 153 | Nov 4–6, len 17 | **key identified**: `WIEDERHOLE` … `TELEG` emerges cleanly |
| 146 | 244 | len 17 | partial: `STELLEN`, `RICHTIGEN` |
| 189 | 84 | len 18 | weak |
| the other 18 | — | — | nothing above noise |

The page 132 result is worth stating carefully. Neither **WIEDERHOLE** nor **TELEG** is in the
scorer's word list, so they were not being optimised for — they emerged. "Wiederhole Telegramm",
repeat the telegram, is exactly the kind of traffic these stations sent. The key for that message is
therefore the Nov 4–6 one, and what remains is deeper reconstruction rather than a key search.

## Honest limits

Only one of the twenty-two is fully read here, and it is one that was already read in 2017. The
search allows at most two insertions or one deletion; messages mutilated more heavily than that, or
mutilated by substitution rather than by loss, are out of its reach. Several of the twenty-two carry
explicit gap marks in the printed transcription, and one is labelled "missing 10 letters" — those
need the Childs originals, not a wider search.

What is new and reusable is the decoder, the machine-readable keys with the three damaged squares
repaired, the settled transposition convention, and the identification of page 132's key.

Reproduce: `python repair.py validate` (page 100), `python repair.py solve` (all), `python deep.py
132 17 3` (the deeper search on page 132).

## Second session (2026-09-15): the 2017 thread consolidated, and the residue tested to a principled stop

### What the comment thread actually holds

The 70 comments under Schmeh's post (saved as `../../research/top50/arts/46.htm`, text in `46_comments.txt`) were read in
full. Norbert (comments 15-49), Armin (13), Thomas (27), Max Baertl (39) and George Lasry (50-53) read far
more than the "12-13" this file assumed, and they did it by the method Norbert states in comment 23: *"add or
remove up to 5 characters at two different positions, exhaustive search with an n-gram value function"*.
Lasry also recovered a **sixteenth key** (comment 50), missing from the published list of fourteen: the CHI key
of 13 November 1918, transposition word **CMBLAKOHIDENFJGP** (length 16), found by solving the two-part message
FFVXV + AFAFF jointly. Its substitution square is rebuilt here from that plaintext (`key16.py`, 24 of 36 cells,
digits and M Q Y unrecovered) and added to `keys.json` as the fifteenth entry.

The table nobody published, in the order of the list:

| Childs page | letters | status | key | reading (2017 author) |
|---|---|---|---|---|
| 73 | 176 + 2 marked gaps | **open** | none fits | - |
| 100 | 122 | solved | Nov 1-3 | KEINE STOERUNG DURCH FEIND X MITTAGS 2 FEINDL X DIV X IM MARSCH AUF BELGRAD X (Armin) |
| 105 | 290 | solved | Nov 1-3 | GERMANIA ETAPPE KONSTANTINOPEL XX FUER MITTELMEER DIVISION ZU X TEL X NR X 62 X DIV X TELEGR X NR X 58 X ERSTELLT X 32141 X Q4 ... VOM X 4 X NOVEMBER ERLEDIGT X ADMIRALSTAB X 32398 X B (Norbert) |
| 109 | 258 | solved | Nov 1-3 | O X K X M X ABENDMELDUNG X S4V4 X UNTERBRINGUNG LETZTER TEILE BEENDET X 1 WEITERER DU X DIV 5 IM MARSCH AUF BELGRADER KAVV X 2 X SONST KEINE EREIGNISSE XX ASO X K511 (Norbert) |
| 132 | 153 + gap | solved | Nov 4-6 | FUER EILVESE X WIEDERHOLE TELEGR X VON VIERTER PERIODE IN FUENFTER X GEBETSORDER 5 MIN X VVV; the encipherer wrote VVV for one VV, hence the odd length (Norbert, comment 37) |
| 146 | 244 | solved | Nov 4-6 | FUNKSTELLE KERTSCH ER HAT BETRIEB X 1F X RUFNAMEN RICHARD EMIL KARL X FUNKSTELLEN DORTIGEN BEREICHS BENACHRICHTIGEN X NACHRICHTENCHEF 4B X 7834 X (Norbert) |
| 152 | 104 | **open** | none fits | - |
| 153 (VFVAX) | 132 | **open** | none fits, incl. the CHI key | - |
| 153 (AXVAA) | 93 + 15 marked gaps | **open** | none fits, incl. the CHI key | - |
| 158 | 240 + 2 gaps | **open** | none fits | - |
| 164 (F-G-X) | 158 + 44 gaps | partial | Nov 7-9 | ... X 9 X 11 X TEMESVAR X ... DIE VON X MIRCO NACH WESTEN UND SUEDEN WEG X LEIDER WEGE VOM GEGNER BESETZT X (Norbert, comment 42) |
| 164 (VFGAG) | 136 + 44 gaps | partial | Nov 7-9 | EL X DIE HOEHE X 828 X O X H X L X MIRCO X SONST KEINE EREIGNISSE VON BEDEUTUNG XX (Norbert, 41/44) |
| 170 | 106 | **open** | none fits | - |
| 171 | 310 + 4 gaps | solved | Nov 7-9 | IN UKRAINE UND POLEN RUBELKURSE STARK STEIGEND INFOLGE BRUCHES ZWISCHEN DEUTSCHLAND UND SOWJETREGIERUNG UND ERWARTUNG DER WIEDERHERSTELLUNG RUSSLANDS DURCH DEUTSCHLAND UND ENTENTE (Norbert) |
| 176 "missing 10 letters" | 214 | solved | Nov 10-12 | DURCHBRUCH VORBEREITET X DURCHBRUCHSRICHTUNG NACH NORDEN ODER NORDOSTEN ERFOLGEN WIRD X KANN JETZT NOCH NICHT BEURTEILT WERDEN X (Norbert) |
| 176 (GGDAA) | 220 | **open** | none fits | - |
| ?? (VGADA; Childs p. 215, 22 Nov) | 237 + 11 gaps | partial | Nov 22-24 | ABS X MIDIV 5 X EILMELDG X 24N X 24N X ARMADA KERTSCH X BRINGT ENTENTE FLOTTE ZWO DIVISIONEN X NEUSEELAENDER X ENGL X U X FRANZO X MIT X ... OHL X KORPS ... (Norbert, comment 32; Baertl) |
| 187 (FFVXV; Childs p. 191, 13 Nov, part 1) | 212 | solved | **CHI 13 Nov (new)** | RUSSISCHEN UND POLN HEERESVERKEHR VOLL ERFASSEN X WICHTIGES BESONDERS AUS POLN VERKEHR UEBER OHL STATION VERZIFFERT FUNKEN (Lasry, Norbert) |
| ??? (AFAFF; part 2) | 142 | solved | CHI 13 Nov | SOWEIT FERNSCHREIBERVERBDG NICHT ARBEITET X REST SCHRIFTLICH X NACH CHEF (Lasry, Norbert) |
| 189 | 84 + 6 gaps | **open** | none fits | - |
| 198 | 165 | **open** | none fits | - |
| 217 | 170 | **open** | none fits | - |

Nine solved, three partial, **ten never read by anyone**. The transcript page 187 (SELLV..., "Stellv Gen Kom 9 AK
Breslau") was a message the Kassel team had already solved and does not belong on the list (Lasry, comment 29).

### Reproduced here from scratch

`blocks.py` implements Norbert's method exactly (up to two block edits of one to five letters, inserted or
deleted, at group boundaries) against all fifteen keys, scored with a German quadgram model (`lm_de.py`, 3.6 M
letters of Gutenberg German, digits and X separators costed separately). It re-derives 105, 109, 146, 171, 176a,
187 and ??? with no hint of the plaintext (the five-letter block FVXAA that Norbert inserted before group 10 of
page 146 comes out as `(45, 5)`; the two five-letter blocks of page 176a as `(10, 5), (130, 5)`), and finds the
Nov 22-24 partial of page ??. `gaps.py` restores the marked gaps to their groups and anneals the residual
single-letter losses; on page 132 it lands on Norbert's text unprompted (...VIERTER PERIODE IN FUENFTER GEBETSORDER 5
MIN...). The scorer, the fifteen machine-readable keys and the gap-aware parser are the reusable part.

### The ten open messages, tested

* **Two block edits, fifteen keys** (`blocks_out.txt`): nothing above -6.7 nats per window for any of the ten,
  where the solved messages come out at -4.4 to -5.5 and random letters at -7.3. So none of them is one of the
  known keys with two or fewer mutilations, which is precisely what defeated the 2017 readers too.
* **The CHI key on the two page-153 messages** (Norbert's untested suggestion of September 2017): direct
  decryption with parity repair, and the block search, both give noise. Either a further unlisted key or
  losses heavier than two blocks.
* **Key-free attack** (`keyless.py`): recover the transposition without the square by annealing the column
  order on the index of coincidence of the resulting letter pairs, then solve the 36-symbol substitution.
  Planted control, 224 letters, key length 19: the IC peak at the true length is faint (0.064 against 0.055-0.066
  elsewhere) and the substitution does not converge; **not recovered**. Lasry's own program needed 356 letters
  at length 16 (comment 50). The ten open messages are 84 to 240 letters. A key-free recovery is therefore out
  of reach at these lengths, with the possible exception of joining messages that share an unknown key, and
  nothing marks which those are.

### Where this leaves it

The list entry should read "22 messages, 9 solved, 3 partly read, 10 open", with Lasry's sixteenth key
published alongside the other fifteen. The ten open ones need either the Childs originals (several carry
explicit gap marks and one says "missing 10 letters"; the printed transcription is not the last word) or a key
that was never in the Childs corpus. This file's earlier line "1 of 22 read" undercounted the field by eight.

## One key at a time (14 Oct 2026)

Under the one-key rule (George Lasry, 14 Oct 2026) the result is now stated per period key. The twenty-two
messages stay one entry, because they are one filed list; `profile.json` `outcome.parts` carries one item per key
and the README one row per part:

| key | messages (Childs pages) | solved | partial | open |
|---|---|---|---|---|
| 1-3 Nov, length 19 | 100, 105, 109 | 3 | 0 | 0 |
| 4-6 Nov, length 17 | 132, 146 | 2 | 0 | 0 |
| 7-9 Nov | 171, 164 (F-G-X), 164 (VFGAG) | 1 | 2 | 0 |
| 10-12 Nov | 176 ("missing 10 letters") | 1 | 0 | 0 |
| CHI 13 Nov (Lasry's sixteenth, length 16) | 187 (FFVXV), AFAFF | 2 | 0 | 0 |
| 22-24 Nov | VGADA (Childs p. 215) | 0 | 1 | 0 |
| no known key fits | 73, 152, 153 (VFVAX), 153 (AXVAA), 158, 170, 176 (GGDAA), 189, 198, 217 | 0 | 0 | 10 |

The last row is "not solved": the entry is not complete while those ten are open. Credits stay as they were:
the published period keys (Lasry, Niebel, Kopal, Wacker), Lasry's CHI key and its two messages (his comments
50-53), Norbert's and Baertl's 2017 readings.
