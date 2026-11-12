// k1s: given K2 order (reading order of grid columns), recover K1 by SA on quadgram score of undo(undo(CT,K2),K1) over all parts.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXP 8
#define MAXN 400
int np; char ct[MAXP][MAXN]; int n[MAXP]; char I[MAXP][MAXN]; float *qg;
static unsigned long long rs=88172645463325252ULL;
static inline unsigned long long xr(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static inline int rnd(int k){return xr()%k;}
void undo(const char*c,int len,const int*ord,int k,char*out){
  int rows=(len+k-1)/k, full=len%k?len%k:k, p=0;
  for(int t=0;t<k;t++){int col=ord[t]; int ln=col<full?rows:rows-1; for(int r=0;r<ln;r++) out[r*k+col]=c[p++];}
}
double score(const int*ord,int k1){ double s=0; char P[MAXN];
  for(int q=0;q<np;q++){ undo(I[q],n[q],ord,k1,P); for(int t=0;t+3<n[q];t++) s+=qg[((P[t]-'a')*26+(P[t+1]-'a'))*676+(P[t+2]-'a')*26+(P[t+3]-'a')]; }
  return s; }
int main(int argc,char**argv){
  // args: file(ct lines) k2order(comma) k1lo k1hi iters restarts seed
  qg=malloc(456976*4); FILE*g=fopen("qg.bin","rb"); fread(qg,4,456976,g); fclose(g);
  FILE*f=fopen(argv[1],"r"); char a[MAXN],b[2*MAXN]; np=0; while(fscanf(f,"%s %s",a,b)==2){strcpy(ct[np],a);n[np]=strlen(a);np++;}
  int o2[64],k2=0; char*tk=strtok(argv[2],","); while(tk){o2[k2++]=atoi(tk);tk=strtok(NULL,",");}
  for(int q=0;q<np;q++) undo(ct[q],n[q],o2,k2,I[q]);
  int k1lo=atoi(argv[3]),k1hi=atoi(argv[4]); long iters=atol(argv[5]); int R=atoi(argv[6]); rs^=atoll(argv[7])*0x9E3779B97F4A7C15ULL;
  int tot=0; for(int q=0;q<np;q++) tot+=n[q]-3;
  for(int k1=k1lo;k1<=k1hi;k1++){ double best=-1e18; int bo[64];
    for(int r=0;r<R;r++){ int o[64]; for(int i=0;i<k1;i++)o[i]=i; for(int i=k1-1;i>0;i--){int j=rnd(i+1),t=o[i];o[i]=o[j];o[j]=t;}
      double cur=score(o,k1),lb=cur; int lo[64]; memcpy(lo,o,4*k1);
      for(long it=0;it<iters;it++){ double T=20.0*(1-(double)it/iters)+0.2; int no[64]; memcpy(no,o,4*k1); int mv=rnd(3);
        if(mv==0){int i=rnd(k1),j=rnd(k1),t=no[i];no[i]=no[j];no[j]=t;}
        else if(mv==1){int x=rnd(k1),y=rnd(k1); for(int i=0;i<k1;i++){if(no[i]==x)no[i]=y;else if(no[i]==y)no[i]=x;}}
        else {int i=rnd(k1),L=1+rnd(k1/2),j=rnd(k1),tmp[64],c=0,blk[64]; if(i+L>k1)L=k1-i; for(int t=0;t<L;t++)blk[t]=no[i+t];
          for(int t=0;t<k1;t++) if(t<i||t>=i+L) tmp[c++]=no[t]; if(j>c)j=c; int oo=0; for(int t=0;t<j;t++)no[oo++]=tmp[t]; for(int t=0;t<L;t++)no[oo++]=blk[t]; for(int t=j;t<c;t++)no[oo++]=tmp[t];}
        double s=score(no,k1); if(s>=cur||exp((s-cur)/T)>(double)(xr()%1000000)/1e6){cur=s;memcpy(o,no,4*k1); if(cur>lb){lb=cur;memcpy(lo,o,4*k1);}} }
      if(lb>best){best=lb;memcpy(bo,lo,4*k1);} }
    printf("k1=%d lm=%.3f ord1=",k1,best/tot); for(int i=0;i<k1;i++)printf("%d%s",bo[i],i<k1-1?",":""); printf("\n");
    char P[MAXN]; for(int q=0;q<np;q++){undo(I[q],n[q],bo,k1,P);P[n[q]]=0;printf("  %s\n",P);} fflush(stdout);
  }
}
