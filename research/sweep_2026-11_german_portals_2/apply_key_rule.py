# Already applied; ids here predate the renumbering of 1989-1996 to 2041-2048 in the merge with main.
"""Key-test results and the 3 Nov 2026 rule change: a cipher with its key filed in the same volume, and no decipherment, may enter the catalogue.

Closes 2026 as read (the one key that could be tested showed a decipherment), 1690 as duplicate of 2004, then writes vetting blocks
with "key_in_volume" for the five leads the rule admits and promotes them. 1980 stays key_lookup: its key is in print, not in the volume."""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LEADS = os.path.join(ROOT, 'research', 'leads.json')
CHECK = os.path.join(ROOT, 'docs', '_check_catalogue.py')
BY = 'Claude session, German portals sweep 2 key test'
TOM = 'nothing found by web search (3 Nov 2026) and no Tomokiyo reference in the repo (known.py); his site was not read page by page'
LAS = 'no paper or GL.htm key for this file found (web search and known.py, 3 Nov 2026)'
NOD = 'not on DECODE: known.py on the shelfmark and names has no hit in the DECODE list (3 Nov 2026)'
ITEMS = {
 1970: dict(where='https://www2.landesarchiv-bw.de/ofs21/olf/druckansicht.php?id_titlaufn=2951408 (print view read 3 Nov 2026); no scan shown',
   extent='item 5 of the file, correspondence of 1726; length not stated',
   cipher='Finding aid quoted: "Chiffrierter Schriftverkehr mit dem Baron von Montigny in Paris mit Chiffriertafeln", 1726. No decipherment is mentioned.',
   edition='no edition of the Montigny letters found (web search 3 Nov 2026); Sattler\'s Geschichte appeared in the results but was not searched for them',
   lit='Deutsche Biographie on Wilhelmine von Grävenitz and Hay\'s A German Pompadour appear in the search, without the cipher; neither was read in full',
   key='HStA Stuttgart A 48/05 Bü 51, item 5: "mit Chiffriertafeln", filed with the letters. Not tested: neither is online.',
   dup='known.py on "A 48/05" and "Montigny": only lead 1668, which names this unit as a sibling, and an unrelated Montigny of 1781 in India.'),
 1979: dict(where='https://www.arcinsys.niedersachsen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=7168843 and 7145076 (read 3 Nov 2026); no scans',
   extent='letters of 1828-30, "z.T. chiffriert"; share in cipher not stated',
   cipher='Finding aid quoted: "z.T. chiffriert" for Nr. 823 and Nr. 347, and "1 Chiffreschlüssel" in Nr. 823. No decipherment is mentioned.',
   edition='no edition of these letters found (web search 3 Nov 2026)',
   lit='The search returned Duke Karl II background and Bundestag records only; nothing on the cipher',
   key='NLA WO 242 N Nr. 823 lists "1 Chiffreschlüssel" in the unit. Its use for Nr. 347 is inferred from the same fonds and correspondent. Not tested: neither is online.',
   dup='known.py on "242 N" and "Veltheim": no other entry for these units (H 242 is a different fonds).'),
 2004: dict(where='https://www.gda.bayern.de/gvl/archive.xhtml?id=Vz++++++3eb11721-0658-4a00-af03-41a136baf5a4 (record read 3 Nov 2026); no Digitalisate link',
   extent='one letter with tables, Prod. 75; length not stated',
   cipher='Finding aid quoted: "Darin: Chiffrierter Brief und Chiffretabellen (Prod. 75)". No decipherment is mentioned.',
   edition='no edition printing this letter found (web search 3 Nov 2026)',
   lit='The search returned pamphlets and general works on the Bavarian Succession; nothing on this letter',
   key='The tables are filed with the letter in Prod. 75. Not tested: not online.',
   dup='known.py on "16091": this lead and lead 1690, the same unit, closed as its duplicate.'),
 2006: dict(where='https://www.gda.bayern.de/gvl/archive.xhtml?id=Vz++++++B9723085-972D-43CE-9EE2-F8A9C2223542 (record read 3 Nov 2026); no Digitalisate link',
   extent='some letters in a file of 1804-05; number not stated',
   cipher='Finding aid quoted: "unter anderem auch chiffrierte Briefe (mit Codeschlüssel)". No decipherment is mentioned.',
   edition='no edition found (web search 3 Nov 2026)',
   lit='The search returned Woellwarth genealogy and general Reichsritterschaft material; nothing on this mission or its cipher',
   key='The code key is in the file, per the finding aid. Not tested: not online.',
   dup='known.py on "4509" and "Wöllwarth": only this lead and a cross-reference to it in catalogue 2005.'),
 2009: dict(where='https://www.gda.bayern.de/gvl/archive.xhtml?id=Vz++++++8D19C993-EA6D-4139-82CD-A658E5D7592D (record read 3 Nov 2026); no Digitalisate link',
   extent='a bound volume of 1811-13; share in cipher not stated',
   cipher='Finding aid quoted: "handschriftlich ergänzte französische Chiffriertabellen (a) alphabetisch, b) numerisch)" and "teilweise Chiffren (nicht aufgelöst)". The archive says the ciphers are not resolved.',
   edition='no edition of this file found (web search 3 Nov 2026)',
   lit='The search returned general histories of the 1812 campaign; nothing on these ciphers',
   key='The tables are in the same volume but are French tables, so they may not read every cipher. Not tested: not online.',
   dup='known.py on "MA 16": only this lead.'),
 2016: dict(where='https://www.arcinsys.niedersachsen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=5364849 (read 3 Nov 2026); no scans',
   extent='cipher pieces in a file of 1544-45; share not stated',
   cipher='Finding aid quoted: "darunter Chiffreteile und Chiffreschlüssel (f. 68)". No decipherment is mentioned.',
   edition='no edition printing these pieces found (web search 3 Nov 2026)',
   lit='Strasser 2017 (Tatra Mt. Math. Publ. 70) covers Heinrich c. 1540 from 1 Alt 8 Nr. 490, not this file; his 2010 article in Braunschweigisches Jahrbuch 91 was not obtained',
   key='NLA WO 1 Alt 8 Nr. 505 f. 68 is the key, per the finding aid; Strasser prints a c. 1540 key of the same duke. Not tested: not online.',
   dup='known.py on "1 Alt 8": siblings Nr. 407-408 (catalogue 2017) and Nr. 549 (lead 2015), not this unit.'),
}
d = json.load(open(LEADS, encoding='utf-8'))
by = {e['id']: e for e in d['leads']}
for n, x in ITEMS.items():
    e = by[n]
    e['access'] = 'archive'
    e['needs_archive_scan'] = 'yes'
    e['prior_art'] = 'open (checked 3 Nov 2026: see vetting block)'
    e['vetting'] = {'date': '2026-11-03', 'by': BY,
        'seen': {'kind': 'not online', 'where': x['where'], 'extent': x['extent'], 'cipher': x['cipher']},
        'prior_art': {'decode': NOD, 'tomokiyo': TOM, 'lasry': LAS, 'edition': x['edition'], 'literature': x['lit']},
        'key_check': x['key'], 'key_in_volume': x['key'], 'duplicates': x['dup'], 'verdict': 'open'}
    e['verify'] = 'Order a scan and try the key filed in the volume; a reading is then "read with known key".'
d_json = json.dumps(d, ensure_ascii=False, indent=1) + '\n'
open(LEADS, 'w', encoding='utf-8').write(d_json)
subprocess.run([sys.executable, CHECK, '--close', '2026', 'read',
    'Key test 3 Nov 2026: read at the time. Cipher letter of 20 Mar 1523 on ff. 19-20 (images 22-23); images 24-25 gloss the same text word by word (the run after "Nemlich" reads "der prinz von Oranien und mir dar zu hab ..."); f. 22 (image 25) is a complete clear copy. Compared on that run; not every passage aligned.'], check=True)
subprocess.run([sys.executable, CHECK, '--close', '1690', 'duplicate', 'Same unit as lead 2004 (Ansbacher Archivalien 16091, Prod. 75).'], check=True)
subprocess.run([sys.executable, CHECK, '--promote'] + [str(n) for n in ITEMS], check=True)
