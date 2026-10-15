"""Apply every known key in keys/ (cryptiana images, transcribed here) to letters (a)-(d).
Letters that the key does not define are shown as [n]. Output -> apply_keys_out.txt"""
import re, os, json, math
HERE = os.path.dirname(os.path.abspath(__file__))

def blocks(spec):
    k = {}
    for s, e, l in spec:
        for n in range(s, e + 1): k[n] = l
    return k
def run(start, letters, step=1):
    return {start + i * step: l for i, l in enumerate(letters)}

KEYS = {}
# marshall.jpg  Blank Marshall 1656-58
KEYS["marshall.jpg (Marshall 1656-58)"] = blocks([(1,5,'a'),(6,9,'b'),(10,13,'c'),(14,17,'d'),(18,22,'e'),(23,26,'f'),
    (27,30,'g'),(31,34,'h'),(35,39,'i'),(40,43,'k'),(44,47,'l'),(48,51,'m'),(52,55,'n'),(56,60,'o'),(61,64,'p'),(65,68,'q'),
    (69,72,'r'),(73,76,'s'),(77,80,'t'),(81,85,'u'),(86,89,'w'),(90,93,'x'),(94,97,'y'),(98,99,'z')])
# hague.jpg / blake.jpg  agent in the Hague 1653-58 = General Blake 1655 : three alphabets 20-43, 50-73, 78-101 (a..z, 24 letters)
h = run(20, "abcdefghiklmnopqrstuwxyz"); h.update(run(50, "abcdefghiklmnopqrstuwxyz")); h.update(run(78, "abcdefghiklmnopqrstuwxyz"))
KEYS["hague.jpg+blake.jpg (Hague agent/Blake 1653-58)"] = h
# charlesii2a.jpg  Barwick / Charles II / Hyde 1659-60 letters
b = blocks([(1,3,'a'),(4,6,'b'),(7,9,'c'),(10,12,'d'),(13,15,'e'),(16,18,'f'),(19,21,'g'),(22,24,'h'),(25,27,'i'),(28,29,'k'),
    (30,32,'l'),(33,33,'m'),(34,36,'n'),(37,39,'o'),(40,42,'p'),(43,45,'q'),(46,48,'r'),(49,51,'s'),(52,54,'t'),(55,57,'u'),
    (58,59,'w'),(62,62,'y'),(63,63,'z')])
# charlesii2.jpg / 2b / 2c  same key, syllables & words
b.update({70:'ab',71:'ad',72:'ac',73:'by',74:'ba',75:'be',76:'ca',77:'ce',78:'ci',79:'de',80:'do?',81:'di',97:'ka',98:'ke',
    132:'af',133:'ar',134:'ap',135:'bi',136:'bo',137:'bo',138:'bu',139:'co',140:'cu',141:'cr',142:'du',143:'dis',
    160:'ki',161:'ko',194:'all',195:'as',196:'at',197:'bl',198:'br',199:'but',200:'ch',201:'cl',202:'ct',203:'dis',204:'den',
    205:'Dr.',221:'kn',255:'and',257:'are',259:'both',261:'can',263:'com',264:'did',265:'doth',266:'done',
    318:'an',319:'act',320:'age',321:'best',322:'better',323:'beleeve',380:'arm',382:'assist',383:'between',385:'business',
    386:'cause',407:'king',408:'king',441:'any',442:'able',447:'count',449:'chief',468:'king',469:'king',507:'bishop',
    512:'concern',531:'kingdom',568:'army',569:'army',572:'Barwick',573:'councel',594:'coll.Knight',635:'H.Cromwell',636:'Clobery'})
KEYS["charlesii2*.jpg (Barwick-Hyde 1659-60)"] = b
# stamford.jpg  William Stamford 1655 (reversed alphabets; several cells uncertain in the image)
s = {2:'m',3:'l',5:'k',6:'i',7:'h',10:'g',11:'f',12:'e',13:'d',17:'c',18:'b',19:'a',
     21:'k',22:'g',23:'h',24:'e',25:'f',26:'c',27:'i',28:'d',29:'a',
     31:'x',32:'y',33:'w',34:'u',35:'t',36:'s',37:'r',38:'q',39:'p',40:'o',41:'n',42:'n',43:'m',44:'r',45:'t',46:'s',47:'i'}
