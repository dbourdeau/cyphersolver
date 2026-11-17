"""Write proposals for the HHStA Türkei I cluster leads 1221-1225 from the Hungaricana harvest (raw/h_sifrir.jsonl,
raw/datecheck.jsonl, raw/regests.jsonl, raw/cluster_stats.txt)."""
import json, subprocess, sys
BY = 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting'
stats = {l.split(':')[0]: l.split(':', 1)[1].strip() for l in open('raw/cluster_stats.txt', encoding='utf8') if l[:4].isdigit()}

COMMON_PA = {
 'decode': 'known.py (DECODE dumps and the repo ledgers) on the envoys\' names (Ungnad, Sinzendorff, Breuner, Eizing, Pezzen, Kreckwitz, Starzer) and Türkei I: DECODE holds only keys for this embassy (Ungnad R392, Breuner R1384, R1590), no record of these despatches; the catalogue holds single letters of the series (342, 343, 2237, 2675, 2676) and the later clusters 1226-1229.',
 'tomokiyo': 'Tomokiyo\'s unsolved.htm (fetched 15 Nov 2026) grepped for the envoys\' names and Türkei: no hit.',
 'lasry': 'Lasry\'s GL.htm list (fetched 15 Nov 2026) grepped for the same names: no hit.',
 'edition': 'The decisive prior art is in the archive itself: the Hungaricana regests of the Viennese inventory (Bécsi Magyar Levéltári Kirendeltség) list, beside the cipher copies marked \'feloldás nélkül\', the same despatches deciphered (\'német feloldás\', \'sifrír és külön feloldás\'), mostly in the parallel letter to Archduke Ernst or Matthias, or as clear copies and extracts of the same day. Some deciphered pieces are printed in part in Hurmuzaki, Documente (cited in the regests). Lang 2015 (MTA doctoral thesis, repertory pp. 252-255, downloaded 16 Nov 2026) lists only Ungnad, Sinzendorff, Breuner and Starzer samples (C.Ung, C.Sin, C.Breu, C.Sta), none of Eizing, Pezzen or Kreckwitz.',
 'literature': 'Earlier web searches recorded on the lead (Láng, Real Life Cryptology 2018; Szabados 2023; ABTK envoy-report editions) found no printed decipherment; the Fazekas-Fodor-Gluck edition covers 1568-1574 only. No further literature search was needed once the archive\'s own decipherments were found.'}


def block(lead, seen_where, extent, cipher, verdict, closed, key_check, dups, searches):
    return {'date': '2026-11-16', 'by': BY,
            'seen': {'kind': 'not online', 'where': seen_where, 'extent': extent, 'cipher': cipher},
            'prior_art': COMMON_PA, 'key_check': key_check, 'duplicates': dups, 'verdict': verdict, 'closed': closed,
            'searches': searches}


SEARCH = [{'query': 'Hungaricana archives search "sifrír*" (2,633 regests, all pages, per_page=100), filtered to Türkei I by Karton',
           'result': 'Cipher regests grouped by despatch date; dates whose only regests say \'feloldás nélkül\' tested further.'},
          {'query': 'Hungaricana search on each such date string ("YYYY.MM.DD"), every Türkei I regest of that date fetched in full',
           'result': 'Clear copies, extracts and decipherments of the same day found for most dates (see note).'}]

