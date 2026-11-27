"""Apply the master-checked corrections (errata.json verdict a, recheck_unanswered.jsonl, chains_missed.jsonl) to the
chain records. Originals are kept as chains_*.jsonl.orig; every change is logged to fixes_log.jsonl."""
import json, glob, shutil, os
R = [  # (chain, old, new) category-(a) readings, from errata.md (28 Nov 2026)
 ('2r.4','بالجزء','بالعجز'),('2r.4','ما للاستطاع','ما لا يستطاع'),('3r.7','لوعني','لوعتي'),('3r.7','لذة','لتذ'),
 ('6v.11','مصرا الا','مصر الا'),('7r.5','صفوا ويكدر','صفوا او يكدر'),('8r.11','يا ادم','ا ادم'),('8r.11','بمنعه','يمنعه'),
 ('19r.7','قمرا اذا','قمر اذا'),('19r.7','ومدد','ومد'),('19r.7','لرابع ','لرابعه '),
 ('22r.1','التناثر','التهاتر'),('22r.1','الجوادر','الخوادر'),('22r.1','انتقام','اتقا'),('22r.1','عارهو و','عاره و'),('22r.1','همو و','هم و'),
 ('22v.9','حذرا','حذر'),('22v.9','اثبتك عذرا','اثبتك اعتذر'),('25r.4','تطلب','نتطلب'),('30r.4','فقالت ان','فقالت اظن'),
 ('36r.11','احوم','احنو'),('37r.1','فقيل','فقبل'),('44v.9','ومسي','ومسيء'),('50v.1','رسايلكم الله','رسايلكم انس'),
 ('63v.1','ابري','ايري'),('63v.1','الاحور','لا يجوز'),('63v.1','الاحوز','لا يجوز'),('63v.1','بحور','يجوز'),('63v.1','وثلثه','فنكته'),
 ('63v.trees','ابري','ايري'),('63v.trees','الاحور','لا يجوز'),('63v.trees','الاحوز','لا يجوز'),('63v.trees','بحور','يجوز'),('63v.trees','وثلثه','فنكته'),
 ('67r.8','الشنا','الشتا'),('78v.13','فاسفكن','سفكن'),('85v.8','يعتز بها','يعتريها'),('86r.9','فقلت','قلت'),('86r.9','جرحي','جرحني'),
 ('94v.5','عبيدهم','عبيد لهم'),('103v.11','هونتا','هونت'),('103v.11','هونت[ا]','هونت'),
 ('20r.8','وخمد','يحمد'),('20r.8','توهمها','ترميها'),('20r.8','للراكبان','للراكب ان'),
]
log = open('fixes_log.jsonl', 'w', encoding='utf8')
files = sorted(f for f in glob.glob('chains_0*.jsonl'))
recs = {}
for f in files:
    if not os.path.exists(f + '.orig'): shutil.copy(f, f + '.orig')
    rows = [json.loads(l) for l in open(f + '.orig', encoding='utf8') if l.strip()]
    recs[f] = rows
byid = {r['chain_id']: (f, r) for f, rows in recs.items() for r in rows}
for c, old, new in R:
    if c not in byid: log.write(json.dumps({'chain': c, 'missing_chain': True}, ensure_ascii=False) + '\n'); continue
    r = byid[c][1]; t = r.get('plaintext', {}).get('text', '') or ''
    if old in t:
        r['plaintext']['text'] = t.replace(old, new, 1)
        r.setdefault('corrections', []).append({'old': old, 'new': new, 'source': 'errata.md verdict a (master, 28 Nov 2026)'})
        log.write(json.dumps({'chain': c, 'old': old, 'new': new, 'applied': True}, ensure_ascii=False) + '\n')
    else:
        log.write(json.dumps({'chain': c, 'old': old, 'new': new, 'applied': False, 'note': 'old reading not found in plaintext.text'}, ensure_ascii=False) + '\n')
# structural fixes from the recheck
def note(c, txt):
    r = byid[c][1]; r.setdefault('corrections', []).append({'note': txt, 'source': 'recheck_unanswered.jsonl / chains_missed.jsonl (28 Nov 2026)'})
for c in ('12v.8', '12v.11'):
    r = byid[c][1]; r['answered'] = 'no'; r['plaintext_candidate_withdrawn'] = r.get('plaintext'); r['plaintext'] = {'text': '', 'note': 'the 13r l.5-8 candidates answer 46v.11+13r.1'}
    note(c, 'candidate plaintext withdrawn: 13r l.5-8 answer 46v.11 + 13r.1')
rc = {json.loads(l).get('chain_id', json.loads(l).get('chain')): json.loads(l) for l in open('recheck_unanswered.jsonl', encoding='utf8') if l.strip()}
for c in ('46v.11', '48r.8'):
    if c in rc:
        r = byid[c][1]; r['recheck'] = rc[c].get('recheck', rc[c]); r['answered'] = 'yes'
        note(c, 'answered after recheck: see recheck field')
byid['46v.11'][1]['continues_as'] = '13r.1'
byid['48r.8'][1]['plaintext'] = {'text': 'see 20r.8: the first 50 words of the 21r l.7-21v l.1 rhymed prose (to جملته)', 'source': 'recheck + solve_48r/REPORT.md'}
byid['48r.8'][1]['heading'] = 'ورابعها'
for f, rows in recs.items():
    with open(f, 'w', encoding='utf8') as o:
        for r in rows: o.write(json.dumps(r, ensure_ascii=False) + '\n')
# merged file, with the missed records appended
allr = [r for f in files for r in recs[f]]
for l in open('chains_missed.jsonl', encoding='utf8'):
    if l.strip():
        m = json.loads(l)
        if m['chain_id'] == '13r.1': m['continues_from'] = '46v.11'
        allr.append(m)
json.dump(allr, open('chains_all.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print(len(allr), 'records')
