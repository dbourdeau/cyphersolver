# Vetting, ajbeling (18 Nov 2026)

Run by Andrew Beling (`ajbeling`) with AI agents on 18 Nov 2026; checked again against main 7d9b91fb8 on 22 Nov 2026.
No person has checked any of it. No cipher word is read here. The manuscripts were viewed in State Papers Online
(Gale) through a subscribing library: they are linked, and no image from it is in this folder. The printed calendars
are public on archive.org.

## Leads

- **957 · duplicate (unchanged).** Thomas Barnes to Charles Paget, draft by Phelippes, Green (1867) p. 328 item 75,
  **14 March 1593**: TNA SP 12/244 f. 140r-v. The vetting of 29 Oct 2026 already gave 1593 and the duplicate with lead
  903; the top-level year and date still say 1594. `lead_updates` sets the year, date, shelfmark, folio and links.
  Two readers, apart and without a key, marked the cipher positions on f. 140r (body and sideways margin): 43 shape
  positions agree (`barnes/`).
- **903 · duplicate (unchanged).** The grouped record: its January hit is Bristowe [Moody] to White, 28 Jan 1592
  (catalogue 955); its March hit is lead 957. The vetting of 16 Nov 2026 could not find the June item in the 1591-1594
  calendar. It is in the 1601-1603 calendar: Wicham to Derick, **1 June [1594]**, Green (1870) pp. 173-175, enclosure
  75.I of Winwood's despatch of 10 April 1602, TNA SP 12/283a ff. 151-152, with the three keys Green lists
  (75.V-VII) at ff. 156-158. `lead_updates` sets the title, dates, shelfmark and links. The June letter has no record of
  its own and could be split off as a lead.

## Wicham's letters and the keys (`wicham/`)

Two readers transcribed the numbers on the September and August letters without a key; a third transcribed the keys
(`wicham/key/`, checksums in `SHA256SUMS`). Five agreed numbers have entries in the first key (Owen twice, Paget,
Jaques, and an S-name whose middle letters are disputed). Two tests were written down before they were run, each run
once, and **both missed** (`NOTES_results.md`; plans with their SHA-256 in `PLAN_*.md` and `*.sha256`; inputs hashed in
`*_inputs.json`, all of which match the files here):

- September, three named slots predicted, all three required: 2 of 3 (best of 1,000 shuffled tables: 1).
- July and August, four names per letter, three hits needed with one in each letter: 2 of 8, both in August (3 of
  1,000 shuffles reached 2).

No word of the June letter is read. The two misses do not rule out that the letters use the first key (75.V): the
tests checked only a few named slots.

`barnes/` and `wicham/` are a record of work. The verdicts and `lead_updates` above rest on Green's calendars and on
the dated, foliated originals; they do not depend on the transcriptions or tests in those folders.

## Catalogue 956, for the maintainers (not edited here)

CONTRIBUTING asks that `catalogue.json` is not edited in a pull request, so this correction is only proposed
(`saintmain_956.md`):

- `date`: Green (1867) p. 309, item 18 prints **Jan. 18** (1593); the entry says 19 Jan. The letter mentions a Parliament summoned
  for 19 February, and Green's next item, no. 19, is dated 19 January. Two of three readers read the day in the closing as 18, one preferred 28; the
  docket on f. 40v has 1592/3.
- `shelfmark`: TNA SP 12/244 ff. 39-40 (Gale scans 40-42; [record](https://link.gale.com/apps/doc/MC4304381018/SPOL)).
  The entry's `verify` field points to SP 12/243.
- Several cipher passages on f. 40r have lighter English written above them; whether they read the cipher was not
  checked.

## Searched and left

Green (1867) and (1870), Winwood's *Memorials* I p. 404 (archive.org); the repository's leads and catalogue for
Barnes, Saint Main, Wicham, Derick, Sterrell and Bristowe; Cryptiana's unsolved list in the repository; the DECODE
harvest in the repository. Left: the June letter's mixed groups that begin with a 2; the S-name of number 144; the
interlinear English on SP 12/244 f. 40r.
