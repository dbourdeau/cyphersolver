# n22 — Annotationes, context-assisted reconciliation

Status: **exploratory and not blind**. All 35 A/B source rows are represented, including the 18-line iota paragraph. The brief's estimate of about 45 lines was not adopted as a row count. `n22_settled.tsv` means a frozen comparison layer, not a fully resolved transcript. Ambiguous letters, cancelled words, signs and numeric groups remain visible. No percentage of words read or novelty claim is made.

## Source and evidence checked

LASA A 1 Nr.530, **frame0251 right, f.221r**, heading *Annotationes*, “No.22”. Source: `sources/raw/deep_2026-11-12/osnabrueck1647_cipheronly/Nr_530/max/A_1__Nr_530__0251.jpg` (2499×2117). Full source and five newly made panels were inspected: `crops/n22_reconcile/shorts.jpg` (α–ζ), `iota1.jpg` (ζ overlap, η–θ, ι1–6), `iota2.jpg` (ι6–14), `iota3.jpg` (ι14–18, κ), `last.jpg` (κ overlap, λ–μ). Panel ranges overlap; they are display derivatives of one source, not independent evidence. Every differing A/B span was compared in these panels; unresolved variants were retained instead of selected from grammar.

The two original TSVs `transcription/n22_A.tsv` and `n22_B.tsv` remain untouched; their notes identify recurring c/e, q/g, minim-count and page-edge doubts. All **101** A/B differing spans are in `crops/n22_reconcile/difference_ledger.tsv`, including word splits, sign-description differences and punctuation. Original glyph spellings are preserved in the ledger even where a cancelled word is no longer treated as running text. The unchanged worksheet key is `key_v3_worksheet.json`, SHA256 `4c4824b0fa67abd5c9c9278befb9ee4948890e68da3a835664d20f07c8e3478f`.

## Historical reading and priority

The strongest long passage is iota. Its alphabetic core concerns a universal amnesty, the limits of commitment to another party, claims and demands in the principal negotiation, religion and liberty, and restitution of ecclesiastical property. The narrative contrasts assurances of good intentions with a refusal even to discuss another restitution demand. Its final claim appears conditional on a party refusing that demand, leaving no hope of Φ. Reading Φ as peace is plausible in context, **but the present alphabetic key does not establish any symbol's meaning**.

Many actor references remain graphical signs. In particular, the crossed-loop/star-like shapes must not be silently called either Sweden or emperor. Delta's proposed *Suecicis gravaminibus* comes from alphabetic letters, not from a symbol assignment. Theta probably contains a commissioner/title and a name resembling Chemnitius, at Minden; epsilon resembles a proper name Lützow/Lurtzow. Neither person is securely identified here. Kappa's count's name is left incomplete. Mu's numeric strings are **not decrypted dates**: second-digit 8/0 uncertainty survives as 9896/9096 and 9888/9088, alongside 24.

**Priority:** iota offers the best passage to collate against a published diary edition: amnesty plus a disputed restitution case gives a sharper content anchor than an uncertain date or guessed name. Next resolve the symbol vocabulary against separate period key pages. The bottom numeric groups require their own documented rule; no rule is invented here.

## Editorial/emendation ledger

The full line record separates frozen cipher, mechanical key output, proposed German/Latin, and English. `⟨A ∥ B⟩` is an unresolved source alternative, decoded on both branches. `[S:...]` and `{clear:...}` are copied through the alphabetic decoder and are not its plaintext output. `[?...]` marks editorial repairs in the proposed reading. Capitalization, spaces and routine u/v presentation are editorial only. English follows the proposal with uncertainty; it is not another source.

Substantive repairs requiring particular caution: beta *quid/oblata*; theta title/name; iota L03 *dergestalt daß*; L04 *unumschrenkten*; L05–07 alliance withdrawal and dangerous intentions; L09–11 *postulata*, *in puncto religionis libertatisque* and an unresolved comparative adjective; L12 the circumstances of a visit; L14 *verfochten/hingegen*; L17 *weil/wann*; kappa's name/message; mu's unread verb and final numerals. Each repaired word is bracketed in place below. This is a readable working reconstruction with holes, not a clean replacement for the manuscript.

## Complete line record

### n22_alpha.L01

