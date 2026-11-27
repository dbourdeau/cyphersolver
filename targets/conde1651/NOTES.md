# conde1651 — Condé to Armand du Lau du Chambon, Aug–Sep 1651 (AD Dordogne 2 E 1841/18; catalogue 1213)

Status: in progress — the reading is finished, the write-up is owed (27 Nov 2026). Catalogue 1213 is finished as a whole: the
bundle 2 E 1841/18 was photographed in full (46 frames) and its only cipher is these five letters, already deciphered by
Brianson (typescript and key in the bundle; read here with his key, outcome "read with known key"); the 1652 letters are in
clear, and the Roman-numeral name table is another system with no ciphertext here, filed apart as research/leads.json 3937.
This work adds something Brianson's unpublished typescript and 1983 summary do not give: the key validated on a held-out page,
a sign-level transcription, English translations, and a list of places where the cipher reads differently from him (division,
entretienne, Bordeaux for his ?/1, avec for his ?/9 ...), with new credits (Brice Dudout, Catherine Schunck). So it takes the
`/writeup` route, not "no write-up" (that is for a target found solved with nothing added). Entry 1213 leaves catalogue.json
with the write-up, listed under "Read or resolved here, and removed". Before the page: the reading_review of each letter, and
the open question of the image conditions (section below: AI analysis of the photographs was not agreed by anyone).

Source: Archives départementales de la Dordogne, 2 E 1841/18 (du Lau du Chambon papers). Photographs taken in Nov 2026 for the project by the Société historique et archéologique du Périgord (Catherine Schunck, SHAP). Images are not distributed and no crop is included; cite « AD Dordogne, 2 E 1841/18 ». Frame numbers (P1370NNN) are the photographer's.

## Images: who took them and on what conditions (CONTRIBUTING, "Conditions of use of the images")
What is established, from our correspondence with the SHAP (secretariat, thread of 10–23 Nov 2026):
- The 46 photographs were taken at the AD Dordogne by **Catherine Schunck** (treasurer of the SHAP), as a
  volunteer, answering our request of 10 Nov 2026 relayed by the SHAP to its members. She sent them by file transfer on
  20 Nov 2026. They are not an order from the archive or from a paid photographer.
- On 23 Nov 2026 the SHAP agreed that she be credited by name, « Catherine Schunck (SHAP) », and listed among the volunteers.
  On showing the images, the SHAP said it had no objection on its side and left it to us to check what the AD Dordogne allow.
- **No written conditions of use came with the photographs**, as far as we know: none from the photographer, none from the SHAP,
  and we did not ask the AD Dordogne. Their reading-room rules on photographs have not been checked.
- **The use of an AI assistant was not raised** with Catherine Schunck, with the SHAP or with the AD Dordogne. Our request
  said that we would do the reading ourselves and publish it with credit; it did not say that the reading would be done by AI
  agents. So AI analysis of these images was **not explicitly agreed** by anyone.
- What we do in the meantime: the images, crops and thumbnails stay private (research copy, never committed or published);
  only our transcription of the signs is in this folder.
- Brianson's typescript and key sheets are photographed in the same bundle. We asked no one (his heirs, the SHAP or the AD Dordogne)
  about reproducing them and no one has agreed to it, so the typescript is not reproduced here (see "Protocol" for the held-out reference).