P = {}
P['1221'] = {
 'verdict': 'partly_read', 'confidence': 'medium',
 'note': 'Hungaricana answers scripts from this machine (16 Nov 2026), so the whole cluster was re-checked regest by regest: ' + stats['1221'] + '. Spot checks show decipherments also hide under range-dated regests (e.g. Sinzendorff 23 Nov 1579, 48863, has Reisach\'s extracts 48862 and a Latin extract 48864 of the same report). As a cluster it is mostly read at the time; the eight residual dates are not proven unread and would each need the parallel Archduke letter checked before a single-letter lead could be split out.',
 'access': 'archive', 'access_note': 'HHStA Wien, not digitised (AIS records stop at Konvolut level, checked by curl 16 Nov 2026); Hungaricana regests answer curl.',
 'residual_dates': '1577.11.14 (48141, triplicate duplicates), 1577.11.23 (48170, \'német másolat és orig.\': a German copy is with it, so read), 1579.01.25 (48506 duplicate), 1579.06.18 (48650), 1579.08.25 (48762 duplicate), 1580.06.01 (49073), 1581.03.18 (49330 triplicate to Ernst), 1581.09.20/10.04 (49483, 49484)'}
P['1221']['vetting'] = block(1221,
 'Hungaricana Viennese-inventory regests (archives.hungaricana.hu/en/lear/BecsSeg/<id>/), harvested by script 16 Nov 2026: all 375 Türkei I cipher regests of Kt. 36-45 from the \'sifrír*\' search, plus full regests of every same-date item for the 30 dates whose cipher regests all say \'feloldás nélkül\'; neighbours read in full for 48858-48868 and 48646-48654, 49069-49077.',
 'Kt. 36-45 (1577-1581): 79 regests say no decipherment, on 59 despatch dates; the despatches run from 2 to 30 folios.',
 'The regests describe the pieces as \'sifrír, feloldás nélkül\' or \'nincs feloldva\' (cipher, no decipherment), many as duplicates or triplicates sent by Venice or Buda; the same Konvoluts hold \'sorközben feloldva\' copies and \'német feloldás\' decipherments, often in the parallel letter to Archduke Ernst.',
 'partly_read', 'Most of the despatches the cluster counts as undeciphered have a deciphered or clear copy of the same date in the same Kartons (25 dates by a deciphered cipher copy, 22 more by a clear copy, extract or decipherment found by date search); the eight residual dates are unproven and a cluster cannot enter the catalogue, so the lead is closed as read in part.',
 'Candidate keys held: Ungnad R392 and Breuner R1384 (DECODE, transcribed in targets/ungnad1576 and targets/sinzendorff1578); untested, no scans. The contemporary decipherments in the same Kartons are the stronger key source.',
 'Catalogue 343 (Sinzendorff 3-7 Sept 1578, Kt. 37 Konv. 2) lies inside this range and is one of its letters; catalogue 342 (Ungnad 1576, Kt. 32) is just before it. No other duplicate.', SEARCH)

P['1222'] = {
 'verdict': 'read', 'confidence': 'high',
 'note': 'Every regest in Kt. 46-49 marked \'feloldás nélkül\' has a decipherment of the same despatch in the same Konvolut: Breuner 21-28 Apr 1582 (49599) by 49597 (to Ernst, \'német feloldás és sifrír\'); the cipher extract of 24 Aug 1582 (49680) by the clear original 49681; the duplicate of 12 Oct 1582 (49717) by 49718-49719; 3 Dec 1582 (49751) by 49752; 12 May 1583 (49853) by 49856; 27 Jul 1583 (49905) by 49907; Pezzen 4 Sep 1583 (49930, 49932, 49933) by 49936. Also for the lead agent: catalogue 2237 (Breuner 12 May 1583, fol. 137-144, 147-151) is regest 49853, and 49856 is Breuner to Ernst of the same day \'feloldás és sifrír\' sharing fol. 147-151, so 2237 looks read at the time and should be re-checked.',
 'access': 'archive', 'access_note': 'HHStA Wien, not digitised; Hungaricana regests answer curl (16 Nov 2026).'}
