# Vetting, first run of research/VET.md (13 Nov 2026)

A test of the vetting brief by a project session (cloud container): a fresh agent (Claude Code, model claude-fable-5-2)
standing in for an outside contributor who was not at the keyboard, so no login and no claim issue. Three leads, chosen
with `python research/vet.py --list --online`. `python research/vet.py --check` prints `result: pass`. **Not applied to
`research/leads.json`**: the three leads are being worked on by Brice Dudout (below), and their verdicts follow that work.
The `by` field of the blocks reads "contributor" because the agent was given no handle.

**All three leads were already taken.** The open-issue check was run only after the work (see "What is left"):
issue #535 (lead 2571) and pull requests #536 (2572, 2573) and #539 (2570), all by bdudout on 13 Nov 2026, cover
the same documents. The blocks below rest on what this pass opened itself; where an issue says more, the block says
so and names it.

## Leads

- **2570** Chemnitz (Nuremberg) to Gustav II Adolf, Nov-Dec 1631: `open`. Images 55 and 56 seen at 1800 px, cipher
  passages bare; not in Arkiv II (register of 1631) or Irmer I; not on DECODE. The glossed letter on image 57 gives
  a crib. Pull request #539 already reports a reading in part made from those glosses, so the reviewer may prefer to
  close this against that target instead of promoting it.
- **2571** Gustaf Horn to Gustav II Adolf, Oct-Nov 1630: `read`. Images 78 and 122 carry a contemporary
  decipherment between the lines; image 79, the only bare leaf, is a second copy of the 9 Oct letter on 78. The
  lead's title is wrong. Same finding as issue #535.
- **2572** JACAR C10072242200, Army Ministry draft, 1879: `read`. The clerk's plain kana is written beside the
  cipher kana in every column of frame 1; the JACAR record text runs the two together. Same finding as pull
  request #536.

Count: open 1, read 2.

## Routes

Worked, by curl with a browser User-Agent, no login:

- Riksarkivet images: `https://lbiiif.riksarkivet.se/arkis!R0000795_00078/full/1800,/0/default.jpg` with the Referer
  `https://sok.riksarkivet.se/`. A region is given in pixels (`/x,y,w,h/1900,/`); `pct:` regions answer 501.
- JACAR: `/das/meta/<code>` and `/das/image/<code>` answered 200 (the sweep had met 403); the PDF path is in the
  viewer page's HTML (`/content/item/.../raw/<code>....pdf`).
- DECODE: `RecordsList?search=<term>` and `research/sweep_2026-11-11_german/decode_search.py`; `RecordsView/<id>`.
  The keyword search does not find the key record R4122 under "Horn".
- archive.org `_djvu.txt` full text: Arkiv till upplysning om svenska krigens historia (`arkivtillupplys01mankgoog`
  is vol. II, letters to the king 1630-32) and Irmer vol. I (`dieverhandlungen01irme`).
- Cryptiana over https (`crypto.htm`, `GL.htm`, `meijiarmy.htm`); the pages are Shift_JIS.

Blocked or not tried: gallica.bnf.fr, babel.hathitrust.org and tandfonline.com answered 403 to a probe (none was
needed for these leads).

## What is left

- 2570: Irmer vols. II-III and Soden not opened; the Riksarkivet volume "Agenten Chemnitz brev" named in pull
  request #539 is not digitised; image 58 not opened; the rest of volume R0000624 not paged.
- 2571: images 78 and 79 were not collated group by group; DECODE R4122 not opened.
- 2572: Nagata 1989 and Sasaki 1995 not checked; the sibling lead 2573 not vetted here.
- Not asked, because the contributor was away: which subscriptions or logins they hold (none were needed), their
  handle, and the "Leads from an archive" issue listing 2570, 2571, 2572, which was not opened.
- Page images are in a scratch directory outside the repository; nothing outside this folder was written.
