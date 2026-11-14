"""Place x term harvest on TNA Discovery (no department filter). Appends to raw.jsonl."""
from harvest import run
PLACES = ["Africa","Gold Coast","Ashanti","Sierra Leone","Gambia","Lagos","Niger","Nigeria","Cape Colony","Natal","Zululand","Transvaal","Orange Free State","Basutoland","Bechuanaland","Rhodesia","Matabeleland","Nyasaland","Zanzibar","Uganda","Kenya","Sudan","Khartoum","Egypt","Abyssinia","Morocco","Tangier","Algiers","Tunis","Tripoli","Congo","Madagascar","Mauritius","Somaliland","Mafeking","Ladysmith","Kimberley","Delagoa Bay","Mozambique","Angola","Liberia","Senegal","Livingstone","Barbary","Fernando Po","Cameroons","Togoland","German East Africa","Benin","Zambezi","Swaziland"]
TERMS = ["cipher","cypher"]
for p in PLACES:
    for t in TERMS:
        run(f"{p} {t}")
