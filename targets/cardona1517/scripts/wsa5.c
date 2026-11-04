// Joint annealing of a sign alphabet and a code-group -> word assignment (wsa4) plus a class constraint (wsa5):
// code groups with the same initial and final (GCLS lines) should stand for words with the same first letter
// (y = i); each conflicting pair costs PC (env, default 4). Rule read from Lannoy's Naples key (Kolosova 2017).
// usage: wsa model task iters restarts seed [unkcost]
// task: "K S G W N" / N token ids (sign <S, group = S+g) / W lines "len l1 l2 ..." / optional "FIX g w" lines
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 4000
#define MAXW 2000
static float *lp[6]; static int K,S,G,W,N,tok[MAXN],wl[MAXW],wd[MAXW][24],fixg[512],U,ul[256],ud[256][4],NL;
static double HW=1.0; static int gcls[512]; static double PC=4.0; static int NCL=0; static int clsm[512][64], clsn[512]; static int fixs[256]; static int ns[256],ng[512];
static double UNK=-12.0, NUL=-3.0, GNUL=-4.0; static int ALLOWNUL=0;
static unsigned long long rs; static int Y_IX=20, I_IX=8;
static double ur(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return (rs>>11)*(1.0/9007199254740992.0);}
static int ri(int n){return (int)(ur()*n);}
static double score(const int*sm,const int*gw){
  int c[4],cl=0; double s=0;
  #define PUSH(x) do{ if(cl<4) c[cl++]=x; else {c[0]=c[1];c[1]=c[2];c[2]=c[3];c[3]=x;} }while(0)
  #define LP(x) ({ int o=cl+1; long idx=0; for(int q=0;q<cl;q++) idx=idx*K+c[q]; idx=idx*K+(x); lp[o][idx]; })
  for(int i=0;i<N;i++){int t=tok[i];
    if(t<S){int u=sm[t]; if(u==U) s+=NUL; else for(int j=0;j<ul[u];j++){int x=ud[u][j]; s+=LP(x); PUSH(x);}}
    else{int w=gw[t-S]; if(w==W){s+=UNK; cl=0;} else if(w==W+1) s+=GNUL; else for(int j=0;j<wl[w];j++){int x=wd[w][j]; s+=LP(x); PUSH(x);}}
  }
  { static double Nu[300],Mw[MAXW+2]; for(int u=0;u<=U;u++) Nu[u]=0; for(int w=0;w<=W+1;w++) Mw[w]=0;
    for(int q=0;q<S;q++) Nu[sm[q]]+=ns[q];
    for(int g=0;g<G;g++) if(gw[g]!=W) Mw[gw[g]]+=ng[g];
    double e=0; for(int q=0;q<S;q++) if(ns[q]) e+=ns[q]*log(ns[q]/Nu[sm[q]]);
    for(int g=0;g<G;g++) if(gw[g]!=W && ng[g]) e+=ng[g]*log(ng[g]/Mw[gw[g]]);
    s+=HW*e; }
  if(NCL){ int conf=0; for(int c=0;c<NCL;c++){ int n=clsn[c]; for(int i=0;i<n;i++){ int wa=gw[clsm[c][i]]; if(wa>=W) continue; int fa=wd[wa][0]; if(fa==Y_IX) fa=I_IX;
        for(int j=i+1;j<n;j++){ int wb=gw[clsm[c][j]]; if(wb>=W) continue; int fb=wd[wb][0]; if(fb==Y_IX) fb=I_IX; if(fa!=fb) conf++; }}}
    s-=PC*conf; }
  return s;
}
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"rb"); 
  for(int o=1,sz=22;o<=5;o++,sz*=22){lp[o]=malloc(sizeof(float)*sz); fread(lp[o],4,sz,f);} fclose(f);
  f=fopen(argv[2],"r"); fscanf(f,"%d %d %d %d %d",&K,&S,&G,&W,&N);
  for(int i=0;i<N;i++){ fscanf(f,"%d",&tok[i]); if(tok[i]<S) ns[tok[i]]++; else ng[tok[i]-S]++; }
  for(int w=0;w<W;w++){fscanf(f,"%d",&wl[w]); for(int j=0;j<wl[w];j++) fscanf(f,"%d",&wd[w][j]);}
  U=K; for(int u=0;u<K;u++){ul[u]=1;ud[u][0]=u;}
  for(int g=0;g<G;g++) fixg[g]=-1; for(int q=0;q<256;q++) fixs[q]=-1;
  {char kw[8];int g,w; while(fscanf(f,"%7s",kw)==1){
     if(!strcmp(kw,"FIX")){fscanf(f,"%d %d",&g,&w); fixg[g]=w;}
     else if(!strcmp(kw,"FIXS")){fscanf(f,"%d %d",&g,&w); fixs[g]=w;}
     else if(!strcmp(kw,"GCLS")){fscanf(f,"%d %d",&g,&w); if(w+1>NCL) NCL=w+1; clsm[w][clsn[w]++]=g;}
     else if(!strcmp(kw,"UNIT")){fscanf(f,"%d",&ul[U]); for(int j=0;j<ul[U];j++) fscanf(f,"%d",&ud[U][j]); U++;}}}
  fclose(f); NL=K;
  long iters=atol(argv[3]); int R=atoi(argv[4]); rs=atoll(argv[5])*2654435761ULL+1; if(argc>6) UNK=atof(argv[6]); { char*h=getenv("HW"); if(h) HW=atof(h); h=getenv("PC"); if(h) PC=atof(h); } if(argc>7){ALLOWNUL=1; NUL=atof(argv[7]); GNUL=atof(argv[8]);} int KV=U+ALLOWNUL;
  int sm[256],gw[512],bsm[256],bgw[512]; double best=-1e18;
  for(int r=0;r<R;r++){
    for(int s=0;s<S;s++) sm[s]= fixs[s]>=0? fixs[s] : ri(K);
    for(int g=0;g<G;g++) gw[g]= fixg[g]>=0?fixg[g]:W;
    double cur=score(sm,gw), T0=fabs(cur)/N*0.6;
    for(long it=0;it<iters;it++){
      double T=T0*(1.0-(double)it/iters)+0.02;
      int kind=ri(10), a,b,oa,ob; 
      if(kind<6){a=ri(S); if(fixs[a]>=0) continue; oa=sm[a]; sm[a]= (U>K && it>iters/2 && ur()<0.3)? K+ri(U-K) : (ALLOWNUL&&ur()<0.05? U : ri(K)); double ns=score(sm,gw);
        if(ns>=cur||ur()<exp((ns-cur)/T)) cur=ns; else sm[a]=oa;}
      else if(kind<7){a=ri(S);b=ri(S); if(fixs[a]>=0||fixs[b]>=0) continue; oa=sm[a]; sm[a]=sm[b]; sm[b]=oa; double ns=score(sm,gw);
        if(ns>=cur||ur()<exp((ns-cur)/T)) cur=ns; else {sm[b]=sm[a]; sm[a]=oa;}}
      else {a=ri(G); if(fixg[a]>=0) continue; oa=gw[a];
        int r2=ri(4); gw[a]= r2==0? (ALLOWNUL&&ur()<0.5? W+1 : W) : (r2==1? ri(W) : (int)(pow(ur(),3)*W));
        double ns=score(sm,gw);
        if(ns>=cur||ur()<exp((ns-cur)/T)) cur=ns; else gw[a]=oa;}
    }
    printf("restart %d score %.2f per-token %.4f\n",r,cur,cur/N); fflush(stdout);
    if(cur>best){best=cur; memcpy(bsm,sm,sizeof sm); memcpy(bgw,gw,sizeof gw);}
  }
  printf("BEST %.2f\nSM",best); for(int s=0;s<S;s++) printf(" %d",bsm[s]); printf("\nGW"); for(int g=0;g<G;g++) printf(" %d",bgw[g]); printf("\n");
}
