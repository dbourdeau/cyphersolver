# The Grand Chiffre letters of 1691 in the Mémoires de Catinat — Louvois and Louis XIV to Catinat, July–September 1691

**Status: read (16 Sept 2026).** Seven despatches printed in figures in *Mémoires et correspondance du maréchal de Catinat*
(Paris, Mongie, 1819), t. II, Pièces justificatives, pp. 295–342, decoded in full with Bazeries' reconstruction of the
Grand Chiffre de 1691 (`../feuquieres/grand_chiffre_1691.tsv`, transcribed from *Le Masque de fer*, 1893). 12,362 groups.
Two of the seven were printed in clear by Bazeries (8 July, 19 August) and serve as controls: our decode of the OCR'd
figures agrees with his clear text at 98.1 % and 99.1 % of characters. The other five, about 9,700 groups, have never
been printed in clear. The largest, Louis XIV's letter of 14 September 1691 (6,331 groups), is the King's decision to
pull the army of Piedmont back over the Alps at the end of the campaign and fight a defensive war in the passes in 1692.

Written up on the site: `../../docs/catinat1691.html`. This is the by-product noted in `../feuquieres/NOTES.md` §2.

## 1. The documents

| id | letter | t. II pages | MDZ scans | groups | printed in clear before |
|---|---|---|---|---|---|
| L1 | Louvois → Catinat, Versailles, 8 July 1691 | 295–299 | 329–333 | 1,074 | yes, Bazeries 1893 pp. 42–46 (the Bulonde arrest, "avec un masque") |
| L2 | Louvois → Catinat, Versailles, 9 July 1691 | 299–304 | 333–338 | 1,611 | opening 130 groups only, Bazeries pp. 47–48 |
| L3 | Louis XIV → Catinat, Versailles, 19 Aug 1691 | 305–309 | 339–343 | 1,259 | yes, Bazeries pp. 292–300, from the minute at the Dépôt de la guerre |
| L4 | Louis XIV → Catinat, 24 Aug 1691 | 309–315 | 343–349 | 1,193 | one passage (Casale, Crenan) Bazeries p. 266 |
| L5 | Louis XIV → Catinat, 29 Aug 1691 | 315–318 | 349–352 | 492 | no |
| L6 | Louis XIV → Catinat, Versailles, 6 Sept 1691 | 318–320 | 352–354 | 402 | no |
| L7 | Louis XIV → Catinat, Fontainebleau, 14 Sept 1691 | 320–342 | 354–376 | 6,331 | no |

Scan number = printed page + 34. The 1819 editor (Le Bouyer de Saint-Gervais) printed the figures as he found them in
Catinat's papers, with the clear passages the clerk had left in clear, and confessed he could not read them
("Nous avons deux grandes dépêches en chiffres de M. de Louvois, dont il a été impossible de trouver la traduction",
quoted by Bazeries p. 57). Bazeries (p. 55) states that apart from the 19 August letter, which exists in clear at the
Dépôt de la guerre (vol. 1041 f. 362), "ces dépêches n'ont pas été enregistrées". *If that is right, the 1819 print is the
only surviving text of the other six, and this reading is the only one there is of five of them.* Not checked against
the SHD inventories.

Bazeries, *Le Masque de fer* (1893), is built on these letters: he reconstructed the code from them, printed the table
(pp. 280–289), the 8 July letter in clear as his introduction and pp. 42–46, the start of 9 July, the 19 August letter
in cipher and clear as his "preuve de l'exactitude", and quoted the Casale passage of 24 August. He did not print the
rest. His interest was the one sentence about Bulonde; the strategic content of August–September went unused.

## 2. Method

1. **Text.** MDZ hOCR of every page (`hocr/<scan>.html`, from `https://api.digitale-sammlungen.de/ocr/bsb10720287/<scan>`),
   page images from the IIIF service (`img/t2_<scan>.jpg`, `fetch_pages.py`). The hOCR carries word boxes but no
   confidences.
2. **Tokenising** (`extract3.py`). Words are read from the hOCR in order; specks (boxes under 30 px high containing only
   digits or points) are dropped, which removes the stray "1"s the OCR planted in the margins and that decode as the
   group 1 = *Passage*; the running heads and the "T. II. 20" signature marks are dropped; show-through glyphs the OCR
   rendered as Greek, Cyrillic or Arabic letters are stripped from the token. Dates written in clear next to a month name
   are kept as clear.
