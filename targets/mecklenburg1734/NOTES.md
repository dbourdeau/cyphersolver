# Hanoverian Privy Council, Mecklenburg commission, 1731-1761 (NLA HA Hann. 9g; Unsolved Catalogue no. 598) — NOTES

Status: in progress. Every cipher passage opened so far (five files, 1731-1738) carries its contemporary
decipherment written between the lines. One passage transcribed and read (Nr. 964 f. 6), one transcribed and read in
part (Nr. 964 ff. 8r-8v, WAINUT section below; not closed); the rest still to transcribe.

**Verdict so far: deciphered at the time.** The Hanover chancery wrote the decipherment above each line of figures, in
the rescripts from London as well as in the reports from Vienna. The catalogue's question ("whether decipherments are
filed with them is not stated") is answered: they are on the same pages. Outcome method, once the passages are
transcribed: *read from existing decipherment*. Checked 26 Oct 2026.

## Sources

- Niedersächsisches Landesarchiv, Abt. Hannover, Hann. 9g (Mecklenburgische Exekution / Kommission), Nr. 97, 379, 563,
  964, 1065, 1130, 1225, 1492, 1494, 1647. Finding-aid entries via the DDB index (Archivportal-D is behind an Anubis
  bot wall; the public Solr index is not).
- Images, public domain mark, no login. METS: `https://www.arcinsys.niedersachsen.de/arcinsys/mets?detailid=<v-id>`.
  Images follow a fixed pattern:
  `https://www.arcinsys-digitalisate.niedersachsen.de/nla_ha/hann._9g/nr._<n>/m_ha_hann._9g_nr._<n>_aufn_<NNN>.jpg`
  (about 7600 × 6700 px, one opening per image; `thumbs/` holds 150 px versions). `scripts/fetch_nla.py n:count ...`
  downloads and downscales them. Images are not committed.

