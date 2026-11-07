"""One-off INGEST of the work so far into the wiki (7 Nov 2026). Writes markdown pages with front matter plus the two lexicons.
After this, pages are edited by the engine or by hand; this script is kept as a record of the first ingest."""
import os,json,sys
sys.stdout.reconfigure(encoding="utf8")
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D="2026-11-07"
def page(rel,fm,body):
    path=os.path.join(ROOT,rel); os.makedirs(os.path.dirname(path),exist_ok=True)
    lines=["---"]
    for k,v in fm.items():
        if isinstance(v,list): lines.append("%s: [%s]"%(k,", ".join(v)))
        else: lines.append("%s: %s"%(k,v))
    lines+=["---","",body.strip(),""]
    open(path,"w",encoding="utf8").write("\n".join(lines))
def S(i,title,body,**kw): page("sources/%s.md"%i,dict(id=i,type="source",title=title,updated=D,**kw),body)
def E(i,title,body,**kw): page("entities/%s.md"%i,dict(id=i,type="entity",title=title,updated=D,**kw),body)
def Y(i,title,body,**kw): page("systems/%s.md"%i,dict(id=i,type="system",title=title,updated=D,**kw),body)
def C(i,title,status,conf,evidence,body,depends=None,refuted_by=None):
    fm=dict(id=i,type="claim",title=title,status=status,confidence=conf,evidence=evidence,depends=depends or [],updated=D)
    if refuted_by: fm["refuted_by"]=refuted_by
    page("claims/%s.md"%i,fm,body)
def Q(i,title,body,**kw): page("questions/%s.md"%i,dict(id=i,type="question",title=title,status="open",updated=D,**kw),body)
def T(i,title,body,**kw): page("tests/%s.md"%i,dict(id=i,type="test",title=title,updated=D,**kw),body)

# ------------------------------------------------------------------ SOURCES (raw material stays where it is; these pages are the wiki's summaries)
S("S01","Pillon collection (Pigeongrammes.zip)","""Alexandre Pillon's digitised pigeongrammes and telegrams (2.9 GB zip, shared via grosfichiers.com 7 Nov 2026, expires 21 Nov). Local copy: `C:/Users/dbour/pigeon_dl/` (outside the repo, third-party and unpublished: do not publish or send to DECODE without his agreement).
Holds LIST_Pigeongrammes.xlsx (66 rows), reconstructed directories R1/R2/R3, transcriptions of ~25 pieces, scans. Reliability: transcriptions about 98% accurate on the lines checked ([[T10]]); digit confusions 5/8/9 occur.""",kind="raw")
S("S02","Inspectors' telegram: scan and transcription","""'Steenackers a Mercadier, rue de Grenelle St Germain 103, Paris. 2me Serie n 1. Tours 2 Novembre (chiffre des inspecteurs)'. A pigeon dispatch: 736 four-digit coded groups (343 distinct) mixed with 437 clear words (names and addresses in clear). Scan sent by Pillon 7 Nov (image, not in repo); transcription = 2emeS-1_ADECHIFFRER.docx; plain copy `targets/pigeongrammes1870/inspecteurs_2nov_partial.txt`; all coded runs with context in `inspecteurs_runs.txt`.
The clear words are original (Pillon, [[S08]]). Key digit strings were checked against the scan ([[T10]]).""",kind="raw")
S("S03","Chaudordy letter: scan and transcription","""'N 36. Mr de Chaudordy a Bordeaux, 18 decembre 1870': two scan pages (MessageChiffre_Chaudordy1/2.jpg) and Pillon's sheet Texte_Chaudordy.xlsx (1,425 groups after our fixes, `chaudordy_nums.json`). Prussian handling marks: 'Aus Paris per Luftballon', initials 'C.o.n.P'. Heading is in clear and matches Favre's printed heading ([[C024]]).""",kind="raw")
S("S04","Favre, Le Gouvernement de la Defense nationale, vol. 2 (1871)","""archive.org `gouvernementdela02favr`, OCR in `C:/Users/dbour/enquete/`. 'Simple recit' pp. 259-272 prints Favre's letters to Chaudordy of 16, 17, 18 and 21 Dec 1870 and short quotes of Chaudordy's replies (20 and 29 Dec). The 18 Dec letter is the plaintext of [[S03]] up to the point where cipher and print diverge ([[C025]]).""",kind="book")
S("S05","Enquete parlementaire, Depeches telegraphiques officielles (1875)","""archive.org ids sc_0001326967_* and enquteparlemen02fran; prefect telegrams by departement, plus the Algeria report sc_0000928533_00000001739293 which prints Dec 1870 telegrams headed '(Chiffre des inspecteurs)' (plaintext only). Used as French/telegraph language material for the LM; does not contain the 2 Nov telegram.""",kind="book")
S("S06","Societe d'acclimatation, Bulletin 1872: 'La poste par pigeons voyageurs'","""archive.org `bulletindelasoci0209soci`, pp. 624-664. Names the Paris pigeon society L'Esperance (Cassiers, Van Rosebeke, Nobecourt, Traclet, Thomas), Steenackers at Tours, Rampont, Chassinat, Segalas, Dagron. No Mercadier, no Nantes or Rennes fancier.""",kind="book")
S("S07","Steenackers, Les telegraphes et les postes pendant la guerre de 1870-1871 (1883)","""Gallica ark:/12148/bpt6k220903s (Cloudflare check on page text) and HathiTrust hvd.hn6bui (in-book search works in Chrome). Searched for the circular's phrases and the Nantes/Rennes addresses: not found. See [[Q04]].""",kind="book")
S("S08","Pillon's statements (emails, 7 Nov 2026)","""Shared code confirmed for the Favre pages; clear words in the inspectors' telegram are original; 'beacons' 0101/0201/0301 mark syllables (first digit not to be over-read, R1 balises 0136/0137/0138); suggested the table is almost alphabetical; suggested 5926 = recevoir, 0603 = depeche, 2215 = capitale; withdrew a Mercadier decomposition; no plaintext exists for any 'A Jules Favre' page; does not know the Nantes/Rennes correspondents.""",kind="correspondence")
S("S09","Pillon's reconstructed directories R1, R2, R3","""Repertoire1.xlsx (1,050 entries 0131-5893, alphabetical word dictionary with balises), Repertoire2_ChiffreNouveau.xlsx (926 entries, disordered, homophones), Repertoire3 (stations/navy, 82). See [[Y03]], [[Y04]].""",kind="raw")

