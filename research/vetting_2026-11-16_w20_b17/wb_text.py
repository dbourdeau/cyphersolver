import re,html,sys
for n in sys.argv[1:]:
    t=open(n,encoding='utf8',errors='replace').read()
    t=re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',t)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    print('=====',n,len(t)); print(t[:3000])
