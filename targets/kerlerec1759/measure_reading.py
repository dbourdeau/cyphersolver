"""Measure marked-word uncertainty, not source accuracy or cipher coverage."""
from pathlib import Path
import importlib.util,json
T=Path(__file__).resolve().parent
R=T.parents[1]
s=importlib.util.spec_from_file_location('v2',R/'research/reading_audit/v2_score.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
rows=[]
for n in (206,207,215):
    text=m.holes((T/f'reading_fr_{n}.txt').read_text())
    cleaned=m.cr.CODE.sub(' CODEWORD ',m.cr.clean_text(text))
    words=[(w,g) for sent in m.cr.sentences(cleaned) for tok in sent for w,g in m.cr.words_of(tok)]
    holes=sum(bool(g) for w,g in words)
    rows.append(dict(document=str(n),words=len(words),holes=holes,unmarked=len(words)-holes,share=(len(words)-holes)/len(words)))
print(json.dumps(rows,indent=2))
