# camerarius1621: Ludwig Camerarius's code of 1621-22 (letters to Count Johann Albrecht of Solms, BSB Clm 10397)

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

Status, 3 Nov 2026: **read in part** (borderline). One letter (n.194) transcribed and decoded; 796 of 844 tokens read
(94.3%), below the 95% bar after the independent check's fixes (the first count, 95.3%, did not survive it). Outcome
method "read from existing decipherment": the Solms letters carry interlinear decipherments in a second hand, so this
is a transcription of an already deciphered letter, not a break (CONTRIBUTING rule 6). Key partly rebuilt as a code
list from glossed pairs. Not in the catalogue: found by WAINUT's sweep of the Munich Camerariana.

Contributed by WAINUT. The work was done with AI language-model agents; an independent agent made the check in
`VERIFY.md`. No human palaeographer has checked the text.

## Documents

- **Solms series**, Halm 1874 p. 91-92, Cam. 47 = **Clm 10397** n.129-210 (the sweep put it in Clm 10398 by mistake;
  Halm's page 92 lists n.129-210 before "Vol. 48. n.1"). MDZ bsb00116446, 912 scans, from microfilm, 1418 px wide.
  Letters of Ludwig Camerarius to Count Johann Albrecht II of Solms-Braunfels, Frederick V's Grand Master of the
  Household, Feb 1621 - late 1622 (scans 581-906). Originals, mostly unsigned ("E. G. underthäniger gehorsamer Diener").
- **Key source n.63**, Clm 10398 (Cam. 48, MDZ bsb00116447) scans 287-290, fol. 140-141v: Camerarius to Frederick V,
  Hamburg 25 Mar / 4 Apr 1622, copy, "z. Th. in Chiffern die erklärt sind": code groups with their meanings written over.
- **n.106**, Clm 10398 scan 469 (fol. 233): "Francesco Rota" to "Mr. Vatron", The Hague 8 Apr 1624. A different system;
  see Open items.

## The system

A nomenclator written into German clear text: code numbers 2-4 digits (about 40 to 3200) for words, names and titles,
in the alphabetical order of the plaintext (a one-part code), with several numbers for frequent values (Chursachsen
552/553/554; König in Dennemarck 1683/1687, König in Böhmen 1684 and probably 1682; Erzstift 923/934; Translation 2850/2851); and numbers below about 70
for single letters, used to spell words not in the list (homophones: "Land 60.49.43.50.63.19.42" = Land-drosten in
n.63). Camerarius names himself in code (484) and writes of himself in the third person.

## Key (`key.tsv`)

87 entries (43 and 1682 set to `doubt` and 1393 renumbered 1394 after the independent check), each with its source (letter and scan) and status: `both` (n.63 gloss and a Solms gloss agree), `n63`,
`solms` (a gloss in a Solms letter), `doubt`. Values come only from glossed pairs; none from context alone. Two
corrections made from glossed pairs: 1181 = Gelt (n.149, scan 641; the n.63 reading "Fried" is withdrawn), 1686 =
König in Engelland (n.172 scan 728 and scan 853, both "Kö. in Engel.").

Tests:
- `scripts/heldout.py`: values from n.63 alone, applied to n.194 (other volume, other recipient), against the
  glosses written in n.194 as transcribed here. 18 occurrences of 11 distinct groups: 14 agree (13 if 553 "Chur S."
  is not accepted as an abbreviation of Chursachsen; 1344 "Gr. hofm." added after the check), 0 disagree, 4
  untestable (no gloss). Limits: it tests key values only, on 11 groups; the n.63 dictionary is typed into the script
  and nothing in the folder proves it was fixed before n.194 was read. The script now flags glossed groups outside
  their n.63 alphabetical slot: 6 flagged, all explained (43 is the doubtful group below; [2]858 sorts as 2858;
  1213 is glossed with the Latin synonym "legat" for Gesandter; 1441, 1442, 1444 are glossed with the duchy only,
  value Hertzog in X).
- `scripts/order_check.py`: 72 firm values, 3 out of alphabetical order, each explained: 1501 D. Hoe (sorts under Hoe),
  2743 -strasse (second part of Berg-strasse), 2858 Bethlen Gabor (sorts under T, Transsylvanien, after Translation
  2850/2851). Limits: it skips groups below 100 (so 43 is never tested) and sorts every "König in X" under König, so
  it cannot see that 1682-1687 interleave Böhmen, Dennemarck and Engelland.

## Survey of n.129-210 (task: find letters without a contemporary decipherment)

Scans 540-912 were fetched one at a time, 1 s apart, and an AI language-model agent counted code groups per page
(working files of WAINUT, not in this target; piece numbers as the model read them, approximate). About 4,500 code groups across about 75 pieces; the densest are n.198-210 (scans 813-896). The
model's "glossed/unglossed" counts proved unreliable (it reported 0 glossed on n.194 fol. 416r, which is glossed), so
gloss presence was checked by eye on bands of these scans: 582 (n.129), 589 (n.131), 597, 601, 609, 619, 625, 637,
641, 646, 651, 703, 715, 724, 728, 741, 749, 754, 757, 795, 797-799, 805, 821, 831, 838, 853, 859.
**Every letter checked carries interlinear decipherments over its code groups**; single groups are left unglossed
here and there (484 Camerarius often; the margin postscript on scan 646 partly). No wholly unglossed letter was found,
so there is no ciphertext-only break in the series: each letter is a transcription job. Not checked by eye: the rest
of the pieces of the survey.

## Reading of n.194 (scans 797, 798 = 800, 799; fol. 413r, 413v, 416r)

Files in `n194/`: `transcription_n194.txt` (102 lines, clear text and code groups), `code_groups_n194.tsv` (60 code
groups: two passes of the digits, the gloss as read, the reading), `decryption_n194.txt` (rebuilt by the checker),
`reading_n194.md` (German), `translation_n194.md` (English).
`python scripts/check_marks.py n194` rebuilds the decryption from transcription, table and key; it fails on any
unmarked departure from the key, any unmarked doubtful value or sign, and any mark without a doubt under it. Result:
`result: ok`.

Word count against the 95% bar (from the checker, after the fixes): clear-text words 784, of which 43 not read
([?word], [...], or under the pasted slip); code groups 60, of which 55 read; all tokens 844, **read 796 = 94.3%**.
Words marked [?word] are counted as not read even where a reading is proposed. Before the independent check the
count was 804 = 95.3%; the check showed two code groups and six clear-text words that should have been marked.

## Fixes after the independent check (VERIFY.md, 3 Nov 2026)

Each point about signs was re-examined on crops of scan 799 at 2.6-5x before it was changed. No disagreement with
the check remains.
- 1393 -> **1394** (l.87): the last sign has the form of the 4 in 1344 and 1684, not the round 3 inside the same
  group. Both of our passes had 1393, so the pass check could not catch it. Value Heilbronn unchanged.
- **1682** (l.72): the gloss reads "K. i. B." (the last letter has two bows and a waist), not "K. in D.". This gloss
  was the only source of key entry 1682, which is now `[?König in Böhmen]`, status doubt. It changes who is asked
  to write to the Lower Saxon Circle: the King of Bohemia (Frederick V), not Christian IV. 1684 = König in Böhmen is
  glossed elsewhere, so a second homophone is plausible.
- **43** (l.83): marked doubtful. The n.63 letter table gives o=43, numbers below about 70 are single letters, and
  43 is out of alphabetical slot for "Dohna". A small stroke before the 4 may be a pen mark or a short 1 (143).
  The gloss "v. Dona" is certain; its first word ("Freyh."? "Burggr."?) is open.
- 1344 (l.83): the gloss is legible as "Gr. hofm.", agreeing with n.63; key status now `both`.
- Clear text marked doubtful: l.71 fürchte ich (or "förchte dz"), l.75 den (or dem/zum), l.79 motus (or modus),
  l.80 verlangen (or "hinlang-"), l.92 schicken (or schreiben). The check also reads part of l.73 ("hett dz drei-")
  where we have two [?...]; not adopted, as we could not confirm it.
- Translation: interpretive fillers are now marked [conjecture: ...].

Transcription method: code digits read twice (strips at 1.5-1.9x, and a second read at another scale; for fol. 413v
the independent second exposure on scan 800). Clear text: read by eye from strips at 1.7-1.9x; an AI language-model
draft (a WAINUT working file, not in this target) was used only as a cross-check and is often wrong.

Summary: Bremen, end of May 1622, during Camerarius's mission to Denmark and the Lower Saxon Circle for the exiled
Frederick V. News of Prince Maurice's raid into Brabant; worry about England, the transfer of the electorate to
Bavaria and the Brussels conference. The Bremen diet has refused the archbishop's triple levy, through Camerarius's
groundwork; imperial envoys at Lüneburg demand a contribution from the Lower Saxon Circle, which is to be granted only
if the Elector Palatine is restored. Electoral Saxony quarters troops in Thuringia. Christian IV of Denmark is
"too deep in private matters" (Osnabrück, Verden) and goes to Norway in June. Christian of Brunswick has raised
100,000 thalers from the Eichsfeld. Camerarius has written several times to the King of Bohemia without an answer.

## Remaining gaps (n.194)

- 1513 (fol. 413r line 28): gloss not legible on the microfilm; no other occurrence seen. Context: something granted
  to the Count of Oldenburg.
- 2472 (fol. 413v line 69): gloss not legible; slot R between Regierung 2456 and Resolution 2503 suggests Reichstag
  (the Norwegian assembly the King must attend); marked doubtful.
- [2]858 (fol. 416r line 82): the left of the group is under a pasted slip; the gloss "B. Gabor" fits 2858 Bethlen
  Gabor (glossed in n.193 and n.180); marked doubtful because the sign is not fully seen.
- 1682 (fol. 416r line 72): gloss "K. i. B." read on re-examination (King of Bohemia; the first read "K. in D." gave
  Denmark). Sole source of the key entry; marked doubtful. A better image of the gloss would settle it.
- 43 (fol. 416r line 83): gloss "v. Dona", but 43 is o in the n.63 letter table and out of alphabetical slot; a small
  stroke before the 4 may make it 143. Marked doubtful.
- Clear text: 43 words not read, of which 6 are covered by the pasted slip on fol. 416r (an outside blocker: needs the
  original or a colour scan); 6 were marked after the independent check (see above); the rest are microfilm-limited
  words in the Kurrent hand.

## Escalation

Tried: n.63 key; glosses in n.193, n.194, n.196 and 20 other scans of the series; alphabetical slot; second exposure
(scan 800); a language-model draft as cross-check. Next: colour scans of the originals from the BSB would settle the
three groups and most uncertain words. The other ~74 letters of the series are open transcription jobs with the same
key; n.193 and n.196 are next (their glosses are already partly read into `key.tsv`).

## Open items

- **n.106 ("Rota" to "Vatron", 1624), not part of this target**: Italian clear text with run-together two-digit numbers and the letters g, p,
  t, c, x, & as code signs; no decipherment on the page; ciphertext-only. Names the Capuchin Giacinto ("Non erubesco
  Evangelium", cf. n.108). Not attempted. A separate system; the one genuinely open target found here.
- n.63 scan 290 pairs not yet read.

## Prior art (3 Nov 2026)

- Dan's repo origin/main: no Camerarius, Clm 10397/10398 or Solms target; open PRs (#201, #216, #227) unrelated. The
  only Camerarius hit is R4284 (Riksarkivet, 1628), a different numerical cipher.
- Web searches (Camerarius, Chiffre, Solms, Clm 10397; Schubert 1955): no decipherment or edition of the
  Camerarius-Solms letters found. F. H. Schubert, *Ludwig Camerarius 1573-1651. Eine Biographie* (Kallmünz 1955; 2nd
  rev. ed. Münster: Aschendorff 2013, 773 pp.) worked through the Camerariana and may quote the glossed passages; not
  seen. Ernstberger's 1961 edition is the Camerarius-Behaim correspondence of 1636-48, not this series.
- The glosses on the pages are contemporary or early decipherments: prior art for every glossed letter.
- After the independent check (3 Nov 2026): one more web search for the *Briefe und Akten zur Geschichte des
  Dreißigjährigen Krieges* with Camerarius, Solms, 1622 found no matching letter, but no volume was opened.
  Schubert (1955; 2013) and the Briefe und Akten series (including the Neue Folge for 1618-1651) remain unchecked;
  either may quote or summarise these letters. **Nothing in the content of n.194 is claimed as new.**

## Images

https://www.digitale-sammlungen.de/en/view/bsb00116446?page=797 (n.194), ?page=795 (n.193), ?page=805 (n.196);
https://www.digitale-sammlungen.de/en/view/bsb00116447?page=287 (n.63), ?page=469 (n.106). Fetched by `scripts/fetch.py`
and the survey script (IIIF, one request at a time, ~1 s apart, User-Agent WAINUT-research); no blocks met. Scans in
`scans/` are not for git.