# ------------------------------------------------------------------ ENTITIES
E("E01","Steenackers (F.-F.)","Director general of telegraphs and posts at Tours; sender of the inspectors' telegram ([[S02]]). Author of the 1883 memoir ([[S07]]). Spelled in the cipher as S-TEEN-A-K-ER-S ([[C004]]).")
E("E02","Ernest Mercadier","Director of telegraphs at the siege of Paris; addressee, rue de Grenelle 103 (central telegraph post). Spelled MER-CA-DI-ER ([[C005]]).")
E("E03","General Trochu","Governor of Paris. Spelled T-RO-CHU in the telegram ([[C012]]).")
E("E04","Comte de Chaudordy","Diplomatic delegate at Tours/Bordeaux; addressee of Favre's 18 Dec 1870 letter ([[C024]]).")
E("E05","Jules Favre","Foreign minister in besieged Paris; writer of the Chaudordy letter; recipient of the 'A Jules Favre' pigeongrammes ([[Y02]]).")
E("E06","Alexandre Pillon","Collector who owns and transcribed the material ([[S01]]); corresponds with us ([[S08]]). Credit and sharing questions are open ([[Q07]]).")
E("E07","Societe colombophile L'Esperance","Paris pigeon society (Cassiers, Van Rosebeke, Nobecourt, Traclet, Thomas), see [[S06]]. Possible context for the pigeon fanciers named in the telegram ([[Q01]]).")

