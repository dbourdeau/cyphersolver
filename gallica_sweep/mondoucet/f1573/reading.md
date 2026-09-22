# Mondoucet 1573, BnF fr. 16127 (catalogue entry 2): which passages lack a reading, and the one that did

Worked 18 Sept 2026. Images: full-resolution IIIF canvases in `../../full16127/` (git-ignored; `../../refetch.py N…`).
Canvas → folio on these leaves: c262 = f. 126r, c264 = f. 127r, c280 = f. 135r, c288 = f. 139r, c292 = f. 141r.

## 1. What the leaves are (the inventory was partly wrong)

| letter | cipher | Court decipherment | verdict |
|---|---|---|---|
| Antwerp, **4 Jan 1573** | f. 126v (4 lines after the clear text), f. 127r (31 lines), f. 127v (4 lines), then sign-off | **none**. ff. 124–125 are the decipherments of the 5 Dec 1572 letters, f. 128 is the King's letter of 1 May 1573. The only help is four interlinear glosses in the Court hand on f. 127r | **the unread passage**, read here in part (§3) |
| Amsterdam, **9 Sept 1573** (not "5 Sept") | block 1 f. 135r (12 lines), block 2 f. 135v (16) + f. 136r (31) + f. 136v (30) + f. 137r (29), tail f. 137v (c. 21 lines) | ff. 139r–141r ("deschiffré"), 17 + 77 + 25 + c. 17 lines; f. 138v is the address leaf | **complete and verbatim**: nothing to solve |

The "ff. 138–140" of the catalogue are the decipherment and address leaf of 9 Sept, not cipher; the cipher is on ff. 135–137.
The "margin readings visibly shortened" of the inventory belong to the later 1573–74 letters (f. 161 etc.), not to these.

## 2. Verification, passage by passage (9 Sept)

Hand transcription of the cipher at glyph level (`ct/f135r.txt`, `ct/f135v.txt`, `ct/f136r.txt`, `ct/f136v.txt`,
`ct/f137r.txt`; 4,735 glyphs) and typing of the decipherment (`pt/f139r_a.txt`, `pt/f139r_b.txt`, `pt/f140v.txt`).
Hard-EM alignment (`align.py`: glyph→letter, glyph→null, skipped letter, glyph→2–8 letters for word signs), seeded
with the 1572 key.

* Length: block 1 441 glyphs / 483 letters (0.91); f. 137r 1,121 / 1,206 (0.93); all of block 2 (ff. 135v–137r)
  4,294 / 4,703 (0.91, the difference being word signs such as *dict, faict, pour, quil, monsieur*). An abridged
  reading would push the ratio well above 1.
* Alignment: block 1 aligns end to end ("mais iay entendu dun cappitaine … la necessite y est grande"). Block 2 aligns
  line for line over 108 cipher lines with about 4,000 glyph-letter pairs, no run of unaligned cipher longer than a
  word, and ends where f. 140v breaks off ("…nouvellement on avoit prise le chasteau de"). Per-line residues are in
  `blk2_align.txt`.
* Tail: f. 137v (c. 21 cipher lines) against f. 141r (c. 17 lines, ending "Du ix sept. 1573"). Compared by length
  only, not transcribed; proportion consistent with the verbatim blocks.

