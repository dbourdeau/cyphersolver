# Hundred-and-twenty-fourth registered predictions: one combined model

- single components (held-out bits per sign): {'bi': 6.384, 'tri': 5.797, 'role': 5.973, 'pos': 5.429}.

## CM1 the combination beats every part
- combined 4.915 (weights {'bi': 0.0, 'tri': 0.37, 'role': 0.0, 'pos': 0.62}), best single 5.429; threshold 0.3 bit.
- **CM1 holds.**

## CM2 under five bits
- combined 4.915; threshold 5.0.
- **CM2 holds.**

## CM3 genre adds
- with genre 4.911 against 4.915; threshold 0.05.
- **CM3 fails.**

## CM4 position-aware bigram adds
- with position bigram 4.915 against 4.915; threshold 0.05.
- **CM4 fails.**

## CM5 the model transfers to new lines
- F lines absent from A + B (413): 5.690; threshold 5.5.
- **CM5 fails.**

## CM6 the model helps on B
- B bigram 5.903, combined 4.733; threshold 0.5.
- **CM6 holds.**

## CM7 the role part matters
- without role 4.911 against 4.915; threshold 0.10.
- **CM7 fails.**

## CM8 the pos part matters
- without pos 5.258 against 4.915; threshold 0.20.
- **CM8 holds.**

## CM9 the tri part matters
- without tri 5.412 against 4.915; threshold 0.10.
- **CM9 holds.**

## CM10 finer position helps
- five-bucket 5.516, four-way 5.429; threshold 0.1.
- **CM10 fails.**

## Summary

Held: CM1, CM2, CM6, CM8, CM9. Failed: CM3, CM4, CM5, CM7, CM10.
