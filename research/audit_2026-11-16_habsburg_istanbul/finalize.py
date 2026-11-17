"""Write findings.json: hand verdicts for the single-letter entries, rule verdicts (raw/verdicts.json, from verdicts.py) with the
hand overrides below for the multi-item entries 1226-1229. Usage: python -I -X utf8 finalize.py"""
import json, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
V = json.load(open(os.path.join(HERE, 'raw', 'verdicts.json'), encoding='utf8'))

# Hand overrides after reading the regests (id: (verdict, note)).
OVR = {
    56147: ('none', 'the same-day 56148 is an expense account with marginal decipherment, not this letter'),
    56259: ('partial', '56260 (same day) is "the last page of the decipherment of Starzer\'s report"; the rest of the decipherment is not filed, and the regest says the cipher continues undeciphered'),
    57657: ('probable', 'duplicate of the 28 Nov 1615 letter to Mollart: 57652 is its German decipherment (cipher copy fol. 236-239), 57658 another cipher copy pointing to the decipherment at fol. 217-219'),
    59436: ('filed', 'the Lustrier-Questenberg letter is itself "deciphered on a separate sheet"; it entered the list only because the regest notes fol. 41-42, a letter of an unknown person to Kurtz, "only cipher"'),
    60408: ('none', 'the same-day 60409 is an Italian copy of a letter to Schmid, not this one'),
    60432: ('none', 'the same-day 60433 is Schmid\'s letter to Propaganda Fide, a different letter'),
    60437: ('none', 'the same-day 60436 is a letter of Ferdinand III to Schmid, a different letter'),
    61418: ('none', 'the same-day 61437/61440 are Ferdinand III\'s letters to the grand vizier, a different letter'),
    60893: ('filed', '18th-c. copy of the 11 Aug 1644 report; the original 60967 is deciphered in the margin, and 60968 is a chancery extract'),
    60927: ('filed', 'chancery extract with its cipher passages undeciphered; the original 60926 of the same day is deciphered in the margin'),
}
LEFT = {59436: 'fol. 41-42 of Kt. 110 Konv. 3: an unknown person to Kurtz, only cipher (not a separate regest)'}

GROUPS = {
    '1226': 'Starzer (and Gratiani, Gallo) 1611-19, Kt. 93-108',
    '1227': 'Radibrati, Lustrier, Kurtz and others 1621-28, Kt. 108-111',
    '1228': 'Schmid 1632-39, Kt. 112-115',
    '1229': 'Schmid, Greiffenklau, Czernin and Ferdinand III 1642-48, Kt. 116-120',
}
items = {}
for i, x in V.items():
    i = int(i)
    v, note = x['verdict'], ''
    if i in OVR:
        v, note = OVR[i]
    items[i] = dict(x, verdict=v, note=note)

STATUS = {'filed': 'decipherment_filed', 'probable': 'decipherment_filed', 'partial': 'partly_filed',
          'parallel': 'partly_filed', 'none': 'open'}
findings = {}
for g, label in GROUPS.items():
    its = sorted([(i, x) for i, x in items.items() if x['group'] == g])
    c = Counter(x['verdict'] for _, x in its)
    open_ids = [i for i, x in its if x['verdict'] == 'none']
    par_ids = [i for i, x in its if x['verdict'] in ('parallel', 'partial')]
    findings[g] = {
        'status': 'partly_filed' if (c['filed'] + c['probable'] + c['partial'] + c['parallel']) else 'open',
        'evidence': (f"{label}: {len(its)} 'no decipherment' cipher regests checked (every 'sifrír*' hit in these Kartons whose "
                     f"regest says feloldás nélkül / nincs feloldva / csak sifrír / sifrírban maradt). Same letter deciphered, "
                     f"copied or extracted elsewhere in the Konvolut or the series: {c['filed']} (regest pointer or same sender, "
                     f"same day, same recipient); probably the same letter: {c['probable']} (no recipient named, a same-day "
                     f"decipherment of the same sender exists); a same-day parallel letter of the same sender to another "
                     f"recipient deciphered, or part of the decipherment filed: {c['parallel'] + c['partial']}; nothing found: "
                     f"{c['none']}. Per-item verdicts and the regest numbers behind them are under 'items'."),
        'leftover': (f"{len(open_ids)} items with no decipherment, clear copy or extract found: {', '.join(map(str, open_ids))}"
                     + (f"; {len(par_ids)} more have only a parallel or partial clear text (a crib): {', '.join(map(str, par_ids))}"
                        if par_ids else '')),
        'items': {str(i): {'status': STATUS[x['verdict']] + ('' if x['verdict'] not in ('probable', 'parallel', 'partial')
                                                            else f" ({x['verdict']})"),
                           'regest': f"BecsSeg {i}: {x['ref']} | {x['date']} | {x['desc'][:200]}",
                           'evidence': '; '.join(([x['note']] if x['note'] else []) + x['evidence'][:4]) or 'no same-day decipherment, clear copy or extract found in the Konvolut or by date search',
                           **({'leftover': LEFT[i]} if i in LEFT else {})}
                  for i, x in its},
    }
json.dump(findings, open(os.path.join(HERE, 'raw', 'multi_findings.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
for g in GROUPS:
    print(g, Counter(x['verdict'] for x in items.values() if x['group'] == g))

# Merge with the hand-written single-letter verdicts (singles.json) into findings.json.
REC = {
    '1226': 'narrow: to the items listed under leftover (Starzer\'s reports to the emperor of Jan-Aug 1611 and Feb-Jul 1613 without '
            'any same-day clear text, his 1612-19 letters to Mollart and Katzensteiner with none found, the Gratiani letter of '
            '21 Oct 1613 and the loose sheets); drop the items marked decipherment_filed. The deciphered same-day pieces are key material.',
    '1227': 'narrow: to the items listed under leftover (mostly Lustrier 1623-27, Radibrati 1621, Kurtz 1623-24); drop the five '
            'whose decipherment is filed and the two probable ones.',
    '1228': 'narrow: to the items listed under leftover (Schmid 1630-39); drop the items marked decipherment_filed.',
    '1229': 'narrow: to the items listed under leftover (Schmid 1642-43, the Torstenson cipher letters of 1643, Greiffenklau 1644-46, '
            'Czernin and Ferdinand III 1644 and 1648); drop the Greiffenklau 1644-47 items whose regests point to their decipherment or extract.',
}
S = json.load(open(os.path.join(HERE, 'singles.json'), encoding='utf8'))
for g in GROUPS:
    findings[g]['recommendation'] = REC[g]
allf = {'_about': 'Habsburg Constantinople (HHStA Türkei I) and other Hungaricana-regest catalogue entries, audited 16 Nov 2026 for '
                  'a decipherment, clear copy or extract of the same letter filed elsewhere. See README.md. Catalogue entries '
                  '1226-1229 are the promoted leads 1226-1229 (no longer in research/leads.json).'}
for k in ['2237', '343', '342', '501', '2675', '2676', '885', '1226', '1227', '1228', '1229',
          '1230', '1231', '1232', '1234', '2455', '2457', '2458', '2459', '2460']:
    allf[k] = S[k] if k in S else findings[k]
json.dump(allf, open(os.path.join(HERE, 'findings.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('findings.json written:', len(allf) - 1, 'entries')
