# Unpublished pages

Pages taken off the site but kept for later. GitHub Pages serves only `docs/`, so nothing here is public.

- `solved.html` ("What has been read, and how"), unpublished 18 Sept 2026. To republish: `git mv unpublished/solved.html docs/`,
  uncomment its `PAGES` entry in `docs/_build_site.py`, restore the links (writeups.html jump bar in `_build_site.py`,
  the catalogue intro in `_catalogue_page.py`, README.md line 16, CATALOGUE.md), and rebuild.
- BnF fr. 3029 f. 134 (DECODE R3670) and BnF fr. 3092 ff. 101-107 (DECODE R3699-R3701): withdrawn 22 Sept 2026 at
  George Lasry's request (he and a historian are publishing their own reading). Not kept here: the pages and all
  working files are held locally outside the repository. Only the content-free `profile.json` files remain in the
  target folders. Do not republish without his word.
- `indus.html` (the Indus script and Parpola's decipherment, tested), a draft of 23 Sept 2026 while `indus/` is in
  progress. Figures: `indus_signs.jpg` and `indus_tablets.jpg` are drawn here in the indus-website font;
  `indus_m414.jpg` is cropped from CISI vol. 1 (1987), p. 100 (decide on rights before publishing). To publish:
  `git mv unpublished/indus*.{html,jpg} docs/`, add a `PAGES` entry (st='stuck', stt='attempted, not read') and an
  `IMAGES` entry to `docs/_build_site.py`, record the portrait / reveal / atlas skips in `docs/_explore_skip.json`
  and `"unlinked"` in `docs/keys.json`, add the README row, and rebuild.
