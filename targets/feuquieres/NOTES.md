# Feuquières → Catinat, Pignerol, 25 January 1691 — **read 2026-09-16** (586 of 601 tokens over the two letters in the code)

Status: read in part (23 Oct 2026, verification 5): the d'Herleville letter reads; the Feuquières letter is decoded, not read (0.545). See "Verification 5" at the end.

Not to be confused with [targets/feuquieres1678](../feuquieres1678/NOTES.md): Louis XIV to the marquis de Feuquières,
9 December 1678 (BnF NAF 22738), a different item, read by George Lasry (BnF cipher research, 10 Oct 2026).


**Result.** The 418-group despatch is written in the *petit chiffre* of the Pignerol governors (Bazeries' term; 367
groups, the small companion of the Grand Chiffre of 1691). The same code carries a second printed letter that nobody
had connected with it: **Louvois to d'Herleville, governor of Pignerol, Versailles, 6 September 1690**, printed in
cipher *with its contemporary "traduction"* in the 1819 *Mémoires de Catinat*, t. I pp. 140-142 (MDZ bsb10720286
scans 212-214, `herleville.txt`, `img1/`). d'Herleville was Feuquières' predecessor at Pignerol; the cipher stayed with
the governorship. The two letters share 72 of the d'Herleville letter's 91 groups, the same 46 % share of tokens on
groups below 100, twenty bigrams and the trigram `25 355 42` (= *de Mon-de[vis]*). Aligning the d'Herleville cipher
with its translation and propagating every reading to the Feuquières letter (and back) gives a key of 167 of the 179
groups used (`key_petit_chiffre_1690.tsv`) and the reading below (`reading.txt` gives the group-by-group alignment).

## The Feuquières letter, as read (17th-century spelling kept; unread groups in brackets)

> Je reçois, Monsieur, à dix heures du matin la lettre que vous me faites l'honneur de m'escrire du vingt-quatre,
> avec le duplicata. Vous aurez veu [par] le retour du courrier que je vous dis [54 257]is [go] exécuter vos ordres.
> [Par] cecy vous sçaurez que je suis tout prest, [333] qu'on ne pense [9 go ri 122] les [des] que vous [122]u les
> commencer. [À] Veillane, persuadé qu'ils enlèveront le [19] au bruit de l'attaque de Veillane, le peu de monde
> qu'il y a et les moyens d'y entrer, tout doi[ven]t faire croire qu'ils ne viendront pas à le défendre
> sérieusement. Je ne sçais du tout par où faire passer à Saint-Ambroise les quatre-vingts maistres que vous [vous]
> demandez ; les chemins pour y aller du costé de Javan e[t] [a 132 257 l] vous coupe[s] [249 86]. En approchant de
> Veillane on trouve deux chemins, dont l'un vous conduit au fauxbourg des Trois Couronnes, l'autre aux maisons [292]
> et le long de l'estang. J'attaqueray [353] deux endrois, et surtout [mes se 271 se s] prendray garde que les dragons
> ne puissent m'eschaper. [342 103 190]

What it says: Feuquières acknowledges Catinat's letter of the 24th (received at 10 a.m. with its duplicate), says he
is ready and that the return of the courier carries his execution of Catinat's orders; the enemy will not defend
Veillane seriously (few men inside, ways in known); he does not see how to get the 80 horse Catinat asked for to
Sant'Ambrogio (the village between Avigliana and Rivoli) because the roads from the Javan side cut across; two roads
lead into Avigliana, one to the faubourg "des Trois Couronnes", the other to the houses along the pond; he will
attack at two points and above all keep the dragoons (Macel's, in the town) from escaping into the castle. This is
exactly the plan of Catinat's "Mémoire pour l'entreprise de Veillane" of 19 Jan (rendezvous at the head of the
estangs, the Javan and Trane roads, the faubourg, the dragoons) and matches Feuquières' own account in his
*Mémoires* ("ce régiment de dragons qu'on vouloit enlever dans la ville"). The letter's date, 25 January, the time
"dix heures du matin", and "du vingt-quatre" are all internal.

The last three groups (`342 103 190`) and the first eight of the d'Herleville letter (`39 249 190 86 40 103 190 11`,
with `103 190` common to both) are almost certainly nulls or a stock closing/opening, as in the Grand Chiffre, where
paragraphs begin and end with two to four "point ou nulle" groups.

