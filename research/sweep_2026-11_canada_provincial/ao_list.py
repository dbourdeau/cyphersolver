import re,html,sys,subprocess,time,json
def txt(h):
    t=re.sub(r"<script.*?</script>","",h,flags=re.S);t=re.sub(r"<[^>]+>"," ",t);return html.unescape(re.sub(r"\s+"," ",t))
def items(h):
    t=txt(h)
    parts=re.split(r"DESCRIPTION_WEB \S[^ ]*(?: [^ ]+)*? \d{4,7} DESCRIPTION ",t)
    return parts[1:]
if __name__=="__main__":
    for k in sys.argv[1:]:
        h=open("ao_%s.html"%k,encoding="utf8").read()
        print("##",k)
        for p in items(h): print("  -",p[:420])
