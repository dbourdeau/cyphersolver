import subprocess, sys
PL = ["Tangier","Morocco","Barbary","Algiers","Tunis","Tripoli","Egypt","Sudan","Khartoum","Gordon","Abyssinia","Zanzibar","Congo","Niger","Sierra Leone","Gold Coast","Ashanti","Cape of Good Hope","Natal","Zulu","Transvaal","Rhodesia","Mozambique","Angola","Madagascar","Ethiopia","Mauritius","Senegal","Gambia","Lagos","Livingstone","Stanley","Mafeking","Boer","Lagos","Kenya","Uganda","Nyasaland","Somaliland","Elmina","Guinea","Goree","Fernando Po","Bornu","Timbuktu","Cairo","Alexandria"]
qs = []
for p in PL:
    qs += [f"cipher {p}", f"cypher {p}"]
subprocess.run([sys.executable, "bl_search.py"] + qs)
