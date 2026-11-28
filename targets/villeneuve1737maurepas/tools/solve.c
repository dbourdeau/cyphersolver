/* coordinate-ascent key fitting: minimise edit distance between decoded passages and gloss.
   '@' (gutter gap) absorbs 0..15 gloss chars free; '#' in gloss absorbs 0..10 decoded chars free. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXP 400
#define MAXC 1000
#define MAXV 16
int NP; int nc[MAXP], ng[MAXP]; int *codes[MAXP]; char *gl[MAXP]; int has[MAXP][MAXC];
char key[MAXC][MAXV]; int known[MAXC];
static char dbuf[40000];
int edit(const char*d,int n,const char*g,int m){
  static int *T=NULL; static long cap=0; long W=m+1;
  if((n+1)*W>cap){cap=(n+1)*W; T=realloc(T,sizeof(int)*cap);}
  for(long i=0;i<(n+1)*W;i++) T[i]=1<<29;
  T[0]=0;
  for(int i=0;i<=n;i++) for(int j=0;j<=m;j++){
    int v=T[i*W+j]; if(v>=1<<29) continue;
    if(i<n && d[i]=='@'){ for(int k=0;k<=15 && j+k<=m;k++){ if(k>0 && g[j+k-1]=='#') break; if(T[(i+1)*W+j+k]>v) T[(i+1)*W+j+k]=v;} continue;}
    if(j<m && g[j]=='#'){ for(int k=0;k<=10 && i+k<=n;k++){ if(k>0 && d[i+k-1]=='@') break; if(T[(i+k)*W+j+1]>v) T[(i+k)*W+j+1]=v;} continue;}
    if(i<n && T[(i+1)*W+j]>v+1) T[(i+1)*W+j]=v+1;
    if(j<m && T[i*W+j+1]>v+1) T[i*W+j+1]=v+1;
    if(i<n&&j<m){int c=v+(d[i]==g[j]?0:1); if(T[(i+1)*W+j+1]>c) T[(i+1)*W+j+1]=c;}
  }
  return T[n*W+m];
}
int pscore(int p){
  int n=0;
  for(int i=0;i<nc[p];i++){int c=codes[p][i];
    if(c==-1){dbuf[n++]='@';continue;}
    if(c<0||c>=MAXC||!known[c]){dbuf[n++]='*';continue;}
    for(char*s=key[c];*s;s++) dbuf[n++]=*s;}
  dbuf[n]=0; return edit(dbuf,n,gl[p],ng[p]);
}
int cur[MAXP];
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"r"); if(fscanf(f,"%d",&NP)!=1) return 1;
  for(int p=0;p<NP;p++){if(fscanf(f,"%d %d",&nc[p],&ng[p])!=2) return 1; codes[p]=malloc(sizeof(int)*nc[p]);
    for(int i=0;i<nc[p];i++){ if(fscanf(f,"%d",&codes[p][i])!=1) return 1; if(codes[p][i]>=0) has[p][codes[p][i]]=1;}
    gl[p]=malloc(ng[p]+2); if(fscanf(f,"%s",gl[p])!=1) return 1;}
  fclose(f);
  int c; char v[64];
  FILE*k=fopen(argv[2],"r");
  if(k){ while(fscanf(k,"%d %63s",&c,v)==2){known[c]=1; if(!strcmp(v,"-")) key[c][0]=0; else strncpy(key[c],v,MAXV-1);} fclose(k);}
  int sweeps=atoi(argv[3]); static int fixedc[MAXC]; if(argc>5){FILE*fx=fopen(argv[5],"r"); int z; while(fscanf(fx,"%d",&z)==1) fixedc[z]=1; fclose(fx);}
  int tot=0; for(int p=0;p<NP;p++){cur[p]=pscore(p); tot+=cur[p];}
  fprintf(stderr,"init %d\n",tot);
  static char cands[6000][MAXV];
  for(int s=0;s<sweeps;s++){
    int changed=0;
    for(c=0;c<MAXC;c++){
      int occ=0; for(int p=0;p<NP;p++) if(has[p][c]) occ=1;
      if(!occ||fixedc[c]) continue;
      int ncand=0; if(c==318) strcpy(cands[ncand++],"");
      for(int p=0;p<NP;p++) if(has[p][c]) for(int i=0;i<nc[p];i++) if(codes[p][i]==c){
        int pos=(int)((double)i/nc[p]*ng[p]);
        for(int a=pos-30;a<pos+30;a++){ if(a<0||a>=ng[p]) continue;
          for(int l=1;l<=6&&a+l<=ng[p];l++){ char t[MAXV]; strncpy(t,gl[p]+a,l); t[l]=0; if(strchr(t,'#')) break;
            int dup=0; for(int q=0;q<ncand;q++) if(!strcmp(cands[q],t)){dup=1;break;}
            if(!dup && ncand<6000) strcpy(cands[ncand++],t);} } }
      int base=0; for(int p=0;p<NP;p++) if(has[p][c]) base+=cur[p];
      int bestsc=base; char best[MAXV]; strcpy(best,key[c]);
      char save[MAXV]; strcpy(save,key[c]); int sk=known[c];
      for(int q=0;q<ncand;q++){
        strcpy(key[c],cands[q]); known[c]=1;
        int sc=0; for(int p=0;p<NP;p++) if(has[p][c]){sc+=pscore(p); if(sc>=bestsc) break;}
        if(sc<bestsc){bestsc=sc; strcpy(best,cands[q]);}
      }
      if(bestsc<base){strcpy(key[c],best); known[c]=1; changed++; for(int p=0;p<NP;p++) if(has[p][c]) cur[p]=pscore(p);}
      else {strcpy(key[c],save); known[c]=sk;}
    }
    tot=0; for(int p=0;p<NP;p++) tot+=cur[p];
    fprintf(stderr,"sweep %d changed %d total %d\n",s,changed,tot);
    FILE*o=fopen(argv[4],"w");
    for(int cc2=0;cc2<MAXC;cc2++) if(known[cc2]) fprintf(o,"%d %s\n",cc2,key[cc2][0]?key[cc2]:"-");
    fclose(o);
    if(!changed) break;
  }
  int gt=0; for(int p=0;p<NP;p++) gt+=ng[p];
  fprintf(stderr,"final %d over %d gloss chars\n",tot,gt);
  return 0;
}
