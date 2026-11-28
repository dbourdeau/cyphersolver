/* Recuit simule, substitution simple avec homophones (plusieurs classes -> une lettre).
   usage: sa model.bin lambda restarts iters seed < input
   input: n puis n entiers (classe >=0, -1 = separateur de mot). Ligne 2 : K (nb classes).
   Essaie le sens direct et le sens inverse ; garde le meilleur objectif.
   Objectif = logP(texte) - lambda * (K - nb lettres distinctes utilisees).
   sortie: dir objectif lm_par_symbole puis cle (K entiers 1..28) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define V 29
static float *T; static int n, K, seq[4096], rs[4096];
static unsigned long long rng;
static double urand(void){ rng ^= rng<<13; rng ^= rng>>7; rng ^= rng<<17; return (rng>>11)*(1.0/9007199254740992.0);}
static int irand(int m){ return (int)(urand()*m); }
static double lmscore(const int *s, const int *key){
  int a=0,b=0,c=0; double t=0;
  for(int i=0;i<n;i++){ int d = s[i]<0 ? 0 : key[s[i]]; t += T[((a*V+b)*V+c)*V+d]; a=b;b=c;c=d; }
  t += T[((a*V+b)*V+c)*V+0] * 0; /* pas de fin forcee */
  return t;
}
static int distinct(const int *key){ int u[V]={0},m=0; for(int i=0;i<K;i++) if(!u[key[i]]){u[key[i]]=1;m++;} return m; }
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"rb"); T=malloc(sizeof(float)*V*V*V*V); fread(T,sizeof(float),V*V*V*V,f); fclose(f);
  double lam=atof(argv[2]); int R=atoi(argv[3]); long IT=atol(argv[4]); rng=strtoull(argv[5],0,10)*2654435761ULL+12345;
  if(scanf("%d",&n)!=1) return 1; for(int i=0;i<n;i++) scanf("%d",&seq[i]); scanf("%d",&K);
  for(int i=0;i<n;i++) rs[i]=seq[n-1-i];
  int nsp = 0; for(int i=0;i<n;i++) if(seq[i]>=0) nsp++;
  double bestO=-1e300, bestL=0; int bestK[512], bestDir=0, key[512], cur[512];
  for(int dir=0;dir<2;dir++){ const int *s = dir? rs: seq;
    for(int r=0;r<R;r++){
      for(int i=0;i<K;i++) key[i]=1+irand(28);
      double L=lmscore(s,key), O=L-lam*(K-distinct(key));
      double Tmp=4.0, Tend=0.05, cool=pow(Tend/Tmp,1.0/IT);
      double rO=O; memcpy(cur,key,sizeof(int)*K);
      for(long it=0;it<IT;it++){
        int a=irand(K), old=key[a], b=-1;
        if(urand()<0.3 && K>1){ b=irand(K); int t=key[a]; key[a]=key[b]; key[b]=t; }
        else key[a]=1+irand(28);
        double nL=lmscore(s,key), nO=nL-lam*(K-distinct(key));
        if(nO>=O || urand()<exp((nO-O)/Tmp)){ O=nO; L=nL; if(O>rO){rO=O; memcpy(cur,key,sizeof(int)*K);} }
        else { if(b>=0){ int t=key[a]; key[a]=key[b]; key[b]=t; } else key[a]=old; }
        Tmp*=cool;
      }
      if(rO>bestO){ bestO=rO; memcpy(bestK,cur,sizeof(int)*K); bestDir=dir; bestL=lmscore(s,cur); }
    }
  }
  printf("%d %.4f %.4f\n",bestDir,bestO,bestL/n);
  for(int i=0;i<K;i++) printf("%d ",bestK[i]); printf("\n"); return 0;
}
