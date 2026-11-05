"""Build candidates.json for the NYC pass of 4 Nov 2026 (README.md here).

Only items whose cipher is still open after the prior-art check become rows. Closed or known and left out:
Gouverneur Morris to Jay, 1 Jan 1783 (printed with the decipherment in the Papers of John Jay, Office of Finance Cypher
No. 1 = WE006), Robert Morris 1790 (Morris's own transcription of the decoded text), Hay to White 1901-02 (State
Department code; the 1903-04 telegrams are lead 1436), "Russian Consulate Key, 1920" (already cited in the catalogue's
RG 64 entry).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
COL = 'https://findingaids.library.columbia.edu/archives/cul-4079134'
CBH = 'https://findingaids.library.columbia.edu/cbh/1974_002/all/'.replace('columbia', 'nyu')
CHECKED = ('open as far as checked (4 Nov 2026: known.py on names and shelfmark; cryptiana livingst.htm names the Morris-Jay '
           'and Morris-Franklin codes only; web search found no edition or study of these items)')

R = [
 dict(year=1794, date='1794 (May; 23 Aug)',
      title='Duportail → Gouverneur Morris: cypher message sent through Thomas Pinckney, with Morris\'s transcription, and two Pinckney notes enclosing messages in cypher',
      correspondents='General Duportail → Gouverneur Morris, via Thomas Pinckney (London); Thomas Pinckney → Morris',
      place='London / Paris', language='English', region='Americas', period='1701-1800',
      shelfmark='Columbia RBML, Gouverneur Morris papers, 1768-1816, Box 3, items 241, 1094 and 1099',
      folio_note='241: transcription in Morris\'s hand of a cypher message and the message in cypher, 4 p.; 1094: unsigned note, [May 1794?], 1 p. enclosing a message in cypher; 1099: Pinckney, London, 23 Aug 1794, 1 p. enclosing a message in cypher',
      cls='C',
      status='Columbia finding aid (read 4 Nov 2026): item 241 "transcription, in Morris\' hand, of cypher message transmitted to Morris through Thomas Pinckney ... and message in cypher, 4 p."; 1094 and 1099 each "enclosing message in cypher". The wording does not say whether Morris\'s "transcription" is of the cipher groups or of a decipherment. No edition or study of these found.',
      why='Morris was being recalled from Paris in the summer of 1794 and his diary has a gap from January to October 1794; a message from a French officer-engineer sent through Pinckney in London is exactly what that gap lacks. Morris and Pinckney had swapped and lost cyphers in 1793 (Pinckney to Jefferson), so the system may be a Morris-Pinckney cypher.',
      importance=3, solvability=3, difficulty=3,
      score_note='Scored from the Columbia finding aid on 4 Nov 2026 (research/nyc_sweep/); not viewed',
      verify='Order items 241, 1094, 1099 from Columbia RBML (reproductions allowed for research); compare the Founders Online Pinckney letters of 1793 for the cypher.',
      links=[{'label': 'Gouverneur Morris papers, Columbia', 'href': COL}],
      seen='catalogue', source='Columbia finding aids sweep (Chrome)', prior_art=CHECKED,
      needs_archive_scan='yes', access_note='Reading-room item at Columbia RBML; request by box and individual item numbers; no scan found online', decode_ids=[]),
 dict(year=1803, date='1803',
      title='Robert R. Livingston (Paris) → his brother: letter on the Louisiana negotiations, "partly in cipher handwriting"',
      correspondents='Robert R. Livingston → his brother',
      place='Paris', language='English', region='Americas', period='1801-1900',
      shelfmark='Center for Brooklyn History, Mid-Atlantic early manuscripts collection 1974.002, Box 1, Folder 25',
      folio_note='one letter in a mixed folder; gift of Dr A. S. Hunt, date unknown',
      cls='C',
      status='Finding aid (read 4 Nov 2026): "1803 letter from Robert R. Livingston at Paris to his brother re: negotiations for the Louisiana purchase, mentions James Monroe and Talleyrand, partly in cipher handwriting." Ambiguous: it may mean cipher or only a cursive hand. Livingston\'s State Department number code of 12 April 1803 (to Madison) is known and printed.',
      why='Livingston and Monroe at Paris in the weeks of the purchase; a private cipher to a brother would show what he kept out of dispatches. Weak: the note may describe handwriting.',
      importance=2, solvability=2, difficulty=3,
      score_note='Scored from the Brooklyn History finding aid on 4 Nov 2026 (research/nyc_sweep/); not viewed',
      verify='Ask Brooklyn History for the folder; check whether the numbers match the State Department code of the Madison letter.',
      links=[{'label': 'Finding aid', 'href': 'https://findingaids.library.nyu.edu/cbh/1974_002/all/'}],
      seen='catalogue', source='NYU special collections sweep (Chrome)', prior_art=CHECKED,
      needs_archive_scan='yes', access_note='Reading-room item at Center for Brooklyn History; no scan found online', decode_ids=[]),
]

json.dump(R, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'rows')