# ------------------------------------------------------------------ SYSTEMS
Y("Y01","Inspectors' code (chiffre des inspecteurs)","""Four-digit groups 0101..9924. An alphabetical lexicon of words and syllables over 0000-9999 ([[C001]]): the number predicts the initial letters of its entry (A ~0200, B ~0900, C ~1100, D ~2500, E ~3300, G ~4000, K ~4900, L ~5100, M ~5500, O ~6100, P ~6800, S ~8300, T ~9200). Beacons 0101/0201/0301/0102 bracket words spelled in syllable groups, mainly proper names ([[C002]]); clear words stay in clear. Known pieces: see `lexicon_inspectors.json`. Own table, not R1 ([[C020]]).""")
Y("Y02","Favre / delegation code (the 'unknown directory')","""Groups 1..~2300, shared by the 'A Jules Favre' pigeongrammes and the Chaudordy letter ([[C023]]). NOT alphabetical ([[C022]]); frequency-banded (1-100 carry 25% of tokens), several groups per common word (de = 25, 57, 81, 967 ...). Firm values in `lexicon_favre.json`. Date and topic profiles identify vocabulary ([[T05]]).""")
Y("Y03","R1 (prefects' code)","Alphabetical word dictionary 0131-5893 with grammatical balises (0104 adjective, 0107 end of paragraph, 0119 plural, 0122 feminine, 0128 future, 0136/0137 syllabic ...). Its numbering has no syllable entries, so its letter ranges do not calibrate the inspectors' table ([[C021]]). Source [[S09]].")
Y("Y04","R2 ('chiffre nouveau')","Disordered directory 1..~2300 with homophones, used for Gambetta-Favre traffic. NOT the code of the Chaudordy letter or the Favre pages ([[C023]]). Source [[S09]].")

# ------------------------------------------------------------------ TESTS
T("T01","Alphabetical-position test on 13 syllable values","`alpha_test.py`. Placed 13 assigned values in an alphabetical French word list (23k entries). Mean |position - value/9999| = 0.012-0.016; a random mapping gives ~0.33. Supports [[C001]]. Signed bias +0.015 used in later tests.")
T("T02","Benchmark loop (MRR on 10 supported items)","`bench_loop.py`. Position only MRR 0.190; +frequency prior 0.565; +bigram context 0.615; isotonic calibration, short-piece prior, name bonus rejected. Stopped after 3 rejections. See [[C021]], [[C031]].")
T("T03","Spelled-run solver validation","`spell_solver.py`. Correct strings rank in the top 0.5% of ~30k candidates (pigeons 8, Mercadier 30, ballon 145, Steenackers 6-8): shortlists but does not decode. Rejects 'Ernest' for 6819 3412 (error 0.17). Supports [[C002]], [[C005]], [[C006]].")
T("T04","Cross-letter check of the early Chaudordy codebook","`crossletter.py`. 63 single-word values; Chaudordy 73 vs 36 shuffled; other seven letters 42 vs ~35: no confirmation (too few known groups per letter). Inconclusive for [[C027]].")
T("T05","Date-profile test across the Favre pages","`timing_cribs.py`. History-only profile ('absent 24 Oct and 14 Nov, present from 28 Nov') ranks 1792 first of 642 groups; 977 and 998 rank 10th and 11th. Supports [[C026]]. Group 780 absent before 28 Nov: [[C029]].")
T("T06","Chance test for the Trochu run","28,897 candidate strings: only one fits 9113 8317 1504 as closely as 'trochu' (mean error <= 0.011); 51 names tried, chance of a lucky fit ~0.15%. For 9802 6124, 0.7% of strings fit as closely as 'vinoy': not significant ([[C013]]). Supports [[C012]].")
T("T07","Blind genre check: family news","Predicted before computing: est / port-ante / bonne santé. Fits 0.000, -0.010/+0.004, -0.004/-0.009; null: a random word pair fits two random groups within 0.01 in 0.05% of trials. Supports [[C009]], [[C010]], [[C011]], [[C014]].")
T("T08","Joint decoder loop","`joint_loop.py`. Beam-Viterbi over the whole telegram. Whole-word groups only 3/20 gold words; bracket-spelled runs 11/20 (+8); free segmentation, consistency voting, monotone bounds: no gain. Misses: bonne|sante, portante, ballon. Supports [[C002]], [[C031]].")
T("T09","R1 overlap test","18% of the inspectors' groups occur in R1's table (10% by chance) and the values make no sense in context. Supports [[C020]].")
T("T10","Scan checks","Rotated, enlarged crops. Chaudordy lines 2-5 and last line of page 2: 2 misreads in ~100 groups (80 should be 50; 639 probably 635). Inspectors' telegram header and the Nantes/Rennes/Trochu lines: transcription correct digit for digit. Supports the reliability of [[S01]], [[S02]].")
T("T11","Scoring of the two Mercadier decompositions","`MER-CAD-IER = 5511 6819 3412` (Pillon, later retracted) mean error 0.23; `MER-CA-DI-ER = 5504 1122 2514 3316` mean error 0.010 against the alphabetical rule. Supports [[C005]], refutes [[C018]].")
T("T12","R1-based isotonic calibration","Replacing the +0.015 bias by an isotonic map fitted on R1's numbering lowered MRR from 0.615 to 0.523. Supports [[C021]].")