## The d'Herleville letter (control: it matches its printed translation, with the clerk's own wording)

> [8 groups] Je mande à M. de Catinat que le roy vous permettoit de demander la contribution au pays de Mondevis, et
> que si vous croyez qu'il convien[s]t au servi[ce s] le roy de les exempter, mesme de permettre aux habitans dudit
> pays de razer la citadelle du[d]it Mondevis, de le faire. — J'atendray avec impatience l'arrivée du prochain
> ordi[n]aire pour sçavoir comment aura réussi vostre entreprise sur le chasteau de Villefranche.

The 1819 "traduction" reads *si vous jugez qu'il convient au service du roi* and *Mondovi*; the cipher has *si vous
croyez*, *Mondevis*, *razer*, *M. de Catinat* as one group (218), *le roy* as one group (102). That the translations
were free renderings, not verbatim decipherments, is also visible on the Grand Chiffre letter of the same day to
Catinat (t. I pp. 142-144), which decodes with Bazeries' table as *importantes nouvelles de la reussite* where the
printed translation has *des nouvelles*. This is why every exact known-plaintext aligner failed (see Method).

## English translation

> **Feuquières to Catinat, Pignerol, 25 January 1691.** I receive, Sir, at ten in the morning the letter you do me the
> honour of writing on the twenty-fourth, with the duplicate. You will have seen [by] the return of the courier that I
> tell you [...] to carry out your orders. [By] this you will know that I am quite ready, [and] that no one thinks [...]
> the [...] that you [wish?] to begin them. [At] Veillane, persuaded that they will carry off the [post] at the noise
> of the attack on Veillane, the few men there are and the ways of getting in all must make one believe that they will
> not come to defend it seriously. I do not at all know by what way to pass the eighty troopers you ask [of us] to
> Saint-Ambroise; the roads for getting there from the Javan side cut across [...]. Approaching Veillane one finds two
> roads, one of which leads you to the faubourg of the Three Crowns, the other to the houses [...] and along the pond.
> I shall attack [at] two points, and above all [...] shall take care that the dragoons cannot escape me. [...]

> **Louvois to d'Herleville, Versailles, 6 September 1690.** [...] I am writing to M. de Catinat that the King
> permitted you to demand the contribution of the country of Mondovì, and that if you believe it suits the King's
> service to exempt them from it, even to allow the inhabitants of the said country to raze the citadel of the said
> Mondovì, to do so. — I shall await with impatience the arrival of the next post to learn how your enterprise
> against the castle of Villafranca will have succeeded.

*Maistres* = mounted soldiers; *enlever le poste* = to surprise and take a garrison; Villefranche = Villafranca
Piemonte, taken by d'Herleville from Pignerol on 2 September 1690.

## The key (design)

Two-part code of 367 groups, the Grand Chiffre's little brother: **letters** (i/j and u/v one letter each) with two to
four homophones each, mostly below 100 (e: 4 41 125 212; s: 21 134 200 252 304; t: 91 322 343 362; n: 51 154 228;
r: 60 82 178 275; a: 32 213 251; u: 37 78 191 285; d: 63 168; l: 43 68; i: 90 144 182; y: 24 59; g: 81 259; x: 181
352; b: 40 50; f: 124 366; p: 5 240; c: 101; m: 28; o: 27; z: 104); **syllables** of the Grand Chiffre kind (ma 106,
ti 175, ro 113, ri 188, ra 135, re 22/44, se 83/110/183, pe 235, ve 150/165, vi 210, co 57/153, di 146/217, li 254,
ca 93, ha 193, he 229, mi 255, bo 318, bu 202, cu 179, fa 108, ga 279, go 145, lo 231, ta 156, te 205, to 250, va 76,
ci 169, do 214/311, su 247, xe 111, on 160, en 65, ns 243, st 234, is 280, oit 126, ment 85, mais 172, moy 334, puis
136, vie 148, sca 328, scavoi 74); **words** (de 25 42 71, que 99 147, le 56 177, la 114 151, les 47, des 237, du 300
347, au 184, et 258 341, si 196, y 24, on 100, ou 197, par 216, pas 195, pour 350, sur 88, tout 266, vous 84 241,
mesme 2, comme 80, peu 278, lettre 15, honneur 31, le roy 102, M. de Catinat 218, Monsieur 296 (with 355 mon), vostre
149, quil 164) and **nulls / points** (52, 194, and the opening and closing groups above). Numbers are spelled (*dix*,
*vingt-quatre*, *quatre-vingts*, *deux*). Place names are spelled (Veillane = ve-il-la-ne, Javan = ia-va-n,
Saint-Ambroise, Villefranche = vi-l-le-f-ra-n-c-he, Mondevis = mon-de-vi-s).

