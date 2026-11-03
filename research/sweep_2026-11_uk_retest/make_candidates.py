# Builds candidates.json for the UK/Ireland retest of 3 Nov 2026 (see README.md). Rows scored from catalogue descriptions only.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRONI = 'https://apps.proni.gov.uk/eCatNI_IE/SearchPage.aspx'
LPL = 'https://archives.lambethpalacelibrary.org.uk/CalmView/Record.aspx?src=CalmView.Catalog&id='
NLS = 'https://manuscripts.nls.uk/repositories/2/archival_objects/'
PRIOR = ('open as far as checked (3 Nov 2026: known.py on shelfmark and correspondent, no hit on this item; one web search; '
         'edition, DECODE on the web and Lasry not searched item by item)')
P = 'PRONI eCatalogue'
L = 'Lambeth Palace Library catalogue (CalmView)'
N = 'NLS, Archives and Manuscripts Catalogue'


def row(year, date, title, corr, place, lang, period, shelf, folio, cls, status, why, imp, sol, dif, links, portal, **kw):
    r = dict(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, region='England', period=period,
             shelfmark=shelf, folio_note=folio, cls=cls, status=status, why=why, importance=imp, solvability=sol, difficulty=dif,
             score_note='Scored from the archive description during the UK/Ireland retest of 3 Nov 2026 (research/sweep_2026-11_uk_retest/); not viewed',
             verify=kw.pop('verify', 'Order or view the leaf; measure the cipher; check for a decipherment or key in the same volume or fonds.'),
             links=links, seen='catalogue', source=portal, prior_art=kw.pop('prior', PRIOR), needs_archive_scan='yes',
             access_note=kw.pop('access', 'catalogue record only; digitisation not checked'))
    r.update(kw)
    return r


