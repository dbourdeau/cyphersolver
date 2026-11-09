"""Second-pass grep over the belgium_lux EAD files (read from the main checkout): wider terms, full own text of each component, minus earlier hits."""
import glob, json, re, sys, os
import xml.etree.ElementTree as ET
SRC = r'C:\Users\dbour\cypher\research\belgium_lux'
TERMS = re.compile(r"(gecodeerd\w*|gecodeer\w*|gecode\w*|\bcod[ée]e?s?\b|d[ée]cod\w*|\bin code\b|\ben code\b|geheim\w*\s+(?:brie|ber|corr|schrift|tekens|teken)\w*|"
  r"(?:lettres?|d[ée]p[êe]ches?|correspondance|billets?)\s+(?:secr[èe]t\w*|cryptées?|cod[ée]e?s?)|crypt\w*|cipher\w*|cyfr\w*|encode\w*|"
  r"sleutel\w*\s+(?:voor|van)\s+(?:het\s+)?(?:ont)?(?:cijfer|geheim|ontsleutel)\w*|ontsleutel\w*|clef\w*\s+(?:de|du|pour)\s+(?:la\s+)?(?:correspondance|chiffre|d[ée]chiffr)\w*|"
  r"caract[èe]res?\s+inconnus|signes\s+conventionnels|en\s+cifras?|cifrad\w*|zifferschrift|chiffrierte?\w*|verschl[üu]ssel\w*|schl[üu]ssel\s+(?:zu|f[üu]r)|"
  r"onleesbaar\w*\s+schrift|geheime\s+schrijf\w*|beschreven\s+in\s+cijfer|in\s+cijfer\w*|met\s+cijfer\w*|encre\s+sympath\w*|jargon|argot)", re.I)
NOISE = re.compile(r"code civil|codex|code pénal|code de|codes? (?:rural|forestier|g[ée]n)|burgerlijk wetboek|geheime politie|secrète? (?:de la )?(?:police|dossier)|crypte\b|cryptes\b|\bcode\b[^.]{0,20}\bde la route|cod[ée]s? (?:de |van )?(?:commerce|handel)|clefs? de voûte", re.I)
prev=json.load(open(os.path.join(SRC,'ead_hits.json'),encoding='utf8'))
seen={(h['ead'],h['unitid'],h['title'][:60]) for h in prev}
def text(el): return re.sub(r'\s+',' ',''.join(el.itertext())).strip() if el is not None else ''
def own_text(c):
    out=[]
    for k in c:
        if re.fullmatch(r'c(\d\d)?',k.tag): continue
        out.append(text(k))
    return ' '.join(out)
CT=re.compile(r'c(0\d|1[0-2])?')
hits=[]
def walk(c,chain,eadid,inv):
    did=c.find('did'); uid=text(did.find('unitid')) if did is not None else ''
    chain=chain+[uid] if uid else chain
    if did is not None:
        own=own_text(c)
        ms=[m.group(0) for m in TERMS.finditer(own)]
        if ms and not NOISE.search(own):
            key=(eadid,uid,text(did.find('unittitle'))[:60])
            hits.append({'ead':eadid,'inventory':inv,'unitid':uid,'chain':chain,'title':text(did.find('unittitle'))[:500],'date':text(did.find('unitdate')),
              'scope':text(c.find('scopecontent'))[:600],'terms':sorted(set(t.lower() for t in ms)),'old':key in seen})
    for k in c:
        if CT.fullmatch(k.tag): walk(k,chain,eadid,inv)
for p in sorted(glob.glob(os.path.join(SRC,'ead','*.xml'))):
    try: root=ET.parse(p).getroot()
    except ET.ParseError: continue
    eadid,inv=text(root.find('.//eadid')),text(root.find('.//titleproper'))
    for dsc in root.iter('dsc'):
        for k in dsc:
            if CT.fullmatch(k.tag): walk(k,[],eadid,inv)
new=[h for h in hits if not h['old']]
json.dump(new,open('grep2_hits.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print(len(hits),'total',len(new),'new')
