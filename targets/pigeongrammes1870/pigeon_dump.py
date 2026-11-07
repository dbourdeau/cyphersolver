import openpyxl,sys
def dump(f,maxr=60,maxc=14):
    wb=openpyxl.load_workbook(f,read_only=True,data_only=True)
    for ws in wb:
        print('==',f.split('/')[-1],ws.title,ws.max_row,ws.max_column)
        for i,r in enumerate(ws.iter_rows(values_only=True)):
            if i>=maxr:break
            if any(v is not None for v in r): print(i+1,[v for v in r[:maxc] if v is not None])
if __name__=="__main__":
    dump(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
