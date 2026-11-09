import json,subprocess,os
sets={'a1546':'68f59b4c-c5e3-431f-9226-00927538c698','b1547':'9c67dac4-f213-4484-9e5e-fb5c1408ea76',
'c1548':'96578a9c-2963-4448-8786-5fa35a3c44e7','d1549':'fa08c81b-4cf3-4914-878e-98059ad124b8',
'e1551a':'3f4f51da-b3b0-4159-9824-f22958c248dd','f1551b':'9ad3b749-cbac-4adc-94cd-b080227c220f',
'g1553':'6990ecfe-8ee7-4994-b2d6-3ccc332ee9e2','h1563':'499ee545-fcd1-4afe-9776-a21cdbf0efb4'}
os.makedirs('img',exist_ok=True)
for k,i in sets.items():
    m=json.load(open(f'man/{i}.json',encoding='utf8'))
    for n,c in enumerate(m['sequences'][0]['canvases']):
        lab=c['label'].split(' - ')[-1].replace('BEU_A.C.felipe.ii.rey.de.espana.ii_','').replace('.tif','')
        p=f'img/{k}_{n:02d}_{lab}.jpg'
        if os.path.exists(p): continue
        subprocess.run(['curl','-sL','-m','90','-o',p,c['images'][0]['resource']['@id']+'/full/1200,/0/default.jpg'])
    print(k,'done')
