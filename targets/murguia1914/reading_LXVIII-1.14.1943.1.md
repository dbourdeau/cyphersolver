# Reading of Murguía's report to Pablo González, Lamadrid, 16 March 1914 (CEHM LXVIII-1.14.1943.1)

Clear text from the original typed letter (pp. 1-2). Coded text in capitals, decrypted with `key_frozen.tsv`. Accents, punctuation and word division are mine. Marks: `{x/y}` the key gives x, the reading takes y; `{+a}` a letter the encipherer left out; `[?w:NN]` a guess for group NN. A contemporary pencil decipherment stands over the coded groups of the typed copy (pp. 3-4, headed "CLAVE EXTRA 3."); this reading was made from the figures and the key, and the places where it differs from the pencil gloss are listed at the end.

> Hónrome en comunicar á Ud. el resultado de mi campaña hasta la fecha, después de la acción de Rodríguez de la que oportunamente dí á Ud. cuenta; manifestándole que el día 4 del presente DESTRUÍ LA VÍA DEL NACI{+O}NAL entre Golondrinas y Huisachito, CORTANDO DOS TRENES militares y sosteniendo un LIGERO TIROTEO con el ENEMIGO, que era BASTANTE NUMEROSO, RETIRÁNDOME luego al puerto de LA CARROZA. Allí tuve noticias de que en MONCLOVA HABÍA POCO ENEMIGO, y de acuerdo con sus instrucciones y en combinación con el General Castro ataqué esta plaza el día 10 del actual, después de batir el 9 una partida de 125 federales en Carrizalejo, que fué dispersada y se remontó á la sierra de la Gloria. La plaza de Monclova, después de 14 horas de rudo combate, quedó en nuestro poder, habiendo tenido combates parciales por rumbo de Castaño, de Ciénegas y Las Estancias, con el enemigo que procedente de Monterrey, Ciénegas y Piedras Negras trataba de auxiliar al de la plaza atacada.
>
> El día 11 por la tarde NOS ATACÓ EL ENEMIGO, QUE EN NÚMERO DE MÁS DE MIL HOMBRES VENÍA DE Monterrey, y tuvimos que REPLEGARNOS A SAN BUENAVENTURA, en donde nuevamente fuí atacado el día 14, Y ME RETIRÉ AL MOLIN{+O} DEL ÁGUILA para tomar el día siguiente 15, en combinación con el compañero Castro, y atacar dicha plaza, lo cual hicimos. [?NO:97] HABIÉNDONOS sido posible TOMAR LA [?PLAZA:88] [por] SER EL ENEMIGO EN NÚMERO MUY considerable, teniendo que REPLEGARNOS HASTA este lugar con objeto DE REORGANIZARNOS.
>
> Con motivo de los COMBATES MENCIONADOS SE ME HA AGOTADO EL PARQUE COMPLETAMENTE, y hoy mando una comisión á CIUDAD JUÁREZ POR SIERRA MOJADA que se encargue de traerme DOSCIENTOS MIL CARTUCHOS, para lo cual me dirijo al Gral. Chao á fin de que se sirva facilitar los medios de que VENGAN ESAS MUNICIONES LO MÁS PRONTO POSIBLE, y le suplico á Ud. que por esta misma vía se sirva influir con quien corresponda en el mismo sentido.
>
> Igualmente tengo el honor de participar á Ud. que al tomar la plaza de Monclova se hicieron 235 prisioneros, contándose entre ellos el Lic. Guillermo Garza, Lic. Andrés Sánchez Fuentes, Manuel de la Fuente, Jr., Lic. Francisco Cantú Cárdenas, Dr. David Cerna, Enrique Oyervides y José Ma. de la Garza, que pertenecen á la Defensa Social, y algunos de ellos se encontraban en la trinchera.
>
> En esta región PIENSO PERMANECER HASTA QUE VENGA EL PARQUE á que me he referido, para CONTINUAR LA CAMPAÑA, y aprovecharé MI ESTANCIA EN ELLA PARA ORGANIZARME debidamente y AUMENTAR MI TROPA en lo que sea posible. Clave Extra 3.
>
> Protesto á Ud. las seguridades de mi distinguida consideración y subordinación respetuosa. Libertad y Constitución. Campamento en Lamadrid, Marzo 16 de 1914. El General, Fran.co Murguía.

"[por]" before SER is a word the sense needs and the figures do not give (88 may stand for "plaza" or for "plaza por"); it is not counted as read.

## Where the figures and the pencil gloss differ

- S01: the figures give NACINAL; the gloss writes "Nacional".
- S02: the figures give CORTANDO; the gloss writes "cruzando". The 2nd and 4th groups (45 o, 69 t) are clean on p. 1.
- S07: 41 is the cell "rr"; the gloss writes "la carroza".
- S11: the figures give MOLIN; the gloss writes "molino".
- S12, S13: the gloss leaves 97 and 88 without a value.
- S19: the figures give ESAS (no t); the gloss writes "estas".
- S22: 26-49-10 gives ELLA (49 = ll); the gloss writes "en el" and puts "para" small over 87.

## Coded runs (checked by scripts/check_marks.py)

S01 | destruí la vía del naci{+o}nal
S02 | cortando dos trenes
S03 | ligero tiroteo
S04 | enemigo
S05 | bastante numeroso
S06 | retirándome
S07 | la carroza
S08 | monclova había poco enemigo
S09 | nos atacó el enemigo que en número de más de mil hombres venía de
S10 | replegarnos a san buenaventura
S11 | y me retiré al molin{+o} del águila
S12 | [?no:97] habiéndonos
S13 | tomar la [?plaza:88] ser el enemigo en número muy
S14 | replegarnos hasta
S15 | de reorganizarnos
S16 | combates mencionados se me ha agotado el parque completamente
S17 | ciudad juárez por sierra mojada
S18 | doscientos mil cartuchos
S19 | vengan esas municiones lo más pronto posible
S20 | pienso permanecer hasta que venga el parque
S21 | continuar la campaña
S22 | mi estancia en ella para organizarme
S23 | aumentar mi tropa
