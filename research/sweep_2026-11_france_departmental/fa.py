import subprocess,re,sys,html,urllib.parse,os
JAR='fa.jar'
def get(u):
    h=subprocess.run(['curl','-s','-m','90','-L','-b',JAR,'-c',JAR,'-A','Mozilla/5.0',u],capture_output=True).stdout.decode('utf8','ignore')
    m=re.search(r"window.location.href='([^']+)'",h)
    if m and len(h)<700: h=subprocess.run(['curl','-s','-m','90','-L','-b',JAR,'-c',JAR,'-A','Mozilla/5.0','https://francearchives.gouv.fr'+m.group(1)],capture_output=True).stdout.decode('utf8','ignore')
    return h
def fa(q,page=1):
    u='https://francearchives.gouv.fr/fr/search?es_escategory=archives&items_per_page=50&q=%s&page=%d'%(urllib.parse.quote(q),page)
    h=get(u)
    cards=re.findall(r'<div class="fa-sr-card.*?(?=<div class="fa-sr-card|</main>)',h,re.S)
    out=[]
    for c in cards:
        t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',c))).strip()
        l=re.search(r'href="(/fr/facomponent/[^"]+)"',c)
        out.append((t[:350],'https://francearchives.gouv.fr'+l.group(1) if l else ''))
    m=re.search(r'(\d[\d\s]*)\s*résultat',html.unescape(h))
    return out,len(h),(m.group(0) if m else '')
if __name__=='__main__':
    for q in sys.argv[1:]:
        o,n,m=fa(q);print('##',q,len(o),n,m)
        for t,l in o[:12]: print(' ',t[:260],l)
