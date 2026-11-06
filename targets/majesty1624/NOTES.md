# majesty1624: unsigned German report to a Majesty on Gabriel Bethlen, undated, filed with letters of 1624 (BSB Clm 10403 n. 65)

Status: read in part, by sense only, NOT validated (Brice Dudout, 6 Nov 2026). The cipher passage was deciphered at the time:
most runs carry an interlinear gloss. We rebuilt the letter key from those glosses and read 4 of the 6 unglossed runs. Daniel's
count on the unglossed runs: 15 of 18 letters (83%), below the 95% bar. There is no held-out part, so no measurement was made,
and no printed text of the piece was found.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Lead no. 2181 (research/leads.json, bavarikon/BSB
sweep of Nov 2026). Not in the catalogue; no DECODE record.

## Document

Munich, Bayerische Staatsbibliothek, Clm 10403 (Collectio Camerariana 53), n. 65, fol. 192-193 (MDZ bsb00116451, scans 411-413;
digitised microfilm, Public Domain Mark 1.0, images credited "München, Bayerische Staatsbibliothek"; none are included here).
Only scan 412 carries cipher. Scans 410, 411, 413 and 414 have none.

Halm (1874, p. 123) lists the piece as "Schreiben an den Kaiser s. d. zum Theil in Chiffern", between letters of Gabriel Bethlen
to the Emperor (Kassa, 29 May 1624). **The addressee is probably not the Emperor**: the text speaks of the Emperor in the third
person ("von dem Kayser erlangt") and addresses "E. M." (Euer Majestät). So it is written to another Majesty; Frederick V,
King of Bohemia, is likely, given the Palatine papers of the collection, but nothing on the leaf names him. The writer is not
named. The report deals with Gabriel Bethlen, the peace with the Emperor, money for 24,000 men and the Margrave's army.

## System (`key.tsv`)

A homophonic alphabet of two-digit numbers, a word code of 4-digit numbers (1410 Herr, 2638 schreiben, 1628 Jenner,
1007 feind, 1853 macht), doubled letters for short words (ZZ mir, Yy zu, Pp er, Gg dass, LL der, aa do) and two single
numbers for words (11 = zu, 71 = dz).

Letters: a 6/9/15, c 8, d 12/36/60, e 13/19, f 14/20, g 24, h 25, i 26, k 30, l 31, n 42/45/51, o 43, r 49, s 50/56/59,
t 63/69, u/ü 61, v 70, w 62 (or s), z 77. Unknown: 27, 32, 65 (one occurrence each).

It is not the casimir1629 family (targets/casimir1629, targets/pawel1624): at best 2 letters of 20 agree, for any shift from -6
to +6. It is not the system of lead 2182 either.

## Texts

`transcription.txt` lists the 19 runs of two-digit numbers with the gloss written over each at the time. `decryption.txt` gives
our decode with `key.tsv` beside the gloss. The 4-digit code groups and the clear German text are not transcribed; the glosses
of the code groups we could read are in `key.tsv`.

Unglossed runs (Daniel's count: 3 certain, 1 probable, 0 restored, 2 unresolved; 15 of 18 letters):

| run | reading | grade | why |
|---|---|---|---|
| 43.31.24.19.51 (l. 8) | -olgen, end of *verfolgen* | certain | split word, glossed at the end of l. 7 |
| 31.26.8.25.13 (l. 2) | -liche: *[löb]liche Herr* | certain | l, h, e from glosses, i = 26 confirmed by *künfdigen*; it follows 1847 (period gloss "böse", read as *löb-*); the clear text above has "der löbliche Herr"; c = 8 rests on this context only |
| 30.61 (l. 4) | kü-, start of *kü\|nfdigen* | certain | split across the line like *verfol\|gen*; the period gloss sits on the second half |
| 50 after Cc (l. 7) | -s (*auffs*) | probable | s = 50 elsewhere |
| 13.32 (l. 2) | e? (between *botten?* and *nehmen?*) | unresolved | 32 occurs once; "es" and "ein" both fit |
| 27.13.65 (l. 3) | ?e? (perhaps *ver-* before *wünden*) | unresolved | 27 and 65 occur once |

Also re-read: 62.61.42.36.19.45, whose period gloss is hard to read ("zu zeitigen"?), decodes *wünden* (or *sünden* if 62 = s):
probable, meaning unclear.

Reading of the cipher passage (normalised; [ ] = restored, ? = uncertain):

> Nun kan E. M. ich mit grundt der Warheit berichten, dz der löbliche Herr mir absonderlich zu botten? e? nehmen?, der meldet
> auch zu schreiben zugelassen, dieweil er, dass zu ?e? wünden? würde, do wolte er … den künfftigen Jenner mit hülff … und …
> er macht …, des … als dan … feind … auffs eüsserst verfolgen helffen.

Summary: the writer assures "E. M." that a "worthy lord" has allowed him to write, and that, if something comes about, this
lord means next January, with help, to pursue the enemy to the utmost. Drawn from the glosses and our decode; the clear text
around the passage is not transcribed.

## Validation

None. No part of the cipher was held out (it is all on one page, and most of it is glossed), no other piece of Clm 10403 shares
the code (sweep of 6 Nov 2026; n. 6 has a signature in cipher only, not looked at), and no printed text was found. The readings
above rest on the sense and on the glosses of the time. No validation.txt.

## Prior work

- The glosses on the leaf are the decipherment of the time (credited `contemporary`, prior solution).
- Halm 1874 p. 123: catalogue entry only. Szilágyi 1879 (Bethlen's letters) has nothing for May 1624. Not reachable as full
  text online: Briefe und Akten NF, Acta Bohemica, Gindely, Hurmuzaki, Tadra (AÖG).
- No target, PR or issue for Clm 10403 n. 65 in this repository (GitHub API, origin/main 2f8603497, 6 Nov 2026). Not on DECODE.

## Limits

- One reader (an agent), on a microfilm scan. No human palaeographic check. Several glosses are hard to read (412.01, 412.07,
  412.08, 1492, 2999).
- The key is read by sense and not measured; 8, 36, 45 rest on one occurrence each.

## Remaining gaps

- 2 unglossed runs unresolved (13.32, 27.13.65) - blocker: too-short; 27, 32 and 65 occur once each
- no held-out part and no measurement - blocker: too-short; the cipher is a single glossed page

Not gaps of this reading (scope): the 4-digit code groups and the clear text of the leaf, which the writer of the time glossed (part of the period decipherment, not transcribed here); the cipher signature of n. 6 of the same volume; leads 2180 and 2182, which use other systems. Disclosed, not a blocker: one agent reader on a microfilm scan, no human palaeographic check (see reading_review).

## Escalation

- [x] siblings: Clm 10403 swept for other enciphered pieces (none share the code); casimir1629 and pawel1624 tried, no fit; lead 2182 compared
- [n/a] clear-pages: no clear copy of the piece is known
- [x] known-keys: casimir1629 family, every shift from -6 to +6: no fit
- [x] print: Halm 1874, Szilágyi 1879 checked; Tadra (AÖG) and the other editions not found as full text
- [x] key-rebuild: letter key rebuilt from the glosses (key.tsv)
- [x] retry: the unglossed runs re-read at high magnification on 6 Nov 2026 (liche, kü-)

## Credits

The glosses are of the time. Brice Dudout: transcription, key, readings of the unglossed runs, summary. Daniel Bourdeau: lead
2181 in research/leads.json, with the Halm reference and the MDZ links.
