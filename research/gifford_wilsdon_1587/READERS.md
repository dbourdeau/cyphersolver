# The two blind readings: what is preserved

The readers' prompts and full returns were not saved as files. They passed between agents as messages inside the Codex app, and its session logs on my machine store those messages only in encrypted form. They cannot be recovered as text. Unlike #827 and #838, this folder therefore has no prompt or return files. What the logs do keep in plain text is below: who read, on which model, when, which image each was shown, and each reader's own one-line status. The only full account of what the readers reported is the coordinating agent's summary, written at 18:17 UTC from their messages. Its wording is the basis of steps 1 and 2 in the [README](README.md).

All times are UTC on 20 November 2026, from the log entries.

| Step | Reader A (`glyphalpha`, gpt-6.1-terra) | Reader B (`modenacont`, gpt-6.2-astra) |
| --- | --- | --- |
| Task received, f. 114 sign crops | 18:12:57 | 18:13:08 |
| Viewed `unknown_left.png`, `unknown_right.png` | 18:13:02 | 18:13:17 |
| Sent its reading to the coordinator | 18:13:14 | 18:13:33 |
| Task received, f. 113 word rows | 18:13:25 | 18:13:40 |
| Viewed `word_rows.png` | 18:13:28 | 18:13:44 and 18:13:50 |
| Sent its reading to the coordinator | 18:13:38 | 18:14:10 |

Each reader saw the two f. 114 crops before the f. 113 crop. Neither was shown `line_detail.png` or `worksheet.png`. Reader A was started for this task with no earlier conversation. Reader B had been started at 18:02 for an unrelated Modena task, with no earlier conversation, and had not met this letter before 18:13. A third reader requested at 18:12:50 never started, because the requested model name did not exist.

Each reader's own status line after sending, as logged (the times are those of the log entries):

- Reader A, 18:13:17: “Completed the independent visual transcription and sent it to the requesting agent.”
- Reader B, 18:13:40: “I sent the two blind readings to the coordinator. Both crops show a curved mark above and to the right of the central graph, separated from it by a visible gap. In the right crop, the mark’s possible attachment to writing above is uncertain.”
- Reader A, 18:13:41: “Sent the independent word-row transcription to the requesting agent, including uncertain readings and adjacent marks.”
- Reader B, received by the coordinator at 18:15:34: “I sent the four sign-and-gloss observations to the coordinator. The second and third glosses have clear terminal dashes. The first gloss and the exact shape of the fourth sign’s raised mark remain uncertain.”

The crops were cut from the Gale State Papers Online images of SP 15/30 ff. 113 and 114 and stay local under that licence. Their SHA-256 hashes:

| File | Cut from | SHA-256 |
| --- | --- | --- |
| `unknown_left.png` | f. 114, first sign, enlarged five times | `2153b03b5f656e55e5af4f0c33ba92d9abb672c00898bfa62d1c5f3fd4cdf35a` |
| `unknown_right.png` | f. 114, second sign, enlarged five times | `0b15efe05aaf6e8cd829c129bc6fc5773edc69e879e07158e079af7cd29ce09c` |
| `word_rows.png` | f. 113, four rows of the word list | `c3b32a68bcf449911c57192faa250d4f10d8f4d493a09e8db43e4c7f8de35cd3` |

So the order of work and the images shown can be checked against the logs, but the content of each reading rests on the coordinator's summary and on my statement.

AI agents did this work; no person has checked it.