3. **Letter boundaries.** The printed headers ("A Versailles le 8 juillet 1691. Monsieur", "LOUIS. 24 août 1691. M. Catinat")
   and the editor's footnote markers "(n) Page NN" are recognised; the cipher ends where the editor turns to the 1676
   table ("Pour rendre la traduction de ces chiffres plus facile…", p. 342). The 1676 table on pp. 343–352 is the older
   *chiffre à chiffrer* of October 1676, not the 1691 code, and is not used.
4. **Decoding.** Each group is looked up in Bazeries' table (587 entries, 91 blank). The decoded units (letters, CV
   syllables, word stems, whole words, nulls, the CANCEL group) are concatenated between nulls and word-segmented by a
   dynamic-programming segmenter (`segment.py`) over a lexicon built from the three 1819 Catinat volumes, Rousset's
   *Histoire de Louvois* IV, Feuquières' *Mémoires* and Bazeries 1893 (17,000 forms; i/j and u/v merged for the search,
   restored afterwards from an unmerged lexicon). The table's ambiguous units (I-J, U-V, Ue-Ve, Ia-Ja…) are resolved the
   same way. The segmentation is a reading aid: `letters/L*.txt` carry the segmented reading and, below it, the groups
   exactly as printed, with page breaks.
5. **Validation** (`validate.py`). Character-level alignment (difflib) of our reading against Bazeries' clear text after
   normalising accents, i/j/y and u/v: 8 July 2,640 of 2,690 characters (98.1 %), 19 August 3,204 of 3,233 (99.1 %).
   The differences are of three kinds: (a) single groups misread by the OCR (e.g. 26 *Vous* read as 24 *Le*; 8 *E*
   read as 587 *Moins*), about one group in seventy; (b) places where Bazeries' clear text does not follow the figures
   as printed (1819 misprints he corrected silently, or table entries like 64 *Da* and 300 *R* where his text has *l'*
   and *ssi*), unresolved; (c) the clerk's "Persuad (ou) Asseur" and "Cependant" entries, which Bazeries renders freely.
6. **Image check** (`verify_crops.py`). Every stretch whose decode the segmenter could not resolve into lexicon words,
   plus every group outside the table's range, was cropped from the page image with its neighbours (137 clusters,
   `crops/sheet_*.png`) and read by eye. Seven OCR errors found and recorded in `corrections.tsv` (3111 → 311; 50g → 509;
   two pairs of run-together groups split; 917 → 91; 00 → 99; 124.0 → 124) and three dates. Almost every other flagged
   stretch was correctly OCR'd and is either seventeenth-century spelling (*jettassiez*, *obligiez*, *bleds*) or a
   table gap. Six groups are printed above 587 in the 1819 edition itself (p. 312: 654; p. 314: 593, 855; p. 319: 942;
   p. 339: 854; p. 342: 595) and stay flagged `[n!]`; one glyph on p. 326 is damaged (OCR 150, could be 170 or 172).

## 3. What the letters say

**L1, Louvois, 8 July.** As Bazeries printed it. The King is surprised the news of Coni came by the post and not by
courier; wants the author of the general assault on the outworks named; Bulonde to be arrested and taken to the citadel
of Pignerol, shut in a room at night and free by day to walk the ramparts "avec un masque"; fortify Carmagnole; what
does Catinat intend at Poirin and Quiers; destroy Quiers and Villeneuve d'Ast if they cannot be held over winter; la
Hoguette sends four battalions and fifteen squadrons; grain to Nice countermanded; up to a million livres to Casale.