# ------------------------------------------------------------------ CLAIMS
C("C001","The inspectors' table is an alphabetical lexicon over 0000-9999","supported",0.95,["T01","T03","T07","T08"],"13 syllable values and 7 whole words fit their alphabetical positions to ~0.015. Predicts the initial letters of any group in this code. Exceptions are possible ('almost alphabetical', [[S08]]).")
C("C002","Groups between beacons are words spelled in syllable groups","supported",0.9,["T03","T08"],"Repeated runs between 0101/0201/0301/0102 give names and words (Steenackers, Mercadier, pigeons). Allowing bracketed runs to be spelled words raised the joint decoder from 3/20 to 11/20 gold words.",depends=["C001"])
C("C003","The first digit of a beacon carries no meaning for now","hypothesis",0.5,["S08"],"Pillon: in R1 the balises 0136/0137/0138 are interchangeable, mostly paired 0136 xxx 0136 or 0136 xxx 0137. Consistent with the mixed pairs seen here (0101..0201, 0201..0101, 0301..0301). Not tested: [[Q03]].")
C("C004","The first spelled run is Steenackers: S-TEEN-A-K-ER-S","established",0.97,["S02","T03","T07"],"Opens and closes the telegram; first and last group equal; heading 'Steenackers a Mercadier'. Word-level identity is fixed by the printed heading; the piece split is phonetic (supported).",depends=["C001","C002"])
C("C005","5504 1122 2514 3316 is Mercadier (MER-CA-DI-ER)","supported",0.93,["T03","T11","S02"],"Four pieces within 0.02 of their alphabetical positions; rank 30 of ~30k by position alone.",depends=["C001","C002"])
C("C006","6816 4001 6129 8328 is pigeons (PI-GE-ON-S)","supported",0.9,["T03","T08"],"Three identical occurrences ('par ... d'abord restreint', 'ces ... mais il ne sera plus'); topic is pigeon fanciers.",depends=["C002"])
C("C007","0919 5121 6129 is ballon (BAL-L-ON)","hypothesis",0.6,["T03"],"Positions fit (rank 145 by position alone) and 6129 = ON as in pigeons; the joint decoder still prefers 'citoyens'. Needs piece-level consistency ([[Q08]]).",depends=["C008"])
C("C008","8328 = S, 3316 = ER, 6129 = ON (each in two words)","supported",0.85,["T03","T08"],"8328 is word-initial in Steenackers and final in pigeons; 3316 ends Steenackers and Mercadier; 6129 is inside pigeons and (probably) ballon.")
C("C009","4007 = general","supported",0.85,["T07","T06"],"Position +0.011; precedes the name 'Trochu' in 'Faites dire au general Trochu'.",depends=["C001"])
C("C010","3407 = est; 7027 0312 = PORT-ANTE ('est bien portante')","supported",0.85,["T07"],"3407 at +0.000; port at -0.010 and ante at +0.004; sentence 'est bien portante a Nantes'.",depends=["C001"])
C("C011","1026 8416 = bonne sante (three times)","supported",0.85,["T07"],"bonne -0.004, sante -0.009. Occurs in 'en bonne sante' x3 incl. 'est en ... a Rennes'.",depends=["C001"])
C("C012","9113 8317 1504 is Trochu (T-RO-CHU)","supported",0.9,["T06","T07"],"One string of 28,897 fits as closely; 'au general Trochu' with 4007.",depends=["C001","C009"])
C("C013","9802 6124 is Vinoy","hypothesis",0.15,["T06"],"Fits (0.012) but 0.7% of strings fit as well: not supported. Name unidentified ([[Q01]]).",depends=["C001"])
C("C014","The last paragraph passes family news for generals' wives at Nantes and Rennes","supported",0.8,["T07","S02"],"'Faites dire au general X que Madame X est bien portante a Nantes, quai de la Fosse 25, ... au general Trochu que Madame ... est en bonne sante a Rennes, quai de l'Universite 2'. Names other than Trochu open.",depends=["C009","C010","C011","C012"])
C("C015","5926 is not 'recu', 0603 is not 'depeche', 2215 is not 'capitale'","supported",0.9,["T07","S08"],"Positions 0.59 (recu would be ~0.77), 0.06 (depeche ~0.25) and 0.22 (capitale ~0.14), each ~0.18 off, ten times the typical error. 5926 is an M/N word; 0603 an A word; 1206 fits capitale.",depends=["C001"])
C("C016","5511 is the abbreviation 'M.'","hypothesis",0.5,["T03"],"Position -0.007 for 'm'; 'monsieur' +0.036.",depends=["C001"])
C("C017","6819 3412 is a surname starting P-E (the other recipient)","hypothesis",0.3,["S08","T03"],"Pierret, Perrier, Piet fit; ~0.5% of names fit as closely; the decoder suggests 'prefet'. Not 'Ernest' (error 0.17).",depends=["C001"])
C("C018","MER-CAD-IER = 5511 6819 3412 (Pillon, retracted)","rejected",0.02,["T11","S08"],"Pillon withdrew it (the run is a different recipient) and it scores 0.23 against the alphabetical rule.",refuted_by=["T11"])
C("C019","4906 is a K-syllable and 0218 an A, not ACK and N","supported",0.8,["T01"],"'ack' would sit at 0.00, K at ~0.49; N would be at ~0.58. Steenackers is spelled S-TEEN-A-K-ER-S, phonetically.",depends=["C001"])
C("C020","R1's table is not the inspectors' table","supported",0.9,["T09"],"18% overlap vs 10% chance; values nonsensical in context.")
C("C021","R1's numbering does not calibrate the inspectors' position map","supported",0.8,["T02","T12"],"R1 has no syllable entries; calibration lowered MRR from 0.615 to 0.523.")
C("C022","The Favre / delegation code is not alphabetical","established",0.95,["T05","S03"],"Verified words (negociations 182, premiere 723, cependant 835, comme 862, question 944, sauf 977, conference 1792, ballon 1980, Bruxelles 2232) lie in no alphabetical order.")
C("C023","The Chaudordy letter uses the Favre / delegation code, not R2","established",0.95,["S03","T05"],"Top-30 frequent groups overlap the Favre pages 10-13 times, R2's own letters 4, R1 0; 40 four-group runs recur across letters.")
C("C024","The Chaudordy letter is Favre's letter of 18 Dec 1870","established",0.97,["S03","S04"],"Heading in clear matches Favre's printed heading; cipher opens with 'nos communications par ballon'; four exact-repeat anchors match the print.")
C("C025","The cipher follows the print for ~330 groups, then departs from it","supported",0.7,["T08","S04"],"Windowed alignment reads for ~330 groups; afterwards nulls accumulate. Cause open ([[Q06]]).",depends=["C024"])
C("C026","1792 = conference","supported",0.92,["T05","S03"],"9 of 11 uses in the letter; absent 24 Oct and 14 Nov, present from 28 Nov; rank 1 of 642 under a history-only profile.",depends=["C023"])
C("C027","977 = sauf, 2232 = Bruxelles, 1980 = ballon, 944 = question, 723 = premiere, 862 = comme, 835 = cependant, 182 = negociations, 998 = partir (Favre code)","supported",0.75,["T05","T04"],"Position-matched anchors in the Chaudordy letter; 977 and 998 also rank among conference-timed groups. Not confirmed across other letters.",depends=["C023"])
C("C028","740 stands for 'la Russie' (not l'Angleterre)","hypothesis",0.5,["S03"],"Alignment of the opening groups puts 2066 = l'Angleterre and 740 = la Russie; an earlier anchor said Angleterre.",depends=["C023"])
C("C029","The table or the clerk changed in late November (group 780)","hypothesis",0.3,["T05"],"780 never occurs before 28 Nov (~2,100 groups) though it looks like a common word. See [[Q05]].")
C("C030","The commonest low Favre groups are inflection markers like R1's balises","open",0.2,["T08"],"Plural, feminine and other words use the same number of groups per syllable in the aligned region; only 43% of groups under 100 align to function words. Neither supported nor refuted.")
C("C031","Position + frequency + bigram context decodes spelled names reliably but not ordinary words","supported",0.85,["T02","T08"],"MRR 0.615 on 10 items; joint decoder 11/20: names and spelled words are right; bonne|sante, portante, ballon lose to function words. Ordinary words need a domain language model.",depends=["C001","C002"])

