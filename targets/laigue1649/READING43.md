# No. 43: Conti's mémoire for Laigue, 5 March 1649 (BnF fr. 3854 no. 43, ff. 117r–120r), read in full

No. 43 is Conti's mémoire *pour Monsieur de Legue*: Geoffroy, marquis de Laigue, Conti's envoy to Archduke
Leopold Wilhelm. It runs to seven pages, ff. 117r–120r (Gallica canvases 245–251).

- It is written in a numerical code of letters and syllables, with clear words mixed in.
- A contemporary hand deciphered it between the lines from f. 117r l. 12 onward.
- **The first twelve lines, 264 groups, were never deciphered.** They are the address and the purpose of the
  mémoire. This file reads them.

## How the code works (rebuilt here)

The key was rebuilt from the glossed groups that agents transcribed from ff. 118r, 118v
and 117v (`n43/pairs_c246.txt`, `pairs_c247.txt`, `pairs_c248.txt`: 1,485 glossed groups). `n43/buildkey.py` tallies them into
`n43/key43.txt`.

- **Single letters: four interleaved alphabets.**

  | Numbers | Direction | Examples |
  |---|---|---|
  | 3–25 | a→z | a 3, b 4, … l 13, … z 25 |
  | 28–50 | z→a | o 37, n 38, i 42, e 46, a 50 |
  | 51–73 | a→z | e 55, i 59, s 68, u 70, x 71 |
  | about 80–98 | z→a | t 80, s 81, n 86, i 90, c 96 |

- **Syllables: consonant blocks of five, in vowel order a e i o u.** For example b 251–255, c 256–260,
  d 261–265, f 291–295, g 296–300, h 301–305, l 336–340, m 341–345, n 346–350, p 375–379, q 380–384,
  r 385–389, s 410–414, t 415–419, v 420–424.
  - A second, homophonic series fills the gaps: do 277, de 279, je 314, gu 321, ne 354, me 358, la 364, ru 390,
    pu 400, se 439, ti 442, te 443, su 445.
- **An underlined number reverses its syllable.** 385 = ra, 385̲ = ar; 416 = te, 416̲ = et; 347̲ = en.
- **Nulls:** numbers roughly 99–250, never glossed anywhere (99, 119, 129, 150, 199, 200, 206, 207, 210, 219,
  222, 225, 229, 230, 237, 240, 250).
- **Code words:** 457 = cardinal, 458 = parlement, 472 = l'archiduc.

## Where the 264 values come from (`n43/decode_opening.py`)

- **220 groups:** the majority gloss the same number carries on the glossed pages.
- **24 groups:** fixed by the alphabet structure (37, 38, 46, 59, 80, 81, 86) or are nulls.
- **20 groups:** second-series syllables fixed by context in the opening itself.
  - They agree with one another and with the block layout: do 277 and de 279 share a block, as do me 358 and
    la 364.
  - These are the least certain values. None changes the sense of a sentence.
  - A targeted scan of ff. 119r–120r **confirmed three of them from the contemporary glosses: 279 = de, 364 = la,
    354 = ne** (underlined 354 = en). None was contradicted; the other 17 do not occur in the glossed text
    (`n43/scan_119_120.md`).

## Text

Clear words in the manuscript are in roman; the deciphered text is in *italics*.

> *Pour Monsieur de Legue. Parce que nous ne doutons que le cardinal ne donne une mauvaise interprétation à toutes
> ses actions, et* qu'il *ne face* principalement *ses effors pour mettre l'archiduc dans la défiance de nos*
> bonnes intentions *sur le sujet de la conférence que [le] parlement a accordée,* j'ay jugé à propos de vous en
> *faire instruire, afin* que vous puissiés *destourner les mauvais effets des artifices du cardinal, et faire
> comprendre à l'archiduc que ce pourparler n'a esté causé et résolu que* par les *retardemens que l'archiduc
> apporte à nous secourir, et que* nous sommes tousiours dans *nos mesmes desseins, sans que rien puisse altérer
> les paroles que nous a[vons données] …*

## The whole mémoire, ff. 117r–120r (edition)

