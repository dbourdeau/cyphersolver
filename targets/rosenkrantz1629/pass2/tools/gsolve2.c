/* gsolve.c : homophonic solver by simulated annealing with an optional monotone-row constraint
   (letters non-decreasing along each row of the code table) and cascade moves.
   usage: gsolve lm.bin problem.txt cands.txt seed restarts iters T0 T1 chiW freq.txt rowcol.txt|- initkey.txt|-
   problem.txt / cands.txt / lm.bin: as hsolve.c (same files).
   rowcol.txt: one line per symbol "row col" (row -1 = unconstrained).
   initkey.txt: one line per symbol "name letter" (start every restart from this key, perturbed); "-" = random.
   iters 0 = score the init key only.
   Moves: (a) set one symbol to a new letter; with the row constraint, row neighbours that would break the
   order are pushed to the same letter (cascade); (b) swap the letters of two symbols in different rows
   (only if both stay in order).
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#define A 27
#define HH 26
#define MAXS 4096
#define MAXSEG 4096
#define MAXC 256
static float *mainT,*pendT,*un1,*un2,*un3,*un4;
static int NSYM,NSEG,NC;
static char symname[MAXS][16];
static int *symc[MAXS]; static int symnc[MAXS]; static char allowed[MAXS][MAXC];
static int segsa[MAXSEG],segea[MAXSEG],seglen[MAXSEG]; static int *seg[MAXSEG];
static int *symseg[MAXS]; static int symnseg[MAXS]; static int symcount[MAXS];
static char cand[MAXC][8]; static int candlen[MAXC]; static int candl[MAXC][8]; static int isbrk[MAXC]; static double BRK=0, HIPEN=0; static int hassbrk[MAXS];
static double expf_[26]; static int usechi=0; static double chiW=0;
static int key[MAXS],bestkey[MAXS],gbestkey[MAXS],initkey[MAXS]; static int haveinit=0;
static int symrow[MAXS],symcol[MAXS]; static int usemono=0;
static int rowof[MAXS]; static int rowmem[64][256]; static int rown[64]; static int rowpos[MAXS]; static int NROW=0;
static double segscore[MAXSEG];
static long lettercount[26]; static long totletters;
static uint64_t rs;
static inline uint64_t rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double rndu(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }
static int ord(int c){ return (candlen[c]&&!isbrk[c])? cand[c][0] : 0; }   /* order value of a candidate (first letter) */
static double score_run(int *buf,int n,int sa,int ea){
    if(n==0) return 0.0;
    double sc=0; int ctx; int i=0;
    if(sa){ ctx=((HH*A+HH)*A+HH)*A+HH; }
    else {
        sc+=un1[buf[0]]; if(n>1) sc+=un2[buf[0]*26+buf[1]]; if(n>2) sc+=un3[(buf[0]*26+buf[1])*26+buf[2]];
        if(n>3) sc+=un4[((buf[0]*26+buf[1])*26+buf[2])*26+buf[3]];
        i=4; if(n<4){ ctx=0; for(int k=0;k<4-n;k++) ctx=ctx*A+HH; for(int k=0;k<n;k++) ctx=ctx*A+buf[k]; if(ea) sc+=pendT[ctx]; return sc; }
        ctx=((buf[0]*A+buf[1])*A+buf[2])*A+buf[3];
    }
    for(;i<n;i++){ sc+=mainT[(size_t)ctx*26+buf[i]]; ctx=(ctx%(A*A*A))*A+buf[i]; }
    if(ea) sc+=pendT[ctx];
    return sc;
}
static double score_seg(int g){
    int buf[4096]; int n=0; int *s=seg[g]; double sc=0; int sa=segsa[g];
    for(int i=0;i<seglen[g];i++){ int c=key[s[i]];
        if(isbrk[c]){ sc+=score_run(buf,n,sa,1)+BRK; n=0; sa=1; continue; }
        for(int k=0;k<candlen[c];k++) buf[n++]=candl[c][k]; }
    sc+=score_run(buf,n,sa,segea[g]);
    return sc;
}
static double hipen(void){ double x=0; if(HIPEN==0) return 0; for(int s=0;s<NSYM;s++) if(hassbrk[s]&&!isbrk[key[s]]) x+=HIPEN; return x; }
static double chi(void){
    if(!usechi||totletters==0) return 0; double x=0;
    for(int a=0;a<26;a++){ double e=expf_[a]*totletters; if(e<0.02*totletters/26.0) e=0.02*totletters/26.0; double d=lettercount[a]-e; x+=d*d/e; }
    return x;
}
static void addcounts(int s,int c,int sign){ for(int k=0;k<candlen[c];k++){ lettercount[candl[c][k]]+=sign*symcount[s]; } totletters+=sign*symcount[s]*candlen[c]; }
/* change list */
static int chs[MAXS],cho[MAXS],nch;
static int inlist[MAXS];
static void setsym(int s,int c){ if(!inlist[s]){ inlist[s]=1; chs[nch]=s; cho[nch]=key[s]; nch++; } addcounts(s,key[s],-1); key[s]=c; addcounts(s,c,1); }
static void undo(void){ for(int i=nch-1;i>=0;i--){ int s=chs[i]; addcounts(s,key[s],-1); key[s]=cho[i]; addcounts(s,key[s],1); inlist[s]=0; } nch=0; }
static void commit(void){ for(int i=0;i<nch;i++) inlist[chs[i]]=0; nch=0; }
static int mono_ok_all(void){ if(!usemono) return 1; for(int r=0;r<NROW;r++) for(int i=1;i<rown[r];i++) if(ord(key[rowmem[r][i-1]])>ord(key[rowmem[r][i]])) return 0; return 1; }
/* cascade: set s to c, push row neighbours; returns 0 if a pushed symbol cannot take the letter */
static int cascade(int s,int c){
    setsym(s,c);
    if(!usemono||symrow[s]<0) return 1;
    int r=rowof[s], p=rowpos[s];
    for(int i=p+1;i<rown[r];i++){ int t=rowmem[r][i]; if(ord(key[t])>=ord(c)) break; if(!allowed[t][c]) return 0; setsym(t,c); }
    for(int i=p-1;i>=0;i--){ int t=rowmem[r][i]; if(ord(key[t])<=ord(c)) break; if(!allowed[t][c]) return 0; setsym(t,c); }
    return 1;
}
int main(int argc,char**argv){
    if(argc<13){ fprintf(stderr,"usage: gsolve lm prob cands seed restarts iters T0 T1 chiW freq rowcol|- initkey|-\n"); return 1; }
    FILE*f=fopen(argv[1],"rb"); int hdr[2]; if(!f||fread(hdr,4,2,f)!=2){fprintf(stderr,"lm\n");return 1;}
    size_t n4=(size_t)A*A*A*A;
    mainT=malloc(n4*26*4); pendT=malloc(n4*4); un1=malloc(26*4); un2=malloc(676*4); un3=malloc(17576*4); un4=malloc(456976*4);
    if(fread(mainT,4,n4*26,f)!=n4*26||fread(pendT,4,n4,f)!=n4||fread(un1,4,26,f)!=26||fread(un2,4,676,f)!=676||fread(un3,4,17576,f)!=17576||fread(un4,4,456976,f)!=456976){fprintf(stderr,"lm read\n");return 1;}
    fclose(f);
    f=fopen(argv[3],"r"); char line[65536]; NC=0;
    while(fgets(line,sizeof line,f)){ char*p=strtok(line," \t\r\n"); if(!p) continue; if(!strcmp(p,"_")){ cand[NC][0]=0; candlen[NC]=0; } else if(!strcmp(p,"|")){ strcpy(cand[NC],"|"); candlen[NC]=0; isbrk[NC]=1; } else { strncpy(cand[NC],p,7); candlen[NC]=strlen(cand[NC]); for(int k=0;k<candlen[NC];k++) candl[NC][k]=cand[NC][k]-'a'; } NC++; }
    fclose(f);
    f=fopen(argv[2],"r"); if(fscanf(f,"%d %d",&NSYM,&NSEG)!=2) return 1;
    for(int s=0;s<NSYM;s++){ int nc; if(fscanf(f,"%15s %d",symname[s],&nc)!=2) return 1; if(nc==0){ symnc[s]=NC; symc[s]=malloc(NC*sizeof(int)); for(int k=0;k<NC;k++) symc[s][k]=k; } else { symnc[s]=nc; symc[s]=malloc(nc*sizeof(int)); for(int k=0;k<nc;k++) if(fscanf(f,"%d",&symc[s][k])!=1) return 1; } for(int k=0;k<symnc[s];k++) allowed[s][symc[s][k]]=1; }
    for(int s=0;s<NSYM;s++){ hassbrk[s]=0; for(int k=0;k<symnc[s];k++) if(isbrk[symc[s][k]]) hassbrk[s]=1; }
    for(int g=0;g<NSEG;g++){ if(fscanf(f,"%d %d %d",&segsa[g],&segea[g],&seglen[g])!=3) return 1; seg[g]=malloc(seglen[g]*sizeof(int)); for(int i=0;i<seglen[g];i++) if(fscanf(f,"%d",&seg[g][i])!=1) return 1; }
    fclose(f);
    for(int s=0;s<NSYM;s++){ symseg[s]=malloc(NSEG*sizeof(int)); symnseg[s]=0; symcount[s]=0; }
    for(int g=0;g<NSEG;g++) for(int i=0;i<seglen[g];i++){ int s=seg[g][i]; symcount[s]++; if(symnseg[s]==0||symseg[s][symnseg[s]-1]!=g) symseg[s][symnseg[s]++]=g; }
    if(getenv("BRK")) BRK=atof(getenv("BRK")); if(getenv("HIPEN")) HIPEN=atof(getenv("HIPEN"));
    rs=strtoull(argv[4],0,10)*2654435761ULL+88172645463325252ULL; for(int i=0;i<20;i++) rnd();
    int restarts=atoi(argv[5]); long iters=atol(argv[6]); double T0=atof(argv[7]),T1=atof(argv[8]); chiW=atof(argv[9]);
    if(chiW>0){ f=fopen(argv[10],"r"); for(int a=0;a<26;a++) if(fscanf(f,"%lf",&expf_[a])!=1) return 1; fclose(f); usechi=1; }
    for(int s=0;s<NSYM;s++){ symrow[s]=-1; rowof[s]=-1; }
    if(strcmp(argv[11],"-")){ f=fopen(argv[11],"r"); for(int s=0;s<NSYM;s++) if(fscanf(f,"%d %d",&symrow[s],&symcol[s])!=2) return 1; fclose(f); usemono=1;
        int rid[1024]; for(int i=0;i<1024;i++) rid[i]=-1;
        for(int s=0;s<NSYM;s++) if(symrow[s]>=0){ int r=symrow[s]; if(rid[r]<0) rid[r]=NROW++; rowof[s]=rid[r]; }
        for(int r=0;r<NROW;r++){ rown[r]=0; }
        for(int s=0;s<NSYM;s++) if(rowof[s]>=0){ int r=rowof[s]; int i=rown[r]++; rowmem[r][i]=s; }
        for(int r=0;r<NROW;r++){ /* sort by col */ for(int i=1;i<rown[r];i++){ int t=rowmem[r][i],j=i-1; while(j>=0&&symcol[rowmem[r][j]]>symcol[t]){ rowmem[r][j+1]=rowmem[r][j]; j--; } rowmem[r][j+1]=t; } for(int i=0;i<rown[r];i++) rowpos[rowmem[r][i]]=i; }
    }
    if(strcmp(argv[12],"-")){ f=fopen(argv[12],"r"); char nm[64],lt[64]; for(int s=0;s<NSYM;s++) initkey[s]=-1;
        while(fscanf(f,"%63s %63s",nm,lt)==2){ for(int s=0;s<NSYM;s++) if(!strcmp(nm,symname[s])){ for(int c=0;c<NC;c++) if((!strcmp(lt,"_")&&candlen[c]==0&&!isbrk[c])||(!strcmp(lt,"|")&&isbrk[c])||(candlen[c]&&!strcmp(lt,cand[c]))) initkey[s]=c; } }
        fclose(f); haveinit=1; for(int s=0;s<NSYM;s++) if(initkey[s]<0){ fprintf(stderr,"init key missing %s\n",symname[s]); initkey[s]=symc[s][0]; } }
    int free_[MAXS]; int nfree=0; for(int s=0;s<NSYM;s++) if(symnc[s]>1) free_[nfree++]=s;
    double gbest=-1e300;
    for(int r=0;r<restarts;r++){
        memset(lettercount,0,sizeof lettercount); totletters=0;
        for(int s=0;s<NSYM;s++) key[s]= haveinit? initkey[s] : symc[s][rnd()%symnc[s]];
        if(usemono&&!haveinit){ for(int q=0;q<NROW;q++){ /* sort the row's letters */ int n=rown[q]; int L[256]; for(int i=0;i<n;i++) L[i]=key[rowmem[q][i]]; for(int i=1;i<n;i++){ int t=L[i],j=i-1; while(j>=0&&ord(L[j])>ord(t)){ L[j+1]=L[j]; j--; } L[j+1]=t; } for(int i=0;i<n;i++) key[rowmem[q][i]]=L[i]; } }
        if(usemono&&!mono_ok_all()) fprintf(stderr,"warning: start key breaks row order\n");
        for(int s=0;s<NSYM;s++) addcounts(s,key[s],1);
        double cur=0; for(int g=0;g<NSEG;g++){ segscore[g]=score_seg(g); cur+=segscore[g]; }
        double curchi=chi(); cur-=chiW*curchi; double curhp=hipen(); cur-=curhp;
        double best=cur; memcpy(bestkey,key,sizeof(int)*NSYM);
        double T=T0, cool= iters>0? pow(T1/T0,1.0/(double)iters) : 1;
        static double newsc[MAXSEG]; static int touched[MAXSEG]; static int segmark[MAXSEG];
        for(long it=0;it<iters&&nfree>0;it++){
            int s=free_[rnd()%nfree]; nch=0; int okm=1;
            if((rnd()&3)==0&&nfree>1){
                int s2=free_[rnd()%nfree]; if(s2==s||key[s2]==key[s]||!allowed[s][key[s2]]||!allowed[s2][key[s]]||(usemono&&rowof[s]>=0&&rowof[s]==rowof[s2])){ T*=cool; continue; }
                int c1=key[s2],c2=key[s]; setsym(s,c1); setsym(s2,c2);
                if(usemono&&!mono_ok_all()) okm=0;
            } else {
                int newc=symc[s][rnd()%symnc[s]]; if(newc==key[s]){ T*=cool; continue; }
                okm=cascade(s,newc);
            }
            if(!okm){ undo(); T*=cool; continue; }
            int nt=0; double d=0;
            for(int i=0;i<nch;i++){ int q=chs[i]; for(int k=0;k<symnseg[q];k++){ int g=symseg[q][k]; if(segmark[g]) continue; segmark[g]=1; touched[nt]=g; newsc[nt]=score_seg(g); d+=newsc[nt]-segscore[g]; nt++; } }
            for(int k=0;k<nt;k++) segmark[touched[k]]=0;
            double nchi=chi(); d-=chiW*(nchi-curchi); double nhp=hipen(); d-=(nhp-curhp);
            if(d>=0||rndu()<exp(d/T)){ cur+=d; curchi=nchi; curhp=nhp; for(int k=0;k<nt;k++) segscore[touched[k]]=newsc[k]; commit(); if(cur>best){ best=cur; memcpy(bestkey,key,sizeof(int)*NSYM); } }
            else undo();
            T*=cool;
        }
        printf("R %d score %.3f |",r,best); for(int s=0;s<NSYM;s++) printf(" %s=%s",symname[s],isbrk[bestkey[s]]?"|":(candlen[bestkey[s]]?cand[bestkey[s]]:"_")); printf("\n"); fflush(stdout);
        if(best>gbest){ gbest=best; memcpy(gbestkey,bestkey,sizeof(int)*NSYM); }
    }
    memcpy(key,gbestkey,sizeof(int)*NSYM);
    memset(lettercount,0,sizeof lettercount); totletters=0; for(int s=0;s<NSYM;s++) addcounts(s,key[s],1);
    double lmonly=0; for(int g=0;g<NSEG;g++) lmonly+=score_seg(g);
    printf("BEST %.3f (lm %.3f chi %.2f hipen %.1f)\n",gbest,lmonly,chi(),hipen());
    for(int g=0;g<NSEG;g++){ printf("%d\t",g); for(int i=0;i<seglen[g];i++){ int c=key[seg[g][i]]; printf("%s",isbrk[c]?"|":(candlen[c]?cand[c]:"")); } printf("\t%.2f\n",score_seg(g)); }
    return 0;
}
