# Rebuilds the mechanical decryption from the transcription + key and checks that the reading departs from it only
# inside {mechanical/clear} marks. usage: python scripts/check_marks.py
import sys,re; sys.path.insert(0,'scripts'); from common import *
T=load_trans('transcription_ind737_letter1.txt'); K=load_key('key_frozen.tsv'); bad=0; n=0
for ln in open('reading_ind737_letter1.md',encoding='utf-8'):
    m=re.match(r'^(\d\.\d\d): (.*)$',ln.rstrip('\n'))
    if not m: continue
    n+=1; mech=dec_line(T[m.group(1)],K).split()
    got=re.sub(r'\{([^/}]*)/[^}]*\}',r'\1',m.group(2)).split()
    if got!=mech: bad+=1; print('UNMARKED DEPARTURE',m.group(1)); print(' mech',mech); print(' read',got)
print('lines checked',n,'failures',bad); sys.exit(1 if bad else 0)
