# waldeck1655: Count Georg Friedrich of Waldeck to Elector Frederick William, September 1655 (catalogue 2539)

Same volume and image route as `../friedrichwilhelm1655/NOTES.md` (Gelders Archief 0370 inv. 1257, register copies).
These are Waldeck's letters to the Elector, kept in his register of acts: mostly clear German in his own cursive, with
short passages in the Elector's number cipher.

| doc | scans | what | state proposed |
|---|---|---|---|
| w787 | 787-789 | letter of 7 Sept 1655: six cipher passages (42 groups) inside clear text | read in part |
| w813 | 813-814 | letter of Königsberg, 14 Sept 1655: three short runs and one block of 12 lines (57 groups) | read in part |

Only the cipher passages and the clear words beside them are edited; the clear text between them is not transcribed.

Key: the Elector's key (`key.tsv`, frozen from c793 in the other folder) applies unchanged. Held-out: these letters were
not used to build it; every number in them is in the frozen key except 18 (read x from "Weixel", 813.c, added after the
freeze) and 51 (twice, 813.a and 814.12), which is not a letter. From context 51 stands for a person, probably the
Elector ("damit [51] an hand zu gehen", "ungeneigt [51] beizustehen"); it is left as [51].

Reading (scripts/check_marks.py passes): w787 106 words, 99 verbatim (93.4%), 1 marked repair, 6 context fills
(binding), 4 holes; Dan's checker clean share 0.889. w813 72 words, 64 verbatim (88.9%), 5 marked repairs, 3 fills, 2
holes ([51]); clean share 0.833. Counts include clear words (w787 about 63, w813 about 12). Four of the w813 repairs are
line ends of scan 814 in the binding where nothing is lost because the word runs on to the next line (D-antzig, e-ine,
ha-lten, au-ch); they are marked `{[...]/}`.

Where the clean share comes from: `docs/_check_reading.py --file` on the sentence text of each reading, shipped as
`work/text_<doc>.txt` (built with the reading by `scripts/make_reading.py` from `work/marked/<doc>.txt`). In folder mode
on the shipped files (`python docs/_check_reading.py waldeck1655`) the reading files score lower, w787 0.629 and w813
0.552, because each `reading_<doc>.md` also holds the marked line-by-line block, where every mark counts as a hole.
`scripts/reading.py` (run by `check_marks.py`) fails when a `[...]` or `[nn]` of the decryption is dropped from a reading
line without a mark.

Content: the conditions with Sweden could hardly be worse; Waldeck has written to Jacob Weiher, to Elbing and to Danzig,
and will speak to the Bishop of Ermland; Danzig offers ships; provisions (vivres) against cartage money or security; news
to General Sparr. 14 Sept: Weiher offers help; Vistula boats ordered at Marienwerder; Magnus reports from Thorn that the
town resolves to defend itself, plans a meeting with Danzig, Elbing and the three voivodes on the Vistula, and is not
unwilling to help [51].

Prior art: as in the other folder (11-12 Nov 2026: catalogue vetting and one web search, nothing found).
Erdmannsdörffer, Graf Georg Friedrich von Waldeck (1869), is not opened; it draws on the Arolsen archive and may quote
the Waldeck side of this correspondence. This is the main open prior-art point.

## Independent review (12 Nov 2026)

The same independent AI language-model agent that reviewed `../friedrichwilhelm1655/` copied six cipher lines of these
letters blind from the scans (813.a, 813.b, 787.a, 787.b, 814.05, 814.07); all agree with the transcriptions number for
number. It reproduced the mark check and the clean shares. Grades (reading_review in `profile.json`): w787 B (only the
cipher passages are edited, so several passages are fragments; 788.20-24 has 4 holes), w813 B (the sentences hold;
[51] is unresolved, and reading it as the Elector is a guess). It found that 814.05, 814.07, 814.08 and 814.10 dropped
the binding hole of the decryption without a mark; they are now marked `{[...]/}` and the counts above are updated. No
state changed.

## Remaining gaps

- The clear text of both letters - blocker: not-attempted; only the cipher passages and the clear words next to them
  are edited, so several passages of w787 are fragments.
- 788.20-788.24 and the line ends of scan 788 - blocker: needs-physical-access; four holes, letters lost in the binding.
- Number 51 (813.a, 814.12) - blocker: open-codes; not a letter, from context a person, perhaps the Elector (a guess).
- 787.a "S{i/c}hweden" - blocker: illegible; 2 or 12 not settled on the image.
- "Magnus" (814.01) - blocker: not-attempted; not identified with certainty.
- Blind second reading of the cipher - blocker: not-attempted; pass 2 was made with the key known; the reviewer's blind
  spot-check of six lines agrees fully.
- Erdmannsdörffer 1869 - blocker: not-attempted; not opened (see Prior art).

## Escalation

- [x] siblings: the Elector's letters in the same volume are read in `../friedrichwilhelm1655/`, which gave the key.
- [x] clear-pages: the register copies carry marginal summaries of the clear text only; no decipherment of the cipher
  passages was found on these scans.
- [n/a] known-keys: the key of the sibling letters applies unchanged; no other key of this correspondence is known.
- [ ] print: Urkunden und Actenstücke VII opened (catalogue vetting); Erdmannsdörffer 1869 not opened.
- [n/a] key-rebuild: the key is complete for letters; only 51, a probable code word occurring twice, is outside it.
- [x] retry: both letters decrypted with the final `key.tsv` (with 18 = x); the remaining holes are binding losses and [51].
