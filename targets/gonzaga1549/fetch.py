import json,subprocess,sys,os
sets={'n1114':'bf3cf88e-72bf-4608-8e75-a0390e17284b','n1120':'2c329985-47ac-4687-8356-ee2a90f24b0f',
'n0930':'656346d0-d012-4621-9973-fca518e5126e','n1542':'c710a32c-42a7-4159-8abc-472aed58f7c9',
'k0513':'0dbb01cc-7d7a-4aac-b3a8-0b6713c56416','k1223':'d824fd53-2d20-4daf-b854-7b654a8d0248',
'k0701':'006d60a7-5e7e-4c4b-bbbc-68760577ce88','k0715':'9b292209-d8f4-4d64-b714-dd50af780c54'}
os.makedirs('img',exist_ok=True)
for k,i in sets.items():
    m=json.load(open(f'man/{i}.json',encoding='utf8'))
    for c in m['sequences'][0]['canvases']:
        lab=c['label'].split(' - ')[-1]; p=f'img/{k}_{lab}.jpg'
        if os.path.exists(p): continue
        subprocess.run(['curl','-sL','-m','90','-o',p,c['images'][0]['resource']['@id']+'/full/1200,/0/default.jpg'])
    print(k,'done')
