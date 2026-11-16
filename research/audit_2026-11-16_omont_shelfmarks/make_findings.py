"""Write findings.json for the Omont shelfmark audit (16 Nov 2026). Evidence: BnF Archives et manuscrits notices read by curl
(am.py; cached outside the repo), Omont OCR from archive.org. python -I -X utf8 make_findings.py"""
import json, os

AM = 'https://archivesetmanuscrits.bnf.fr/ark:/12148/'
F = {}


def add(i, status, correct, note, evidence):
    F[str(i)] = {'status': status, 'correct_shelfmark': correct, 'note': note, 'evidence': evidence}


# ---- catalogue entries --------------------------------------------------------------------------------------------
add(2726, 'ok', 'BnF fr. 3654 (Anc. 9021(2)), nos. 6, 8, 11-19',
    'Volume and items right (rescoped by batch B). The FOLIOS in the entry are shifted by one item: the notice page prints each '
    'item\'s folio before the item, not after it. Correct folios (Omont\'s printed "(Fol. N.)" and the component display agree): '
    'no. 6 f. 10, 8 f. 14, 11 f. 20, 12 f. 22, 13 f. 26, 14 f. 28, 15 f. 32, 16 f. 34, 17 f. 37, 18 f. 40, 19 f. 43 '
    '(the entry has ff. 12, 16, 22, 26, 28, 32, 34, 37-47). Nos. 21-23 "avec chiffre et dechiffrement" (siblings with decipherment). No Gallica link.',
    AM + 'cc501068 (Francais 3654): nos. 6, 8, 11-19 "Lettre, avec chiffre" to Breves, Nov 1611 - Nov 1613; component '
    'FRBNFEAD000050106_d0e119 "foliotation: Fol. 10 / 6 Lettre, avec chiffre ..."; Omont OCR p1cataloguegnr02bibluoft: "6. Lettre, avec chiffre ... ix novembre 1611. (Fol. 10.)"')
add(2732, 'shelfmark_wrong', 'Omont items 34, 49, 70, 72 belong to the volume closed by "(Anc. 8554.)", the one after fr. 3028; fr. 3027 (Anc. 8552) has no listed cipher item',
    'The folio_note (Omont nos. 34, 49, 70, 72; ff. 67, 100-105, 182, 186-202) is taken from the Omont entry that follows fr. 3028 '
    '(Henri d\'Albret, Bonnivet to Robertet, La Tremoille ...; "34. Lettre en chiffre (Fol. 67.)"), which closes "(Anc. 8554.)". '
    'fr. 3027 = Anc. 8552 and fr. 3028 = Anc. 8553 (both Bonnivet letters to Montmorency/La Rochepot, no cipher item), so by sequence '
    'the volume holding those items is fr. 3029, a volume withheld at Lasry\'s request: its notice was NOT opened here and nothing about it is '
    'confirmed. The cipher leaf the 14 Nov vetting saw at Gallica fr. 3027 (btv1b9060066q) view 69 is real but is not Omont\'s no. 34: '
    'the fr. 3027 notice has item 15 at f. 67 (Bonnivet to La Rochepot, La Coste Saint-Andre, 18 July) and lists no cipher. The entry needs '
    'rescoping to the fr. 3027 leaf actually seen (f. 67 area, unlisted cipher) and the fr. 3029 items removed; ask before anything touches fr. 3029.',
    AM + 'cc49486k (Francais 3027, Anc. 8552, Gallica btv1b9060066q): 30 Bonnivet items, no "chiffre" (loupe search empty); '
    + AM + 'cc49487t (Francais 3028, Anc. 8553): 32 Bonnivet items, no cipher; Omont OCR p1cataloguegnr01bibluoft lines 108222-108701: '
    'entry "5027" closes Anc. 8552, "3028" closes Anc. 8553, the next entry (cipher items 34, 49, 70, 72) closes Anc. 8554.')
add(2746, 'ok', 'BnF fr. 20140 (Gaignieres 679), f. 16 ff.',
    'Notice: "Correspondance, originale et en partie chiffree, de Charles de Danzay, ambassadeur en Danemark, 1557-1567 (fol. 16)". '
    'No decipherment recorded. Gallica btv1b52521512h (and btv1b10782904z).',
    AM + 'cc51725m (Francais 20140)')