## Method (what finally worked, and what did not)

1. **Bazeries' Grand Chiffre de 1691 transcribed** from the Gallica page images of *Le Masque de fer* pp. 280-289
   (`bazeries/f305-f315.jpg`, `grand_chiffre_1691.tsv`, 587 entries, 91 left blank by Bazeries). Checked by decoding
   the 19 Aug 1691 despatch he prints as proof (`aug1691_decoded.txt`) and the three Louvois-Catinat letters of 6, 8
   and 10 Sept 1690 printed in cipher in the 1819 *Mémoires* t. I: all read cleanly. The table gives the *design* of
   the petit chiffre (Bazeries, p. 272: "il ne différait du grand que par son nombre de groupes"): letters with
   homophones, CV syllables, word stems, nulls, i/j and u/v merged.
2. **Second letter found.** The hOCR of all three 1819 volumes was pulled from the MDZ API (`fetch_mdz_ocr.py`,
   `catinat1819_*.txt`, not tracked) and searched for runs of numbers. Vol. I pp. 140-141 holds the d'Herleville
   letter in the petit chiffre with its translation; vol. II pp. 297-343 holds some 12,000 groups of Grand Chiffre
   letters of 1691 (Louvois to Catinat, no translations printed; they decode with the table, a by-product to exploit
   separately); vol. I pp. 15-17 holds an older Casal cipher of the 1680s with the editor's partial interlinear
   decipherment.
3. **Exact known-plaintext alignment fails** (beam aligner `align.py`, self-tested on synthetic encodings: fine),
   because the translation is not verbatim and because i/j, u/v are single letters. Annealers scored on the
   translation's 5-grams, on the LM with the closed inventory, or with the partial key fixed, all produced word salad
   (`solver_gc.py`, `solver_trad.py`, `solver_joint.py`, `solver_fixed.py`): the design-faithful control
   (`make_control_gc.py`) confirms 10-12 % recovery, truth outscored by more than 1,000 nats. Stochastic search is the
   wrong tool here.
4. **What worked: anchoring by hand and propagating between the two letters.** The second half of the d'Herleville
   P2 admits one segmentation of exactly 31 groups (*comment aura réussi vostre entreprise sur le chasteau de
   Villefranche*) in which every repeated group agrees; those units, carried into the Feuquières letter, gave *heures
   du matin*, *du vingt-quatre*, *m'escrire*, *duplicata*; each new word fixed further groups (Veillane from the
   thrice-repeated `301 151 310`, *enleveront*, *trouve*, *doivent* from 150 = ve, *dragons* / *chemins* / *maisons*
   from 243 = ns, Saint-Ambroise from the *faire passer à …* clause, *le long de l'estang*, *dont l'un … l'autre*).
   `show.py`, `ctx.py` and `reading.txt` are the working tools; `key_partial.txt` the working key.

## What remains

