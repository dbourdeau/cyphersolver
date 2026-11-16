# Sweep: Omont NAF, Saint-Germain and Petits fonds volumes, "en chiffre" pieces (15 Nov 2026)

Brief: cover what the 14 Nov Omont sweep missed (Nouvelles acquisitions francaises, Ancien Saint-Germain), find "avec chiffre / en chiffre / chiffre /
lettres chiffrees" pieces with no decipherment, correct shelfmarks against Gallica, dedupe, one key per entry.
**Result: 8 rows in `candidates.json`, 11 bare-key or system leads in `key_leads.json`.** catalogue.json and leads.json untouched; no merge, no commit.
Every row is scored from the printed entry (`seen: catalogue`), no leaf viewed.

## What was swept (archive.org `*_djvu.txt`, curl)

The ids the 14 Nov sweep tried (`CatalogueBnfNaf*`) do exist; the file inside is named differently from the item id, so `download/<id>/<id>_djvu.txt` is a 404.
Use `archive.org/metadata/<id>` for the file name, e.g. `CatalogueBnfNaf3061-6500/Catalogue_gnral_des_manuscrits_fran_djvu.txt`.

- NAF II (3061-6500) `CatalogueBnfNaf3061-6500`; NAF III (6501-10000) `CatalogueBnfNaf6501-10000`; NAF IV (10001-11353, 20001-22811) `CatalogueGeneralDesManuscritsNAF4` (a second scan is `cataloguemanfran04bibluoft`).
- Ancien Saint-Germain III (18677-20064) `CatalogueGeneralDesManuscritsAncStGermFr3`.
- **Anciens petits fonds francais (fr. 20065-33264), never swept before**: tome I (20065-22884) `p4catalogue01bibluoft`, II (22885-25696) `p4catalogue02bibluoft`, III (25697-33264) `p4catalogue03bibluoft` / `cataloguegnrald05manugoog`. The 14 Nov sweep covered only fr. 1-15369.
- `cataloguemanfran01-03`, `cataloguegnrald03` and `p2catalogueg02/03` are other scans of volumes already covered.

`extract.py` dehyphenates, splits on shelfmark headings and keeps segments with a cipher word (`chiffr*`, `chifre`, `cryptogr*`, `steganogr*`, `ecriture secrete`), dropping
bindings ("au chiffre de ..."), "chiffres romains", Chifflet and the like; `seg_all.txt` is its output (38 segments, read by hand). `make_candidates.py` writes the rows.
**Yield is thin by nature:** the NAF and Petits-fonds entries are one-line descriptions of mostly 18th-19th-century papers, so "en chiffre" turns up only a few times per volume.
OCR heading numbers are unreliable here too (for example 'Noailles' items print as "1715. - 393 feuillets" and the Renaudot recueil as "1603"); numbers in the rows come from
the printed entry lines, and the unresolved ones are flagged in the row.

## Not swept (blocked or not found)

- **Ancien Saint-Germain I (fr. 15370-17058)** is on Gallica (`bd6t5396366p`), but the `.texteBrut` URL returns a "Verification de securite" page in Chrome; not clicked through.
  **Saint-Germain II (17059-18676?)**, **NAF I (1-3060)** and **NAF V (11354-13004, 22812-24218; Gallica `bpt6k130152p`)**: no archive.org item; NAF V on Gallica shares the security check on texte brut.
  These are the largest remaining gaps (Saint-Germain holds the Harlay correspondence).
- HathiTrust full-text search: 403 to curl (not retried in Chrome). Google Books not tried.
- `Table generale` (Gallica `bd6t5381243x`) not read; could index "chiffre" across all tomes.

## Rows, best first

1. **fr. 23202, Mazarin to abbe Fouquet 1651-60**, originals "chiffres", key copied at ff. 1-2, 4 DECODE records already solved (R7894-R7897), 3/4/2, Gallica `btv1b9063488m` (title checked).
2. **fr. 20506, Gaignieres VII: depeches chiffrees to Montmorency (Italy)**, 250 ff., volume partly known (Dodieu ff. 49, 52; Ranzo copy ff. 136-138), NAF 4206 keys at hand, 3/4/2, Gallica `btv1b525047581`.
3. **fr. 20140 f. 16, Danzay in Denmark 1557-67**, partly ciphered, 2/3/3, Gallica `btv1b52521512h`.
4. **fr. 23227-23228, Roslet to Cardinal de Noailles 1700-13**, keys at tome I ff. 1-6, 2/4/2, no Gallica record found, shelfmark from the printed line only.
5. **NAF 4543 f. 180, Audibert's musical-notation cipher 1746**, 3/3/3, not on Gallica by SRU.
6. **NAF 11238, Abelard to Heloise in cipher by Villette, 1768**, 15 ff., 2/5/1: a crib-able known text, the easiest row here.
7. **NAF 3145-3146 bis, Chanvallon and Breval to Lorraine 1601-30**, keys at end of vol. II, 2/3/3.
8. **NAF 22330 f. 107, "lettres en chiffres" to Breiffenstein at Delft, 1585**, 2/2/3.

## Dedupe

`known.py` and shelfmark grep: nothing on fr. 20140, 20746, 20975, 23026, 23227, 23594, NAF 3145, 4543, 22330. Already in the ledgers and so not rows: **fr. 20974** (R2276, catalogue 194; keys volume), **fr. 22225** (villeneuve1737 covers it; catalogue Maurepas lead),
**fr. 23054** (blasco1597 and Lasry's Spanish numerical letters), **NAF 4206** (R9467, R9481), and the volume fr. 20506 (partly, kept as a row). Duplicate: NAF 22336 f. 97 is a sibling of lead 1195 (BULAC MS.ARA.52, Haüy, 1781), see `key_leads.json`.
Withheld by request and not touched: fr. 3029 and fr. 3092 (neither appears in the new entries).

## Gallica shelfmark check (SRU, Chrome tab of my own, 6-10 s spacing)

Title matched the printed entry for fr. 20140, 20506, 20974, 20975, 23202. Found no record (not digitised under that string, or not found) for fr. 20746, 22882, 23026, 23227, 23594 and for the NAF numbers queried (3145, 4206, 4543, 11238, 22330, 8431); the NAF source string
on Gallica was not established, so "no record" for NAF means unconfirmed, not undigitised. Gallica SRU returned 429 for most of an hour after a first loop at 3.6 s plus the security-check page; the 429s were retried at 10 s with 30 s backoff.

## Blocks (for COVERAGE)

- gallica.bnf.fr `.texteBrut` on a catalogue ark: "Verification de securite" interstitial in Chrome (no CAPTCHA solved or clicked). `/SRU` still answers but 429s quickly (this session within a few requests at 3.6 s).
- archive.org: Saint-Germain I-II and NAF I have no OCR item; the file name inside an item is not the item id.
- HathiTrust full-text search 403.
Note: raw/ (archive.org djvu texts, 15 MB) was deleted after the run; refetch per the README to rerun extract.py.