add(2838, 'ok', 'BnF fr. 15567 (Harlay 329 (7)), f. 24',
    'Notice: "Depeches chiffrees orig. de Matignon (f. 24), - et de Bellievre-Hautefort (f. 158 et suiv.)". No decipherment recorded. '
    'The notice names the writer of f. 24 as Matignon; the entry says "unknown writer". Gallica btv1b90639282.',
    AM + 'cc459423 (group Francais 15540-15584), component FRBNFEAD000045942_d0e7249 (Francais 15567, 1584 janvier-mars)')
add(2839, 'ok', 'BnF fr. 15567, ff. 158 ff.',
    'Notice: "Depeches chiffrees orig. ... de Bellievre-Hautefort (f. 158 et suiv.)". No decipherment recorded. Gallica btv1b90639282.',
    AM + 'cc459423, component FRBNFEAD000045942_d0e7249')
add(2840, 'ok', 'BnF fr. 15568 (Harlay 329 (8)), f. 151',
    'Notice: "Depeches chiffrees de Matignon (f. 151)": the notice names Matignon as writer (entry: "unknown writer, Matignon side"). '
    'No decipherment recorded. Gallica btv1b9063927n. Consultation needs authorisation (conservation).',
    AM + 'cc459423, component FRBNFEAD000045942_d0e7448 (Francais 15568, 1584 avril-decembre)')
add(2841, 'ok', 'BnF fr. 15568, f. 207',
    'Notice: "Depeches chiffrees ... de Bellievre-Hautefort, orig. (f. 207)". No decipherment recorded. Gallica btv1b9063927n.',
    AM + 'cc459423, component FRBNFEAD000045942_d0e7448')
add(2842, 'ok', 'BnF fr. 15571 (Harlay 329 (11)), f. 37',
    'Notice describes only "Depeche chiffree orig. de M. de Chasteauneuf, envoye en Angleterre (f. 34)"; the f. 37 block is not in the '
    'notice but was seen on the image (wave 6). Volume confirmed. Gallica btv1b90618802.',
    AM + 'cc459423, component FRBNFEAD000045942_d0e8447 (Francais 15571, 1585 octobre-decembre)')

# ---- leads, Ancien fonds (sweep_2026-11-14_omont_bnf) --------------------------------------------------------------
add(2724, 'shelfmark_wrong', 'BnF fr. 3251 (Anc. 8760) and fr. 3252 (Anc. 8761)',
    'fr. 3231/3232 are Guise letters to Nemours. The Birago letters are fr. 3251: "avec chiffre" nos. 6, 18, 42, 45, 63, 71, 73, 77, 82, 85, 86, 87, 90 '
    '(Sept 1570 - Oct 1572; no. 20, 30 Nov 1570, "avec chiffre et dechiffrement"), and fr. 3252: nos. 30 (26 Apr 1571), 67 (8 Jan 1572), 77 (13 Mar 1572, in French) '
    '(no. 24, 5 Apr 1571, with decipherment). Gallica: fr. 3251 btv1b9060248g, fr. 3252 btv1b9060232m. Catalogue 318 / Lasry list (fr. 3252) is the neighbour.',
    AM + 'cc49712p (Francais 3251, Anc. 8760); ' + AM + 'cc49713x (Francais 3252, Anc. 8761); ' + AM + 'cc496925 (fr. 3231, Guise cardinals to Nemours, no cipher)')
add(2725, 'shelfmark_wrong', 'BnF fr. 3641 (Anc. 9130)',
    'fr. 3057 is Francis I to La Fayette. The Philip II / Mendoza / Ibarra volume is fr. 3641: "avec chiffre" without decipherment nos. 3, 5, 6 '
    '(Philip II to Mendoza, Aug-Sept 1589), 27, 28 (Mendoza, 2 May 1590), 43, 48, 50 (Ibarra, Nov 1592), 58 (Feria, 7 Apr 1593); about 50 '
    'further items "avec chiffre et dechiffrement" (nos. 1-2 Farnese, 8-25 Philip II/Mendoza 1589, 30-32, 34-41, 45-54, 59-62), so the keys are rebuildable. '
    'Gallica btv1b52508089f.',
    AM + 'cc500920 (Francais 3641, Anc. 9130); ' + AM + 'cc49517j (fr. 3057: Francis I letters, no cipher); Omont OCR: the entry closes "(Anc. 9130.)"')