- **Cipher:** `⟨zbktergq ∥ zbktcrqqz⟩ ⟨xrfedfbr ∥ xrfcdfbr⟩`
- **Literal:** `⟨asyldioc ∥ asylqicca⟩ ⟨mindensi ∥ minqensi⟩`
- **Proposed:** [?asyli.../...] Mindensi.
- **English:** [Unresolved phrase] of/at Minden; grammatical construction uncertain.

### n22_beta.L01

- **Cipher:** `⟨ehre ∥ chrc⟩ bqrtrqdl ⟨ed gotzlz qggWdizlrgfd rherqdfl ∥ cd getzlz qqgWdizlrzfd rhcrqdfl⟩`
- **Literal:** `⟨duid ∥ quiq⟩ scilicet ⟨de oglata cooperatione iudicent ∥ qe odlata ccoperatiane iuqicent⟩`
- **Proposed:** [?quid] scilicet de [?oblata] [?cooperatione] [?iudicent].
- **English:** [?What], namely, they [?think] of the [?offered cooperation].

### n22_gamma.L01

- **Cipher:** `dioz [S:△] rfWixxrb`
- **Literal:** `erga [S:△] inprmmis`
- **Proposed:** erga [△] [?imprimis].
- **English:** Toward [△] [?especially].

### n22_delta.L01

- **Cipher:** `⟨dmqdWlrb ∥ dmgdWlrb⟩ bhdqrqib ⟨oizhzxjfrshs ∥ oizhzxrfrsh⟩`
- **Literal:** `⟨exceptis ∥ exoeptis⟩ suecicrs ⟨grauamrnibub ∥ grauaminibu⟩`
- **Proposed:** [?exceptis] [?Suecicis] [?gravaminibus].
- **English:** [?Except for the Swedish grievances]. [Swedish is an alphabetic repair, not an identification of a symbol.]

### n22_epsilon.L01

- **Cipher:** `thilagp`
- **Literal:** `lurtzow`
- **Proposed:** [?Lützow/Lurtzow].
- **English:** [Possible proper name, not securely identified.]

### n22_zeta.L01

