#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){ FILE*f=fopen("corpus.txt","r"); static double c[456976]; int a[4],k=0,ch; long tot=0;
 while((ch=fgetc(f))!=EOF){ if(ch<'a'||ch>'z')continue; a[0]=a[1];a[1]=a[2];a[2]=a[3];a[3]=ch-'a'; if(++k>=4){c[((a[0]*26+a[1])*26+a[2])*26+a[3]]++;tot++;} }
 float*o=malloc(456976*4); for(int i=0;i<456976;i++) o[i]=log10((c[i]+0.01)/tot);
 FILE*g=fopen("qg.bin","wb"); fwrite(o,4,456976,g); fclose(g); printf("%ld\n",tot); }
