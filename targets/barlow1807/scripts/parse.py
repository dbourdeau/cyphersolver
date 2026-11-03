import re
def words(text):
    """split a transcription into items: ('C',[tokens]) cipher word or ('P',word) clear word"""
    text=re.sub(r'\{(?:over|struck|date):[^}]*\}|\[[^\]]*\]','',text)
    text=re.sub(r'^L\d+\s*','',text,flags=re.M)
    text=text.replace('=\n','').replace('-\n','')
    items=[]
    for m in re.finditer(r'(\d[\d?]*(?:\s*,\s*\d[\d?]*)*)|([A-Za-z]+)',text):
        if m.group(1):
            items.append(('C',[t.replace('?','') for t in re.split(r'\s*,\s*',m.group(1))]))
        else: items.append(('P',m.group(2).lower()))
    return items