Twelve groups unread (singletons or doubletons: 9, 19, 54, 122, 132, 194, 257, 271, 292, 333, 353 and the
opening/closing nulls), and a few units marked `?` in the key: *Trois Couronnes* (237 322 46 is 153 u ro n ne s;
"des trois couronnes" is the reading that fits the groups, a faubourg or inn of that name at Avigliana is
unverified), *do* 214/311, *par ou* 216/197, *vous* 241 (perhaps *nous*), *le roy* 102 vs *roy*. Check against the
original (SHD, Archives du dépôt de la guerre vol. 1079, where Catinat's 29 Jan report also sits) if it can be seen.
Bazeries' reading of 1893 was never published; this is, as far as we know, the first since his.

---

# Earlier state (2026-09-15): attempted, not solved — kept for the record

# Feuquières → Catinat, Pignerol, 25 January 1691 — attempted 2026-09-15

Cryptiana "French Cipher Despatch received by General Catinat (1691)"; Tomokiyo's article `louisxiv.htm` §7 ("An
Unbroken (?) Code/Cipher for Catinat (1691)"). Antoine de Pas, marquis de Feuquières, governor of Pignerol since the
end of the 1690 campaign, to Nicolas de Catinat, commanding in Piedmont, then at Suze.

## Sources (all reachable from scripts, 2026-09-15)

* **The ciphertext.** *Mémoires et correspondance du maréchal de Catinat* (Paris, Mougie, 1819), t. II, Pièces
  justificatives (1), pp. 283-284. Bayerische Staatsbibliothek digital copy bsb10720287, scans 317-318
  (`img/t2_0317.jpg`, `img/t2_0318.jpg`, fetched from the IIIF image API; the hOCR of the whole volume comes from
  `https://api.digitale-sammlungen.de/ocr/bsb10720287/<scan>`). Tomokiyo's transcription was collated against the
  page images: **three corrections on p. 284**: `114 285 362` (Tomokiyo 283), `154 259 143` (Tomokiyo 250),
  `156 99 135 59` (Tomokiyo 133). `ciphertext.txt` carries the corrected text: **418 groups, 160 distinct, range
  4-366**, in two paragraphs (the print indents a new paragraph at `65 32 5 240 ...`).
* **What the letter is about.** The 1819 editor (t. II p. 8): "Nous avons une dépêche chiffrée de Feuquières, datée
  du 25 janvier 1691, à Pignerol, où il se concerte avec Catinat sur l'attaque de Veillane, fixée pour le 27. Tous
  nos efforts ont été vains jusqu'à présent pour la traduire." Veillane = Avigliana, in the Susa valley between Suze
  and Rivoli, held by a Savoyard garrison (500 Germans of Lorraine, the Croix-Blanche, four companies of Macel's
  dragoons, per Catinat 12 Jan). The attack of 27 January 1691 failed; Feuquières and Catinat blamed each other
  (Catinat to his brother, Gap, 19 Feb 1691, t. II pp. 6-8; Feuquières, *Mémoires*, quoted in the note below).
* **Cribs from the same weeks.** *Lettres inédites des Feuquières* (Paris, 1845), t. V, pp. 323-334 (archive.org
  `lettresinditesde05tien`, OCR): Catinat to Feuquières, Suze, 12 Jan 1691 (used as the control plaintext,
  `control_plain.txt`), and Catinat's **"Mémoire pour l'entreprise de Veillane", Suze, 19 Jan 1691**: Feuquières to
  leave Pignerol in the evening with all his cavalry and dragoons and 1,200 foot; rendezvous "à la teste des estangs
  de Veillane"; two roads, by Gumiane and Javan or by Trane past the Chisola below Piosasque; seize the Capucins and
  the faubourg; four days' bread, oats for the horses, powder, three pack-horses or mules of tools and hatchets,
  miners' tools from the Pignerol magazines, a hundred grenades; Suze's column, two cannon, 20 horses to be asked of
  Feuquières. The 25 Jan letter is Feuquières' answer to this memoir. Its vocabulary is in `solver.py` (DOMAIN, CRIBS).
* **Bazeries.** Burgaud and Bazeries, *Le Masque de fer* (1893), p. 272, says Bazeries deciphered this "petit chiffre"
  as well; no text was ever published (Tomokiyo). "Petit chiffre" is Bazeries' term for a two-table code with few
  entries (jfbouch.fr). Bazeries' Catinat papers (the Grand Chiffre, DE=34/42/97, entries to 587) are a different
  code; Feuquières wrote to Louvois in the Grand Chiffre and to Catinat in this small one.

## Structure

| test | result |
|---|---|
| tokens / distinct / max | 418 / 160 / 366; IC 0.0088 (Norbert on Klausis Krypto Kolumne, 2016: the Catinat 1702 letter gives 0.0088 too) |
| share of tokens below 100 | **46 %** (192 tokens on 50 distinct groups; 96 of 363 possible values = 26 % of the range). Mean 3.8 tokens per used low group vs 2.1 above 100: the high-frequency units (letters) sit below 100, the syllables and words above. Same skew as Catinat 1702 (253 of 591 below 100) |
| step-10 chains (Croissy one-part signature) | 20 chains of ≥3 among the 160 used values; random sets of 160 values give 16.9 ± 2.6, P = 0.16. Pairs (g, g+10): 69 observed vs 68.3 expected. **No column structure**: not a Croissy table. Consistent with a two-part arrangement inside each block |
| repeats | `301 151 310` ×3 (twice as `150 301 151 310`), `101 229 255 243` ×2, `60 300 57 78` ×2, `210 51 81 91` ×2, `78 44 200` ×2, `317 101 193` ×2, `44 200` ×3; 26 further bigrams ×2; no immediate doublets |
| letter block | 50 distinct groups below 100 for ~22 letters: 2-3 homophones per letter, as in the Louvois code of 1676 (t. II pp. 343-352: 3 numbers per letter, 2 per syllable, 11 nulls, 300 entries). Sukhotin on the low-group adjacency gives a vowel class of 15 groups carrying 72 of 192 low tokens (38 %) |
| spelled stretches | 100 runs of consecutive low groups; 14 of length ≥4, longest 9 (`65 21 63 59 65 91 22 60 52`) |

So the working model is: letters with homophones scattered over 1-99, CV syllables, a few hundred-odd words and nulls
scattered over 100-366, no alphabetical order in either block. That is the design the solver and the control assume.

## Attack

`solver.py`: simulated annealing over group → unit, units = letters / nulls below 100 and CV syllables, common letter
groups, the 500 most frequent words of the period corpus, the Veillane vocabulary and period spellings above 100;
scored by the spaceless 7-gram French model of the Chaulnes attempt (`../chaulnes/lm7.pkl`, 6.1 M characters), a
per-letter bonus, a unit prior, a null penalty and a crib bonus (each crib word counted at most twice); moves include
placing a crib word over a run of groups with the letter/syllable split dictated by the groups' classes.

`make_control.py`: Catinat's letter of 12 Jan 1691 encoded with a random code of the inferred design (letters 2-3
homophones over 1-99, syllables 1-2 numbers and ~100 words over 100-366, nulls), encoding rates tuned to the
target's profile: 418 tokens, 155 distinct, 184 low tokens (target 418 / 160 / 192).

