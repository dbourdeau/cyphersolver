# Rufus King to James Madison, London, 25 April and 8 June 1801 (NARA RG 59, DD Great Britain vol. 9) — NOTES

Status: no write-up

**Verdict: closed, already in print.** Session 2026-10-26. Catalogue entry 487 (Founders Online sweep,
`research/founders_emlo/`). Nothing new to read, so no site page; the entry is removed from the catalogue.

## The documents

Founders Online abstracts (Papers of James Madison, Secretary of State Series 1, 1986):

| Despatch | Founders | Madison Papers source note | Print |
|---|---|---|---|
| No. 14, London, 25 Apr 1801 | [02-01-02-0163](https://founders.archives.gov/documents/Madison/02-01-02-0163), PJM-SS 1:115 | RC, 5 pp., marked duplicate, clerk's hand, docketed by Wagner with King's no. 15 as received 8 July. "Final paragraph partly in code; key not found." | King, *Life and Correspondence* 3:436-38 |
| No. 21, London, 8 June 1801 | [02-01-02-0361](https://founders.archives.gov/documents/Madison/02-01-02-0361), PJM-SS 1:272-73 | RC, 4 pp., marked duplicate, clerk's hand, signed by King, docketed by Wagner as received 7 Sept. "Partly in code; key not found." | King, *Life and Correspondence* 3:472-73 |

(The catalogue entry called the first one "no. 15"; it is King's no. 14, docketed together with no. 15 of 26 April.)

## The print settles it

Charles R. King (ed.), *The Life and Correspondence of Rufus King*, vol. 3 (New York 1896), printed from King's own
papers (his drafts and letter-books), gives both despatches in full and sets **the words that were in code in
italics**, with the footnote "Italics in cipher" (p. 438; the same note appears about twenty times in the volume).
Page images checked on the Internet Archive scan `lifecorresponden03king` (leaf n471 = p. 438, n505-n506 =
pp. 472-473); transcriptions with the italics marked: `king_1801-04-25_print.txt`, `king_1801-06-08_print.txt`.

- **25 Apr 1801, final paragraph.** 13 italic runs, 96 of the paragraph's 124 printed words; the clear words
  between them ("complete", "effect", "former occasion", "attention to business", "respecting", "nature",
  "suffered", "quite", "founded", "difficulties, as well as those of the country, are much encreased") are roman.
  Content: George III's relapse. The recovery is not complete, the remedies have not worked as in 1788-89, he
  relapsed after attending to business too early (or on the news about Hanover), and there is "well founded"
  anxiety that he will never completely recover; his state is extreme debility. The ministers' difficulties are
  made worse by this uncertainty.
- **8 June 1801.** Only "Lord Hawkesbury and Mr. Addington" is italic (p. 473; no footnote on that page). The coded
  part is the names of the two ministers who told King, in separate conversations, that Britain would be ready to
  give the United States by treaty every limitation of the right of search it conceded to any other nation.

So the plaintext of every coded word is printed. The Madison Papers editors' "key not found" means only that no
decoding was written on the duplicates and the editors did not have King's code. It does not mean the content
is unknown.

## What was not done, and why

- **The coded duplicates were not seen.** NARA M30 roll 9 is not online as far as found (NARA catalog/web search,
  26 Oct 2026); FamilySearch/Fold3 copies need an account. So the code groups were not transcribed, and the code
  was not identified or rebuilt. Which code King used is open: the system is not measured. The same volume has
  King asking the Department for "a new cipher" and mentions Jay's cipher, found among the legation papers. With
  the printed plaintext as a crib, a rebuild from the code groups would add a key, not a text. That is not a
  reason to keep the entry open.
- Which copy the 1896 editor worked from is not stated at these letters. The italics show he knew which words were
  in code, so he had a coded copy with its decoding, or King's draft with the code marked.

## Remaining gaps

- none left open here. Both gaps recorded on 26 Oct 2026 (the code groups of the duplicates, said to be on "M30 roll 9, not
  online"; King's code key) were closed on 11 Nov 2026 by `../king1797` (Andrew Beling, pull request #398): see the update below.

## Update, 11 Nov 2026: the code is King's 769 code, and the duplicates are online

From `../king1797` (contributed by Andrew Beling, pull request #398; checked on integration):

- Despatches vol. 9 (1801) is NARA M30 **roll 7** (NAID 188513785), not roll 9, and it is online. The duplicate of 25 Apr 1801
  is frame 007-0142 R (124 code groups among clear); the 8 Jun 1801 run is frame 007-0162 R, lines 2-3 (12 groups).
- The code is the one King used in all his despatches from 14 Jan 1797 to 2 Apr 1803 (the = 769). Its key was rebuilt in
  `../king1797` from the State Department clerks' interlinear decipherments and tested on a held-out despatch.
- The code groups of both duplicates are transcribed in `../king1797/checks/bare_items.tsv`. With the key frozen for that test
  they agree with the italic words of the print: 85 of 100 covered groups for 25 Apr, 9 of 9 for 8 Jun ("Lord Hawkesbury and Mr
  Addington"), against at best 0.21 and 0.222 for 1,000 permuted keys (`../king1797/NOTES.md`, section 6).
- The Madison Papers abstract of No. 21 has "Swedes and Danes" where King's print and the coded run have "Lord Hawkesbury and Mr
  Addington" (noted by the contributor; the abstract was not re-read here).

The verdict of this folder is unchanged: both texts were already in print, and it keeps no page. The key and its write-up are
under `../king1797` (one key, one entry).

## Escalation

- [x] siblings: the other King despatches in vol. 9 that Wagner decoded are the obvious key source; not viewable online
- [x] clear-pages: n/a, no images
- [n/a] known-keys: no image of the code groups to test a key on
- [x] print: King, Life and Correspondence 3:436-38, 472-73 prints both in full with the coded words in italics
- [n/a] key-rebuild: no ciphertext
- [n/a] retry: no ciphertext; the text itself is complete in print

## Outcome

Method: read from existing decipherment (the 1896 print). Extent complete for the text; key not recovered. The
reading existed long before this work (1896), found during the attempt. No DECODE record covers these letters, so
there is no DECODE queue entry.
