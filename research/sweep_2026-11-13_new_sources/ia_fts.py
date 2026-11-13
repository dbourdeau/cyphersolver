import json,subprocess,sys,urllib.parse,re
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
def q(query,size=40,frm=0):
    u='https://be-api.us.archive.org/fts/v1/search?'+urllib.parse.urlencode({'q':query,'size':size,'from':frm})
    r=subprocess.run(['curl','-s','-m','60','-A',UA,u],capture_output=True,text=True).stdout
    return json.loads(r)
if __name__=='__main__':
    for qq in sys.argv[1:]:
        d=q(qq)
        h=d['hits']
        print('##',qq,h['total'])
        for x in h['hits']:
            f=x['fields']
            print(x['_id'].split('|')[0][:50],f.get('meta_year'),(f.get('meta_title') or [''])[0][:60],f.get('meta_collection'),'|',' // '.join(x.get('highlight',{}).get('text',[]))[:150].replace('\n',' '))
