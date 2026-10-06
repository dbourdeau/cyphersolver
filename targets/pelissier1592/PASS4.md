# Fourth pass brief (one page per agent): close the [?] gaps

Working dir: C:\Users\dbour\cypher\targets\pelissier1592 (Git Bash; python). Read GLYPHS.md and PASS3.md first (the split
glyph tokens, the crop tools, the canvas map 46r=100 46v=101 47r=102 47v=103 48r=104 48v=105 49r=106 49v=107 50r=108).
Page files: t<folio>.txt (tokens), reading_<folio>.md (reading; "Rows still unresolved" lists open rows with tokens),
READING.md (all pages; the section "## f. <folio>" is this page). Freeze the pass-3 state first:
`cp t<folio>.txt t<folio>_p3.txt; cp reading_<folio>.md reading_<folio>_p3.md` (skip if they exist).

Goal: turn as many [?] words on this page into honest readings as possible. The project's rule is that a word counts
as read only when the signs, as seen in the image, decode to it under the key (GLYPHS.md / cands.txt), allowing at most a
writer's slip that the context forces and that you name. A word that merely fits the context does not count: leave it [?].

For every [?] (and every "..." inside {braces}) on the page:
1. Locate its tokens in t<folio>.txt and its place on the scan; crop at high zoom (`python crop.py img/cNNN.jpg X0 Y0 X1 Y1
   crops/p4_<folio>_<row>.jpg 1900`, 300-600 px of original width per view) and re-read each sign against GLYPHS.md and the
   atlas (cal/atlas/). Look especially for missed or doubled signs, nulls (#, #o, #x, C) misread as letters and vice versa,
   and split-family confusions.
2. Fix the tokens (add a `# p4:` comment with what you saw), run `python beam.py t<folio>.txt`, and check the decoded French.
   Also try `python diag.py 2.0` style reasoning: if one sign must be some other letter, say which sign and look again at it.
3. Pool: if an open sign or word recurs on other pages, grep the other t*.txt files and use those occurrences.
4. If the reading is firm, replace the [?] in reading_<folio>.md AND in the matching place in READING.md. Doubtful but
   sign-supported readings get (?); unsupported ones stay [?]. Never alter text outside this page's section in READING.md.
Save after every few gaps. Update the "Rows still unresolved" list. Do not edit any file outside targets/pelissier1592/,
do not commit, do not edit cands.txt (report a missing token instead). Do not launch subagents.

Report back (short): [?] count on the page before and after (count in READING.md's section), each new reading with its row
and the sign evidence in one line, the gaps that stay open and why (illegible blot / hole / sign unknown / code group).
