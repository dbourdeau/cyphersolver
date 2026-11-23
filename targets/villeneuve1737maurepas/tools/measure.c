/* Frozen measure (PREREG-0/1): score = 1 - editdist/len(gloss letters) on held-out passages,
   lacunae: '@' gutter gap absorbs 0..15 gloss chars free, '#' gloss lacuna absorbs 0..10 decoded chars free.
   Unknown code -> '*' (never matches). 200 controls = frozen key values shuffled among its codes (Fisher-Yates, LCG seeded). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXP 64
#define MAXC 1000
#define MAXV 16
int NP; int nc[MAXP], ng[MAXP]; int *codes[MAXP]; char *gl[MAXP];
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
double score(char K[][MAXV], int *kn){
  long err=0,len=0;
  for(int p=0;p<NP;p++){int n=0;
    for(int i=0;i<nc[p];i++){int c=codes[p][i];
      if(c==-1){dbuf[n++]='@';continue;}
      if(c<0||!kn[c]){dbuf[n++]='*';continue;}
      for(char*s=K[c];*s;s++) dbuf[n++]=*s;}
    dbuf[n]=0; err+=edit(dbuf,n,gl[p],ng[p]);
    for(int j=0;j<ng[p];j++) if(gl[p][j]!='#') len++;}
  return 1.0-(double)err/len;
}
unsigned long long st;
unsigned rnd(){ st=st*6364136223846793005ULL+1442695040888963407ULL; return (unsigned)(st>>33);}
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"r"); if(fscanf(f,"%d",&NP)!=1) return 1;
  int ngr=0;
  for(int p=0;p<NP;p++){if(fscanf(f,"%d %d",&nc[p],&ng[p])!=2) return 1; codes[p]=malloc(sizeof(int)*nc[p]);
    for(int i=0;i<nc[p];i++){ if(fscanf(f,"%d",&codes[p][i])!=1) return 1; if(codes[p][i]!=-1) ngr++;}
    gl[p]=malloc(ng[p]+2); if(fscanf(f,"%s",gl[p])!=1) return 1;}
  fclose(f);
  int c; char v[64]; FILE*k=fopen(argv[2],"r");
  while(fscanf(k,"%d %63s",&c,v)==2){known[c]=1; if(!strcmp(v,"-")) key[c][0]=0; else strncpy(key[c],v,MAXV-1);}
  fclose(k);
  st=strtoull(argv[3],0,10);
  double s=score(key,known);
  if(argc>4){printf("{\"score_only\": %.4f, \"cipher_groups\": %d}\n",s,ngr); return 0;}
  int ids[MAXC],nk=0; for(c=0;c<MAXC;c++) if(known[c]) ids[nk++]=c;
  static char K2[MAXC][MAXV]; double best=-9, sum=0; static double ctl[200];
  for(int r=0;r<200;r++){
    int perm[MAXC]; for(int i=0;i<nk;i++) perm[i]=i;
    for(int i=nk-1;i>0;i--){int j=rnd()%(i+1); int t=perm[i];perm[i]=perm[j];perm[j]=t;}
    memset(K2,0,sizeof(K2));
    for(int i=0;i<nk;i++) strcpy(K2[ids[i]],key[ids[perm[i]]]);
    ctl[r]=score(K2,known); sum+=ctl[r]; if(ctl[r]>best) best=ctl[r];
  }
  printf("{\"score\": %.4f, \"cipher_groups\": %d, \"best_control\": %.4f, \"mean_control\": %.4f, \"criterion\": \"score>=0.85 and score>=best_control+0.30\", \"pass\": %s}\n",
    s, ngr, best, sum/200, (s>=0.85 && s>=best+0.30)?"true":"false");
  return 0;
}
