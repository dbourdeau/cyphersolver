# Blind reading brief: Enoch Long's cipher journal, 1779-1780

You are reading lines of a soldier's pocket journal (Enoch Long junior, a New Hampshire private in Rhode Island,
1779-1780), photographed from microfilm. He wrote plain English mixed word by word with a private cipher: each cipher
word is an ordinary English word written with one invented sign per letter, word spaces kept. His spelling is his own
(e.g. "dreamd", "uper").

Your job is to read the signs, one by one, as carefully and literally as possible. Someone else has read these lines
before; you must NOT look for or open their reading. Open only the files named in this brief: this brief, the chart
images in `work/chart/`, and the crops in `work/crops/` listed in your batch file. Do not open any other file or folder
(not the worktree, not NOTES, not any .tsv other than your batch list). Do not search the web.

## The two alphabets

**Alphabet A** (used July to September 1779 and in 1780). Signs are altered letters:

| letter | sign |
|---|---|
| a | short upright stroke (sometimes an a-like arch) |
| b | Greek-beta-like loop (β) |
| c | reversed c (ɔ) |
| d | small loop with a curl, like ∂ |
| e | two short bars with a hook, like a flattened reversed e or "=" |
| f | inverted f, like j or ɟ |
| g | g-like loop |
| h | slanted stroke "\", often bent at the top |
| i, j | a dot |
| k | rare; not settled |
| l | tall stroke (taller than a) |
| m | small cross "+" |
| n | short dash "-" |
| o | o (Long also writes o for u in some words: "op" for up) |
| p | looped sign like φ |
| r | v-like or small hooked stroke |
| s | z- or 3-shape (ʒ) |
| t | t with a high cross |
| u | inverted u, an arch (∩) |
| v | inverted v (∧) |
| w | wavy double stroke (~) |
| x | rare (an x-like sign) |
| y | f-like sign with a descender |

Worked examples (13R, lines 11-16; images `work/chart/A_example_line11.png` ... `line16.png`), braces = written in plain:
- line 11: {of procuring} [interlined above] I wrote {in my} letter to my
- line 12: dear {this, if I} send you {a} letter
- line 13: {with the} oper [= upper] part plain rub
- line 14: {it with your} hot box iron and
- line 15: {you may} read writing where
- line 16: {you} could {see none}

**Alphabet B** (from 4 October 1779). On 4 October Long wrote two rows of bare signs, 18 + 7, which we take as his new
alphabet in order, a to s without j, then t to z (`work/chart/B_alphabet_rows.png`; the values are our inference from
the order, he wrote no letters):
- row 1: a = short stroke with a small flag at the top; b = υ or 0-like loop; c = c; d = long curved stroke (ʃ);
  e = short dash; f = 6; g = 9 with a long tail; h = short slant "\"; i = a dot; k = 2; l = long straight slash "/";
  m = a cursive w-like sign (cups, ∪∪, with a tail); n = short dash (the same as e); o = o; p = S-like hooked loop;
  q = a hook like "?"; r = ʒ with a curl; s = a second ʒ-like sign (hard to tell from r)
- row 2: t = L with a loop at its foot; u = a stroke with a hook (ɩ); v = an i-like stroke with a dot; w = a cursive
  m-like sign (humps, ∩∩); x = +; y = colon ":"; z = a longer double dash "="

Known look-alikes on this film: in B, e/n (identical dashes, and z close), r/s, m/w (cups or humps), d/l (curved or
straight long stroke), a/u (flag at top or hook at foot); in A, a/l (short or tall stroke), e/s, h/r, n/dash marks
used as punctuation, i (dot) against specks.

## The crops

Each crop (`work/crops/Kxxx.png`) has two panels. The upper panel shows the target line with a little of the lines
above and below; the target line lies between the two red rules. The lower panel is the same band enlarged. Read only
the target line. Parts of neighbouring lines may show at the top or bottom edge of the lower panel; ignore them.
Interlined words written just above the target line (small, inserted with a caret) belong to it: mark them "ins".
Your batch file says whether the line is in alphabet A or B. Some lines are partly plain English.

## What to write

Write one TSV file, `work/blind/out_batchN.tsv` (N = your batch number), with this header:

`code	pos	kind	signs	n_signs	n_legible	letters	word_guess	note`

One row per word, in order from left to right:
- `kind`: `plain` (ordinary handwriting), `cipher`, `ins-plain`, `ins-cipher` (interlined), `struck` (struck through),
  or `mark` (a dash, brace or other non-word).
- `signs`: for cipher words, one item per sign, space-separated: the best letter, then `/` and any alternative(s) you
  cannot exclude, or `?` for a sign you cannot read at all. Example: `t h o a/u g h t`. For plain words, write the word.
- `n_signs`: how many signs the word has (your best count; write `~5` if unsure); `n_legible`: how many you could
  read.
- `letters`: your best letters joined (use `?` for unread signs).
- `word_guess`: the English word, if the letters make one; leave empty if they do not. Do not force a word: if the
  signs do not support one, leave it empty and say so in `note`. Never fill a word from what the sentence seems to
  need.
- `note`: anything that matters (e.g. "sign 3 could be a blot", "word runs into the margin").

If a whole line is unreadable, write one row with kind `cipher`, signs `?` and a note. Work slowly: zoom by reading
each crop more than once; there is no hurry. When done, give a short report: how many lines, how many words, how many
signs you read, and which crops were poor.
