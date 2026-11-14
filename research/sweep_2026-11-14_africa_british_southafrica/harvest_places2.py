"""Second place pass: non-cipher wordings (in figures / in characters / secret writing / cryptogram) x Africa places."""
from harvest import run
PLACES = ["Africa","Gold Coast","Sierra Leone","Gambia","Cape","Natal","Zanzibar","Sudan","Egypt","Abyssinia","Morocco","Tangier","Algiers","Tunis","Tripoli","Congo","Transvaal","Rhodesia"]
for p in PLACES:
    for t in ['"in figures"','"in characters"','"secret writing"','decipher']:
        run(f"{p} {t}", maxpages=3)
