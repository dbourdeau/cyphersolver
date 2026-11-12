# One-off builder for contract/WORDS.tsv from b55 R2_marks.tsv (R2 word order) + this folder's adjudications.
# Columns: line widx r2word consword accepted r2align note
#  consword: consensus tokens as seen (labels; υ = rounded n-form, Z = hapax Z-form, ? = illegible/blotted), '-' if no consensus word
#  accepted: adjudicated plaintext, one char per consensus token; {x} = letter the writer omitted, inserted by emendation (no sign); <x> = sign lost at torn edge, restored (no unit); '?' = no accepted value;
#            for code/abbrev tokens the whole token value.
#  r2align: '=' identity, else comma list of consensus token index per R2 token ('-' = R2 token has no consensus counterpart)
import csv,sys
M='/home/claude/en/trackB/b55_augustoni_cpp/work/R2_marks.tsv'
rows=[l.rstrip('\n').split('\t') for l in open(M) if not l.startswith('#')]
ACC={'cose':'cose','rochetta':'rochetta','rimetendolo':'rimetendolo','prevost[o]':'prevost<o>','rissolse':'rissolse',
 'cosa':'cosa','cosi':'cosi','volessero':'volessero','altro':'altro','pentiti':'pentiti','ardire':'ardire','ne':'ne',
 'tenevano':'tenevano','sospesi':'sospesi','incantati':'incantati','dubitar':'dubitar','li':'li','punti':'punti','vera':'vera',
 'causa':'causa','dubitiamo':'dubitiamo','acordo':'acordo','reco':'reco','le':'le','sue':'sue','ragioni':'ragioni','feudi':'feudi',
 'se':'se','[s/v]e':'?e','ha':'ha','ministri':'ministri','instato':'instato','escludere':'escludere','compromesso':'compromesso',
 'istesso':'istesso','gran':'gran','canceliero':'canceliero','prevosto':'prevosto','quassi (=quasi)':'quassi','negotiato':'negotiato',
 'dubio':'dubio','ricercare':'ricercare','conscesso':'conscesso','[A.V.]':'av','avertita':'avertita','sentisse':'sentisse',
 'opporsi':'opporsi','??':None,'impertinenca':'impertinenca','voluto':'voluto','forca':'forca','far':'far','la':'la',
 'generale':'generale','potuto':'potuto','argutia?':'a??utia','una':'una','letera':'letera','prevos[to]':'prevos<to>','dove':'dove',
 'dice':'dice','[ag]gionta':'aggionta','significare':'significare','tottal':'tottal','esclusione':'esclusione','parole':'parole',
 'ultime':'ultime','hone[s]tare':'hone{s}tare','non':'non','habb[i]no':'habb{i}no','tal':'tal','pensiero':'pensiero',
 'scritura':'scritura','privata':'privata','pena':'pena','minore':'minore','malenconico':'malenconico','visitare':'visitare',
 'informato':'informato','avertito':'avertito','vi':'vi','scoprite':'scoprite','bisogno':'bisogno','dubito':'dubito','dovero':'dovero',
 '[per]':'per','[per/poi]':'per?','[I.]':'I.','[PP.]':'PP.','[25.]':'25.','-':None}
CONS={('L06','po64ug4op'):'po64υg4gp',('L07','H4ugp'):'Hyυgp',('L09','f6c7tc'):'f6c7tc',('L10','p3'):'?3',
 ('L12','L74u'):'L74υ',('L12','64u63mp37c'):'64υ63mp37c',('L12','zq4Dmp'):'Zq4nnp',('L13','u3lcgp4gc'):'υ3lcgp4gc',
 ('L14','6con6D?xc'):'6con6D?nc',('L16','pfv37gpuDu64'):'pfv37gpυDυ64',('L18','yq74'):'gq74',('L19','47y?gp4'):'47g?gp4',
 ('L20','lpcog4'):'allpcog4',('L21','a3qtp'):'a3qtp',('L23','ocu'):'ocυ',('L24','a47'):'a47'}
ALIGN={('L20','lpcog4'):'2,3,4,5,6,7',('L26','fam7o6copp6c'):'0,1,2,3,4,5,6,7,8,-,9,10',('L22','l'):'-'}
NOTE={('L18','yq74'):'sign 1 = looped-descender g (t), as g in L17 qcmygc; R2/pass2 y, pass1 g',
      ('L20','lpcog4'):'image shows a-l-l: allpcog4 = AGGIONTA literal; R2 took a+l as clear',
      ('L16','ul4oc'):'unresolved; literal FGANO; candidate l\'[i]ngano not adopted',
      ('L17','n6y'):'unresolved; hyphenated with L18; literal SCU-',('L18','gq74'):'',
      ('L19','47y?gp4'):'argutia/astutia unresolved; literal ART?TIA',('L10','p3'):'gutter sign unreadable'}
out=open('/home/claude/en/trackB/b72_augustoni_repair/contract/WORDS.tsv','w')
out.write('line\twidx\tr2word\tconsword\taccepted\tr2align\tnote\n')
w={}
for r in rows:
    line,r2,cw,plain=r[0],r[1],r[2],r[3]
    i=w.get(line,0); w[line]=i+1
    cons=CONS.get((line,r2),cw)
    if r2=='l': cons='-'
    acc=ACC[plain]
    if acc is None: acc='?'*len(cons) if cons!='-' else '-'
    out.write('\t'.join([line,str(i),r2,cons,acc,ALIGN.get((line,r2),'='),NOTE.get((line,r2),r[5] if len(r)>5 else '')])+'\n')
out.close()