P['1222']['vetting'] = block(1222,
 'Hungaricana regests 49597, 49599, 49680, 49681, 49716-49719, 49751, 49752, 49853, 49856, 49905, 49907, 49926-49938 read in full (archives.hungaricana.hu/en/lear/BecsSeg/<id>/), 16 Nov 2026, after harvesting all 88 Türkei I cipher regests of Kt. 46-49 from the \'sifrír*\' search.',
 'Kt. 46-49 (1582-1583): 8 regests say no decipherment, on 7 despatch dates.',
 'Breuner and Pezzen despatches to Rudolf II in cipher (\'sifrír, feloldás nélkül\', some duplicates and triplicates); each has a same-date decipherment (\'német feloldás\', \'sifrír és külön feloldás\') in the same Konvolut.',
 'read', 'Every despatch of Kt. 46-49 marked as undeciphered has its contemporary decipherment filed with it (to Rudolf or in the parallel letter to Archduke Ernst), so nothing in the cluster is unread.',
 'Breuner\'s 1583 key is said to be DECODE R1590 (an 18th-century code per targets/sinzendorff1578, doubtful); R1384 is his 1575 key. Not needed: the decipherments are in the Kartons.',
 'Catalogue 2237 (Breuner 12 May 1583, Kt. 48 Konv. 3 fol. 137-144, 147-151) is one of these letters (regest 49853); its same-day decipherment 49856 shares fol. 147-151.', SEARCH)

P['1223'] = {
 'verdict': 'partly_read', 'confidence': 'medium',
 'note': stats['1223'] + '. The residue is weaker than it looks: Eizing to Rudolf 23 Feb 1587 (51049, cipher, no decipherment, with covering letters 51048, 51052) has its text deciphered in Eizing to Ernst of 18 and 23 Feb (51046, \'német feloldás\'), and Eizing and Pezzen 31 Jul 1587 (51268) has a German copy 51266 of the same day. Closed as read in part; any single letter split out later must first be matched against the Archduke\'s deciphered parallel letters.',
 'access': 'archive', 'access_note': 'HHStA Wien, not digitised; Hungaricana regests answer curl (16 Nov 2026).',
 'residual_dates': '1586.02.18 (51043), 1586.04.14 (50801), 1586.10.01 (50900 duplicate), 1587.02.03 (51051 duplicate), 1587.02.23 (51049, deciphered via 51046)'}
P['1223']['vetting'] = block(1223,
 'Hungaricana regests harvested by script 16 Nov 2026: all 233 Türkei I cipher regests of Kt. 51-63, full regests of every same-date item for the 16 clean dates, and neighbours 51044-51053 and 51265-51270 read in full.',
 'Kt. 51-63 (1584-1587): 54 regests say no decipherment, on 41 despatch dates; many are duplicates sent per Venice.',
 'Eizing and Pezzen despatches in cipher (\'sifrír, feloldás nélkül\'), originals and duplicates; the same Konvoluts carry \'német feloldás\' decipherments, mostly in Eizing\'s parallel letters to Archduke Ernst, and German copies.',
 'partly_read', 'Most dates of the cluster have a deciphered or clear copy of the same despatch in the same Kartons, and the spot-checked residue (51049) is deciphered in the parallel letter to Ernst; a cluster cannot be promoted, so the lead is closed as read in part.',
 'No Eizing or Pezzen key is held on DECODE or in the repo; the contemporary decipherments in the Kartons would give the key.',
 'No catalogue entry for Eizing or Pezzen; leads 1222 and 1224 are the neighbouring Pezzen ranges.', SEARCH)

P['1224'] = {
 'verdict': 'partly_read', 'confidence': 'medium',
 'note': stats['1224'] + '. Of the residue, Pezzen 12 Nov 1588 (51863) sits beside 51864, the deciphered postscripts of 11, 12 and 14 Nov to the relation of 10 Nov, which the date search missed because the regest is dated as a range; the Ernst letters of 1589-91 (52148, 52189, 52466, 52526, 52529, 52562, 52653, 52725) are themselves the Archduke\'s copies and may have Rudolf twins deciphered. Closed as read in part.',
 'access': 'archive', 'access_note': 'HHStA Wien, not digitised; Hungaricana regests answer curl (16 Nov 2026).',
 'residual_dates': '1588.05.12 (51681, endorsed \'Aug. Busbecke\'), 1588.09.16 (51773 duplicate), 1588.11.12 (51863, see 51864), 1589.03.24 (52028, orig., presented 25 Apr 1589), 1589.08.04, 1589.09.28, 1590.07.20, 1590.09.04, 1590.09.15, 1590.11.23, 1591.03.14, 1591.05.29, 1591.07.10, 1591.10.18'}
