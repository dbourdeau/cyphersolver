// Exact exhaustive search with order-independent upper bounds; 200 full shuffled searches.
#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <random>
#include <string>
#include <thread>
#include <vector>
using namespace std;
constexpr int S=201,U=216,L=369,F=8;
struct Entry{int len,first,last;double inside;int known,hit;};
struct Best { double score=-1e100; long long id=-1; };
struct Result {array<Best,S> best; vector<Best> top; long long tested=0,pruned=0;int maxhits=-1,maxdistinct=-1;long long hitid=-1;array<int,5> any{};};
vector<int> values,freq;array<array<int,L>,S> seq;double lp[729],uni[27];vector<Entry> key;int N;array<int,5> smallidx; vector<int> multipliers;vector<array<int,4>> perms;
const char* names[F]={"direct_shift","modular_shift","reverse_digits","digit_permutation","decimal_offsets","split_modular_shift","affine_modular","split_direct_shift"};
int wrap(int x){x%=N;if(x<0)x+=N;return x+1;}
int rev(int x){int y=0;while(x){y=10*y+x%10;x/=10;}return y;}
int smalllo,smallhi,largelo,largehi;
long long countf(int f){if(f==0)return N+1899;if(f==1)return N;if(f==2)return 1;if(f==3)return 24;if(f==4)return 10000;if(f==5)return 1LL*N*N;if(f==6)return 1LL*multipliers.size()*N;return 1LL*(smallhi-smalllo+1)*(largehi-largelo+1);}
void mapping(int f,long long id,int* m){
 int a=0,b=0;if(f==5){a=id/N;b=id%N;}if(f==6){a=multipliers[id/N];b=id%N;}if(f==7){a=smalllo+id/(largehi-largelo+1);b=largelo+id%(largehi-largelo+1);}
 for(int i=0;i<U;i++){int x=values[i],y=0;
 if(f==0)y=x+int(id)-1899;
 else if(f==1)y=wrap(x-1+id);
 else if(f==2)y=rev(x);
 else if(f==3){int ds[4]={x/1000,x/100%10,x/10%10,x%10};for(auto p:perms[id])y=y*10+ds[p];}
 else if(f==4){int pow=1,z=id;for(int j=0;j<4;j++){y+=((x%10+z%10)%10)*pow;x/=10;z/=10;pow*=10;}}
 else if(f==5)y=wrap(x-1+(x<100?a:b));
 else if(f==6)y=wrap(a*(x-1)+b);
 else y=x+(x<100?a:b);
 m[i]=(y>=1&&y<=N)?y:0;
 }
}
void test(int f,long long id,Result& r){
 int m[U],fst[U],lst[U],cf[27]={},cl[27]={};mapping(f,id,m);r.tested++;
 int hits=0;array<int,5> hs{};int distinct=0;
 for(int j=0;j<5;j++){if(key[m[smallidx[j]]].hit){hits++;r.any[j]=1; hs[distinct++]=key[m[smallidx[j]]].hit;}}
 sort(hs.begin(),hs.begin()+distinct);distinct=unique(hs.begin(),hs.begin()+distinct)-hs.begin();
 if(hits>r.maxhits || (hits==r.maxhits && distinct>r.maxdistinct)){r.maxhits=hits;r.maxdistinct=distinct;r.hitid=id;}
 double inside=0;int len=0;
 for(int i=0;i<U;i++){auto &e=key[m[i]];fst[i]=e.first;lst[i]=e.last;cf[e.first]+=freq[i];cl[e.last]+=freq[i];len+=freq[i]*e.len;inside+=freq[i]*e.inside;}
 double bu=0,fu=0,minb=1e100,minf=1e100,maxuni=-1e100;
 for(int a=0;a<27;a++)if(cl[a]){double v=-1e100;for(int b=0;b<27;b++)if(cf[b])v=max(v,lp[a*27+b]);bu+=cl[a]*v;minb=min(minb,v);}
 for(int b=0;b<27;b++)if(cf[b]){double v=-1e100;for(int a=0;a<27;a++)if(cl[a])v=max(v,lp[a*27+b]);fu+=cf[b]*v;minf=min(minf,v);maxuni=max(maxuni,uni[b]);}
 double bound=(inside+min(bu-minb,fu-minf)+maxuni)/len;
 double threshold=1e100;for(auto b:r.best)threshold=min(threshold,b.score);
 threshold=min(threshold,r.top.size()<10?-1e100:r.top.back().score);
 if(bound<threshold-1e-12){r.pruned++;return;}
 for(int s=0;s<S;s++){
  if(bound<r.best[s].score-1e-12 && (s!=0 || r.top.size()>=10 && bound<r.top.back().score))continue;
  auto &sq=seq[s];double total=inside+uni[fst[sq[0]]];int prev=lst[sq[0]];
  for(int j=1;j<L;j++){int cur=sq[j];total+=lp[prev*27+fst[cur]];prev=lst[cur];}
  double score=total/len;
  if(score>r.best[s].score)r.best[s]={score,id};
  if(s==0 && (r.top.size()<10 || score>r.top.back().score)){
   r.top.push_back({score,id});sort(r.top.begin(),r.top.end(),[](Best a,Best b){return a.score>b.score;});if(r.top.size()>10)r.top.pop_back();
  }
 }
}
int main(int argc,char**argv){
 string which=argc>1?argv[1]:"WE028";int threads=argc>2?stoi(argv[2]):8;
 ifstream in("search_input.txt");int n;in>>n;vector<int> cipher(n);for(auto &x:cipher)in>>x;values=cipher;sort(values.begin(),values.end());values.erase(unique(values.begin(),values.end()),values.end());freq.assign(U,0);
 for(int i=0;i<L;i++){seq[0][i]=lower_bound(values.begin(),values.end(),cipher[i])-values.begin();freq[seq[0][i]]++;}
 mt19937 rng(18080220);for(int s=1;s<S;s++){seq[s]=seq[0];shuffle(seq[s].begin(),seq[s].end(),rng);}
 ofstream sh("shuffle_indices_"+which+".txt");for(int s=0;s<S;s++){for(int v:seq[s])sh<<v<<' ';sh<<'\n';}
 for(auto &x:uni)in>>x;for(auto &x:lp)in>>x;int tables;in>>tables;
 while(tables--){string name;in>>name>>N;key.resize(N+1);for(auto &e:key)in>>e.len>>e.first>>e.last>>e.inside>>e.known>>e.hit;if(name==which)break;}
 for(int a=1;a<N;a++)if(gcd(a,N)==1)multipliers.push_back(a);
 array<int,4> p={0,1,2,3};do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
 int sm[]={17,18,38,1,14};for(int j=0;j<5;j++)smallidx[j]=lower_bound(values.begin(),values.end(),sm[j])-values.begin();
 int maxs=0,mins=100,maxl=0,minl=10000;for(int x:values)if(x<100){maxs=max(maxs,x);mins=min(mins,x);}else{maxl=max(maxl,x);minl=min(minl,x);}
 smalllo=1-maxs;smallhi=N-mins;largelo=1-maxl;largehi=N-minl;
 ofstream out("raw_results_"+which+".tsv");out<<setprecision(14);out<<"family\tcontrol\tscore\tid\n";
 ofstream top("top_candidates_"+which+".tsv");top<<setprecision(14)<<"family\tscore\tid\tcoverage\tmapping\n";
 ofstream hit("function_hits_"+which+".tsv");hit<<"family\tmax_hit_groups\tdistinct_target_words\tid\tindividual_possible\n";
 for(int f=0;f<F;f++){
  long long count=countf(f);Result seed; // deterministic evenly spaced seeds, same for all control searches
  int seeds=min(512LL,count);for(int j=0;j<seeds;j++)test(f,j*(count-1)/max(1,seeds-1),seed);
  vector<Result> results(threads,seed);vector<thread> pool;
  cerr<<which<<' '<<names[f]<<" candidates="<<count<<" start\n";
  for(int t=0;t<threads;t++)pool.emplace_back([&,t]{for(long long id=t;id<count;id+=threads)test(f,id,results[t]);});
  for(auto &t:pool)t.join();Result merged;
  for(auto &r:results){for(int s=0;s<S;s++)if(r.best[s].score>merged.best[s].score)merged.best[s]=r.best[s];merged.top.insert(merged.top.end(),r.top.begin(),r.top.end());if(r.maxhits>merged.maxhits || (r.maxhits==merged.maxhits&&r.maxdistinct>merged.maxdistinct)){merged.maxhits=r.maxhits;merged.maxdistinct=r.maxdistinct;merged.hitid=r.hitid;}for(int j=0;j<5;j++)merged.any[j]|=r.any[j];merged.pruned+=r.pruned-seed.pruned;}
  for(int s=0;s<S;s++)out<<names[f]<<'\t'<<s<<'\t'<<merged.best[s].score<<'\t'<<merged.best[s].id<<'\n';out.flush();
  sort(merged.top.begin(),merged.top.end(),[](Best a,Best b){return a.score>b.score;});vector<long long> seen;int m[U];
  for(auto b:merged.top){if(find(seen.begin(),seen.end(),b.id)!=seen.end())continue;seen.push_back(b.id);if(seen.size()>10)break;mapping(f,b.id,m);int known=0;for(int i=0;i<U;i++)known+=freq[i]*key[m[i]].known;top<<names[f]<<'\t'<<b.score<<'\t'<<b.id<<'\t'<<double(known)/L<<'\t';for(int j=0;j<L;j++)top<<m[seq[0][j]]<<',';top<<'\n';}top.flush();
  hit<<names[f]<<'\t'<<merged.maxhits<<'\t'<<merged.maxdistinct<<'\t'<<merged.hitid<<'\t';for(int v:merged.any)hit<<v;hit<<'\n';hit.flush();
  cerr<<which<<' '<<names[f]<<" best="<<merged.best[0].score<<" bound_pruned="<<merged.pruned<<'/'<<count<<" max_function_hits="<<merged.maxhits<<" distinct="<<merged.maxdistinct<<'\n';
 }
}
