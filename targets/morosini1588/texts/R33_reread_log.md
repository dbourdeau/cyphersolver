# Re-reading log, R33 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R33_decryption.txt` (character model on DECODE's D1697 under Meister
no. 40): the subject clear (the clergy and the Council of Trent) but garbled words in most lines ("terra tolera",
"ognuno di scendendo", "eletore sentio niza in premi"). Clean-sentence share 0.511.

## 1. Is there a text already?

- DECODE images: 8 cipher pages (189r–192v) and 11 "cleartext" images (contact sheet checked; two read in part):
  clear despatches and avvisi of the same weeks (Paris, Savoy, Spanish armada), ff. 188–197. Not decipherments. No
  interlinear glosses on the cipher pages.
- Print: Tempesti, *Vita di Sisto V* (1754) II, book VII §§ XXXI–XXXV (scratchpad OCR ll. 1339–1420) paraphrases the
  letter point by point, including the four reservations and the legate's four arguments. Used for sense only. Rome's
  decipherments (Francia 27) not imaged.

## 2. Word decode and hand re-parse

From `R33_worddecode.txt`; about one word in eight re-parsed by hand (`R33_corrections.tsv`, 94 rows). Causes:
- Decoder's wrong splits on correct figures: "ci uoria" (decoder "uiuo ria"), "dicendo", "non la uogliono",
  "le loro esentioni" (decoder "eletore sentio niza"), "s'ofersero", "aquetarli", "pontiglio d'honore", "onde", "ma anco
  santi", "era honesto", "come madre pia", "guardasigilo", "io risposi", "spontare", "andarò".
- The -mente abbreviation m + 8, twelve times (ultimam., liberam., grandem., ostinatam., grauem., priuatam.,
  ligitimam., specialm., ragionam[ento], distintam., risolutam., compitam.) and "bo. mem.".
- Codes the decoder missed or misread: 135 (dot on the 3), 213 (dot on the 1, twice), 151, 226 (once undotted), 141
  (undotted in "quelli del clero"); "2 1 2^. 6" in "come madre" is a spurious dot.
- About 30 single-figure slips taken from context (tsv "figures+context").

## 3. Image checks (crops, scratchpad only)