Results (`sweep_control.txt`, `seed_test.txt`, `run_real_*.txt`):

| run | result |
|---|---|
| n-gram objective, calibration sweep on the control (`sweep_control.txt`, 100k iterations each, six weightings of letter bonus, unit prior and crib bonus) | in every weighting the solver's best wrong key outscores the **true key** by 150 to 1,400 nats; recovery 4-12 % of tokens. Decomposition: the true text has 779 letters and scores -1.84 nats per letter under the LM; the solver's texts have 830-2,250 letters made of dictionary words and score -1.3 to -1.5 per letter, so the letter bonus and the crib bonus are farmed by mapping groups to long words ("canon cavalerie et canon ce sa garnison de cette canon...") |
| word-segmentation objective (`solver_w.py`: Viterbi over a period dictionary, 7 nats per uncovered letter) | same wall: after 3,000 iterations a word salad of short function words ("a sa es a ne se sa le le ai au son et la on...") scores -1,590 against the truth's -1,724; 34/418 tokens recovered |
| how much crib would bite (`seed_test.txt`: a fraction of the true code fixed, the rest annealed, 100k iterations) | 20 % of groups given → 14 % of the remaining tokens recovered; 40 % → 43 %; **60 % → 63 %**; 80 % → 81 %. Even with most of the code in hand the objective still prefers a wrong completion (best -1,650 vs truth -1,844 at 60 %). The Veillane cribs, a dozen words, are far below what is needed |
| real letter, two seeds, 300k iterations (`run_real_1.txt`, `run_real_2.txt`) | scores -81 and -155, i.e. the crib-farmed regime the control predicts; outputs are strings of crib words joined by letters ("de veillane le s pointe l i s te est trane s e r e poudre a chevaux...") and are **not readings**. Not reported as a decipherment |

**Verdict: attempted, not solved.** 418 groups over a 160-group two-part nomenclator are as underdetermined as the
300 groups of the Chaulnes letter were, and the crib vocabulary, though certain, is too small to constrain it. What
would open it: Bazeries' working papers (he read the letter, *Le Masque de fer* p. 272), a second letter in the same
code (Feuquières' other despatches to Catinat of the winter 1690-91 are in the Catinat papers; the 1819 editor
printed only this one), or the key itself among Louvois' ciphers (BnF fr. 6204 holds Louvois' keys of the 1690s,
checked for Chaulnes; a Feuquières-Catinat "petit chiffre" of 366 entries would be the thing to look for there).

