# Hebrew-script cryptology sweep (6 Nov 2026)

Scope: Hebrew, Judaeo-Arabic, Ladino, Yiddish, Aramaic, Samaritan; Cairo Geniza; medieval Ashkenazi, Sephardi, Italian and
Provencal manuscripts. 1000-1400 CE first, to 1500 second. Goal: a real ciphertext of text length, unread, with images.
Nothing here is in `catalogue.json`; `candidates.json` only for real leads. Scratch files are outside the repo.

Method: web search first, `curl` where WebFetch fails (the Princeton Geniza Project (PGP) certificate fails in WebFetch but
works with `curl -sk -L -A Mozilla/5.0`), then Chrome for anything with a bot check.

## Sources tried (log, appended as I go)

| Source | Route | Result |
|---|---|---|
| Princeton Geniza Project, `geniza.princeton.edu/en/documents/?q=cipher` | curl, HTML scrape | 39 hits for "cipher" (tag `cipher`), plus queries "cryptic", "secret script", "atbash", "encoded", "unidentified script". See Geniza table. Mostly (a) fiscal/chancery "cipher" signs (Arabic-script `adda`, `nuqila`, basmala monograms), (b) Atbash pen trials, (c) a handful of real Hebrew-script cipher texts. |
| Cambridge Genizah Research Unit blog (Elbaum, Q&A Wednesday, 22 Jun 2022) | WebFetch | Source for T-S NS J479; names Bohak, Zinger, Ashur, D'Ottone-Rambach as people who handled other Geniza ciphers |
| Web searches (general: Hebrew crypto literature, Tomokiyo, HistoCrypt/Cryptologia, Schmeh, Ashkenazi alphabets, colophon ciphers, Spanish/Italian Jewish ciphers) | WebSearch | Nothing beyond the Geniza and the short colophon/key material below; see Literature and negative results |
| CUDL search (`cudl.lib.cam.ac.uk/search?keyword=cipher`) | curl 403 (CloudFront); Chrome gets an AWS WAF challenge (HTTP 202 on API calls) and an empty result shell | Blocked. PGP carries the CUDL cataloguers' descriptions anyway, so little is lost |
| CUDL images, `images.lib.cam.ac.uk` IIIF | `curl https://images.lib.cam.ac.uk/iiif/<id>.jp2/full/1600,/0/default.jpg` | **Works with plain curl**, full resolution (`/full/full/0/default.jpg` too). IDs are in the PGP page source (e.g. `MS-TS-NS-J-00479-000-00001`) |
| National Library of Israel (KTIV, `nli.org.il`) | Chrome | Cloudflare "Just a moment" challenge that did not clear in 6 s. Not clicked through. Needs the user to clear it in Chrome, then search "cipher" and the Hebrew terms (*ketav sod, zofen, ketav ha-malakhim*) |
| Friedberg Genizah Project (`fjms.genizah.org`) | curl | Front page loads (200); catalogue is JS and needs registration. Not swept |
| DECODE harvest in the repo (`catalogue_harvest/decode/list.json`, 10,106 records) | local grep for Hebrew/Yiddish/Ladino/Judeo/Aramaic/Jewish/Geniza | **One** hit: Beinecke Mellon MS 136 (Arndt, 1798, cleartext German/Hebrew/Latin), not a Hebrew-script cipher. DECODE has no Hebrew-script record |
| `archive_sweep_2026-10/known.py` (hebrew, geniza, T-S NS, ketav, atbash, albam, Judaeo) | local | Only hits are `sweep_2026-11_arabic/README.md` (overlap note below); nothing in `catalogue.json`/`leads.json` except a 1809 Spanish courier packet (Hebrew-cursive "carta cifrada") |
| Bohak, "Cracking the Code and Finding the Gold" (CSIC 2010, pp. 9-23; whole volume PDF on `albert.ias.edu`) | Chrome PDF viewer + screenshots (curl gets a JS challenge; in-page fetch 403) | Read pp. 15-16. See the Bohak cipher family below |
| Bodleian *Medieval Manuscripts in Oxford Libraries* TEI (`github.com/bodleian/medieval-mss`) | `gh api search/code` | Western (Latin/vernacular) shelfmark series only: no `MS. Heb.` / `Opp.` / `Mich.` folders. "Hebrew cipher", "Judaeo-Arabic", "atbash", "ciphered Hebrew" return 0 ("cipher" alone returns 19 Latin/English MSS). Hit the GitHub rate limit after about 12 queries |
| Neubauer, *Catalogue of the Hebrew MSS in the Bodleian* (1886) and Margoliouth, *Catalogue of the Hebrew and Samaritan MSS in the British Museum* (1899, vols 1-2), archive.org djvu text | local grep for cipher/cryptogram/secret writing/alphabet/Temurah/Malachim/atbash | **Empty.** Neubauer uses "decipher" only for illegible hands; BM uses "cipher" only for Arabic numerals. Hebrew-script catalogues of this era do not describe cipher passages in those words. (Cowley's 1906 volume 2: archive.org item 404, not obtained) |

## Overlap with `sweep_2026-11_arabic` (same day)

That sweep already scraped the same PGP `q=cipher` list (39 hits); rows 1-10 of its table equal my first Geniza rows (T-S NS
70.1, AS 205.186, K24.23, NS J479, K24.19 family, K2.4). I only found it through `known.py`, so my PGP scrape of that list is a
duplicate. What this sweep adds: the other PGP vocabulary (cryptic, symbols, glyph, code), image checks (J479, AS 187.240,
13J18.19, J277), T-S 13J18.19 (a Coptic-numeral code in a 1139 letter), T-S AS 187.240 as a real candidate, the Bohak article
read, and the non-Geniza negatives.

## Geniza table (from PGP descriptions; none image-checked by me yet)

| Shelfmark | Date | Language / system | Extent | Status |
|---|---|---|---|---|
| T-S NS J479 (CUL; PGPID 8804) | no earlier than mid-13th c. (cites al-Busiri, d. 1295) | Judaeo-Arabic in an "idiosyncratic (unique?)" symbol cipher, ~22 symbols, some Hebrew letters have more than one glyph; also two pornographic passages, signature al-faqir Ishaq al-yahudi | one folio, both sides full, jottings in all directions | **Not read.** Elbaum has an annotated tentative alphabet (images on the Genizah blog, URLs below), says it is likely a made-up code, no solution published |
| T-S NS 70.1 verso (CUL; PGPID 26158) | undated | Judaeo-Arabic letter in a cipher | a letter | **Cracked by Gideon Bohak in 2025**, to be published by Bohak, Zinger and Elbaum. Already read; unpublished |
| T-S AS 205.186 (CUL; PGPID 42291) | undated | Judaeo-Arabic "bialphabetic" cipher: letters alef-tet with dot x10 and double dot x100 (i.e. the Hebrew alphabet by numerical value written as 1-9 with dots) | letter fragment, damaged | **Deciphered by Elbaum** (in PGP 2026); trivial numeral cipher |
| T-S K24.19 (PGPID 32681) | undated | Hebrew magical spell in cipher (Khatun daughter of Qatzur adjures jinn to reveal hidden gold) | one spell | **Read by Bohak 2010**, "Cracking the Code and Finding the Gold", in Alvarez-Pedrosa and Torallas Tovar (eds.), *Edicion de textos magicos de la Antiguedad y de la Edad Media* (CSIC, Madrid), 9-23. Same cipher listed in T-S K5.7, Misc.10.60, Misc.11.91, Misc.22.218, K24.23, ENA 3211.1-2 |
| T-S K24.23 (PGPID 32686) | undated | Judaeo-Arabic magic formulary, "in part with a cipher" (FGP) | part of a formulary | Probably the Bohak cipher; unchecked |
| T-S K24.24 (PGPID 33913) | undated | "Unidentified alphabet or cipher", magic | fragment | Unchecked |
| T-S K5.7 (PGPID 42030) | undated | magical characters "in an indecipherable cipher" with signs below (CUDL) | a sequence | Unchecked; same group as Bohak's |
| T-S AS 187.240 (PGPID 42435) | undated | Hebrew bifolio of pen trials with a cipher section, "merits examination (might be solvable based on the surrounding formulae)" | a section of a bifolio | Added to PGP in 2026, flagged unsolved |
| ENA 4100.7b (JTS; PGPID 11951) | undated | letter from a son in Qus to his mother, Judaeo-Arabic with lines 7-12 in cipher, noticed by O. Zinger | 6 lines | Tag "cipher, to examine" |
| ENA 3207.17 (JTS; PGPID 10130) | undated | magical recipes, bottom half of recto 6 lines in "code or cipher with symbols like Arabic letters" | 6 lines | Unchecked |
| T-S K2.4 (PGPID 29394) | 22 May 1135 (dated) | Arabic/Hebrew/Judaeo-Arabic miscellany, P3 "the secret letters", P4 f. 1v instructions on ciphers (Atbash, term *qabala*) with two Atbash examples | keys/examples only | Key material, not a ciphertext; the oldest dated Hebrew-script cipher key found so far (1135) |
| CUL Or.1080 J277 (PGPID 34004) | undated | three keys to Hebrew ciphers: (1) the Coptic-numeral cipher of Bodl. MS heb. f 102/28, (2) Atbash, (3) a pangram mnemonic key | keys only | Key material |
| Bodl. MS heb. f 102/28 (PGPID 19549) | undated | tribes of Israel in a Greek/Coptic-numeral cipher | a list | Key-type specimen |
| T-S K5.39, K5.47, 16.140 (1121), AS 153.438, AS 186.57, ENA 3982.15 | 11th-12th c. | Atbash pen trials | alphabets | Atbash exercises, nothing to read |
| JRL Gaster Hebr. 1863/6b, 11b; T-S NS 225.25b, AS 204.100, NS 338.60, Misc.27.4.33; BL Or 10656.15 | undated | "cryptic" Judaeo-Arabic | | Read "cryptic" as obscure content, not cipher; not followed |

Other Geniza cipher notes (Elbaum blog 2022): Oded Zinger found a letter in Arabic/Judaeo-Arabic with a portion in an
incomprehensible cipher, nearly every word beginning with alef (so not a plain substitution); Amir Ashur: some India Book merchants
use Coptic numerals as an uncracked code; D'Ottone-Rambach published an encrypted Qur'an manuscript (JIM 11/2, 2020, pp. 133-176).

Images for T-S NS J479: https://genizahfragments.lib.cam.ac.uk/wp-content/uploads/2025/05/t-s_ns_j479r.jpg and
https://genizahfragments.lib.cam.ac.uk/wp-content/uploads/2025/05/t-s_ns_j479_annotated.png ; CUDL page to be located.

## New Geniza findings beyond the `q=cipher` list (images viewed 6 Nov 2026)

| Shelfmark | Date | What | Extent | Status |
|---|---|---|---|---|
| **T-S AS 187.240** (CUL; PGPID 42435; tag `cipher`, added to PGP 2026) | undated Geniza, paper (probably 12th-14th c., unassessed) | Bifolio of pen trials. Viewed both sides: recto and verso carry several ruled-off blocks of word-divided (dotted) Hebrew letters that are not Hebrew words, and the lower right of the verso has a block of invented glyphs (not Hebrew letters) in lines that open with the same sign group again and again. Repeated lines suggest one formula written several times, possibly in two systems (Hebrew-letter and glyph). PGP: "merits examination (might be solvable based on the surrounding formulae)" | about 30-40 short lines in all | **Unread, no edition.** Image: `https://images.lib.cam.ac.uk/iiif/MS-TS-AS-00187-00240-000-0000{1,2}.jp2/full/full/0/default.jpg` (plain curl). First tests: atbash, albam, ayak-bekar, the J277 keys, then a crib-seeded substitution solve on the repeated formula lines |
| **T-S NS J479** (CUL; PGPID 8804) | after mid-13th c. (al-Busiri, d. 1295; paper) | See Geniza table. Viewed recto: about 25 lines in a clean pen, glyphs close to cursive Hebrew letters with extra variants, plus Arabic-script lines (a petition opening, circled in Elbaum's annotated copy) and a vertical marginal line. Cribs: the scribe's signature ("al-faqir Ishaq al-yahudi", repeated), two verses of al-Burda (a known text), legal formula *jara dhalika fi akhir jumada*, the alphabet written out several times in both directions (Elbaum: the scribe may have been developing the cipher) | one folio, both sides, roughly 1,200 glyphs | **Unread; Elbaum's partial mapping (about 22 symbols) is unpublished.** Images: CUDL `MS-TS-NS-J-00479-000-0000{1,2}.jp2`; Elbaum's annotated copy at `genizahfragments.lib.cam.ac.uk/wp-content/uploads/2025/05/t-s_ns_j479_annotated.png`. Contents partly pornographic, which matters for how it is written up |
| **T-S 13J18.19** (PGPID 9097; India Book IV, 41) | after 1 Nisan 1139 (Yitzhaq b. Avraham Ibn Ezra, in Spain, to Halfon b. Netanel ha-Levi) | Judaeo-Arabic letter; recto lines 11-12 and verso line 5 are Coptic/Greek numerals used as a code "presumably substituting for Hebrew letters, mechanism not yet determined". Elsewhere names are hidden by code names ("the elephant"; "harf al-nun") | two lines plus about 11 numerals | Unread. Image `MS-TS-00013-J-00018-00019-000-0000{1,2}.jp2`. A candidate key sits in the same collection: CUL Or.1080 J277 verso key 1 and Bodl. MS heb. f 102/28 are a Greek/Coptic-numeral cipher for Hebrew letters. Oldest dated unread Hebrew-script cipher found (1139) but too short for anything but a key test |
| F 1908.44U / Bodl. MS heb. e 94/30 (Halfon letters, 1139) | 1139 | "Much of the letter is written in coded language" (code names), a nomenclator-style argot, not a cipher | whole letters | Not a ciphertext; context for 13J18.19 |
| T-S AS 178.169 (PGPID 36936) | undated | list pairing each Arabic phrase with a nonsense "translation or code word" (trade argot, cheeses) | a list, Arabic script | Code list, Arabic script, not Hebrew |
| T-S AS 153.317 (PGPID 22224) | 17th-19th c. | ledger in Hebrew letters in an unidentified argot (Ladino and Turkish words) | 16 entries | Out of period |
| JRL Gaster Hebr. 177 (Rylands) | 17th-18th c. | nineteen angelic alphabets (charakteres) f. 44b-45a | alphabets | Key-type material, out of period; charakteres are not text ciphers |
| Colophons with the scribe's name in atbash: Cambridge Geniza Nehemiah fragment, Joseph b. Nimorad, 903/4 CE; a Geniza colophon of Av 4876 AM (1116 CE), Halfon b. Joseph; Sotheby's 2017 mahzor flyleaf (atbash and ayak-bekar for the patriarchs and Moses) | 904, 1116 | one name each | a few letters | From a web-search snippet (CUDL MS-TS-NS-00246-00026-00002 cited); I did not open it. Oldest Hebrew-script dated cipher use found, but a name only |

### The Bohak cipher family (read from the article)

Bohak 2010, pp. 15-16: a substitution cipher "not attested elsewhere" (Hebrew letters), found on strip-shaped fragments of one
recipe book, 11th c. by script. Fragments: T-S Misc.10.60 (encrypted recipe title in the margin), T-S Misc.11.91 (line 20),
T-S Misc.22.218 (recipe title and an unexplained 9-letter sequence), T-S K24.23 (several lines of formulae), JTSL ENA
3211.1-2 (titles; a verso of voces magicae), and T-S K24.19, the only continuous text (Chatun's dream request for hidden gold),
read and published by Bohak. He thinks the cipher was meant to raise magical potency, not to hide the text. PGP links the
related hand to the cantor Abu Sahl Levi (d. 1211; ENA 3581.8, T-S AS 173.247) and Manchester B 5652 carries the same cipher as
eight other fragments (catalogue note). Verdict: key published, the texts are titles and formulae a few words long, already
read by Bohak. No work for us.

## Literature and negative results

- **Dead Sea Scrolls "Cryptic A/B/C"** (Qumran, Second Temple): Cryptic A deciphered 1955; Cryptic B claimed by E. Oliveiro
  (Groningen, *Dead Sea Discoveries*, Dec 2025, 17 of 22 letters). Not the period; recorded as the oldest Hebrew-script
  ciphertext, already attacked.
- **Samaritan *tashqil* colophon cryptograms** (a scribe's name in a letter grid in Pentateuch scrolls; Gotthiel 1906 on a
  disputed "734 CE" date): short, read.
- **Kabbalistic and Ashkenazi cipher alphabets** (*ketav ha-malakhim*, Alphabet of Metatron, *transitus fluvii*, Agrippa's
  Malachim, the *Sefer Raziel* material): alphabets and charakteres, i.e. key material. No preserved long ciphered text
  turned up; the ones I could place are 16th-18th c. The *Sefer Hasidim* search found no cipher alphabet.
- **Hebrew-letter cipher in a Christian chancery** (Aragon, Navarre, Italy; Latin or Romance text enciphered with Hebrew
  letters): searched in English, Spanish and Italian, no documented case. (Hebrew-letter *transcription* of Romance, aljamia,
  is not a cipher.)
- **Alchemy and medicine in Hebrew script**: Ferrario's Geniza alchemy fragments and the Gaster/Rylands recipe books: no cipher
  noted. The Hebrew-looking "secret alphabet" alchemical items already in the repo are German texts in invented signs
  (Heidelberg Cod. Pal. germ. 597, 1426, read 1869; the Dresden alphabet MS), not Hebrew-script targets.
- **Jewish merchants' letters** (Goitein, *Letters of Medieval Jewish Traders*): code names and argot, no cipher beyond the
  Geniza items above.
- **HistoCrypt, Cryptologia, Tomokiyo, Schmeh**: no article on a medieval Hebrew-script cipher. Tomokiyo's site did not surface.
  Schmeh's Hebrew-looking items are 20th century (Schaub letter 1920s, Dominas notes, a church statue inscription). The NSA
  *Cryptologic Quarterly* 2014 piece on Renaissance cryptography and the Cabala is about Christian use of *temurah/ziruf*, not
  about preserved ciphertexts.
- **Needs Chrome or a human**: NLI KTIV (Cloudflare), CUDL search (AWS WAF), FGP catalogue (registration), the Bohak volume
  beyond pp. 15-16 (only viewable in Chrome's PDF viewer).
- **Not covered**: Hebrew manuscripts of Italy (Parma Palatina, Ambrosiana, Vatican ebr.), BnF Hebreu on Gallica, JTS, Sefaria,
  the Schoenberg Database, Oxford's own Hebrew catalogue pages. No cipher-specific route was found, and none can be searched
  without a catalogue term; the Hebrew terms (*ketav sod, ketav nistar, tzofen, ketav ha-malakhim*) in each OPAC are the next
  step for a human.

## Verdict

No unread Hebrew-script ciphertext before 1400 of the size the project usually needs was found outside the Geniza, and inside
it the set is small. The best leads are all Cambridge Geniza items with images fetchable by curl: **T-S AS 187.240** (dozens
of short lines in two cipher systems with repeated formula lines, no edition), **T-S NS J479** (one folio, both sides, after
c. 1250, known cribs, Elbaum's partial key unpublished) and, for date, **T-S 13J18.19 (1139)** (a short Coptic-numeral code
with a candidate key in J277). Real Hebrew-script cipher use is rare and mostly short (titles, names, spell lines). Bohak,
Zinger and Elbaum are working the Geniza set (NS 70.1 cracked 2025, unpublished), so any attempt should be coordinated with
Alan Elbaum (Princeton Geniza Project) before anything is published or sent anywhere.
