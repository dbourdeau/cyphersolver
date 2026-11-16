import am_search as a, json
for ty in ['File','Series','Fonds']:
  for t in ['jazz','cijfer*','geheimschrift']:
    d=a.q(t,ty,per=2); print(ty,t,d['total'])
    if d['rows'] and t=='cijfer*': print(json.dumps(d['rows'][0],ensure_ascii=False)[:900])
