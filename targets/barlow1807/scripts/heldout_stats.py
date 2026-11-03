"""Word and sign counts from the marked readings, per page range. Pages 14-19 were never seen when key_final.txt was
frozen, so their counts are the held-out result.  usage: heldout_stats.py"""
import re
def stats(pages):
    c=dict(words=0,doubt=0,clean=0,drops_only=0,changed=0,signs=0,sg_drop=0,sg_change=0)
    for p in pages:
        for r in open(f'reading/r{p:02d}.txt',encoding='utf8').read().split():
            if re.fullmatch(r'\[\d{4}(,\d{4})*\]',r): continue
            c['words']+=1
            if r.startswith('[?'): c['doubt']+=1; continue
            ch=len(re.findall(r'\{[a-z?]+>[a-z]+\}',r)); dr=len(re.findall(r'\{[a-z?]+>\}',r))
            base=re.sub(r'\{([a-z?]*)>[a-z]*\}',r'\1',r); base=re.sub(r'\[[a-z]+\]','',base).replace('_','')
            c['signs']+=len(base); c['sg_drop']+=dr; c['sg_change']+=ch
            if ch: c['changed']+=1
            elif dr: c['drops_only']+=1
            else: c['clean']+=1
    return c
for name,pg in [('pages 1-13 (key trained here)',range(1,14)),('pages 14-19 (held out)',range(14,20))]:
    c=stats(pg); w=c['words']
    print(f"{name}: cipher words {w}; read clean {c['clean']} ({100*c['clean']/w:.1f}%), read with signs dropped only {c['drops_only']} ({100*c['drops_only']/w:.1f}%), read with a letter changed {c['changed']} ({100*c['changed']/w:.1f}%), doubtful {c['doubt']} ({100*c['doubt']/w:.1f}%)")
    print(f"   letters decoded in read words {c['signs']}: kept {c['signs']-c['sg_drop']-c['sg_change']} ({100*(c['signs']-c['sg_drop']-c['sg_change'])/c['signs']:.1f}%), dropped {c['sg_drop']}, changed {c['sg_change']} ({100*c['sg_change']/c['signs']:.1f}%)")
