using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
class Segment {
 static Random rng=new Random(1577); static float[] lp; static int A; static string alpha;
 static double Score(int[] k,int[][] g){double s=0;foreach(var z in g){int a=k[z[0]],b=k[z[1]],c=k[z[2]],d=k[z[3]];s+=lp[((a*A+b)*A+c)*A+d];if(a==b&&b==c)s-=6;}return s;}
 static void Main(string[] args){string root=args[0];alpha=File.ReadAllText(root+"/alphabet.txt");A=alpha.Length;byte[] bytes=File.ReadAllBytes(root+"/quad.bin");lp=new float[bytes.Length/4];Buffer.BlockCopy(bytes,0,lp,0,bytes.Length);string[] lines=File.ReadAllLines(root+"/runs_digits.txt");int cycles=args.Length>1?int.Parse(args[1]):7000;
 for(int mode=0;mode<2;mode++)for(int mask=1;mask<1024;mask++){
 var vocab=new List<string>();var seqs=new List<int[]>();int bad=0;
 foreach(string raw in lines){string s=mode==0?raw:new string(raw.Reverse().ToArray());var ts=new List<int>();for(int i=0;i<s.Length;){int len=(mask&(1<<(s[i]-'0')))!=0?2:1;if(i+len>s.Length){len=1;bad++;}string tok=s.Substring(i,len);if(mode==1)tok=new string(tok.Reverse().ToArray());if(!vocab.Contains(tok))vocab.Add(tok);ts.Add(vocab.IndexOf(tok));i+=len;}if(mode==1)ts.Reverse();seqs.Add(ts.ToArray());}
 int n=vocab.Count;if(n<19||n>55||bad>8)continue;var gl=new List<int[]>();foreach(var s in seqs)for(int i=0;i<s.Length-3;i++)gl.Add(s.Skip(i).Take(4).ToArray());int[][] grams=gl.ToArray();double best=-1e20;int[] bk=null;
 for(int restart=0;restart<3;restart++){int N=Math.Max(A,n);var k=new int[N];string extra="esantirulodcmp";for(int i=0;i<N;i++)k[i]=i<A?i:alpha.IndexOf(extra[(i-A)%extra.Length]);for(int i=N-1;i>0;i--){int j=rng.Next(i+1),t=k[i];k[i]=k[j];k[j]=t;}double score=Score(k,grams);
 for(int it=0;it<cycles;it++){int a=rng.Next(n),b=rng.Next(N),t=k[a];k[a]=k[b];k[b]=t;double ns=Score(k,grams),temp=2.0*(1.0-it/(double)cycles)+.12;if(ns>=score||rng.NextDouble()<Math.Exp((ns-score)/temp)){score=ns;if(score>best){best=score;bk=(int[])k.Clone();}}else{t=k[a];k[a]=k[b];k[b]=t;}}
 }
 string decode=String.Join("|",seqs.Select(s=>new string(s.Select(t=>alpha[bk[t]]).ToArray())));Console.WriteLine(mode+"\t"+mask+"\t"+(best/grams.Length).ToString("F6",System.Globalization.CultureInfo.InvariantCulture)+"\t"+bad+"\t"+n+"\t"+decode+"\t"+String.Join(",",vocab.Select((v,i)=>v+"="+alpha[bk[i]])));
 }
 }
}
