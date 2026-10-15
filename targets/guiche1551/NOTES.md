# La Guiche (Rome) to Montmorency, 22 Nov 1551: catalogue no. 10 (part)

Catalogue entry 10 ("La Guiche (Rome), Noailles (Venice), Seure (Lisbon)", class C) grouped three ambassadors'
letters in two BnF recueils. Worked 2026-09-21 (one session, Claude Opus 5). Split on 14 Oct 2026 from the joint
entry under the one-key rule: Noailles 1558 (`../noailles1558/`) and Seure 1558 (`../seure1558/`) are different
ciphers, each with its own page; see section 2.

Outcome: **La Guiche read in part (new reading, key recovered ciphertext-only)**: 429 of 431 tokens have a value
(measured, 14 Oct 2026); the struck-through opening reads only in fragments.

## 1. La Guiche → Montmorency, Rome, 22 Nov 1551 (fr. 3138 no. 22)

Gallica btv1b90601662, view 65 (f. 60v–61r; the cipher is all on f. 60v, signature "Claude de la Guiche e. de
Mirepois" on f. 61r). About 13 lines of cipher set inside clear text. The first two lines are struck through by
the writer. No decipherment on the leaf, the next leaf or in the margin.

- Transcription: `guiche_ct.txt`, 406 signs, 22 distinct (sign codes in the file header). Made from full-resolution
  crops of each line.
- System: a simple substitution, one sign per letter, no word division. 22 signs map onto the 22-letter alphabet
  of the period. `3`=e is 16% of the text.
- Attack: `solve1.py` (permutation annealing with swap moves, `fr-1530-despatches` 5-gram, no spaces, 16 restarts)
  gave "le conte sainctefiore est mal satisfaict" on its best restart. The first free many-to-one annealer
  (`solve.py`) collapsed onto i/x and failed. `refine.py` then fixed the confirmed signs and re-annealed the others.
  Corrections were made by hand from context: F=qu ("que facilement"), 8=p ("party pour", "pourroit"), P=y ("avec
  moy", "roy"), A=v ("vous", "service").
- Key: 3=e t=r #=i e=u Q=t B=s r=a f=d d=n 4=o o=o (second o) p=c W=l (also g in "Diego") F=q D=m P=y A=v g=f
  8=p X=g; c and 5 (1–2 occurrences) are unassigned.
- Reading (`reading_raw.txt`, then the text below with the clear words around it). Normalised, [?] = unsure:

  > [struck: Dom Diego (a faict) constituer prisonnier en ce(ste ville) … un Siennois … croy que … est au dit …]
  > le procès duquel j'ay trouvé moien de veoir, *affin de informer led. Sr cardinal du contenu en icelluy pour
  > selon cela mettre tel fondement qu'il advisera* : … l'am[bass]adeur de Senes qui estoit icy, lequel est party
  > pour s'en retorner a Senes avec Dom Diego. … Le conte [de] Sainte Fiore est mal satisfaict de […], et que
  > facilement se reduiroit au service du roy … *[clear: de la Seance]* … le service … *Car ledict personnage qui
  > estoit icy tractant* avec moy la faire du sieur +arna+e a dorne[?] *la responce qu'a…* … vous informer du …
  > que le roy pourroit avoir du dict sieur +arna+e et aux [?] … des conditions qu'il demanderoit.

- The subjects are the Sienese envoy leaving Rome with Dom Diego (Diego Hurtado de Mendoza, imperial ambassador and
  master of Siena, a few months before the Sienese rising of July 1552), and the Count of Santa Fiora (a Sforza,
  the pope's relation) being discontented and ready to come over to the king's service, on conditions. This is the
  Parma war winter.
- Open: the name "sieur +arna+e" (signs `t r t d r t 3`; the `t` there may be a plain + distinct from the barred
  sign read r); signs c and 5; the struck-through first two lines, which read only in part. Grade: key C (secure
  for the 15 signs above), text M where marked.
- Prior art: web search found no edition of this letter; no decipherment in the volume.

## 2. Noailles 1558 and Seure 1558: split off

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 10 grouped three letters in
three different ciphers. Noailles's Venice letter of 13 Nov 1558 (fr. 3151 no. 33, another symbol alphabet, with a
marginal decipherment of the time) is now `../noailles1558/`; Seure's six Lisbon letters of Dec 1558 (fr. 3151 nos.
39-44, homophonic with numeral codes) are `../seure1558/`. Each is a different cipher with its own page. This entry
is La Guiche's letter only.

## Files

- `guiche_ct.txt`: La Guiche transcription. `reading_raw.txt`: decryption per line with the key above.
- `solve.py` (failed free annealer), `solve1.py` (permutation annealer), `refine.py`.
- Images: `research/gallica_sweep/btv1b90601662/`, `research/gallica_sweep/btv1b9059865k/`, `research/gallica_sweep/hi/` (git-ignored).

## Remaining gaps

- La Guiche f. 60v: the four-dot code sign (::) after 'mal satisfaict de' and sign 5 - blocker: open-codes; :: occurs once (conjecture 'l'Empereur', grade I), 5 only in the struck lines; the name is read 'Barnabe Adorne' (30 Sept 2026)
- La Guiche f. 60v: the two struck-through first lines - blocker: illegible; struck through by the writer; read only in part

## Escalation

- [x] siblings: leaf, next leaf and margin of La Guiche checked; fr. 3138 view 70 has Morvilliers' 1549 letter with its decipherment (a different key)
- [x] clear-pages: La Guiche has no decipherment on the leaf, the next leaf or the margin
- [n/a] known-keys: every letter sign has its value from the ciphertext-only key; the open pieces are a one-off code sign (::) and the writer's struck lines, which no letter key of the period would supply
- [ ] print: not done — only a web search; Ribier, Lettres et memoires d'estat (1666), not grepped for this letter (Gallica and HathiTrust refused this session's requests on 14 Oct 2026)
- [x] key-rebuild: permutation anneal (solve1.py) plus refine.py with fixed signs; qu, p, y, v fixed by context
- [x] retry: the second pass of 30 Sept 2026 re-read every doubtful sign on the image with the extended key (+ = b, ff c = ss, the L2x run, X -> B in 'service'), see Corrections

## Corrections

- **30 Sept 2026 (reported while quotations were pulled for Lasry's list; checked on `guiche_ct.txt`,
  `reading_raw.txt`, the key above and the view 65 image, main checkout `gallica_sweep/hi/g65full.jpg`).**
  (a) The site's portrait strip named the recipient as Henry II. The letter is to Montmorency: the close on f. 61r is
  "Monseigneur, je prie Dieu vous donner ...", and the king is in the third person ("au service du roy"). The
  guiche1551 recipient in `docs/_portraits.json` is now Anne de Montmorency (`portrait_anne-de-montmorency.jpg`, the
  file already used for gramont1529, raince, rome1536), and the strip on `docs/guiche1551.html` was regenerated to match.
  (b) The reading had "la m… de ceux de Sienes qui estoit icy". L3 `W r D t r F c r f 3 e t f 3 B 3 d 3 B` gives
  "lamraq?adeur de senes", with no "ceux": the text is "l'am[bass]adeur de Senes qui estoit icy", the Sienese envoy
  that "lequel" then refers to. The bracketed signs `t r F c` give r a q and an unassigned sign with the key; "bass"
  is inferred from context (grade I). The clear line just above this run ends "... les propos que Mignet[?] a tenus a",
  which fits. Both "Sienes" of the sentence are now "Senes", as deciphered.
  (c) The page had "mal satisfaict, et que"; L5 ends `f 3 3 Q` "de et", so it now reads "mal satisfaict de …, et que",
  as here. On the image a four-dot sign (::), not in `guiche_ct.txt`, stands between "de" and "et"; not deciphered,
  perhaps a code for a name.
  Leads seen while checking, not acted on (the key, counts and grades are unchanged): (1) after "qu'il advisera" the
  image has a cipher run of 24 signs that is not in `guiche_ct.txt`; in the file's codes `r W r 8 t r Q # F e 3 F e r e
  3 B 3 d Q 3 d f e`, it gives "a la pratique qu'aves entendu". (2) The sign transcribed `t` at the fourth place of L3
  and in "+arna+e" (L9, L11) is a plain cross, distinct from the barred cross that is r: read as b it gives
  "l'ambassadeur" and "du sieur Barnabe Adorne" (L9 "... a dorne"), perhaps Barnaba Adorno. (3) `F c` stands for "ss"
  in both places it occurs: "l'am[bass]adeur" (L3) and L12 `r e F c #` "au?i", i.e. "aussi" where the page has "aux [?]".
  These need a re-transcription pass.

- **30 Sept 2026, second entry (filling the gaps in the quotation for Lasry's list; image `gallica_sweep/hi/g65full.jpg`,
  line crops at full resolution).** The three leads above were checked and applied.
  (1) The 24-sign run after the clear "qu'il advisera" is now `L2x` in `guiche_ct.txt`
  (`r W r 8 t r Q # F e 3 F e r e 3 B 3 d Q 3 d f e`); with the key unchanged it reads "a la pratique qu'aves
  entendu" (grade H key / C reading: every sign has its established value).
  (2) The plain cross (no bar), new code `+`, is b: L3 "l'ambassadeur" (`W r D + r F c r f 3 e t`), L9 and L11
  "Barnabe" (`+ r t d r + 3`, the barred cross in the middle is r, as in "sieur" just before and "Adorne" just after).
  The name is "le sieur Barnabe Adorne", presumably a Genoese of the Adorno family, not identified (grade M).
  (3) `F c` = ss in both places (L3 ambassadeur, L12 "aussi"); c is no longer unassigned.
  (4) L10: the image has the barred p (s) where the transcription had X, so "du service" (the v of service is written
  with the sign read f elsewhere, and "informer" has the c-sign for f: look-alike slips, read by context, grade M).
  (5) The four-dot sign after "mal satisfaict de" is in the transcription as `:`. It occurs once, so it cannot be
  deciphered; it is a code for a person or power. Context gives a conjecture: "et que facilement se reduiroit au
  service du roy" means the count was then in someone else's service, and Sforza Sforza, count of Santa Fiora, had
  gone back into Charles V's service after Paul III's death (Treccani, Dizionario Biografico, "Sforza, Sforza").
  The page reads "mal satisfaict de [l'Empereur?]" (grade I); the Pope is the alternative.
  (6) The clear lines between the runs were read from the image: "... qu'il advisera [cipher] Et aussi pour dire aud.
  Sr cardinal les propos que Mignet[?] a tenus a [cipher: l'ambassadeur ... Dom Diego] Et pour ce que ledict Sr
  cardinal a commancé a vous escripre de ceste affaire, je m'en remettray a ce qu'il vous en escripra. J'entendz que
  [cipher: le conte Sainte Fiore ...]". The reading on the page now runs continuously from the Sienese envoy to
  Santa Fiora.
