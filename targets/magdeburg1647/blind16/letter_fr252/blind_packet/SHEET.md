# SHEET: label names for this cipher (names only, no values)

You are transcribing a 17th-century cipher written with ordinary-looking lower-case letters plus some drawn symbols.
Write what is on the page, shape by shape. The labels below are the names the key itself uses for its signs. They are
only names: nothing here tells you what any sign means, and you must not try to work that out.

## 1. Letter signs (24 labels)

    a b c d e f g h i k l m n o p q r s t u w x y z

There is no j and no v label. If you see a shape that looks like j or v, write it as `{?j}` or `{?v}`.

How to tell the look-alikes apart (shape notes from earlier readers of this hand; shape only):

- z: written like a "2", often with a long tail sweeping down to the right under the following letters.
- i: a short "1"-like minim, usually undotted. r: a "v"-like stroke with a right-hand ear. Separate them by the ear.
- g and q: both have a closed bowl. q has a short straight descender; g has a longer descender that curves or hooks left.
- c and e: c is a plain arc with a small head; e is the same arc with a tick or small eye at mid-height.
- t and l: t is short with a crossbar; l is tall and plain, often with a foot.
- f and final n: f has a descender and a crossbar; final n has two minims and a long horizontal exit stroke.
- h: tall ascender plus arch, ascender often looped. k: h-shape with a kink, or a capital K.
- d: bowl plus tall ascender, sometimes written as a separate c-shape plus l-shape.
- w is always a capital W. p has a plain descender. y is v-shaped with a tail and no dots.
- Two minims with two dots, the second descending: write `i` then `{?j}`, not y.

## 2. Symbols (name signs)

Drawn symbols (triangle, square, square with a cross or bars, star, asterisk, spiral, circle with a cross, double
triangles, crossed strokes, planet-like marks and so on) are name signs. Write each as `{S:short-shape-name}` using
plain shape words you choose and then keep the same name for the same shape every time, e.g. `{S:triangle}`,
`{S:square-x}`, `{S:star6}`, `{S:spiral}`, `{S:circle-cross}`. List every symbol name you used at the end of BLIND.tsv
in a comment line `# symbols: ...` with one short description each.

## 3. Marks and doubts

- A word break as you see it on the page: a single space between tokens.
- A sign you cannot read: `?`. A sign you can read only as one of two labels: `[g|q]` (any two labels).
- Blot, hole or strike-through over cipher: `{blot}` or `{struck:abc}` with what you can see.
- Underlining, a bar over a word, dots or a tittle: note as `{mark:underline}` etc. after the token.
- Clear (not cipher) words inside or around the cipher: do not transcribe them in the token column; they go only in the
  `clear_word_before` column as described in PROMPT.txt.