add(2727, 'shelfmark_wrong', 'BnF fr. 3375 (Anc. 8878) nos. 3, 61, 63; fr. 4697 and fr. 4691 right',
    'fr. 3374 (Cabriani 1585-86, 42 items) has no cipher item; the cited nos. 3 (Guazzo, 1586), 61 (Nevers to Scipione Gonzaga, 22 June 1586) and '
    '63 (Nevers to the Patriarch, 20 July 1586) are fr. 3375 (also no. 26, Camillo Volta, 24 Mar 1586, with decipherment). fr. 4697: nos. 16-17, 23, 26 '
    '(Nevers to Scipione Gonzaga, copies, "Chiffre"), 30 (to Volta, minute), 70 (7 Feb 1587); nos. 22, 24 (Volta) "Chiffre et dechiffrement". '
    'fr. 4691: no. 104 (to Volta, 13 Sept 1585, minute, Chiffre) and nos. 20-21 (Guazzo notes, 1572, Chiffre). None on Gallica.',
    AM + 'cc498417 (Francais 3375, Anc. 8878); ' + AM + 'cc57747b (fr. 4697, Anc. 9519); ' + AM + 'cc57741w (fr. 4691, Anc. 9513); ' + AM + 'cc498400 (fr. 3374, no cipher)')
add(2728, 'ok', 'BnF fr. 3422 (Anc. 8923), nos. 27, 60, 62, 68, 69, 70',
    'All six "Lettre, avec chiffre" to Nevers, 8 Apr - 27 June 1589 (the "one more" is no. 70, Tours, 27 June); no decipherment noted. Not on Gallica.',
    AM + 'cc498940 (Francais 3422)')
add(2729, 'shelfmark_wrong', 'fr. 3624 nos. 47, 51, 67; fr. 3625 no. 55 (Lauriere); fr. 3614 nos. 58, 61; fr. 3634 nos. 4, 45, 60, 80; fr. 3646 nos. 55, 67',
    'Volumes mostly right, item list partly wrong. The "Lairiere" letter (fr. 3624 no. 53 in the lead) is fr. 3625 no. 55, f. 66 (Sr de Lauriere, Chalons, 9 July 1593; '
    'his letter of 13 July 1593, no. 10, has a decipherment). fr. 3614 no. 64 is a plain letter (Chandon); cipher items there are 58 (Nevers to Montholon, copy) and 61. '
    'fr. 3634 no. 20 is only "signee d\'un chiffre" (a cipher signature); 45 (f. 46) and 80 (f. 84, Regnyer, "lettre chiffree") are cipher items the lead omits. '
    'fr. 3646 "no. 53 (f. 108)" is no. 55 (f. 108, "Depeche, en chiffre, du 6 fevrier 1593"). None on Gallica.',
    AM + 'cc500742 (fr. 3624); ' + AM + 'cc500759 (fr. 3625, no. 55); ' + AM + 'cc50064v (fr. 3614); ' + AM + 'cc500848 (fr. 3634); ' + AM + 'cc500976 (fr. 3646)')
add(2730, 'ok', 'BnF fr. 3329 (Anc. 8832), fr. 3409 (Anc. 8912), fr. 4717 (Anc. 9539)',
    'fr. 3329: no. 1 "Table de dechiffrement anonyme", no. 2 "Table de chiffrement de M. de Humieres pour correspondre avec M. d\'Entragues", '
    'nos. 78 (f. 159), 81 (f. 164, not 104), 82 (f. 165, not 105) "avec chiffre", and no. 107 (Maineville, Anet, 30 Sept, avec chiffre) not in the lead. '
    'fr. 3409 no. 49 (21 Nov 1578) right; no. 39 is a "Chiffre" (key). fr. 4717 no. 49 (Laisne, 2 Apr 1577) right; no. 11 "Clef d\'un chiffre". No decipherment noted for the lead items. Not on Gallica.',
    AM + 'cc497913 (fr. 3329); ' + AM + 'cc49879s (fr. 3409); ' + AM + 'cc57767r (fr. 4717)')
add(2731, 'shelfmark_wrong', 'BnF fr. 2988 (Regius 8513)',
    'fr. 2986 (Anc. 8511) has no cipher item. fr. 2988: no. 1 and 3 "Lettre en chiffre de Hieronimo Ranzo", no. 2 "Double de lettres escriptes en chiffre par Nicolas Raince... '
    'Romme, XVme decembre 1526", and 26 "Piece en chiffre" (nos. 7-55). No decipherment noted. Already on DECODE (R2293-2323, mostly non-decrypted; see the 14 Nov vetting note). '
    'Gallica btv1b525240150 / btv1b9059908w.',
    AM + 'cc49442s (Francais 2988); ' + AM + 'cc494409 (fr. 2986, no cipher)')