- **Cipher:** `⟨hfel ∥ hfcl⟩ dpzi ⟨hdizxrlldeb ∥ hdzxrlldeb⟩ [S:crossed-triangles/MM-like mark] xhiblt ⟨ehiqzt ∥ chiqat⟩`
- **Literal:** `⟨undt ∥ unqt⟩ ewar ⟨ueramitteds ∥ ueamitteds⟩ [S:crossed-triangles/MM-like mark] murstl ⟨durcal ∥ qurczl⟩`
- **Proposed:** [?Undt] [?zwar] [?vermittels] [angular sign] [?fürstl.] [?Durchl.].
- **English:** [?And indeed through] [angular sign's] [?Princely Highness].

### n22_eta.L01

- **Cipher:** `aprbqudf [S:crossed-triangles/MM-like mark] [S:XX] ⟨et ∥ ex⟩ [S:barred B] [S:C-shaped curve with point; possible opening parenthesis] prd di ezt ⟨fgqu erdbdi ∥ fqqu crdbdi⟩ lzodf ⟨edk ∥ sdk⟩ [S:two small loops joined by stroke with cross] ⟨∅ ∥ o⟩ edpdbl ⟨hfel ∥ hfcl⟩ edf [S:crossed-triangles/MM-like mark]`
- **Literal:** `zwischen [S:crossed-triangles/MM-like mark] [S:XX] ⟨dl ∥ dm⟩ [S:barred B] [S:C-shaped curve with point; possible opening parenthesis] wie er dal ⟨noch dieser ∥ ncch qieser⟩ tagen ⟨dey ∥ bey⟩ [S:two small loops joined by stroke with cross] ⟨∅ ∥ g⟩ dewest ⟨undt ∥ unqt⟩ den [S:crossed-triangles/MM-like mark]`
- **Proposed:** Zwischen [angular sign] [XX] [?et; possibly clear Latin] [barred B] ([?wie] er [?das] [?noch] dieser Tagen [?bey] [paired-loop/cross sign; possible extra g] [?gewesen] [?undt] den [angular sign]
- **English:** Between [unresolved signs] ([?as] he had recently [?been with] [unresolved sign], and had...

### n22_eta.L02

- **Cipher:** `⟨bgfediapdrundt sdtbdi ∥ bgfediapidrundt sctbdi⟩ sdphbl df djgidx ⟨zfllbqahterodl ∥ dfllbqahtcrodl⟩ udlld`
- **Literal:** `⟨sonderzweihfel belser ∥ sonderzwreihfel bqlser⟩ bewust en erorem ⟨anttsczuldiget ∥ enttsczulqiget⟩ hette`
- **Proposed:** [?sonder Zweifel] [?selber] [?bewußten] [?errorem] [?entschuldiget] hette).
- **English:** ...[?excused an error which he himself undoubtedly knew of]). [Several words and syntax repaired; not a firm sentence.]

### n22_theta.L01

- **Cipher:** `⟨edfedizt qgjrtzirhb quedxfrlrhex ∥ odfclizt qgxrbzirhb qucdx?frlrd?⟩ rlag ⟨ah xrfedf ∥ dh xrfcdf⟩`
- **Literal:** `⟨denderal corilarius chdemnitiudm ∥ genqtral comisarius chqem?nitie?⟩ itzo ⟨zu minden ∥ eu minqen⟩`
- **Proposed:** [?General] [?Commissarius] [?Chemnitius] itzo [?zu Minden].
- **English:** [?General commissioner Chemnitius], now [?at Minden]. [Title/name proposed, person not identified.]

### n22_iota.L01

- **Cipher:** `⟨prdfduxtrqu ∥ prlfduxtrqu⟩ frqul zttdrf [S:o°o] [S:three heavily cancelled words; A unreadable, B b?fcd?fc??? crd m??] [S:box with horizontal rungs] xrl ⟨edx ∥ cdx⟩ [S:arch with inner hook/m-like loop] pdbdf ⟨hfel edx ∥ hfcl cdx⟩ trd`
- **Literal:** `⟨wienehmlich ∥ witnehmlich⟩ nicht allein [S:o°o] [S:three heavily cancelled words; A unreadable, B b?fcd?fc??? crd m??] [S:box with horizontal rungs] mit ⟨dem ∥ qem⟩ [S:arch with inner hook/m-like loop] wesen ⟨undt dem ∥ unqt qem⟩ lie`
- **Proposed:** [?Wie nehmlich] nicht allein [o°o] [three cancelled words] [ladder] mit [?dem] [arch] Wesen [?undt dem] lie-
- **English:** [?How, namely], not only [o°o] [cancelled words] [ladder] had meant faithfully by [?the] [arch] affairs and the dear...

### n22_iota.L02

- **Cipher:** `sdf [S:circle with vertical stroke, like Φ] db ⟨rdediadrl ∥ rdcdiadrl?⟩ lidptrqu odxdrfdl ⟨bqfedrf ∥ bgfcdf⟩ ⟨zhqe ∥ zhqu⟩ ⟨erd ∥ crd⟩ [S:box with horizontal rungs] drfd ohld ⟨rfldflrgf zhed ∥ rfldflrgfabed⟩`
- **Literal:** `ben [S:circle with vertical stroke, like Φ] es ⟨iederzeit ∥ ieqerzeit?⟩ trewlich gemeinet ⟨scndein ∥ sonqen⟩ ⟨aucd ∥ auch⟩ ⟨die ∥ qie⟩ [S:box with horizontal rungs] eine gute ⟨intention aude ∥ intentionzsde⟩`
- **Proposed:** ben [Φ] es [?jederzeit] trewlich gemeinet, [?sondern] [?auch] [?die] [ladder] eine gute [?intention habe],
- **English:** ...[Φ], [?at all times], but [?also] [ladder] had a good [?intention]...

### n22_iota.L03

- **Cipher:** `idblztl ezt [S:o°o] fqqu fdptrqubl ze [S:crossed loop with upright strokes] sdpddtrqu odbquirdsdf ⟨hfel ∥ hfcl⟩ hxs diludrithfod`
- **Literal:** `restalt dal [S:o°o] ncch newlichst ad [S:crossed loop with upright strokes] beweelich geschrieben ⟨undt ∥ unqt⟩ umb ertheirlunge`
- **Proposed:** [?dergestalt daß] [o°o] [?noch] newlichst ad [crossed loop] [?beweglich] geschrieben [?undt] umb [?Ertheilung]
- **English:** ...[?such that] [o°o] had [?recently] written [?earnestly] to [crossed loop] and requested the [?granting]...

### n22_iota.L04

- **Cipher:** `drfdi hfrhdibzt ⟨ehiquodudfidf hfel ∥ chiquodudfcdf hfcl⟩ ??? ⟨hfhxsbquiedfrlldr ∥ hfhxsbquidtrlldn⟩ zxfdblrd ⟨edsdlldr ∥ edsdlldn⟩ [S:box with horizontal rungs] zodi`
- **Literal:** `einer uniuersal ⟨durchgehenren undt ∥ qurchgehenqen unqt⟩ ??? ⟨unumbschrdenittei ∥ unumbschrelittef⟩ amnestie ⟨debettei ∥ debettef⟩ [S:box with horizontal rungs] ager`
- **Proposed:** einer universal [?durchgehenden] [?undt] [lost word] [?unumschrenkten] Amnestie [?gebetten], [ladder] [?aber]
- **English:** ...of a universal, [?comprehensive] and [lost word] [?unrestricted] amnesty. [Ladder], [?however]...

### n22_iota.L05

- **Cipher:** `odgdf ruxed bdisbl ⟨dqfldblridt ∥ d?fldblridt⟩ udlld brd pdid xrl [S:▽] ⟨bjudqu ∥ bgudqu⟩ frqul ⟨udishfedf ezb?? ∥ udishfcdf ezbbd⟩`
- **Literal:** `geoen ihmde serbst ⟨ecntestirel ∥ e?ntestirel⟩ hette sie were mit [S:▽] ⟨srhech ∥ sohech⟩ nicht ⟨herbunden das?? ∥ herbunqen dasse⟩`
- **Proposed:** [?gegen] [?ihm] [?selbst] [?contestiret] hette, sie were mit [▽] [?so hoch] nicht [?verbunden], [?daß sie]
- **English:** ...had [?affirmed to him himself] that she/they were not [?so strongly bound] to [▽] that...

### n22_iota.L06

- **Cipher:** `frqul ⟨rdediqdil zsdlef nqfld ∥ rdcdiqdil zsldlcf nifld⟩ zhqu ⟨bgsztel ∥ bqsztcl⟩ prd ⟨hfsrxrqhd gedi odneuitrqud rfedf ∥ hfsrurqbd gcdi odnzuitrqud rfcdf⟩`
- **Literal:** `nicht ⟨iedercert abetdn fcnte ∥ ieqercert abtetqn frnte⟩ auch ⟨sobaldt ∥ scbalqt⟩ wie ⟨unbimicue oder gefdhrliche inden ∥ unbihicse oqer gefahrliche inqen⟩`
- **Proposed:** nicht [?jederzeit] [?abtreten] [?könnte], auch [?sobald] [?sie] [?unbillige?] oder [?gefährliche] [?inten-]
- **English:** ...she/they could not [?withdraw at any time], and as soon as [?she/they] perceived [?unjust?] or [?dangerous] intentions...

### n22_iota.L07

- **Cipher:** `lrqfdb [S:▽] ⟨xdiqjld ∥ xdiqrld⟩ ⟨hgfrufdn ∥ hqfrufdn⟩ zbldttdf pgtld ⟨lldiredgdf ∥ udircdgdf⟩ xdrfdldn db ⟨erd ∥ srd⟩ [S:△] frqul`
- **Literal:** `ticnes [S:▽] ⟨mercrte ∥ mercite⟩ ⟨uonihnef ∥ ucnihnef⟩ astellen wolte ⟨tterideoen ∥ heriqeoen⟩ meinetef es ⟨die ∥ bie⟩ [S:△] nicht`
- **Proposed:** [?tiones] [▽] [?merckte], [?von ihnen] [?abstehen] wolte. [?Hingegen] [?meineten] es [?die] [△] nicht
- **English:** ...of [▽], would [?withdraw from them]. [?Conversely], [△] did not mean it...

### n22_iota.L08

- **Cipher:** `dsdf ⟨bgohl ∥ bqohl⟩ ztbbrd ⟨hgizdsdf dgbohd ∥ hgiadsdf dgbshd⟩ frl xrfhb qgorlzid ⟨ehzx ∥ chzx⟩ [S:circle with vertical stroke, like Φ] ⟨hfel ∥ hfcl⟩ ⟨phiedf ∥ phcdf⟩ brqu`
- **Literal:** `eben ⟨sogut ∥ scgut⟩ alssie ⟨uoraeben eosgue ∥ uorzeben eosbue⟩ nit minus cogitare ⟨duam ∥ quam⟩ [S:circle with vertical stroke, like Φ] ⟨undt ∥ unqt⟩ ⟨wurden ∥ wuqen⟩ sich`
- **Proposed:** eben [?so gut] als sie [?vorgäben], [?eosque] nit minus cogitare [?quam] [Φ], [?undt] [?würden] sich
- **English:** ...quite [?so well as they pretended], and [?they thought no less of ... than of] [Φ]; and... [The comparison's other object is missing/unclear.]

### n22_iota.L09

- **Cipher:** `⟨edidf Wizdldftrqfdb fhet Wgblkzk edkrefinhrodi uzhsluzfethfo erdbrd ∥ cdidf Wizdldfbrqfdb fhct Wgblhtzk sdkqfinlrodi uzhsluzfcthfo crdbrd⟩ fhu hgf dr`
- **Literal:** `⟨deren praetenlicnes nudl postyay deyidnrfuiger haubthandlung diesie ∥ qeren praetensicnes nuql postulay beycnrftiger haubthanqlung qiesie⟩ nuh uon ei`
- **Proposed:** [?deren] [?praetensiones] [?undt] [?postulata] [?bey künftiger] [?Haubthandlung], [?die sie] [?nun] von ei-
- **English:** ...their [?claims and demands] would [?become apparent] at the [?forthcoming principal negotiation], which they [?now]...

### n22_iota.L10

- **Cipher:** `fdi adrl edi ⟨zfedif Wiglizurldf ∥ ztcdif Wiglizurildf⟩ pgt zhbpdxbdn ⟨[S:barred B] g ∥ bq⟩ udlld xzt brqu ⟨zhqitrfWf ∥ zhqufrfWq⟩`
- **Literal:** `ner zeit der ⟨andern protrahiten ∥ alqern protrahirten⟩ wol auswemsef ⟨[S:barred B] o ∥ sc⟩ hette mal sich ⟨aucrlinpn ∥ auchninpc⟩`
- **Proposed:** ner Zeit der [?andern] [?protrahirten], wol [?ausweisen]. [?So] hette [?man] sich [?auch in puncto]
- **English:** ...postponed from one time to [?another]. [?Thus one] should [?also, in the matter of]...

### n22_iota.L11

- **Cipher:** `⟨idtrorgfrb trsdilzlrbzhd ∥ idtrorqfrb trsdilzlribchd⟩ bqpdxfir ah edfdf [S:crossed loop with upright strokes] rqudf ⟨ztbak ∥ ztbah⟩ ⟨edfen ∥ edfsn⟩ [S:▽ with vertical stem and crossbar] edb ⟨sdlldf ak ∥ sdblbf ah⟩`
- **Literal:** `⟨religionis libertatisaue ∥ religicnis libertatirsque⟩ scwemnri zu denen [S:crossed loop with upright strokes] ichen ⟨alszy ∥ alszu⟩ ⟨dendf ∥ denbf⟩ [S:▽ with vertical stem and crossbar] des ⟨betten zy ∥ bestsn zu⟩`
- **Proposed:** [?religionis libertatisque] [?schwerer?] zu denen [crossed-loop]-ischen als [?zu] [?denen] [stemmed ▽] des [?Besten zu]
- **English:** ...[?religion and liberty], [?less readily?] expect the best from those of [crossed-loop party] than from those of [stemmed triangle]. [Comparative adjective unresolved.]

### n22_iota.L12

- **Cipher:** `⟨udibdudf prdeff ∥ ulibdudf prdcff⟩ fqqu ⟨erdlubf ∥ crdbdf⟩ xgiodn [S:arched loop over horizontal bar] lruxed ⟨hfugibduifb ∥ hfuqibdudfb⟩ ezdi [S:∠] fqqu ⟨kzxt ∥ htzt⟩`
- **Literal:** `⟨hersehen wiednn ∥ htrsehen wieqnn⟩ ncch ⟨diethsn ∥ qiesen⟩ morgef [S:arched loop over horizontal bar] tihmde ⟨unhorsehrns ∥ unhcrsehens⟩ daer [S:∠] ncch ⟨yaml ∥ ulal⟩`
- **Proposed:** [?versehen]. [?Wie denn] [?noch] [?diesen] [?Morgen] [arch over bar] [?ihm] [?unversehens], [?da er] [∠] [?noch] [?...]
- **English:** ...as [?indeed this very morning] [arched sign] had [?unexpectedly spoken to him], when [∠] was still [?...]...

### n22_iota.L13

- **Cipher:** `⟨odtdef ∥ odtdcf⟩ odpdbdf ⟨ahotbWiqquef hfef ∥ xhodbWiqqucf hfcf⟩ Wdi ⟨drbqhubhx ∥ drbqhibhx⟩ hfldi ⟨zfedif ∥ zfcdif⟩ idblrlhlrqfdx edi edrbl`
- **Literal:** `⟨geledn ∥ geleqn⟩ gewesen ⟨zuglsprcchdn undn ∥ mugesprcchqn unqn⟩ per ⟨eiscuhsum ∥ eiscursum⟩ unter ⟨andern ∥ anqern⟩ restituticnem der deist`
- **Proposed:** [?gelegen] gewesen, [?zugesprochen] [?undt] per [?discursum] unter [?andern] [?restitutionem] der [?geist-]
- **English:** ...and, in conversation, among other things, had [?strongly defended] the restitution of ecclesiastical...

### n22_iota.L14

- **Cipher:** `trqudf ohldi zferd [S:crossed loop/star-like sign] rbqudf uzil udingquldf udiodgdf zodi ⟨hzfedi ∥ hqfcdi⟩ [S:Θ] [S:open U/V-shaped mark with hook] ⟨idblrlhlgfb ∥ idblrlhlqfb⟩`
- **Literal:** `lichen guter andie [S:crossed loop/star-like sign] ischen hart herfochten hergeoen ager ⟨uander ∥ ucnqer⟩ [S:Θ] [S:open U/V-shaped mark with hook] ⟨restitutons ∥ restitutcns⟩`
- **Proposed:** lichen Güter an die [crossed-loop/star]-ischen hart [?verfochten], [?hingegen] [?aber] [?von der] [Θ] [U/V] [?Restitutions-]
- **English:** ...goods to the [unresolved party], but [?conversely], regarding the [Θ] [U/V] [?restitution]...

### n22_iota.L15

- **Cipher:** `bzqud [S:C-shaped curve with point; possible opening parenthesis] ⟨erd ∥ crd⟩ zdi [S:∠] ⟨hfldibquredtrqu ∥ hfldibqurcdtrqu⟩ xrlntdrb dipdufdl udlld {clear: )} ⟨frqulbugidf pgttdf ∥ frqulbuqidf pqttdf⟩`
- **Literal:** `sache [S:C-shaped curve with point; possible opening parenthesis] ⟨die ∥ qie⟩ aer [S:∠] ⟨unterschidelich ∥ unterschiqelich⟩ mitfleis erwehnet hette {clear: )} ⟨nichtshoren wollen ∥ nichtshcren wcllen⟩`
- **Proposed:** Sache ([?die] [?der] [∠] [?unterschiedlich] mit Fleiß erwehnet hette) [?nichts hören wollen],
- **English:** ...matter (which [∠] had deliberately mentioned [?in various ways]), had [?refused to hear anything]...

### n22_iota.L16

- **Cipher:** `⟨bgfedif ∥ bgfcdzf⟩ brqu ⟨zhbeihgtrqu ∥ zhbeihqtrqu⟩ hdifduxdn eztof xzt xqquld ⟨ezihqf ∥ ezhqf⟩ fhi blrttd ⟨bqapsdiodf ∥ bqapdiodf⟩`
- **Literal:** `⟨sondern ∥ sonqean⟩ sich ⟨ausdruolich ∥ ausdruclich⟩ uernehmef dalgn mal mcchte ⟨darucn ∥ daucn⟩ nur stille ⟨sczwbergen ∥ sczwergen⟩`
- **Proposed:** [?sondern] sich [?ausdrücklich] [?vernehmen] [?lassen], [?man] [?möchte] [?davon] nur stille [?schweigen],
- **English:** ...but had [?expressly let it be known] that [?one should simply remain silent about it]...

### n22_iota.L17

- **Cipher:** `pzf ⟨bgtqudb ∥ bqtqudb⟩ [S:crossed loop with upright strokes] ⟨frxdixdui ∥ frodixdui⟩ [S:struck word; A fdxef, B fdxf] drfodudf ⟨phied hfel ∥ phicd hfcl⟩ zth [S:ink blot] ⟨zhqa ∥ zhqu⟩ ⟨fremmdxdui ∥ frmmdixdui⟩ [S:circle with vertical stroke, like Φ]`
- **Literal:** `wan ⟨solches ∥ sclches⟩ [S:crossed loop with upright strokes] ⟨nimermehr ∥ nigermehr⟩ [S:struck word; A fdxef, B fdxf] eingehen ⟨wurde undt ∥ wurqe unqt⟩ alu [S:ink blot] ⟨aucz ∥ auch⟩ ⟨nidxxemehr ∥ nixxermehr⟩ [S:circle with vertical stroke, like Φ]`
- **Proposed:** [?weil/wann] [?solches] [crossed loop] [?nimmermehr] [struck word] eingehen [?würde undt] [?also] [blot] [?auch] [?nimmermehr] [Φ]
- **English:** ...[?because/if] [crossed loop] would never agree to such a thing, and thus [blot] [?never] [Φ]...

### n22_iota.L18

- **Cipher:** `⟨[S:angle with an X across it] ∥ ∅⟩ ahugnndf ⟨blhfed ∥ blhfcd⟩ {clear: )}`
- **Literal:** `⟨[S:angle with an X across it] ∥ ∅⟩ zuhoffen ⟨stunde ∥ stunqe⟩ {clear: )}`
- **Proposed:** [possible raised crossed-angle mark] zu hoffen [?stünde]).
- **English:** ...could be hoped for). [If Φ is peace, the argument is that this demand prevents hope of peace; symbol meaning remains provisional.]

