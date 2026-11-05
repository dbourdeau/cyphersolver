"""Build candidates.json for the Riksarkivet Turcica/Polonica volume sweep (5 Nov 2026).
Rows come from contact sheets (24 images per volume) and full-size checks listed in findings.md."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'Riksarkivet Turcica/Polonica volume sweep (IIIF, Referer route), Nov 2026'
SCORE = ('Scored from sampled images (24 per volume, suspects at 900 px) viewed during the Riksarkivet Turcica sweep, '
         '5 Nov 2026 (research/sweep_2026-11_riksarkivet_turcica/)')
ACCESS = ('scans public on Riksarkivet (sok.riksarkivet.se), no login; scripts need the header '
          'Referer: https://sok.riksarkivet.se/ for the 4000xxxx image series')
PRIOR = ('open as far as checked (5 Nov 2026): known.py finds nothing on the shelfmark or the correspondents; '
         'web search found no decipherment or edition of these letters; DECODE, Tomokiyo and Lasry not searched')


def links(rec, man, imgs):
    out = [{'href': f'https://sok.riksarkivet.se/arkiv/{rec}', 'label': 'NAD record'},
           {'href': f'https://lbiiif.riksarkivet.se/arkis!{man}/manifest', 'label': 'IIIF manifest'}]
    out += [{'href': f'https://sok.riksarkivet.se/bildvisning/{man}_{i:05d}', 'label': f'image {i}'} for i in imgs]
    return out


ROWS = [
    dict(
        year=1712, date='1710-1714',
        title="Stanisław Poniatowski's letters to Charles XII from the Porte: French number cipher with interlinear decipherment",
        correspondents='Stanisław Poniatowski (major general in Swedish service, the King\'s agent at the Ottoman court) -> Charles XII',
        place='Constantinople / Adrianople', language='French (2-3 digit number code mixed with clear words)',
        region='Scandinavia',
        shelfmark='Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/5/8 (Generalmajoren Stanislaus Poniatowski, 1710-1714)',
        folio_note='437 images (series 40006063). Cipher with French decipherment between the lines at images 274, 310 and 328 '
                   '(whole pages); only 24 of 437 images sampled.',
        cls='A',
        status='Catalogue: "Generalmajoren Stanislaus Poniatowski", no mention of cipher. Sampled pages carry long runs of '
               'number groups with the French plaintext written above them by the recipient\'s clerk.',
        why='The King\'s chief negotiator at the Porte during the Bender exile (Prut campaign, 1711 peace, the Kalabalik); '
            'his ciphered reports with their decipherments give a key and a dated series.',
        importance=4, solvability=5, difficulty=2,
        verify='Page the volume and list every ciphered letter; rebuild the code from the interlinear pairs; check whether '
               'Poniatowski\'s code is the Funck/Perman field-chancery code (groups like 135, 61, 87 recur in both).',
        links=links('g1VeVtRgrKYxpcyNAbmkV0', '40006063', [274, 310, 328]),
    ),
    dict(
        year=1712, date='1710-1714',
        title='Bender field-chancery number code: Funck, Perman and von Müllern despatches with interlinear decipherments',
        correspondents='Thomas Funck (envoy at the Porte) -> Charles XII and the Kanslikollegium; commission secretary Hans Perman '
                       '-> H. G. von Müllern; von Müllern -> Funck',
        place='Constantinople / Bender', language='Swedish and French (2-3 digit number code)',
        region='Scandinavia',
        shelfmark='Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/6/9, I/6/10, I/6/14 and I/7/16 '
                  '(Funck to the King 1710-13; to the Kanslikollegium 1711-13; from von Müllern 1711-13; Perman to von Müllern 1711-14)',
        folio_note='I/6/9: 536 images (40006064), image 335. I/6/10: 98 images (40006065), images 58, 66, 70, 86. '
                   'I/6/14: 235 images (40006068), images 69-70 (Müllern to Funck 20 Aug 1711). I/7/16: 153 images (40006070), '
                   'images 20, 33, 39, 45, 71, 77 (whole pages). Drafts in clear: I/6/11 (523 images) and I/6/12 (541).',
        cls='A',
        status='Catalogue says nothing of cipher. The same groups recur in all four volumes (290, 504, 204, 664, 746, 891), '
               'each with the decipherment written between the lines (Swedish; French letter by letter in I/6/14). '
               'Catalogue #1769 (Funck I/6/13, the King\'s letters to Funck) is this code without glosses.',
        why='Charles XII\'s secret correspondence from Bender with his envoys at the Porte, 1710-14. The glossed pages give the key '
            'for #1769 and for any other unglossed despatch of the exile years.',
        importance=4, solvability=5, difficulty=2,
        verify='Collect the interlinear pairs from I/7/16 (densest), rebuild the code, then apply it to #1769 (I/6/13). '
               'Fold this lead into #1769 as its key material if the editor prefers one entry per key.',
        links=links('M3siS1vkbKo6Jzg0U4on60', '40006070', [20, 77])
              + [{'href': 'https://sok.riksarkivet.se/bildvisning/40006064_00335', 'label': 'I/6/9 image 335'},
                 {'href': 'https://sok.riksarkivet.se/bildvisning/40006065_00066', 'label': 'I/6/10 image 66'},
                 {'href': 'https://sok.riksarkivet.se/bildvisning/40006068_00070', 'label': 'I/6/14 image 70'}],
    ),
    dict(
        year=1657, date='1657',
        title="Clas Rålamb's despatches from Constantinople: number cipher with interlinear decipherment",
        correspondents='Clas Rålamb and Gotthard Vellingk (envoys extraordinary) -> Charles X Gustav',
        place='Constantinople', language='Swedish (number code, groups 1-110 and a few in the 800s)',
        region='Scandinavia',
        shelfmark='Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/2/2 (E.o. ablegaterna Clas Rålamb och Gotthard Vellingk, 1657)',
        folio_note='132 images (series 40008933). Cipher at image 23 (two pages of number runs with Swedish between the lines) '
                   'and image 88 (letter of 12 June 1657 signed Clas Rålamb).',
        cls='A',
        status='Catalogue: the volume title only. Rålamb\'s embassy is well studied (his diary, ed. Callmer 1963; the Rålamb '
               'paintings), but no account of his ciphers was found. A different code from the 1711 Funck code.',
        why='The Swedish embassy to Mehmed IV in 1657-58, sent to bind Transylvania into Charles X\'s Polish war; its ciphered '
            'reports and their decipherments give a dated 1650s Swedish chancery code.',
        importance=3, solvability=5, difficulty=2,
        verify='Page the volume for every cipher passage; rebuild the code from the interlinear pairs; compare with the '
               'Rákóczi cipher of 2119.5/4 (lead 2243) and Cantersten 1648.',
        links=links('eWy9xynckH1kcXy2OkH6B5', '40008933', [23, 88]),
    ),
    dict(
        year=1648, date='1648',
        title="Secretary L. Cantersten's despatches from Poland: number cipher with interlinear decipherment",
        correspondents='L. Cantersten (Swedish secretary in Poland) -> Queen Christina',
        place='Poland', language='Swedish (number code, small groups 1-110)',
        region='Scandinavia',
        shelfmark='Riksarkivet, Diplomatica Polonica, SE/RA/2115/I/5/17 (Sekreteraren L. Cantersten, Brev till Kungl. Maj:t, 1648)',
        folio_note='72 images (series R0003211). Image 10: two pages of number runs with Swedish between the lines; images 36 '
                   'and 39 look the same at sheet size. His drafts are I/5/18 (27 images), probably the clear text.',
        cls='A',
        status='Catalogue: volume title only. Sampled page 10 is mostly cipher with the decipherment written above.',
        why='Reports from Poland in the year of Władysław IV\'s death and the Khmelnytsky rising; a dated 1640s Swedish code '
            'with its decipherment and probably the drafts.',
        importance=3, solvability=5, difficulty=2,
        verify='Page I/5/17 for every cipher passage; check I/5/18 for the clear drafts; rebuild the code.',
        links=links('2LDwTnrr44s6hyQquIzkK9', 'R0003211', [10, 36, 39]),
    ),
    dict(
        year=1767, date='1765-1770',
        title="Consul J. A. Molinari's despatches from Tunis: unglossed number cipher in unbroken digit strings",
        correspondents='Johan Adam Molinari (Swedish consul at Tunis) -> the Kanslipresident (Stockholm)',
        place='Tunis', language='French (cipher text numeric, digits run together without separators)',
        region='Other',
        shelfmark='Riksarkivet, Diplomatica Turcica, bihang Tunisica, SE/RA/2119/2119.7/2 (Svenska konsulers skrivelser, J. A. Molinari, 1764-1778)',
        folio_note='732 images (series R0003585). Image 123: letter of Tunis 21 March 1765, a page of digit strings ending in '
                   'clear French; image 366: letter of 7 July 1770, two pages of digit strings, clear close; image 153 looks the same. '
                   'Only 24 of 732 images sampled.',
        cls='C',
        status="Catalogue: consuls' letters, J. A. Molinari; no mention of cipher. The sampled cipher pages carry no decipherment. "
               'The digits are written continuously, so the group length must be found first (likely 2- or 3-digit groups).',
        why="Sweden's consul at Tunis during the 1760s crises with the Regency and the Mediterranean passport system; an "
            'unglossed 18th-century consular code, a ciphertext-only target.',
        importance=3, solvability=3, difficulty=3,
        verify="Page the volume for every cipher letter and any decipherment or key slip; look for the Kanslikollegium's "
               'consular code of the 1760s (Riksarkivet chiffer collections); measure digit-string lengths for the group size.',
        links=links('dw0JGQ1VMKAKw5yXW6pKS1', 'R0003585', [123, 153, 366]),
    ),
]

rows = []
for r in ROWS:
    r.update(source=SRC, score_note=SCORE, access_note=ACCESS, prior_art=PRIOR, seen='image', needs_archive_scan='no',
             period='1701-1800' if r['year'] > 1700 else '1611-1650' if r['year'] < 1651 else '1651-1700')
    rows.append(r)
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
