"""Batch duplicate check: for each term print hit count and the set of files (not snippets)."""
import sys,re,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','archive_sweep_2026-10'))
import known
corpus=list(known.texts())
for term in sys.argv[1:]:
    rx=re.compile(re.escape(term),re.I)
    files={}
    for p,t in corpus:
        n=len(rx.findall(t))
        if n: files[p]=n
    top=sorted(files.items(),key=lambda x:-x[1])[:4]
    print(f'{term!r}: {sum(files.values())} hits in {len(files)} files', [f"{os.path.basename(os.path.dirname(p)) or p}/{os.path.basename(p)}" for p,_ in top])
