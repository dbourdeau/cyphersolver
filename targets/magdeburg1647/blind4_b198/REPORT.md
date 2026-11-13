# REPORT b198: blind fourth reading, Magdeburg slips, LASA A 1 Nr. 530 (f.102, f.104, f.204)

Reader b198 (Claude Fable). Written 13 Nov 2026 UTC. Times in LOG.md are UTC.

## Bottom line

- All three slips fall below the 65% line on the first-pass strict count: f.102 33/84 = 39.29%, f.104 49/100 = 49.00%, f.204 25/52 = 48.08%. [measured]
- Shuffle control: 0 of 5,000 random keys score at or above the true decode, at both seeds, for every slip. [measured]
- The gap between the two is my transcription, not the key. Most E words differ from German by one letter in the hard pairs I flagged before the freeze, chiefly c/e (for example decoded "qie", "qurch", "herjen"). [derived] Nothing was emended; the frozen files stand.

## Disclosures on blindness

- The key was printed in the task text (step 3), so it was visible to me before the freeze. I ran no decode and wrote no plaintext before the freeze. [stated]
- While reading the image I noticed that the capital W behaves as an ordinary letter. No other pre-freeze inference about content was used. [stated]
- I opened nothing under trackB except my own folder, and did not read EN-DECISIONS.md or EN-STATE.md. During the run the shell working directory was reset by the system to other trackB paths; I listed and read nothing there. [stated]
- Project check tool: stamps/stamp.sh was run for the freeze and for the result. There is no separate check tool for transcriptions. [stated]

## Rules fixed for the count

- Units are cipher words as divided in the frozen files. Clear German text, struck-out matter and symbols are not units. N = 0 as instructed.
- S: German or Latin word as it stands (u/v, i/j, dt, th; names; run-together words where every part reads).
- SP: counted as S only through a common 17th-century spelling outside the four listed (bey, tz, wolte/solte, were, umb, no umlaut, aw). Listed separately so they can be recounted.
- E: everything else, including line-end fragments (de, inter, osna, behal and so on), single letters, and words one letter off.
- The slips contain nomenclator symbols of the kind listed in the frame 3 Catalogus (f.102: 14, f.104: 11, f.204: 7). These are word codes I cannot read. A supplementary figure with symbols as N is given.

## Per slip figures

| Slip | Words | S | SP | E | Figure of record (S+SP)/(S+SP+E) | Listed spellings only S/all | Symbols as N | Shuffle seed 20261112 | Shuffle seed 7 |
|---|---|---|---|---|---|---|---|---|---|
| f.102 | 84 | 22 | 11 | 51 | (22+11)/(22+11+51) = 33/84 = 39.29% | 22/84 = 26.19% | 33/98 = 33.67% | 0/5000 | 0/5000 |
| f.104 | 100 | 34 | 15 | 51 | (34+15)/(34+15+51) = 49/100 = 49.00% | 34/100 = 34.00% | 49/111 = 44.14% | 0/5000 | 0/5000 |
| f.204 | 52 | 21 | 4 | 27 | (21+4)/(21+4+27) = 25/52 = 48.08% | 21/52 = 40.38% | 25/59 = 42.37% | 0/5000 | 0/5000 |

Shuffle detail (German 4-gram model, add-0.1 smoothing, letters plus space, umlauts folded, 5,000 random 26-letter permutations per seed):

- f102: 604 characters, true log-probability -1968.93; best shuffle -2071.42 (seed 20261112) and -2084.93 (seed 7); mean shuffle -2287.10 and -2285.86.
- f104: 805 characters, true log-probability -2431.70; best shuffle -2771.42 (seed 20261112) and -2774.70 (seed 7); mean shuffle -3032.02 and -3030.92.
- f204: 353 characters, true log-probability -990.00; best shuffle -1217.80 (seed 20261112) and -1220.90 (seed 7); mean shuffle -1335.50 and -1335.12.
- Corpus: Project Gutenberg pg5323 (Effi Briest, German), md5 e966df334531570ffaaf4b4466ce2494, 566801 characters after cleaning, function-word share 0.11 (language check passed).
- What this test shows: the key turns my letter strings into German-like text far beyond chance. It does not test the symbols and does not show that any single word is read.

## Freeze

```
2026-11-13T11:32:41Z
554a5cd3ea8a303ba108f04402d63494  tx/f102.txt
a66738b89b05c692b3dcca24668da006  tx/f104.txt
339e12012cec6f7f15af28039429a1c1  tx/f204.txt
85d057152e3f2000e1926b066cee140dce301fabff416ea8fe4c13fed413d388  tx/f102.txt
aa122aae3590a0e47e2c49b170d2a5301e0cee5804c9d065713025ae6bdafa56  tx/f104.txt
7c25b80e00a6889c06b907ce45dd31a25e3d9cac84a18e7058f2921f47e50d69  tx/f204.txt
```
Stamp label magdeburg_blind4_freeze: manifest SHA-256 9817e4172ef8300cb01cebe7dc31a68f687e900ed644995301cb7305df204d9a, Sectigo RFC 3161 granted 13 Nov 2026 11:32:42 GMT, OpenTimestamps submitted.