### n22_kappa.L01

- **Cipher:** `⟨edbfedoidf ∥ edbfdodf⟩ brd [S:△] edf ⟨oizndf ∥ ozndf⟩ ⟨hgfedibsdia ∥ hgfzdibsdia⟩ ⟨hfel ∥ hfcl⟩ [S:arched loop over horizontal bar] rfhdiezqul udlldf [S:A-like arch with hooked crossbar] zhqu ⟨ruxed ∥ ruxd⟩`
- **Literal:** `⟨desndegren ∥ desnegen⟩ sie [S:△] den ⟨grafen ∥ gafen⟩ ⟨uondersberz ∥ uonaersberz⟩ ⟨undt ∥ unqt⟩ [S:arched loop over horizontal bar] inuerdacht hetten [S:A-like arch with hooked crossbar] auch ⟨ihmde ∥ ihme⟩`
- **Proposed:** [?Deswegen] sie [△] den [?Grafen] [?von ...sberg/...] [?undt] [arch over bar] in Verdacht hetten, [A-like arch] auch [?ihm]
- **English:** [?For that reason] they/[△] suspected [?Count von ...] and [arched sign]; [A-like sign] had also... [Name unresolved.]

### n22_kappa.L02

- **Cipher:** `[S:arched loop over horizontal bar] ezb pzt di otdrqu ⟨ruxed ∥ ruxd⟩ bdrfdf fzuxdf ⟨ehqfldi odbdldl ∥ ehfldi odbdlal⟩ udlld di ⟨ruxed pgft ztlpqldf ∥ ruxd pgt ztlpgildf⟩`
- **Literal:** `[S:arched loop over horizontal bar] das wal er gleich ⟨ihmde ∥ ihme⟩ seinen nahmen ⟨ducnter gesetet ∥ dunter gesetzt⟩ hette er ⟨ihmde wonl altwcten ∥ ihme wol altworten⟩`
- **Proposed:** [arch over bar], [?daß was] er gleich [?ihm] seinen Nahmen [?darunter gesetzt] hette, er [?ihm wohl antworten]
- **English:** ...[said] to [arched sign] that, though he had [?put his name underneath it], he would [?answer him]... [Syntax provisional.]

