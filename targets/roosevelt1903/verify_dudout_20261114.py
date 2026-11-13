"""roosevelt1903: list of the 22 codebook groups with the NARA T1171 roll 1 image used and the entry read there
(14 Nov 2026, read by eye on the images; the images are not in the repository). Compares with key_excerpt.tsv."""
import sys
R=sys.argv[1] if len(sys.argv)>1 else '.'
URL='https://catalog.archives.gov/medialz/dc-metro/rg-059/2034503/T1171/T1171-01/T1171-01-%04d.jpg'
READ={'56169':(559,'What is the'),'41276':(410,'Object'),'18427':(181,'British government'),'47372':(471,'Request'),
'33900':(336,'I'),'52844':(526,'Do not think'),'25361':(250,'Desirable'),'52597':(523,'That the'),'53664':(534,'Trip'),
'38401':(382,'Should be made'),'10000':(97,'A'),'41798':(415,'One'),'34036':(337,'If they'),'53279':(530,'Touch'),
'28040':(277,'English'),'43758':(435,'Port'),'36556':(362,'It should'),'16440':(161,'Be'),'11698':(113,'After the'),
'53149':(529,'To'),'34553':(342,'In my'),'36885':(365,'Judgment')}
key={}
for l in open(R+'/key_excerpt.tsv'):
    f=l.rstrip('\n').split('\t')
    if f[0].isdigit(): key[f[0]]=f[1]
ok=0
for g,(img,txt) in READ.items():
    same=key.get(g,'').lower()==txt.lower(); ok+=same
    print(g,URL%img,repr(txt),'agrees' if same else 'DIFFERS: '+key.get(g,'-'))
print(ok,'of',len(READ),'entries agree')
