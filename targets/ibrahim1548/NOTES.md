# Sigismund August, Frater Georg Martinuzzi and Queen Isabella to Ibrahim Pasha, 1548 (catalogue 885)

Status: in progress (images are public; not yet transcribed; key R367 not yet applied)

## Documents
HHStA Wien, StAbt Türkei I:
- 7-4-4 (AIS 7040827), fol. 28-30: Sigismund August to Ibrahim Pasha. 2 cipher copies, 1 Latin copy. Beilage zu 7-4-3.
- 7-4-5 (AIS 7040824), fol. 31-34: Frater Georg to Ibrahim Pasha, 6 Jun - 2 Jul 1548. 3 cipher copies, 1 Latin copy. Beilage zu 7-4-3.
- 7-4-9 (AIS 7040845), fol. 51-59: Malvezzi to Ferdinand I, with two enclosed cipher copies.

## Access (corrected 30 Oct 2026)
The first session (29 Oct 2026) recorded the item as blocked: the AIS records say "Erforderliche Bewilligung: Kein
Zugang (Reservatbestand)", "Physische Benützbarkeit: Nicht möglich", "Zugänglichkeit: Ausgewählte
Archivmitarbeiter/-innen", and the bildansicht.aspx viewer showed nothing anonymously. That claim was wrong and is
withdrawn. Those fields govern the physical originals. The digital copies ("Reproduktion vorhanden: Digitale
Aufnahme") are public:

- The Austria sweep (`research/aut_hhsta/README.md`) viewed Türkei I scans without a login: GET the detail page
  for the session cookie, then `bild.aspx?VEID=<id>&DEID=<n>&SQNZNR=<page>` or
  `getimage.aspx?veid=<id>&deid=10&sqnznr=<page>&width=4000&klid=9` with a Referer.
- The catalogue vetting (29 Oct 2026, `research/vetting_2026-10/out_02.json`) downloaded and viewed 7-4-4 image 3:
  a full page of symbol cipher, about 13 lines, marked A, "Dupl. 1548", nothing written over or under it.
- The same route serves the RK Maximiliana scans (`targets/maximiliana1510/fetch_ais.py`).

`fetch_ais.py` in this folder downloads all three units to `img/` (git-ignored).

On 30 Oct 2026 the fetch could not run from that session: its egress proxy refused www.archivinformationssystem.at
(CONNECT 403, "host not allowed for this session"; WebFetch: DNS not resolved; web.archive.org also not allowed). That
is a limit of that cloud session's network settings, not of the archive. Run the fetch from a session that allows the
host, or from a local checkout.

## Key candidate: R367
The key is held: `targets/malvezzi1548/k367.txt` (DECODE R367 transcription, Tabella I and II) and `k386.txt` (R386,
second copy of the alphabet); the sign forms of this hand are in `targets/malvezzi1548/read_A.md` and `read_B.md`.

The cipher copies were made in Malvezzi's office at Constantinople in 1548 and sent to Ferdinand. The R367 code list
has code words for exactly these persons: Vb = rex Poloniae, zos = Frater Georgius, zes = Regina Isabella,
zis = Joannes Sigismundus, Sis = Ibrahim Passa. Malvezzi would encipher intercepted or copied letters for Ferdinand in
his own key, so R367 is the first key to test.

Note: the catalogue vetting's `key_check` says R367 does not apply ("other correspondents' ciphers"). That was judged
from the correspondents, not from the signs. If R367 reads the copies, entry 885 is a key lookup and should be closed
through `docs/_check_catalogue.py --close`, not edited by hand.

Check: the Latin exemplar filed with each letter is probably the plaintext. Method if the key fits: "read with known
key" (a key already identified for Malvezzi's correspondence); "key recovered based on adjacent plaintext" if the key
differs and is rebuilt from the Latin exemplar.

## Prior art
No decipherment found: repo (only malvezzi1548 related), web search, AIS descriptions.
Not checked: the printed Austro-Turcica 1541-1552 volume itself (pp. 276-278) for enclosures.

## Next steps
1. `python targets/ibrahim1548/fetch_ais.py` from a session that can reach archivinformationssystem.at.
2. Transcribe 7-4-4 image 3 first (13 lines), in the sign names of `k367.txt`.
3. Apply R367 (Tabella I letters, doubled-letter numbers, Tabella II code syllables; nulls as in malvezzi1548).
4. Align with the Latin exemplar; measure the share that reads; then 7-4-5 and 7-4-9.

## Remaining gaps
- all cipher copies (7-4-4, 7-4-5, 7-4-9) - blocker: not-attempted; images are public but were not downloaded: the 30 Oct 2026 session's network policy refused the AIS host. Not an archive blocker.

## Escalation
- [ ] siblings: 7-4-3 (the covering file) and the Latin exemplars in 7-4-4 and 7-4-5 to be read with the images
- [ ] clear-pages: the Latin exemplar is the likely plaintext; not yet seen
- [ ] known-keys: R367 / R386 held in targets/malvezzi1548; not yet applied (no transcription)
- [ ] print: Austro-Turcica 1541-1552 pp. 276-278 not seen
- [n/a] key-rebuild: nothing to rebuild before a transcription exists
- [n/a] retry: nothing read yet