### n22_kappa.L03

- **Cipher:** `pgtld ⟨udrdsjhgif zhbeihgrtrqu bhzdflerdldf ∥ udrdsdhqf zhbeihqrtrqu bhzdflsrdldf⟩ tzbbdn`
- **Literal:** `wolte ⟨heiebruorn ausdruoilich suaentdieten ∥ heiebeucn ausdrucilich suaentbieten⟩ lassef`
- **Proposed:** wolte, [?hiebevorn] [?ausdrücklich] [?zu entbieten] [?lassen].
- **English:** ...had previously [?expressly sent word]. [Sentence not secure enough to identify the underlying exchange.]

### n22_lambda.L01

- **Cipher:** `zhb [S:∠] xrl [S:crossed loop with upright strokes] odnhildx ⟨erbggub ∥ crbqquib⟩`
- **Literal:** `aus [S:∠] mit [S:crossed loop with upright strokes] gefurtem ⟨disoohs ∥ qiscchrs⟩`
- **Proposed:** Aus [∠] mit [crossed loop] geführtem [?Discours].
- **English:** From a conversation conducted by [∠] with [crossed loop].

### n22_mu.L01

- **Cipher:** `urq ⟨edndidsdll rherqrhx ∥ edndidsdl rhcrqrhx⟩ [S:△] ⟨ed ∥ edl⟩ [S:o°o] di ⟨aijfd ∥ aiqfd⟩ rhfdf frqul ⟨erd duud ∥ crd duid⟩ drfdf ⟨sdtbdin ∥ sdtdiw⟩ [S:circle with vertical stroke, like Φ]`
- **Literal:** `hic ⟨deferebett iudicium ∥ deferebet iuqicium⟩ [S:△] ⟨de ∥ det⟩ [S:o°o] er ⟨zrrne ∥ zrcne⟩ iunen nicht ⟨die ehhe ∥ qie ehre⟩ einen ⟨belserf ∥ belerp⟩ [S:circle with vertical stroke, like Φ]`
- **Proposed:** Hic [?deferebat iudicium] [△] [?de] [o°o]: er [?...] [?ihnen] nicht [?die Ehre], einen [?bessern] [Φ]
- **English:** Here he [?reported the judgement] of [△] concerning [o°o]: he [unread verb] them not [?the honor] of making a [?better] [Φ]...

