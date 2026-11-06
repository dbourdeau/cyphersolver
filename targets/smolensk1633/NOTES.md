# AGAD AR dz. II nr 1116 — the besieged at Smolensk to Krzysztof Radziwiłł, 1 June 1633

Status: read. Catalogue no. 1588. Key recovered here on 5 Nov 2026 (Claude Opus 5.5), from the ciphertext with the
stock formula *W.X.Mci* of the clear close as a crib; 95.0% of the 1,856 cipher signs read directly, 99.4% counting
words read from sense with one doubtful sign; one word of 11 signs open. No earlier decipherment of this letter
found.

## The document

AGAD, Archiwum Warszawskie Radziwiłłów (zesp. 354), dz. II nr 1116 (1/354/0/2.1/1116): "Szyfrowany list urzędników i
obywateli województwa smoleńskiego, znajdujących się w oblężonym Smoleńsku, do Krzysztofa księcia Radziwiłła,
kasztelana wileńskiego i hetmana polnego litewskiego, zawierający informacje o rozwoju wydarzeń". Seven microfilm
frames on szukajwarchiwach.gov.pl (https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/29638410): 1 and 7 film
cards, 2 film record sheet, 3 cover "1116", **4 = f. 1r (the cipher, 35 lines)**, **5 = f. 2r (2 cipher lines, the
clear close, about 17 signatures)**, 6 = the address leaf. Full scans are 2520x3626 px (`_max`); they are not
committed. The site blocks scripts (Imperva); the images were fetched in the user's Chrome (frame 4 downloaded with
permission; frame 5 read in the browser).

Heading in clear: *1633 Junii 1. Jaśnie Oświecone Książę a nasz wielce Mściwy Panie.* Close in clear: *... W.X.Mci
naszego Mciwego ... Dat z oblężenia Smoleńskiego 1 Junij 1633.* The letter was sent out of Smolensk during the siege
by Shein's Muscovite army (Oct 1632 – Sept 1633), the eighth month of it by the writers' count.

## The system and key (`key.tsv`)

A simple substitution, one sign per letter, with word division kept, written as digits told apart by **where a
cross stroke sits**: a plain digit, the same digit with a small cross on its top (ᵗ3, 5ᵗ, ᵗ7), the digit struck
through (4̶, z-shaped 7, 8 with a bar through its top loop), 8 with an overbar, 6 with a top flag (б), a free cross
with a foot (ŧ), a free plain cross (+), and three 1-0 groups (ŧ0, +0, 10). A delta sign stands for the X of
*W.X.Mci*. 24 signs in all (`python docs/_check_profile.py --measure` gives 1,856 signs; `decipher.py --measure`).

| letter | sign | letter | sign | letter | sign |
|---|---|---|---|---|---|
| a | 9 | i, y, j | 4 | r | б (6^) |
| ą | 9^ | k | 10 | s, ś | + |
| b | 1 | l, ł | ᵗ3 (3^) | t | 4̶ (4/) |
| c, ć | 6 | m | ᵗ7 (7^) | u | +0 |
| d | 3 | n, ń | 8̶ (8/) | w | ŧ0 (t0) |
| e | 8 | o, ó | 5ᵗ (5^) | z, ż, ź | ŧ (t) |
| ę | 8^ | p | z-shaped 7 (7/) | ch | 6 2 |
| f | 5 | g | 7 | h | 2 |

No nulls, no homophones beyond i/y/j sharing one sign, no code words: names and titles are spelled (*Smoleńska*, *Kró.
Mci*, *W.X.Mci*). The cross positions are hard to see on the microfilm: ŧ0 against +0, 4 against 4̶, and the two
crossed 7s are the commonest doubts, and most doubtful words in `reading.tsv` come from them.

## How it fell

1. A first transcription (`draft_f1.txt`, lines 1-15) recorded every crossed digit as one class. A free
   substitution solver (`solve.py`, pl-1790, order 4) on it gave noise, as did a teen-number hypothesis
   (crossed digit = 10-19, `teen.py`). With one letter per sign it produced fragments (*wiadomosli*,
   *niemriialiez*), which suggested the signs were right in kind but merged.
2. The clear close has *W.X.Mci*; the cipher has the group `ŧ0,Δ,7 6 4` four times, so ŧ0 = w, Δ = X, crossed 7 = M,
   6 = c, 4 = i. The repeated 12-sign word then fitted *nieprzyiaciel* only if б and ŧ were two letters (r, z).
