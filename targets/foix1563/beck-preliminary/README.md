# Catherine de' Medici to Paul de Foix: proposed partial decipherment

**Lawrence Beck, with the assistance of ChatGPT**  
Photographs, earlier transcriptions and prior source research: **Daniel Bourdeau**

Preliminary review release 1.0, 3 October 2026. Based on audit v0.9 / source-key v13.

## Scope and status

This is an evidence-bearing **proposed partial decipherment for independent review**, not a completed or independently authenticated solution. It concerns only the four encrypted extracts in British Library Add MS 4136, ff.148v-149, DECODE R9241, copied under 15 January 1563. The separately deciphered Coligny material is outside this contribution.

The proposed key produces connected French, including:

> que son but seroit de nous faire entrer en quelque debourssement de deniers, dont nous n'avons nule intention

> that his aim would be to draw us into some expenditure of money, which we have no intention of making

This spans D1:13-D4:12: 75 source units, 90 emitted letters. It does not identify a person, bribe, demand or completed transaction. Its source distinctions and word-code values remain proposed. No exact independent plaintext, authenticated original key, historical priority or verified solved-word percentage is claimed.

## Read the evidence

Start with [the consolidated report](REPORT.md), then [the full French and English reading](FRENCH_AND_ENGLISH.txt), [open questions](OPEN_QUESTIONS.md) and [sources and access limits](SOURCES.md).

The complete key is in `data/key.json`, with additional entry-specific qualifications in `data/key_notes.json`. `data/source.seed.xz` preserves the full source transcription losslessly, including the source IDs and earlier origin mappings. No observations or key values have changed from the frozen research result.

## Reproduce

From this folder, use Python 3 with its standard library:

```text
python scripts/verify.py
python scripts/decode.py
python scripts/decode.py --span D1:13 D4:12 --tokens
```

The decoder restores `data/source.json` from the small template/LZMA seed and checks its original SHA-256. It refuses to overwrite a modified local source. The verifier checks the package hashes, 41 lines, 1,038 current units, 96 labels, 25 unknown occurrences, 1,041 v9 source origins, all three quoted anchors and the complete RX=l rival. It also generates:

```text
KEY_REGISTER.md
data/key_register.json
results/token_replay.json
review.html
```

These derived files make all occurrences, qualifications and proposed expansions inspectable. Open `review.html` locally for the token ledger. Use `data/line_coordinates.json` with separately obtained photographs for handwriting review. The coordinates identify whole-line context, not exact per-sign boxes.

**Passing checks establishes integrity and computational replay, not historical correctness.** This is not an independent rediscovery solver. A valid future correction requires a new version, not protection of the old key merely because it passes its own verifier.

## Remaining problems

RX=mm is preferred provisionally but conflicts at A4; the complete RX=l rival is retained. Codes 26, 34, 70 and 10 and the M/N monograms remain unassigned. Some null families, singletons, numerical boundaries and already-assigned malformed words remain disputed. Do not silently replace those gaps with credit, profit, offered or a historical name.

The last two research audits added tests and source leads, not plaintext. This upload consolidates the existing result and does not announce a further decipherment.

## Public-package boundary and integration

No manuscript photographs, crops, private correspondence, credentials or restricted third-party full texts are included. Reviewers require separately obtained source access to authenticate handwriting; this package grants no image-reuse permission.

This contribution adds only `targets/foix1563/beck-preliminary/`. It does not change Daniel's notes, the parent profile, Coligny results, catalogue statistics, solved status, site templates or generated pages. `SITE_NOTE.md` contains optional introductory wording for use after review. Merging these files does not itself create a live-site page.

Lawrence directed the project; ChatGPT performed the recorded source comparison, computation, interpretation, translations and drafting. Daniel provided the photographs and prior source work. No independent reviewer has yet endorsed the Catherine result. Further work continues.