So every cipher passage of 9 Sept has a full, literal Court reading. The letter itself (Alba on Alkmaar, "elle ne se
peult assaillir que par ung seul endroict"; his recall "le roy catholique… luy mandoit que maintenant il avoit assez
longuement travaillé"; Medinaceli; the King of Poland's passage and Danzig; a letter from France predicting "choses
plus remarcables et plus grandes que la journée saint Barthélemy") is readable in clear on ff. 139–141.

## 3. 4 January 1573, Antwerp: the cipher without a reading

Clear context (f. 126r–v): Orange "estoit tousjours à Delft où il faict tout ce qui luy est possible pour assembler
gens et argent"; the Colonel Mondragon; "le Comte Ludovicq ne perd pas temps à faire pratiques et menées par les
Comtes des Allemans(?), et m'a entendu qu'il se donnoit fort secrètement …", then cipher.

**Key.** The 9 Sept alignment gives a 1573 key of c. 55 signs (`key1573.json`).
It is the 1572 system (same homophones: d/n/c = e, v = t, O = s, G = m, k = n, g/h/H = a, # = p, x = q, l = o …).

**Decoder.** Beam search, P(letter | glyph) from the aligned counts × a 24-letter period-French 5-gram
(`decode1573.py`, `fr5.npy` built by `build_lm.py`; `SM=0.3 NP=3.5`, width 600).

**Control (held out).** Key re-estimated from block 2 only (`key_blk2only.json`), block 1 decoded blind and scored
against the Court's reading (`score_ctl.py`): **77 % of letters correct** (303/391); 71 % with the default null
penalty (the penalty was chosen on this same control, so 77 % is slightly optimistic). A variant with a word-space LM and the scribe's gaps as cues scored lower (61–64 %) and was dropped, although
66 % of the scribe's gaps do fall at word boundaries (base rate 22 %).

**Independent check.** Between f. 127r ll. 25–26 the Court decipherer wrote "hambourg" above the cipher. The key,
which never saw this page, decodes l. 26 as "…ambourg eron croit debuoir servir pareil…".

**Reading** (`ct/f126v_127.txt` → `dec_4jan.txt`, verbatim machine output; below, the stretches that read, word-divided
by me; [ ] = conjecture, … = unread):

    126v  … des costez de Coulongne [et] Francfort … se puisse sçavoir de quelle part … argent …
    127r 1–3   … entretenir leurs … dans leurs soldats particuliers …
         4–5   … soient levées de gens … depuis naguières … seize ou dix-huit …
         6–8   … [enseignes] tenant des … marchés … plusieurs … ce soit … le cours des princes … et ce qui se passera …
         9–11  … [à vostre] Majesté … en fera … capitaine Alexandr[e] … qui m'a semblé … prise …
        12     … soubz ombre de chercher parti … couvrira …
        13–15  … personne … charge d'advertir [vostre] Majesté … deux mois …
        16–17  … quelque chose de … désavantaige [et] desservice qu'il fera …
        18–20  … pris ceste ferme … avec … argent … entretenement …
        21–23  … semblable prendroit de … [davantaige] … [ne] oublier de
        24–25  [vous] advertir … la prise … l'Angleterre avoit … tenir cent [mil] …
        26     [H]ambourg, [où] on croit debvoir servir pareil …
        27–31  … descouvert … avoit quelque temps que certain [evesque] de ce grand … de ce grand …
    127v  … quelque … [vostre] Majesté … advertir de ce … [il] fauldra …

About two-thirds of the 1,468 glyphs fall in stretches that read. Subject: Louis of Nassau's levies for Orange in the
Rhineland (Cologne, Frankfurt), their money and pay, a capture, and English money for the rebels by way of Hamburg,
in the winter of the siege of Haarlem (invested Dec 1572, fell July 1573).

Other interlinear glosses on f. 127r not yet matched: over l. 19 "?nuactynch" (read unsure; Enkhuizen?), over
l. 22 "Lan…", over l. 27–28 "?couillart". "[dauantaige] [dru]" in l. 23 are words written in clear inside the cipher.

**Limit.** Transcription, as in 1572: the 4 Jan hand is smaller and the `a`/alpha class stands for r, l, y and i.
Re-reading the doubtful glyphs on the strips (`s263/`, `s264/`, `s265/`, git-ignored, rebuilt by `strips.py`)
is the next step, not a new model.

## Files

`ct/` transcriptions · `pt/` decipherment · `align.py` · `align_out.txt`, `blk2_align.txt` · `key1573.json`,
`key_blk2only.json` · `decode1573.py`, `decode_sp.py` (dropped variant) · `build_lm.py`, `build_lm_sp.py` ·
`score_ctl.py` · `dec_4jan.txt` · helpers `q.py`, `band.py`, `lines.py`, `strips.py`, `stack.py`.

## 4. Re-transcription pass, 21 Sept 2026

All 39 lines of 4 Jan re-checked against the strips (`ct/f126v_127_v2.txt`, 20 glyph edits marked `# v2:`;
decoded as `dec_4jan_v2.txt`, same settings). Net gain small: l. 03 "particuliers", l. 30 "avec … que le produit",
l. 23 "…oublier de"; l. 05 lost "seize". Two shapes do exist inside the `a` class (round closed a vs. open alpha with
crossing tail) but the 9 Sept key does not separate them, so they stay merged. Verdict: the passage stays **read in
part**. It will not move further without a key that splits a/alpha, i.e. re-transcribing 9 Sept block 2 with the
split and re-aligning, or finding a decipherment elsewhere.

**a/α split (same day).** Open alpha marked `α` on f135r, f137r (`ct/*_split.txt`, `ct/blk2_split.txt`) and 4 Jan
(`ct/f126v_127_v3.txt`, 52 α). Re-alignment (`key1573_split.json`): α = r (42) and nothing else; round a = y/l/i on
the split pages, never r. Held-out control 77.5 % → 78.3 %. 4 Jan v3 (`dec_4jan_v3.txt`) gains "avant dire" (l. 14),
"il voudroit qui" (l. 29), "donneur" (l. 13). Still read in part. What remains: split α on f135v–f136v too (cleans the
round-a values), then the l/d/b foot-curl confusion.

**Full split + constrained pass.** α marked on all five 9 Sept pages (`key1573_split2.json`: round a = l65 y47 i26,
α = r123). Held-out control 79.0 % (NP=3.5), 73.7 % (NP=1.0). `tryalt.py` tested 11 image-ambiguous glyph
alternatives on 4 Jan; 4 kept on decoder score (`ct/f126v_127_v4.txt`, `dec_4jan_v5.txt`), none settled by image.
Best composite reading ≈ 55–60 % of letters (≈ 65 % with conjectures); ll. 03–04, 13, 21–22, 27, 31 stay unread.
**Closed as read in part**: ciphertext-only decoding has plateaued at ~79 % letter accuracy on the control, so a
full reading of 4 Jan needs a contemporary decipherment (not in fr. 16127) or a copy of the letter elsewhere.

## 5. Solved: the clear text is in print (21 Sept 2026)

The whole 4 Jan cipher passage is printed in clear by L. Didier, *Lettres et négociations de Claude de Mondoucet*,
t. 1 (Paris/Reims 1891; archive.org identifier `lettresetngocia01mondgoog` = vol. 1, which covers the Reims register Sept 1572 – Sept 1573; earlier noted here as t. 2 in error), pp. 141–142, from Mondoucet's own letter register (Bibliothèque de Reims MS), dated "D'Anvers,
ce IIIIe jour de janvier 1573". OCR in `pt/f126v_127_didier.txt` (archive.org `lettresetngocia01mondgoog`).
It confirms the decode word for word where it read ("seize ou dix huict cappitaines", "soubz umbre de chercher party",
"désavantaige de vostre service", "ceste forme de wartgueld avec le duc de Brunsvick", "cent mil escuz à Hambourg, que
l'on croyt debvoir servir pour pareil effect") and fills the gaps: the German captain sent to spy, Alba's wartgeld with
Brunswick and Saxe-Lauenburg, and an Irish bishop kept at Antwerp by Alba for the Ireland practice (line 31's
"l'Irlande" and the gloss "?couillart" region). Glosses: "Lan…" = Lauembourg. The passage is **read** (from print);
this project's contribution is the independent ciphertext-only recovery (~79 % control) and the 1573 key with α = r.
Contamination note: the edition existed before any of this work but was not consulted until after passes 1–3.
