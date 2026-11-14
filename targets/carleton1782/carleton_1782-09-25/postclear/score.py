from pathlib import Path
from collections import Counter,defaultdict
import csv,json
P=Path(__file__).resolve().parent;E=P.parent/'preclear'
rows=list(csv.DictReader((E/'predictions.tsv').open(),delimiter='\t'))
# Source alignment made only after independently checkpointed freeze.
unknown={1:'',8:'y',11:'make',14:'into',16:'Indian',17:'Country',22:'Major',26:'consist',28:'four',29:'hundred',30:'Continental',33:'six',34:'hundred',35:'Militia',37:'Volunteers',38:'are',42:'for',47:'West',52:'eighth',54:'October',57:'march',62:'open',65:'Creek',68:'',71:'into',74:'Country',84:'consist',88:'Men',94:'are',95:'Continental',98:'for',100:'Pit',101:'early',103:'October',105:'march',106:'towards',107:'lake',119:'Country',125:'several',133:'contributed',134:'much',138:'present',152:'Orders',154:'Major',158:'Commands',162:'you',165:'Assistance',166:'You',167:'may',172:'Continentals',175:'Washington',176:'are',185:'here',189:'most',195:'g',198:'September'}
special={5:'Pensyl',6:'vania',7:'assembly',13:'incursions',45:'near',50:'Susquehannah',66:'',67:'',87:'thousand',93:'Whom',111:'Object',112:'is',129:'escaped',132:'have',142:'is',164:'any',168:'require',179:'Ver',180:'plan',181:'ks',192:'',194:'repairing'}
notes={1:'Duplicate heading absent from clear body; excluded from prediction scoring.',5:'Editorial split of Pensylvania at cipher group boundary; not an independent whole-word prediction.',6:'Second segment of Pensylvania.',7:'Frozen group lacks final y; following17-17 was misclassified W rather than spelling continuation.',8:'After-clear boundary correction:17-17 spells y on fixed key; not a newly inferred word code.',13:'Frozen literal incuosions; intended incursions. Image/source discrepancy retained.',42:'Word code plus clear t forms fort; inferred underlying for, not proven printed headword.',45:'Frozen qualified in/on does not cover clear near; likely original Clinton13-14 allocation not universal.',50:'Frozen literal susnuehannah; possible special q glyph, not repaired in score.',64:'Pines clear in second witness B.146 p.54; first witness letter form less certain.',65:'First Creek aligns clear; subsequent to Pines Creek is extra in both cipher layouts.',66:'Extra to Pines Creek in cipher; no separate clear counterpart.',67:'Extra to Pines Creek in cipher; no separate clear counterpart.',68:'Extra to Pines Creek in cipher; no separate clear counterpart.',87:'Frozen43-19 predicted hundred; clear thousand. Tight crop is compatible with43-19 in both copies; earlier40 hypothesis not established. Count failure; original manuscript needed to distinguish code/clear conflict from copying or digit error.',93:'Qualified who differs in case-form from clear Whom.',96:'Clear inserts will before assemble; not separately located in cipher.',98:'Word code plus clear t forms fort.',111:'i/j equivalence permitted for literal obiect.',129:'Main escapedo; duplicate appears escapedd. Neither silently normalized.',132:'Frozen unqualified has vs clear have; morphology mismatch.',164:'Frozen qualified an vs clear any; prior table had an/any caveat, but frozen prediction was only an.',168:'Frozen reuuire; third symbol may be special q. Strict failure retained.',179:'First cipher segment of Verplanks.',180:'Middle cipher segment of Verplanks.',181:'Last cipher segment of Verplanks; apostrophe ignored in letter comparison.',189:'Code plus clear ly forms mostly; underlying headword not proved.',192:'Archival Cypher Signed/Signal notation; not part of numerical message prediction.',194:'Frozen repairin lacks final g; following23-1 was misclassified W.',195:'After-clear boundary correction:23-1 spells g, not a new word-code value.',198:'Calendar month; date supported by clear heading/docket.'}
norm=lambda s:''.join(c for c in s.lower() if c.isalpha()).replace('j','i')
out=[]
for r in rows:
 i=int(r['order']);pred=r['mechanical_prediction'];clear=unknown.get(i,special.get(i,pred.split(' / ')[0]))
 if i in special:clear=special[i]
 if r['kind']=='C':status='already_clear_or_notation'
 elif r['basis']=='uncovered word code':status='uncovered_before_clear'
 elif not clear:status='no_clear_counterpart'
 elif r['basis']=='Clinton qualified':status='qualified_set_agrees' if norm(clear) in [norm(x) for x in pred.split(' / ')] else 'qualified_mismatch'
 else:status='exact_ij_equivalent' if norm(clear)==norm(pred) else 'literal_or_lexical_mismatch'
 out.append(dict(r,clear_alignment=clear,status=status,alignment_note=notes.get(i,'')))
with (P/'comparison.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=out[0].keys(),delimiter='\t');w.writeheader();w.writerows(out)
classes={}
for basis in dict.fromkeys(r['basis'] for r in out):classes[basis]=dict(Counter(r['status'] for r in out if r['basis']==basis))
summary={'total_frozen_units':200,'classes':classes,'spelling_comparison':'43 frozen S groups, including split names; not 43 independent words. i/j, capitalization, spaces and apostrophes normalized. Other letters not repaired.','qualified_comparison':'Agreement means the clear form belongs to the frozen proposed set; it is not an unambiguous prediction.','preclear_proposals':'Evaluated separately in PROPOSALS_REVIEW.md; excluded from mechanical tally.','new_clear_associations':'Uncovered units are not counted as predictions. Misgrouped letter tokens and extra cipher phrases excluded from recovered word-code headwords.'}
(P/'SCORE.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
# New values remain post-clear evidence only.
d=defaultdict(list)
for r in out:
 if r['basis']=='uncovered word code' and int(r['order']) not in {1,8,68,195}:d[r['tokens']].append(r)
with (P/'new_associations.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['tokens','local_readings','orders','limit'],delimiter='\t');w.writeheader()
 for t,rr in sorted(d.items(),key=lambda x:tuple(map(int,x[0].split('-')))):
  w.writerow({'tokens':t,'local_readings':' / '.join(sorted({r['clear_alignment'] for r in rr})),'orders':' '.join(r['order'] for r in rr),'limit':'Post-clear association only; not tested prediction or identified printed headword. '+('Suffix construction requires qualification.' if t in {'6-6','23-12'} else '')})