3. At 4.4x zoom the crosses split into classes by position: a z-shaped 7 (p) against a 7 with a top cross (m); a
   footed ŧ (z) against a plain + (s). With those, line 1 read straight off: *Za gwałtownym i potężnym a barzo
   ścisłym opasaniem straża murów smoleńskich ...* (7 = g, 3^ = ł, 4/ = t, 8/ = n, 8^ = ę, 1 = b). The 1-0 groups
   split three ways (ŧ0 w, +0 u, 10 k) from *trudna*, *długi*, *iako*.
4. The whole page was re-transcribed in the finer classes from crops upscaled 2.5x (`transcription.txt`), and the
   key applied mechanically (`decipher.py`); doubtful signs were checked again at 3.5-5x.

## The reading

`reading.md` (Polish), `translation_en.md` (English), `reading.tsv` (word by word, with status). The garrison and
citizens tell Radziwiłł that sending letters out is nearly impossible; the enemy, with mines, gunfire and trenches,
is at the walls; the brother they sent out will report; they cannot hold much longer; they beg him not to let the
place, its churches, clergy, children, women, nobility and common people perish through slow relief, since he took
its rescue upon himself; the enemy is split among his camps, sconces and blockhouses, and a sortie from the walls
could join his advance; the senators promised relief within weeks and they are now in the eighth month.

Spelling is the period's: *prozba*, *rożnych*, *s pośrzodku*, *wszytkich*, *przyszedszy*, *iako*, *nierychłe*,
*dufność*, *oblewaiąc*, *prętkie*.

## Measurement

`python decipher.py --measure`: 1,763 of 1,856 signs (95.0%) in words the key reads as written; 82 signs (4.4%) in
words read from sense with one or two doubtful signs, marked [?]; 11 signs (0.6%) unread. Statistical validation
(`validation.tsv`, `docs/_validate.py`, pl-1790): reading -2.521 per letter, random keys -5.747 (z 7.6), key annealed
onto shuffled ciphertext -4.171 (z 86.1); pass.

## Prior work

- Nagielski, "Szyfrowane depesze Samuela Stanisława Sokolińskiego ze Smoleńska z 1633 r.", *Miscellanea
  Historico-Archivistica* XI (2000), 287-304 (AGAD PDF tom-11_0_merged.pdf, read 5 Nov 2026): prints five
  deciphered letters of Sokoliński, 31 May - 30 June 1633, from AR dz. V 1477/14779 and the contemporary clear copy
  AR dz. II nr 1115. Not this letter (1 June, from the officials and citizens); no key table given.
- The leads vetting of 3 Nov 2026 found nr 1115's frames hold only the letter of 31 May.
- DECODE (known.py), Tomokiyo, Lasry's GL.htm: nothing (vetting, 3 Nov 2026). Web search on phrases of the
  reading (5 Nov 2026): nothing.
- Whether this letter's cipher is the same as Sokoliński's: not tested (his originals were not seen). The nr 1115
  copy and the AR dz. V letters would show it, and the key here would then read them.

## Remaining gaps
- f1r.13 last word, signs 7/.5^.+.7/.8.4.8.6.4.1?.9 (+ f1r.14 6.t.4.6): decodes p-o-s-p-e-i-e-c-i-b-a | czyć, no
  word; probably "(o)baczyć" with a miswritten or misread first half - blocker: illegible; the small 1 and the crosses
  are not clear on the microfilm frame, tried at 5x
- 82 signs in 15 words read from sense with a doubtful sign each, listed in reading.tsv - blocker: illegible;
  microfilm, cross positions

## Escalation
- [x] siblings: AR dz. II nr 1115 (clear copy fascicle) checked by the vetting; holds the 31 May letter only
- [x] clear-pages: the clear heading and close used (W.X.Mci crib); no interlinear decipherment on f. 1-2
- [n/a] known-keys: no key of the Smolensk letters held or printed (Nagielski gives none)
- [x] print: Nagielski 2000 read; this letter not printed
- [x] key-rebuild: key complete (24 signs, all letters of the text)
- [x] retry: every doubtful word checked again at 3.5-5x; three corrected (przemysłów, przy uniżonych prozbach, po
  rożnych)

## Files

- `transcription.txt`: sign-level transcription, f. 1r lines 1-35 and f. 2r lines 1-2, notation in its header.
- `key.tsv`, `decipher.py` (raw decipherment; `--measure`), `make_reading.py` (builds `reading.tsv` and
  `validation.tsv`).
- `reading.md`, `translation_en.md`, `reading.tsv`, `validation.tsv`.
- `draft_f1.txt`, `solve.py`, `teen.py`: the first, coarser transcription and the solver runs that did not break it.
- `WORKLOG.md`, `profile.json`.
