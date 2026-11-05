# Sweep turin_genoa_naples (2 Nov 2026): 0 rows

Target: online inventories of the Archivi di Stato of Torino, Genova, Napoli and Palermo (cifra/cifrario/cifrata in
Lettere ministri, Negoziazioni, Carte Farnesiane).

Instruction in force: "Re-vet without web search", so no WebSearch or search-engine lookups were used to find portals;
only direct archive hostnames guessed from the institutions' names.

## What happened
- Opened my own Chrome tab. A Google results page was loaded once by mistake (one navigation, nothing read from it) and not repeated.
- archiviodistatotorino.beniculturali.it: Chrome error page (domain does not load).
- archiviodistatotorino.cultura.gov.it and archiviodistatogenova.cultura.gov.it: navigation accepted, but every
  get_page_text / javascript_tool call was refused by the extension ("page navigated to a different domain"), i.e. the page
  redirects off the allowed origin and could not be read.
- Stopped after three failed attempts per the Chrome guidance. No ciphertext or record was seen, so no row was written.
- No CAPTCHA met or touched; no login. About 6 requests in total.

## Terms used
None searched (no inventory reached).

## Not reached
All four archives. Napoli and Palermo hostnames were not tried. Next attempt: find the working inventory portal
(e.g. the Piemonte/Liguria regional archive portals, SIAS/SIUSA, Archivio di Stato di Napoli "Carte Farnesiane" finding aid)
from a link the user supplies, then run the cifra/cifrario/cifrata terms as same-origin fetch calls.
candidates.json is an empty list.