**Bazeries' book, read (2026-09-15, Gallica PDF bpt6k1523532j supplied by Daniel; OCR text in `masque_de_fer_1893.txt`).**
Burgaud and Bazeries, *Le Masque de fer* (1893) settle two points and print nothing usable. P. 37: among the
undeciphered despatches in the Catinat papers is "une du marquis de Feuquières, portant la date du 25 janvier 1691,
dont ni l'auteur, ni personne depuis n'a pu donner la traduction" (i.e. the 1819 editor and everyone since). P. 272,
note 1: "La dépêche de Feuquières à Catinat du 25 janvier 1691, relative à Veillane, était composée avec le petit
chiffre. Le déchiffrement de cette dépêche par le commandant Bazeries a en même temps permis de constater que le petit
chiffre de 1691 ne comportait que 367 groupes alors que le grand en employait 587." The petit chiffre was thus the
garrison-commanders' companion of the Grand Chiffre (p. 272: "spécialement affecté à la correspondance avec les
gouverneurs, intendants, commandants de place"), **367 groups**, which matches the observed maximum of 366. The annex
prints only the Grand Chiffre tables (pp. 273 ff.); no petit-chiffre table and no word of the letter's plaintext
appear anywhere in the 338 pages (searched for Feuquières, Pignerol, Veillane, petit chiffre, 25 janvier). So the
book confirms the reading existed and leaves it where Tomokiyo said: in Bazeries' papers. Those would be at the
Service historique de la Défense (Vincennes), either among his own papers or as pencil decodes on the Catinat
volumes he worked from (Archives du dépôt de la guerre, vols. 1032-1099 are the ones the book cites).

Also checked and negative: no clear copy or paraphrase of the letter anywhere in the three volumes of the 1819
Mémoires (full OCR searched for Veillane, Feuquières, chiffre); the 1845 Lettres inédites print Catinat's side of the
exchange (12 and 19 Jan) but no Feuquières letter of January 1691; Bazeries' papers are not online.

## Files

| file | purpose |
|---|---|
| `ciphertext.txt` | corrected transcription, with the three collation notes |
| `img/` | page images of pp. 283-284 from the BSB IIIF server, and crops |
| `louis1676.jpg` | Tomokiyo's partial table of the 1676 Louvois two-part code, the design comparison |
| `control_plain.txt`, `make_control.py`, `control.txt`, `control_key.txt` | matched synthetic control |
| `solver.py` | the solver (n-gram objective) |
| `run_real_*.txt`, `sweep_control.txt`, `seed_test.txt`, `solver_w.py`, `sweep_control.py`, `seed_test.py` | run logs and the two calibration harnesses |
| `masque_de_fer_1893.txt` | OCR text of Burgaud and Bazeries 1893, from the Gallica PDF (PDF itself not tracked) |
| `catinat1702_1.txt` | Tomokiyo's frequency table of the 1702 Catinat letter (43 % of 591 tokens below 100, 50 low groups: the same design) |

**Update 16 Sept 2026:** the Grand Chiffre letters of t. II pp. 295-342 (12,362 groups) are now decoded in full in `../catinat1691/`; see its NOTES.md and docs/catinat1691.html.

## Verification 5, 23 Oct 2026

Plain-bar check (French 1690-91; the word list knows the period spelling). The reading bodies are now cut out of the
decryption files: `texts/feuquieres1691_reading.md` and `texts/herleville1690_reading.md`. The d'Herleville letter
scores plain 0.667, explicit 0.833 (the misses are Mondevis, razer and the bracketed letters the cipher lacks) and has
its printed contemporary translation: keeps read. The Feuquières letter scores 0.545 on both measures (6 of 11
sentences): the five failing sentences carry three to six unread singleton groups each. The sense of the letter is
clear, but it is under the bar: **decoded, not read**. fraction_read 0.975 -> 0.304 (183 of 601 groups), class read ->
read in part.

## Remaining gaps

