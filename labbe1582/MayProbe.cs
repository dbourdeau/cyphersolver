using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
class Segment {
 static Random rng=new Random(1577); static float[] lp; static int A; static string alpha;
 static double Score(int[] k,int[][] g){double s=0;foreach(var z in g){int a=k[z[0]],b=k[z[1]],c=k[z[2]],d=k[z[3]],e=k[z[4]];s+=lp[(((a*A+b)*A+c)*A+d)*A+e];if(a==b&&b==c)s-=6;}return s;}
 static void Main(string[] args){string root=args[0];alpha=File.ReadAllText(root+"/alphabet.txt");A=alpha.Length;byte[] bytes=File.ReadAllBytes(root+"/penta.bin");lp=new float[bytes.Length/4];Buffer.BlockCopy(bytes,0,lp,0,bytes.Length);string[] lines={"330213456.","4316.2523119351351531143556.453236.43136.5315551935431513556.130433021345."};int cycles=args.Length>1?int.Parse(args[1]):7000;
 for(int mode=0;mode<1;mode++){int mask=0;
 var vocab=new List<string>();var seqs=new List<int[]>();int bad=0;
 foreach(string raw in lines){var ts=new List<int>();foreach(string part0 in raw.Split('.')){string part=part0;if(mode==1&&part.EndsWith("6"))part=part.Substring(0,part.Length-1);for(int i=0;i<part.Length;i+=2){string tok=part.Substring(i,Math.Min(2,part.Length-i));if(tok=="6")continue;if(!vocab.Contains(tok))vocab.Add(tok);ts.Add(vocab.IndexOf(tok));}}seqs.Add(ts.ToArray());}
 var seeds=new Dictionary<string,char>{{"33",'m'},{"02",'a'},{"13",'i'},{"45",'s'},{"04",'a'},{"43",'n'},{"16",'e'}};
 if(mode==2)seeds.Clear();
 var full=new List<int>(seqs[0]);foreach(char c in "plusieurs"){string sym="_"+c;if(!vocab.Contains(sym))vocab.Add(sym);seeds[sym]=c;full.Add(vocab.IndexOf(sym));}full.AddRange(seqs[1]);seqs=new List<int[]>{full.ToArray()};
 int n=vocab.Count;if(n<19||n>55||bad>8)continue;var gl=new List<int[]>();foreach(var s in seqs)for(int i=0;i<s.Length-4;i++)gl.Add(s.Skip(i).Take(5).ToArray());int[][] grams=gl.ToArray();double best=-1e20;int[] bk=null;
 for(int restart=0;restart<1000;restart++){int N=Math.Max(A,n)+7;var k=new int[N];string extra="esantirulodcmp";for(int i=0;i<N;i++)k[i]=i<A?i:alpha.IndexOf(extra[(i-A)%extra.Length]);for(int i=N-1;i>0;i--){int j=rng.Next(i+1),t=k[i];k[i]=k[j];k[j]=t;}foreach(var kv in seeds)if(vocab.Contains(kv.Key))k[vocab.IndexOf(kv.Key)]=alpha.IndexOf(kv.Value);double score=Score(k,grams);
 for(int it=0;it<cycles;it++){int a=rng.Next(n),b=rng.Next(N);if(seeds.ContainsKey(vocab[a])||(b<n&&seeds.ContainsKey(vocab[b])))continue;int t=k[a];k[a]=k[b];k[b]=t;double ns=Score(k,grams),temp=2.0*(1.0-it/(double)cycles)+.12;if(ns>=score||rng.NextDouble()<Math.Exp((ns-score)/temp)){score=ns;if(score>best){best=score;bk=(int[])k.Clone();}}else{t=k[a];k[a]=k[b];k[b]=t;}}
 }
 string decode=String.Join("|",seqs.Select(s=>new string(s.Select(t=>alpha[bk[t]]).ToArray())));Console.WriteLine(mode+"\t"+mask+"\t"+(best/grams.Length).ToString("F6",System.Globalization.CultureInfo.InvariantCulture)+"\t"+bad+"\t"+n+"\t"+decode+"\t"+String.Join(",",vocab.Select((v,i)=>v+"="+alpha[bk[i]])));
 }
 }
}
