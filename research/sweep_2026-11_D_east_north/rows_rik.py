"""Rows from the Riksarkivet (Stockholm) digitised Diplomatica volumes, contact sheets viewed 4 Nov 2026."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from cand import add

NAD = 'https://sok.riksarkivet.se/arkiv/'
VIEW = 'https://sok.riksarkivet.se/bildvisning/'
PRIOR = ('open as far as checked (4 Nov 2026: known.py on the shelfmark and the correspondents found nothing; not on DECODE as far as the '
         'Nordic dump goes; no web search hit for a decipherment; Tomokiyo and Lasry not searched for this item)')


def row(man, nid, imgs, **kw):
    r = dict(region='Scandinavia', seen='image', source='Sweep D, Riksarkivet IIIF volume pass, Nov 2026',
             score_note='Scored from sampled images (20 per volume, plus full-size views where noted) viewed during sweep D (research/sweep_2026-11_D_east_north/), Nov 2026',
             prior_art=PRIOR, needs_archive_scan='no', access_note='scans public on Riksarkivet (sok.riksarkivet.se), no login')
    r.update(kw)
    r['links'] = [{'label': 'NAD record', 'href': NAD + nid},
                  {'label': 'IIIF manifest', 'href': f'https://lbiiif.riksarkivet.se/arkis!{man}/manifest'}] + \
                 [{'label': f'image {i}', 'href': f'{VIEW}{man}_{i:05d}'} for i in imgs]
    return r


rows = [
    row('R0000481', 'rp6JwGDAFasc5R6mtPZn00', [37, 38, 40, 41, 42], year=1713, date='Nov-Dec 1713 (received 16 Nov 1713)',
        title="Philipp (Pylyp) Orlyk, Bender: Latin despatches in numeric cipher with the Latin plaintext written between the lines",
        correspondents="Pylyp Orlyk (hetman in exile of the Zaporozhian Host, Charles XII's circle at Bender) -> a Swedish or allied correspondent ('Excellentia', clear covering letter to Mirowicz at image 43)",
        place='Bender', language='Latin', period='1701-1800',
        shelfmark='Riksarkivet, Diplomatica Muscovitica, Cosacica, SE/RA/2113/2113.2/2 ("Fältherren Philip Orliks brev", 1711-1741), ff. about 38-46 (images 37-42 of R0000481)',
        folio_note='394 images (R0000481). Images 37-42: about 6 openings of 2-to-3-digit numbers (values 1-450) with Latin plaintext written line by line above, headed "clavis"; image 43 is the clear covering letter signed Philippus Orlik, Bender 1713.',
        cls='A',
        status='Catalogue calls the volume Orlyk\'s letters to the Swedish king; no mention of cipher. The images carry an interlinear decipherment in the same hand, so the text was read at the time; no key table seen on these openings (a "clavis" is mentioned in the heading of image 37). Not on DECODE (Nordic dump) and not in the repo.',
        why='Hetman Orlyk\'s own cipher during the Pruth aftermath and the Bender stay (Tatar khan, Augustus II, Ukraine, Cossack Ukraine and the Porte): a Ukrainian-Swedish cipher with a plaintext crib for the whole key.',
        importance=4, solvability=5, difficulty=2,
        verify='View images 37-43 and 40-42 at full size, transcribe the numerals against the Latin lines, rebuild the key (homophones, nomenclator), then check the rest of the volume for further cipher.'),
    row('R0003589', 'BZZb19ExraUD08aOGW31T0', [36, 140, 279, 383, 417, 556], year=1736, date='1734-1737',
        title="Höpken and Carlson (Constantinople) to the Chancery College: four-digit numeric code passages with Swedish interlinear plaintext",
        correspondents='Carl Fredrik von Höpken and Edvard Carlson -> Kanslikollegium and the chancery president', place='Constantinople', language='Swedish',
        period='1701-1800', shelfmark='Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/22 (Brev till Kanslikollegium och ..., 1734-1737)',
        folio_note='695 images (R0003589). Image 383 seen at 1000 px: a Swedish letter with rows of four-digit numbers (1000-1700) and Swedish plaintext written between the rows, underlined. Similar underlined passages at about images 36, 140, 279, 417, 556, 660 (thumbnails).',
        cls='A', status='Catalogue: plain letters to the Kanslikollegium and Höpken. The interlinear writing shows the passages were deciphered on receipt; whether every cipher passage in the volume was glossed is not seen. Sibling of the volumes 9/20 and 9/21 (already rows from the 2 Nov volume pass).',
        why='Ottoman-Swedish diplomacy under Frederick I, with a four-digit word code and a large amount of plaintext crib in one volume.',
        importance=3, solvability=5, difficulty=2,
        verify='Page every opening; list the cipher passages and which carry a gloss; build the code from the glossed passages and test it on 9/20-9/21.'),
    row('R0003592', 'iQNIAR5DBKcS0qJ74XjuZ0', [183, 235, 340, 366], year=1739, date='1738-1741',
        title="Höpken and Carlson (Constantinople) to the Chancery College, 1738-41: numeric code passages with interlinear writing",
        correspondents='Carl Fredrik von Höpken and Edvard Carlson -> Kanslikollegium and the chancery president', place='Constantinople', language='Swedish',
        period='1701-1800', shelfmark='Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/23 (Brev till Kanslikollegium ..., 1738-1741)',
        folio_note='522 images (R0003592). Thumbnails show boxed rows of numbers at about image 183 and underlined interlinear passages at 235, 340, 366 (not seen at full size).',
        cls='A', status='Catalogue: plain letters. Cipher seen at thumbnail size only; the same hand, years and code as the 9/20-9/22 volumes.',
        why='The 1738-41 run, covering the Swedish alliance negotiations before the 1741 war.', importance=3, solvability=4, difficulty=2,
        verify='View images 183, 235, 340, 366 at full size; transcribe and glossed-versus-unglossed count.'),
    row('R0003653', 'jGqe5FBo3aUbD63MrKnPm2', [56, 98, 112, 153], year=1739, date='1736-1746',
        title="Constantinople legation papers (chargé d'affaires Carlson, 1736-46): number-cipher passages with interlinear plaintext",
        correspondents='Swedish chargé d\'affaires at Constantinople <-> Stockholm', place='Constantinople', language='Swedish', period='1701-1800',
        shelfmark='Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/29 (Beskickningshandlingar, 1736-1746)',
        folio_note='278 images (R0003653). Image 56 (received 17 Jan 1739): a letter whose lower half is underlined number rows with a gloss; images 98, 112, 153 have similar underlined passages (thumbnail); the rest is accounts and lists.',
        cls='A', status='Catalogue: "Beskickningshandlingar", despatches from Stockholm to Constantinople. Cipher seen at thumbnail size.',
        why='Despatches from Stockholm to the legation with ciphered passages and glosses: the other direction of the same code.', importance=3, solvability=4, difficulty=2,
        verify='View images 56, 98, 112, 153 at full size.'),
]
for r in rows:
    add(r)
