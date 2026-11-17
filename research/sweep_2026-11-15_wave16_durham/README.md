# Wave 16 (15 Nov 2026): Durham, Abbas Hilmi II papers, HIL/64 and HIL/65, the frames wave 15 left

Continues `research/sweep_2026-11-15_wave15_arabic2/` (section 2). Wave 15 screened the two-form frames and sampled
8 of the 264 six-form frames. This pass screens the rest for telegrams with cipher groups and for clear copies.

## Route

Plain Python/curl to `iiif.durham.ac.uk`, no bot check. Manifests copied to `raw/`.

- `fetch.py <hil64|hil65> <first> <last>`: finds the bounding box of the forms on wave 15's 1,024-px copy, then
  fetches that box as a 2 x 2 grid of IIIF region requests (1,024 px each, one request a second) and stitches it to
  about 2,050 px (`img/<tag>/<frame index>_<HIL numbers>.jpg`). A form is then about 650 px wide.
- `prep.py <tag> <first> <last>`: 1,100-px screening copies (`img/v/`), one frame per image; a form is about 350 px
  wide, enough to tell words from letter groups. `view.py <tag> <idx> crop x0 y0 x1 y1`: full-resolution crop.
- Frame index = 0-based position in the manifest (the number at the start of the file name); wave 15's README counts
  frames from 1.

## Progress log

(appended as the work goes; per-part notes are in `notes_*.md`)

- 15 Nov, part 1 done: hil64 frame indices 0-67 (HIL/64/1-400), all 68 frames. Notes: `notes_hil64_a.md`.
  Cipher: 64/17 (Arabic letter runs; clear copy 64/16), 64/214 (clear copy 64/61-62), 64/239-240 (clear copy
  64/118-119), 64/400 (bare, 8 groups, 9 Jan 1909). About 51 code-word forms.
- 15 Nov, part 2 done: hil64 frame indices 68-135, 232, 233 (HIL/64/401-816, 1008-1011), all 70 frames. Notes:
  `notes_hil64_b.md`. **Clear copy of telegram no. 30 of 13 July 1912 (the cipher at 64/890-891) found, all three
  sheets: HIL/64/739 + 738 + 737.** Cipher: 64/402 (clear copy 64/403), 64/759-761 (clear copy 64/762-764).
  24 code-word telegrams. No clear copy of 64/400.
- 15 Nov, part 3 done: hil65 frame indices 25-88 (HIL/65/51-428), all 64 frames. Notes: `notes_hil65_a.md`.
  Cipher: 65/272-273 (Siwa, 7 June 1913, 7 groups, bare). Wave 15's two pairs confirmed. 16 code-word forms.
- 15 Nov, part 4 done: hil65 frame indices 89-152 and 297-311 (HIL/65/429-810, 1100-1127), all 79 frames. Notes:
  `notes_hil65_b.md`. Cipher: 65/1122 (Khartoum, 26 Feb 1914, 5 groups, bare). 24 code-word telegrams.
- Every frame wave 15 left is now screened (281 frames). Next: a second look at the two-form frames wave 15 saw
  only in part (hil64 136-231, hil65 153-296), for clear copies of the three bare telegrams (`sheet15.py`).
- 15 Nov, second look done: hil64 136-231 (`notes_hil64_c.md`) and hil65 0-24, 153-296 (`notes_hil65_c.md`; 291-296
  by the lead session), whole forms on sheets of wave 15's 1,024-px copies. No clear copy of the three bare telegrams,
  no further cipher form, no third cipher sheet of 64/890-891.

Other scripts: `region.py` (hi-res IIIF region by canvas fractions), `sheet15.py` (whole-form sheets of wave 15's
copies), `waitprep.py` (wait for the fetch, then prep).

## Result (15 Nov 2026)

**Coverage.** All 546 frames of the two files have now been looked at: wave 15 screened 265, this pass the other 281
(hil64 indices 0-135 and 232-233; hil65 indices 25-152 and 297-311) at 1,100 px a frame, about 350 px a form, with
full-resolution crops or IIIF regions on every suspect. The 259 two-form frames wave 15 saw as strips were looked at
again as whole forms at about 390 px a form. Limits: (a) a single enciphered word inside a long clear telegram could
pass unseen at that size (one such doubt: 65/551, "very CKKxy accompany", probably a copying slip); (b) the Arabic
forms were judged by look (running script against runs of isolated letters), not read; (c) the fetch box clipped a
few frames: 64/71, 74, 365, 368, 532-534, 719-721 were checked on wave 15's 1,024-px copies instead (all clear
English); (d) no group was collated a second time.

