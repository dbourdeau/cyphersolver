import json,sys
p=json.load(open('profile.json',encoding='utf8'))
p['solution'].append({"date":sys.argv[1],"kind":sys.argv[2],"what":sys.argv[3],"result":sys.argv[4]})
json.dump(p,open('profile.json','w',encoding='utf8'),ensure_ascii=False,indent=2); print(len(p['solution']))