## Prior art (EXISTING)
- Gen. Arnaud de Brianson, « Sur cinq lettres chiffrées du prince de Condé (1651) », *Bull. Soc. hist. et archéol. du Périgord* CX (1983), 4ᵉ livraison: letter-by-letter summary and description of the system (issue #478).
- The dossier itself also holds Brianson's **complete typescript decipherment** of the five letters (CAPITALS = deciphered, ?/n = unresolved codes; a later all-lower-case version with codes pencilled in), and **his key**: a handwritten syllable grid (tilde / acute / diaeresis series) and a key sheet « Chiffre de Louis II de Bourbon, prince de Condé (août et septembre 1651) » (alphabet with homophones and symbols, caron words, macron names). Unpublished; not reproduced here.
- The letter of 25–27 Aug (18-11) carries brown-ink interlinear glosses of a few phrases (period or early; e.g. « n'y avoir aucun esgard », « mr le presydent dafis », « du retour des deputés »): a partial old decipherment.
- So 1213 is **already solved**. What this target adds: an independent check of Brianson's key on a held-out page, a sign-level transcription, a re-reading with the frozen key, and the list of places where the cipher reads differently from his typescript.

## Bundle (46 photos)
Folder cover; the five cipher letters (P1370687–688, 700–703, 705–706, 710–711; address panels 694, 704, 707, 709, 712; P1370689, presumably p. 4 of the 17 Aug letter, is an unusable grey frame); clear letters of 1651–1652 (incl. the Barbezieux agreement with du Dognon, Sept 1651, and Brouage, 2 June 1652); a period **name table** of another nomenclator (P1370715–717: « Noms propres de personnes, villes, bourgs et rivières », 110 entries with Roman-numeral codes 17–186 in A–V order, plus a « Nombre » table mapping numbers to capitals A–Z). It is a different system, probably late 1651–1652, and none of these letters uses it (see "The Roman-numeral name table" below; an earlier version of these notes called it blank, with an A–Z alphabet without values, which was wrong); Brianson's key sheets (718–719) and typescripts (720–727).

## The cipher
Two-digit numbers (some one-digit) with a superscript mark, plus about 20 symbols. Unmarked numbers 15–40 and the symbols: homophonic alphabet. Tilde, acute and diaeresis: syllables in consonant series (ga…gu, ca…cu, da…du, fa…fu, ha…hu; la…lu, ma…mu, na…nu, pa…pu, ba…bu; qua/que/qui, ra…ru, sa…su, ta…tu, va…vu) and short words. Caron: words (affaire, armes, ennemi, ami, avant, afin, aboutissement…). Macron: proper names (16 Paris, 18 Bordeaux, 65 Guyenne, 74 le Président, 81 le chevalier, 82 Monsieur…). Same graphic family as the Condé–Barrière key of 1655, different table.

## Protocol and measure (prereg/)
- K2 = Brianson's key as left in the dossier, transcribed by us without seeing the ciphertext transcription; frozen with SHA-256 together with the protocol, the scorer and the reference (prereg/PREREG.sha256).
- Held-out: all cipher of P1370688 (17 Aug letter, pp. 2–3) between its first clear passage and its last cipher run; 410 signs measured. Reference: Brianson's capitals for the same passages, ?/n removed (`prereg/reference_brianson_688.txt`). **The reference is held outside the repository**: it is 693 letters of Brianson's unpublished typescript and no one has agreed to its reproduction. Only its SHA-256 is given (`prereg/PREREG.sha256`: 4efeb03a879ef980cd38c034526e3bdcb6f7d01bca44b33ee40bd6ff022312b6); the typescript itself is in the bundle at the AD Dordogne (P1370721). The file was in the first commit of this pull request and was removed in the follow-up; `validation.json` no longer prints it.
- Transcription: two blind passes + blind arbiter (blind/P688_*).
- Result (validation.json): **K2 0.869 vs best of 200 permuted-key controls 0.293 → pass.** Our 1655 Condé–Barrière key on the same portion: 0.205 (below its controls) → fail. P1370688 is burnt.
- **The '?' step, not in PREREG.md.** The blind arbiter kept a '?' on 29 of the 412 held-out signs (a mark or a digit it was unsure of). Before the run, every '?' was removed mechanically and the sign kept as read; nothing else changed (`prereg/transcription_mesure.json`, now in this folder, = `blind/P688_arbiter.json` without the '?'). Its SHA-256 (f36e6988…) was added to `prereg/PREREG.sha256` at 02:06 on 23 Nov 2026, after PREREG.md was frozen (01:43) and before the result file (02:08), by file times. PREREG.md does not say it: the protocol says only that the arbitrated file is hashed before the measure. **The filed transcription fails without this step**: with the flags kept, score.py gives K2 0.792 against a best control of 0.296 (re-run 23 Nov 2026, as Daniel Bourdeau found). The pass therefore rests on a step that was declared after the run, not pre-registered. Other deviation declared: both keys scored in the same single run.

## Reading
All five letters transcribed (two blind passes + blind arbiter per group, blind/P1–P3_*), decoded with the frozen K2 (decryption.txt) and read by rule of #728 (reading_*.md, notes in French). English translations of the cipher passages, with the same holes: translation_en_*.md. Sure words = every sign in K2 and transcribed without '?'. Most holes come from symbols the transcribers and our key transcription name differently (see key_K2b.tsv), not from the cipher.

| Letter | Shelfmark | Cipher signs | Cipher words | Sure | Probable | Restored | Unresolved | Share |
|---|---|---|---|---|---|---|---|---|
| 6 Aug (PS 8 Aug) | 18-14 | 427 | 154 | 77 | 58 | 14 | 5 | 0.500 |
| 13 Aug | 18-12 | 383 | 155 | 92 | 51 | 6 | 6 | 0.594 |
| 17 Aug | 18-3 | 635 | 264 | 170 | 78 | 6 | 10 | 0.644 |
| 25 Aug (PS 27 Aug) | 18-11 | 238 | 113 | 66 | 40 | 2 | 5 | 0.584 |
| 3 Sep (PS 4 Sep) | 18-10 | 235 | 102 | 73 | 25 | 0 | 4 | 0.716 |
| **Total** | | 1,918 | 788 | 478 | 252 | 28 | 30 | **0.607** |

Counts after the blind sign check of 23 Nov 2026 (section "Sign check"); before it: 6 Aug 75/60/14/5, 25 Aug 64/42/2/5, total 474 sure (0.602).

(Brianson dated the first letter 5–6 Aug in 1983; his typescript and the letter say 6 Aug, postscript 8 Aug.)

## Where the cipher reads differently from Brianson's typescript
Word level, each checked against the signs (details in each reading file):
- 17 Aug: « de cette **division** » (46¨ = di, two clear dots) where he typed REVISION; « creu **m'en** devoir ouvrir » (he omits m'en); « n'en parle **plus** », « ne sera **pas** cogneue », « ne doute **plus** » (94′ plus / 84′ pas; his PLUS and PAS are swapped); « en mesme **estat** » for his restoration (TEMPS); « en **ce rencontre** » for « cet encontre »; « ou **chevalier** Todias » (81¯) for his (PAR); « l'**alarme** » for his restoration (ENNUI); he adds AI before « respondu » (no sign); his ?/1 (twice) = **Bordeaux** (18¯ in his own key) and ?/9 = **avec** (48ˇ).
- 13 Aug: « **entretienne** » (67¨ 67~ 69¨ 55′, all sure) for his « entreprenne »; « **ie** n'aye » (he omits ie); « **des** » (51~) for « de »; « n'entre » (sing.) for « n'entrent »; his bare 18̄ = Messieurs de **Bordeaux** (his own key).
- 6 Aug: « l'**aboutissement dans** ces messieurs » (50ˇ, 49¨, both in his key) for his « l'(accord) de ces messieurs »; the cipher opens a passage with « **utiles** » (54ˇ), which he leaves out, and has no « toutes les nouvelles »; word order « rentrent en pas vne » vs his « pas en une ».
- 25–27 Aug: he leaves out the cipher clause « il faut **n'y avoir aucun esgard** » (also in the brown-ink gloss); « l'envoy de vre **homme** » (HOMME is in cipher; he reads the clear « vre » as « vivres »); his 18̄ = **Bordeaux**, his restoration (province) = **Guyenne** (65¯, his key). The brown-ink glosses agree with the cipher where they exist.
- 3–4 Sep: « les armes à **Bordeaux** » (he leaves 18̄); « en estat de **faire** prendre »; « **d'**autant que ». Date: « De Paris le 3e septembre 1651 » as Brianson (not « 23e »: the postscript of the 4th answers « la vostre du dernier du mois passé »).
- Codes he left ?/n and still open here: 96 (×6; he suggests du Dognon in 1983), 97 (×4; Laisné), 99, 59 (bare; 59¯ = Richelieu in his key), 66′, 98′, 12~, 35~, 62′, 8¯, and the marginal insertion of 17 Aug « 85 π 38 68 33 32 / 95 » (« ‹85› et tous ‹95› »; his « lire par un … … » is unread clear text, not this insertion).
- Where he reads more than the frozen key gives (counted as holes here): rien, car comme, nous en, vaisseaux, succès; nos ennemis, leurs, ses vues, jugerez, important, Madame; Conseil (29¨), Madame (83¯), avoir (45ˇ), pas (83′), la dessus / la maniere.

## K2b (key_K2b.tsv) — not validated
Corrections found after decoding: the transcribers' low π = Brianson's « pi-barré » (e), their « w » = his « u » (n), their б-shaped « sigma » = his U/V « 6 » (u/v); 19′ = le, and 18′ = la (his grid's acute row seems shifted by one column); 45ˇ avoir, 98 bien, 48 du, 83′ pas, etc. No fresh held-out portion remains, so K2b is not validated and is never used for a sure word.

## Sign check, 23 Nov 2026

Level sought: "AI decipherment, human-checked on a sample of signs" (`outcome.sign_check`, held in `sign_check_pending.json`
until the field is in profile.schema.json; files in `sign_check/`). It checks how fourteen doubtful or decisive signs are
written, not the key as a whole, and it changes neither the class (already solved) nor the state (read in part).

**Sheet.** Seventeen questions: fourteen targets and three controls. Each question boxes one sign (a superscript mark, a digit
or a symbol) and offers shapes cut from sure words of the same hand, plus "none / other shape", "cannot tell", "illegible"
and "not a sign". No gloss, reading, value, place or date was shown. The three controls are signs of sure words with a known
answer (¯ of 18¯ Bordeaux, 9 of 94′ plus, ¨ of 96¨ ie): **all three correct (3 of 3)**. The targets: seven signs that carry
our corrections to Brianson's typescript (A1-A7), five doubtful signs or sign names (B1-B5), two code shapes whose value stays
out of the sheet (C1-C2).

**Who did what.** The checker is Brice Dudout (a member of the project, not an independent reader). An AI model (Claude Opus 5.5)
wrote the selection rule, cut the thumbnails, built the sheet, scored the answers and read the remarks. The answer key
(which option is which) stayed private until the answers were exported, and is not committed. No image, crop or thumbnail is
committed (see "Images").

**Rule.** `sign_check/sheet-C-rule.md` (in French, as written), SHA-256
5661bbd0f8aa1b5f32f37e8b563e848fd2b170b8140ffa46e95a4bddcf2eebdd, written and hashed before the thumbnails were cut and
before any answer. Its integration clause (section "Intégration") was applied as written, with no change. Answers:
`sign_check/sheet-C-answers.json`, exported 2026-11-23T19:41:21Z, SHA-256
f28aa79635beb692f77e543327e711d666a9ebd24f2be70d1092c4699fd6355f; results: `sign_check/sheet-C-results.tsv`.

**Effect (by the clause; the blind files in `blind/`, the frozen key and K2b were not touched).** Settled signs are marked `!`
in transcription.txt and decryption.txt is updated for them.
- The seven corrections to Brianson are confirmed at the sheet: « division » (A1), « chevalier » (A2), « l'alarme » (A3),
  « plus » (A4), « dans » (A5), « Guyenne » (A6), and « homme » (A7), which becomes sure.
- New sure words (+4): « l'aboutissement » (B1, the sign is Π = l, not a low π; 25 Aug), « homme » (A7, 25 Aug), « messieurs »
  (B3, the sign is a 6 = v/u, not the sigma of the key; 6 Aug), « disposition » (B5, 46¨; 6 Aug).
- B2 was answered with the other proposed shape: the mark on 19 in « ie {19} puisse » (25 Aug) is ¨, so K2b's 19′ = le is
  not supported there, and « le » goes from probable to restored. No sure word lost.
- B4 (mark on 97 in « {besoin} », 3 Sep): "none / other shape", remark « Deux traits »: word unchanged (probable).
- C1 (59, 13 Aug): the first digit is 5; the code stays unread. C2 (stroke right of 99, 6 Aug): "none / other shape", remark
  that it is not a mark above a digit but rather a comma before the clear text; by the clause the word is unchanged
  (‹99›, unresolved either way).
- K2b: the sigma-to-6 naming (B3) is supported on the transcription at that place; 19′ = le (B2) is not. K2b stays not
  validated (a shape check validates no value).
- Counts: 6 Aug 75 -> **77** / 154; 25 Aug 64 -> **66** / 113; the other letters unchanged; total 474 -> **478** / 788
  (0.602 -> **0.607**). The rule foresaw at most 479 (B4 would have made the fifth) and at most a loss of 4.

**Limits.** One checker inside the project; three controls; the signs were chosen because they were doubtful or decisive and
the options were cut from the same hand: a diagnostic, not a sample of the text. No person has audited the model's part. This is
not a `human_check`. The check does not touch the open codes.

## The Roman-numeral name table (P1370715–717)

Studied 23 Nov 2026 (follow-up to the first commit). Transcription of the table: `key_names_1652.tsv` (code, code as written, entry, person/place, whether the count of minims was taken from the sequence, frame). Photographs by Catherine Schunck (SHAP); transcribed and analysed by AI agents (Claude Opus 5.5) run by Brice Dudout; not checked by a person on the images.

### What it is
- The proper-name part of a nomenclator: 110 entries (46 persons, 64 places: towns, bourgs, rivers, islands), filed under initials A–V. Within each initial, persons come first and then places. Numbering rises steadily from 17 to 186, and dotted blank lines are kept free between blocks. Codes 1–16 and any alphabet or syllable table are missing, so this is one part of a larger key. The rest is not in the bundle.
- Period corrections: in the places column, "Condé" is struck through and rewritten "Conac" (code 55 unchanged). There is one modern pencil note: "erreur : XL" against "La Boutonne R. — Lx", because Lx (60) is already used for the Charente.
- The names belong to the Saintonge–Aunis–Guyenne war of the princes' Fronde. On the royal side they include Harcourt, Plessis-Bellière, Folleville, Montausier, Saint-Luc and "le Mazarin". On the princes' side they include Condé, Conti, Marsin, Tarente, Nemours, Beaufort, Rohan, La Rochefoucauld, Viole, Baltazar, Chouppes and du Daugnon. Spain and Vatteville also appear. The places include Brouage, Taillebourg, Tonnay-Charente, Tonnay-Boutonne, Saintes, Pons, Cognac, Barbezieux, Talmont, Oléron and Ré. All of this is consistent with **late 1651–1652**, when du Lau was governor of Saintes and then maréchal de camp at Brouage (letter of 2 June 1652 in the same bundle). Retz is still "le Coadjuteur".
- "M. de Chambon" (45) is Armand du Lau du Chambon himself. The copy is his.
- Full table: key_names_1652.tsv (code, code as written, entry, person/place, flag where the count of minims was taken from the sequence, frame).

### Is it the key of the 1651 letters? No.
We checked it against the name codes of the 1651 key (Brianson's macron series, K2) and found **0 agreements out of 9**:

| Name | 1651 letters | This list |
|---|---|---|
| Paris | 16¯ | 130 |
| Bordeaux | 18¯ (4×, sure) | 31 (18 = Amboise) |
| Guyenne | 65¯ / 95¯ | not listed |
| Richelieu | 59¯ (also bare 59 in "59 et Madame de Richelieu sont à Richelieu") | 59 = Crazannes |
| le chevalier | 81¯ | 81 = Gaixe (?) |
| Monsieur | 82¯ | 82 = La Garonne |
| le Président | 74¯ | 74 unassigned |
| du Dognon | 96 (context: his quarrel with the Parlement; Brianson) | 64 |
| Laisné | 97 (Brianson) | 96 |

### Effect on the unresolved codes of the reading
The frozen reading stays at 474/788 sure words. None of the open codes is resolved by the list.

| Code in letters | Occurrences | Value in this list | Proposed | Why not |
|---|---|---|---|---|
| 96 (bare) | 10 | M. Laisné | no | 96 = du Dognon by context; different system |
| 97 (bare) | 6 | Mr de Lorge | no | 97 = Laisné (Brianson); different system |
| 99 (bare) | 5 (+2 uncertain) | unassigned | no | |
| 95 (bare, marginal insertion) | 1 | M. de Longueville | no | different system; 95¯ = Guyenne in K2 |
| 85 (bare, marginal insertion) | 1 | unassigned | no | |
| 64 (bare?) | 1 | M. du Daugnon | no | the clear text nearby names du Dognon, but he is 96 in these letters; mark uncertain |
| 59 (bare) | 2 | Crazannes | no | Richelieu context |
| 8¯, 83¯, 12~, 35~, 62′ | 1 each | unassigned, or 35 = Bergerac | no | |

No key test was run because no key hypothesis applies to the letters. A names-only portion would in any case be under 300 signs, which our protocol counts as not measurable.

### Prior art
- Not in Brianson's article (BSHAP 1983), which describes only the 1651 nomenclator.
- Not in his key sheets or typescripts left in the bundle (P1370718–727).
- Not in catalogue.json (entry 1213 does not mention it), leads.json or targets/, checked on 23 Nov 2026.
- New, as far as we know.

### Use elsewhere
This list could be the name key for any 1651–1652 cipher letter from Condé's network in Saintonge and Guyenne: du Lau, Marsin, Baltazar, Viole, du Daugnon, Tarente, Lenet's papers, or the déchiffrement tables at Chantilly (leads.json 1846, Ms 1876). In such letters, names would appear as numbers 17–186 and plaintext numbers as the capitals A–Z. None of the letters in this bundle uses it: the 1652 letters here are in clear.

Filed as a lead of its own by the maintainers at the integration of PR #937 (27 Nov 2026, one key per entry): research/leads.json 3937, from `research/dudout_leads_2026-11-27_conde1651/`. Not vetted and not in the catalogue.

## Not done
No reading_review recorded (left to the reviewer). No image or crop in this folder. Brianson's papers at the SHD (GR 1KT 211 / 1 Kmi 62) not seen.

## Remaining gaps

- Open name and word codes - blocker: open-codes; 96 (bare, 10×), 97 (bare, 6×), 99 (bare), 59 (bare), 66′, 98′, 12~,
  35~, 62′, 8¯, 83¯, 29¨ and the 17 Aug marginal insertion « ‹85› et tous ‹95› »: neither Brianson's key nor the reading
  settles them; Brianson left them ?/n too (1983: 96 probably du Dognon, 97 very probably Laisné); the 1652 name table of
  the same bundle is another system (0 of 9 known names agree) and resolves none; another letter in this key, or its full
  table, would.
- K2b, the corrections found after decoding - blocker: too-short; symbol-name correspondences, the 18′/19′ grid shift and
  about 20 values (`key_K2b.tsv`); no fresh held-out portion of 300 signs or more remains (P1370688 burnt, the four other
  letters used to find K2b), so K2b is not validated and never gives a sure word.
- Fourth page of the 17 Aug letter (P1370689, a grey frame) - blocker: needs-physical-access; the end of the letter from
  « travaillez de [mesme] sorte », its date and close are not seen; a new photograph at the AD Dordogne would give them.

## Escalation

- [x] siblings: the whole bundle 2 E 1841/18 photographed (46 frames) and opened: clear letters of 1651–1652, the brown-ink
  glosses, Brianson's key sheets and typescripts, the Roman-numeral name table (P1370715–717, studied above). Other
  bundles of 2 E 1841 not seen.
- [x] clear-pages: the brown-ink interlinear glosses of the 25–27 Aug letter compared with the reading (they agree where
  they exist); Brianson's typescript capitals used as the held-out reference; the clear 1652 letters of the bundle hold no
  decipherment.
- [x] known-keys: Brianson's key (K2, pass), our Condé–Barrière key of 1655 (K1, 0.205, fail) and the 1652 name table
  (0 of 9 names agree) tried.
- [x] print: Brianson, BSHAP CX (1983) read; catalogue.json, research/leads.json and targets/ checked (23 Nov 2026); no
  other edition known to us. Not seen: Brianson's papers at the SHD (GR 1KT 211 / 1 Kmi 62); Lenet's papers and the
  Chantilly decipherment tables (leads.json 1846, Ms 1876) not searched for other letters in this key.
- [x] key-rebuild: K2b from the decoded letters (key_K2b.tsv), kept apart and not validated.
- [x] retry: the doubtful marks and digits that decide a word were put to a blind sign sheet (14 targets, 3 controls,
  23 Nov 2026; section "Sign check") and the words regraded: 474 -> 478 sure. The open codes need another letter in the
  same key (Remaining gaps).
