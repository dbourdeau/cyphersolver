// kpb: recover K2 of a double columnar transposition from approximate known plaintext.
// For the right K2, undo(CT,K2) = K1-columnar of PT: adjacent letters are PT letters k1 apart.
// Score = #adjacent pairs of I (over all parts, shared K2) lying in the set of PT pairs at distance k1 (+-tol).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXP 8
#define MAXN 400
int np; char ct[MAXP][MAXN], pt[MAXP][MAXN*2]; int n[MAXP], m[MAXP];
float S[MAXP][26][26];
static unsigned long long rs=88172645463325252ULL;
static inline unsigned long long xr(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static inline int rnd(int k){return xr()%k;}
void undo(const char*c,int len,const int*ord,int k,char*out){
  int rows=(len+k-1)/k, full=len%k?len%k:k, p=0;
  for(int t=0;t<k;t++){int col=ord[t]; int ln=col<full?rows:rows-1; for(int r=0;r<ln;r++) out[r*k+col]=c[p++];}
}
int score(const int*ord,int k2){
  char I[MAXN]; float s=0;
  for(int q=0;q<np;q++){ undo(ct[q],n[q],ord,k2,I);
    for(int t=0;t+1<n[q];t++) s+=S[q][I[t]-'a'][I[t+1]-'a']; }
  return (int)(s*100);
}
int main(int argc,char**argv){
  if(argc<8){fprintf(stderr,"kpb file k1lo k1hi k2lo k2hi iters restarts [tol] [seed] [shufflePT]\n");return 1;}
  FILE*f=fopen(argv[1],"r"); char a[MAXN],b[MAXN*2]; np=0;
  while(fscanf(f,"%s %s",a,b)==2){strcpy(ct[np],a);strcpy(pt[np],b);n[np]=strlen(a);m[np]=strlen(b);np++;}
  int k1lo=atoi(argv[2]),k1hi=atoi(argv[3]),k2lo=atoi(argv[4]),k2hi=atoi(argv[5]);
  long iters=atol(argv[6]); int R=atoi(argv[7]); int tol=argc>8?atoi(argv[8]):0;
  if(argc>9) rs^=atoll(argv[9])*0x9E3779B97F4A7C15ULL;
  int shuf=argc>10?atoi(argv[10]):0;
  if(shuf){ for(int q=0;q<np;q++) for(int i=m[q]-1;i>0;i--){int j=rnd(i+1);char t=pt[q][i];pt[q][i]=pt[q][j];pt[q][j]=t;} }
  int tot=0; for(int q=0;q<np;q++) tot+=n[q]-1;
  for(int k1=k1lo;k1<=k1hi;k1++){
    double dens=0;
    for(int q=0;q<np;q++){ double N[26][26]={{0}}; double pa[26]={0},tk=0;
      for(int j=0;j<m[q];j++) pa[pt[q][j]-'a']++;
      for(int x=0;x<26;x++) pa[x]=(pa[x]+0.1)/(m[q]+2.6);
      for(int d=k1-tol; d<=k1+tol; d++){ double kap = d==k1?1.0:(abs(d-k1)==1?0.5:0.25); 
        for(int j=0;j+d<m[q];j++){ N[pt[q][j]-'a'][pt[q][j+d]-'a']+=kap; tk+=kap; } }
      for(int x=0;x<26;x++)for(int y=0;y<26;y++){ double E=tk*pa[x]*pa[y]; S[q][x][y]=log((N[x][y]+0.5*E+0.01)/(1.5*E+0.01)); if(S[q][x][y]<-1.5)S[q][x][y]=-1.5; }
    }
    for(int k2=k2lo;k2<=k2hi;k2++){
      int best=-1000000000,bord[64];
      for(int r=0;r<R;r++){
        int ord[64]; for(int i=0;i<k2;i++)ord[i]=i; for(int i=k2-1;i>0;i--){int j=rnd(i+1);int t=ord[i];ord[i]=ord[j];ord[j]=t;}
        int cur=score(ord,k2), lb=cur, lord[64]; memcpy(lord,ord,sizeof(int)*k2);
        double T0=getenv("T0")?atof(getenv("T0")):200.0;
        for(long it=0;it<iters;it++){
          double T=T0*(1.0-(double)it/iters)+1.0;
          int no[64]; memcpy(no,ord,sizeof(int)*k2);
          int mv=rnd(3);
          if(mv==0){int i=rnd(k2),j=rnd(k2);int t=no[i];no[i]=no[j];no[j]=t;}
          else if(mv==1){ // swap two grid columns' ranks: i.e., swap values
            int x=rnd(k2),y=rnd(k2); for(int i=0;i<k2;i++){ if(no[i]==x)no[i]=y; else if(no[i]==y)no[i]=x; } }
          else { // move a block of reading order
            int i=rnd(k2),L=1+rnd(k2/2),j=rnd(k2); int tmp[64],c=0; if(i+L>k2)L=k2-i;
            int blk[64]; for(int t=0;t<L;t++)blk[t]=no[i+t];
            for(int t=0;t<k2;t++) if(t<i||t>=i+L) tmp[c++]=no[t];
            if(j>c)j=c; int o=0; for(int t=0;t<j;t++)no[o++]=tmp[t]; for(int t=0;t<L;t++)no[o++]=blk[t]; for(int t=j;t<c;t++)no[o++]=tmp[t]; }
          int s=score(no,k2);
          if(s>=cur || exp((s-cur)/T) > (double)(xr()%1000000)/1e6){cur=s;memcpy(ord,no,sizeof(int)*k2); if(cur>lb){lb=cur;memcpy(lord,ord,sizeof(int)*k2);}}
        }
        if(lb>best){best=lb;memcpy(bord,lord,sizeof(int)*k2);}
      }
      printf("k1=%d k2=%d score=%.3f ord=",k1,k2,best/100.0/tot);
      for(int i=0;i<k2;i++)printf("%d ",bord[i]); printf("\n"); fflush(stdout);
    }
  }
}