**L2, Louvois, 9 July** (new beyond the first 130 groups). The more the King reflects on Coni the more he is touched,
for the reputation of his arms and for the obstacles the place will put to winter quarters in Piedmont; a siege with the
whole army is no longer possible. Two tasks: fortify Carmagnole so the enemy "n'osent le regarder", and destroy every
place the enemy could hold in winter to trouble the communication with Casale and Pignerol: Villeneuve d'Ast and Quiers
are of that kind, and when marching to change the garrison of Casale Catinat "les devriez brusler absolument",
sparing the churches as far as may be; castles that could pinch his quarters or ease the Turin–Asti road, the same;
and all this "de manière qu'il ne paroisse point qu'elles vous aient esté prescrites". Seize Bene if practicable;
burn Carignan if the enemy could occupy it. Seek a battle before the Germans arrive, avoid one after, to let them fall
sick and waste "faute de payement"; not a prescription to retire, but to post and entrench so that an attack comes at
the enemy's disadvantage. The King prescribes nothing, "vous ouvre seulement des vues". Send Vins back to the Provence
frontier and use his two battalions in the rear garrisons, not Pignerol, where two Irish battalions already are. Press
the engineers for a plan of Carmagnole with the water levels. The harvest being nearly in, oblige the peasants to shelter
their grain in the King's garrisons, with commissaries from Catinat and Bouchu to hold the governors to it; Bouchu to
send weekly states of what comes in and what is sold. Monsieur de Savoie's talk about the negotiations "mériteroit
bien" two thousand bombs into Turin, and breaking the bridge of Turin would be very useful, but these again are views,
not orders. The Germans cannot be in Piedmont before 15 August, march "avec une répugnance infinie", and many desert.
Fill Carmagnole with forage. Troops going to Casale might pass by Montafia and burn there, as the Suze garrison did at
Pianezza.

**L3, Louis XIV, 19 August.** As Bazeries printed it: Carmagnole's weakness, Caraffa's foresight in stocking grain,
Chamlay sent out with the King's full intentions, live as long as possible where it is best for the service, pull the
grain of Saluces, Savillan and Fossano into Carmagnole or Pignerol.

**L4, Louis XIV, 24 August** (new except the Casale passage). Chamlay is charged to explain the King's thoughts on
every course open "dans la suite de cette guerre"; Catinat and he are to weigh together what is practicable, knowing
the state of the King's affairs, of his negotiations, of the country and of the enemy's strength. Will the enemy march
into Savoy, or unite on the Turin side to make Catinat consume the forage and recross the mountains first, leaving them
the whole country between Turin and Pignerol; the King views with pain whatever would force him out. The negotiation at
Rome makes it very desirable to prolong the army's stay beyond the mountains. Casale: Barbezieux writes to Crenan to
palisade town and citadel, money for eighteen months, grain; the garrison should be stronger in cavalry; artillery
officers and gunners wanted, and Crenan to train soldiers to handle the guns. Carmagnole: since Chamlay's memoir the
King no longer finds Catinat so resolved to abandon it and hopes he and Chamlay will resolve to keep it. Some at court
believe that with Villefranche fortified and a large infantry corps in it, and Saluces, Savillan and Fossano garrisoned,
the army could winter in Piedmont; the King does not tire of raising it, but Catinat is not to let the King's wish
override his own judgement of what serves best. Pignerol's safety is "le premier objet" in every plan; if next year is
to be defensive, then precautions and works where needed, the Suze side well guarded, the Savoy passes garrisoned, the
small towns of Dauphiné and Provence closed. Étapes for the Maurienne and Tarentaise approved. The King would greatly
wish Catinat could take Coni at the end of the campaign; if he thinks it possible, prepare the artillery and supplies.

**L5, Louis XIV, 29 August** (new). The chevalier de la Farre has forwarded proposals for a treaty with the people of
Mondovì; the King thinks them good and would grant what they hold, but the army is no longer in a state to take
quarters there, so the treaty can only serve to sound those people and profit later; Catinat may conclude as he judges.
The enemy's march toward Savoy: the King doubts they can attempt anything without preparations, but the resident at
Geneva reports they have asked the city for passage (which will be refused) and would go by the Valais into the
Chablais; la Hoguette is warned. It would be vexing if an enemy entry into Savoy put the army out of state to take
Coni at the end of the campaign. La Hoguette keeps all his troops and the régiment royal at Suze; the King will not
prescribe Catinat's movements; but do not go far from Carmagnole for supplies, and if the enemy approached Pignerol
for some "algarade" the King would be angry, but Catinat knows the weight of things and will go to the most pressing.

**L6, Louis XIV, 6 September** (new). If anyone is to be sent to Casale this winter the only road is by Genoa, and it
is not safe. The King is not sorry at Catinat's decision about the passes, having been pained to see so few troops
guarding them. Larray has sent an Irish battalion to Briançon fearing the Barbets (the Vaudois) meant to seize the town,
and has told Bachevilliers to redouble his care. Pleased with the prince d'Elbeuf. If Catinat is to pass the Po, do it
before the enemy moves toward him, and so that if they came at Pignerol he could trouble their plans; right to withdraw
the sick from the abbey near Pignerol. Chamlay has arrived.

