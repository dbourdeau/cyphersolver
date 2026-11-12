# R9610 — Alonso Sánchez to Charles V, Venice, 2 June 1522 (RAH Salazar 9/24 ff. 132r-134r; DECODE R9610)

Reading by Brice Dudout (Claude Opus 5.5), 12 Nov 2026. Source: DECODE R9610
(<https://de-crypt.org/decrypt-web/RecordsView/9610>), images P1-P3; no image is reproduced here.
Date in clear at the foot of f. 134r: *en venecia a ij de junio de dxxij*. Not calendared in CSP Spain 2 (Daniel's
entry-by-entry check, NOTES); no decipherment imaged on the record. Tomokiyo (2025) printed the opening line, "A-y-e-r en
la t-a-r-de h-o-v-e carta-s de t-r-e-n-t-o de b-a-n-i-si-o con un-a p-o-s-t-a que me"; the reading below agrees with it.

**Method.** `R9610_signs.txt` (130 cipher lines, 2,722 tokens without nulls and clear words) was transcribed blind, by
sign shape, and frozen by SHA-256 (`protocol/SHA256SUMS`) before any decoding, together with `protocol/PREREG_lot2.md`
(the key stays unchanged, so no new measure). It was decoded with `../key_codes.tsv` unchanged and the letter signs of
`../alpha.py` (`scripts/decode_lot2.py`, raw output `R9610_decode.txt`) and read by sense.

**Markup.** plain = sure; {w} = probable (a declared look-alike, PREREG_lot2 §1: g = r|y, q/Yo = s|t, P = f|s, 3 = d|e,
Z = a|s|c, B = m|r, tt = p|n, resolved by sense); {w†} = probable, but one sign of *my blind transcription* departs from
the form the sense needs, and the needed form is a sign of Daniel's table (see "Transcription errors" below); [w] =
restored; <w> = unresolved (raw decode kept); «…» = clear in the letter, not counted. The † class was not declared in
the PREREG, so the count is given both ways.

| page | sure | probable | probable † | restored | unresolved | words | read (S+P) | with † |
|---|---|---|---|---|---|---|---|---|
| f. 132r | 140 | 44 | 28 | 0 | 32 | 244 | 75.4 % | 86.9 % |
| f. 132v | 166 | 50 | 12 | 1 | 28 | 257 | 84.0 % | 88.7 % |
| f. 133r | 155 | 58 | 23 | 0 | 27 | 263 | 81.0 % | 89.7 % |
| f. 133v | 163 | 39 | 22 | 1 | 37 | 262 | 77.1 % | 85.5 % |
| f. 134r | 67 | 20 | 11 | 0 | 13 | 111 | 78.4 % | 88.3 % |
| **letter** | **691** | **211** | **96** | **2** | **137** | **1,137** | **79.3 %** | **87.8 %** |

**Read in part** under the 95 % rule either way (pre-registered count 79.3 %; 87.8 % if the † words are admitted).
Counted by `scripts/count_reading.py`.

**Transcription errors (†).** The decode shows where my shape labels split or merged Daniel's signs, always the same way:
my `q` (and some `g`) is the l-sign `9` (pol q = *mil*, Q n q m # = *salvo*, pol g = *mill*); my `oo` covers both of
alpha.py's ∞ signs, `oo` = d and `OO` = g (*seguros*, *cargo*, *pagado*, *tengan*, *Griti*); `Z` is sometimes ∂ = d
(*conduto*, *perdida*, *ronpida*, *padre*); my `P` is in places the m-sign (*almirante*, *San Marco*, *conforman*,
*Carmona*); `Lo` stands for the s-like sign (*pasasen*, *fuessen*, *pusiessen*); the pair `tt #` is one sign, alpha.py's
`jt` = u/v (*nueva*, *Savoya*, *estavan*, *Verona*, *entrava*). No value outside Daniel's table is used.

**Code groups absent from the key** (39 groups; listed in `R9610_decode.txt`): proposals only, none applied —
`sod` = *govierno* (3 contexts, s-block bracket after *governador*), `dud` = *vino* (2 here + 2 in R9607, after *vi*),
`lud` = *presente* (here "estando escriviendo la <lud>", R9607 "a [..] del <lud> recebi"), `cid` = *xxii* (c-block
numerals, "cartas de <cid> de abril"). Details in `R9607_recheck.md`.

**Names.** Banisio = Jacopo Bannisio (imperial secretary at Trento); the Visorey de Napoles = Charles de Lannoy; Prospero =
Prospero Colonna; Theodoro [Trivulcio] (spelled run unresolved); Andrea Griti; the almirante de Francia = Bonnivet; the
bastardo de Savoya; *Carmona* is Sánchez's spelling of Cremona (as in R9607); *Tnina* = Knin, besieged by the Turks.

## Reading, line by line

```
132r.01 {ayer} en la {tarde} {hove} cartas de
132r.02 {Trento} de Banisio con {una} {posta†} que me <ba>
132r.03 {y} dize me que el Visorey de Napoles {havia} enbiado alli a un <dvzsan> con
132r.04 xxiv {mil†} ducatos que {Prospero} <(s|t)(d|e)> {havia} {pedido†} {y} que
132r.05 {havia} {escrito†} al <puc> que <tim> se <po(a|s|c)i(s|t)(d|e)ner>
132r.06 para {enbiarlos†} al <caspo> {y} <(d|e)e(s|t)pondi(f|s)s(d|e)> que te-
132r.07 {niendolo} en {Mantua†} el lo {pornia}
132r.08 se {duro} alli {pero} que en {passarlo†} por {tierras} {de}
132r.09 esta Señoria esa bien {escrevir†} me a mi <pidiet(a|s|c)>
132r.10 {salvo†} <conduto(f|s)> assi <bic> <banhsio> me dize que {se}
132r.11 {pida} si me <pasec(a|s|c)(f|s)a(r|y)> con los de esta republica
132r.12 esta <sanyana(r|y)> <dixe(s|t)> es {tenia} havisso que en
132r.13 <Trento: s(d|e)ento> {havia} <yum> {cantidad} de dinero de vuestra
132r.14 magestad que lo havian de <sev(a|s|c)(r|y)a> {Mantua†} que <(s|t)es>
132r.15 <(r|y)odania> me <dieten> un {salvo†} {conduto†} como
132r.16 {pasasen†} <se dvros> con ellos que lo {levavan†}
132r.17 {respondieron†} me que no me {podian†} {dar}
132r.18 {salvo†} {conduto†} {pero} que {escrivirian} a los rec-
132r.19 {tores} de {Verona} que {enbiasen} con <pan(r|y)(a|s|c)> para que pa-
132r.20 {sasen†} <se dvros> por sus {tierras} <ha(s)ste>
132r.21 el {Mantua†} no {y} que {ellos†} me <sasian(f|s)ia>-
132r.22 do {y} es que {pasarian†} <se dvra> mente <(f|s)o(s|t)(s|t)(r|y)(f|s)>
132r.23 con <(r|y)(d|e)n(s|t)a(r|y)> me {y} {dixeron} me <escrevie(s|t)(f|s)a> los que
132r.24 {levavan†} el dinero que {havisasen} a los rec-
132r.25 {tores} de {Verona} {a} que tiempo se {sian} en {tierras†}
132r.26 de esta Señoria por que para {entonces} {ternian}
132r.27 alli quien {los} {aconpanyase†} {y} assi lo {escrivo†}
132r.28 a {Banisio†} con esta {posta} que a mi <muc> no
132r.29 <ha(s)san> estos otra cosa creo dexan de {dar†} el sal-
132v.01 {vo†} {conduto†} por que no lo sepan franceses {pero} pues <beg>
132v.02 <vef> es lo mesmo me e {contentado} el {salvo†} [conduto]
132v.03 para el Visorey de Napoles me lo <vud(r|y)on> muy {complido†} para el {y}
132v.04 toda su {conpanya} {y} con esta {posta} lo enbio {a}
132v.05 {Banisio†} que lo {guarde†} para <havi> dicho visorey {sea}
132v.06 alli llegado que no {tardara} pues {a} xxvi del pasado
132v.07 me escrevio {partiria} de <v(r|y)(m|r)a(r|y)v(d|e)(r|y)nia> «a buenas jornadas
132v.08 que no tenia» {a} que se {detener} «que no havia necessidad»
132v.09 de {hazer} {infanteria} «esta manyana» me {dixeron} ha-
132v.10 {rian} <tib> de la persona que han de {enbiar} al dicho visorey {y} me
132v.11 lo {harian} {saber} si lo <con iz h(d|e)(r|y) en> «antes que
132v.12 esta se cierre» {sera} vuestra magestad havisado quien {sera}
132v.13 aqui es venido un <d el (s|t)ie(r|y)> hombre de Francia que es de {Theo}-
132v.14 {doro} <(r|y)(r|y)iveo(r|y)cho> que {enbiaron} estos al Rey de Francia despues
132v.15 de la {perdida†} de lo <(a|s|c)ibasa> se el <ca(r|y)oabe>
132v.16 <(r|y)o> de la <(a|s|c)(r|y)o(m|r)ees> <ref> no partio a los xvii del passa-
132v.17 do de {Leon†} {traxo} cartas del Rey de Francia para los de esta
132v.18 {republica} {y} para <Andrea Griti: an(a|s|c)(r|y)(f|s)ad(r|y)i(s|t)h> con <(f|s)o(r|y)(f|s)es> de {una}
132v.19 <pug> {sustancia†} {diziendo†} {ser} que ho-
132v.20 {viessen†} por cierto que {perderia} {a} Francia {y} la vida antes
132v.21 que {dexar} esta {enpresa} {y} que <ha(s)vug do> las esc-
132v.22 {usaciones} que de su parte {este} las ha echo {y} que
132v.23 las <acfester> cree {puesto} que <(f|s)(r|y)a> <ahun do> de otros
132v.24 de lo {contrario} {pero} que ellos <tien(f|s)> por muy
132v.25 buenos <a(r|y)ido(s|t)(r|y)s> que el mal <sod> de {Lautrec}
132v.26 <ha(s)se(r|y)do> causa de todo el {danyo} que {se} <menda(r|y)oe(r|y)(r|y)>
132v.27 a Francia {y} {enbiava} a esta {enpresa} al {almirante†}
132v.28 de Francia que {tenia} por cierto el <(r|y)os> no <to> lo no fal-
133r.01 {tarian} de la gente son obligados mas {harian} de mas {y} que
133r.02 {y} es <(r|y)odava> en todo <dieten> su {ayuda} {y} <xu> al
133r.03 dicho {almirante†} el qual {traher} {ha} <mad> de {azer}
133r.04 lo que {ellos†} {aconseiarian†} esto me todo <se(r|y)do> <(a|s|c)e>
133r.05 muy cierto <a(s|t)ie(r|y)(f|s)ado> se {y} assi yo bien se que {Lau}-
133r.06 {trech} {era} muy <vel do> de estos {y} {queria} {poner} se
133r.07 en las {tierras} de estos con la gente que fue a {Carmona†}
133r.08 {y} no lo {consintieron†} antes {Andrea†} {Griti†} {se}
133r.09 {protesto} que {fuessen†} a {Carmona†} {a} {guardar} la tambien
133r.10 {y} es <(r|y)e(a|s|c)vi(r|y)ho> la {vtrech} que {pusiessen†}
133r.11 gente {suya} en {Carmona†} {y} {respondieron} que <(r|y)i>-
133r.12 <an> {guardar} sus {tierras} el dicho {Lautrecha} los
133r.13 xxv dizen partio de <be(r|y)da(r|y)o> la {buelta†} de Francia
133r.14 con <fol> <caroabos> dizen creen <ni (s|t)> de los de {Car}-
133r.15 {mona†} han {ydo} con el por que no {tenia} <con si d(f|s)>
133r.16 {cient} <caroabos> es {ydo} por donde {fueron} el
133r.17 {bastardo} de {Savoya†} {y} los otros dizen verna
133r.18 el {almirante†} de Francia con {mill†} {y} {dozientas}
133r.19 {lanças} <ci> {mil†} {gascones†} {y} <mi> {mil†} suyos que de-
133r.20 <nv(f|s)(r|y)obaxa(r|y)…n> {pero} «por lo que se siente en todo»
133r.21 el camino {hasta} {Leon†} no hay un hombre de guerra
133r.22 {este} {embaxador} del Turco que aqui <pe> {a} xxv dizen
133r.23 estos que <dud> mas por espia que por otro {pero} lo que
133r.24 {y} es ha dicho {y} estos dizen que {trahe} es que se que <b(a|s|c)> el
133r.25 Turco que de sus {tierras} de estos se {aze} <ni> da <s(r|y)o>
133r.26 a los suyos {y} tambien que se {salvan†} en {tierras}
133r.27 de estos <nig> {christianos†} que se {huyen} que lo
133r.28 <re(f|s)(d|e)dien> {y} {provean} otramente que {tengan†} por
133v.01 {ronpida†} la paz <pid(d|e)(r|y)es> tambien un <con iho(r|y)(d|e)>
133v.02 un veneciano que no esta aqui que en tiempo passado se fue el
133v.03 {padre†} con {ioyas} de un {tesoro} del Turco de va-
133v.04 {lor†} de {hasta} <cu> {mil†} ducatos dizen estos que el dicho
133v.05 {embaxador} no <dud> a otro {y} que assi lo han {escrito†}
133v.06 a sus {embaxadores} {a} todas partes yo e {tenido} un <(a|s|c)>
133v.07 <espiar do> <sa> la {puerta} de casa del dicho embaxa-
133v.08 {dor} {y} <aibsi> {entrava†} al <dvno> del <sod> de
133v.09 estos de los que {tienen} {cargo†} de lo {secreto†}
133v.10 por ver si <a con i> {alguna†} {secreta} <ruc> {y} {hasta}
133v.11 <adora> no han <deg> <entr(f|s)ar> persona <nof> de <nid> <ci(f|s)>
133v.12 ni publica ni <guc> {este} {embaxador} del Turco dizen ha dicho que
133v.13 el Turco no {armaria} mas de <gid> {velas} por <far> [todavia]
133v.14 <(a|s|c)> los havisos {conforman†} que arma {cient} {velas}
133v.15 esta {Señoria} {tiene†} cartas de <cid> de {abril†} que dizen
133v.16 {armava†} {y} no sabian para donde el duce me
133v.17 ha dicho que no cree por {este} {anyo} <ha(s)da> cosa de <(f|s)o(f|s)
133v.18 (d|e)n(s|t)o(r|y)(d|e)d> aqui arman con {razonable†} {prisa†}
133v.19 {entiendo} que no {cunpliran†} el <nog> de {las}
133v.20 {cinquenta†} galeras {salvo†} de <cag> {a} <ceg> {hasta}
133v.21 que {tengan†} mas cierto havisso del {armar} del Turco {y} en-
133v.22 {tonces} {partira} su capitan <sec> de <pod> que en su parti-
133v.23 da se {veran} los havisos {ciertos} de la armada
133v.24 del Turco por aqui <p(r|y)ob(r|y)ica mente> no {pero} los del
133v.25 <sod> dizen que el Turco {yra} sobre <pvba> aqui <(f|s)v(r|y)io>
133v.26 un {procurador} de {San Marco†} han
133v.27 echo luego {procurador} a su <con iho> por <cu> {mil†}
133v.28 ducatos que ha {pagado†} han <(a|s|c)o(f|s)en> en <cado> cosa
134r.01 {nueva†} que no {solian†} {azer} {procuradores}
134r.02 si no muy <vi(f|s)io(s|t)(r|y)a> {hora} por <ens los> <az(f|s)n(f|s)o>
134r.03 <cos(f|s)on(s|t)(f|s)o(r|y)ench> fue a <(r|y)(d|e)(r|y)(a|s|c)> se {despe}-
134r.04 {dir†} de esta {Señoria} <ha(s)(r|y)e echo> la {costa} <ores> parti-
134r.05 do {y} <da> {a} {Ferrara} {entiendo†} que ha <bic> el <soc(f|s)
134r.06 (m|r)o> de Francia no verna en tiempo {y} que {Carmona†} se
134r.07 {entregara†} a los de vuestra magestad estando escrivien-
134r.08 do la <lud> los de esta {republica} me han <bil do> un <s>
134r.09 {treslado} que {sera} con esta que han hovido
134r.10 {nueva†} que los {turcos} {estavan†} sobre {Tnina}
134r.11 han me dicho los de esta {republica} que han {escrito}
134r.12 a {Verona†} que {hagan†} al Visorey de Napoles todo {acatamiente} {y} se-
134r.13 <(r|y)vicho(r|y)> que {le†} {reciban} muy bien «en venecia
134r.14 a ij de junio de dxxij»
```
