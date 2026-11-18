# Wave 20 vetting, batch b13 (16 Nov 2026)

Leads: 2667 1696 2653 2437 2896 2897 2898 2224 2082 1293 2081 1295 2089 1299 1910 2489 1908 1904.
Proposed vetting blocks are in `proposals.json`, merged from `p/*.json` by `add.py`. The lead agent applies them;
leads.json and catalogue.json are untouched. `prior.py` / `prior_out.txt`: known.py plus greps of Tomokiyo's
unsolved.htm and Lasry's GL.htm (both fetched 15 Nov 2026). `sheets.py` makes contact sheets. Images are in `img/` (git-ignored).

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2667 | open | medium | Thüringen Findbuch: Nr. 2661 'Schreiben in Geheimschrift (Bl. 191-195)', no decipherment; not online |
| 1696 | key_lookup | high | W 004 Nr. 119 is digitised; cipher found inline on images 022-023 (Landsberg, 5 Jan 1677), key on image 133 reads it (45-19-13-36 = KEIN) |
| 2653 | read | high | DDB Solr record: 'Chiffriertes Schreiben mit Dechiffrierung' |
| 2437 | open | medium | Stein ed. II/2 list has no Niebuhr letter Oct-Dec 1808; 7 scans seen, no plaintext; Niebuhr letters ed. 1926 unchecked |
| 2896 | none | - | Klemm 2025 (study of MS 1662) behind Brill bot check |
| 2897 | none | - | IIS: no images; host timed out |
| 2898 | none | - | IIS: no images; host timed out |
| 2224 | partly_read | medium | MTT 1906 prints all four letters; only 7 single '(titkos jel)' signs open |
| 2082 | none | - | three-volume cluster, ArchiveGrid bot check |
| 1293 | not_cipher | medium | MHS edition: 1760 reply 'in shorthand'; 1757 'brief note in undeciphered code' in Paine's hand |
| 2081 | not_cipher | medium | MHS blog page images: stroke shorthand; 1840s owners sought a stenographer |
| 1295 | none | - | MHS guide only; Vodra edition not online |
| 2089 | none | - | MSU finding aid only |
| 1299 | none | - | SHD inventory host refuses connections; probably duplicates of the despatches Pusch decoded |
| 1910 | none | - | series-level only, Hungaricana bot check |
| 2489 | open | low | MNL records: 'részben megfejtetlen titkosírással'; consider merging into catalogue 2475 |
| 1908 | none | - | APE Cloudflare; title-only unit |
| 1904 | open | low | MNL records 'titkosírással írt levél'; no. 8939 decipherment note is the doubt for 7950 |

## Routes found this pass

- **DDB Solr API answers curl** although Archivportal-D and DDB item pages are behind Anubis:
  `https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select?q=id:<ITEMID>&wt=json` gives the full
  record text, `digitalisat`, and `provider_item_id` (for LAV NRW, the `Vz_` id).
- **LAV NRW Msc. VI images**: `https://www.landesarchiv-nrw.de/data01/Abt_Westfalen/Msc_VI/00119/MSC_VI_00119_NNN.jpg`.
- **lwl.org (Westfälische Geschichte) is under maintenance** (redirects to /baustelle/), but the Stein-edition PDFs
  `txt/fs-NNNNN.pdf` come from the Internet Archive (`web.archive.org/web/<ts>id_/...`). Large files need range-resume
  (`rng.py`-style); the Wayback CDX API timed out. fs-11559 is the 'Verzeichnis der in Band II/2 abgedruckten Stücke',
  fs-11598 is Band III's, fs-11742 is Band VII's. The `325dig-download` scans on lwl.org still answer.
- **MNL AdatbazisokOnline** record pages answer curl; search result lists are rendered by JS (counts only).

## Errors in lead records

- 1696: `access` should be "online" (digitised, 134 images); the volume does contain ciphertext, not just the key.
- 2437: the unit has 7 images (000-006, three written pages), not 14.
- 2489: E Fasc. 112 fol. 1-4 is dated 27 Dec with no year in the MNL record (the lead gives 1708 overall).
