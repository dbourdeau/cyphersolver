# Frame check (George Lasry, 30 Oct 2026)
Worktree: C:\Users\dbour\cypher-leads (not C:\Users\dbour\cypher). Input in_NN.json (<=20 catalogue entries whose images are online but whose
cipher location was never confirmed); write out_NN.json: {"<id>": {...}} incrementally.
Goal per entry: open the exact page/frame/folio the entry names (folio_note, shelfmark, links, ark, decode_ids) and LOOK at it.
Result object:
  {"result": "confirmed" | "no_cipher_at_frame" | "not_found" | "unreachable",
   "href": "direct URL of that specific page/frame (IIIF image URL, viewer URL with page, DECODE RecordsView, etc.)",
   "frame": "folio/frame/canvas label, e.g. 'f. 124r (canvas 128)'",
   "saw": "what is on that page: cipher system (signs/digits/letters), how many lines, whether a decipherment/gloss is written on it, language",
   "note": "optional: the frame that does carry the cipher if the named one does not; metadata errors"}
Rules: "confirmed" only if you saw cipher text on that page yourself. If the named frame has none, say no_cipher_at_frame and, if you can find the
right frame nearby, give it in href/frame/note. Never infer from the description. If you cannot open the images, result "unreachable" with the
blocker in "note". Do not edit catalogue.json. Use Claude in Chrome (mcp__claude-in-chrome__*; load tools in ONE ToolSearch call; read the
chrome-browser skill first). One tab at a time, polite pace, never click CAPTCHAs/checkboxes (ask the user), no logins. Only use tabs you open; close
them. Known routes: Gallica via openapi.bnf.fr IIIF image URLs (canvas ~ folio+4, drifts); BNE bnedigital.bne.es (screenshots); RAH records via
Objeto digital; CEHM viewer URL pattern; Newberry after ~8 s; CONTENTdm /digital/iiif/{alias}/{ptr}/full/1400,/0/default.jpg. Blocked: Abhilekh Patal,
Academia Sinica, LAC viewer, PARES (429), Gale, Besançon reCAPTCHA. Finish all entries; final reply one line per id: result + 8 words.
DECODE (de-crypt.org) full images need a login; thumbnails ~190px are useless. Do not spend time on DECODE-only entries: record nothing for them (leave out of output) unless the entry also links a library viewer.

## DECODE entries (supersedes the DECODE note above)
The user confirmed a DECODE cookie is available. For a DECODE record <id>:
  python C:\Users\dbour\cypher-leads\research\frame_check_2026-10\decode_fetch.py <id> <scratch dir>\decode\r<id> [max pages]
saves full-size page images (view them with the Read tool; they are copyrighted: keep them in the scratchpad, never in the repo). The record page
(saved as rec<id>.htm there) lists the pages; the entry's folio_note says which one. If the output says FORBIDDEN the cookie expired: stop and report.
DECODE images are 10+ MB: shrink with PIL (Image.thumbnail((1800,1800))) into the scratch dir before viewing with Read; crop for detail.
decode_fetch.py only matches TH_*_P<n>.jpg; records with .png thumbnails, unnumbered .jpg or .pdf-only pages need a hand-rolled fetch (see scratchpad scripts from d02).
