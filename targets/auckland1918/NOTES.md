# Auckland 1918: Consul-General Winslow and the US Navy, cables on unknown wireless signals (catalogue 757)

Status: read (Brice Dudout, 28 Oct 2026; every word of both cables read, counted in letters: outgoing cable 94 of 94 letters certain; reply 305 of 305 letters read in their sense, 297 certain, 8 restored from their word (6 transmission errors, 2 overstruck letters), 0 unresolved; the final "OK" and the number 17527 are not interpreted; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Published write-up:
https://bdudout.github.io/europe-chiffree/en/documents.html#auckland-1918

## Document

NARA, RG 59, Central Decimal File 1910–29, 763.72/9377 (file unit 763.72/9366–9450, Feb.–Apr. 1918), microfilm M367, roll 83, images 0110–0114: despatch no. 370 (26 Feb.), letter from HMS Philomel (14 Feb.), despatch no. 375 (4 Mar.), copies of both cables.
cable sent 18 February 1918; reply dated 28 February, 10 a.m., received at Auckland 1 March 1918; covering despatch no. 375 of 4 March 1918. Auckland → San Francisco; Washington → Auckland (“via Pacific”).
Sender: Alfred A. Winslow, American Consul-General at Auckland; reply: unnamed office in Washington (“usgovt”), probably the Navy Department. Recipient: the Naval Commander, San Francisco; then the Consul-General at Auckland.
NARA file unit: https://catalog.archives.gov/id/27107744 (images 0110-0114, public domain; not reproduced here).

On 12 February 1918, at 3.50 a.m., a New Zealand station heard an unknown transmitter working “automatic” on 2,000 metres, too fast to read, like Nauru in its German days. The New Zealand naval authorities asked the United States Consul-General whether it was American. Winslow queried San Francisco by cipher cable; the answer came from Washington on 1 March, also in cipher: no, and a suspicious automatic station was being heard in the United States itself. Both cables are in Vigenère, the key being the name of the month: FEBRUARY.

## System and key

Vigenère with the ordinary alphabet, key **FEBRUARY** (the name of the month), the same key for both cables.
The outgoing cable is in 5-letter groups (94 letters); the reply in 10-letter "words" (305 letters) plus the number 17527.

How it was found: on the reply alone, repeats TKUTZMS (distance 104), IFOSRLI (32) and EERMS (56) give a period of 8;
the index of coincidence is 0.062 at period 8; a frequency fit per column gives FEBRUARY. The key was frozen
(SHA-256 a1b7a242...) and applied unchanged to the outgoing cable of 18 February, which had not been used: it gives
94 of 94 letters of continuous English. None of 1,000 shuffles of that ciphertext, decrypted with the same key,
reaches its English letter-frequency score.

## Reading

First published decipherment, to our knowledge. Outgoing cable: 94 letters out of 94, with no correction. Reply: 297 of 305 letters give the text directly; the other 8 are transmission or copying errors (six transmission errors, two overstruck letters), each forced by its word; every word is read. Only the last two letters (“OK”) and the number “17527” stand outside the text.

Files: `transcription.txt`, `decryption.txt` (key under each line, garble table), `reading.md`, `translation.md`, `key.txt`.

## Notes

- The New Zealand question. On 14 February 1918 Staff Paymaster W. J. Brown, for the Naval Adviser to the New Zealand Government (HMS Philomel, Wellington), wrote that a New Zealand station had heard on 11 February at 4.20 p.m. GMT (12 February, 3.50 a.m. NZ time) an unknown station on about 2,000 metres, automatic sending too fast to tell dots from dashes, reminiscent of Nauru “whilst that station was under German control early in the war”. As an American journal reported automatic working being installed between California and Honolulu, he asked for a check by cable.
- The answer is negative, and disturbing. The Americans used no automatic working between Honolulu and San Francisco, and their wavelengths were above 4,000 m: the transmitter heard on 2,000 m was therefore not American. Washington added that a “suspicious” automatic station had been heard in the United States since 15 February on 4,200, 10,000, 11,000 and 15,000 m We have not tried to identify these transmitters.
- “From whence it came”. On 4 March Winslow wrote that he did not know which office the reply came from, “further than it was sent from Washington, D.C.”, and supposed the Navy Department. He does not say he could not read it: the key is the same as for his own cable, and he knew the subject. The State Department noted “A3 – To Navy (by CA)”.
- A makeshift cipher. A Vigenère with a monthly key (the name of the month) gave no security in 1918: the period shows in the repeats (TKUTZMS 104 letters apart, IFOSRLI 32), and the key can be guessed. The State Department had codes (Gray, Green…); these cables show a consul and the Navy, with no common code, making do with an elementary method.
- The errors. Six of the eight are transmission errors, mostly typical confusions of Morse signals (i/t, g/w, z/p, z/x); they do not come from the encipherer. Two letters are overstruck on the Auckland copy (groups 10 and 28). “PERI[O]D”: the encipherer left out an O in the clear (the key stays in step). The final “OK” and the number “17527” are not interpreted.

## Catalogue remark

The catalogue says the reply "could not be read by its recipient". Winslow's despatch of 4 March says only that he did
not know which office in Washington it came from ("I am at a loss to know from whence it came, further than it was sent
from Washington, D.C."); the key is the one he used himself, so he could most likely read it.
