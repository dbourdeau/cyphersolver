"""Build candidates.json (and key_leads.json) for the Czech lands and Slovakia sweep (6 Nov 2026).

Rows come from item-level archive descriptions found through the ARON portals (MZA Brno, SOA Plzeň, SOA Zámrsk)
and the Národní archiv VadeMeCum; hits are in aron_hits.jsonl / aron_details.jsonl / vmc_hits.jsonl. None of the
items has digitised images in the portals (ARON reports 0 digital objects for every one), so every row is
seen: "catalogue". Key-only items (a key with no ciphertext stated) go to key_leads.json, not candidates.json,
because merge.py accepts only cls A/B/C.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'Czech lands and Slovakia sweep (ARON portals, NA VadeMeCum), Nov 2026'
SCORE = ('Scored from the item-level archive description during the Czech/Slovak sweep, 6 Nov 2026 '
         '(research/sweep_2026-11_czech_slovak/); not viewed')
ACC_MZA = ('description only on MZA ARON (www.mza.cz/aron, item record has no digital objects); scans must be ordered '
           'from the Moravský zemský archiv, Brno, or the box consulted in the reading room')
ACC_PLZ = ('description only on SOA Plzeň ARON (aron.soaplzen.cz, no digital objects); scans to order from SOA Plzeň '
           '(family archives at the Klášter u Nepomuka branch)')
ACC_NA = ('description only in the Národní archiv VadeMeCum (no scans of the documents); order scans from the '
          'Národní archiv, Praha (Chodovec)')
ACC_ZAM = 'description only on SOA Zámrsk ARON (no digital objects); SOkA Rychnov nad Kněžnou holds the item'
PRIOR = ('open as far as checked (6 Nov 2026): known.py (catalogue, leads, targets, DECODE and HCPortal dumps) finds nothing on '
         'the shelfmark or the correspondents; web searches on the correspondents with cipher/šifra and on cryptiana '
         '(Collalto, Scaglia, Fossombroni, Nostitz, Verdugo/Anhalt) found no edition, study or decipherment; Lasry not searched '
         'beyond that')


def aron(base, uid, label='archive record'):
    return {'href': f'{base}/apu/{uid}', 'label': label}


MZA = 'https://www.mza.cz/aron'
PLZ = 'https://aron.soaplzen.cz'
ZAM = 'https://aron.vychodoceskearchivy.cz'

COLL = 'MZA Brno, G 169 Rodinný archiv Collaltů Brtnice, I. část'
DIET = 'MZA Brno, G 140 Rodinný archiv Ditrichštejnů Mikulov, Historický archiv, Cizí státy'

ROWS = [
    # ---- Collalto (Rambaldo XIII Collalto, imperial field marshal, president of the Hofkriegsrat, d. 1630) ----
    dict(
        year=1626, date='1624-1629',
        title="Sebastian Lustrier's letters and reports from Constantinople to Rambaldo Collalto, 26 pieces, mostly in cipher",
        correspondents='Sebastian Lustrier (imperial resident at the Porte) -> Rambaldo Collalto (president of the Hofkriegsrat)',
        place='Constantinople', language='Italian or German (not stated)', region='Central Europe', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 1774',
        folio_note='26 pieces, "většinou šifrováno" (mostly enciphered) per the inventory',
        cls='B',
        status='MZA inventory: "Dopisy a zprávy Lustriera z Cařihradu; 26 kusů, většinou šifrováno". No decipherment mentioned. '
               'Same sender as catalogue #1227 (Lustrier/Radibrati -> Ferdinand II, HHStA Türkei I Kt. 108-111, ciphered '
               '1621-31, no decipherment): the Hofkriegsrat copy-stream of the same intelligence, probably the same cipher. '
               'inv. 1776 of this fonds holds a Collalto-Harrach key and more Lustrier letters (separate row).',
        why='Habsburg intelligence from the Porte in the years of the Bethlen Gábor wars and the 1627 Szőny peace, addressed to '
            'the head of the war council; a second archive of the Lustrier cipher doubles the ciphertext for #1227.',
        importance=4, solvability=2, difficulty=3,
        verify='Order scans of inv. 1774 and inv. 1776 (key); compare the cipher with catalogue #1227 and with the Kurtz von '
               'Senftenau ciphers printed in the Graz GAMS edition (1623-24).',
        links=[aron(MZA, 'a39e28bc-2ff1-4a50-bdba-65f7f49287f3')], access_note=ACC_MZA,
    ),
    dict(
        year=1630, date='1630',
        title="Abbot Alessandro Scaglia's letters to Rambaldo Collalto from Madrid, Turin and elsewhere, 17 pieces, mostly in cipher",
        correspondents='Alessandro Scaglia, abbot of Staffarda (Savoyard diplomat) -> Rambaldo Collalto',
        place='Madrid / Turin / other', language='Italian (probable)', region='Central Europe', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 1775',
        folio_note='17 pieces, "většinou šifrováno"',
        cls='C',
        status='MZA inventory: "Dopisy opata Scaglia z Madridu, Turína a jiných měst; 17 kusů, většinou šifrováno". No key or '
               'decipherment mentioned. Scaglia is not in the repo.',
        why='Savoy\'s chief diplomat writing to the imperial commander in Italy during the War of the Mantuan Succession (1630, '
            'siege of Mantua, Casale); a Savoy-Empire channel not otherwise known in cipher.',
        importance=4, solvability=2, difficulty=3,
        verify='Order scans; check the key in inv. 1776 and the Savoyard ciphers of Scaglia in the Archivio di Stato di Torino '
               '(Lettere ministri) for the system.',
        links=[aron(MZA, '83ee3a6e-f71b-4105-81f4-5a15001423c1')], access_note=ACC_MZA,
    ),
    dict(
        year=1629, date='1629',
        title='Rossi to Rambaldo Collalto, 66 letters, partly in cipher (Mantuan war)',
        correspondents='Rossi (agent; first name not given) -> Rambaldo Collalto',
        place='unknown', language='Italian (probable)', region='Central Europe', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 1862',
        folio_note='66 pieces, "částečně šifrováno" (partly enciphered)',
        cls='C',
        status='MZA inventory: "Dopisy Rossiho Rombaldovi Collalto; částečně šifrováno, 66 kusů". Correspondent not identified.',
        why='A long run (66 letters) of one correspondent in the year Collalto took command in Italy: enough ciphertext for a '
            'ciphertext-only attack if the system is a nomenclator with a small alphabet.',
        importance=3, solvability=2, difficulty=3,
        verify='Order scans; identify Rossi; compare with inv. 1776 key.',
        links=[aron(MZA, '9774e7df-de71-426c-803b-22ff64ee04f1')], access_note=ACC_MZA,
    ),
    dict(
        year=1628, date='1625-1630',
        title='Prince Hans Ulrich von Eggenberg to Rambaldo Collalto, 19 letters, partly in cipher',
        correspondents='Hans Ulrich von Eggenberg (Ferdinand II\'s chief minister) -> Rambaldo Collalto',
        place='Vienna (probable)', language='Italian and German', region='Central Europe', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 1719',
        folio_note='19 pieces, "část šifrováno" (part enciphered)',
        cls='C',
        status='MZA inventory: "Dopisy Knížete Oldřicha z Eggenberka Rombaldovi Collalto; 19 kusů, italština, němčina, část '
               'šifrováno". The catalogue holds Eggenberg only as an author of a 1622 Gutachten (HHStA Spanien Varia, #1721).',
        why='The Emperor\'s first minister to the war-council president in 1625-30 (Wallenstein\'s first generalate, Mantua): '
            'ciphered passages at the very top of the imperial government.',
        importance=4, solvability=2, difficulty=3,
        verify='Order scans; compare with inv. 1776 key and inv. 1698 (Ferdinand II).',
        links=[aron(MZA, '95ba6f88-08c5-4bf9-ab12-cd0eb5d41c7e')], access_note=ACC_MZA,
    ),
    dict(
        year=1629, date='1626-1629',
        title='Emperor Ferdinand II to Rambaldo Collalto, letters of the Italian campaign; one piece in cipher',
        correspondents='Ferdinand II -> Rambaldo Collalto',
        place='Vienna', language='German or Italian (not stated)', region='Central Europe', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 1698',
        folio_note='several letters, "1 kus šifrováno" (one piece enciphered)',
        cls='C',
        status='MZA inventory: "Listy císaře Ferdinanda II. Rombaldovi Collalto: zejména z doby italského tažení 1629; 1 kus '
               'šifrováno".',
        why='An imperial order to the commander in Italy kept in cipher, 1629.',
        importance=4, solvability=1, difficulty=3,
        verify='Order a scan of the ciphered piece; take with inv. 143 (12 Feb 1630) and inv. 1776 (key).',
        links=[aron(MZA, '8f9fe9ac-5281-4e79-b484-961a919657bf')], access_note=ACC_MZA,
    ),
    dict(
        year=1630, date='12 Feb 1630',
        title='Ciphered imperial decision to Rambaldo Collalto on the Mantuan "felony" (Duke of Nevers)',
        correspondents='Ferdinand (the inventory says Ferdinand III; in 1630 more likely Ferdinand II) -> Rambaldo Collalto',
        place='Vienna (probable)', language='unknown', region='Central Europe', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 143',
        folio_note='one document dated 12 Feb 1630',
        cls='C',
        status='MZA inventory: "Šifrované rozhodnutí Ferdinanda III. Rombaldovi Collalto ohledně mantovské felonie", 12.2.1630. '
               'No decipherment mentioned.',
        why='The Emperor\'s ruling on Charles de Nevers\'s forfeiture of Mantua sent in cipher to the besieging commander, five '
            'months before the sack of Mantua.',
        importance=4, solvability=1, difficulty=3,
        verify='Order a scan; check whether the decision is printed (Mantuan Succession documents) to supply a crib.',
        links=[aron(MZA, '889e6d42-8c17-468e-88cc-e3295eeaa170')], access_note=ACC_MZA,
    ),
    dict(
        year=1630, date='1630',
        title='Ciphered letter to the Mantuan resident in Paris, intercepted by Rambaldo Collalto at the siege of Mantua (original)',
        correspondents='Mantuan court (Duke of Nevers\'s ministers) -> Mantuan resident in Paris (intercepted)',
        place='Mantua', language='Italian or French (probable)', region='Italy', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 142',
        folio_note='one original letter',
        cls='C',
        status='MZA inventory: "Dopis šifrovaný revidentovi [rezidentovi] mantovskému v Paříži, poslaný a zachycený Rombaldem '
               'Collalto při obležení Mantovy; originál". No decipherment mentioned.',
        why='An intercepted Gonzaga-Nevers despatch to Paris from inside besieged Mantua: Mantua\'s appeal to Richelieu in the war\'s '
            'decisive year.',
        importance=4, solvability=2, difficulty=3,
        verify='Order a scan; compare with Gonzaga-Nevers ciphers of 1628-30 in the Archivio Gonzaga (Mantua) and in AE '
               'Correspondance politique Mantoue.',
        links=[aron(MZA, '5b37359b-9020-413c-b9df-72d4e69ecee1')], access_note=ACC_MZA,
    ),
    dict(
        year=1627, date='1619-1630',
        title='Tilly, Gallas, Questenberg, Aldringen and Trauttmansdorff to Rambaldo Collalto, 10 letters, partly in cipher',
        correspondents='Johann Tserclaes Tilly; Matthias Gallas; Gerhard von Questenberg; Johann von Aldringen; Maximilian von '
                       'Trauttmansdorff -> Rambaldo Collalto',
        place='various', language='German / Italian (not stated)', region='Central Europe', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 1740 (series "Dopisy Rombaldovi Collalto")',
        folio_note='10 pieces, "částečně šifrováno"',
        cls='C',
        status='MZA inventory: "Od hraběte Jana Tillyho, Mathiase Gallase Questenberga, Aldringena, Trautmannsdorfa; 10 kusů, '
               'částečně šifrováno".',
        why='Commanders and ministers of the first half of the Thirty Years\' War writing to the war council president; Gallas and '
            'Aldringen ciphers of the 1630s are studied (Charles University theses) but not these early ones.',
        importance=3, solvability=2, difficulty=3,
        verify='Order scans; compare with the Gallas war-chancery cipher list (Charles University BA thesis 2017, '
               'hdl 20.500.11956/91542).',
        links=[aron(MZA, 'a337ad28-11c8-44c8-95d2-4ee85f15e433')], access_note=ACC_MZA,
    ),
    dict(
        year=1625, date='1613-1630',
        title='Letters to Rambaldo Collalto (Molart, Lustrier, Spinola, nuncio Castro and others) with the Collalto-Harrach cipher key',
        correspondents='Molart, Sebastian Lustrier, Ambrogio Spinola, the nuncio Castro and others -> Rambaldo Collalto; key for '
                       'Collalto <-> Harrach',
        place='various', language='Italian / German', region='Central Europe', period='1611-1650',
        shelfmark=f'{COLL}, inv. č. 1776',
        folio_note='24 pieces (Montenero), with a cipher key ("připojen šifrovací klíč pro styk mezi Collaltem a Harrachem")',
        cls='B',
        status='MZA inventory: "Dopisy Rombaldovi Collalto adresované odesílateli: Molart, Lustriers, Spinola, apoštolský nuntius '
               'Castro a jiní, připojen šifrovací klíč pro styk mezi Collaltem a Harrachem; 24 kusů". Whether the letters themselves '
               'carry cipher is not stated; the key is the point.',
        why='A key of the Collalto chancery (with Karl von Harrach, Ferdinand II\'s privy councillor and Wallenstein\'s father-in-law) '
            'filed with Lustrier letters: the likely key route for the ciphered Collalto files above.',
        importance=3, solvability=3, difficulty=2,
        verify='Order scans of the key; test it on inv. 1774, 1775, 1719, 1862.',
        links=[aron(MZA, '9328af01-e1e8-444a-bd48-cbf22a488882')], access_note=ACC_MZA,
    ),
    # ---- Dietrichstein (Prince Ferdinand Joseph Dietrichstein, Obersthofmeister of Leopold I) ----
    dict(
        year=1686, date='1686',
        title='Count Anton Johann Nostitz, imperial envoy in Stockholm, to Prince Ferdinand Dietrichstein: reports partly in cipher',
        correspondents='Anton Johann Nostitz-Rieneck (imperial envoy to Sweden) -> Prince Ferdinand Joseph Dietrichstein',
        place='Stockholm', language='German', region='Central Europe', period='1651-1700',
        shelfmark=f'{DIET} > Švédsko, inv. č. 69',
        folio_note='21 fol., "Zprávy, částečně šifrované"',
        cls='B',
        status='MZA inventory: reports, partly ciphered, on Sweden and its neighbours (Danish-Hamburg dispute and fighting, the '
               'Emperor\'s request for a Swedish contingent against the Turks); German, 21 fol. Key route: SOA Plzeň, Rodinný '
               'archiv Nostitz-Rieneck, inv. 91 (Nostitz\'s Swedish diplomatic correspondence 1685-1690, "přiložen klíč k šifře"; '
               'separate row).',
        why='Imperial diplomacy in Stockholm in the year of the Augsburg League and the Danish siege of Hamburg; key held in another '
            'Czech archive.',
        importance=3, solvability=3, difficulty=2,
        verify='Order scans of inv. 69 and of SOA Plzeň Nostitz-Rieneck inv. 91 (key); apply.',
        links=[aron(MZA, '85bef9d1-beea-4f5e-ac22-bbc0a928b558')], access_note=ACC_MZA,
    ),
    dict(
        year=1686, date='1685-1688',
        title='Count Wenzel Ferdinand Popel von Lobkowitz, imperial envoy in Paris, to Prince Ferdinand Dietrichstein: reports partly in cipher',
        correspondents='Wenzel Ferdinand Popel von Lobkowitz (imperial envoy to Louis XIV) -> Prince Ferdinand Joseph Dietrichstein',
        place='Paris', language='German (probable)', region='Central Europe', period='1651-1700',
        shelfmark=f'{DIET} > Francie, inv. č. 34',
        folio_note='folio count not given; "Zprávy, částečně šifrované"',
        cls='C',
        status='MZA inventory: reports, partly ciphered, and correspondence: journey and arrival in Paris 1685, the ceremonial, '
               'Franco-Spanish relations (fear that France will exploit the truce). No key or decipherment mentioned.',
        why='The Emperor\'s envoy at Versailles between the Truce of Ratisbon and the Nine Years\' War, writing to Leopold I\'s '
            'Obersthofmeister.',
        importance=4, solvability=2, difficulty=3,
        verify='Order scans; look for Lobkowitz\'s official despatches (HHStA Frankreich Berichte) with their decipherments as a '
               'parallel text.',
        links=[aron(MZA, 'b99bfeb4-fdc7-4849-9459-8ab24861815a')], access_note=ACC_MZA,
    ),
    dict(
        year=1680, date='1679-1680',
        title='Military reports to FML Jakob Leslie from Upper Hungary, with cryptographic letters of Lt-Col Saponara and their number key',
        correspondents='Lt-Col Saponara and others -> Field Marshal-Lieutenant Count Jakob Leslie',
        place='Tokaj / Košice / Kežmarok', language='German, Latin, Italian, French', region='Central Europe', period='1651-1700',
        shelfmark=f'{DIET} > Rakouské země > Uhry, inv. č. 676',
        folio_note='folio count not given; "kryptografické dopisy podplukovníka Saponary s číselným šifrovacím klíčem"',
        cls='A',
        status='MZA inventory: military reports to Leslie during the campaign in Hungary (Tokaj, Košice, Kežmarok): cryptographic '
               'letters of Lt-Col Saponara with a numerical cipher key, prisoners from the insurgents (Thököly\'s kuruc), troop '
               'movements, supply. Key filed with the letters.',
        why='Field intelligence from the start of the Thököly rising, with its key in the same file: a quick, checkable reading.',
        importance=3, solvability=3, difficulty=1,
        verify='Order scans of the Saponara letters and the key; apply.',
        links=[aron(MZA, '41d6e42d-d213-482e-8543-757c0aa4355d')], access_note=ACC_MZA,
    ),
    # ---- SOA Plzeň ----
    dict(
        year=1687, date='1685-1690',
        title='Swedish diplomatic correspondence of the imperial envoy Anton Johann Nostitz, with a key to the cipher',
        correspondents='Leopold I and the imperial chancery <-> Anton Johann Nostitz-Rieneck (envoy in Stockholm)',
        place='Vienna / Stockholm', language='German', region='Central Europe', period='1651-1700',
        shelfmark='SOA Plzeň, Rodinný archiv Nostitz-Rieneck, Sokolov, Osobní záležitosti, Antonín Jan Nostitz-Rieneck, inv. č. 91 '
                  '(orig. sig. H 3), kart. 18',
        folio_note='folder; "Přiložen klíč k šifře" (cipher key attached)',
        cls='B',
        status='SOA Plzeň inventory: among others missives of Leopold I with copies of notes to the King of Sweden (Swedish royal '
               'family, alliance against the Turks, France, England, Spain, Denmark, Poland); key to the cipher attached. Whether '
               'ciphertext is in the file is not stated. Sibling of MZA G 140 inv. 69 (Nostitz\'s partly ciphered reports to '
               'Dietrichstein, 1686).',
        why='The key of the imperial embassy in Stockholm 1685-90, with rescripts that may be partly ciphered; unlocks the '
            'Dietrichstein reports.',
        importance=3, solvability=3, difficulty=2,
        verify='Order scans of the key and any ciphered rescripts; test on MZA G 140 inv. 69.',
        links=[aron(PLZ, '98194254-4cad-4ecb-876f-34b15f262f9c')], access_note=ACC_PLZ,
    ),
    dict(
        year=1624, date='1621-1627',
        title='Prince Christian II of Anhalt-Bernburg to Wilhelm Verdugo: letters in cipher',
        correspondents='Christian II (the Younger), Prince of Anhalt-Bernburg -> Wilhelm (Guillermo) Verdugo, imperial colonel, '
                       'from 1623 governor of the Lower Palatinate',
        place='unknown', language='German or Italian (not stated)', region='Central Europe', period='1611-1650',
        shelfmark='SOA Plzeň, Rodinný archiv Verdugo, Doupov, Vilém Verdugo, Veřejná činnost, inv. č. 13 (orig. sig. C 4), kart. 2',
        folio_note='folder 1621-1627; writing field: "šifrované písmo" (cipher script)',
        cls='C',
        status='SOA Plzeň inventory: folder "Kristian ml. kníže z Anhaltu", 1621-1627, writing "šifrované písmo". Verdugo captured '
               'Christian at the White Mountain (1620) and negotiated his release (May 1621); a ciphered correspondence between '
               'them afterwards is not reported in the literature found. Christian\'s diaries are edited (HAB Wolfenbüttel '
               'digital edition) and may name the letters.',
        why='A Protestant prince pardoned after the White Mountain keeping a ciphered line to the Spanish-imperial officer who had '
            'held him: a small, unexpected channel of 1620s politics.',
        importance=3, solvability=2, difficulty=3,
        verify='Order scans; search the digital edition of Christian II\'s diaries (diglib.hab.de / edition) for Verdugo and '
               '"Ziffer" to date the letters and find cribs.',
        links=[aron(PLZ, '67ffa475-51b9-4ffd-b16d-515a4e354025')], access_note=ACC_PLZ,
    ),
    dict(
        year=1644, date='1644',
        title='Burgrave [of Dohna] to Maximilian von Trauttmansdorff, 1644, with a cipher key enclosed',
        correspondents='[Burgrave of Dohna] -> Maximilian von Trauttmansdorff (Ferdinand III\'s chief minister)',
        place='unknown', language='German (probable)', region='Central Europe', period='1611-1650',
        shelfmark='SOA Plzeň, Rodinný archiv Trauttmansdorffů, Pozůstalosti, Maxmilián z Trauttmansdorffu, Korespondence s '
                  'jednotlivci, inv. č. 148, kart. 8',
        folio_note='folder; "Přiložen šifrovací klíč"',
        cls='B',
        status='SOA Plzeň inventory: folder "[z Donína], purkrabí", 1644, "Přiložen šifrovací klíč". Ciphertext not stated. Other '
               'letters of this fonds are on DECODE (Kurtz von Senftenau 1639, inv. 200 kart. 9, R3811-R3815, '
               'targets/kurtz1639); this folder is not.',
        why='Trauttmansdorff in 1644 was preparing the Westphalian negotiations; a correspondent issued with a key implies a '
            'ciphered exchange in that year.',
        importance=3, solvability=2, difficulty=2,
        verify='Order scans of inv. 148; check whether the Dohna letters carry cipher; ask whether DECODE\'s Trauttmansdorff '
               'harvest (R3811 ff.) covered kart. 8.',
        links=[aron(PLZ, '4001bde3-70fe-44cb-b215-9c6a6aa619f0')], access_note=ACC_PLZ,
    ),
    dict(
        year=1694, date='1686-1702',
        title='Reports from agents to Count Christoph Wenzel Nostitz, with a cipher key attached',
        correspondents='agents (unnamed) -> Christoph Wenzel Nostitz (Bohemian official, later Oberstlandkämmerer?)',
        place='unknown', language='German (probable)', region='Central Europe', period='1651-1700',
        shelfmark='SOA Plzeň, Rodinný archiv Nostitzů - Planá, Starší větev, Kryštof Václav z Nostitz, Veřejná činnost, '
                  'Korespondence, inv. č. 306, kart. 84',
        folio_note='folder "Zprávy od agentů"; "Přiložen šifrovací klíč"',
        cls='B',
        status='SOA Plzeň inventory: folder "Zprávy od agentů" (reports from agents), 1686-1702, cipher key attached. Ciphertext '
               'not stated; agents\' reports filed with a key usually carry ciphered passages.',
        why='A Bohemian magnate\'s intelligence reports over sixteen years with their key.',
        importance=2, solvability=3, difficulty=2,
        verify='Order scans; confirm the reports carry cipher; apply the key.',
        links=[aron(PLZ, '7630fbf6-b30d-4596-9259-6e2c3ac7527a')], access_note=ACC_PLZ,
    ),
    # ---- Národní archiv Praha ----
    dict(
        year=1799, date='1798-1799',
        title='Vittorio Fossombroni to Count Marulli, Tuscan envoy to the Cisalpine Republic: ciphered letters, with the Grand Duke\'s ciphers',
        correspondents='Vittorio Fossombroni (Tuscan foreign minister) -> Count G. Marulli (Tuscan envoy at Milan)',
        place='Florence -> Milan', language='Italian', region='Italy', period='1701-1800',
        shelfmark='Národní archiv, Rodinný archiv toskánských Habsburků - Ferdinand III. (NAD 1044/2), inv. č. 7, kart. 1',
        folio_note='folder 1798-1799: ciphers used by Grand Duke Ferdinand III in correspondence with political figures, and '
                   'ciphered letters of Fossombroni to Marulli',
        cls='B',
        status='NA finding aid no. 474 (RAT díl IV): "Šifry užívané v písemném styku velkovévody Ferdinanda s různými osobnostmi '
               'politického života. Šifrované dopisy V. Fossombroniho toskánskému vyslanci v cisalpské republice hraběti '
               'Marullimu." Keys and ciphertext in the same folder; no decipherment mentioned.',
        why='Tuscany\'s foreign minister instructing his envoy to the French sister-republic in the months before the French '
            'occupation of Tuscany (March 1799); the Grand Duke\'s own cipher tables filed with them.',
        importance=4, solvability=3, difficulty=2,
        verify='Order scans of kart. 1; apply the filed ciphers; check the Fossombroni papers in the Archivio di Stato di Arezzo '
               'and the Esteri files in the Archivio di Stato di Firenze for Marulli\'s side.',
        links=[{'href': 'https://vademecum.nacr.cz/vademecum/permalink?xid=79cb05ea-3aba-4858-b908-096244506dd0',
                'label': 'NA VadeMeCum record'}], access_note=ACC_NA,
    ),
    dict(
        year=1812, date='1812',
        title='Ciphered letter to Metternich, 1812 (original), filed with "Noty a šifry" in the Acta Clementina',
        correspondents='unknown -> Clemens von Metternich (Austrian foreign minister)',
        place='unknown', language='unknown (French or German probable)', region='Central Europe', period='1801-1900',
        shelfmark='Národní archiv, Rodinný archiv Metternichů - Acta Clementina (NAD 611/4), Varia, X. Tabulky, stavební plány, '
                  'šifry, inv. č. 96, kart. 36, fol. 16-17 (9th partial inventory, finding aid no. 1237, A. Haas 1968, p. 11)',
        folio_note='fol. 16-17, one original ("Šifrovaný dopis Metternichovi 1812 - 1 orig."); the same section has inv. 98 '
                   '"Noty a šifry - 4 opisy (fol. 24-30)", undated, possibly keys',
        cls='B',
        status='Seen in the scanned typescript finding aid (NA VadeMeCum, finding aid 1237, scan 15 of 39): section X "Tabulky, '
               'stavební plány, šifry", inv. 96 "Šifrovaný dopis Metternichovi 1812 - 1 orig. (fol. 16-17)", inv. 98 "Noty a '
               'šifry - 4 opisy (fol. 24-30)". Sender and decipherment not stated. The ciphertext itself is not online.',
        why='A ciphered original addressed to Metternich in 1812, the year of the Franco-Austrian alliance and the Russian '
            'campaign, kept by Metternich among his curiosa with copies of ciphers.',
        importance=3, solvability=2, difficulty=3,
        verify='Order scans of kart. 36 fol. 16-17 and 24-30; identify the sender; test inv. 98 as the key.',
        links=[{'href': 'https://vademecum.nacr.cz/vademecum/', 'label': 'NA VadeMeCum (search "Acta clementina", finding aid 1237)'}],
        access_note=('the finding aid is scanned in NA VadeMeCum (Zoomify viewer); the documents are not; order from the Národní '
                     'archiv, Praha'),
        seen='catalogue',
    ),
    # ---- SOA Zámrsk ----
    dict(
        year=1831, date='1831',
        title='Seykora family memoir book written in a number cipher',
        correspondents='a member of the Seykora family, Kostelec nad Orlicí (private notes)',
        place='Kostelec nad Orlicí', language='Czech or German (probable)', region='Central Europe', period='1801-1900',
        shelfmark='SOkA Rychnov nad Kněžnou, Rodinný archiv Seykorových, Kostelec nad Orlicí, inv. č. 60/1 (storage 44)',
        folio_note='one manuscript book, "Kniha pamětních zápisů (rukopis - číslová šifra)"',
        cls='C',
        status='SOA Zámrsk ARON: "Kniha pamětních zápisů (rukopis - číslová šifra)", 1831. A private memoir book in a number '
               'cipher; no key mentioned.',
        why='A whole ciphered diary of a small-town family in the 1830s: a long ciphertext, probably a simple number substitution, '
            'good for a ciphertext-only attempt.',
        importance=1, solvability=3, difficulty=2,
        verify='Ask SOkA Rychnov for a few scans; check length and system.',
        links=[aron(ZAM, 'a87cd5fb-f392-479a-a284-b120b20f2698')], access_note=ACC_ZAM,
    ),
]

KEY_LEADS = [
    dict(year=1630, date='17th century (c. 1625-1634)',
         title='Cipher key used by "Archduke Maximilian" (so the inventory; Archduke Maximilian III died in 1618, so probably Elector Maximilian I of Bavaria) with Albrecht von Wallenstein, Duke of Friedland; and a second, general key',
         shelfmark=f'{COLL}, inv. č. 1887',
         note='MZA inventory: "Šifrovací klíč, kterého užíval arcivévévoda Maxmilian ve styku s vévodou frýdlantským Albrechtem z '
              'Valdštejna; druhý šifrovací klíč, všeobecný". Key only. For Wallenstein ciphertexts see Roubík 1931 '
              '(Valdštejniana, NA NAD 189).',
         links=[aron(MZA, 'e6020539-09f4-4ca3-a403-53c547cbd914')]),
    dict(year=1758, date='1758',
         title='Prussian cipher key used in the Silesian fortresses (copy), Laudon papers',
         shelfmark='MZA Brno, Rodinný archiv Laudonů, Bystřice pod Hostýnem, Gideon Ernst Laudon, Vojenské záležitosti, Sedmiletá válka, inv. č. 73',
         note='German, 8 fol., copy. Captured or intercepted Prussian key of the Seven Years\' War; would fit any intercepted Prussian '
              'fortress correspondence of 1758.',
         links=[aron(MZA, '3ea791b4-9697-4f47-a532-f3c56895aba5')]),
    dict(year=1705, date='undated (1686-1724 context)',
         title='Cipher keys used by Gottlieb, Ernst Friedrich and Leopold Viktorin Windischgrätz with ministers',
         shelfmark='SOA Plzeň, Rodinný archiv Windischgrätzů, Oddělení B, Spisy, Říšská dvorní rada - miscellanea, inv. č. 1403 (orig. 103), item 5',
         note='Keys of the Windischgrätz diplomats (Gottlieb W. was imperial envoy and Reichshofrat president). Check against the '
              'repo target windischgraetz1720 and the Windischgrätz-Starhemberg key DECODE R7928.',
         links=[aron(PLZ, '66bb7756-a204-421a-ac63-e01b67e4980c')]),
    dict(year=1837, date='1837',
         title='"Cifra numerica" of the Tuscan legation in Paris',
         shelfmark='Národní archiv, Rodinný archiv toskánských Habsburků - Zastupitelské úřady (NAD 1044/11), inv. č. 56, sig. XXIII/1-55, kart. 44',
         note='Sub-file "Cifra numerica" in the 1837 files of the Tuscan legation in Paris (finding aid no. 364). Whether ciphertext '
              'accompanies it is not stated.',
         links=[{'href': 'https://vademecum.nacr.cz/vademecum/permalink?xid=a288b5e2-6f60-40e9-bfdb-0422eb53a703', 'label': 'NA VadeMeCum record'}]),
    dict(year=1818, date='1818',
         title='Decipherment key ("dešifrovací klíč") filed with Stürmer\'s despatches from Constantinople, Hudelist papers',
         shelfmark='Národní archiv, Rodinný archiv Metternichů - Acta Clementina (NAD 611/4), korespondence politická Hoppe, Hudelist, '
                   'Neumann (finding aid no. 621, A. Haas), p. 9, item of Sept 1818',
         note='Seen in the scanned finding aid (VadeMeCum, scan 11 of 31): "... Stürmer Metternichovi 1818 1 orig., dešifrovací klíč, '
              'Fleischackel Hudelistovi ...". Stürmer was internuncio at the Porte; the key may serve his ciphered reports in HHStA Türkei.',
         links=[{'href': 'https://vademecum.nacr.cz/vademecum/', 'label': 'NA VadeMeCum (search "Hudelist")'}]),
    dict(year=1822, date='1822',
         title='Decipherment key for the Metternich-Lieven correspondence (copy), in the bound volumes of Metternich letters to Dorothea Lieven',
         shelfmark='Národní archiv, Rodinný archiv Metternichů - Acta Clementina (NAD 611/4), korespondence politická Lieven '
                   '(6th partial inventory, finding aid no. 623), "Correspondance intime du Prince de Metternich 1818-1826", vol. IX, fol. 4',
         note='Seen in the scanned finding aid (scan 7 of 9): "fol. 4: dešifrovací klíč pro korespondenci Metternich-Lievenová 1822 - '
              'opis". The letters are largely printed (Hanoteau 1909 for 1818-19; Quennell 1937 for her side), so a ciphered '
              'passage would first be checked against print.',
         links=[{'href': 'https://vademecum.nacr.cz/vademecum/', 'label': 'NA VadeMeCum (search "Acta clementina", finding aid 623)'}]),
    dict(year=1810, date='c. 1806-1815',
         title='List of ciphers used in the Metternich-Floret correspondence',
         shelfmark='Národní archiv, Rodinný archiv Metternichů - Acta Clementina (NAD 611/4), Osobní věci Klementa Metternicha, '
                   'inv. č. 322 (14th partial inventory, finding aid no. 1242, p. 35)',
         note='Seen in the scanned finding aid (scan 41 of 66): "Seznam šifer používaných v korespondenci Metternich-Floret". '
              'Engelbert von Floret was Metternich’s secretary of embassy in Paris and later his close aide.',
         links=[{'href': 'https://vademecum.nacr.cz/vademecum/', 'label': 'NA VadeMeCum (search "Acta clementina", finding aid 1242)'}]),
]


def main():
    rows = []
    for r in ROWS:
        r = dict(r)
        r.setdefault('source', SRC)
        r.setdefault('score_note', SCORE)
        r.setdefault('prior_art', PRIOR)
        r.setdefault('seen', 'catalogue')
        r.setdefault('needs_archive_scan', 'yes')
        rows.append(r)
    json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(KEY_LEADS, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(rows), 'rows,', len(KEY_LEADS), 'key leads')


if __name__ == '__main__':
    main()