Sources for this text:
- **f. 117r, first 12 lines:** decoded here (above).
- **Everything after that:** the contemporary interlinear decipherment. It was transcribed group by group
  (`n43/pairs_c245.txt` … `pairs_c251.txt`, about 3,300 glossed groups) and joined by `n43/assemble.py`
  (`n43/body_assembled.txt`).

Editorial conventions:
- Spelling follows the decipherer.
- Accents, apostrophes and punctuation are modern.
- [ ] marks letters supplied; […] marks a gap; (?) marks a doubtful reading.

> **Pour Monsieur de Legue.** Parce que nous ne doutons que le cardinal ne donne une mauvaise interprétation à
> toutes ses actions, et qu'il ne face principalement ses efforts pour mettre l'archiduc dans la défiance de nos
> bonnes intentions sur le sujet de la conférence que [le] parlement a accordée, j'ay jugé à propos de vous en
> faire instruire, afin que vous puissiés destourner les mauvais effets des artifices du cardinal, et faire
> comprendre à l'archiduc que ce pourparler n'a esté causé et résolu que par les retardemens que l'archiduc
> apporte à nous secourir, et que nous sommes tousiours dans nos mesmes desseins, sans que rien puisse altérer les
> paroles que nous a[vons données] de travailler fortement pour procurer aux deux couronnes la tranquillité et la
> paix par l'esloignement de ceux qui s'y opposent. Comme nous espérons aussy que l'archiduc, n'estant pas capable
> de manquer aux assurances qu'il nous a fait donner de traiter avec nous, n'aura point adjousté de foy aux envoyez
> du cardinal, et ne se sera pas laissé esblou[ir] à ce que cet ennemy commun luy aura pu faire dire sur le
> prétexte que nous songeons à un accommodement particulier dans cette conférence, sur le sujet de laquelle vous
> ferez remarquer à l'archiduc quels en ont esté les motifs, quel le dessein, et l'estat où sont les choses, selon
> ce qui suit.
>
> Ayant cru qu'il estoit de la bienséance que [le] parlement donnast avis à la Reyne de l'arrivée de dom Joseph et
> de ses propositions, le cardinal, qui voyoit bien que de ce véritable acheminement à la paix s'ensuivoit sa
> ruyne, affin d'en destourner le coup ou du moins d'en retarder l'exécution, a fait proposer une conférence qui
> pust tirer les choses en longueur et luy donnast loisir de destourner les bonnes intentions de l'archiduc, en
> nous faisant soubçonner de nous relascher de nos droicts, à quoy l'on a employé Vautorte. Il nous auroit esté
> très facile de refuser cette conférence si le secours de l'archiduc se fust trouvé prest, et que nous n'eussions
> point esté si fort pressés de la nécessité des vivres. Mais dans ces deux conjonctures très pressantes, et sur
> lesquelles je vous ay desja despesché trois personnes, nous avons estimé à propos, en attendant de vos
> nouvelles, de ne pas empescher la conférence, afin de donner encor[e] un peu de temps à l'archiduc de se mettre en
> estat de venir à nous, et de pouvoir cependant faire subsister cette grande ville jusqu'à ce que nos forces
> jointes en ayent levé le blocus. La conférence a donc esté acceptée, mais avec cette condition que l'on y
> traitera non seulement du […] de ce royaume, mais de la paix générale ; par où l'archiduc pourra juger qu'en
> cela mesmes nous voulons [b]ien tesmoigner que nostre dessein va tousiours à ne rien faire sans traiter avecque
> luy, ainsi que nous nous y sommes engagez. L'avantage présent qui nous revient de conférer est que, ne faisant
> aucune suspension d'armes, et estant au contraire en estat d'entreprendre ce jour mesme quelque chose de fort
> considérable pour faire entrer des vivres à Paris, outre quelques [c]onvoys que nos troupes font et les petits
> secours des paisans, les ministres de Saint-Germain nous accordent de laisser venir de Corbeil cent muids de
> bleds chaque jour, à commencer de celuy-cy, qui est le premier de la conférence, tant qu'elle durera ; ce qui nous
> peut faire couler encor quelque temps, mais, à dire le vray (?), fort peu, en vous attendant.
>
> Quand à l'effet de la conférence, vous ferez entendre à l'archiduc qu'ayant esté les maistres de la nomination
> des députés, tant du parlement que des autres compagnies souveraines, et le parti le plus juste ayant facilement
> prévalu partout, ces députés de plus estant tous gens de bien, dans le zèle de la paix générale et dans une haine
> irréconciliable pour le ministériat du cardinal, la conférence ou tirera en longueur ou se rompra, selon ce que
> le bien de nos affaires et les projets de la paix que nous voulons traiter avec l'archiduc nous sembleront
> requérir, sans qu'il s'y puisse rien conclure si le cardinal ne se retire ; auquel cas, en y appellant
> l'archiduc, le traité de la paix générale se conclura sans difficulté. Mais comme il n'y a aucun lieu d'espérer
> que la seule douceur et la raison des arrests luy persuadent de quitter les affaires, et qu'il y faudra employer
> la force, aussy est-il impossible que ce traité, en l'estat où il est, puisse avoir aucun effet. Vous ferez
> encore remarquer à l'archiduc sur cet article que le pouvoir qu'on a donné aux députés de traiter ne doit en
> aucune sorte faire appréhender qu'ils puissent conclure, puisque, quand ils seroient autant créatures du
> cardinal qu'ils sont gens de bien et dévoués à la bonne cause, ils n'ont pas la puissance de se relascher de la
> moindre chose sur l'article du cardin[al], […] qu'il est condamné par [le] parlement, et que, selon les loix et
> l'institution dont […]te compagnie, […] ne […] jamais non pas casser, mais seulement affoiblir l'un de ses
> arrests. Pour mon particulier et celuy de Messieurs les généraux, j'estime que l'archiduc aura tout sujet de se
> louer de ce que ny moy ny les autres n'avons pas voulu assister à la conférence ; ce que nous avons fait pour
> plusieurs raisons, dont les apparentes sont de faire voir hautement à tout le monde que nostre interest ne nous
> conduit point, et que si nous en avons quelques-uns à ménager, nous en laissons au parlement, des députés duquel
> nous sommes assurés, la décision entière ; ce qui establit tousiours nostre réputation, nous gaigne crédit dans les
> provinces et affermit la justice de nostre cause. Mais les raisons solides et effectives qui nous esloignent du
> pourparler sont que nous avons voulu demeurer en estat de le rompre toutes les fois que bon nous sembleroit et que
> nous jugerions à propos pour l'establissement de la paix des deux couronnes ; ayant en cela eu esgard
> principalement à tesmoigner à l'archiduc que nous ne négligeons pas une seule mesure que nous ne la prenions pour
> luy faire connoistre qu'estant unis de parole pour la paix générale, nous nous conservons en un estat où rien ne
> sçauroit nous obliger à luy en manquer.
>
> Sur tout ceci vous pourrez assurer positivement l'archiduc, premièrement que, le peuple de Paris estant disposé
> [et] fort pressé par la disette des vivres, et voulant qu'on le menast au combat, ce que nous n'avons pas cru
> devoir hazarder, y allant de la cheute de tout le parti, nous avons accepté une conférence pour pouvoir vivre
> parmi nos incommodités encore un peu de temps et donner lieu à l'archiduc de nous secourir ; et en second lieu,
> que ladite conférence estant composée de nostre costé de gens de bien, ne pouvant de plus aboutir à rien durant
> le ministériat du cardinal condamné par le parlement, et moy ny Messieurs les généraux n'ayant point voulu [y]
> estre, affin d'en demeurer tousiours les maistres et de nous résoudre avec les gens de bien du parlement au parti
> qui nous sembleroit le plus à propos pour effectuer les bons desseins qui nous sont communs avec l'archiduc, vous
> pouvez assurer l'archiduc et luy en donner ma parole expresse que, dès le moment qu'il entrera en France, cette
> conférence se rompra, en ayant des moyens seurs (?) et certains, et qu'on en commencera une autre plus sincère et
> plus asseurée avecque ses députés, qui nous donnera bientost la paix.
>
> Mais comme nous sommes extraordinairement pressez, et que si le secours n'arrive (?) aussy promptement que le
> besoin que nous en avons est grand, les affaires pourroient tomber en une extrémité d'où […] ne seroit capable de
> les relever, pressez, mais sans relasche, l'archiduc sur ce qu'il n'y a plus un seul moment à perdre pour nous
> secourir, et qu'il peut bien juger combien nos nécessitez sont augmentées depuis le xxij febvrier que je luy
> despeschay pour luy dire qu'elles estoient très pressantes. Sollicitez-le encore d'amener […] (?), auquel, selon
> et jusques où vous le jugerez à propos, vous donnerez part de ces choses ; sollicitez-le de nous faire secourir de
> toutes leurs forces, dont nous avons une nécessité entière, outre que cela acheminera plustost à un
> accommodement général. Que s'il se trouve quelque difficulté de la part de l'archiduc, ce que je ne veux pas
> croire, à ne point entrer sans traité, avancez-en tousiours […], et faites en sorte qu'il ne tienne pas à cela que
> nous ne soyons secourus, réitérant encor à l'archiduc la parolle que je luy ay faict donner par tous mes envoyés,
> que je l'assure qu'il sera satisfaict sur tout ce qu'il sçauroit souhaiter, et que, conspirant luy et moy de
> toutes nos forces à la paix des peuples de l'Europe et à l'union asseurée et ferme des deux couronnes, il n'y a
> rien de mon costé qui soit capable de m'obliger à ne pas conclure ce que je me promets aussi de l'archiduc.
> **À Paris, le 5me mars 1649.**

