# labels.py viewer.html -> pos<TAB>viewer_id<TAB>label  (from the ASF MAP filza viewer page)
import re,sys
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
for i,(vid,lab) in enumerate(re.findall(r'riproduzione/\?id=(\d+)"[^>]*>\s*([^<]+?)\s*<',t)):
    print(i+1,vid,lab,sep='\t')