add(2733, 'shelfmark_wrong', 'BnF fr. 2933 (Anc. 8469), no. 11, f. 54',
    'fr. 2935 is a 3-item copy volume (Anc. 9722). The Salviati letter is fr. 2933 no. 11, "Lettre en chiffres, et en italien, de Johannes, cardinalis de Salviatis... '
    'Die XVI octobris 1525", f. 54 (OCR "34"). No decipherment noted. Gallica btv1b90600674.',
    AM + 'cc493855 (Francais 2933); Omont OCR p1cataloguegnr01bibluoft: heading "2935" (for 2933) closes "(Anc. 8469.)"')
add(2734, 'decipherment_filed', 'BnF fr. 2996 no. 25 (1546) and fr. 3138 (Anc. 8657) no. 24 (1549)',
    'Lead already closed read for the 1546 despatch (fr. 2996, volume right; item is no. 25, not 23). The 12 Nov 1549 despatch is NOT in fr. 3137 '
    '(no cipher item there) but fr. 3138 no. 24, and the notice says "avec chiffre et dechiffrement": a decipherment is filed with it. '
    'Same volume no. 22: Claude de La Guiche, bishop of Mirepoix, Rome, 22 Nov 1551, "avec chiffre", no decipherment noted (a sibling not in the ledgers checked). '
    'Gallica fr. 3138 btv1b90601662; fr. 2996 btv1b9060087w.',
    AM + 'cc49600t (Francais 3138, no. 24); ' + AM + 'cc49450h (fr. 2996, no. 25 "Depeche en chiffre de Morvillier ... 24 janvier 1546"); ' + AM + 'cc49599p (fr. 3137, no cipher)')
add(2735, 'shelfmark_wrong', 'BnF fr. 3045 (Anc. 8570), no. 29',
    'fr. 3043 has no cipher item. "29 Lettre, avec chiffre, de Robert Cenalis, evesque d\'Avranches... au roy... A Venyse, le XIIIe d\'octobre" is fr. 3045; '
    'no decipherment noted in the notice, but DECODE R4231 (fr. 3045 f. 36, decrypted) is very probably this letter (14 Nov vetting). Siblings in fr. 3045: '
    'no. 24 (Galeazzo Visconti, 1528, "lettre chiffree") and no. 31 (Georges de Selve, Venice, 5 July 1536, "lettre chiffree"). Gallica btv1b9060156p.',
    AM + 'cc49504m (Francais 3045); ' + AM + 'cc495024 (fr. 3043, no cipher)')
add(2736, 'shelfmark_wrong', 'BnF fr. 3586 (Anc. 9075) no. 57; fr. 3575 (Anc. 9064) nos. 29, 36',
    'fr. 3086 (Charles V letters of grace) and fr. 3373 (Bellievre 1587) hold none of it (OCR 5/3 swap in the hundreds). 22 Nov 1597 Pezenas letter = fr. 3586 no. 57; '
    '14 June 1598 Pezenas letter = fr. 3575 no. 29; the key "36 Chiffre" = fr. 3575 no. 36. No decipherment noted. Gallica: fr. 3575 btv1b90605406; fr. 3586 none.',
    AM + 'cc50035g (Francais 3586); ' + AM + 'cc50023s (Francais 3575); Omont OCR: entries close "(Anc. 9075.)" and "(Anc. 9064.)"')
add(2737, 'shelfmark_wrong', 'BnF fr. 3659 (Anc. 9153), no. 24',
    'fr. 3638 is Marguerite de Valois. "24 Lettre, avec chiffre, du duque de Monteleon... a don Pedro de Toledo... De Paris, 18 de ottobre 1617. En espagnol. Copie." is fr. 3659 '
    '(a Bethune embassy volume with Louis XIII and Puysieulx letters "avec chiffre et dechiffrement", nos. 8, 36, 41, 73-74). No decipherment noted for no. 24. Not on Gallica.',
    AM + 'cc501101 (Francais 3659); ' + AM + 'cc500887 (fr. 3638)')
add(2738, 'shelfmark_wrong', 'BnF fr. 3693 (Anc. 9192; tome I of fr. 3693-3694, Blainville embassy in England 1625-26), nos. 13, 22, 26',
    'fr. 3689 is Bassompierre in Switzerland. The bishop of Mende pieces are in "Ambassade de Mr de Blainville, ambassadeur extraordinaire en Angleterre, 1625 et 1626": '
    'no. 13 "Advis en chiffre" by the bishop of Mende, no. 22 "Advis en chiffre ... receu le 26 aoust 1625", no. 26 "Lettre en chiffre ... receue le 29 aoust 1625". '
    'The year is 1625, not 1623 (OCR), and the context is England (Mende was Henrietta Maria\'s almoner), not France. Likely register copies. No decipherment noted. Not on Gallica.',
    AM + 'cc50138c (group Francais 3693-3694, Anc. 9192; loupe hits d0e246, d0e357, d0e409); ' + AM + 'cc501335 (fr. 3689, no cipher)')