### Notes on the edition

- **People.**
  - *Dom Joseph* is José de Illescas, the Archduke's envoy, whose arrival and proposals were laid before the
    parlement in late February 1649.
  - *Vautorte* is probably François Cazet de Vautorte, used by the court in the approach that led to the
    conference.
- **Code words.** The code has whole-word groups for *la Reyne* (451), *France* (482), *l'archiduc* (472), *le
  cardinal* (457) and *le parlement* (458).
  - The 500s are dates: 560 518 = "xxij feburier", 543 519 = "5me mars 1649".
  - 509 (f. 119v l. 14) carries a gloss that was written and struck through, apparently "duc de Lorraine". It is
    left open here.
- **Places left open** ([…] in the edition):
  - f. 117v l. 18: *du […] de ce royaume*.
  - f. 118v ll. 5–8: the passage on the parlement's arrests.
  - f. 119v l. 14: the object of *amener*.
  - f. 120r l. 0: *avancez-en tousiours […]*.
  - In each of these the gloss is faint, blotted or run together. They need a second look at the leaf, not more
    cryptanalysis.
- **Clear words.** Clear words in the manuscript are not distinguished from deciphered ones in this edition; the
  per-line files keep the distinction (`#word`).
- **Checks on the opening's key.** The new pairs confirm more of the opening's context and structural values:
  443 = te, 445 = su, 86 = n, 37 = o and 43 = h, besides 279, 364 and 354 again.

## Notes

- **Why the opening was left undeciphered.** The second-series syllables (277, 279, 314, 321, 354, 358, 364, 390,
  400, 439–445) and the alphabet values 37, 80, 81 and 86 never occur in the glossed text of ff. 117v–118v
  (1,485 glossed groups): no pair confirms them and none contradicts them. The opening leans on a part of the key
  the body hardly uses, which may be why the contemporary decipherer did not gloss it.
  - Checks against the complete f. 117v pairs: 46 = e, 59 = i and 38 = n agree with the alphabet layout.

- **Date: 5 March 1649.** The deciphered last line of f. 120r reads "le 5me mars 1649" (`n43/scan_119_120.md`).
- (Superseded:) The mémoire is undated. The opening says the conference (Rueil, from 4 March 1649) has already been granted
  and that the Archduke's slowness in sending help provoked it. That places it in early or mid March 1649,
  before nos. 41–42 (26–27 March).
- Slips in the original:
  - *effors* is enciphered with an extra `s` (effor-s-s).
  - *mauvais effets* lacks the *fe* (ef-[229 null]-t-s).
- My transcription of the opening is in `n43/opening_c245.txt`, the decoded text in `n43/opening_decoded.txt`.
