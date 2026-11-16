# Lejava to Stomoniakov via Kopp, Nr 1196, 5 April 1921

Status: read in part (16 Nov 2026, recounted over cipher words: 9 of 21 words, 42.9%; was read, counted over letters)

Source, prior work and the solver are in `stomoniakov1921/NOTES.md`; the rest of the file is `kopp1921/NOTES.md`. No DECODE record: NARA material.


Heading in clear: "Kopp fuer Stomaniakov Berlin Luetzowufer 1", numbers given as 01004-01720, RAION. 167 letters, 11 columns.
Score -2.74 per character; shuffled control -4.47; held-out Russian -2.14.

Read-out order of the columns (0-10): 1 0 3 4 9 10 2 6 5 7 8. Rank of each column: 1 0 6 2 3 8 7 9 10 4 5.

```
soobschitef
edorovnkomu
dvoetochieo
dnovreminno
danorampori
ajenielitvi
nosuperevod
eberlinupba
tuzakazamna
uchnotechni
cheskogootd
elekontrval
iuaepiatqde
siittybiach
rubleizolot
om
```

## Reading, item by item

Decrypted text as one line, for checking: `soobschite fedorovnkomu dvoetochie odnovreminno danorampori ajenie litvino su perevode berlin upbatu zakazam nauchnotechnicheskogo otdele kontrvaliuae piatqdesiittybiach rublei zolotom`

| Decrypted | Russian | English |
|---|---|---|
| soobschite | сообщите | inform |
| fedorovnkomu | Федоровскому | Fedorovskii |
| dvoetochie | двоеточие | colon: |
| odnovreminno | одновременно | at the same time |
| danorampori ajenie | дано распоряжение | an order has been given |
| litvino su | Литвинову | to Litvinov |
| perevode berlin | [о] переводе [в] Берлин | for a transfer to Berlin |
| upbatu zakazam | [в] уплату заказам | in payment of the orders |
| nauchnotechnicheskogo otdele | научно-технического отдела | of the Scientific-Technical Department |
| kontrvaliuae | контрвалюта | countervalue |
| piatqdesiittybiach rublei zolotom | пятьдесят тысяч рублей золотом | fifty thousand gold rubles |

Slips such as `n` for `s`, `m` for `s` and `b` for `l` look like radio or copying errors. `litvino su` is read as Литвинову
from context: the name could also be another official's, so Litvinov is probable, not certain.

Translation: Inform Fedorovskii, colon: at the same time an order has been given to Litvinov for a transfer to Berlin in
payment of the orders of the Scientific-Technical Department, countervalue fifty thousand gold rubles.

Who: "Fedorovskii" is probably N. M. Fedorovskii, a VSNKh mineralogist on the board of its Scientific-Technical Department
in 1922-27. Nothing found so far places him in Berlin in 1921, so this is not confirmed. This reading is by the model and
has not had outside review.

## Read share over cipher words only (16 Nov 2026)

README Conventions now count the read share over the words written in cipher, holes by words, sure words only, and a
letter corrected in a key rebuilt here is a hole (the one-digit rule needs a surviving period key). The telegram is
wholly cipher (167 letters; the heading in clear is not in `reading.txt`), so nothing had to be separated. By hand,
word by word, `decryption.txt` against `reading.txt`: 21 reading words, **9 read as the decryption stands**
(soobschite, dvoetochie, dano, perevode, Berlin, zakazam, nauchnotechnicheskogo, rublei, zolotom) and **12 holes**: the
three prepositions supplied in brackets ([о] [в] [в]) and nine words whose decrypted letters differ from the reading
(fedorovnkomu n for s, odnovreminno, rasporiazhenie m for s, litvino-su s for v, upbatu b for l, otdele e for a,
kontrvaliuae, piatqdesiittybiach: пятьдесят and тысяч). **1.0 -> 0.429**, class **read -> read in part**; the key stays
recovered. The old 1.0 counted letters. `v10_relabel.py` gives 0.864 (3 holes of 22 words, the hyphenated compound counted as two): it counts
only the bracketed words, because the slipped words are not marked in the reading; no declaration changes that. Taking
the nine slipped words as read, 18 of 21 (85.7%) is still under the bar.

## Remaining gaps

- the nine words whose decrypted letters differ from the reading (Fedorovskii, odnovremenno, rasporiazhenie, Litvinovu, uplatu, otdela, kontrvaliuta, pyatdesyat, tysyach) and the three omitted prepositions - blocker: too-short; one 167-letter telegram in a key recovered here, no second copy to check the slipped letters against, and the omitted words are not in the cipher

## Escalation

- [x] siblings: the other letters of the file were split off per key (`kopp1921/NOTES.md`: voikov1921, voikov1921b, stomoniakov1921); none is a second copy of this message
- [n/a] clear-pages: only the heading of this telegram is in clear; no clear copy of its text is recorded here
- [n/a] known-keys: the key was recovered from this text; the other letters of the file use other widths and keys
- [n/a] print: not searched for a printed text in this recount; none is recorded in the notes
- [x] key-rebuild: the 11-column key was found by a low-width scan with a shuffled control at each width (width 11 -3.47 against -4.47), then polished to -2.74 (held-out Russian -2.14); the column order is the whole key of a transposition
- [n/a] retry: nothing to retry the slipped letters against without a second copy of the telegram
