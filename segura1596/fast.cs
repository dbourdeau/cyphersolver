using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
class Fast {
 static float[] lp; static int[][] wins; static int A,N; static string alpha; static Random rng=new Random(1596);
 static double Score(int[] k) {double s=0; foreach(int[] w in wins){int x=0;foreach(int t in w)x=x*A+(t<0?-t-1:k[t]);s+=lp[x];}int[] c=new int[A];foreach(int v in k)c[v]++;for(int j=0;j<A;j++)s-=30*Math.Max(0,c[j]-("aeiou".Contains(alpha[j])?3:1));return s;}
 static void Main(string[] args) {
  string dir=args[0]; var lines=File.ReadAllLines(dir+"/input.txt");alpha=lines[0];A=alpha.Length;string[] syms=lines[1].Split(' ');N=syms.Length;
  int[] text=lines[2].Split(' ').Select(int.Parse).ToArray();var ww=new List<int[]>();for(int i=0;i<text.Length-4;i++){var w=text.Skip(i).Take(5).ToArray();if(w.Any(x=>x>=0))ww.Add(w);}wins=ww.ToArray();byte[] b=File.ReadAllBytes(dir+"/lm.bin");lp=new float[b.Length/4];Buffer.BlockCopy(b,0,lp,0,b.Length);
  int runs=int.Parse(args[1]);double best=-1e99;int[] bk=null;
  for(int run=0;run<runs;run++) {int[] k=new int[N];for(int j=0;j<N;j++)k[j]=rng.Next(A);if(run%3==2 && bk!=null){k=(int[])bk.Clone();for(int j=0;j<N/3;j++)k[rng.Next(N)]=rng.Next(A);}double cur=Score(k);
   for(int it=0;it<40000;it++){int i=rng.Next(N),j=rng.Next(N),oi=k[i],oj=k[j];if(rng.NextDouble()<.5){k[i]=oj;k[j]=oi;}else{k[i]=rng.Next(A);}double ns=Score(k),T=4*Math.Pow(.05/4.0,it/40000.0);if(ns>=cur||rng.NextDouble()<Math.Exp((ns-cur)/T))cur=ns;else{k[i]=oi;k[j]=oj;}}
   if(cur>best){best=cur;bk=(int[])k.Clone();Console.WriteLine("RUN "+run+" SCORE "+best);string keys=String.Join(" ",syms.Select((s,j)=>s+"="+alpha[k[j]]));Console.WriteLine(keys);Console.WriteLine(new string(text.Select(t=>t<0?Char.ToUpper(alpha[-t-1]):alpha[k[t]]).ToArray()));File.WriteAllText(dir+"/best.txt",keys+"\n"+best+"\n");}
  }
 }
}
