# Unpublished pages

Pages taken off the site but kept for later. GitHub Pages serves only `docs/`, so nothing here is public.

- `solved.html` ("What has been read, and how"), unpublished 18 Sept 2026. To republish: `git mv unpublished/solved.html docs/`,
  uncomment its `PAGES` entry in `docs/_build_site.py`, restore the links (writeups.html jump bar in `_build_site.py`,
  the catalogue intro in `_catalogue_page.py`, README.md line 16, CATALOGUE.md), and rebuild.
- `fr3029f134/` (BnF fr. 3029 f. 134, "Letter to the King") and `fr3092/` (Duprat at Calais 1521, BnF fr. 3092),
  unpublished 22 Sept 2026 at George Lasry's request: he and a historian have already deciphered and analysed these
  letters for a publication of their own, and a page here, even with attribution, would preempt it. Each folder holds
  the page, its images and its reveal JSON. Do not republish, or send the readings to DECODE (their
  `decode_updates/queue.json` entries carry `skip`), without his word. To republish: move the files back into `docs/`
  (reveal.json to `docs/reveal/<slug>.json`), uncomment the `PAGES` entries and restore the `IMAGES` entries in
  `docs/_build_site.py`, restore the README, SOLVED_CATALOGUE and SOLVED_RANKING rows from git history, and rebuild.
