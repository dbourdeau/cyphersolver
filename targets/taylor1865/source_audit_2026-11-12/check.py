"""Portable literal checks; no language scoring or semantic acceptance algorithm."""
from pathlib import Path
import argparse,csv,hashlib,json
P=Path(__file__).resolve().parent
KEYS=['COMERETRIBUTION','COMPLETEVICTORY','MANCHESTERBLUFF','THENAVYOURPRIDE','OURNAVYOURPRIDE']
def decrypt(text,key,phase=0):
 out=[];n=phase
 for word in text.split():
  out.append(''.join(chr((ord(c)-ord(key[(n+i)%len(key)]))%26+65) for i,c in enumerate(word)));n+=len(word)
 return ' '.join(out)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--images',type=Path,help='Optional directory containing the three named original JPEGs');args=ap.parse_args()
 rows=list(csv.DictReader((P/'JANUARY.tsv').open(),delimiter='\t'))
 readers=list(csv.DictReader((P/'JANUARY_READERS.tsv').open(),delimiter='\t'))
 assert len(rows)==len(readers)==13
 for row,reading in zip(rows,readers):
  assert row['group']==reading['group']
  phase=int(row['key_phase_0based']);assert (int(row['start_cipher_position'])-1)%15==phase
  for ciphercol,literalcol in [('original','original_decryption'),('reader_A','A_decryption'),('reader_B','B_decryption')]:
   assert decrypt(row[ciphercol],KEYS[1],phase)==row[literalcol]
  assert row['reader_A']==reading['reader_A'] and row['reader_B']==reading['reader_B']
 assert decrypt('ODYXXRO',KEYS[1],2)=='CONTENT'
 old='VEASGW LVWVEW VCG DS FIEX NF LFGH XCYKG MRU THIBJLG WT CJS FX EVWJ JMNCH'
 new='VEASGW LVWVEW VCG DS EIEX NF LFGH XCYKG MRU THIBJLG WT GJS EX FVWJ JMNH'
 expected='TQOOPS SEOUKD NOT BE SENT UO DEMO POLIS AND PORTIRN OF THE ST ORDS BLTO'
 assert len(old.replace(' ',''))==58 and len(new.replace(' ',''))==57
 assert decrypt(new,KEYS[0])==expected
 assert decrypt('EIEX',KEYS[0],17)=='SENT' and decrypt('GJS',KEYS[0],44)=='THE'
 assert decrypt('FIEX',KEYS[0],17)=='TENT'  # the first glyph may be the clerk's F: SENT/TENT is open
 mech=list(csv.DictReader((P/'APRIL_MECHANICAL.tsv').open(),delimiter='\t'))
 assert len(mech)==228
 for row in mech:
  assert row['key'] in KEYS
  assert decrypt(row['cipher'],row['key'],int(row['phase']))==row['literal']
 assert sum(row['message']=='April11_suffix' for row in mech)==225
 for line in (P/'PAYLOAD.sha256').read_text().splitlines():
  expected_sha,name=line.split('  ',1)
  assert hashlib.sha256((P/name).read_bytes()).hexdigest()==expected_sha,name
 if args.images:
  for row in json.loads((P/'SOURCES.json').read_text())['assets']:
   f=args.images/row['path'];assert f.stat().st_size==row['bytes']
   assert hashlib.sha256(f.read_bytes()).hexdigest()==row['sha256'],str(f)
  print('PASS all 3 reacquired original image hashes.')
 print('PASS 13 January groups / 54 cipher letters; CONTENT exact; April10 THE exact, EIEX->SENT / FIEX->TENT (open), 57 revised letters; 225 April11 comparisons reproduced, none accepted in accompanying review. Payload hashes verified.')
 print('April10 literal:',expected)
if __name__=='__main__':main()