**L7, Louis XIV, 14 September, Fontainebleau** (new; 6,331 groups, about twenty printed pages). Chamlay has reported at
length on his mission and on his conferences with Catinat. The King has seen "avec peine" that the upshot is to withdraw
the army of Piedmont over the mountains at the end of the campaign for want of quarters and subsistence; that
Carmagnole, on Chamlay's description, cannot be perfected before winter and its garrison would be lost; and that, the
difficulty and cost of subsisting beyond the mountains being what they are, it seems better not to send the army back
next year but to fight a defensive war that covers the frontier places of Piedmont, stops the enemy in the Alps and
makes them "se consommer inutilement dans leur propre pays". He has weighed the prejudice: the enemy masters of Italy,
the allies and neutral princes forced to declare against him, Casale lost "de veue" and as good as in enemy hands, the
reputation of his arms damaged among enemies and allies alike, who would take it for weakness. Against that: the near
impossibility of subsisting in Piedmont without Turin; a country "fort estroit et extrêmement couvert", cut by rivers
and torrents that swell in hours and cannot be bridged with boats; the distance of Casale; the sickness of the troops
every campaign from the climate, the fruit and the water, with no hospitals to hold them; the enemy's freedom to engage
or not behind the Doire and the Po and their fixed bridges. On the other side, Catinat's plan for the defensive: troops
on the frontiers of Provence, Dauphiné and Savoy at the chief cols, on the heights of Saint-Pierre near Pignerol and
about Suze; cheaper subsistence, fewer sick, near certainty the enemy cannot pierce the mountains; their embarrassment
before Casale for fear the army returns; and the surplus of cavalry, left on the Saône or in Franche-Comté, that can be
sent to Germany, either to recall the Germans from Piedmont or to gain on them there, while Monsieur de Savoie must
either keep the allied army idle in Piedmont, to his country's ruin, or let it go and see the French come back. "Après
toutes ces discussions… j'ay comparé les inconvénients et les avantages d'un parti avec ceux de l'autre… et je me suis
déterminé à préférer le parti solide à l'honorable": recross the mountains at the end of the campaign, do not return in
1692, defensive war in the cols of the Alps and on the heights of Pignerol and Suze as Catinat proposes.

That decided, the orders. Prolong the campaign as long as possible without ruining the army, and give up Carmagnole as
late as possible: both are essential to the negotiation now being made with the Pope and other princes and states of
Italy, whose success would extricate the King from Casale "et mesme peut-estre de la guerre de Piedmont". The enemy and
the Italian powers must not learn that he means to quit Piedmont for good; the works at Carmagnole are to go on, pushed
"avec un peu moins de vivacité et de dépense". When ordered to quit, carry off the most valuable effects, use the
cavalry to carry grain on the crupper to Pignerol, the wagons for guns and munitions, throw the rest into the water,
tear up the fortifications, burn the palisades, gates, hay and grain. Hold Carmagnole and stretch the campaign to All
Saints or even Saint-Martin, to see clearly how the Italian negotiation stands. The enemy may think of bombarding
Pignerol, which "me donneroit beaucoup de mortification en présence de mon armée": prevent it while there, and secure
the munitions for after the army has gone. Guard the valleys of Pragelas and Pérouse for the Briançon–Pignerol road;
watch the Val d'Aosta side of Savoy. After recrossing, attack Coni at the end of the campaign, which the season will
allow since no enemy will be on his hands and the infantry can be covered in the villages; examine the heights of
Saint-Pierre and of Suze closely and report. Orders go out to bring the artillery and stores for the siege of Coni to
Lyon and Grenoble, to fortify the towns and castles of the Provence, Dauphiné and Savoy frontiers and above all
Briançon, against the valleys of Luzerne, Saint-Martin and Angrogne; a magazine of munitions at Grenoble; winter
quarters by Catinat's memoir, though feeding the troops meat as he and Bouchu propose looks hard. A final recapitulation,
and a caution about the retreat itself: separate with such precaution that the enemy can attempt nothing; la Hoguette
to see that neither food nor troops enter Coni.

## 4. What remains

* Six groups misprinted above 587 in 1819 and one damaged glyph (p. 326) are unread; about a hundred groups fall on
  entries Bazeries left blank (`[n?]`), most of them rare syllables, and read from context.
