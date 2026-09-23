# Beinecke Mellon MS 136, "Das zweyte Silentium Dei", Glücksbrunn 1798 (DECODE R2873)

Status: read (22 Sept 2026). The book carries its own key (p. 83, "Die Figur unserer geheimen Schrift"). Every
cipher passage in the book, 31 passages on 19 pages between pp. 24 and 76, was transcribed and read with that key:
1,545 cipher signs, 345 words. Two signs are unread and three words are doubtful. The long p. 24 passage was
already read in 2022 (Lasry's transcription, Kopal's decryption, published on Schmeh's blog), and a blog reader
had read most of the short passages, with gaps. This is the first complete reading of the cipher text in the
book.

## What the catalogue entry gets wrong

The catalogue entry is catalogue 168, from DECODE R2873, "Johann Arndt (1555-1621) (Glücksbrunn) to unknown
recipient, 18 Sep 1798". It is wrong on several points:

- It is not a letter and has no recipient. It is a 129-page alchemical manuscript book, *Das zweyte Silentium Dei
  in Königs Salomonis des Weisen paradiessischen Lustgarten*. The book describes a "magische Machine": three
  burning glasses in a row that focus sunlight onto glass dishes and capels for calcining, distilling and
  "tinging".
- Johann Arndt (1555-1621) is the pseudonymous author named on the title page ("durch Johann Arndt ...",
  with a preface signed "Joh. Arndt 1599"). The book is a Rosicrucian-Paracelsian compilation. The 1798 date
  (18-25 Sept.) and Glücksbrunn are the copy's (Yale: "by Gottfried Klaussen(?)").
- The cipher is not "graphic signs" of unknown type. It is a pigpen-type alphabet, "unsere geheime Schrift" or
  "geheime Sprache, so Crucis Rosen[...]" (p. 16), with ligature signs. The key is drawn in the book.
- "Only short parts are encrypted" is right. Pages 24 and 75-76 hold the longer passages. Everything else is single
  words or phrases inside clear German sentences.

## Source

- Beinecke Rare Book and Manuscript Library, Mellon MS 136. Yale Digital Collections OID 10187248
  (https://collections.library.yale.edu/catalog/10187248), manifest /manifests/10187248, 70 images of openings
  (canvas 1436094 front cover ... 1436161 pp. 128-129, 1436163 back cover). Access: public. The site is behind a
  bot check, so curl returns an empty 202. The manifest was read in the browser, and the IIIF image server
  (collections.library.yale.edu/iiif/2/<canvas>/full/full/0/default.jpg) then downloads with curl.
- Canvases with cipher: 1436109 (pp. 24-25), 1436111 (29), 1436112 (31), 1436113 (32), 1436118 (43),
  1436119 (45), 1436120 (47), 1436123 (53), 1436124 (54-55), 1436125 (56), 1436127 (60-61), 1436128 (62),
  1436132 (70), 1436134 (75), 1436135 (76). Key: 1436138 (p. 83). Images are in `img/` (git-ignored).
- DECODE R2873: 129 pp., Non-decrypted, images behind login. Not opened here; the Yale images are the same book.

## Prior work (contamination)

Found by a web search on 22 Sept 2026, after the cipher pages had been located and the key had been read
from p. 83, but before any passage was transcribed.

- Klaus Schmeh, "Ein verschlüsseltes Buch aus dem Jahr 1798", Cipherbrain (scienceblogs.de), 4 March 2022,
  https://scienceblogs.de/klausis-krypto-kolumne/2022/03/04/ein-verschluesseltes-buch-aus-dem-jahr-1798/ .
  The book is no. 00114 on his Encrypted Book List. The tip came from Nils Kopal. Kopal's video decrypts the p. 24
  page from a transcription by George Lasry and also shows a CrypTool attack without the key. The post prints
  the p. 24 plaintext and notes that the key is on p. 83.
- Comment 4 on that post (Christof Rieber, 10 March 2022) lists readings of the short passages on pp. 25, 29, 31,
  32, 43, 45, 53, 54, 55, 60, 61, 62, 70, 75 and 76. It has gaps ("[?]", "(..)") and several misreadings. It
  gives "rotiere" where the text has *lutire* (p. 60), "noch" for the cipher *No.* (pp. 25, 60), "nachtnach" for
  *nach und nach*, and "raschen" for the p. 75 *sta=cken*. It also misses the passages on pp. 47 (second line),
  53 (third), 56 and 76 (*seine centralische Strahlen*).
- Ashrowan 2016 (Edinburgh PhD appendices, era.ed.ac.uk 1842/31017) discusses the book (alchemical catoptrics);
  not read here.

What this folder adds: a sign-level transcription of every passage in the book, read with the key and checked
word by word against the images; the corrections above; five passages not read before; and corrections to the
published p. 24 text ("Stöpsel", not "Stopfel"; "Löchlein"; "zu lit. b muss lutirt werden"; "arbeitet").

## The key (p. 83)

The page has a circle with two diagonals and a tic-tac-toe grid, so nine square cells and four triangles. Each
cell holds two letters, the second marked with a dot. The sign is the shape of the cell's walls:

| sign | ┘ | ⊔ | └ | ⊐ | □ | ⊏ | ┐ | ⊓ | ┌ | V | > | < | Λ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain | a | c | e | g | i | l | n | p | r | t | v | | z |
| dotted | b | d | f | h | (k) | m | o | q | s | u | w | y | (x) |

To its right is a table of ligature signs: ae, oe, ui (used for ü), ch, ck, sch, ss, st, th, und, "dergl.",
ll, lich, n, nn, o, and a "tz" sign. A later hand added v, w, y, x and z for the triangle cells in pencil.
A double stroke over a sign doubles it. The key reads every passage without change; no other key was needed.

## Reading

The reading is in `reading.txt` (German, with the clear context), the sign-level transcription in
`transcription.txt`, and `decode.py` maps the transcription back to signs and counts it. The cipher words are
the working parts of the recipes: vessels and materials ("gläserne Schaalen", "Capellen", "Salpeter", "nitrum",
"Tiegel"), procedures ("nach und nach", "einkoche", "lutire"), and the p. 24 key to the figures of the machine
(what the letters A-S on the plates stand for). On p. 70 the metals are melted each in its own planet's hour,
and pp. 75-76 give the geometry of the three burning glasses (M. O. Q. inches, largest glass toward the sun).

Measured (`python decode.py`): 1,545 cipher signs in 31 passages, 345 words, 2 signs unread.

## The recipes in English (22 Sept 2026)

The clear German around every cipher passage was transcribed and translated, recipe by recipe, in
`clear/pp24-49.md` and `clear/pp50-77.md` (German, then English, page by page; cipher words in ‹ › and bold).
It covers pp. 24-32, 43-48, 50-56, 59-63, 69-71 and 73-77. Pages with no cipher and no step of these recipes
were skipped (33-42, 49, 57-58, 64-68, 72). Thirteen recipes are on the site page, section 04: spirit of
mercury; the glass stone (silver, gold, medicine); ores in four operations; aurum potabile; feather alum; oil
of talc; Attractio Astri Mundi and the seed water; the vitrified stone; flowers per descensum; the flower
"cure"; concentration of wine; the seven-metal electrum and mirror; the rules for setting the machine. The clear
text also shows a slip in the cipher: p. 60 enciphers "lutire das Glas No. S.", but the luted glass is P
(p. 24 legend, and "No. P." in clear on p. 61). Several Kurrent words in the clear text are marked (?).

## Remaining gaps

- p. 24, No. M.: "ist ein gläserner {?}", one sign, probably a pictographic or alchemical vessel sign, not in the
  key. Blocker: no-key-material. The key has no such sign, and the plate on p. 21 shows the vessel but gives
  no name.
- p. 54, "ein wenig dig..." (probably *digerirende* Hitze). The word runs into the gutter after "dig". Blocker:
  illegible. Tight binding, and the Yale image is the only one.

Doubtful readings (C grade): p. 24 "steig der Spiritus ☿ii" (steig/steigen); p. 24 "No. K. ist d gläserne"
(one sign, perhaps an abbreviated *die*); p. 53 "nach K." (a clear-script K. after the cipher, sense unclear);
p. 75 "einige sta=cken zu enden" (read letter by letter, sense unclear; Rieber guessed "raschen").
"Renien" (p. 24, No. S.) reads cleanly but is an obscure word.

## Escalation

- [x] siblings: the book is a single manuscript. All 129 pages were checked for further cipher (contact sheets of all
  70 openings, full-resolution passes on the pages with signs). No cipher before p. 24 or after p. 76 except the
  key on p. 83; pp. 84-87 give a cabbalistic letter-number table (clear).
- [x] clear-pages: the book's figures (pp. 21-23) label the apparatus with the same letters as the p. 24 key text.
- [x] known-keys: the book's own key, p. 83, reads everything.
- [x] print: Schmeh 2022 blog and Kopal video (p. 24 plaintext), Rieber's comment (short passages); both used as
  a check after the independent reading, and the differences are recorded above.
- [n/a] key-rebuild: the key is complete for every letter used. The two gaps are a sign outside the key and a
  word hidden in the gutter.
- [x] retry: the doubtful words were re-read at 2x crops of the full-resolution image (p. 75 *sta=cken*, p. 54
  gutter word). No change.