add(2739, 'shelfmark_wrong', 'fr. 3837 nos. 15, 18 (right); fr. 3758 (Anc. 9256) nos. 100, 104; fr. 3854 (Anc. 9353) nos. 41, 42',
    'fr. 3837 (Bouthillier, 1633) right, plus no. 3 "Table de chiffrement de Bouteiller pour correspondre avec M. de Guron" (key). fr. 3730 and fr. 3834 are copy volumes '
    'with no cipher item. The Chatillon pieces are fr. 3758 ("lettres ... de l\'annee 1635"): no. 100 Louis XIII to Chatillon and Breze, last of June 1635, and no. 104 Chatillon to Servien, '
    'Nijmegen, 3 Aug 1635 (year 1635, not 1633). The Conti memoirs are fr. 3854 nos. 41 (26 Mar 1649) and 42 (27 Mar 1649); no. 43 (a Conti memoir) has a decipherment. '
    'Gallica: fr. 3758 btv1b9058223v, fr. 3854 btv1b52520094g; fr. 3837 none.',
    AM + 'cc50278c (fr. 3837); ' + AM + 'cc502017 (Francais 3758, Anc. 9256; loupe d0e1368, d0e1423); ' + AM + 'cc502952 (Francais 3854); ' + AM + 'cc50175g (fr. 3730), ' + AM + 'cc50275n (fr. 3834): no cipher')
add(2740, 'ok', 'BnF fr. 3796 (Anc. 9291), no. 38',
    '"38 Lettre, avec chiffre, de Louis XIII a mon cousin le duc de Nevers, Paris, 28 Dec 1618." No decipherment noted. Not on Gallica.',
    AM + 'cc502323 (Francais 3796)')
add(2741, 'ok', 'BnF fr. 4137 (Anc. 9333; in group fr. 4133-4138), no. 112, f. 128',
    '"Memoyre que Mr de Sabran a envoye en chiffre a S. A. de Savoye, a Mr de Bordeaux et a Mr d\'Hemery, le 3e septembre" [1637], f. 128. No decipherment noted. '
    'The group notice has no Gallica link; the sweep found btv1b9060192j for fr. 4137.',
    AM + 'cc505343 (group Francais 4133-4138), component FRBNFEAD000050534_d0e6616')
add(2742, 'shelfmark_wrong', 'BnF fr. 4734 (Anc. 9513(2); tome I of fr. 4734-4736), no. 51',
    'fr. 4733 is "Memoires concernants les affaires de la maison de Mantoue" with no cipher item. "51 Lettre du Sr de Lanssac au roi Charles IX. De Varsawia, le 26 avril 1573. Avec chiffre." '
    'is in fr. 4734-4736 (tome I). Courcelles, Edinburgh, 4 Oct 1586 (no. 141) is in the same group "avec chiffre et dechiffrement". Many Polish-embassy siblings there '
    'have decipherments (Monluc 53-55, 85-92; Lanssac 60-61, 63, 65, 70), so the key is rebuildable. Not on Gallica.',
    AM + 'cc57784f (group Francais 4734-4736; loupe d0e2544, d0e4489); ' + AM + 'cc577836 (fr. 4733, no cipher)')
add(2743, 'shelfmark_wrong', 'BnF fr. 3457 (Anc. 8956), no. 2',
    'fr. 3437 is a copy volume (Anc. 9765) with no cipher item. "2 Lettre du roi Henry [IV] a mon cousin le cardinal d\'Ossat... Fontainebleau, le premier jour de mai 1601. Avec chiffre." '
    'is fr. 3457. No decipherment noted for it; sibling no. 6 (Henri IV to the bishop of Rennes, 21 Feb 1598) is "avec chiffre et dechiffrement". Not on Gallica.',
    AM + 'cc49932f (Francais 3457); ' + AM + 'cc49910j (fr. 3437)')
