"""Wave 12: lead 2873 (Adrian VI 1522-23) has no letter left once CSP Spain vol. 2 is matched by date and sender instead of folio.
Moves the entry from catalogue.json back to research/leads.json (as the 15 Nov audit did), verdict 'read', with a closed note."""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
cp, lp = os.path.join(ROOT, 'catalogue.json'), os.path.join(ROOT, 'research', 'leads.json')
raw = open(cp, encoding='utf8').read(); C = json.loads(raw); CL = C if isinstance(C, list) else C['entries']
e = next(x for x in CL if x['id'] == 2873)
note = ("decipherment_filed (wave 12 date match, 15 Nov 2026): the two letters left after wave 11 are both printed by Bergenroth in CSP Spain vol. 2, which the "
        "index folios had missed because the folios differ: Adrian VI to Charles V, Rome 30 Sep 1522 (CSP no. 478, Salazar A.26 f.53; index f.58) and Rome 2 Mar 1523 "
        "(CSP no. 532, Salazar A.27 f.174, 'Autograph in cipher ... Deciphered by the Secretary Quintana'; index f.172). Same sender, same date: a calendar entry means the "
        "editor read the letter, and the 2 Mar letter has a contemporary decipherment filed. Nothing open to solve in this lead. The folio offsets (5 and 2) are not explained; "
        "the volumes were not seen.")
e['vetting']['verdict'] = 'read'; e['vetting']['closed'] = note
CL.remove(e)
open(cp, 'w', encoding='utf8').write(json.dumps(C, ensure_ascii=False, indent=1))
LL = json.load(open(lp, encoding='utf8')); LS = LL if isinstance(LL, list) else LL['leads']
LS.append(e); LS.sort(key=lambda x: x['id'])
open(lp, 'w', encoding='utf8').write(json.dumps(LL, ensure_ascii=False, indent=1))
print('moved 2873')
