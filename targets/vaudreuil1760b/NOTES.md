# Vaudreuil to Berryer, Montréal, 29 Aug 1760 (ANOM COL F3 16 ff.115r-v): the letter on the loss of Canada

Status: read (ff.115r-v only, by the period interlinear decipherment; ff.116-119 are outside this entry).

Brice Dudout with AI agents (Claude Opus 5.5), 23 Nov 2026. Images:
Archives nationales d'outre-mer (France), COL F3 16 ff.115r-v, IREL FRANOM82_247MIOM013_F3_016_187-188 (free
reuse, ANOM decision 2018-1, with credit); not in this folder. This is lead 1208 ("Vaudreuil to Berryer announcing
in figures the loss of the colony"). The letter runs to f.119 (images 189-195); this entry covers only the two
pages on file, ff.115r-v.

## Prior work
Already solved at the time: the clerk wrote the decipherment above every line of all nine pages. Parkman,
*Montcalm and Wolfe* II (1884) pp.380-381 translates passages; Richard's 1899 calendar summarises it. The letter
cites Vaudreuil's earlier cipher letters of 23 April, 26 and 28 June and 13 August 1760 (the last is catalogue 1391,
targets/vaudreuil1760).

## Test (protocol hashed before any computation: PREREG_fr.md, SHA-256 45352c61...)
- Key: the 1757 Vaudreuil table (ANOM C11E 10, LAC e001295274), unchanged. In the repository it is
  `targets/vaudreuil1759a/dudout/key.tsv` (SHA-256 fc77f13b...). The hash 7b5aecb2... in PREREG_fr.md is that of our
  local file KEY_v2.tsv: the same 700 numbers and values, with French column names and without the English header
  lines. Rerun: `python3 measure.py ../vaudreuil1759a/dudout/key.tsv cipher_ff115.txt gloss_ff115.txt`.
- Portion: ff.115r-v, 561 groups (cipher_ff115.txt) vs the gloss (gloss_ff115.txt), both hashed before the run.
- **Result: 0.9739 characters; best of 200 shuffled tables 0.2221 (mean 0.142) → pass.** Words: 294/318 (92.5%).
- Dates: the table was validated on the glossed letter of 8 May 1759 (ANOM C11A 104 ff.79-83, LAC transcript;
  `targets/vaudreuil1759a/dudout/validation.txt`), which is the "8/5/1759" of PREREG_fr.md; the earliest letter read
  with it is cat. 1388, dated "A Montréal le 8 avril 1759" in clear on the page. So the same table served from at
  least 8 Apr 1759 to 29 Aug 1760.

## Content (from the gloss)
ff.115r-v: Vaudreuil recalls his cipher letters on "notre déplorable situation" and the overwhelming British forces
by water and land; asks that the King be told of the zeal of the troops and Canadians at the battle of 28 April
(Sainte-Foy) and the siege of Québec, which he hoped to retake "si une ou deux frégattes nous fussent parvenues";
the British navy's vigilance meant abandonment; Murray burns the houses of those who defend their country, so
Vaudreuil decreed death for Canadians who surrender their arms or desert and the burning of the houses of those who
do not join; the Canadians stay loyal.

## Not done
ff.116-119 (images 189-195): neither figures nor gloss transcribed; they are outside this entry and its fraction
(1.0 = 318/318 gloss words of ff.115r-v).