add(2744, 'shelfmark_wrong', 'BnF fr. 3828 (Anc. 9322) nos. 8, 10, 17, 18, 19, 21, 26; fr. 3825 (Anc. 9319) no. 28; fr. 3835 (Anc. 9329) no. 15',
    'Confirms batch B: fr. 3826, 3823 and 3855 have no cipher item. Richelieu to Rance and to the queen, 14 Apr - 25 May 1629 = fr. 3828; "Nouvelles, avec chiffre, adressees a M. de Rance, Suze, 21 mars" = fr. 3825 no. 28; '
    'Richelieu to Rance (undated) = fr. 3835 no. 15. No decipherment in the notices; Avenel t. III prints them with the cipher explained (batch B; lead verdict read). Not on Gallica.',
    AM + 'cc502685 (fr. 3828); ' + AM + 'cc50265f (fr. 3825); ' + AM + 'cc50276w (fr. 3835); ' + AM + 'cc50266p, cc50263z, cc502969 (fr. 3826, 3823, 3855: no cipher)')

# ---- leads, NAF / Petits fonds (sweep_2026-11-15_omont_naf) --------------------------------------------------------
add(2745, 'ok', 'BnF fr. 23202 (Gaignieres 2799)',
    'Notice: "Originaux chiffres ou autographes; on y a ajoute (fol. 1-2) une copie du chiffre." No decipherment recorded in the notice (the 15 Nov vetting saw partial interlinear '
    'decipherment on the leaves; DECODE R7894-R7897 solved). Gallica btv1b9063488m.',
    AM + 'cc52504r (Francais 23202)')
add(2747, 'ok', 'BnF fr. 23227-23228 (in group fr. 23210-23229, Noailles papers)',
    'Component: "XVIII-XIX Lettres du pere Roslet, minime, au cardinal de Noailles (1700-1713). 223 et 257 feuillets ... en tete du tome I, fol. 1-6, des clefs des chiffres employes". '
    'Does not say which letters are ciphered; no decipherment recorded. No Gallica link.',
    AM + 'cc525100 (group Francais 23210-23229), component FRBNFEAD000052510_d0e2980')
add(2748, 'ok', 'BnF NAF 3145-3146 bis',
    'Notice: "A la fin du tome II sont ajoutes differents chiffres." Key sheets only; the notice does not say any letter is ciphered. No Gallica link.',
    AM + 'cc39749w (NAF 3145-3146 bis)')
add(2749, 'ok', 'BnF NAF 22330, f. 107',
    'Notice item: "Lettres, en chiffres, adressees a Conraden Breiffenstein, oder Laurentzen Riedet, a Delft, etc." No decipherment recorded. No Gallica link. '
    'Found through the site\'s simple search (resultatRechercheSimple.html, POST TEXTE_LIBRE_INPUT).',
    AM + 'cc4087c (NAF 22330), component FRBNFEAD000004087_d0e242')
add(2750, 'ok', 'BnF NAF 11238',
    'Notice: "Epitre d\'Abailard a Heloise, transcrite en caracteres cryptographiques. XVIIIe siecle." No decipherment recorded. No Gallica link.',
    AM + 'cc59029 (NAF 11238), found by simple search "cryptographiques"')
add(2751, 'ok', 'BnF NAF 4543 (tome I of NAF 4543-4544, Le Dran, Memoires musicaux), f. 180',
    'Notice: "Fol. 180. Papiers d\'Audibert, maitre de musique de l\'Academie du roi, a Lyon, relatifs a l\'emploi de la notation musicale pour chiffrer les depeches (1746)." No Gallica link.',
    AM + 'cc40429t (NAF 4543-4544), component d0e86')
add(2752, 'decipherment_filed', 'BnF fr. 20506 (Gaignieres 394; in group fr. 20500-20576)',
    'Volume right. The notice now records that it "Contient notamment des lettres chiffrees de Marie Stuart a l\'ambassadeur de France en Angleterre, Michel de Castelnau, entre 1578 et 1584" '
    'with the bibliography Lasry, Biermann and Tomokiyo, "Deciphering Mary Stuart\'s lost letters from 1578-1584", Cryptologia 47/2: a published decipherment covers a large part of the '
    'volume\'s cipher (not a decipherment filed in the volume). With Dodieu (catalogue 308), Ranzo ff. 136-138 (R4450) and Cenalis f. 96 (R4815) also read, the lead should be closed or narrowed '
    'to named letters outside these. Gallica btv1b525047581.',
    AM + 'cc518506 (group Francais 20500-20576), component FRBNFEAD000051850_d0e635 (Francais 20506)')

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'findings.json')
json.dump(F, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(F), Counter(v['status'] for v in F.values()))
