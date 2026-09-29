import numpy as np, sys, json, time, collections

def cycle_rank_by_L(A,Lmax=10):
 N=len(A); neigh=[list(map(int,np.flatnonzero(A[i]))) for i in range(N)]; edges=[tuple(map(int,x)) for x in np.argwhere(np.triu(A,1))]; ei={e:i for i,e in enumerate(edges)};cd=len(edges)-N+1
 piv={}; rank=0; counts=collections.Counter(); ranks={}; cycles=[]
 def add(c):
  nonlocal rank
  bits=0;z=list(c)+[c[0]]
  for u,v in zip(z[:-1],z[1:]): bits ^= (1<<ei[tuple(sorted((u,v)))])
  q=bits
  while q:
   p=q.bit_length()-1
   if p in piv:q^=piv[p]
   else:piv[p]=q;rank+=1;break
 for s in range(N):
  def dfs(path,seen):
   u=path[-1]
   for v in neigh[u]:
    if v==s:
     l=len(path)
     if 4<=l<=Lmax and path[1]<path[-1]: cycles.append(tuple(path));counts[l]+=1
     continue
    if v<=s or v in seen or len(path)>=Lmax:continue
    seen.add(v);path.append(v);dfs(path,seen);path.pop();seen.remove(v)
  for v in neigh[s]:
   if v>s:dfs([s,v],{s,v})
 # sort by length so progression exact
 cycles.sort(key=len)
 piv={};rank=0;byL={}
 for c in cycles:
  add(c);byL[len(c)]=rank
 # fill cumulative
 last=0
 for L in range(4,Lmax+1):
  if L in byL:last=byL[L]
  ranks[L]=last
 return {'N':N,'E':len(edges),'cycle_dim':cd,'counts':dict(counts),'ranks':ranks,'span_L':next((L for L in range(4,Lmax+1) if ranks[L]>=cd),None),'ncycles':len(cycles)}
if __name__=='__main__':
 out=[]
 for spec in sys.argv[1:]:
  label,path=spec.split('=',1);A=np.load(path,allow_pickle=True)['A'].astype(np.int8);t=time.time();r=cycle_rank_by_L(A,10);r['label']=label;r['sec']=time.time()-t;out.append(r);print(json.dumps(r),flush=True)
 open('results/cycle_rank_autonomous.json','w').write(json.dumps(out,indent=2))
