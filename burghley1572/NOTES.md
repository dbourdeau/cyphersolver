# Burghley to Walsingham, 2 Sept 1571 (BL Harley MS 260 ff. 143-145; DECODE R8357; catalogue 128)

Status: no write-up — attempted and closed unread (22 Sept 2026). The letter is clear English except for two short
cipher groups. There is no key on DECODE, from Tomokiyo or in print, and Digges (1655) prints the groups as they stand.
The catalogue entry stays as "attempted, open". DECODE corrections are queued.

## What the record is

DECODE R8357 ("William Burghley", "Scotland", 2 Sep 1572, 6 pp.) is a copy in **Walsingham's embassy letter-book**
(Harley MS 260), not an original. It holds three documents:

- f. 143r top: the end of a Latin paper (the Queen's answer on the Anjou marriage/religion, cf. CSP Foreign ix no. 1974).
- ff. 143r-146r: **Lord Burghley to Francis Walsingham, ambassador in France**, "from Audley End by Walden the second
  day of September 1571", signed "Yor assured frind William Burghley", with a postscript about news from Scotland.
- f. 146r foot: the start of Walsingham's reply "To the right honorable ... the Lord of Burghley".

DECODE metadata to correct:
- Date: **2 Sept 1571**, not 1572. The page heads read "September 1571". The letter covers de Foix's embassy (he left
  4 Sept 1571), Higford, the Duke of Norfolk's secretary, and the money sent in cipher to Lord Herries (the Ridolfi plot).
- Receiver: **Sir Francis Walsingham**, English ambassador in France (Paris); the address is on f. 143r.
- Place: written at **Audley End (Saffron Walden)**, Essex, not "Scotland". Only the postscript mentions Scotland.
- Images are not in reading order: P1 f.143r, P4 f.143v, P2 f.144r, P5 f.144v, P6 f.145r, P3 f.145v (end of the
  letter and date; the pencil number there reads "146").

Printed in full: Dudley Digges, *The Compleat Ambassador* (London, 1655), pp. 123-124 (archive.org
`bim_early-english-books-1641-1700_the-compleat-ambassador_digges-dudley-elder_1655`, OCR line ~11330). CSP Foreign
ix does not calendar it (it has only the Queen's letter of the same date, no. 1974, "Printed by Digges").

## The cipher

The only enciphered passage is on f. 143v (image P4), lines 21-22 (`transcription.txt`, `cipher_groups.txt`):

> … and at the first he found such favourable answers as he accompted the matter his own; to tell you truly the
> **[ʒ368]** is wholly added with a certaine incircumscribible **[45 □477ה ⌐□⌐418]**, and if some of them have
> privately or indirectly impugned the same, … he nor they shall have hereafter a quiet conscience.

Two items: `ʒ368` (a name or noun: the subject of "is wholly added") and `45 □477ה ⌐□⌐418` (a noun after
"incircumscribible", i.e. boundless). The letter mixes numbers (45, 477, 418, 368) and signs (ʒ, □, ה, ⌐), so it is a
numerical nomenclator with sign prefixes and suffixes, not a letter-for-letter alphabet. Digges prints "3/3 68" and
"45 7477 4 28418", undeciphered.

Context guesses (grade I, not a reading): the first item could be "the Queen", "the Council" or "Leicester"
("if some of them" suggests a body of councillors), and the second "affection" or "desire" for the marriage. Nothing
tests them.

## What was tried (22 Sept 2026)

1. **Images.** Downloaded the six DECODE images with the saved cookie. The letter is clear apart from the one line
   above. Images are git-ignored.
2. **Print.** Digges 1655 prints the whole letter, with the cipher undeciphered. CSP Foreign ix (BHO, Sept 1571, 1-15)
   does not calendar it. Tomokiyo's cryptiana "elizabeth" page has no Burghley-Walsingham key for 1570-73.
3. **Known keys.** The Cecil-Norris table (1567-70, Walsingham's predecessor in Paris; see norreys1567) spells words
   letter by letter; this cipher uses numbered code groups. Read with it, `45□477ה⌐□⌐418` gives "p t ? p u u …",
   nonsense. Ruled out.
4. **Siblings.** Harley 260 has eight other DECODE records (R8356, R8358-R8364, 1571-72), all "Non-decrypted, short
   parts encrypted only", with no key record. The Digges OCR of their cipher spots (e.g. "29006 for marriage",
   "22977090", "10875") is garbled. The whole series seems to hold a few dozen isolated groups, too few for a
   ciphertext-only attack on a code.

## Remaining gaps
- f. 143v item 1 `ʒ368` - blocker: no-key-material; single nomenclator group, no key on DECODE, in Tomokiyo or in print
- f. 143v item 2 `45 □477ה ⌐□⌐418` - blocker: no-key-material; code groups with sign affixes, occur once, Digges prints them undeciphered

## Escalation
- [x] siblings: Harley 260 records R8356, R8358-R8364 listed; all non-decrypted, no key record
- [x] clear-pages: all six images viewed; no decipherment or interlinear gloss
- [x] known-keys: Cecil-Norris table (norreys1567) tried, ruled out
- [x] print: Digges 1655 pp. 123-124 (cipher left as is); CSP Foreign ix Sept 1571; Tomokiyo elizabeth page
- [n/a] key-rebuild: two items, no repeats and no crib; nothing to anneal against
- [n/a] retry: nothing was read to retry

What would settle it: the Walsingham-Burghley cipher of 1570-73 (possibly among the cipher keys in TNA SP 106 or
in BL Cotton/Harley), or the original letter if it carries a gloss.