### The catalogue entry: HIL/64/890-891 has its plaintext in the file

Telegram no. 30, 129 words, Railhead, 13 July 1912, to Herbert ("Sawahil"), Alexandria, signed Armstrong. The cipher
copy (64/891 sheet 1, 64/890 sheet 2; clear English with runs of five-letter groups; no sheet 3 in the file) has a
**complete clear copy in three sheets at HIL/64/739 + 738 + 737** (hil64 frame index 122, bottom row, right to left):
"214. your O.1. and H.20. yesterday I inspected 42 bales and found they contained Karki clothes and grey great coats
450 suits of former and 90 of latter stop I wired Matrooh and have received instructions to detain till orders stop
the suits are military pattern but have plain but tons ..." (full text in `notes_hil64_b.md`). Same number, word
count, station and date on both; the clear words of the cipher copy match (clear "the suits are military pattern but
have" = cipher copy "the suits are bfefp ptqaf rrvtw but have", read at 390 px). The telegram it answers (Herbert's
"O.1" of 13 July) is at 64/732 + 731, clear. So catalogue entry 2899 is a key-recovery case with known plaintext, not
a bare text: its record needs changing by whoever holds the catalogue (not touched here).

### Cipher / clear pairs (key material; not in candidates.json)

All are simple substitution with the words run together and regrouped in fives, set inside clear text; the alphabet
differs between 1908 and 1912. No cipher form carries a decode. Groups uncollated.

| Cipher | Clear copy | Telegram | Size |
|---|---|---|---|
| HIL/64/17 (frame 2) | HIL/64/16 (frame 2) | no. 1028, 41 words, Cairo 20 Dec 1907, Minister of the Interior to the Governor of Alexandria; **Arabic**, three runs of isolated Arabic letters replacing phrases | about 39 letters |
| HIL/64/214 (frame 36) | HIL/64/62 + 61 (frame 10) | no. 1054, 129 words, 26 Sept 1908, Khartoum to Mulki Cairo (Katfia trial) | about 46 groups; a second cipher sheet not seen |
| HIL/64/240 + 239 (frame 40) | HIL/64/119 + 118 (frame 20) | no. 1882, 179 words, 30 Nov 1908, Hakimam Khartoum to Bernard Cairo | about 33 groups in 7 runs; t=o h=f i=u s=w e=y checked on one run |
| HIL/64/402 (frame 68) | HIL/64/403 (frame 68) | no. 1656, 3 Jan 1909, Lewa Khartoum to Stack, Harbia, Cairo | 5 groups `VBuxp cupum xpfuB xpguw spcov` = a name ("Miralai Ibrahim Nagis ...", clear read at 1,100 px only) |
| HIL/64/761 + 760 + 759 (frame 126) | HIL/64/764 + 763 + 762 (frames 127, 126) | no. 5685, 139 words, Cairo 19 Nov 1912, Ferasudan to Awaid, Port Sudan | about 115 groups; e=m t=x r=w a=y o=v i=g s=b n=d h=h |
| HIL/64/891 + 890 (frame 173) | HIL/64/739 + 738 + 737 (frame 122) | no. 30, 129 words, Railhead 13 July 1912, Armstrong to Herbert Alexandria | 17 groups on two sheets (wave 15's count) |
| HIL/65/157-158 (frame 42) | HIL/65/160 + 159 (frames 42, 43) | no. 499, 107 words, Khartoum 12 May 1913, Phipps to Slatin | 24 groups (wave 15) |
| HIL/65/148 (frame 41) | HIL/65/153 (frame 42) | Erkowit to Stack, 16 May 1913 | about 49 letters (wave 15) |

Frame numbers in the table are 0-based manifest indices. The HIL/64/17 pair corrects wave 15's "no Arabic cipher
seen": there is one Arabic telegram with letter cipher, and its plaintext is beside it.

### Bare cipher telegrams (candidates.json, three)

1. **HIL/64/400** (hil64 frame 67, bottom right). Form G 14, no. 408 (or 458), 57 words, 9 Jan 1909, Khartoum to
   Herbert, Cairo, signed Sirdar. A quoted telegram in clear (a request to admit the son of the late Colonel Hassan
   Bey Tewfik to the Military School), then 8 groups: `Vdugk cesux ybypg eyybp xdwrt jbpef pzyot bpdjv` (the hand
   writes b like a capital B; group 5 fourth letter r or e). Crop: `img/v/region_hil64_067_62_67.jpg`.
   Key material of the same weeks: 64/402 = 403 (3 Jan 1909), 64/239-240 = 118-119 (30 Nov 1908).
2. **HIL/65/273 + 272** (hil65 frame 62). Form G 13, no. 3, 65 words, Siwa 7 June 1913, to Director Sawahil,
   Alexandria. "80. Boxes and effects for Sidi Ahmed have been delivered at Jaghboub stop following obtained by Aisa
   Mayrof and Bash Chawish Farag who went with same Secret ( `aBmbd - xwlmh - bggtc - Fudug - v.t.li - medwd midibi
   -` ) code Jaghboub to receive many notables expected from Egypt one of deserters Mansood Said is not dead but is at
   Nakhaila between Salloom and Derna". Seven groups (the last of six letters as written), dots in the fifth with an
   Arabic word written above it (perhaps "mafqud", missing). The copyist's brackets and the words "Secret ... code"
   mark the run. Crop: `img/v/region_hil65_062_36_02.jpg`.
3. **HIL/65/1122** (hil65 frame 309, left). Form G 13, no. 1796, 42/44 words, Khartoum 26 Feb 1914, to Ferasudan,
   Cairo, signed Malisudan. "672. Aglossa fss 69 over 28 fistularia no objection `wftzk ccuqk knpby xpoyt xuota`
   perhaps not necessary refer question to Dawa as this is continuation of examination but if Kabbud Cairo considers
   this necessary he may obtain authority direct." Five groups after two code words (group 2 fourth letter q or g;
   group 3 second letter n or u). Crop: `img/v/region_hil65_309_05_43.jpg`.

