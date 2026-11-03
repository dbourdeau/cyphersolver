# Vetting of the uk_retest leads, 3 Nov 2026. Writes vetting blocks to research/leads.json; --promote and --close are run separately.
import json

BY = 'claude, uk_retest vetting session'
DATE = '2026-11-03'
NO_DECODE = 'Not on DECODE: known.py (which includes the DECODE list) has no hit for {}.'
NO_LASRY = 'No Lasry paper or GL.htm item found: known.py and a web search on the correspondents.'
TOMO_ELIZ = ("cryptiana elizabeth.htm read 3 Nov 2026: no Anthony Bacon, Standen or Lambeth entry; only a passing note of a 1595 Wilton "
             'to Essex polyalphabetic letter, after Daybell p. 157.')
TOMO_NONE = 'No cryptiana page on this correspondence found by web search; not listed in the pages checked.'

OPEN = {
    1989: dict(
        seen=dict(kind='not online', where='Lambeth CalmView record MSS-647-662/649/490-5, read 3 Nov 2026. The leaves were not seen: images are behind the Early Modern England subscription; microfilm is Lambeth MS Film 793',
                  extent='ff. 490-5, 6 leaves; how much is cipher is not stated',
                  cipher="Archive's description: 'Letters in cypher to BACON (Anthony), Secretary to the Earl of Essex.' No decipherment is noted, but the leaves were not seen, so an interlinear reading is not excluded."),
        prior_art=dict(decode=NO_DECODE.format("'MS 649' or 'Anthony Bacon'"), tomokiyo=TOMO_ELIZ, lasry=NO_LASRY,
                       edition="Birch, Memoirs of the Reign of Queen Elizabeth (1754) i, OCR searched: he uses Bacon's papers and summarises cipher letters (Standen 8 Sept 1592, 'most part in cypher'; Foulis; Morison), so some cipher in this series was read then. His folio notes are poorly OCRed and no citation of vol. iii ff. 490-5 was found, so whether he used these leaves remains unsettled.",
                       literature="Web search; Tosh's 2013 QMUL thesis on Bacon's letters is the likeliest discussion, but its PDF did not download; Hammer 1999 not read. No study of these leaves found."),
        key_check='No Bacon, Standen or Essex secretariat key is held in the repo. Tomokiyo gives none. The sender is unknown, so no key can be matched.',
        duplicates="known.py on 'MS 649', 'Anthony Bacon' and 'Standen': only the lead itself and a catalogue entry that mentions Standen's cipher sets of 1594 as a possible pair. Not a duplicate."),
    1991: dict(
        seen=dict(kind='not online', where='PRONI eCatalogue records D572/17/53, /56, /70, /106, /159, read 3 Nov 2026; the letters are open on microfilm MIC/438/5-6, not online',
                  extent='three items; length not stated',
                  cipher="Archive's descriptions: 'Copy letter in cipher'; 'Copy letter in cipher - partly deciphered by Macartney'; 'Letter in cipher'. Only /56 notes a reading, and that is partial."),
        prior_art=dict(decode=NO_DECODE.format("'D572' or these letters; 'Francis Drake' hits only catalogue 833 and lead 1156"), tomokiyo=TOMO_NONE, lasry=NO_LASRY,
                       edition='HMC Fortescue (Dropmore) iii, OCR searched: 17 Drake mentions and a summary of his secret intelligence, no text of these letters. Roberts, Macartney mission literature not read. The Foreign Office copies in FO 28 were not checked and may carry decipherments.',
                       literature='Web search found no study of Drake’s 1795 cipher; BL Drake papers are catalogued as partly cypher, with no reading noted.'),
        key_check="No Drake key is held. Catalogue 833's Drake-Stuart readings (1803-04) are unobtained and later. Macartney's partial reading on /56 is the likely way in.",
        duplicates="known.py on 'D572', 'Macartney', 'Francis Drake', 'Grenville': siblings only (catalogue 833, lead 1156 Devon; Huntington Macartney papers are India 1780s). Not a duplicate."),
    1992: dict(
        seen=dict(kind='not online', where='RMG archive records rmgc-object-480816 (CRK/4/136), 480811 (CRK/4/131), 480790, read 3 Nov 2026; catalogue only, no image found',
                  extent='one letter, length not stated; siblings CRK/4/108, /131 and the 13 Apr 1796 letter are partly cipher',
                  cipher="Archive's description: 'Drake to unknown, My Lord, undated [1796], in cipher'. No decipherment noted."),
        prior_art=dict(decode=NO_DECODE.format("'CRK/4' or '480816'"), tomokiyo=TOMO_NONE, lasry=NO_LASRY,
                       edition="Nicolas's Nelson Dispatches prints mainly Nelson's outgoing letters; vol. 1 OCR has no Drake cipher passage; vol. 2 (1795-97) could not be downloaded, so is unchecked. The addressee is unknown, so no calendar could be searched by name.",
                       literature='Web search found no discussion of the Drake-Nelson cipher.'),
        key_check='No Drake key is held; see lead 1991, the same writer and years. The Nelson correspondence may share a cipher with it.',
        duplicates="known.py on 'CRK/4', '480816', 'Francis Drake': siblings only (catalogue 833, leads 1156, 1991). Not a duplicate."),
}
HOLD = {
    1990: 'Held 3 Nov 2026: a single leaf "Latin and cypher"; the cipher may be a few words, and nothing but the catalogue line is known.',
    1995: 'Held 3 Nov 2026: PRONI T series is usually a typed copy that may not reproduce the cipher, and the record already summarises the content. See the Chatsworth original first.',
    1996: 'Held 3 Nov 2026: a register of Melfort\'s Rome letters of 1690 exists (BL Lansdowne 1163, per NLI), and Macpherson i notes Melfort drafts with key and cypher, so this is probably readable from those. NLS record not reread (Cloudflare).',
}

leads_doc = json.load(open('research/leads.json', encoding='utf-8'))
leads = leads_doc if isinstance(leads_doc, list) else leads_doc['leads']
by_id = {x['id']: x for x in leads}
for i, v in OPEN.items():
    by_id[i]['vetting'] = dict(date=DATE, by=BY, verdict='open', **v)
for i, note in HOLD.items():
    by_id[i]['vetting_note'] = note
r = by_id[1992]
r['shelfmark'] = 'Royal Museums Greenwich (National Maritime Museum), CRK/4/136 (siblings CRK/4/108, /131, partly in cipher)'
json.dump(leads_doc, open('research/leads.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
