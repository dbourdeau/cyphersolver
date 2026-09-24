# Two cipher letters to Johann Georg von Ilten, London, Feb-Mar 1743 (GWLB Hannover, Ms XXIII 1234:29,2)

Status: read (key found in the same papers, Ms XXIII 1234:31,1 pp. 386-391; both letters deciphered with it)

Worked 24 Sept 2026, as a sibling of catalogue entry 346 (`ilten1697/`). The archive scan of 23 Sept 2026
(`oldest/scan_2026-09-23/hard_targets.md` item 8) listed these two letters under "Also"; they were not a catalogue
entry of their own.

## Documents

Johann Georg von Ilten (1688-1749), Hanoverian lieutenant-general ("General Lieutenant" in
Steinberg's address), was with the Hanoverian troops of the Pragmatic Army in 1743. His "Sammlunge von Krieges Commissariat undt Landt-Sachen" are Ms XXIII 1234 in the
Ilten papers at the GWLB. Kalliope describes volume 29,2 (1741/1743) as operational papers for the 1743
campaign "und teilweise chiffrierter Korrespondenz".

1. **Unsigned letter, "866.223 den 15/26 Febr 1743"**, Ms XXIII 1234:29,2 pp. 73-75 (Kalliope DE-611-HS-4136816,
   "Von Unbekannt an Johann Georg von Ilten ... Teilweise dechiffrierter Brief"). German clear opening, then 25
   lines of numeric code (189 groups) with **no decipherment at all**, then German clear text again ("eine
   Affaire ... zwischen dem Obrist von Hardenberg und dem Major d..."). Kalliope's "partly deciphered" means the
   clear parts; the cipher was never read.
2. **Ernst von Steinberg, London, 29 Mar / 9 Apr 1743**, pp. 119-121 (Kalliope DE-611-HS-4136823, "Teilweise
   dechiffrierter Brief"). German letter with three code runs (34 groups); p. 121 is a contemporary worksheet
   with the groups glossed syllable by syllable, partly wrongly.

Images: GWLB Kitodo, METS `DE-611-BF-85387` (Kitodo id 53368), pp. 73-75 = phys. 81-83, pp. 119-121 = phys.
127-129. Public domain. In `img/` (git-ignored).

## The key

Kalliope's record for **Ms XXIII 1234:31,1** (1745/1746, METS `DE-611-BF-85391`, Kitodo id 68740) lists
"eine Chiffre-Tabelle", "S. 386-391 [Chiffres]". Fetched (phys. 410-417):
- pp. 386-388: encoding side, alphabetical ("a - 25, 61, 244, 301, 467, 720", "ab, le - 321", ...), with an
  "Additamentum" of officers' names (Adelebs, Bülow, Hammerstein, Ilten 845, Sommerfeldt, Pontpietin ...).
- pp. 390-391: decoding side, 1-863 in columns, blank numbers unused, and the note
  **"NB. les Chiffres qui restent ne signifient rien"**: blanks and 864-1000 are nulls.
- Two control groups: 101 and 783 "annulle la precedente", 453 "repete la precedente".
The decoding side was transcribed in two halves by two agents (`key1743/decode_001_400.tsv`,
`key1743/decode_401_863.tsv`), each checked against groups whose values the Steinberg worksheet gives
(28 checks; the one mismatch was 17 = "et", which with 294 = "re" gives the worksheet's "être"). Spot-checked
against the sheet here (172 Duc, 442 ap, 445 donne, 446 no). Uncertain readings are marked in the note column
(long s / f: 403, 405, 459, 460, 490, 672, 749).

The key is the one both letters use: Steinberg's worksheet values agree with it group for group
(344 ex, 515 tra, 126 it, 15 de, 5 l', 782 in, 225 c, 721 tion, 266 qui, 767 vi, 353 ent, 97 de, 259 envoyé,
41 au, 472 Mylord Stair, 147 le, 705 dernier, 750 me, 98 na, 450 ge, 714 nt, 172 Duc, 414 secret, 618 general,
126 it, 3 e, 740 alleman, 384 de).

## Reading

`reading.md` (text, translation, notes); `decode_*_signs.txt` sign by sign; `decode1743.py` applies the key.

- **Letter 1**: dateline 866.223 = [null] **Londres**. The cipher is French: Du Pontpietin's
  instructions to Lieutenant-General Sommerfeldt about forage are approved, and the troops are to eat up the forage in their
  quarters so the French find nothing if they quarter there after them; Ilten is to use this "last point" with
  his usual prudence. 188 of 189 groups take a value; 186 read as sense.
- **Letter 2**: "un extrait de l'instruction qui vient d'être envoyée au Mylord Stair" (enclosed), to be used
  "quoique avec le dernier ménagement du secret" among "[la] généralité allemande" of His Majesty. 34 of 34.
  The contemporary worksheet got "in-tra-c-tion" (644 is "tru"), left out 278.613 "quoique avec", and wrote
  172 as "Duc".
- 172 is "Duc" on the sheet but stands for **du** in both letters ("le general Du Pontpietin", "du soin",
  "du secret").

Sender of letter 1: unsigned. It is written from London (dateline) in the code Steinberg used five weeks later,
and it speaks for the King ("ainsi que j'ay ordre de le marquer"); the German Chancery in London under Steinberg
is the likely source. Not proven.

## Remaining gaps

- Letter 1 p. 74 l. 3: group 75? (last digit lost in the binding; 751, a null, fits the stroke) and the 283 (r)
  before it, "consument avec r.. même bonne discipline" - blocker: needs-physical-access; the digit is inside the
  gutter on the scan
- Letter 1 p. 74 l. 4: 59 (e) after "discipline" reads as a stray letter - blocker: too-short; one sign, the
  sentence reads without it

## Escalation

- [x] siblings: Kalliope search "Ilten dechiffr*/chiffr*/Chiffre*" in the Ilten papers: these two letters, the
  four 1697-1706 letters (`ilten1697/`, other codes, read at the time) and the key sheet in 1234:31,1
- [x] clear-pages: p. 121 is the contemporary worksheet for letter 2; letter 1 has none
- [x] known-keys: the 1234:31,1 table fits both letters
- [n/a] print: the key reads both letters in full
- [n/a] key-rebuild: key complete for the groups used
- [x] retry: gutter digits re-read from a full-resolution crop (51, 407, 59, 95, 70, 705)

## Leads not followed

- Volume 29,2 is "teilweise chiffriert" as a whole; only these two letters are catalogued singly. Other cipher
  passages in 29,2, 29,3 and 31,1 (1741-1746) would read with the same table.