For none of the three was a clear copy found anywhere in HIL/64 or HIL/65 (every frame looked at, with the limits
above). HIL/66 onwards was not searched.

### Handling notes on clear copies (no groups)

64/338 and 64/409 ("Decypher yourself ..."), 64/354 ("Decypher following telegram ... also send him letter cipher"),
65/469 (Baqbaq, 13 Jan 1913, Webb Bowen: "am not in possession of your Cypher had to work it out"), 65/496, 539,
1109 ("Decypher yourself"), 65/901 ("Decipher and hand over following ...", seven sheets, clear), 65/41-42 (wave 15).

### Code-word tally (dictionary code words in clear English; spellings approximate)

About 133 telegrams, all Sudan Government traffic, none in the Coastguard or Sinai telegrams.

- HIL/64/1-400: about 51 forms (list in `notes_hil64_a.md`).
- HIL/64/401-816: 24 (404, 410, 411, 425, 439, 455, 461, 494, 497-498, 522, 523-526, 532, 554, 574, 580, 604,
  605-606, 628, 637, 644, 647, 653, 776, 783).
- HIL/64/817-1007: 2 (904, 917); doubtful 920, 997.
- HIL/65/1-50, 811-1099: 16 (11, 13, 813, 823, 824, 835, 849, 856, 910, 911, 928-929, 961, 964, 966, 984,
  1030-1031); doubtful 912, 1029.
- HIL/65/51-428: 16 (59, 93, 107, 225, 227, 229, 246, 248, 359, 360, 381, 386, 388, 416, 424, 425).
- HIL/65/429-810, 1100-1127: 24 (457, 477, 478, 587, 588, 608, 682-683, 688, 709, 735, 737-741, 757, 764, 783, 793,
  795, 799, 802, 1113, 1117, 1119, 1121, 1122, 1123).

Meanings given on the forms: 64/136 "Fissurum (January) to Flaccidus (March)"; 64/296 "Adulterino (Khedive)" (used
so again on 65/961). Fl... and Fi... words stand where a month or date is expected; A... words stand for persons,
offices or phrases. 65/682-683 and 65/1030-1031 (Naib to Lewa, 1914) are almost wholly code words.

### For a vetting step

- Collate every pair at full resolution and rebuild the alphabets (1907 Arabic, 1908-09, 1912, 1913); try the
  1908-09 alphabet on 64/400 and the May 1913 one on 65/1122. 64/890-891 can be closed the same way.
- 65/273: decide whether the groups are the Coastguard's cipher or a code text brought back from Jaghbub.
- HIL/66 and later units of the Abbas Hilmi telegram files were not opened.
