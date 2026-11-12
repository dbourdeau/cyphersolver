# LOG b173_biermann_195e. Times UTC (date -u). Nothing sent or posted. python3 -I; plain curl, each image fetched once.
Thu Nov 12 16:01:11 UTC 2026 Start. Read b171 LOG.md (incl. sign-reading notes) + PARKED.tsv, b165 PARKED.tsv, b171 copies of b165/b152 scripts (full, crop, zoom, dec_once, kt2, mkseg, ledger, toklist, mkpack, shuffle_de152, spec234), b152 ao152.py head. Key copied unchanged from b171/frozen:
38c7c1e592843cb7f2f3f9dd0f23b987  frozen/table_M3.json
e9698159feb8b7f6c0ddd89e8ccc3a97  frozen/words_FROZEN_v4.json
4d38a72d94ade07ec483c72de09cac57  scripts/kt2.py
Thu Nov 12 16:01:24 UTC 2026 Fetched 247-250 once (plain curl via full.py); md5 in dl/HASHES.md5
Thu Nov 12 16:06:14 UTC 2026 260195 img 248R-250R. FROZEN tx/kl_195_248_tx.txt md5 8d79e2f31840fa5a43a3ebd636e196dd at Thu Nov 12 16:06:14 UTC 2026; DECODE ONCE at Thu Nov 12 16:06:14 UTC 2026 -> work/decode_195_248_ONCE.txt
Thu Nov 12 16:07:27 UTC 2026 Judged ONCE (mkseg + ledger, first run):
S: word units 122; tokens 307
E: word units 21; tokens 75
N: word units 0; tokens 0
units 143 tokens 382 of 382
 E glossed-but-wrong: hafen 4 + satisfaction 8 + unternommenen 9 + darinnen 5 + angelegenen 6 + geneigt 5 + oft 3 + offentlichen 8 + falle 2 = 50
 E unread/unmapped: le 1 + [211] 1 + [181]sen 3 + cooperati 6 + [211] 1 + on 2 + [34]n 2 + gegen[110] 2 + [418] 1 + [110] 1 + gegeniten 4 + [189] 1 = 25
 N: 
 S units by token length: 62x1 + 11x2 + 18x3 + 17x4 + 4x5 + 3x6 + 1x7 + 2x8 + 1x9 + 2x10 + 1x11 = 307 tokens in 122 units
Thu Nov 12 16:07:42 UTC 2026 248: strict S 122 / 143 = 85.31% (E 21, N 0); tokens 307/382. Shuffle 0/5000 both seeds (true -4.0237; best -4.1848 / -4.3326). Content: wintering of the Dutch ships in Danish harbours [NAVY]; help to satisfaction for extraordinary costs of the war; Elector's cooperation; States General to bind themselves, not to make [peace] with Sweden until their aim attained and all restored to the state before the Brömsebro treaties; King inclined to the States; Sweden an open or secret enemy; take from that crown the means to harm them; assurance of assistance; secret treaties between the States and Sweden rumoured.
NOTE (not applied): '[' decodes to f in all 3 readable places (o[fen, o[t, o[fentlichen): key observation only. 485 'mu' fits 'ne' in geneigt, angelegenen, darinnen, unternommenen but 'mu' fits in muglichen. Insert placement split 'cooperati|on' (insert belongs elsewhere, probably after 'darinnen'); scored as placed, 2 E units. Figure of record stands.
Thu Nov 12 16:08:16 UTC 2026 Prior art 248: git -C cs grep -l origin/main '260195|4857445[5-8]' -> only targets/lorraine1592/src/fr4ns.json (unrelated float, as b171). Local OCR (b91 dl: dm_bind16, frid_djvu, Danske Magazin): Bromsebro/Klingenberg hits unrelated (one Fridericia line on Klingenberg as postmaster). Clear as far as checked.
Thu Nov 12 16:08:16 UTC 2026 260195 img 247R. FROZEN tx/kl_195_247_tx.txt md5 d46fe356267651d1d394ab7c92199830 at Thu Nov 12 16:08:16 UTC 2026; DECODE ONCE at Thu Nov 12 16:08:16 UTC 2026 -> work/decode_195_247_ONCE.txt
Thu Nov 12 16:08:31 UTC 2026 Judged 247 ONCE (mkseg + ledger, first run):
S: word units 40; tokens 106
E: word units 8; tokens 31
N: word units 0; tokens 0
units 48 tokens 137 of 137
 E glossed-but-wrong: keine 2 + unbillig 5 + dienen 3 + erfahrung 8 + gelernet 5 + angezogenen 6 = 29
 E unread/unmapped: [280] 1 + [151] 1 = 2
 N: 
 S units by token length: 23x1 + 2x2 + 5x3 + 2x4 + 1x5 + 3x6 + 2x7 + 1x8 + 1x11 = 106 tokens in 40 units
Thu Nov 12 16:08:42 UTC 2026 247R: strict S 40 / 48 = 83.33% (E 8, N 0); tokens 106/137. Shuffle 0/5000 both seeds (true -4.1315; best -4.4177 / -4.4088). Content: promotion of their commerce; no unreasonable means to raise [?]; the States themselves have learnt by experience the harm Sweden did them, helping it to the advantages gained in the Brömsebro treaties. NOTE (not applied): 485 'mu' where 'ne' fits again (dienen, gelernet, angezogenen); 'x'(m) in erfahrumng. Prior art: same cs grep (api 48574455 covered), clear.
Thu Nov 12 16:09:40 UTC 2026 FILED packs klingenberg_late_sep1675_dutch_ships_draft + klingenberg_late_sep1675_commerce_bromsebro_leaf (+ FILE_NOW). Images 247-250 deleted (md5 kept). Neighbours: 247L French to Gioe (30 Sept, skip); 251-252 German clear on sheet (not fetched).
Thu Nov 12 16:09:50 UTC 2026 Fetched 253-254 once.
Thu Nov 12 16:11:05 UTC 2026 253R (P.S. 'Auch Hochedelgebohrner ... Plenipotentiaire', NAVY: Swedish fleet 20 ships to sail; cipher 5 rows at foot, ~45 tokens, same phrase 'ob solten zwischen [den Staten und Schweden ...]' as 250R) continues on 254L (cipher ~90 tokens). 254L cipher column is largely illegible: heavy mirror show-through of 253R plus overstriking and overwritten numbers (e.g. r1 '491?', r2 '482?', r5 '414?', row '940/359?'). Not transcribed, not decoded (no freeze): PARKED for a better image or a second reader. 254R docket to Klingenberg Sept 1675 (sheet). Images 253-254 deleted (md5 kept).
klingenberg_late_sep1675_dutch_ships_draft parse OK; tx md5 8d79e2f3 text==md5 True file==md5 True pack md5 e926fc1e
klingenberg_late_sep1675_commerce_bromsebro_leaf parse OK; tx md5 d46fe356 text==md5 True file==md5 True pack md5 f5d1aaea
Thu Nov 12 16:11:21 UTC 2026 Pre-publish check: key md5s 38c7c1e5/e9698159/4d38a72d match; 2 tx files match tx/FROZEN.md5; packs parse, md5s consistent (above). dl/ holds only HASHES.md5; folder 7.4 MB. PARKED.tsv written. STOP (context budget). Nothing sent, posted or stamped.