* The OCR error rate measured on the two control letters is about one group in seventy. The image check caught the
  errors that break the French; substitutions that leave plausible French (24/26, 8/587) survive at that rate, so a
  reader quoting a passage should check it against `img/` (the group boxes are in `groups.json`).
* Bazeries' table is a reconstruction. Where his clear text of the 8 July letter departs from the printed figures
  (64 *Da*, 300 *R*, 5 *Regiment*, 587 *Moins*), the question is whether the 1819 print or his table is wrong; only the
  originals at Vincennes would settle it.
* Whether the minutes of the 9 July, 24 and 29 August, 6 and 14 September letters survive at the SHD (Bazeries says
  they were not registered) is not checked. Rousset's *Louvois* and Catinat's biographers would show whether the
  substance of the 14 September decision was known from other papers; a quick search of Rousset IV for "parti solide"
  finds nothing, but that is not a study.
* The word segmentation is heuristic and leaves some joins and splits wrong (*cham lay*, *jesuis*); it does not affect
  the group-level decode.

## 5. Files

`extract3.py` (tokenise, split, decode, segment; writes `letters/L1..L7.txt`, `groups.json`, `letters_summary.json`),
`segment.py` (lexicon and DP segmenter), `validate.py` (against Bazeries' clear texts), `verify_crops.py` (suspect
clusters and contact sheets), `corrections.tsv` (OCR fixes keyed by scan and box), `fetch_pages.py`, `hocr/`, `img/`,
`crops/`. Earlier drafts `extract.py`, `extract2.py` kept for the record. Table and corpora in `../feuquieres/`.

## Verification 5, 23 Oct 2026

Plain-bar check (French 1691; the word list knows the period spelling). L2, L5 and L6 had been scored on the
segmenter's unpunctuated runs in `letters/L*.txt` (plain 0.50, 0.579, 0.562). The word division was re-done by hand on
the decodes, with punctuation, clear passages in ⟨ ⟩ and group values unchanged; groups whose value does not fit the
sense are marked [?] (L2: homme, parti, batails/Montcas, reisson, sepaoit, povaz, fois, de meur; L5: "resolus
[?intention] [?marquée] [?r] le passage"; L6: "tres bon [?honneur]", "je [?m'en leve]"). New files
`letters/L2_reading.md`, `L5_reading.md`, `L6_reading.md`: plain 0.833, 0.906, 0.724; explicit 0.939, 0.938, 0.862.
All three keep read. The doubtful groups are a pointer for an image check of the 1819 print (OCR or printer's slips).


## Read share over cipher words only (16 Nov 2026)

README Conventions, 16 Nov 2026: the read share counts the words written in cipher.

How the cipher was separated: the 1819 print gives some passages in clear, and `letters/L*.txt` ("Groups as printed")
marks every clear word in `<angle>` brackets. Each run of clear words was found in the reading (letters compared without
spaces, accents or punctuation, so that the word division of the reading does not matter) and left out. The L5 and L6
readings also mark the clear passages in ⟨ ⟩, which give the same split. The holes in the clear text, the dates
[1er!] (L1), [?g] (L3) and [28?] (L6), are not counted. Holes by words with the `v2_score` rules; a word with an
apostrophe is one word. Script: `python research/reading_audit/r23_angle_split.py catinat1691`. One run is removed
by hand: L3's clear "Vous me parlez dans une de vos lettres du 13" (9 words), which the script misses because the
reading has [?e] after *13*; that [?e] stays a cipher hole.

| letter | before (whole letter) | after (cipher words) | state |
|---|---|---|---|
| L1, 8 July | 0.983 | 0.982 (532 of 542) | read, unchanged |
| L2, 9 July | 0.982 | 0.981 (757 of 772) | read, unchanged |
| L3, 19 Aug | 0.981 | 0.979 (608 of 621) | read, unchanged |
| L4, 24 Aug | 0.979 | 0.966 (564 of 584) | read, unchanged |
| L5, 29 Aug | 0.985 | 0.973 (249 of 256) | read, unchanged |
| L6, 6 Sept | 0.973 | 0.963 (184 of 191) | read, unchanged |
| L7, 14 Sept | 0.968 | 0.966 (2,926 of 3,030) | read, unchanged |

All seven stay over the bar; the class is unchanged. The group figures (Bazeries' controls, 98.1% and 99.1%) are
unchanged.