- 189r l. 12 and 190r l. 12 (the transcriber's "? ? ?"): holes eaten through the paper by the ink; the figures are lost.
- 192r l. 24 – 192v l. 1 ("a qualche min…"): 192r ends "2 1 2 9 0 2 1 5 0 5 6 2 0 1 7 0 1" as transcribed; 192v l. 1
  has faint figures in the left margin not transcribed; the word stays unread.

## Result

Before 0.511 → after 0.729 clean-sentence share (on the "## Reading" body). By hand: 13 unread stretches ([…]) and
about 15 partly carried words in about 1,540 words; every sentence of the argument carries. Grade B (about 30
figure-context corrections; several holes are physical).

## Still open, and why

- 189r l. 1 (opening), l. 7, l. 8; 190r l. 1 ("[?dui anni]"); 192v ll. 4–5: no word parse of the transcribed figures
  (no outside blocker; a further image pass could close some).
- 189r l. 12, 189v l. 12, 190r l. 12, 190v l. 21, 192v l. 8: holes in the paper (image): blocker = damage.
- 192r l. 24 – 192v l. 1: one word ("min…") not read; 192v margin figures faint.
- 192v l. 9: the closing figures (with 221 lettere) not read.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for, the figures parsed (`r2p_parseall.py`). As on R32, the ink has
spread and the verso shows through over the lines; there are small holes in the paper (189v l. 16, 191r l. 5) and
blots (190v l. 10). No cancellation stroke could be told from the show-through.
Filled:
- 192r l. 2 "intendea": "171 31 35 01 26 35 2" (31 = nt): the period form as written (was "intende[u]a").
Left, with blockers (191r l. 5 "qualsiuog[l]ia": the l would stand where the paper is holed; 190v l. 10 "dispia[c]eria":
a blot over the place of the c; both illegible):
- 189r l. 1 "[…] N S": "9 7 5 2 4 7" (best parse "oicst"). Blocker: no-key-material.
- 189r l. 2 "S di dar[mi] intorno ala": "2 6 2 1 0 0 1 2 0 1" (best parse "darran"). Blocker: no-key-material.
- 189r l. 7 "sia riceuto […] liberam[ente] come": "7 1 0 1 5 1 5 0 1 7 4 2 3 5 0 0 2 1 2 0 8" (best parse "inrtliberam"). Blocker: no-key-material.
- 189r l. 8 "di christiani […] parue ala": "2 2 6". Blocker: too-short.
- 189r l. 12 "concilio et […] et [?d]": "1 7 1". Blocker: too-short.
- 189r l. 12 "[…] et [?d] esiderio che": "(none)". Blocker: nothing written there; no-key-material.
- 189v l. 4 "di non uole[r] [?per] dere": "3 9 1 5 0 3 5 2 6 4" (best parse "uoleaper"). Blocker: no-key-material.
- 189v l. 4 "di esere [?esenti] da i": "1 5 3 4 5 3 5 0 2 1 5 1 7 1" (best parse "esulati"). Blocker: no-key-material.
- 189v l. 6 "che uenti [et] per uedere": "(none)". Blocker: nothing written there; no-key-material.
- 189v l. 7-8 "di dimandare unita[mente] con i": "1 7 3 0 1 1 7 | 1 5 2 1 2 8" (best parse "unita"). Blocker: no-key-material.
- 189v l. 11-12 "i suoi canon[i]ci et che": "2 5 | 2 1 0 1 9 1 0 2 5 1 7 1" (best parse "acnonci"). Blocker: no-key-material.
- 189v l. 12 "et che [?…] inouando [questo]": "(none)". Blocker: nothing written there; no-key-material.
- 189v l. 12 "[?…] inouando [questo] disordine non": "1 7 1". Blocker: too-short.
- 189v l. 15-16 "benefici che [?posedono] altri per": "7 0 9 1 4 5 3 5 2 6 9 8 | 8 1 9 8" (best parse "poseatocon"). Blocker: no-key-material.
- 189v l. 16 "pretensa libertà […] dela chiesa": "2 0 5 2" (best parse "mc"). Blocker: no-key-material.
- 189v l. 18 "questa superiorità [?fra] tute [l']": "2 3 2 7 2" (best parse "frlta"). Blocker: no-key-material.
- 189v l. 18 "[?fra] tute [l'] altre nationi": "5". Blocker: too-short.
- 189v l. 19-20 "nationi christiane [?mantenere] ostinatam[ente] Onde": "2 0 2 1 3 1 3 5 8 1 1 7 0 0 5 9 4 7 1 7 0 1 2 | 5 1 2 1 2 0 8" (best parse "manteinlostinatan"). Blocker: no-key-material.
- 189v l. 24 "ringratiauano di uole[r] publicare il": "3 9 1 5 0 3 5 2" (best parse "uolea"). Blocker: no-key-material.
- 190r l. 1 "almeno di [?dui anni] per dichiarare": "2 6 3 7 1 9 2 2 5 2 0 1 7" (best parse "duroacani"). Blocker: no-key-material.
- 190r l. 12 "oficio più […] che io": "6 9 1 2 1 5 2 5" (best parse "toaec"). Blocker: no-key-material.
- 190r l. 14 "quei che in[st]igati dal demonio": "1 7 1 0 1 4 1 7 7 4 0 2 1 5 1 1 7 1" (best parse "inhiigati"). Blocker: no-key-material.
- 190r l. 19 "generale ligitimam[ente] con[gregato] et finito": "5 0 1 7 4 0 1 7 1 5 1 7 2 0 2 1 2 0 8 1 9 1 9 3 2 1 9" (best parse "ligitimanoconuao"). Blocker: no-key-material.
- 190r l. 20 "ecetioni che [l] oro non": "(none)". Blocker: nothing written there; no-key-material.
- 190r l. 24 "Lorena di bo[na] mem[oria] et": "4 2 9 1 8 2 0 3 5 2 0 8" (best parse "bomem"). Blocker: no-key-material.
- 190v l. 1 "ambasciatori di [?S. M.tà] che tuti": "(none)". Blocker: nothing written there; no-key-material.
- 190v l. 2 "haueuano sotoscrito [?et] aprouato che": "5 6". Blocker: no-key-material.
- 190v l. 10 "et che dispia[c]eria asai a": "2 6 1 7 4 4 1 7 2 3 5 0 0 1 7 2" (best parse "dissiaueria"). Blocker: illegible (blot).
- 190v l. 10 "N S pregando[la] a considerar": "3 3 3 5 4 0 2 1 0 1 2 6 1 9 1 1 1" (best parse "pregandorr"). Blocker: no-key-material.
- 190v l. 11-12 "titolo di christianis[si]mo non [d]": "1 2 | 1 4 0 0 1 7 4 7 1 7 2 1 0 1 1 7 4 5 2 2 0 9" (best parse "zhristianiscano"). Blocker: no-key-material.
- 190v l. 12 "christianis[si]mo non [d] ourebe hauere": "(none)". Blocker: nothing written there; no-key-material.
- 190v l. 14-15 "a lei conu[e]niua di hauere": "7 6 3 7 3 | 0 1 1 7 3 7 2 1 2" (best parse "ituuniua"). Blocker: no-key-material.
- 190v l. 19 "che il [?concilio] [fose] publicato": "1 9 9 1 4 5 1 5 3" (best parse "roose"). Blocker: no-key-material.
- 190v l. 20 "ma che […] considerasi che": "9". Blocker: too-short.
- 191r l. 5 "pii di qualsiuog[l]ia altro re": "9 0 2 1 5 0 4 1 7 1 3 9 1 4 0 1 7 2" (best parse "qualsiuogia"). Blocker: illegible (hole in the paper).
- 191r l. 11 "contra quello [che] S M": "6". Blocker: too-short.
- 191r l. 12 "nel suo rag[i]onam[ento] fato ali": "1 2 1 4 0 9 1 2 1 2 0 8" (best parse "zrsnoam"). Blocker: no-key-material.
- 191r l. 14 "suo regno altr[a] religione che": "2 2 7 0 0" (best parse "altr"). Blocker: no-key-material.
- 191r l. 15 "chiesa catolica [?apost.] romana ala": "2 7 2 0 7 9 1 4 7 8 5 6" (best parse "aiaposit"). Blocker: no-key-material.
- 191r l. 19 "gratie ala [?Francia] che però": "1 5 2". Blocker: no-key-material.
- 191v l. 3 "dise che [?non] poteua sprezare": "3 3". Blocker: no-key-material.
- 191v l. 4 "né meno [?contra] il consenso": "5 6 4 9 2" (best parse "ettra"). Blocker: no-key-material.
- 191v l. 11 "suo guardasigilo fato[mi] intendere ala": "8 3 0 2 1 5 1 9 1 2 0 7" (best parse "mtomi"). Blocker: no-key-material.
- 191v l. 20 "questo negotio [?Ma] da qualch": "2 0 1 2 1 2 8" (best parse "ana"). Blocker: no-key-material.
- 192r l. 3 "forza si [p] ublicase il": "4 7". Blocker: too-short.
- 192r l. 8 "ne poteua [scr] iuere a": "1". Blocker: too-short.
- 192r l. 16 "metono loro [?più] dificoltà de": "2 0 1 7 1 7 3" (best parse "miu"). Blocker: no-key-material.
- 192r l. 24 "a qualche […]": "2 0 1 7 0 1" (best parse "min"). Blocker: no-key-material.
- 192v l. 1 "[…] generale congregatione": "2 1 2 5 1 1 2 1 7 7 0 3 0 1 2 1 2" (best parse "atzriinfra"). Blocker: no-key-material.
- 192v l. 4 "con modi destr[i] di guadagnare": "2 6 3 5 4 9 111^." (best parse "detr[il"). Blocker: no-key-material.
- 192v l. 4-5 "più che […] in questo": "4 1 3 1 0 3 3 7 | 1 9 1" (best parse "hunuuo"). Blocker: no-key-material.
- 192v l. 5 "punto et […] si potrà": "4 1 3 5 3 7 1 8" (best parse "heur"). Blocker: no-key-material.
- 192v l. 7 "di quello [che] dourò [f]": "(none)". Blocker: nothing written there; no-key-material.
- 192v l. 7 "[che] dourò [f] are per": "2 0". Blocker: too-short.
- 192v l. 8 "compitam[ente] a […] uolontà et": "5 5 0 2 1 2" (best parse "ela"). Blocker: no-key-material.
- 192v l. 9 "N S […]": "8 7 2 2 9 5 7 9 6 9 5 7 221^. 0 5 7 2 0 0 166^. 4" (best parse "aaoeioetei[lettere]liar[questo]s"). Blocker: no-key-material.
Result: 1 hole filled; 55 left, each with its blocker.

## 14 Nov 2026: one-digit slips (Brice Dudout, with Claude Opus 5.5)

README rule of 14 Nov 2026. Meister no. 40 is the key of the period (the Secretariat's key for Morosini, 8 June 1587),
not one rebuilt here. Every hole of the r2p list was tested for the word the sense wants with exactly one digit
changed (no insertion, no deletion); the candidates were looked at on the DECODE R33 images (crops kept privately).
Closed:
- 189v l. 4 "uole{+r}": 3 91 50 35 2 | 64 per; a hooked 2 (or the clerk's final 1 with a flourish): read either way.
- 189v l. 24 "uole{+r}": 3 91 50 35 2 | 70 37 42 ...; a 2 with a flat base. Slip.
- 192r l. 16 "{+p}iù": 20 17 173; the first figure is a 2 like the 2 of the following 26, not a 7. Slip.
- 189v l. 4 "esenti": DECODE "0 2 1 5 1 7 1"; the figure read 2 has the same hooked form as the line's final 1
  (171 = i): 01 n, as in "esentioni" (l. 8-9). Read from the figures (a slip for 01 if it were a 2: read either way).
- 191v l. 11 "fatomi": 8 30 2 15 191 20 7, a lone null 8. Read from the figures.
Looked at, not counted: 190v l. 14 "conu[e]niua" (76 37 3 at the line end, at the gutter: a lost 5 cannot be ruled
out); 190r l. 14 "in[st]igati" (the figure that would be 15 is under show-through); 192v l. 4 "destr[i]", 191v l. 4
"[?contra]", 189v l. 16 "[?posedono]" (blot, show-through, hole in the paper). Read share by words 78 -> 73 holes in
1,506 words, 0.948 -> 0.952: read.
