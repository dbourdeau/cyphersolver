/* Recuit simule par MOTS (chaines avec separateurs), substitution avec homophones.
   usage: salex lm4_sp.bin lex.bin rho lambda restarts iters seed [mode] < input
   mode 0 (defaut) : score lexical ci-dessous ; mode 1 : logP_4grammes(" w ") pour tout mot, + rho si hors lexique.
   input : n, puis n entiers (classe >=0, -1 = separateur), puis K.
   Score d'un mot w (lettres l1..lk) :
     si w est dans le lexique (compte >= 2) : log((c+0.5)/N)
     sinon : logP_4grammes(" w ") + rho          (rho < 0 = penalite hors lexique)
   Objectif = somme des scores de mots - lambda*(K - lettres distinctes).
   Sens direct et inverse essayes ; le meilleur objectif decide (aucun regard au clair).
   Sortie : dir objectif nb_mots_hors_lexique, puis la cle (K entiers 1..28). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <stdint.h>
#define V 29
#define HS (1<<20)
static float *T; static uint64_t *hk; static float *hv; static double N;
static int n, K, seq[4096], rs[4096];
static int nw, ws[1024], wl[1024];           /* debut et longueur de chaque mot */
static int cw[512][1024], ncw[512];           /* mots contenant chaque classe */
static unsigned long long rng;
static double rho; static int mode;
static double urand(void){ rng ^= rng<<13; rng ^= rng>>7; rng ^= rng<<17; return (rng>>11)*(1.0/9007199254740992.0);}
static int irand(int m){ return (int)(urand()*m); }
static uint64_t mix(uint64_t x){ x^=x>>33; x*=0xff51afd7ed558ccdULL; x^=x>>33; return x; }
static double lexget(uint64_t code){ uint64_t h=mix(code)&(HS-1); while(hk[h]){ if(hk[h]==code) return hv[h]; h=(h+1)&(HS-1);} return 1.0; }
static double wscore(const int *s, int w, const int *key){
  int st=ws[w], L=wl[w]; uint64_t code=1;
  double v=1.0;
  if(L<=12){ for(int i=0;i<L;i++) code=code*32+key[s[st+i]]; v=lexget(code); if(mode==0 && v<=0.0) return v; }
  int a=0,b=0,c=0; double t=0;
  for(int i=0;i<L;i++){ int d=key[s[st+i]]; t+=T[((a*V+b)*V+c)*V+d]; a=b;b=c;c=d; }
  t+=T[((a*V+b)*V+c)*V+0];
  return (v<=0.0) ? t : t+rho;
}
static int distinct(const int *key){ int u[V]={0},m=0; for(int i=0;i<K;i++) if(!u[key[i]]){u[key[i]]=1;m++;} return m; }
static void words_of(const int *s){
  nw=0; int i=0; memset(ncw,0,sizeof(ncw));
  while(i<n){ if(s[i]<0){i++;continue;} int st=i; while(i<n&&s[i]>=0) i++; ws[nw]=st; wl[nw]=i-st;
    for(int j=st;j<i;j++){ int k=s[j]; if(ncw[k]==0||cw[k][ncw[k]-1]!=nw) cw[k][ncw[k]++]=nw; }
    nw++; }
}
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"rb"); T=malloc(sizeof(float)*V*V*V*V); if(fread(T,sizeof(float),V*V*V*V,f)!=V*V*V*V) return 2; fclose(f);
  hk=calloc(HS,8); hv=calloc(HS,4);
  f=fopen(argv[2],"rb"); uint64_t code; float lc; long tot=0; N=0;
  /* lex.bin : paires (uint64 code, float compte) */
  while(fread(&code,8,1,f)==1 && fread(&lc,4,1,f)==1){ N+=lc; tot++; uint64_t h=mix(code)&(HS-1); while(hk[h]) h=(h+1)&(HS-1); hk[h]=code; hv[h]=lc; }
  fclose(f);
  for(int h=0;h<HS;h++) if(hk[h]) hv[h]=(float)log((hv[h]+0.5)/N);
  rho=atof(argv[3]); double lam=atof(argv[4]); int R=atoi(argv[5]); long IT=atol(argv[6]); rng=strtoull(argv[7],0,10)*2654435761ULL+12345; mode = argc>8 ? atoi(argv[8]) : 0;
  if(scanf("%d",&n)!=1) return 1; for(int i=0;i<n;i++) if(scanf("%d",&seq[i])!=1) return 1; if(scanf("%d",&K)!=1) return 1;
  for(int i=0;i<n;i++) rs[i]=seq[n-1-i];
  double bestO=-1e300; int bestK[512], bestDir=0, key[512], cur[512]; static double sc[1024];
  for(int dir=0;dir<2;dir++){ const int *s = dir? rs: seq; words_of(s);
    for(int r=0;r<R;r++){
      for(int i=0;i<K;i++) key[i]=1+irand(28);
      double W=0; for(int w=0;w<nw;w++){ sc[w]=wscore(s,w,key); W+=sc[w]; }
      double O=W-lam*(K-distinct(key)), rO=O; memcpy(cur,key,sizeof(int)*K);
      double Tmp=4.0, Tend=0.05, cool=pow(Tend/Tmp,1.0/IT);
      static double nsc[1024]; static int touched[1024], mark[1024]; int stamp=0; memset(mark,0,sizeof(mark));
      for(long it=0;it<IT;it++){
        int a=irand(K), old=key[a], b=-1;
        if(urand()<0.3 && K>1){ b=irand(K); int t=key[a]; key[a]=key[b]; key[b]=t; }
        else key[a]=1+irand(28);
        stamp++; int nt=0; double dW=0;
        for(int q=0;q<ncw[a];q++){ int w=cw[a][q]; if(mark[w]!=stamp){mark[w]=stamp; touched[nt++]=w;} }
        if(b>=0) for(int q=0;q<ncw[b];q++){ int w=cw[b][q]; if(mark[w]!=stamp){mark[w]=stamp; touched[nt++]=w;} }
        for(int q=0;q<nt;q++){ int w=touched[q]; nsc[w]=wscore(s,w,key); dW+=nsc[w]-sc[w]; }
        double nO=W+dW-lam*(K-distinct(key));
        if(nO>=O || urand()<exp((nO-O)/Tmp)){ O=nO; W+=dW; for(int q=0;q<nt;q++) sc[touched[q]]=nsc[touched[q]]; if(O>rO){rO=O; memcpy(cur,key,sizeof(int)*K);} }
        else { if(b>=0){ int t=key[a]; key[a]=key[b]; key[b]=t; } else key[a]=old; }
        Tmp*=cool;
      }
      if(rO>bestO){ bestO=rO; memcpy(bestK,cur,sizeof(int)*K); bestDir=dir; }
    }
  }
  { const int *s = bestDir? rs: seq; words_of(s); int oov=0; for(int w=0;w<nw;w++) if(wscore(s,w,bestK)>0.0 || 1){ int st=ws[w],L=wl[w]; uint64_t c=1; for(int i=0;i<L;i++) c=c*32+bestK[s[st+i]]; if(L>12||lexget(c)>0.0) oov++; }
    printf("%d %.4f %d\n",bestDir,bestO,oov); }
  for(int i=0;i<K;i++) printf("%d ",bestK[i]); printf("\n"); return 0;
}