P['1224']['vetting'] = block(1224,
 'Hungaricana regests harvested by script 16 Nov 2026: all 207 Türkei I cipher regests of Kt. 65-76, full regests of every same-date item for the 29 clean dates, and neighbours 51860-51866 and 52024-52032 read in full.',
 'Kt. 65-76 (1587-1591): 59 regests say no decipherment, on 53 despatch dates.',
 'Pezzen\'s despatches to Rudolf II and Archduke Ernst in cipher (\'sifrír, feloldás nélkül\', several \'csak sifrír\'), with presentation dockets; the same Konvoluts carry \'német feloldás\' decipherments and clear copies.',
 'partly_read', 'Two thirds of the dates have a deciphered or clear copy of the despatch in the same Kartons, and spot checks of the residue find decipherments under range-dated regests; a cluster cannot be promoted, so the lead is closed as read in part.',
 'No Pezzen key is held on DECODE or in the repo; the contemporary decipherments in the Kartons would give it.',
 'No catalogue entry for Pezzen 1588-91; 51681 (12-21 May 1588) is endorsed \'Aug. Busbecke\' and may belong to Busbecq\'s correspondence rather than Pezzen\'s.', SEARCH)

P['1225'] = {
 'verdict': 'partly_read', 'confidence': 'medium',
 'note': stats['1225'] + '. Kreckwitz wrote in cipher to Rudolf and in parallel to Archduke Matthias, and the Matthias letters are deciphered (e.g. 53268 of 26 Apr 1593, cipher, beside 53269 \'német feloldás\', which names his letter of the 23rd sent per Venice, i.e. 53267). Starzer 1610 (55874, 55875) has \'feloldása nincs\' but Starzer\'s run continues in catalogue 1226. Closed as read in part.',
 'access': 'archive', 'access_note': 'HHStA Wien, not digitised; Hungaricana regests answer curl (16 Nov 2026).',
 'residual_dates': '1593.03.13 (53228), 1593.04.23 (53267), 1593.05.12 (53276), 1593.05.17 (53277), 1593.05.19 (53278), 1595.11.14 (53401 duplicate)'}
P['1225']['vetting'] = block(1225,
 'Hungaricana regests harvested by script 16 Nov 2026: all 86 Türkei I cipher regests of Kt. 77-92, full regests of every same-date item for the 16 clean dates, and neighbours 53058-53063 and 53263-53271 read in full.',
 'Kt. 77-92 (1592-1610): 26 regests say no decipherment, on 22 despatch dates, almost all Kreckwitz 1592-93.',
 'Kreckwitz despatches \'csak sifrír, feloldás nélkül\' (cipher only), originals and duplicates; the same Konvoluts carry his deciphered parallel letters to Archduke Matthias (\'német feloldás és sifrír\').',
 'partly_read', 'Most dates have a deciphered copy or a deciphered parallel letter in the same Kartons; a cluster cannot be promoted, so the lead is closed as read in part.',
 'No Kreckwitz key is held on DECODE or in the repo; Ungnad R392 is for 1576-77. The deciphered Matthias letters would give the key.',
 'Catalogue 1226 (Starzer 1611-1619) continues the Starzer run; the two 1610 Starzer pieces of this lead belong with it.', SEARCH)

json.dump(P, open('e_turkei.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(subprocess.run([sys.executable, '-I', '-X', 'utf8', 'put.py', 'e_turkei.json'], capture_output=True, text=True).stdout)
