"""Hand-curated Abhilekh Patal rows -> candidates.json (links resolved from hits/*.jsonl). All rows are archive-description leads."""
import json, glob
ID={}
for fn in glob.glob('hits/*.jsonl'):
    for l in open(fn):
        r=json.loads(l)
        if r.get('Identifier'): ID.setdefault(r['Identifier'], r['itemId'])
U='https://www.abhilekh-patal.in/Category/ItemDetails/ItemDetails?itemId='
def links(*idents): return [{"label": i, "href": U+ID[i]} for i in idents]
NOTE="Scored from the archive record title and metadata during the 11 Nov 2026 Abhilekh Patal sweep (research/sweep_2026-11-11_asia/); not viewed"
ACC="Page images are on Abhilekh Patal behind a free registered login (ReadContent); not used in this sweep. The record page shows title, file number, page count and OCR keywords only, no abstract."
SRC="National Archives of India, Abhilekh Patal sweep (11 Nov 2026)"
def PA(extra): return "open as far as checked 11 Nov 2026: "+extra+" Tomokiyo's list (repo unsolved.htm) and the repo (known.py) have no entry; DECODE RecordsList search returned no records. The file itself was not seen, so a decipher inside it cannot be excluded."
def row(**k):
    k.setdefault("region","Other"); k.setdefault("period","1901-1950"); k.setdefault("cls","C")
    k.setdefault("score_note",NOTE); k.setdefault("seen","catalogue"); k.setdefault("source",SRC)
    k.setdefault("needs_archive_scan","no"); k.setdefault("access_note",ACC)
    return k
