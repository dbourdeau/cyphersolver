from pathlib import Path
import json,csv,sys
base=Path(__file__).resolve().parent
# Post-test editorial language judgments; integers exhaust the original signs in each proposed word.
segments=[
 [(7,'abstenerse','sure'),(1,'de','sure'),(4,'hacer','sure'),(6,'indicaciones','sure')],
 [(5,'[¿castigo?]','conjecture'),(6,'[¿impuesto?]','conjecture')],
 [(7,'individuos','sure')],
 [(1,'por','sure'),(1,'el','sure'),(1,'general','sure')],
 [(4,'proceder','sure'),(1,'con','sure'),(6,'energía','sure')],
 [(7,'individuos','sure'),(4,'h[…]','unresolved')],
 [(5,'[…]diciosa','unresolved')],
 [(1,'[¿no?]','uncertain page-edge boundary')],
 [(2,'[¿hará?]','would require h')],
 [(6,'sorprender','sure')],
 [(3,'ellos','sure')],
 [(7,'[¿vigilancia?]','conjecture')],
 [(3,'sobre','sure')],
 [(2,'[¿son?]','conjecture'),(2,'[¿más?]','uncertain boundaries'),(6,'[¿peligrosos?]','conjecture')]]
if __name__=='__main__':
    results=json.loads((base/'may19.json').read_text());runs=[r.split() for r in (base/'may19.runs').read_text().splitlines()]
    w=csv.writer(sys.stdout,delimiter='\t',lineterminator='\n')
    w.writerow(['run','proposed_word','groups','original_key_emissions','literal_joined','editorial_reading','status'])
    for n,(tokens,parts,words) in enumerate(zip(runs,results['emissions'],segments),1):
        pos=0
        for j,(size,reading,status) in enumerate(words,1):
            take=slice(pos,pos+size);vals=parts[take]
            w.writerow([n,j,' '.join(tokens[take]),' · '.join(vals),''.join(vals),reading,status]);pos+=size
        assert pos==len(tokens)
