"""Venetian-diplomatic Italian character model for this target, now registered in lang/ as model 'it-venezia'
(sources it-renaissance + it-nunziature + it-relazioni twice, i.e. Alberi's Relazioni degli ambasciatori veneti at
double weight; lang/sources.json, lang/models.json). This script builds or rebuilds that model and writes the
word-frequency table dec.py uses for its (unused by default) lexicon bonus, corpus/venwords.json.

Until 9 Oct 2026 this script built its own copy into corpus/venlm.o5.sp (same corpus, same 47,007,119 characters;
1.3% of 5-gram cells differ, rare ones, since the registry joins the files in another order and with other
separators).dec.py now loads 'it-venezia';
LOCAL_VENLM=1 makes it load the old local table, which the 9 Oct calibration figures in NOTES were made with.
The Relazioni texts are found in targets/ottobon/corpus/ (git-ignored) or fetched from the Internet Archive.
Usage: python -I build_venlm.py [--rebuild]"""
import os, sys, json, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm, corpora
m = lm.load('it-venezia', order=5, spaces=True, rebuild='--rebuild' in sys.argv)
print('it-venezia', m.meta.get('chars'), 'chars')
spec = lm.registry()[0]['it-venezia']
text = lm.norm(corpora.text(spec['sources']), spec['norm'], True)
w = collections.Counter(text.split())
os.makedirs(os.path.join(HERE, 'corpus'), exist_ok=True)
json.dump({k: v for k, v in w.items() if v >= 2}, open(os.path.join(HERE, 'corpus', 'venwords.json'), 'w'))
print('words', sum(w.values()), 'types', len(w))