KEYS["stamford.jpg (Stamford 1655)"] = s
# butler.jpg  John Butler 1656 (scattered numbers; 400-425 = plain alphabet)
bt = {2:'o',3:'e',5:'e',6:'t',7:'f',10:'g',13:'w',14:'q',16:'u',18:'i',19:'u',24:'n',26:'p',31:'t',36:'a',39:'k',40:'m',
      43:'d',44:'l',48:'r',49:'s',50:'l',60:'h'}
bt.update(run(400, "abcdefghiklmnopqrstuvwxyz"))
KEYS["butler.jpg (Butler 1656)"] = bt
# charlesII1.jpg  "intercepted letter of king Charles II" 1655 (upper case = Tomokiyo's conjectures)
c1 = run(20, "aAABBcCCdDeeeFFFgGGhHiIIKKllMM") ; c1.update(run(50, "MnNNoOOPPPQQrrRsstTTuUUwwWXXy"))
c1.update({113:'bu',114:'by',167:'ey',288:'of',239:'the'})
KEYS["charlesII1.jpg (Charles II intercepted 1655)"] = {k: v.lower() for k, v in c1.items()}
# kingston1.jpg  Kingston 1658
kg = run(1, "esabcdefghiklmnopqrstuwxysaeiouy"); kg.update({33:'c',34:'g',37:'r',38:'p',39:'l'})
KEYS["kingston1.jpg (Kingston 1658)"] = kg
# Westrope 1655 (from cryptiana thurloe.htm text, used by previous agent) : 3 per letter from 20
KEYS["Westrope 1655 (text)"] = blocks([(20 + 3*i, 22 + 3*i, l) for i, l in enumerate("abcdefghiklmnopqrstuwxy")])

def load(name):
    t = open(os.path.join(HERE, name), encoding="utf-8").read()
    return t
def groups_a():
    t = load("a_beverning_1653.txt")
    segs = re.findall(r"--- CIPHER passage \d ---\n(.*?)\n--- clear", t, re.S)
    return [re.findall(r"\d+", s) for s in segs]
def groups_b():
    return [["18","15","4","20","87","q","t","20","y","1"], ["12","m","17","24","15","8","15","17","f","20","18","15","9","7","6","13","20"]]
def groups_c():
    return [["2","3","1","4","7","4","6","4","9","7","2","3"], ["0","9","3","7"]]
def groups_d():
    t = load(os.path.join("..", "waddall1656", "d_waddall_1656.txt"))  # moved 14 Oct 2026
    seg = re.search(r"--- CIPHER \(inline\) ---\n(.*?)\n--- end", t, re.S).group(1)
    # keep clear words as tokens starting with '#'
    toks = re.findall(r"\d+|[A-Za-z][A-Za-z',]*", seg)
    return [toks]

# English LM for a crude readability score on (b),(d)
J = json.load(open(os.path.join(HERE, "..", "beale", "en_lm.json")))["quad"]; TOT = sum(J.values())
LM = {k: math.log10(v / TOT) for k, v in J.items()}; FLOOR = math.log10(0.01 / TOT)
def sc(txt):
    txt = re.sub("[^a-z]", "", txt.lower())
    return sum(LM.get(txt[i:i+4], FLOOR) for i in range(len(txt) - 3)) / max(1, len(txt) - 3)

LETTERS = {"(a) Beverning 1653": groups_a(), "(b) du Gard 1656": groups_b(), "(c) Brussels 12 Aug 1656": groups_c(),
           "(d) Waddall 1656": groups_d()}
out = []
for ln, segs in LETTERS.items():
    out.append(f"\n===== {ln} =====")
    for kn, key in KEYS.items():
        lines = []
        for seg in segs:
            parts = []
            for g in seg:
                if g.isdigit():
                    parts.append(key.get(int(g), f"[{g}]"))
                else:
                    parts.append(g if len(g) > 1 else g.upper())   # clear words / stray letters
            lines.append(" ".join(parts) if ln.startswith("(d)") else "".join(parts))
        txt = " | ".join(lines)
        cover = sum(1 for seg in segs for g in seg if g.isdigit() and int(g) in key)
        total = sum(1 for seg in segs for g in seg if g.isdigit())
        out.append(f"  {kn:40s} cover {cover:3d}/{total:3d} enq={sc(txt):6.2f} : {txt}")
res = "\n".join(out)
print(res)
open(os.path.join(HERE, "apply_keys_out.txt"), "w", encoding="utf-8").write(res)
