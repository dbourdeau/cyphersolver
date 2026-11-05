# Internet Culturale sweep (2 Nov 2026) - blocked, 0 rows

Opened my own Chrome tab on `internetculturale.it/it/16/search?q=cifra&__meta_typeTipo=manoscritto&pag=1`. The site
returned "Firewall Captcha Authentication" (arithmetic CAPTCHA). Per CLAUDE.md I did not solve it. No search term was run,
no record read, no web search used (task: re-vet without web search). candidates.json is empty.

Not reached: everything, including the 28,624 full-text hits for "cifra".
To resume: clear the CAPTCHA by hand in a tab on internetculturale.it, then run same-origin fetches at one request per
2-3 s as in research/chrome_pass_2026-11/README.md (`/it/16/search?q=<term>&pag=N`), dropping hits through known.py.