PL = [{'label': 'PRONI eCatalogue search', 'href': PRONI}]
R = [
    row(1593, 'not dated in the record; MS 649 is vol. 3 of the Bacon papers, reported as 1592-1594', 'Letters in cypher to Anthony Bacon, secretary to the Earl of Essex',
        'unknown → Anthony Bacon', 'unknown', 'unknown', '1589-1598', 'Lambeth Palace Library MS 649, ff. 490-5', 'ff. 490-5, 6 leaves',
        'C', "Catalogue: 'Letters in cypher to BACON (Anthony), Secretary to the Earl of Essex'; no decipherment noted. Microfilm: Lambeth MS Film 793.",
        "Essex's foreign intelligence network. A whole item catalogued as cipher, and the correspondents of this volume include agents such as Anthony Standen.",
        5, 3, 3, [{'label': 'Lambeth record', 'href': LPL + 'MSS-647-662%2f649%2f490-5'}], L,
        verify="See the leaves (Lambeth Film 793, or the Early Modern England / State Papers Online images of MS 649, subscription). Check Birch's Memoirs of Elizabeth 1754, Birch's copies in BL Add MS 4109-24, and Bill's 1974 index.",
        prior="open as far as checked (3 Nov 2026: known.py on 'MS 649' and 'Anthony Bacon' no hits; Tomokiyo elizabeth.htm has no Bacon or Standen entry, and notes only a 1595 Wilton to Essex polyalphabetic letter from Daybell; web search found no decipherment; Birch 1754 not checked)",
        access='images reported in a subscription database (Early Modern England, Adam Matthew); not seen'),
    row(1620, 'early 17th century (the neighbouring item is c. 1620)', "Unsigned letter to 'My Lord' on an intercepted letter of the King of Spain and Cardinal Albert, Latin and cypher",
        "unknown → 'My Lord'", 'unknown', 'Latin', '1611-1650', 'Lambeth Palace Library MS 941, item 182', 'item 182, 1 f.', 'C',
        "Catalogue: 'concerning the contents of an intercepted letter by the King of Spain, Cardinal Albert, and others. Latin and cypher. 1 f.'; no decipherment noted.",
        'A single leaf that may be a codebreaker report on Spanish intercepts: the cipher may be the intercept itself.', 3, 3, 3,
        [{'label': 'Lambeth MS 941', 'href': LPL + 'MSS%2f929-942%2f941'}], L),
    row(1795, '5 and 26 Sept 1795, and one letter of 1795', 'Francis Drake, Genoa → Lord Grenville: copy letters in cipher, one partly deciphered by Macartney',
        'Francis Drake → Lord Grenville (copies in the Macartney papers)', 'Genoa', 'English', '1701-1800',
        'PRONI D572/17/53, D572/17/56, D572/17/159 (open copies on microfilm MIC/438/5-6)', 'three items', 'B',
        "Catalogue: 'Copy letter in cipher'; /56 'partly deciphered by Macartney'; /159 'Letter in cipher'. Related: D572/17/106 Trevor to Macartney on a Madrid cipher letter 'which he and Macartney were unable to read', sent to Drake for deciphering; D572/17/70 Bute to Drake.",
        "Macartney's partial decipherment of /56 is a crib into a system that is otherwise unread here. Grenville's Foreign Office copy (FO 28) may be deciphered, so check it first.",
        3, 4, 2, PL, P, verify='Order MIC/438/5-6. Compare FO 28 at TNA and BL Drake papers (a 1795-96 volume is described as partly cypher).',
        family='Drake cipher family: catalogue entry 833 and lead 1156'),
    row(1796, 'undated, [1796]', "Francis Drake → 'My Lord', in cipher", "Francis Drake → unknown 'My Lord'", 'Genoa', 'English', '1701-1800',
        'Royal Museums Greenwich, archive object 480816', 'item described as in cipher', 'C',
        "Catalogue title: 'Drake to unknown, My Lord, undated [1796], in cipher'; no decipherment noted.",
        'Same minister and system as the PRONI Genoa copies, in a Nelson-related series; found while checking those. A wholly ciphered letter.', 3, 4, 2,
        [{'label': 'RMG record', 'href': 'https://www.rmg.co.uk/collections/archive/rmgc-object-480816'}], 'Royal Museums Greenwich archive catalogue',
        verify='Get the shelfmark from the RMG record and see the letter; check whether Nicolas prints it in Nelson’s dispatches.',
        family='Drake cipher family: catalogue entry 833 and lead 1156'),
    row(1805, '[c. Sept 1805]', 'Harford Jones → Grant, copy letter in cipher', 'Harford Jones → Grant', 'Baghdad (Jones\'s post; not stated in the record)', 'English', '1801-1900',
        'PRONI D3030/2109 (Castlereagh papers)', 'one copy letter', 'C',
        "Catalogue: 'Copy letter from Jones to Grant. [In cipher.] [Castlereagh Correspondence, v, 428.]'. Printed, so probably already deciphered there.",
        'East India Company intelligence from Baghdad; the print should give the plaintext, which would make this a closed pair and a key source for siblings.', 2, 4, 2, PL, P,
        verify='Read Castlereagh Correspondence v, 428 first: if it gives the text, close this lead.'),
    row(1816, 'May 1816', 'Castlereagh papers: extract in cipher of the preceding document', 'unknown (see D3030/4980)', 'unknown', 'unknown', '1801-1900',
        'PRONI D3030/4981', 'one extract', 'C', "Catalogue: 'Extract in cipher of the foregoing.' The foregoing record gives the context and perhaps the plaintext.",
        'If the foregoing item is the clear text this is a crib pair for a Foreign Office cipher of 1816.', 2, 3, 2, PL, P, verify='Read D3030/4980 in the eCatalogue first.'),
    row(1740, '24 March 1739/40', 'Duke of Devonshire → Legge: draft letter partly in cipher, on the Talbots of Malahide and the risk of invasion',
        '[Devonshire] → [Legge]', 'Ireland / London', 'English', '1701-1800', 'PRONI T3158/151 (T = transcript or copy; original presumably Chatsworth)', 'heavily amended draft, part in cipher', 'C',
        "Catalogue: 'Heavily amended draft letter, partly in cipher'. The description summarises the content, so the sense may be known.",
        "Lord Lieutenant's correspondence during the 1740 invasion scare; a draft may show clear text before encipherment.", 2, 4, 2, PL, P,
        verify='PRONI T series is usually a typed copy: check whether it reproduces the cipher at all before anything else.'),
    row(1690, 'catalogue date not captured; Melfort was in Italy from about 1689-91', 'Excerpts from letters of Lord Melfort to Mary of Modena and probably Lewis Innes, from Italy, partly in code',
        'Lord Melfort → Mary, Queen of James II and VII; Lewis Innes', 'Italy', 'English', '1651-1700', 'NLS MS.3836, ff. 3-8', 'ff. 3-8', 'C',
        "Catalogue: 'written from Italy (partly in code), on his interviews and the attitude of various of the Powers to King James'.",
        'Jacobite court. Excerpts with code words left standing are the kind of text a name code can be rebuilt from; check Macpherson, Original Papers, first.', 3, 3, 3,
        [{'label': 'MS.3836', 'href': NLS + '38177'}], N),
]

with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8') as f:
    json.dump(R, f, ensure_ascii=False, indent=1)
print(len(R))