# ------------------------------------------------------------------ QUESTIONS
Q("Q01","Who are the Nantes (9802 6124) and Rennes (1114 5911 0131) correspondents?","Quai de la Fosse 25 (Nantes) and quai de l'Universite 2 (Rennes). Names unknown to Pillon. A source naming the fanciers or the generals' families would give syllables to test the table ([[C013]], [[C014]]).")
Q("Q02","Who is the other recipient 6819 3412 before Mercadier?","See [[C017]]. Someone in the Paris telegraph or post administration.")
Q("Q03","What do the different beacon pairs mean?","0101..0201, 0201..0101, 0301..0301, 0101..0102, 0102..0102: name type? capital? number of syllables? See [[C003]].")
Q("Q04","Is the 2 Nov telegram printed anywhere?","Not in the Enquete, Favre, Dagron, the 1872 article or (by phrase search) Steenackers 1883 ([[S05]], [[S07]]). A printed text would give a codebook directly.")
Q("Q05","Did the table change in late November?","[[C029]]; Pillon calls R2 the 'new cipher' in some correspondence.")
Q("Q06","Why does the Chaudordy cipher depart from the printed text after ~330 groups?","[[C025]]: shorter transmitted version, phrase codes, or Favre's later editing.")
Q("Q07","May we share results with Satoshi Tomokiyo, and how should Pillon be credited?","Asked in the draft reply; nothing public until he agrees ([[E06]]).")
Q("Q08","Does piece-level consistency fix 'ballon' (bal|l|on)?","If 6129 = ON from pigeons and Steenackers' ER is fixed, the run 0919 5121 6129 should decode as BAL-L-ON ([[C007]], [[C008]]).")

