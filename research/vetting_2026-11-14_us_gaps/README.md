# Vetting, US gaps sweep leads 2669-2674 (14 Nov 2026)

Run by a Claude Code session (Claude Sonnet 5.5). `research/sweep_2026-11-14_us_gaps` (6 rows) merged as leads 2669-2674 (the first merge
took one row; five rows had region/period values outside the merge vocabulary and were corrected in `candidates.json`). `make.py` builds
`vetting.json`; `python research/vet.py --check` passes.

- **Promoted (1):** 2670 (Dundas papers, Penn Ms. Coll. 888 Box 11 f. 26: Malcolm's memorandum of 2 Dec 1798 in clear plus a cypher copy; `seen.kind` "not online").
- **Closed (3):** 2669 read (Deane to Wilson 1780: the FLP sheets are the deciphered letters themselves, with a modern transcription); 2671 not_cipher
  (Forbath diary: German stenography); 2673 not_cipher (the Morgan item is Macdonald's covering letter; transcription of the code letter was sent to Strickland in 1850).
- **Unvetted (2):** 2672 (Fraser diaries: not digitised, unclear whether the Greek is a cipher), 2674 (Devoiants: decipherments only as far as the abstract says, on-site only).
- Access notes: Bryn Mawr ArchivesSpace and Morgan CORSAIR return 403 to WebFetch; a Chrome tab gets through (Bryn Mawr's Cloudflare check passed unaided after a few seconds).
