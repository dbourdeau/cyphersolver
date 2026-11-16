## What this adds

<!-- Target folder(s), documents covered, and what changed: a reading, a key, a transcription, a correction. -->

## Reading checklist (for any document claimed as read, in full or in part)

A mechanical decryption is not a reading (George Lasry, 22 Oct 2026). For each document:

- [ ] The plaintext is given as **coherent sentences** in the document's own language, holes marked in place
      (`[...]`, `[?word]`, `[47]` for an unidentified code). A few holes; not holes in almost every sentence.
- [ ] An **English translation** of those sentences, with the same holes (not needed if the plaintext is English).
- [ ] The **decryption**, line by line against the **transcription**, both listed in `profile.json` `outcome.texts`
      with the key file in `outcome.key_file`.
- [ ] The decryption is the **unedited output of the key**; every letter or word of the reading that the key does not
      give is marked in the reading (README Conventions, 16 Nov 2026), and every key value used is in a listed key file.
- [ ] A document that decodes but does not yet read is marked `"state": "decoded, not read"`; key sheets, code lists
      and worksheets `"state": "not prose"`.
- [ ] `python docs/_check_reading.py <folder>` run; paste its last line here:

```
```

- [ ] The reading was checked against the images, and the tools used (AI included) are named in NOTES.md.

- [ ] If the key is recovered but the text does not read yet, the method says how the key was obtained and the documents are marked "decoded, not read" (that is a fine state to submit). To go further: let a model complete nomenclator entries and split the decryption into text, check where it stops making sense against the images, fix the transcription or key, repeat (CONTRIBUTING, "From a key to a reading")

## Reviewer, before merging

- [ ] Read each document's reading as sentences against its translation, and three sentences picked at random
      against the images. Record it on each `outcome.texts` entry: `"reading_review": {"grade": "A|B", "by": "...",
      "date": "YYYY-MM-DD", "note": "..."}` (A coherent with scattered holes, B coherent but raw). A document with
      holes in most sentences gets `"state": "decoded, not read"` instead.

## How to credit you

<!-- Full name, initials or a handle, and a link if you like. -->
