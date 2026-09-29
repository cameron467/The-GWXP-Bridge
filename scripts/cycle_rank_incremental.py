import numpy as np, sys, json, time

def analyze(A,Lcap=9):
 N=len(A);neigh=[list(map(int,np.flatnonzero(A[i]))) for i in range(N)];edges=[tuple(map(int,x)) for x in np.argwhere(np.triu(A,1))];ei={e:i for i,e in enumerate(edges)};cd=len(edges)-N+1;piv={};rank=0;counts={};ranks={}
 def addcycle(c):
  nonlocal rank
  zz=list(c)+[c[0]];q=0
  for u,v in zip(zz[:-1],zz[1:]):q^=1<<ei[tuple(sorted((u,v)))]
  while q:
   p=q.bit_length()-1
   if p in piv:q^=piv[p]
   else:piv[p]=q;rank+=1;return
 for L in range(4,Lcap+1):
  cnt=0;t=time.time()
  for s in range(N):
   def dfs(path,seen):
    nonlocal cnt
    u=path[-1]
    if len(path)==L:
     if s in neigh[u] and path[1]<path[-1]:cnt+=1;addcycle(tuple(path))
     return
    for v in neigh[u]:
     if v<=s or v in seen:continue
     seen.add(v);path.append(v);dfs(path,seen);path.pop();seen.remove(v)
   for v in neigh[s]:
    if v>s:dfs([s,v],{s,v})
  counts[L]=cnt;ranks[L]=rank;print('L',L,'cnt',cnt,'rank',rank,'/',cd,'sec',time.time()-t,flush=True)
  if rank>=cd:break
 return {'N':N,'E':len(edges),'cycle_dim':cd,'counts':counts,'ranks':ranks,'span_L':(max(ranks) if rank>=cd else None)}
if __name__=='__main__':
 label,path=sys.argv[1],sys.argv[2];A=np.load(path,allow_pickle=True)['A'].astype(np.int8);r=analyze(A);r['label']=label;print(json.dumps(r));open(f'results/cycle_rank_{label}.json','w').write(json.dumps(r,indent=2))
