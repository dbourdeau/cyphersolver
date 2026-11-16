"""Write the vetting blocks for leads 2838-2842 (Omont wave 6, 15 Nov 2026) into research/leads.json."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'research' / 'leads.json'
d = json.loads(P.read_text(encoding='utf-8'))
by = {l['id']: l for l in d['leads']}

COMMON_PA = {
    'decode': 'known.py plus the DECODE dumps (views.jsonl, views_b, views_c) and the Cryptoole snapshot, 15 Nov 2026: no record for fr. 15566-15572 outside the Matignon/Mayenne 1586 leaves of fr. 15571-15572 (other folios); the dumps are partial, so "not on DECODE" is as far as they go.',
    'tomokiyo': 'Tomokiyo, "French ciphers during the Reigns of Charles IX and Henry III" (cryptiana.web.fc2.com/code/henryiii.htm, fetched 15 Nov 2026): reconstructs the cipher tables named below from this volume but prints no reading of this text.',
    'lasry': 'Lasry\'s list GL.htm (cryptiana.web.fc2.com/code/GL.htm, fetched 15 Nov 2026, grepped for 15567, 15568, 15571, Bellievre, Hautefort): no entry. His one entry in this run of volumes is fr. 15566 f. 50, a different leaf.',
    'edition': 'No edition of the Bellievre papers for 1584-85 is known; Omont (Catalogue des manuscrits francais, Ancien Saint-Germain I, 1898) only lists the folios.',
    'literature': 'Web searches 15 Nov 2026 (Bellievre, Hautefort, Matignon cipher 1584, fr. 15567/15568): only Tomokiyo and the Lasry-Tomokiyo-Biermann Mary Stuart papers, unrelated.',
}


def vet(n, seen_where, extent, cipher, key_held, dups, key_check):
    pa = dict(COMMON_PA)
    by[n]['vetting'] = {
        'date': '2026-11-15',
        'by': 'claude session 15 Nov 2026 (Claude Sonnet 5.5), Omont wave 6 Chrome/Gallica pass',
        'seen': {'kind': 'scan', 'where': seen_where, 'extent': extent, 'cipher': cipher},
        'prior_art': pa,
        'key_check': key_check,
        'key_held': key_held,
        'duplicates': dups,
        'verdict': 'open',
    }


DUP = ('known.py "15566", "15567", "15568", "15571", "Bellievre", "Hautefort" (15 Nov 2026): the folios are in no ledger; fr. 15571/15572 hits are other leaves '
       '(Matignon Cipher-3 f. 179, Mayenne-Forget, Camus etc., catalogue item 12), and the 1580 Bellievre items are fr. 15906. ')

vet(2838, 'Gallica fr. 15567, ark btv1b90639282, IIIF view 29 (openapi.bnf.fr), viewed at 1400 px on 15 Nov 2026',
    'f. 24: ten lines of cipher signs at the top, then about seven lines of clear text',
    'Sign cipher (homophonic, signs with dots and bars) seen on the leaf; clear paragraph below. A few words are written between the first cipher lines; they are not a decipherment of the block (partial at most).',
    'Tomokiyo\'s reconstructed "Matignon\'s Cipher-1" (from f. 24 and f. 54 of this volume), an image on his page; not copied or tested here.',
    DUP + 'f. 54 of the same volume uses the same cipher per Tomokiyo; not a lead here (not viewed).',
    'Only the Tomokiyo table (key_held); no key in the volume was seen. Not tested.')
vet(2839, 'Gallica fr. 15567, ark btv1b90639282, IIIF views 164-170 (f. 158-164), viewed 15 Nov 2026 (700-px sheets, view 165-168 and 170 and view 29 at 1400 px)',
    'ff. 158-161: about six pages wholly or mostly cipher (two sign alphabets); ff. 162-164 cipher passages inside clear letters',
    'Sign cipher seen over several full pages; the letter closes in clear "de Grenoble ... mars 1584". No decipherment visible on or beside the cipher pages at 700 px; Tomokiyo reports partial interlined decipherment on ff. 158 and 160 (a few words, to reconstruct the table).',
    'Tomokiyo\'s reconstructed "Hautefort\'s Cipher" (from ff. 158, 160 of this volume and f. 207 of fr. 15568), an image on his page; not tested here.',
    DUP + 'Same cipher as lead 2841 (fr. 15568 ff. 207-208) per Tomokiyo: kept separate (different volume and pages).',
    'Only the Tomokiyo table (key_held). Not tested. The interlined words on ff. 158/160 are the partial per-word reading he used for the table, not a full decipherment.')
vet(2840, 'Gallica fr. 15568, ark btv1b9063927n, IIIF views 159-160 (f. 151-152), viewed 15 Nov 2026 (700-px sheet)',
    'ff. 151-152: two pages, dense cipher after plain opening lines',
    'Sign cipher seen over two pages; plain heading lines only. No decipherment on the leaves or in the next folios viewed (views 158-162).',
    'Tomokiyo\'s reconstructed "Matignon\'s Cipher-1" (image on his page; from fr. 15567 ff. 24, 54); not tested here.',
    DUP + 'Tomokiyo lists f. 151 of fr. 15568 under Matignon\'s Cipher-1; distinct from lead 2838 (fr. 15567 f. 24).',
    'Only the Tomokiyo table (key_held). Not tested.')
vet(2841, 'Gallica fr. 15568, ark btv1b9063927n, IIIF views 215-216 (f. 207-208), viewed 15 Nov 2026 (700-px sheet)',
    'ff. 207-208: two full pages, about 36 lines each, entirely cipher',
    'Sign cipher seen over two full pages; no clear text on either leaf and no decipherment beside them (view 214 is a plain letter in another hand).',
    'Tomokiyo\'s reconstructed "Hautefort\'s Cipher" (see lead 2839); not tested here.',
    DUP + 'Same cipher as lead 2839 per Tomokiyo; different volume.',
    'Only the Tomokiyo table (key_held). Not tested.')
vet(2842, 'Gallica fr. 15571, ark btv1b90618802, IIIF views 41-43 (f. 37-38), viewed 15 Nov 2026 (700-px sheet)',
    'f. 37: cipher block of about seven lines at the top of the leaf, then clear text',
    'Sign cipher seen at the top of f. 37; clear text below and on f. 38 (a different letter in another hand). The decipherment Tomokiyo mentions is f. 36 for ff. 34-35, not for this block; none on or with f. 37.',
    'Tomokiyo\'s reconstructed "Chasteauneuf\'s Cipher" (from ff. 34-35, deciphered in f. 36), an image on his page; not tested here, and whether the f. 37 signs belong to the same alphabet was not checked.',
    DUP + 'The script_wave5 README (this day) saw this block (Omont "f. 34") and left it as a note; fr. 15571 f. 177 and f. 179 are other leaves already in the repo.',
    'Only the Tomokiyo table (key_held). Not tested.')
d['leads'] = list(by.values()) if False else d['leads']
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('ok')
