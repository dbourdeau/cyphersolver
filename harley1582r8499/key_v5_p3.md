# Key v5 changes from p3.01-p3.31 (full-resolution crops of img/p3.jpg, 6 x 1200 px pieces per line)

Reading in final_v5_p3.txt. Measured: 685 non-null signs, 532 firm (77.7%), 78 tentative, 75 unread; 89.1% incl. tentative.

| label | v4 | v5 | evidence |
|---|---|---|---|
| `.B` (dot before B) | fi / before (tentative) | **not** (word code) | "could **not** find in this heart" p3.03 (clear text p3.15 "came not fynde in his herte"), "he will **not** entre in service to the French king" p3.01, "did **not** mistrust my wordes" p3.07-08, "can **not** forget this offence" p3.16, "can **not** lyve in England" p3.21, "he entended **not** to return" p3.21-22, "entendid **not** to open" p3.27. Plain B = of stays |
| `U_HOOK` (ꝑ-like hooked sign) | u/v | **r** | "wo**r**des" p3.08, "cha**r**ge" p3.18, "suffe**r**" p3.23, "depa**r**t" p3.06, "pe**r**ceved" p3.12, "decla**r**id" p3.31, "ent**r**e" p3.01 |
| `NULL_LOOP` when drawn crossed (ꝸ-like, relabelled F_LOOPCROSS) | null | **f** (key f "ꝸ-crossed") | "su**ff**er" p3.23 (with BBAR), "o**ff**ence" p3.16, "e**ff**ect" p3.31, "**f**orget" p3.19. The plain looped ꝺ stays null, but reads **i** in "f-i-nd" p3.03, "k-i-nd" p3.10, "l-i-ve" p3.30 (tentative) |
| `b` / `d+` drawn as ƀ (t with loop) | l / i | **f (BBAR)** | "fawte" p3.28, "suffer" p3.23, "offence" p3.16 |
| `<` (α-cross) | g | **f** where dotted: "**f**orget" p3.16, "e**ff**ect" p3.31 | as v5_p2 (`<.` = f) |
| `E_SLASH` (crossed ꝗ) | unread | **g**, tentative | "for**g**et" p3.19, "**g**entelmen" p3.29 |
| `Y_LATIN` / underlined ƞ | us / unread | **for** (key ƞ̲) | "Carew **for** Carew" p3.14, "**for**get" p3.19 |
| `9` | null | **m** where hooked: "advertse**m**entes" p3.05, "com-**m**andment" p3.25, "**m**ay" p3.30; `9 .` (dotted) p3.05, p3.19, p3.25, p3.29 unread/null |
| `··` (two dots, DOTS2) | null | **y** (key y "··") | "ma**y**" p3.24 |
| `x=` / `-8` | e / c | unchanged; `x=` stands for a in "gentleman" p3.23 (tentative), `-8` for s in "case" p3.18 (tentative) |
| `H` | y/u | y in "gyveth" p3.04, "lyve" p3.21; v in "receve" p3.02, "serve" p3.25 |
| `pt` | u/h | **h** in "**h**ome" p3.30 (as v5_p1a); u in "return" p3.15; v in "give" p3.23 |
| `Q_CIRC` (q in an oval) p3.31 | it | **is** (key ⓖ-type circled sign), tentative |
| `n .` p3.19 after "it" | unread | Carew, tentative |
| caret `A` under p3.31 | – | insertion mark for an omitted letter: "dec^arid" = declarid |

Checked and unchanged: `F_OVERBAR` = a ("charges", "commandment"), `XUND` = s ("service", "advertsmentes", "against"), `S_DOTBELOW` = would/will (p3.01, p3.19, p3.22, p3.25), `-4` = that, `C:` = that they, `Ie` = I (tentative), `E_DOTBEFORE` = Monsieur de, `CIRC_RING` (small circle sitting on a large one) read as your highness (tentative; it is not the concentric ⊚ of the Prince of Spain).

Still open on p3: `.p` (p3.01, p3.14, p3.20), `Q_TAIL` p3.04, `.9`, `h .` (p3.05, p3.20, p3.21, p3.25, p3.29), `.E` (p3.09, p3.17, p3.23), the C-family run p3.09 and p3.17 (`C_CEDILLA`, `C_DOT`, `C_DOTBEFORE`, `L_DOTS`), `.Z` (p3.02, p3.12, p3.22, p3.28), `TALL_F_LOOP` p3.17, `CIRC_BIG` (Monsieur de ...), `E_CROSS` p3.27, `.k` p3.16/p3.26, `F_PLAIN` p3.29, the p3.26 run `zo v or b H x=`, Y_ETA where "us" fails (p3.02, p3.05, p3.28).
