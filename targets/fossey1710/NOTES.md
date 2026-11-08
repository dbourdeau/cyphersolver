# fossey1710: Thomas Fossey's notebook of veterinary recipes, 1710-1716 (Beinecke GEN MSS VOL 855)

Status: read (8 Nov 2026). Contributed by Harumi-Matsuba (issue #204; repository `Harumi-Matsuba/fossey1710-public`, commit 4197d83, text and data CC BY 4.0, code MIT), who worked with Anthropic Claude and a second reading by Claude Sonnet, Claude Fable and OpenAI Codex. **No human has checked the transcription**, and the project has not seen the images (collections.library.yale.edu is not reachable from here); what the project checked is the files against each other (`VERIFICATION.md`).

## The document

Beinecke Rare Book and Manuscript Library, Yale University, GEN MSS VOL 855, a notebook of farm and veterinary remedies (1710-1716) in which parts of the recipes are written with digits mixed into the English; 76 public IIIF images (https://collections.library.yale.edu/catalog/33569870), cipher digits on 38 of them, 36 transcribed (two show the same leaves with a pasted slip moved). Catalogue 818 (a "test item", importance 1: "Some sections are completed in a cryptographic code"; the ledger already recorded on 28 Oct 2026 that vowels are replaced by digits, so the method was known; the nine-letter key and the full reading are the contributor's).

`transcription.txt` and `reading.txt` consolidate his 36 per-image files (`data/transcription/`, `data/reading/`) with one block per image (his Japanese comment lines are left out); `key.tsv` the key with its evidence, `open_tokens.tsv` and `g9.tsv` the unresolved forms and the 9-or-g places, and `contributor_*.md` his documents (README, method, the list of what stays open, the second reading and its agreement figures, the prior-art search).

## The cipher

Nine common letters of English are replaced by digits, every other letter stands as written: 1 a, 2 e, 3 i, 4 o, 5 u, 6 l, 7 m, 8 n, 9 r (w is written uu; the digit 0 never occurs). The substitution is not applied consistently: 1,295 words with digits stand against 242 without inside the cipher lines. The key is anchored by a plain heading on image 18 ("for a blow in a horses eye to eat of ye Cell") written again in cipher on image 19 ("f49 a b6455 38 a h49s2s ey2").

## Reading, holes and agreement

Of 3,490 cipher symbols (digit occurrences), 3,359 (96.2%) fall in words that make sense; 3,332 of 3,492 (95.4%) if the 13 places where the digit 9 and the letter g are written alike are not resolved in favour of the reading that makes a word. 131 symbols (3.8%, 31 distinct forms) stay open, mostly drug and preparation names, disease names and a few struck-through forms; text hidden under pasted slips is not counted (`contributor_open.md`). Independent second readings, made from the images alone with no sight of the first reading, agree with it on decoded characters at 90.2% to 90.7% over all 36 images (Claude Sonnet) and 91.3% (Codex); the lowest page is image 27 at 70.6% with the lines under pasted slips excluded, and image 70, a page in two columns, first agreed only 66.7% because the readers walked the columns in a different order and 87.5% to 91.7% once a column rule was added.

## Remaining gaps

- Drug names, disease names and personal names whose spelling is not settled (131 symbols, 31 forms; `contributor_open.md`, `open_tokens.tsv`), and the 13 places where 9 and g are written alike - blocker: illegible; the spellings are the writer's own and no reference text fixes them
- Lines hidden under pasted slips (images 25, 27 and 29 to 34) and struck-through lines, which only the original can settle - blocker: needs-physical-access; the lines are not visible in any of the images
- A human check of the transcription against the Beinecke images, and of the 9-or-g and 1-or-long-s places - blocker: needs-physical-access; the project's environment cannot reach collections.library.yale.edu

## Escalation

- [x] siblings: no sibling or neighbouring notebook with the same cipher is known; images 6 to 70 of this volume are the only cipher pages
- [x] clear-pages: the plain heading on image 18 and the plain words inside the cipher lines read and compared; image 70 (pen practice) carries a table of exactly the nine letters
- [x] known-keys: no earlier key; the catalogue's note of vowels as digits is a description of the method, not a key
- [x] print: the contributor searched this ledger, Tomokiyo's unsolved list, Cryptoole and GitHub on 31 Oct and 1 Nov 2026 (`contributor_prior_check.md`): no reading found
- [x] key-rebuild: the key was read from the clear heading repeated in cipher, then every unreadable word was retried with candidate re-readings of the shapes this hand confuses (`contributor_method.md`)
- [x] retry: second readings by three models of different families on every image, with the places of disagreement settled at full resolution by the contributor; the project did not retry them