## Transcriptions (as frozen)

### f102
```
# LASA A 1 Nr. 530 f.102 (frame 0118). Blind transcription b198. Conventions: [x?] doubtful letter read as x; # illegible; {S:name} nomenclator symbol; {clear} German clear text not transcribed; {del} struck-out matter; capitals W K O as written.
01 {clear} [c?]di udijdf id[n?]qix rildn edWhlrild sdK {S:triangle} {S:gammagamma} ruid ed
02 ch[g?]lr[g?]f hsdiodsdn udl[r?]d {S:circledot} fz[q?]uxztb xrl pdbdfsdqrg pdodf b ahbqudiladf zfd
03 nzfodn czizhn {S:ladder} {S:gamma} bquzi[n?]fdi {clear}
04 {clear} xdcrzl[g?]idb icrdijrfdf odsizh[q?]ul p[k?]icdn hfl[g?]
05 [O?]rhf czinhi zfduxdf p[g?]tld {clear}
06 {clear} {S:starcross} [h?]xs b oi[g?]bahluhf pdid pzfbrd cziodgdf crd {S:spectacles} oigbotgozp uf[e?]l
07 bzoaf fdsbl fdpdi {del} rfhd[l?]blrlhi [u?]ne[t?] qgfnrixzlr[g?]f [h?]isdi izodif[e?]qin
08 hfdl qiqbdf {del} prd rf[r?]tdrqudf xzo[c?]dshid a[i?]tsdiblzl sidxdf hduicdn gbfz
09 sih[g?]y hf[e?]t xrf[e?]df sdydxdn {clear}
10 {clear}
11 {clear} {del} {S:ellipse} {S:triangle} bdtsbl pdodf {S:crossedsquare} hf[e?]l {del} hduicdf {del} rfldi
12 dbr[i?]dl {clear}
13 {clear} {S:quadrilateral} {S:blot}
14 qzflatzi egqlg##ldrf {clear}
15 {clear} {S:stararrow} dzfr qhx {S:pentagram} trqrb bWrirlh hdilrorfrb
16 odl[i?]rsdf {clear} ruxdh[u?]f udiladn {del} ozfodn
17 g[e?]di Wign[q?]ixz hdt dmWt[g?]izf[e?]r qzhbz odid[e?][e?]l p[g?]icdf {clear}
```

### f104
```
# LASA A 1 Nr. 530 f.104 (frame 0121). Blind transcription b198. Conventions as f102. {ins} marks an interlinear insertion joined at its place.
01 czichiqu brdruxd {del} ztldiuzf[e?]l bdtlazxd odczfqydf gdxzqudl ztbpz
02 p[g?]tozt drfdi h[g?]fodf udijdf tdozlrb zhn crd hrdi blidrlrodf hfrlhdixdrfld xrf
03 crbqudl{del} tdufblh[q?]ydn ah bdrfdi idq[g?][g?]xWdfb drf zsbdudn uzsdf xgqald
04 SdKpdtqudi ggqzbrgf diruxd zhqu crdbds rfugudx hdilizpdf sdirquldl diudh[l?]
05 h[g?]fdrfdx {S:starcross} hdiblzf[c?]dn ztbpzt rufdf hgfedfdn {S:triangle} {S:gammagamma} hfldi zfcdin {del} {S:bowtie} ahiod
06 gdfbzlrbnz[q?]lr[g?]f {del} nhiodbqutzodf pdid eg[q?]uczb{ins}db {S:doubleM} z[e?][e?]rdb hrizd hdistdrsdf
07 b[g?]tld [P?]drtzsdi hrdsdh[g?]i sdirquldl[c?]r xzbdf bgpgt {S:gammagamma} bdtsbl odgcdn xri ztbzhqu
08 {S:sun} {del} gdo[c?]n {S:spiral} {S:zigzagM} hfila[t?]zi zhb {S:gammagamma} fzqu bqupd[c?]df zsod[q?]zfofdn idtzbrgf
09 odiz[c?]d czb[q?][g?]f{del}lizirhx sdirquldl ztbbqud[r?]fdl hdixhlutrqu czbbgtqudb h[g?]fcdn
10 {S:starcross} Wgbl idWhtbzx Wig cdqtrfzf[c?]z bhz zt[r?]bchd q[g?]fqrtrzf[c?]z rfhrcrz ztbg
11 zhbodgds[e?]f pdi[c?]d
12 srbbrqu dlpz[f?] drf[d?] nhotrqud [q?][q?]qzbr[g?]f zfdrfdx xhfbldirbqudf shiodi g[e?]h
13 rf zf[i?]rlid pdoc dbahhrfcrqridf didhofdld
```