# ------------------------------------------------------------------ LEXICONS (machine-readable state used by the engine)
lex=[]
def L(g,kind,reading,status,claims,conf): lex.append(dict(group=g,kind=kind,reading=reading,status=status,claims=claims,confidence=conf))
for g,r in (("8328","s"),("9214","teen"),("0218","a"),("4906","k"),("3316","er")): L(g,"piece",r,"supported",["C004","C008","C019"],0.9)
for g,r in (("5504","mer"),("1122","ca"),("2514","di")): L(g,"piece",r,"supported",["C005"],0.9)
for g,r in (("6816","pi"),("4001","ge"),("6129","on")): L(g,"piece",r,"supported",["C006","C008"],0.85)
for g,r in (("9113","t"),("8317","ro"),("1504","chu")): L(g,"piece",r,"supported",["C012"],0.85)
L("7027","piece","port","supported",["C010"],0.8); L("0312","piece","ante","supported",["C010"],0.8)
L("0919","piece","bal","hypothesis",["C007"],0.6); L("5121","piece","l","hypothesis",["C007"],0.6)
L("4007","word","general","supported",["C009"],0.85); L("3407","word","est","supported",["C010"],0.85)
L("1026","word","bonne","supported",["C011"],0.85); L("8416","word","sante","supported",["C011"],0.85)
L("5511","word","m","hypothesis",["C016"],0.5)
json.dump(dict(code="inspectors",entries=lex),open(os.path.join(ROOT,"lexicon_inspectors.json"),"w"),indent=1,ensure_ascii=False)
fav=[]
for g,r,st,cl,cf in (("1792","conference","supported",["C026"],0.92),("977","sauf","supported",["C027"],0.75),("1413","10","supported",["C026"],0.9),("1024","12","supported",["C026"],0.9),
                     ("1319","decembre","supported",["C026"],0.9),("2232","bruxelles","supported",["C027"],0.75),("1980","ballon","supported",["C027"],0.75),("944","question","supported",["C027"],0.75),
                     ("723","premiere","supported",["C027"],0.75),("862","comme","supported",["C027"],0.75),("835","cependant","supported",["C027"],0.75),("182","negociations","supported",["C027"],0.75),
                     ("998","partir","supported",["C027"],0.7),("1915","armistice","supported",["C026"],0.85),("740","russie","hypothesis",["C028"],0.5),("2066","angleterre","hypothesis",["C028"],0.5)):
    fav.append(dict(group=g,kind="word",reading=r,status=st,claims=cl,confidence=cf))
json.dump(dict(code="favre",entries=fav),open(os.path.join(ROOT,"lexicon_favre.json"),"w"),indent=1,ensure_ascii=False)
print("seeded:",sum(len(f) for _,_,f in os.walk(ROOT)),"files")