R=[
row(year=1912,date="1912",title="Yuan Shikai (Peking) → unknown (Tibet frontier), message in Chinese cypher that the Government of India could not properly decypher",
 correspondents="Yuan Shikai (\"Yaoshikinan\" in the record title), Peking → unknown, probably Chinese officials in Tibet or the Chumbi valley",place="Peking",language="Chinese",
 shelfmark="National Archives of India, Foreign Department, Deposit Cypher, 1912, Nos. 86-87 (PR_000004118254; duplicate record PR_000006222155)",
 folio_note="14 pp.; one message plus notes (OCR keywords: A.H. Grant, Simla)",
 status="Record title: \"Message in Chinese Cypher from Yaoshikinan, Peking which cannot be properly decyphered\". The title itself says the Cypher Branch failed to read it. Whether the groups are copied in the file is likely but not confirmed (no login used). Not on DECODE.",
 why="A message from the President of the new Chinese Republic during the 1912 expulsion of Chinese troops from Tibet, taken off the Indian telegraph line and left unread by Simla.",
 importance=4,solvability=2,difficulty=3,
 verify="Log in to Abhilekh Patal and open PR_000004118254: confirm the figure groups are copied and no later decypher is filed; then try the standard Chinese telegraph code and the key found by Capt. Campbell in 1907 (PR_000006228785).",
 links=links("PR_000004118254","PR_000006222155"),
 prior_art=PA("web search (Yuan Shikai 1912 cipher telegram Tibet intercepted Government of India) found no study or printed text of this message.")),
row(year=1907,date="1907-1909",title="Chinese officials in the Chumbi valley, cypher telegrams copied for the British Trade Agent at Yatung (Capt. W. L. Campbell), with Campbell's discovery of a key",
 correspondents="Chinese officials in the Chumbi valley (Chang Yin-tang's staff; OCR keyword \"Cheung Yuk Tong\") ↔ Peking / Lhasa; copies to Capt. W. L. Campbell, later Lt. F. M. Bailey",place="Yatung / Chumbi valley",language="Chinese",cls="B",
 shelfmark="National Archives of India, Foreign Department, Confidential B External C, 1907, File No. 45506 (PR_000006228785; duplicate PR_000004256746, dated 1908); sequel Foreign, Cypher Confidential, 1909 (PR_000004129545, 10 pp.)",
 folio_note="40 pp. + 10 pp.",
 status="Record title: \"Supply to Captain W.L. Campbell ... of copies of all Cypher telegrams sent or received by Chinese officials in the Chumbi Valley. Discovery of a 'Key' to the Chinese Cypher by Captain Campbell\". So at least part was read at the time; how many telegrams are copied in the file and whether each has a reading is not known. Class B: key reported in the file.",
 why="Chinese frontier traffic during Chang Yin-tang's mission and the British evacuation of Chumbi (1907-08); the key would also serve the later Chinese telegram files of 1908-15.",
 importance=3,solvability=3,difficulty=2,
 verify="Open PR_000006228785 after login: count the telegrams, see whether Campbell's key is written out and which telegrams lack a reading.",
 links=links("PR_000006228785","PR_000004256746","PR_000004129545"),
 prior_art=PA("web search (Campbell Yatung Chinese cypher telegrams Chumbi 1907 key) found only narrative histories of the Chumbi occupation, nothing on the telegrams.")),
row(year=1910,date="1908-1915",title="Chinese cypher telegrams acquired from the Indian telegraph lines for the Chief of the General Staff (Tibet frontier, Gyantse and Yatung)",
 correspondents="Chinese officials in Tibet ↔ Peking / Chengtu, via the Indian lines; repeated by the British Trade Agents at Gyantse and Yatung",place="Gyantse / Yatung / Calcutta",language="Chinese",
 shelfmark="National Archives of India, Foreign Department, Cypher Confidential, 1910-11, File 19/45 \"Acquisition of Chinese telegrams for the Chief of the General Staff\" (PR_000004147891; duplicate PR_000006222079); with Cypher Confidential 1909 No. 76 \"Return ... of Five Chinese Cypher Telegrams\" (PR_000004129548), 1911 Nos. 63-66 (PR_000004147900), Deposit Cypher 1913 No. 26 (PR_000004052244) and No. 51 (PR_000004052267), 1915 No. 56 (PR_000004053170)",
 folio_note="67 pp. main file; siblings 6, 31, 18, 7 and 6 pp.",
 status="Titles only: copies of Chinese cypher telegrams were taken for the General Staff from 1908, the Director-General of Telegraphs stopped the supply in 1911, and from 1913 the trade agents repeated them \"in groups of five figures so as to avoid the Chinese detecting\" it. The 1915 record has the OCR keyword \"Chinese Code\". No title says they were read. Likely the standard four-figure Chinese telegraph code, possibly with an additive.",
 why="The Chinese side of the 1910-12 occupation of Lhasa and the collapse of Chinese rule in Tibet, as intercepted by India.",
 importance=3,solvability=2,difficulty=3,
 verify="Open PR_000004147891 after login and see whether the 67 pp. hold the figure groups or only correspondence about obtaining them; test a sample against the standard Chinese telegraph code.",
 links=links("PR_000004147891","PR_000006222079","PR_000004129548","PR_000004147900","PR_000004052244","PR_000004052267","PR_000004053170"),
 prior_art=PA("web searches on the Chinese telegrams repeated from Gyantse and Yatung found no edition; the British Blue Books on Tibet print no cipher text.")),
row(year=1905,date="1904-1905",title="Russian cypher telegrams obtained by the British Consul-General at Meshed, and the Russian Consul at Bombay's foreign telegrams, copied for the Intelligence Branch",
 correspondents="Russian consulate-general at Meshed and Russian Consul at Bombay ↔ St Petersburg / Tehran / Tashkent (unknown in detail)",place="Meshed; Bombay",language="Russian or French",
 shelfmark="National Archives of India, Foreign Department, Confidential B Frontier, 1905, File 67/77 (PR_211200042292; duplicate records PR_000007019085 and PR_000006228867, the latter dated 1904)",
 folio_note="72 pp.",
 status="Record title: \"Supply to the Intelligence Branch of copies of (a) foreign telegrams received or sent by the Russian Consul at Bombay, (b) Certain Russian Cypher telegrams obtained by H.B.M's Consul at Meshed, (c) All telegrams from or to Russia which pass through Bombay or Karachi\". Nothing says they were read. Whether the groups themselves are in this file, or went to the Intelligence Branch with only covering letters kept, is not confirmed.",
 why="Russian consular cipher traffic in Khorasan and India during the Russo-Japanese War and the last phase of the Great Game.",
 importance=4,solvability=2,difficulty=5,
 verify="Open PR_211200042292 after login; look for copied figure groups. The London side should be in IOR/L/PS (QDL File 2626/1905 'Persia: Military Attaché at Meshed' is the neighbouring subject).",
 links=links("PR_211200042292","PR_000007019085","PR_000006228867"),
 prior_art=PA("web search (Russian cipher telegrams obtained British consul Meshed 1904-05 Intelligence Branch) returned only QDL files on the Meshed attaché post, none mentioning the telegrams or a reading.")),
row(year=1909,date="1908-1912",title="Foreign cypher telegrams acquired in Persia, the Persian Gulf and Maskat for the Chief of the Staff's Intelligence Branch",
 correspondents="foreign consuls and agents in Persia and the Gulf (unknown; Russian, German, French and Turkish posts are the likely senders) → their governments",place="Bushire; Maskat; Persia",language="unknown",
 shelfmark="National Archives of India, Foreign Department, Cypher Confidential, 1909, Nos. 72-75 \"Acquisition of Foreign Cypher telegrams for the Chief of the Staff's division (Intelligence Branch)\" (PR_000004129547; duplicate PR_000006222017); 1910 File 1 (PR_000004147856; duplicate PR_000006222044); 1909 No. 175, Maskat (PR_000004129558); Deposit Cypher 1912 No. 17 and Nos. 39-44, disposal (PR_000004118201, PR_000006222124)",
 folio_note="89 pp. + 44 pp. + 9, 13 and 14 pp.",
 status="Titles only (OCR keywords: Persia, Major P. M. Sykes; Persian Gulf, J. B. Wood; Major P. Z. Cox, Bushire). The files arrange for copies of foreign governments' cypher telegrams to be taken at Gulf and Persian telegraph offices and passed to the General Staff. No title mentions a decipher. The telegrams may be listed rather than copied.",
 why="A pre-1914 Indian programme of collecting foreign diplomatic ciphertext in the Gulf; if the groups survive they are unread Russian, German or Ottoman consular traffic.",
 importance=3,solvability=2,difficulty=5,
 verify="Open PR_000004129547 after login and see which governments' telegrams are copied and in what quantity.",
 links=links("PR_000004129547","PR_000006222017","PR_000004147856","PR_000004129558","PR_000004118201","PR_000006222124"),
 prior_art=PA("no study of this collection programme found by web search; the catalogue already holds a different Bushire item (QDL, Government Telegraph Code telegrams 1918-26).")),
row(year=1916,date="1915-1916",title="German cypher messages intercepted by the wireless stations at Bushire and Butcher Island (Bombay), sent to the India Office",
 correspondents="German wireless stations (probably the Isfahan / Baghdad / Nauen links; unknown) → unknown",place="Bushire; Butcher Island, Bombay",language="German",cls="B",
 shelfmark="National Archives of India, Foreign and Political Department, Cypher Confidential, 1916, File 72/81 (PR_000004051912; duplicate PR_000006079452); sibling 1915 File 101/134 \"Disposal of certain German Cypher Codes etc. seized at the German Consulate, Bushire ... Supply of German Cypher telegrams ... in connection with investigation ... with regard to German Cyphers\" (PR_000004052138; duplicate PR_000006079429)",
 folio_note="26 pp. (1916) and 87 pp. (1915)",
 status="Titles only (OCR keyword: Captain H. V. Biscoe). The 1916 file forwards intercepted German wireless cypher messages to London; the 1915 file concerns the code books taken at the Bushire consulate in March 1915 and German cypher telegrams sent for the investigation. London (Room 40) read German diplomatic codes of this family, so the traffic was probably read there; no reading is implied in the Indian file. Class B: key family known in the literature (the Bushire books).",
 why="German wartime traffic in Persia (Wassmuss, Niedermayer); the intercept copies may survive only here.",
 importance=3,solvability=2,difficulty=4,
 verify="Open PR_000004051912 after login for the intercept sheets; compare with TNA HW 7 / ADM 223 for Room 40 readings.",
 links=links("PR_000004051912","PR_000006079452","PR_000004052138","PR_000006079429"),
 prior_art=PA("web search (German cypher messages intercepted Bushire Butcher Island 1916) found the Cryptologia note on the Bushire code books and QDL files on Wassmuss, but no text or reading of these intercepts.")),
row(year=1917,date="1916-1917",title="Chinese code telegrams intercepted by the Canadian censorship, sent to the Government of India",
 correspondents="unknown Chinese senders in or via Canada (Pacific cable) → unknown",place="Canada (Pacific cable censorship)",language="Chinese",
 shelfmark="National Archives of India, Foreign and Political Department, Deposit Cypher, 1917, File No. 19 (PR_000004084171; duplicate records PR_000006080323 and PR_000006010493)",
 folio_note="71 pp., 121.9 MB",
 status="Record title: \"Chinese Code Telegrams intercepted by the Canadian Censorship authorities\" (OCR keywords: Sir E. Grey, London, Political Department). A 71-page file in the Cypher Branch's deposit series, so the telegrams are probably in it. No mention of a reading. May be the plain four-figure Chinese telegraph code.",
 why="Wartime Chinese traffic over the Pacific cable (possibly revolutionary or Ghadr-linked) that London passed to India.",
 importance=2,solvability=3,difficulty=2,
 verify="Open PR_000004084171 after login; if the groups are four-figure, decode a sample with the standard Chinese telegraph code book.",
 links=links("PR_000004084171","PR_000006080323","PR_000006010493"),
 prior_art=PA("web search (\"Chinese code telegrams\" Canadian censorship 1916-17) found only FRUS and CO 129 papers on wartime code restrictions.")),
row(year=1917,date="1917",title="Siamese Government cypher telegrams to its officials abroad, detained by the censor at Rangoon",
 correspondents="Siamese Government, Bangkok → Siamese legations abroad",place="Rangoon (censor)",language="Thai, French or English (unknown)",
 shelfmark="National Archives of India, Foreign and Political Department, External-B, 1917, Nos. 38-42 (PR_211200051015)",
 folio_note="18 pp.",
 status="Record title: \"Release of certain Cypher telegrams from the Siamese Govt. to their officials abroad which were detained by the Censor at Rangoon\". The file is about releasing them; copies of the detained telegrams may or may not be attached.",
 why="Siamese diplomatic cipher on the eve of Siam's entry into the war (July 1917).",
 importance=2,solvability=1,difficulty=5,
 verify="Open the images after login to see whether the telegrams are copied.",
 links=links("PR_211200051015"),
 prior_art=PA("no search beyond the repo and DECODE was run for this item.")),
row(year=1920,date="Jul-Nov 1920",title="German Legation at Tehran → Auswärtiges Amt, cypher telegrams of 1920, copies passed to the Russian cypher expert M. Jukowsky",
 correspondents="German Legation, Tehran → German Foreign Office, Berlin",place="Tehran",language="German",
 shelfmark="National Archives of India, Foreign and Political Department, External-B, Nov 1920, No. 64 (PR_000007024262; duplicate PR_211200051089); with External-B, July 1920, Nos. 192-199 (PR_000007023842)",
 folio_note="14 pp. and 26 pp.",
 status="Titles: \"Question of supply of German Cypher [telegrams] received and despatched from Tehran to Monsieur Jukowsky a Russian Cypher Expert\" and \"Removal of prohibition on the use of cypher ... by the German Legation at Tehran; cypher messages despatched by the Legation to the German Foreign Office\". The telegrams were being collected for a hired expert to break; the outcome is not in the titles, and the groups may not be in these B proceedings.",
 why="Post-war German diplomatic cipher from Persia, and a rare trace of a White Russian cryptanalyst working for the British.",
 importance=2,solvability=1,difficulty=5,
 verify="Open PR_000007024262 after login; look for the cypher groups and for any report of Jukowsky's result.",
 links=links("PR_000007024262","PR_211200051089","PR_000007023842"),
 prior_art=PA("no web search hit for Jukowsky as a cypher expert was looked for beyond the repo and DECODE.")),
row(year=1943,date="1943",title="Tibetan Government → its representative at Chungking, code message sent through the British Mission wireless station at Lhasa",
 correspondents="Tibetan Government (Kashag / Foreign Bureau), Lhasa → Tibetan representative, Chungking",place="Lhasa",language="Tibetan",
 shelfmark="National Archives of India, External Affairs Department, External Branch, 1943, File 79-X-43-Sec. (NAIDLF00697820)",
 folio_note="32 pp.",
 status="Record title: \"Transmission of certain Code Message from the Tibetan government to their Representative in Chungking through the British Mission wireless station at Lhasa\". The message passed through British hands in code; whether its text is on file, and whether the British could read it, is not stated.",
 why="A Tibetan government code of the 1940s, hardly documented anywhere.",
 importance=2,solvability=1,difficulty=5,
 verify="Open NAIDLF00697820 after login and see whether the code groups are copied.",
 links=links("NAIDLF00697820"),
 prior_art=PA("no dedicated web search run for this item.")),
]
json.dump(R,open('candidates.json','w'),ensure_ascii=False,indent=1)
print(len(R))
KEYS=[
 {"title":"Word Cypher for communication with Colonel Bailey at Tashkend, 1919","shelfmark":"NAI, Foreign and Political, Deposit Cypher, 1919, No. 20 (PR_000004053933; duplicate PR_000006080430), 10 pp.","note":"Key/word cipher issued for F. M. Bailey's Tashkent mission; no ciphertext implied.","links":links("PR_000004053933")},
 {"title":"Telegraph code sent by the Ottoman Bank to the Afghan National Bank, Kabul, intercepted 1940","shelfmark":"NAI, External Affairs, War Secret, 1940, File 11(8)-W (NAIDLF00918296), 9 pp.","note":"A commercial code table taken in censorship (OCR keywords: bank, key, code, cipher, table).","links":links("NAIDLF00918296")},
 {"title":"Translation of code messages found concealed on Ghulam Reza near Kermanshah, April 1918","shelfmark":"NAI, Foreign Department, Secret War B, Progs. Jan 1919 No. 272 (NAIDLF00578521), 18 pp.","note":"Already translated (read) per the title; kept as a crib/key source for Persian wartime agent codes.","links":links("NAIDLF00578521")},
 {"title":"German cypher codes seized at the German Consulate, Bushire, 1915","shelfmark":"NAI, Foreign and Political, Cypher Confidential, 1915, File 101/134 (PR_000004052138), 87 pp.","note":"Disposal of the seized code books; also listed as a sibling in candidates.json (German intercepts row).","links":links("PR_000004052138")},
]
json.dump(KEYS,open('key_leads.json','w'),ensure_ascii=False,indent=1)