### f204
```
# LASA A 1 Nr. 530 f.204 (frame 0233). Blind transcription b198. Conventions as f102.
01 odbpdodf zhqu prd[l?]di n[q?]todf[r?]df lzodf crd udijdf odbzfldn
02 [c?]hiqu xrqu rfugudx hdilizpdf dl Wig [q?]dilg sdirquldf zhqu {S:halfcirclebar}
03 bdtsbl brqu hdlfduxdn tzbdf crd[t?]d odnzuitrqul q[g?]fbrtrz gsuzfcdf
04 pdidn [c?]zbxzf trdsdi {S:triangle} crd dila hf[e?]l bl[r?][r?]ldi {S:crossedsquare} {S:threebarbox} hf[e?]lzhqu
05 {S:doublesquare} ahi id[y?][q?]xWdfb urfodsdf b[g?]tld fhi czxrl crd {S:pentagram} sdKzf[c?]df
06 f[g?]qu rfuzsdf[c?]dn hf[c?]t odfrbdf[c?]df ohldin stdrsdf {S:starcross} zsdi b sduzt
07 Wdf x[g?]qald
```

## Decodes (one pass, frozen key, doubtful letters decoded as read)

### f102
```
01 qer* herjen* refcrm* irtef* deputirte bey ihre de*
02 quotion* ubergebef* hetie* nachmals mit wesenbecio wegen s* zuschertzen ane*
03 fangef* qarauf* scharfner*
04 meqiatores* rqierjinen* gebraucht wyrqef* unto*
05 giun* qarfur* anehmen* wolte
06 umb s* groszuthun were wansie qargeoen* qie* grosglogaw hndt*
07 sagzn* nebst newer inuetstitur* hfdl* confirmation urber* ragerndcrf*
08 unet* crcsen* wie inileichen* magqebure* zrlberstat* bremen uehrqef* osna*
09 bruok* undl* minden bekemef*
11 selbst wegen undt uehrqen* inter*
12 esiret*
14 cantzlar docto##tein*
15 eani* cum licis* spiritu uertiginis
16 getriben ihmeuhn* hertzef* gangef*
17 oder profcrma* uel explorandi causa gereddt* worqen*
```
* marks a word counted E. Full ledger: dec/f102.ledger.tsv.

### f104
```
01 qarqurch* sieihme alterhandt* seltzame geqancken* oemachet* alswa*
02 wolgal* einer uongen* herjen* legatis auf qie* uier streitigen unituermeinte* min*
03 qischet* lehnstuckef* zu seiner recoompens* ein absehef* haben moczte*
04 beywelcher oocasion* erihme auch qieseb* inhohem uertrawen berichtet erheut
05 uoneinem uerstanqef* alswal* ihnen uondenef* unter anqerf* zurge*
06 oensatisfaction* furgeschlagen were dochqases* addies* uirae* uerbleiben
07 solte weilaber uiebeuor* berichtetqi* masen* sowol selbst geoqef* mir alsauch
08 oegqf* unrtzlar* aus nach schweqen* abgecangnef* relasion*
09 geraqe* qascontrarium* berichtet alsscheinet uermuthlich qassolches* uonqef*
10 post repulsam pro qeclinanqa* sua alisque* concilianqa* inuiqia* also
11 ausgeoebdn* werqe*
12 bissich etwan eine fugliche cccasion* aneinem munsterischen burger odu*
13 in anritre* wegq* eszuuinqiciren* ereugnete
```
* marks a word counted E. Full ledger: dec/f104.ledger.tsv.

### f204
```
01 geswegen* auch wieter* fclgenien* tagen qie* herjen* gesantef*
02 qurch* mich inhohem uertrawen et pro certo berichten auch
03 selbst sich uetnehmef* lasen qiele* gefahrlicht* consilia obhanqen*
04 weref* qasman* lieber qie* ertz undt stiiter* undtauch
05 zur rekcmpens* hingeben solte nur qamit* qie* beyanqen*
06 noch inhabenqef* unql* genisenqen* guterf* bleiben aber s* behal*
07 pen* moczte*
```
* marks a word counted E. Full ledger: dec/f204.ledger.tsv.

## Every doubtful or illegible letter

### f102: 39 doubtful letters, 2 illegible, in 36 words

