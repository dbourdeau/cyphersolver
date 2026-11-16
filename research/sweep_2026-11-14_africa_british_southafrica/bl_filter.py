import json,re,sys
AF=r'Africa|Gold Coast|Sierra Leone|Gambia|Lagos|Niger\b|Cape of Good Hope|Cape Colony|Cape Town|Natal|Zulu|Zanzibar|Kenya|Uganda|Nyasa|Rhodesia|Sudan|Khartoum|Egypt|Cairo|Alexandria|Morocco|Tangier|Tangiers|Mogador|Abyssinia|Ethiopia|Barbary|Algiers|Algier|Tunis|Tripoli|Congo|Ashanti|Transvaal|Boer|Basuto|Bechuana|Swazi|Somali|Mauritius|St Helena|Senegal|Angola|Mozambique|Livingstone|Stanley|Liberia|Dahomey|Cameroon|Madagascar|Zambezi|Mafeking|Ladysmith|Gordon|Elmina|Guinea|Goree|Timbuktu|Bornu|Fernando Po|Morocco|Fez|Marocco'
CW=r'cipher|cypher|decipher|decypher|code'
seen={}
for l in open('bl_hits.jsonl'):
    r=json.loads(l); seen.setdefault(r['shelfmark'],r)
print(len(seen),'unique BL records')
n=0
for sm,r in seen.items():
    t=r['text']
    hits=[]
    for m in re.finditer(r'(cipher|cypher|decipher|decypher)',t,re.I):
        w=t[max(0,m.start()-220):m.end()+220]
        if re.search(AF,w): hits.append(w.replace('\n',' '))
    if hits:
        n+=1; print('##',sm,'|',r['text'][:0]); [print('   ...',h) for h in hits[:3]]
print(n)
