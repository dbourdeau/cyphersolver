# Solution steps log (for profile.json)

2026-09-22
1. access: DECODE R2276 record page + 3 PNG images fetched with the project cookie (img/, git-ignored). worked.
2. literature search: Tomokiyo cryptiana guise.htm: fr. 20974 no.1 (pp.1-4) "undeciphered"; "In 2021, Norbert Biermann
   found that this can be read with the Nevers-Piles cipher" (private communication, no text published). unsolved.htm
   lists it as Solved (Biermann, private). Web search: no published decipherment. worked (prior identification, no text).
3. key from source: Tomokiyo's partial Nevers-Piles table (NeversPiles.png) + orbais/ values from fr. 4715 f. 2. worked.
4. transcription, pass 1: all three pages, 93 lines, ~4,100 signs, labels per LABELS.md; page 3 read rotated 180.
5. solver run: free homophonic anneal (every label -> one letter) under fr-1530-despatches 5-gram: collapses to e/s
   soup (-2.67/char). failed.
6. solver run: anneal of the unknown labels only, Tomokiyo values fixed: -3.0/char, nothing readable. failed.
7. solver run: polyphonic beam (each label a small candidate set, conflated shapes allowed): words appear
   (presence, chapitre, chanoines, archidiacre brulart, postulation, rome, lansquenetz, parme, elbeuf, cinquante mil
   escus). worked (partial).
8. transcription, pass 2: page 1 re-transcribed by hand at 2x; pages 2 and 3 re-transcribed by two agents at 1.5-3x
   (g/G que split, open/closed box, new signs % W U Y q @). worked.
9. solver run: word-level Viterbi over a 30k-word lexicon (Henri IV letters + 1520s despatches + Rome recueil) with word
   bigrams, one substitution per word; hard-EM re-estimation of label value sets (hardem.py). worked: content
   identified (Reims chapter postulation, grand archidiacre Brulart, abbey of Saint-Remi, Elbeuf ransom, Parma).
10. identification: letter is c. 1589-92 on the Reims archbishopric postulation (Pellevé), not 1556 / Guise.
11. access: Gallica fr. 20974 f4 viewed: letter's blank verso with the 1556 "general d'Albany" key (Tomokiyo no. 2)
    pasted on; source of the 1556/Guise attribution; not the letter's key. ruled out (as key).
12. reading, round 1 (two agents): p. 2 and p. 1 ll. 19-40 + p. 3 with key.json (EM sets). Content and date line found:
    "de Reims ... dix neufiesme de iuin", Mayenne's delays, 18,000 lansquenets + 8,000 reiters, Parma, Elbeuf ransom.
    Many "readings" were key-conforming letter strings, not French. partial.
13. key from source: Tomokiyo's table header row (a..z, nulls) read: strict one-value-per-glyph key (key_strict.json);
    uq = p/g, open box = r, hooked v = m, crossed oo = l, curled d = x; nulls = tailed e, cursive x, dotted x. worked.
14. key-rebuild: value counts estimated from aligned readings (keyest.py); extra codes found by readers: ʒ+Ձ = cardinal,
    d with superscript t = il, ce-ligature = pour, ʒ = du, n = et/x; key_v2 -> EM -> key_v3 -> key_v4. worked.
15. reading, round 2/3 (agents, key_v4, images): p. 3 472/563 signs (83.8%), date "de Reims du dix neufiesme de iuin",
    last word "contribuer"; p. 1 ll. 1-18 in French with gaps. partial. (session interrupted 22-23 Sept; agents resumed)
16. reading, gap rounds (agents, key_v5/v6, images; 2026-09-23): p. 1 90.1%, p. 2 84.5%, p. 3 87.9%; new codes
    ꝺ+superscript o = faire, large hooked b = ie, ẋ = vous, bb = leur, ʒ = le; page-1 dotted M = unread feminine code.
    Whole letter 3426/3925 = 87.3% (reading_draft.txt). partial.
17. reading, final sweep (two agents, full-letter context). (in progress)
