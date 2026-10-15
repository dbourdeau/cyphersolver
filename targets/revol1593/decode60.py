"""Decoder for the Court symbol cipher no. 60 (BnF fr. 3995 ff. 109-111), used by Henri IV, Revol and the duc de
Nevers, Aug 1593 - May 1594.  Input: a ct_*.txt transcription in the glyph tags of key60.txt (space-separated,
'|' ignored, [clear: ...] passed through).  Output: token-by-token decode with '?' for unknown tags.

The table below is the deciphering table of ff. 110v-111 plus the cursive values confirmed from the interlined
crib (fr. 3986 f. 151).
Corrected 12 Oct 2026 from issue #32 (tunarob), checked on the images: see the issue #32 block in
key60.txt. Old ASCII tag o- still decodes tu; b is o– (en dash). Tags: 4 = x, ſ+ = l, 4+ = i, 4+b = bien,
2+ = u|i (sheet u; table "u, J"), n+ = p, ‡ = d, ‡o = u, ++ = i (sheet), ⱶⱶ = u (copyist form, atlas60.md).  Tags are ASCII/Unicode stand-ins; see key60.txt for what each denotes.
"""
import re, sys

KEY = {
    # alphabet (enciphering sheet, homophones) -- cursive values in the letters
    '∂':'a','o':'a','x':'a','·q':'a','o\'':'a',
    'o–':'b','∞':'b','oo':'b','14':'b','n~':'b','∩':'b',
    '//':'c','∠':'c','c~':'c','o–o':'c',
    '=':'d','‡':'d','.x.':'d','·x':'d','uij':'d',
    'f':'e','ue':'e','ur':'e','x:':'e','x.':'e','9':'e',
    'g':'de','8':'t','>':'f','L':'f',
    'a+':'g','H#':'g','h+':'g','c+':'g','5+':'g','g+':'gu','q++':'g','∩+':'g','V+':'g','8o\'':'g',
    'ξ':'h','z8':'h','uu+':'h',
    '4+':'i','4+b':'bien','to':'i','++':'i','ⱶⱶ':'u','♀':'u','u+':'aussi','d+':'i','2+':'u|i','n+':'p',
    'ſ+':'l','ꝗ':'l','cH':'l','t':'ru','p~':'l',
    't\'':'m','ʃ':'m','ß':'n','ɱ':'m','m':'m','ſ':'m','A':'m',
    'fs':'n','T':'n','⊥':'n','s':'n','TL':'n','1':'n',
    'π':'o','Δ|':'o','ᛉ':'o','Δ':'o','X':'o','\\\\':'o',
    'g3':'p','v+':'p','10':'p','7':'p',
    '9+':'q','A-':'q','8+':'tous',
    'oe':'r','v':'li','///':'r','X~':'r','d\'':'r','do':'r','ꝺo':'r','ꝺ':'r',
    'y':'s','6':'di','r':'s','b':'s','c':'s',
    '2z':'t','ꝛ':'luy','ɤ':'t','La':'t','.xx.':'t','xx':'t',
    'v\'':'u','‡o':'u','ll':'bon','20':'u','4':'x','sqrt':'u',
    '17':'x','29':'x','30':'x',
    'c‡':'y','2‡':'y','oto':'y','L++':'y','2++':'y','C':'y',
    'q-':'z','±':'z','F-':'z','y~':'z','3':'ri',
    # syllabary / figures
    'ai':'bi','d':'be','η':'bo',':.':'na','φ':'ca','18':'ce','t3':'ci','∝':'co','l':'cu','p':'da','de':'de',
    '12':'du','91':'fa','16':'fe','Lo':'fi','o-\'\'':'fo','w':'fu','λ':'la','+o':'le','–o–':'tu','o-':'tu','–o':'fo','V':'lo','q\'':'lu',
    'rp':'ma','ro':'me','.|.':'mi','aj':'mo','ct':'mu','x~':'ne','50':'ni','52':'no','53':'nu','54':'pa','42':'pe',
    'q~':'pi','tt':'po','13':'pu','pr':'qua','pi':'que','L40':'qui','.:':'ra','E':'re','m~':'ro','ae':'armee',
    '2':'sa','X+':'se','X++':'si','Q':'so','ꝑ':'so','C~':'su','Δ\'\'\'':'ta','q':'te','e':'to','o-\'':'ua',
    'w\'':'vu','3~':'vi','ci':'mu','h3':'ceulx','com':'plus','cy':'ilz','ss':'qu\'ilz',
    # word signs
    'n':'et','+':'nostre','|-':'nous','+7':'vous','θ7':'fait','Q\'':'est','f++':'qu\'il','p\'':'fault','s\'':'en',
    'theta':'des','-|-':'paix','|--':'guerre','_|_':'combat','.:.':'Je','+8':'sans','8o':'raison','d8':'tant',
    '~~':'deux','5':'comme','45':'tout','60':'affaires','67':'affin','92':'chacun','94':'dont','96':'chose',
    '97':'catolique','99':'davantage','lh':'beaucoup','cc':'car','car':'tousiours','est':'rien','cS':'leurs',
    'Se':'mais','Le':'audiance','Jl':'gouvernement','OO':'assistance','nre':'grand','per':'moy','po':'pour','ꝑ3':'pour',
    'p3':'pour','G~':'quelque','tt\'':'aultre','n\'':'ville','+++':'moins','w+':'Les','+w':'aux','+w\'':'les',
    '4++':'asseurance','p-o':'Iceux','p-o\'':'Icelluy','F':'Armes','ↄ':'neantmoins','V(inv)':'deffaute','V\'':'tresve',
    'Vre':'non','T\'':'autorite','δ':'rencontre','w\'\'':'avec','w\'\'\'':'aiant','8~':'Riviere','8~\'':'Religion',
    '8~~':'par','8~~~':'Province','k':'ont','&t':'f','G':'vitoire','8\'':'ainsi','++O':'d\'autant','q+':'village',
    # names and places
    'oo+':'le Roy','O++':'le Pape','3+':'le grand Seigneur','#\'':'l\'Empereur','8+\'':'Roy d\'Espaigne',
    '+C':'la Seigneurie de Venise','+phi':'le grand Duc de Toscane','R':'Duc de Mantoue','phi':'Duc de Ferrare',
    'alpha\'':'Duc de Savoye','oo b':'Duc de Lorraine','II':'Cardinal de Bourbon','X.':'Mr de Chomberg',
    'ooo':'Conte de Soissons','oo~':'Mr de Montpensier','8++':'Mr de Longueville','otto':'Conte de St Paul',
    '###':'Mr de Montmorency','O':'Cardinal Gondy','Psi+':'Mareschal de Retz','phi-o':'Mareschal d\'Aumont',
    '#~':'Mareschal de Bouillon','4+\'':'Mr d\'Espernon','X~~':'Mr de Schomberg','ʊ':'Alphonse d\'Ornano',
    'G\'':'Mr Desdiguieres','4+\'\'':'Marquis de Pisany','+oo':'Mr de Sancy','R\'':'Mr Gondy','++C':'Mr de Maisse',
    'obo':'Mr de Sillery','Δ+':'Mr de Fresne','A\'':'Mr de la Chastre','77':'Duc de Mayenne','E\'\'':'Duc de Guise',
    'L7':'Mr de Nemours','*':'Mr d\'Aumale','Q+':'Mr de Mercure','Q\'\'':'Mr d\'Elbeuf','H\'\'':'Mr de Rosne',
    'H':'St Pol','A:':'Mr de Belin','Φ':'Mr de Bellievre','Φ\'':'Mr de Villeroy','7~':'President Jeannin',
    'H\'':'Chevalier de Diou','S':'Mr Zamet','t5':'Bassompierre','P':'Monsieur','P\'':'Madame','m\'':'Royne d\'Angleterre',
    'M':'prelatz','J':'consistoire','Cg':'?Cg',
}
ROMAN = {'ij':'a','iij':'d','x':'d','xxij':'le Legat','xxiij':'Ambassadeur d\'Espagne','xxiiij':'Duc de Feria',
    'xxv':'Ambassadeur de Venise','xxvj':'princes protestans','xxvij':'estatz des Pays Bas','xxviij':'Conte de Nassau',
    'xxix':'Francois','xxx':'Italiens','xxxj':'Espagnolz','xxxij':'Reistres','xxxiij':'Lansquenetz','xxxiiij':'Anglois',
    'xxxv':'Wallons','xxxvj':'Neapolitains','xxxvij':'Suisses','xxxviij':'France','xxxix':'Espagne','xl':'Italie',
    'xlj':'la Suisse','xlij':'Angleterre','xliij':'la Savoye','xliiij':'l\'Allemagne','xlv':'le Piemont','xlvj':'le Milanois',
    'xlvij':'la Lorraine','xlviij':'Cardinaux','xlix':'Evesques','lxj':'Lion','lxij':'Tours','lxiij':'St Denys','lxiiij':'Mante',
    'lxv':'Chartres','lxvj':'Bordeaux','lxvij':'Blois','lxviij':'Melun','lxix':'Corbeil','lxx':'Vernon','lxxj':'Senlis',
    'lxxij':'Compiegne','lxxiij':'Chaalons','lxxiiij':'Meaux','lxxv':'Pontoise','lxxvj':'Caen','lxxvij':'Dreux',
    'lxxviij':'Verneuil','lxxix':'Rome','lxxx':'Venise','iiijxx':'Florence','iiijxxj':'Mantoue','iiijxxij':'Marseille',
    'iiijxxiij':'Ferrare','iiijxxv':'Verone'}
NULLS = {'ſo','-oo','4‡','g#','***'}

def decode_line(line):
    out=[]
    for m in re.finditer(r'\[clear:[^\]]*\]|\S+', line):
        tok=m.group(0)
        if tok.startswith('[clear'): out.append(tok); continue
        if tok=='|': continue
        t=tok.rstrip('?')
        if t in NULLS: out.append('·'); continue
        if t in ROMAN: out.append('['+ROMAN[t]+']'); continue
        v=KEY.get(t)
        out.append((v if v else '?'+t) + ('?' if tok.endswith('?') else ''))
    return ' '.join(out)

if __name__=='__main__':
    for fn in sys.argv[1:]:
        for line in open(fn,encoding='utf-8'):
            if line.startswith('#') or not line.strip(): continue
            tag,_,body=line.partition(':')
            print(tag+':', decode_line(body))