- Feuquières to Catinat, 25 Jan 1691: decoded, not read (0.545); groups 9, 19, 54, 122, 132, 194, 257, 271, 292, 333, 353 unread - blocker: no-key-material; each occurs once or twice, in no other text of the petit chiffre; the original (SHD A1 1079) is not digitised

## Escalation

- [x] siblings: the d'Herleville letter of 1690 in the same code found and used (Sept 2026); no third letter known
- [x] clear-pages: the 1819 Mémoires print no translation of the Feuquières letter; Feuquières' own Mémoires give the plan, not the text
- [x] known-keys: Bazeries' Grand Chiffre table gives the design only; the petit chiffre table is not printed
- [x] print: 1819 Mémoires de Catinat t. I-III searched (hOCR) for further petit-chiffre text
- [x] key-rebuild: 167 of 179 groups from the two letters (key_petit_chiffre_1690.tsv)
- [x] retry: re-read 23 Oct 2026 (v5); the original at the SHD (A1 1079) could settle printing slips but is not online


## Verification 14 Nov 2026 (Brice Dudout, with Claude Opus 5.5)

Re-read of the open passages of the Feuquières letter on the MDZ page images (`img/t2_0317.jpg`, `img/t2_0318.jpg`):
the groups around every gap (lines 6, 7, 9, 10, 12, 22-23 of p. 283; lines 2-7 of p. 284) were read again on the page
image, one pass at page resolution: they agree with `ciphertext.txt`; no printing slip found by eye. Then context work on the gaps, with the values carried through both letters:

| group | was | now | evidence |
|---|---|---|---|
| 241 | vous? | **me** | three contexts, all better with *me*: "que je **me** disposois", "les quatre-vingts maistres que vous **me** demandez" (Catinat's memoir of 19 Jan asks Feuquières for the horse; the old reading needed a supplied *[vous]*), "dont l'un **me** conduit". 316 = me already (*vous me faites*): a second homophone |
| 54, 257 | unread | po, so (probable) | "que je me di-s-**po-so**-is", *disposois*; 280 = is is sure (*reçois, sçais, trois, endrois*). 257's second context (*Javan et ta 132 257 l*) does not read with *so*: kept probable |
| 145 | go | go (unchanged) | sure from *dra-go-ns*; in "disposois 145 exécuter" the sense wants *à*: a clerk's or printer's slip, shown as supplied [à] |
| 194 | unread | null (probable) | "ce _ cy" = *cecy* is complete without it |
| 333 | unread | et (probable) | "tout prest, **et** qu'on ne pense"; "des Trois Couronnes, **et** l'autre aux maisons"; third homophone of *et* (258, 341) |
| 353 | unread | par | "J'attaqueray **par** deux endrois" |

Also: *doivent* (214 do i 150 ve 263 nt) and *dès* (237) are decoded, not supplied; `342 103 190` (closing) and `249 86`
are the key's nulls and are left out of the reading body. Key: `key_petit_chiffre_1690.tsv`, SHA-256
28de3e9662c35c5ea9e0f103d109786b3c5db6c7db186fcd3834887c97b817f3 (frozen before any count).

**No measurement.** No portion of this code was left unseen: the two known letters (601 groups) were both used to build
the key, so a held-out test (≥ 150 groups, 200 shuffled keys) is impossible. The new values rest on context only.

**Count (v10 `share` rule, `texts/feuquieres1691_reading.md`):** 176 words, 14 holes, read_share **0.926** (it was
0.875 on the 23 Oct reading: 168 words, 24 holes). Still under the 95 % bar: **read in part**. Groups still open:
9, 122 (×2), 19, 132, 292, 271 (and 257's second context). Conjectures not used in the reading: 19 = *poste* or
*quartier*; 292 = *qui*; `317 183 271 110 200` after *et sur tout* may hide *[toutes] choses* (271 = cho) but that
would make 317 *es*, against *m'escrire*/*m'eschaper*; *Javan et ta-132-so-l* may hold a second road name (the memoir's
Trane) or *estant ...*: none fits the groups cleanly.

**Neighbour checked:** the Catinat letter of 15 Sept 1702 (`../catinat1702`) has the same design but another
assignment (Norbert Biermann 2016; our test of this 1690 key on it, Nov 2026: rank 122 of 200 shuffled keys); it gives
no value for this code.