| Nr. | Arcinsys | images | dates | finding aid ("Enthält: u.a.") | seen |
|---|---|---|---|---|---|
| 97 | v2492433 | 12 | 1733 | chiffrierte Verlautbarung, Christian Ludwig ↔ Seckendorf secret talk | all 12 |
| 379 | v2492434 | 23 | 1731 | zwei chiffrierte Schreiben an Georg II., Karl Leopold's Submissionsschrift | 4-8 |
| 563 | v2493774 | 19 | 1738-39 | chiffrierter Bericht aus Wien (Khart's "Gnadengeschenk"); chiffriertes Reskript | 5-8 |
| 964 | v2493412 | 19 | 1734-35 | chiffrierte Berichte Erffas aus Wien, Reichskontingent | all 19 (thumbnails), f. 6 zoomed |
| 1065 | v2493405 | 392 | 1734-38 | chiffrierte Reskripte Georgs II., schwarzburgische Truppen | not opened |
| 1130 | v2492829 | 16 | 1735-36 | chiffrierter Bericht Erffas, Rostock commandant | 5-8 |
| 1225 | v2493363 | 64 | — | chiffrierte Korrespondenz mit von Haus in Wien | not opened |
| 1492 | v2492740 | 308 | 1733-35 | z. T. chiffrierte Reskripte; Schwerin | not opened |
| 1494 | v2492742 | 253 | 1736-39 | chiffrierte Berichte Erffas, schwarzburgische Truppen | not opened |
| 1647 | v2493788 | 105 | 1760-61 | chiffrierter Bericht Steinbergs aus Kopenhagen | not opened |

## Cipher passages seen (image numbers = `aufn_NNN`)

| file / image | folio | piece | cipher | decipherment |
|---|---|---|---|---|
| 97 / 003 | f. 2r | P.S. to the King, Vienna 14 Jan 1733 (pr. 21 Jan) | about 9 lines of figures | interlinear |
| 97 / 004 | ff. 2v-3r | same P.S., continued | about 14 lines | interlinear |
| 97 / 011 | f. 10r | rescript, St James 2/13 Mar 1733 | 7 lines | interlinear |
| 563 / 006 | f. 4r | report, Vienna 1738 | 5 lines | interlinear |
| 563 / 007 | f. 4v | same | 8 lines in two runs | interlinear |
| 964 / 007 | f. 6r | rescript, St James 6/17 Dec 1734 | 4 lines | interlinear; **transcribed** (`texts/964_f6.txt`) |
| 1130 / 007 | ff. 6v-7r | Erffa's report on the Rostock command, 1735 | about 14 lines in four runs | interlinear |

The outgoing drafts (e.g. 964 / 004, to Erffa, 5 Dec 1734; 1130 / 005, to Erffa, 1735) are clear Konzepte with the
passages to be enciphered underlined. They are a second plaintext source for the outgoing letters, whose enciphered
originals are in Vienna, not here.

## The cipher

Undivided runs of figures, written continuously across lines, inside letters otherwise in clear German. A code, not a
letter substitution: on f. 6 about 140 figures carry about 20 words / 120 letters ("was ihr wegen des Mecklenburgischen
Reichs Contingents und dass dessen Stellung von des Königs von Preussen Maj. nicht übernommen werden möge"), too few
for one 2-digit group per letter, so the groups stand for syllables or words (probably 3- or 4-figure groups of a
Hanoverian code). Group boundaries are not marked. No key table was built.

## Remaining gaps

- The other cipher passages are not transcribed. Blocker: none from outside; it is transcription work on public
  images. Five files (1065, 1225, 1492, 1494, 1647; 1,122 images) not yet opened.
- No group-by-group check of a decipherment against the figures; that needs the code (rebuildable from the
  interlinear pairs, which would also give the Hanoverian code of the 1730s).
- Nr. 1647 (Steinberg, Copenhagen 1760-61) is a different decade and probably a different code; not opened.
- Nr. 964 ff. 8r-8v (WAINUT section below), the five barred stretches (BAR1, BAR2, BAR3, tails of C5 and C12; about
  72 of 461 figures, no decipherment over them): probably nulls, not unread text (see "Barred stretches" below).
  Blocker: not attempted. Confirming it needs part of the code, rebuilt from the interlinear pairs of more passages
  (the key-rebuild step below); if a stretch turns out to be text, the same rebuild would read it.
- Nr. 964 ff. 8r-8v, uncertain words: the gloss over C3, the end of C2's gloss, the last word over C4, and in the
  clear text "[?jetzt] [?hereinkommenden]", the word before C2, "[?hätten]", "[?begreiflich]" and the councillor's
  name "[...] Rath [?Verporten]". Blocker: none from outside; another pass on the public images by a reader of
  German chancery hands. This piece is not closed at "read in part": the words are workable.

## Escalation

- 0a siblings / clear pages: done in the sense that matters: the decipherments are on the cipher pages themselves.
- Next: page through 1065, 1225, 1492, 1494, 1647 (thumbnails are too small; fetch at 2400 px), list the cipher
  pages, transcribe each run with its interlinear decipherment, then align runs to decipherments to rebuild the code.
- Prior art: not on DECODE (Archivportal-D sweep README); no printed edition of these Hann. 9g pieces found in the
  quick web check of 26 Oct 2026. The decipherment found is the contemporary one, not a modern one.
- Nr. 964 ff. 8r-8v (WAINUT, 27 Oct 2026):
  - [x] siblings: f. 6 in the same file compared; no shared figure strings, and no barred run recorded there
  - [x] clear-pages: the clear text around each run used for the sense, including the null test of the barred
    stretches; the clear draft on image 004 noted
  - [ ] known-keys: no Hanoverian code of the 1730s found to try
  - [x] print: one web search, no edition found; "von Knörre" probably identified (see Prior work below)
  - [ ] key-rebuild: aligning glosses to figures across more passages (Nr. 97, 563, 1130, 1494) could rebuild part
    of the code and settle whether the barred stretches are nulls
  - [ ] retry: the uncertain words on another pass

## Contribution by WAINUT (27 Oct 2026)

Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company. The work was done with AI language-model
agents; the transcription was made with a vision-capable language model from the full-resolution NLA images, and
every figure and gloss was re-read independently by a second agent. This section adds one cipher piece that the
table above does not list: Nr. 964 ff. 8r-8v. The files in `texts/` are unchanged; above, the status line and the
main Remaining gaps and Escalation sections gain the f. 8 entries (review fix). The new files
are in `wainut/`, and `profile.json` gains one document (`964-f8`), its `outcome.texts` entry, one gap, two
credits and dated solution steps; existing entries are untouched.

**Scope.** Before starting we checked this folder's NOTES and WORKLOG: f. 8 is not listed or transcribed here, and we
know of no one else working on it. The other cipher passages listed above (Nr. 97, 563, 1130) are **not**
transcribed in this contribution, and the five unopened files stay unopened.

### Nr. 964 ff. 8r-8v: Erffa to George II, P.S. no. 13, Vienna 18 Dec 1734 (received 25 Dec)

- **Source.** Images aufn_009 (right page, f. 8r) and aufn_010 (left page, f. 8v) of Nr. 964 (Arcinsys v2493412;
  METS `https://www.arcinsys.niedersachsen.de/arcinsys/mets?detailid=v2493412`;
  [image 009](https://www.arcinsys-digitalisate.niedersachsen.de/nla_ha/hann._9g/nr._964/m_ha_hann._9g_nr._964_aufn_009.jpg),
  [image 010](https://www.arcinsys-digitalisate.niedersachsen.de/nla_ha/hann._9g/nr._964/m_ha_hann._9g_nr._964_aufn_010.jpg)).
  Docket "Wien den 18. Dec. 1734", "P.S. 13. praes. d. 25. Dec. 1734", signed Erffa; folio numbers 8 and 9 on the
  page. On the contact sheet of all 19 images, 004 and 011-018 look clear (drafts, a Copia); that was not re-checked
  independently.
- **Cipher.** 16 runs of undivided figures in the secretary's hand, **461 figures** in all
  (`docs/_check_profile.py --measure wainut/964_f8_cipher.txt --drop-first --width 1`). 13 runs carry a
  decipherment written above them in a smaller, darker hand. Five stretches have a long stroke drawn above them and
  no decipherment: three whole runs (BAR1 16 figures, BAR2 21, BAR3 16) and the tails of C5 (about `...29835 1457`)
  and C12 (about `...657720511`), about 72 figures. The clear text resumes right after each of them.
- **Transcription** (`wainut/964_f8.txt`, line by line with the glosses and the clear text; `wainut/964_f8_cipher.txt`,
  figures only). The two readings agree digit for digit. C11's 2nd figure (2) is uncertain (a blot); C12's 4th
  figure was read 6 by the second reader and left open by the first. In BAR2 the 5 after `26533` is a clear figure.
  A review pass changed one figure that both readers had as 8: the 2nd figure on C8's second line is more likely a
  2 (`...1204 / 22958`), because the upper loop that made it look like an 8 is the descender of the "y" of the gloss
  "beyden", in the darker ink. It is marked uncertain. The repeat check gives the same results either way.
- **Glosses**, as written: C1 "dem RhsRaht von Knörre"; C2 "dasjenige [?bewürket] w[...]"; C3 "[?dienstlich]" (the
  two readers had "dieserhalb" and "dinst[l?]ich"); C4 "[?befürchtet] und hier eingeleitet zu werden" (the last
  word may be "werben", to recruit); C5 "nunmehr, der von Knörre"; C6 "über sich genommen mit dem"; C7 "RVCantzler
  Grafen von Metsch und dem"; C8 "von Bartenstein, wenn ich mir vorher bey / beyden"; C9 "man mit Ihr. Kayserl.
  Mayt."; C10 "statt würcklicher Stellung gedachten"; C11 "Contingents über ein gewisses Quan-"; C12 "tum an Geld
  übereinkämen"; C13 "meinet der von Knörre".
- **Reading** (`wainut/964_f8_reading.md`, German; `wainut/964_f8_translation.md`, English). Erffa has informed the
  Imperial Aulic Councillor von Knörre about the raising of the Reich contingent on the part of Mecklenburg. Knörre
  is willing to help. Once Erffa has put the matter to them, he will speak with Vice-Chancellor Count Metsch and with
  Bartenstein and try to make them see that the best means is for Mecklenburg to agree with the Emperor on "a certain
  sum of money instead of the actual raising of the said contingent". If the Emperor approves, Metsch could make his
  intention known to a Privy Councillor whose name is not read with certainty ("[?Verporten]"). The ciphered parts
  are the names and the money proposal. This is the Vienna side of the matter in the rescript on f. 6 (6/17 Dec
  1734: Prussia should not take over raising the Mecklenburg contingent) and Erffa's answer to the rescript of 5 Dec
  1734 (the clear draft of that rescript, to Erffa at Vienna, is on image 004). State: **read in part**, because of
  several uncertain words (workable, see Remaining gaps) and the five barred stretches (probably nulls, see below).
  The piece is not closed.
- **Where the gloss "der von Knörre" sits.** It is written over C5's figures `2152220834 0590365 97`, which do not
  contain the Knörre figures. BAR2, which follows, does (`2159826533...13571`, as in C13 "der von Knörre"). Either the
  gloss was moved up for lack of space, or the code has two different groups for the same words. Open.

### Check against the figures (no key)

No key is in the file or in this repository, so the decipherment is **not checked group by group**. What was
checked is whether it is consistent with repeats in the figures (`python wainut/repeats.py`):

| String | Runs | Glosses over those runs |
|---|---|---|
| `2653313571` (10 figures) | C1, C13 only | both "...von Knörre" |
| `2159826533` (10 figures) | C13, BAR2 | C13 "der von Knörre"; BAR2 none |
| `2653313` (7 figures) | C1, C13, C7 | "von Knörre" twice, "Grafen von Metsch" |
| `26533` | C1, C7, C13, BAR2 | |
| `13571` | C1, C13, BAR2 | |
| `31544` | C2, C5, C6 | no common word is obvious |

- **Control.** Shuffling the figures inside each run (2,000 times, each run's digit counts kept) never gives a
  shared string longer than 8 figures, and never a 5-figure string in four or more runs. The repeats are real code
  structure, and they fall on the runs glossed "von Knörre" and "von Metsch".
- **Limits.** `26533` is not in every run whose gloss has "von" + a name: C8 ("von Bartenstein") and C5 ("der von
  Knörre" written above it) lack it. C8 has 44 figures for about 39 letters, about one figure per letter; that rules
  out two figures per letter but does not by itself show a code of variable-length groups.
- **Cross-check with f. 6.** The London rescript on f. 6 (`texts/964_f6_cipher.txt`) shares no 5-, 6- or 7-figure
  string with f. 8, not even for "Contingents", "Stellung" or "von"; against shuffled f. 8 runs, one or more chance
  6-figure matches come up about 4% of the time. So the London-Hanover rescripts and the Vienna-Hanover reports
  probably use different codes, or the code is strongly homophonic.

### Barred stretches: probably nulls (review, 27 Oct 2026)

The maintainer's review asked whether the barred stretches are nulls rather than unread text. Tested on the figures
and the sense, without a key:

- **The sense needs nothing there.** The glossed runs carry about 1.2 figures per gloss letter (390 figures for 316
  letters; C1 1.11, C13 1.17, C8 1.13). At that rate the 72 barred figures would be about 60 letters, some 8-10 words.
  Yet the clear text and the glosses read straight through every bar: "der von Knörre [C5 tail, BAR2] hat sich
  gantz willig dazu erklärt"; "über ein gewisses Quantum an Geld übereinkämen [C12 tail, BAR3]." ends the
  sentence. BAR1 is the weakest case, because the end of C2's gloss before it is not read.
- **They are built from neighbouring real groups.** BAR2 (`215222 159826533 5 13571`) is C13's "der von Knörre"
  string `2159826533`+`13571` with one 5 inserted, preceded by the `215222` that opens the stretch under C5's
  "der von Knörre". BAR1 ends with `40546`, which opens C9; BAR3 opens with `16514`, which is in C11. The C5 and
  C12 tails share no 5-figure string with any glossed run.
- **f. 6 has none.** The London rescript on f. 6 (`texts/964_f6.txt`) records no barred run; all four runs are
  glossed and the gloss reads through. That transcription was not made with bars in mind, so this is weak.
- **Reading.** A stroke over figures that the decipherer did not gloss, where the sense is complete and the figures
  copy real groups, is what recognised padding looks like. So the barred stretches are probably nulls. This is not
  proved: it needs the code (key-rebuild), and the other passages (Nr. 97, 563, 1130) are not transcribed, so no
  barred runs there were looked for. In the reading files the stretches stay marked as holes.

### Prior work

The decipherment is the contemporary one, on the same pages. One web search (Reichshofrat Knorr 1734, Erffa,
Bartenstein, Contingent) found no printed edition of this report and no identification of "von Knörre". A
biographical entry for a Georg Christian (von) Knorr at Vienna turned up in the first pass. Checked in review (one
search, 27 Oct 2026): the Niedersächsische Bibliographie person record gives Georg Christian von Knorr (b. Oettingen
1691, d. 22 Jan 1762), Hofrat in Brunswick-Wolfenbüttel service at Blankenburg from 1725, ennobled 1728, Wirklicher
Reichshofrat in Vienna from 1730; the Francke-Halle database adds Wolfenbüttel envoy in Vienna. "RhsRaht von
Knörre" in 1734 is therefore **probably** Georg Christian von Knorr; only these two short entries were seen.

Remaining gaps and escalation for this piece are in the main sections above.

### Files (in `wainut/`)

- `964_f8.txt`: line-by-line transcription (figures, interlinear decipherment, clear text)
- `964_f8_cipher.txt`: the 16 runs of figures only
- `964_f8_reading.md`, `964_f8_translation.md`: the reading as German sentences, and its English translation
- `repeats.py`: the repeat table, the shuffle control and the f. 6 cross-check (standard library)

## Read share over cipher words only (16 Nov 2026)

README Conventions, 16 Nov 2026: the read share counts the words written in cipher. Neither entry had a read share.

| document | before | after | state |
|---|---|---|---|
| 964 f. 6 (`texts/964_f6_reading.md`) | none | 1.0 (21 of 21 cipher words) | read, unchanged |
| 964 ff. 8r-8v (`wainut/964_f8_reading.md`) | none (whole piece 0.896) | 0.862 (56 of 65) | read in part, unchanged |

- How the cipher was separated: both readings put the contemporary interlinear decipherment of the figure runs in
  ⟨ ⟩ inside the clear text; the ⟨ ⟩ words are the cipher. On ff. 8r-8v the five barred stretches stand outside the
  ⟨ ⟩ and are cipher too.
- Holes on ff. 8r-8v: [?bewürket], [...], [?dienstlich] and [?befürchtet] inside the ⟨ ⟩, and the five barred stretches,
  one word each, because their size in words is not known. The uncertain words of the clear text ([?jetzt],
  [?hereinkommenden], the word before C2, [?hätten], [?begreiflich], [?Verporten]) are not counted. If the barred
  stretches are nulls ("Barred stretches" above), the share is 56 of 60 (0.933).
