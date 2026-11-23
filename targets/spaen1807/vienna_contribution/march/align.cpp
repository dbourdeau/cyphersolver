#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
struct Edge { int start, len, label; double prior; int whole; };
struct Row { int lo,hi; vector<int> edges; vector<double> weights; };
using Matrix = vector<vector<double>>;

int main(int argc,char** argv){
    if(argc!=4) return 2;
    ifstream input(argv[1]); int n,m,l,k,q; input>>n>>m>>l>>k>>q;
    const double wholePreference=stod(argv[2]);
    vector<int> codes(n), frequency(k,0);
    for(int& c:codes){input>>c;if(c>=0) frequency[c]++;}
    vector<Edge> edges(q);
    vector<vector<int>> byStart(m+1);
    vector<double> opportunity(l,0);
    for(int j=0;j<q;j++){
        auto& e=edges[j];input>>e.start>>e.len>>e.label>>e.prior>>e.whole;
        if(e.whole) e.prior*=wholePreference;
        opportunity[e.label]+=e.prior;byStart[e.start].push_back(j);
    }
    double sum=accumulate(opportunity.begin(),opportunity.end(),0.0);
    for(double& x:opportunity) x/=sum;
    vector<Row> rows(n+1);
    for(int i=0;i<=n;i++){
        double center=1.0*i*m/n;
        rows[i].lo=max(0,(int)ceil(center-110));rows[i].hi=min(m,(int)floor(center+110));
    }
    for(int i=0;i<n;i++){
        auto& r=rows[i];auto& next=rows[i+1];
        for(int pos=r.lo;pos<=r.hi;pos++) for(int j:byStart[pos]){
            int dest=pos+edges[j].len;
            if(dest>=next.lo && dest<=next.hi)r.edges.push_back(j);
        }
        r.weights.resize(r.edges.size());
    }
    Matrix own(n,vector<double>(l,0)), pooled(k,vector<double>(l,0));
    Matrix forward(n+1,vector<double>(m+1,0)),backward=forward;
    auto scale=[](vector<double>& v){
        double mx=*max_element(v.begin(),v.end());
        if(mx<=0 || !isfinite(mx)) throw runtime_error("No finite alignment");
        for(double& x:v)x/=mx;
    };
    for(int round=0;round<=15;round++){
        for(int i=0;i<n;i++){
            auto& r=rows[i];int code=codes[i];
            vector<double> ratio(l,1);
            if(round && code>=0 && frequency[code]>=2){
                for(int label=1;label<l;label++){
                    double other=max(0.0,pooled[code][label]-own[i][label]);
                    double bayes=(1.7 + other/opportunity[label])/(1.7+frequency[code]-1);
                    ratio[label]=pow(min(220.0,bayes),min(0.94,0.44+0.085*round));
                }
            }
            for(size_t b=0;b<r.edges.size();b++){auto& e=edges[r.edges[b]];r.weights[b]=e.prior*ratio[e.label];}
        }
        if(round==15) break;
        for(auto& v:forward) fill(v.begin(),v.end(),0);
        for(auto& v:backward) fill(v.begin(),v.end(),0);
        forward[0][0]=1;backward[n][m]=1;
        for(int i=0;i<n;i++){
            auto& r=rows[i];
            for(size_t b=0;b<r.edges.size();b++){auto& e=edges[r.edges[b]];forward[i+1][e.start+e.len]+=forward[i][e.start]*r.weights[b];}
            scale(forward[i+1]);
        }
        if(forward[n][m]<=0) throw runtime_error("End unreachable");
        for(int i=n-1;i>=0;i--){
            auto& r=rows[i];
            for(size_t b=0;b<r.edges.size();b++){auto& e=edges[r.edges[b]];backward[i][e.start]+=backward[i+1][e.start+e.len]*r.weights[b];}
            scale(backward[i]);
        }
        for(auto& v:pooled) fill(v.begin(),v.end(),0);
        for(int i=0;i<n;i++){
            auto& v=own[i];fill(v.begin(),v.end(),0);
            if(codes[i]<0 || frequency[codes[i]]<2)continue;
            auto& r=rows[i];
            for(size_t b=0;b<r.edges.size();b++){auto& e=edges[r.edges[b]];v[e.label]+=forward[i][e.start]*r.weights[b]*backward[i+1][e.start+e.len];}
            double z=accumulate(v.begin(),v.end(),0.0);
            if(z<=0)throw runtime_error("Zero posterior");
            for(int j=0;j<l;j++){v[j]/=z;pooled[codes[i]][j]+=v[j];}
        }
    }
    vector<vector<int>> back(n+1,vector<int>(m+1,-1));
    vector<double> prev(m+1,-INFINITY);prev[0]=0;
    for(int i=0;i<n;i++){
        auto& r=rows[i];vector<double> next(m+1,-INFINITY);
        for(size_t b=0;b<r.edges.size();b++){
            int j=r.edges[b];auto& e=edges[j];int dst=e.start+e.len;
            double score=prev[e.start]+log(r.weights[b]);
            if(score>next[dst]){next[dst]=score;back[i+1][dst]=j;}
        }
        prev.swap(next);
    }
    int end=m;vector<int> path(n);
    for(int i=n;i>0;i--){int j=back[i][end];if(j<0)throw runtime_error("Traceback");path[i-1]=j;end=edges[j].start;}
    ofstream out(argv[3]);out<<"ordinal\tstart\tend\tlabel\n";
    for(int i=0;i<n;i++){auto& e=edges[path[i]];out<<i+1<<"\t"<<e.start<<"\t"<<e.start+e.len<<"\t"<<e.label<<"\n";}
}
