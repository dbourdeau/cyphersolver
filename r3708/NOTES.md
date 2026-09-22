# Paris informant to the Nevers household, 6 June 1588: BnF fr. 3976 ff. 133-134 (DECODE R3708)

Catalogue entry "Unknown sender to unknown recipient", DECODE R3708 (6 Jun 1588, Non-decrypted, 3 pp., numerical).
Session of 22 September 2026.

Status: read. All 18 cipher runs read (226 of 230 signs certain, 98.3%, measured from `ciphertext.txt`/`reading.tsv`);
four signs read from context only; the code numbers are partly identified. The same informant's letter of 9 June
(f. 139, not on DECODE) was added the same day: 6 runs, 106 of 106 signs read by the key, every run matching its
contemporary interlinear gloss (`ciphertext_f139.txt`, `reading_f139.tsv`); its code glosses identify 10, 38, 98, 107.

## The document

* BnF fr. 3976 = Gallica `btv1b9060548h`. **f. 133r = canvas 223, f. 133v = canvas 224, f. 134r = canvas 225**
  (foliation checked on the leaves; canvas 227 = f. 135, the Paris échevins' letter of 7 June). Full resolution
  4895 × 6460 px. Crops in `img/` (git-ignored).
* Dated at the head "6 de Juin 1588" and at the foot "Ce 6. Juing a 10 heures du soir", signed with the same
  cipher monogram as ff. 62 and 131. Same hand and same cipher as f. 62 (R3705, read in `nevers1588/`) and f. 131.
* Three pages of clear French with **18 cipher runs** set into the text and bare code numbers
  (4, 9, 10, 11, 12, 23, 24, 25, 33, 79, 94, 102, 104, 105, 106). No decipherment on the leaves.

## Prior art

DECODE: Non-decrypted, no transcription. The key was already rebuilt here from the sibling f. 131 (glossed) and
f. 62 (`nevers1588/key.md`, 22 Sept 2026). No print of this letter found; not in Tomokiyo's Nevers page.

## Method

The `nevers1588` key applied unchanged read most runs at sight (Nevers, ligueurs, pardonne). The runs that did not
read at once were re-transcribed at native resolution and read in context. The key was confirmed and extended:

* ϙ (y with a cross below) = y, confirmed by **Montmorency** and **artillerye**.
* the 4 with a cross below = **z** (curez, bruictz; Pichena**z** for Pichenat). The old key had it as q.
* `[` (bracket-like sign) and the long J-like sign = n in "nommé", "conseil", "Nevers en court", "Nuilly";
  the long J-like sign = p in "prevost" (R12).
* z = a (Arsenac, Pichenat); 2 = a (La Cassine); 9 = r (artillerye, Nevers en court), h (Pichenat, blanche).
* o = u in "bruictz" (o is otherwise l).
* Underlined numbers inside a run are code numbers, as in the clear text: "au conseil de <9> et <106>".

## Reading

The runs in their clear context (`reading.tsv`, cipher in bold):

> Je suis tres marry qu'aiez pris en mauvaise part ce qui a esté escript a 24 [...] Mais parce qu'avant son
> partement il offroit a 11 de demourer s'il en estoit de besoing, on estimoit qu'il se portast encore mieulx qu'alors
> et par consequent sans peril de sa personne il pouvoit s'approcher de **Roy**. Or nous avions bien consideré que si
> **Nevers** alloit veoir 11 sans estre mandé d'affection, il y pourroit recevoir quelque pire traictement [...]
> Secondement, 24 se peult souvenir qu'estant a **La Cassine** 11 ne luy escripvoit qu'a force, et neantmoings apres
> qu'il fut venu il luy fit caresse et honneurs [...] Tiercement tout le monde desire **Nevers en court** beaucoup plus
> que l'on ne faisoit alors. Et non seulement **ligueurs** mais aussi les aultres [...] un bruit que 102 renvoye des
> deputez vers 11 avec charge [...] de le supplier que pour tesmoigner a 102 qu'il **pardonne** et n'a mauvaise
> volonté, il luy laisse pour 94 ou 4 ou 9 ou 24 a son choix. Ledit 102 n'a encore envoyé vers **Nevers** [...]

> Il n'y a que les **curez St André et St Benoist** qui font rage de **mutiner le peuple**. [...] Quant a l'eslection
> des prevost des marchans et eschevins, elle n'a esté aultrement faicte que je vous l'ay mandé, que j'avois entendue
> de **Pichenat**. [...] Mais comme vous scavez, ce ne sont gens d'estat, de sorte que **par ruses et faulx bruictz**
> on leur faict tousjours passer quelque carriere, car si tost que quelque chose a esté resolu en l'hostel de ville,
> **le prevost Chapelle** ne fault de rapporter le tout au **conseil de 9 et 106** pour adviser les moyens de rompre
> les deliberations qui ne leur plaisent, ou assistent tousjours **33 et de Bray, l'evesque de Lion, Nuilly**. L'on
> m'a asseuré neantmoings que ces jours passez 9 voullant faire sortir **l'artillerye de l'Arsenac** pour aller a
> **Corbeil**, l'un des eschevins, **nommé Cotteblanche, dist** qu'il ne consentiroit jamais que cela se feist sans
> permission du Roy.

> Quant a 33, j'ay perdu tout ung jour pour cuyder le veoir, mais il fut toute l'apresdisnée chez 105, qui est logé
> au logis de **Montmorency**.

This is Paris three weeks after the Barricades (12 May 1588): the new League municipality (La Chapelle-Marteau
prévôt, Cotteblanche among the new échevins) steered by Guise's council, the preachers Aubry (St André des Arts) and
Boucher (St Benoît), Pigenat (St Nicolas des Champs), Pierre d'Épinac archbishop of Lyon and the président de
Neuilly; Guise's siege of Corbeil (the town was held against the League in June 1588; f. 131 reports it surrounded
by Guise's troops) and Cotteblanche refusing the Arsenal's guns without the King's leave.

Code numbers, from context here and on ff. 62 and 131:

| code | reading | evidence |
|---|---|---|
| 11 | le Roy | glossed f. 131; "deputez vers 11", "sans permission du Roy" |
| 24 | the duc de Nevers | glossed "nevers" on f. 131 (read as "Navarre" in `nevers1588`, corrected); "24 ... estant a La Cassine" |
| 102 | Paris | "102 renvoye des deputez vers 11" |
| 9 | the duc de Guise | "9 voullant faire sortir l'artillerye ... pour aller a Corbeil"; conseil de 9 |
| 12 | Catherine de Médicis | "chez 12 elle a resolu d'envoyer 79 vers 24" |
| 104 | a woman of the Nevers household, probably the duchesse de Nevers | "ce qu'elle a faict", "104 ... ne se deliberoit de partir ce jourd'huy du logis" |
| 10 | the duc d'Épernon | glossed "Espernon" on f. 139; fits f. 62 "a la ruyne de 10" and f. 133 "la survenue de 10 qui est maintenant absent" |
| 38 | Garrault | glossed on f. 139 ("mesmement 38", "Led. 38 ne bougera") |
| 98 | la paix | glossed on f. 139 ("par ce moyen l'on aura 98") |
| 107 | the Grand Écuyer (Bellegarde) | glossed "Grand Escuyer" on f. 139 ("107 s'insinue es bonnes graces de 9") |
| 79 | a messenger of the Queen Mother to Nevers | f. 133 "envoyer 79 vers 24"; f. 139 "79 vous l'aura peu dire ... quand il partit"; the gloss is not legible (Mo...ers?) |
| 4, 23, 25, 33, 94, 105, 106 | not identified | 4, 9, 24, 94 are candidates Paris offers the King "a son choix" (a governor?) |

Who the letter goes to is open: "vous" is someone who took offence at what was written to 24, so a person close to
Nevers rather than the duke himself.

## Remaining gaps

- R08 "curez St André **et** St Benoist": the signs `+` (e) and `2 t` (et) occur only here; read from context.
  Blocker: too-short (single occurrences).
- R14 `1o` in "Nuilly" (i): single occurrence; the name is spelled "Nuilly" in clear on f. 133r. Blocker: too-short.
- R14 "de Bray": letters read (8 = b/v), the person not identified; "de vray" is possible. Identification is a
  history question, not a cipher gap.
- Code numbers 4, 23, 25, 33, 79, 94, 105, 106: open-codes; the informant's number list is not known; the sibling
  letters gloss 9, 10, 11, 24, 38, 98, 107, and the gloss over 79 on f. 139 is illegible.

## Escalation

- siblings: done. ff. 62 (R3705) and 131 give the key; f. 131's gloss over 24 re-read as "nevers". f. 139 (9 June)
  read in full and its code glosses used (10, 38, 98, 107). No other letter of this informant in fr. 3976 per the
  BnF notice (pieces 30, 70, 71, 74).
- clear pages: done. The letter's own clear text gives the context of every run.
- known keys: done. `nevers1588/key.md` applied unchanged, then extended.
- print: not done. Gomberville's *Mémoires de Nevers* (1665) not searched for this letter.
- key rebuild: done. Additions in `nevers1588/key.md` (ϙ = y, crossed 4 = z, [ = n).
- retry: done. Native-resolution second pass on R08, R10, R11, R12, R14.

## f. 139: the letter of 9 June 1588

* BnF fr. 3976 f. 139, piece 74 of the BnF notice ("Lettre chiffrée avec déchiffrement contenant des nouvelles de
  Paris. Ce 9 juing 1588"), Gallica view 234 (f. 139v blank, view 235). Not a DECODE record. Same hand and monogram.
* One page, six cipher runs and code numbers 9, 10, 11, 24, 38 (three times), 79, 98, 107. A contemporary hand wrote
  the plaintext over every run and over most code numbers.
* The key read all 106 signs as it stands (`python r3708/decode.py f139`), and each reading matches the gloss. This is
  an independent check on the key: the glosses were not used to build it.

> C'est chose veritable que le prevost des Marchans s'est retourné mettre en la Bastille. Je n'ay peu descouvrir au
> vray qu'il se face aucune **levee de deniers**. Mais bien m'a l'on asseuré, mesmement 38 [Garrault], que
> **notaires** cherchent **argent a rente**, dont **Nilly, Marcel, prevost des marchans et eschevins** respondent.
> Mais beaucoup ont faict difficulté d'en bailler, et de moy je m'estonne que **Marcel y soit** meslé. On dit que
> 107 [le Grand Escuyer] s'insinue es bonnes graces de 9 [Guise] et en presse. Son frere a aussi quitté 10
> [Espernon]. Sans la haste que j'ay je vous eusse faict ung petit discours succinct de ce qui fut dit en l'assemblée
> de ville des cappitaines dont je vous ay cy devant escript, encore que j'estime que 79 vous l'aura peu dire
> amplement, car cela se scavoit desja quand il partit. L'on tient pour certain que 11 [le Roy] accorde a 9 **la
> lieutenance generalle**, et que par ce moyen l'on aura 98 [la paix]. 38 a plusieurs advis a donner a 24 [Nevers]
> quand il sera pres de 11, tant pour le general que pour son particulier, dont il ne l'advertit maintenant a cause
> que cela seroit inutille estant absent. Ce 9 Juing. [monogram]
> J'ay encloz ung pacquet pour Monsr de Lorme, medecin. Led. 38 ne bougera.

The Bastille, the League's forced loans guaranteed by the new municipality (Neuilly, Claude Marcel, the prévôt and
échevins), and the rumour that Henri III would make Guise lieutenant-general (done by the Edict of Union, July 1588).