### n22_mu.L02

- **Cipher:** `ahxzqudf ztbdi ⟨udrsdhgif ∥ icdrsdhqif⟩ ah [S:two crosses on one bar] ⟨bg ∥ bq⟩ ⟨pdidlb ∥ pdtddb⟩ zhqu xrl edi ⟨stjldf ∥ stqldf⟩ zxfdblrz gedl`
- **Literal:** `zumachen alser ⟨heibeuorn ∥ rqeibeucrn⟩ zu [S:two crosses on one bar] ⟨so ∥ sc⟩ ⟨werets ∥ welees⟩ auch mit der ⟨blrten ∥ blcten⟩ amnestia odet`
- **Proposed:** zu machen als er [?hiebevorn] zu [double cross]. [?So] [?wäre es] auch mit der [?bloßen] amnestia [?oder]
- **English:** ...than he formerly [made] at [double cross]. [?Thus] [?nothing would be achieved] with mere amnesty or...

### n22_mu.L03

- **Cipher:** `zhqu idblrlhlrqf ⟨zozt?x ∥ zoztdx⟩ {clear: ⟨9896 ∥ 9096⟩.} frqul zhbodirquldl brfldxzt izerm xztr ⟨erd ∥ crd⟩ oizhz`
- **Literal:** `auch restituticn ⟨agal?m ∥ agalem⟩ {clear: ⟨9896 ∥ 9096⟩.} nicht ausgerichtet sintemal radix mali ⟨die ∥ qie⟩ graua`
- **Proposed:** auch [?restitution ...] ⟨9896/9096⟩ nicht ausgerichtet, sintemal radix mali [?die] grava-
- **English:** ...also [?restitution ...] ⟨9896/9096⟩, since the root of the evil, the public grievances... [Numeral left uninterpreted.]

