# eaglepass1917 - reading (Spanish), Mexican embassy to the consul at Eagle Pass, 17 April 1917

Marks: a plain word comes out of `key.tsv` on `transcription.txt` letter for letter, uncorrected. {word} is a word with one
letter (two in necesito and presidente) that the key does not give and that is read from the sense: a hole under the README
read bar. Word division, accents and punctuation are ours; the cipher has none. The telegram is in telegraphic style
(articles and prepositions left out), as written.

## Reading

Para {presentar} los a comité censura nombrado {por} {presidente} Wilson {necesito} mándeme mayor brevedad posible
nombres {periodistas} y agentes información {que} propalan {falsas} {noticias} y agitan opinión principalmente con
noticias complots {alemanes}. Debemos poder {comprobarlo} caso {necesario}.

## Reading with the emended letters marked

The same text, with each letter that the key does not give in [ ] (the extra cipher letter N in "falsas" is left out,
next to the bracket). This is the form `replay.py` compares with the key output.

<!-- replay -->
Para presen[t]ar los a comité censura nombrado p[o]r pre[s]iden[t]e Wilson n[e]c[e]sito mándeme mayor brevedad posible
nombres periodis[t]as y agentes información q[u]e propalan [f]alsas notic[i]as y agitan opinión principalmente con
noticias complots al[e]manes. Debemos poder co[m]probarlo caso nec[e]sario.
<!-- /replay -->

## Holes: the eleven words that need a letter from the sense (cipher positions 1-based, counted in `transcription.txt`)

| Position | Word | Key gives | Cipher letter typed | Letter needed (cipher) | On the photograph |
|---|---|---|---|---|---|
| 11 | presentar | presenmar | F | T | F clear |
| 40 | por | prr | Y | V | last letter of XQVEY heavily inked, apparently typed over; partly a reading doubt |
| 45, 50 | presidente | precidenee | S; P | C; T | both clear (P for T: an e/t exchange) |
| 59, 61 | necesito | ntctsito | T; T | P; P | both clear (e/t exchanges) |
| 108 | periodistas | periodiseas | P | T | P (or F), not T (e/t exchange) |
| 131 | que | qoe | V | B | V clear; a stroke follows (DV/PEYV) |
| 142 | falsas | fwalsas | N (extra) | none | an extra letter in the group MNX |
| 153 | noticias | noticsas | C | Z | C clear |
| 205 | alemanes | altmanes | T | P | T clear (e/t exchange) |
| 225 | comprobarlo | cocprobarlo | S | F | S clear |
| 241 | necesario | necmsario | F | P | F in all three transcriptions; F and P are hard to tell apart on this halftone |

## Words clean only under a doubtful reading

- información (position 121): read M, which gives f; the photograph allows N, which gives w ("inwormación"). Two of the three
  transcriptions prefer N. If N, this word is a hole too.
- mándeme mayor (position 73): read F (two transcriptions, and the reviewer after a closer look); P would give "mándemeeayor".
- que (position 130): cipher D occurs only here; its value q rests on the reciprocal pair with cipher Q = d.

## Count (37 words, 246 letters)

- With the readings in `transcription.txt`: 26 of 37 words clean (70.3%); 159 of 246 letters in clean words (64.6%).
  11 words are holes, all completed from the sense.
- If position 121 is N: 25 of 37 words (67.6%), 148 of 246 letters (60.2%).
- If position 241 were P (as first proposed, against the photographs): 27 of 37 words (73.0%), 168 of 246 letters (68.3%).
- Every word is identified and the sentences run from end to end; under the 95% word bar the telegram is read in part.