`01 [c?]di`, `01 id[n?]qix`, `02 ch[g?]lr[g?]f`, `02 udl[r?]d`, `02 fz[q?]uxztb`, `03 bquzi[n?]fdi`, `04 xdcrzl[g?]idb`, `04 odsizh[q?]ul`, `04 p[k?]icdn`, `04 hfl[g?]`, `05 [O?]rhf`, `05 p[g?]tld`, `06 [h?]xs`, `06 oi[g?]bahluhf`, `06 uf[e?]l`, `07 rfhd[l?]blrlhi`, `07 [u?]ne[t?]`, `07 qgfnrixzlr[g?]f`, `07 [h?]isdi`, `07 izodif[e?]qin`, `08 rf[r?]tdrqudf`, `08 xzo[c?]dshid`, `08 a[i?]tsdiblzl`, `09 sih[g?]y`, `09 hf[e?]t`, `09 xrf[e?]df`, `11 hf[e?]l`, `12 dbr[i?]dl`, `14 egqlg##ldrf`, `16 odl[i?]rsdf`, `16 ruxdh[u?]f`, `17 g[e?]di`, `17 Wign[q?]ixz`, `17 dmWt[g?]izf[e?]r`, `17 odid[e?][e?]l`, `17 p[g?]icdf`

### f104: 40 doubtful letters, 0 illegible, in 33 words

`01 ztldiuzf[e?]l`, `02 p[g?]tozt`, `02 h[g?]fodf`, `03 tdufblh[q?]ydn`, `03 idq[g?][g?]xWdfb`, `04 diudh[l?]`, `05 h[g?]fdrfdx`, `05 hdiblzf[c?]dn`, `06 gdfbzlrbnz[q?]lr[g?]f`, `06 eg[q?]uczb{ins}db`, `06 z[e?][e?]rdb`, `07 b[g?]tld`, `07 [P?]drtzsdi`, `07 hrdsdh[g?]i`, `07 sdirquldl[c?]r`, `08 gdo[c?]n`, `08 hfila[t?]zi`, `08 bqupd[c?]df`, `08 zsod[q?]zfofdn`, `09 odiz[c?]d`, `09 czb[q?][g?]f{del}lizirhx`, `09 ztbbqud[r?]fdl`, `09 h[g?]fcdn`, `10 cdqtrfzf[c?]z`, `10 zt[r?]bchd`, `10 q[g?]fqrtrzf[c?]z`, `11 zhbodgds[e?]f`, `11 pdi[c?]d`, `12 dlpz[f?]`, `12 drf[d?]`, `12 [q?][q?]qzbr[g?]f`, `12 g[e?]h`, `13 zf[i?]rlid`

### f204: 21 doubtful letters, 0 illegible, in 18 words

`01 prd[l?]di`, `01 n[q?]todf[r?]df`, `02 [c?]hiqu`, `02 [q?]dilg`, `03 crd[t?]d`, `03 q[g?]fbrtrz`, `04 [c?]zbxzf`, `04 hf[e?]l`, `04 bl[r?][r?]ldi`, `04 hf[e?]lzhqu`, `05 id[y?][q?]xWdfb`, `05 b[g?]tld`, `05 sdKzf[c?]df`, `06 f[g?]qu`, `06 rfuzsdf[c?]dn`, `06 hf[c?]t`, `06 odfrbdf[c?]df`, `07 x[g?]qald`

Notes on the doubts:
- c/e, g/q, t/l, i/r and final f/n as described in SHAPES.md.
- "ij" (two dotted minims, second descending) is transcribed i+j in udijdf (three times) and icrdijrfdf. The decode suggests the scribe meant two i. Left as frozen.
- f.102 line 5 [O?]: a circle with a dot, attached to "rhf"; it may be the circle-dot symbol rather than a letter.
- f.102 line 14 ##: two letters under ink blots, possibly deletions.
- The lone "b" with a looped cross-stroke (f.102 lines 2 and 6, f.204 line 6) may be an abbreviation sign rather than the letter b.
- f.104 line 6: "db" is written above the line and joined to eg[q?]uczb at its place.
- f.104 line 8: a capital M-like zigzag after the spiral is taken as a symbol, and ":/" before hfila[t?]zi as punctuation.
- Words at the right edge (f.102 zfd, hfl[g?]; f.104 diudh[l?], g[e?]h) run into the dark margin of the scan.

## What I opened (complete list)

- Task text and attached context only. No memory files read.
- /home/claude/en/EN-SYSTEM.md, first 60 lines (general method).
- /home/claude/en/stamps/stamp.sh: existence checked and executed twice; contents not read.
- Five images, one plain GET each, from recherche.landesarchiv.sachsen-anhalt.de/images//A_1/Nr_530/max/: frames 0118, 0121, 0233, 0003, 0051 (md5s in LOG.md).
- https://www.gutenberg.org/cache/epub/5323/pg5323.txt, one plain GET.
- My own folder: img/, crops/ (Pillow crops of the five frames), tx/, dec/, scripts/, corpus/.
- Nothing else under /home/claude/en/trackB/. Not EN-DECISIONS.md, not EN-STATE.md. No web search. No decode, reading, word list or score by anyone else.