### n22_mu.L04

- **Cipher:** `xrfz Whserqz ⟨hqf ∥ hgf⟩ {clear: 24.} {clear: ⟨9888 ∥ 9088⟩.} ⟨udjhidlef ∥ udjhidlcf⟩`
- **Literal:** `mina pubdica ⟨ucn ∥ uon⟩ {clear: 24.} {clear: ⟨9888 ∥ 9088⟩.} ⟨heruretdn ∥ heruretqn⟩`
- **Proposed:** mina [?publica] [?von] 24. ⟨9888/9088⟩ [?herrührten].
- **English:** ...arose [?from] 24. ⟨9888/9088⟩. [No date or numeric-code solution asserted.]

## Verification and audit

The settled TSV was hashed in `PREDECODE_SHA256SUMS` before the new mechanical decode. `decode.py` verifies that manifest before applying the unchanged key, and leaves descriptions/clear text untouched. `difference_ledger.tsv` records all A/B disagreements; `readings.json` records the separate editorial proposals.

```sh
python3 -I crops/n22_reconcile/decode.py
python3 -I crops/n22_reconcile/render.py
```

Run from this project folder with the full relative path prefixed as needed. These scripts only rewrite this group’s new mechanical/report artifacts. Source, reader and derivative hashes are in `crops/n22_reconcile/SHA256SUMS`. No independent new validation statistic is claimed.
