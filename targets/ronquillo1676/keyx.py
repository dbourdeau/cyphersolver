import json
K=json.load(open('../balbases1677/key.json',encoding='utf8'))
# hernannunez1674 additions (same volume, image-checked)
K.update({'d':'que','N':'V.S.','N_':'V.S.','30':'p','6+':'o','4':'t','161':'resolucion','os':'para','a':'','>':'',
          '167':'suecia','13':'e','bof':'guerra','cuf':'inglaterra','187':'tiempo','149':'quanto','111':'comercio',
          'cin':'haviendo','cel':'hacer','on':'electo','69':'ru','32':'x'})
K.update({'Infinity'+v:'c'+v for v in 'aeiou'}); K['Infinity']='c'
# values fixed by em.py against the sixteen margins (5 Oct 2026; counts in em_run.txt)
K.update({'5':'a','17':'o','33':'u','xoy':'con','144':'ion','83':'or','M_':'V.S.','r':'y','C+':'ll'})
# code values read from the margin decipherments, 22 Oct 2026 (ronq re-read; NOTES 22 Oct block). Only groups not
# already in the key are added; where the margins disagree with an existing value (97, do, 59, 67, 51, 112, 120, 135,
# 163, 170, 11, bi) the key is left as it was and the readings follow the margin case by case.
_ronq={'ers':'jo','bes':'espera','fos':'ningun','for':'ningun','121':'congreso','dos':'munster','fis':'negocio',
 'fan':'oficio','bel':'favor','fa':'novedad','143':'porque','100':'algun','122':'conviene','123':'convenien',
 'bil':'forma','cil':'holande','cep':'junta','82':'ir','K':'j','I':'i','12':'c','34':'ex','es':'ja','X':'ju',
 '139':'plenipotencia','140':'particular','154':'reydefrancia','155':'reydeinglaterra','116':'carta','in':'españa',
 'or':'dinamarca','be':'estado','er':'dios','168':'sumagestad','141':'paraque','dal':'mucho','dol':'medio',
 'bo':'empeño','bu':'enemigo','bon':'fuerza','bin':'franceses','cu':'general','90':'ajuste','99':'armas',
 '104':'batalla','107':'beneficio','109':'bruselas','173':'suceso','182':'siempre','fes':'noticia','fol':'ocasion',
 'fel':'opinion','dun':'nuev','cun':'hech','con':'haber','126':'correo','175':'secret','400':'','470':'','760':''}
K.update({k:v for k,v in _ronq.items() if k not in K})
# 14 Nov 2026 (verification): three code values glossed in the margins of the sibling letters, not yet keyed:
# fin = ofrece (R975, R977, R981), al = despues (R980, R981 x2; balbases1677 R986 x2), 91 = asist- (R981 x2).
K.update({k:v for k,v in {'fin':'ofrece','al':'despues','91':'asist'}.items() if k not in K})
