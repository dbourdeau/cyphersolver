# ilten1743: readings

Key: the numbered table in the Ilten papers, GWLB Ms XXIII 1234:31,1, pp. 390-391 (decoding side, 1-863;
"NB. les Chiffres qui restent ne signifient rien": blank numbers and 864-1000 are nulls), with the
alphabetical encoding side on pp. 386-388. Transcribed in `key1743/`. Applied by `decode1743.py`;
sign-by-sign output in `decode_feb26_signs.txt` and `decode_mar29_signs.txt`.

## 1. Unsigned letter from London to Johann Georg von Ilten, 15/26 Feb 1743 (Ms XXIII 1234:29,2 pp. 73-75)

Dateline in cipher: `866.223` = [null] Londres.

German opening (clear): "Dasjenige was unterm 18ten February anhero berichtet worden, ist gestern zu recht
eingelauffen, und davon gebührender Vortrag geschehen; es dienet solches zur guten Nachricht, und ist durchgehends
approbirt worden." (Kurrent, read at word level.)

Cipher (189 groups), deciphered here with the key, French:

> Pour ce qui regarde les instructions que Monsieur le general Du Pontpietin a donné à Monsieur le Lieutenant
> general de Sommerfeldt par rapport aux fourages, elles sont aussi approuvées, ainsi que j'ay ordre de le marquer,
> aussi bien qu'on ne doutoit point du soin qu'on auroit de continuer à tenir toujours une bonne et exacte
> discipline dans ce pays là. Cependant on souhaite que les trouppes consument avec r[?] même bonne discipline [e]
> ce qu'il y a de fourage dans ces quartiers, afin qu'il n'en reste rien si l'envie prenoit aux François de vouloir
> prendre quartier après vous dans ce pays là, de sorte qu'ils n'y trouveroient point ni fourage ni rien de ce qui
> seroit necessaire pour la subsistance des trouppes [repeated]. Vous ferez usage de ce dernier point selon votre
> prudence ordinaire [empeche: annulled].

Translation: As for the instructions that General Du Pontpietin has given to Lieutenant-General Sommerfeldt about
forage, they are likewise approved, as I am ordered to tell you, and no one doubted the care that would be taken to
keep up good and exact discipline in that country. Still, it is wished that the troops, with the same good
discipline, consume what forage there is in those quarters, so that none is left if the French should take it into
their heads to quarter there after you, and they would find neither forage nor anything else needed to keep troops.
You will use this last point with your usual prudence.

Then clear German: "ein Affaire ... zwischen dem Obrist von Hardenberg und dem Major d..." (p. 74 foot, continuing on p. 75).

Notes on the groups:
- 172 is "Duc" in the table; here it stands for "du" twice ("le general Du Pontpietin", "du soin").
- 823 Pontpietin, 805 Sommerfeldt, 858 fourage are nomenclator names/words.
- 453 "repete la precedente" follows 639 (trouppes); 101 "annulle la precedente" cancels 697 (empeche).
- Gutter digits read from the full-resolution crop: 51 (ne), 407 (les), 59, 95 (n), 70 (la), 705 (dernier).
- Open: `283.75?` before `750` (me): 283 = r, and the third digit of 75? is lost in the binding (751, a null on
  the sheet, fits the visible stroke). "avec r.. même" does not read as written; "avec la même" is the sense.
  `59` (e) after "discipline" is superfluous. These three tokens are counted as not reading.

Measure: 189 cipher groups; 188 given a value (75? open); 186 read as sense (283, 75?, 59 not). 98.4%.

## 2. Ernst von Steinberg (London) to J. G. von Ilten, 29 Mar / 9 Apr 1743 (Ms XXIII 1234:29,2 pp. 119-121)

German letter with three cipher runs (34 groups). p. 121 is a contemporary worksheet glossing the groups.

"Auf Sr. Königl. Mayt. gnädigsten Befehl habe ich nicht nur das heute an den Herrn General du Pontpietin
ergehende Königl. Rescriptum Copeylich hiebey zu schließen, sondern auch einen [extrait de l'instruction qui vient
d'être envoyée au Mylord Stair] zur Nachricht, und zu dem Ende mit anzufügen, damit Ew. Hochwollgebohren
[quoique avec le dernier ménagement du secret] bey Sr. Königl. Mayt. [généralité allemande] Gebrauch davon machen
mögen."

- Run 1: 344 ex, 515 tra, 126 it, 15 de, 5 l', 782 in(s), 644 tru, 225 c, 721 tion, 266 qui, 767 vi, 353 ent,
  97 de, 17 et, 294 re, 259 envoyé, 41 au, 472 Mylord Stair.
- Run 2: 278 quoique, 613 avec, 147 le, 705 dernier, 750 me, 98 na, 450 ge, 750 me, 714 nt, 172 du[c], 414 secret.
- Run 3: 618 general, 126 it, 3 e, 740 alleman(de), 384 de → "généralité allemande".

The contemporary worksheet (p. 121) read 644 as "tra" ("in-tra-c-tion"), left out 278.613 (quoique avec), and wrote
172 as "Duc"; it has 17.294 as "ê-tre". With the key the three runs read in full.
