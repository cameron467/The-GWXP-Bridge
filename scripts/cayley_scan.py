import numpy as np, itertools, math, json, sys, time
G=2.;U=.1;KAP=.3;EPS=.025;TAU=5.;D=6

def shapes_for_n(N,maxrank=3):
 out=[]
 out.append((N,))
 for a in range(2,int(np.sqrt(N))+1):
  if N%a==0:
   b=N//a
   if a<=b: out.append((a,b))
 for a in range(2,int(round(N**(1/3)))+2):
  if N%a: continue
  M=N//a
  for b in range(a,int(np.sqrt(M))+1):
   if M%b==0:
    c=M//b
    if b<=c: out.append((a,b,c))
 return out

def coords(shape):
 return np.array(list(itertools.product(*[range(s) for s in shape])),dtype=int)

def neg_tuple(t,shape): return tuple((-int(x))%s for x,s in zip(t,shape))
def flatten_tuple(t,shape):
 idx=0
 for x,s in zip(t,shape): idx=idx*s+x
 return idx

def candidate_generators(shape):
 C=coords(shape); out=[]
 for t in map(tuple,C):
  if all(x==0 for x in t): continue
  nt=neg_tuple(t,shape)
  if nt==t: continue # order 2 => only one neighbor, not allowed for degree-6 pair
  if flatten_tuple(t,shape)<flatten_tuple(nt,shape): out.append(t)
 return out

def precompute(shape):
 K=coords(shape); gens=candidate_generators(shape); N=len(K)
 cos=np.empty((len(gens),N),float)
 for i,g in enumerate(gens):
  phase=np.zeros(N)
  for j,s in enumerate(shape): phase += K[:,j]*g[j]/s
  cos[i]=np.cos(2*np.pi*phase)
 return gens,cos

def eval_batch(cos,trip):
 # trip Bx3 indices
 C1=cos[trip[:,0]];C2=cos[trip[:,1]];C3=cos[trip[:,2]]
 w=(C1+C2+C3)/3.0
 ex=np.exp(G*w)
 tr=-ex.mean(axis=1)
 # each generator pair contributes N undirected edges => capacity/N=sum K_s^2
 k1=(ex*C1).mean(axis=1);k2=(ex*C2).mean(axis=1);k3=(ex*C3).mean(axis=1)
 cap=U*(k1*k1+k2*k2+k3*k3)
 det=-KAP*np.log(EPS+1-w).mean(axis=1)
 tpn=36*np.mean(w**3,axis=1) # triangles per vertex exact (floating integer fraction)
 E=tr+cap+det+TAU*tpn
 # normalized Laplacian gap = second smallest 1-w; equivalently 1-second largest w
 ws=np.sort(w,axis=1)
 gap=1-ws[:,-2]
 return E,tpn,gap

def scan_shape(shape,samples,seed):
 gens,cos=precompute(shape); M=len(gens);rng=np.random.default_rng(seed)
 if M<3:return None
 # random unique triples + exhaustive if cheap
 totalcomb=math.comb(M,3)
 if totalcomb<=samples:
  trip=np.array(list(itertools.combinations(range(M),3)),dtype=int)
 else:
  seen=set(); arr=[]
  # include triples among first min(20,M) canonical low-index gens exhaustively
  q=min(20,M)
  for t in itertools.combinations(range(q),3):seen.add(t);arr.append(t)
  while len(arr)<samples:
   t=tuple(sorted(rng.choice(M,3,replace=False).tolist()))
   if t not in seen:seen.add(t);arr.append(t)
  trip=np.array(arr,dtype=int)
 best=None
 for st in range(0,len(trip),1000):
  b=trip[st:st+1000];E,T,gap=eval_batch(cos,b);ix=int(np.argmin(E));
  cand=(float(E[ix]),float(T[ix]),float(gap[ix]),tuple(map(tuple,[gens[q] for q in b[ix]])))
  if best is None or cand[0]<best[0]:best=cand
 return dict(shape=tuple(int(x) for x in shape),ngen=int(M),tested=int(len(trip)),energy=best[0],tri_per_vertex=best[1],gap=best[2],generators=tuple(tuple(int(y) for y in g) for g in best[3]))

def main(N,samples=30000):
 t=time.time();outs=[]
 for j,sh in enumerate(shapes_for_n(N)):
  x=scan_shape(sh,samples,10000+N*17+j)
  if x:outs.append(x);print(json.dumps(x),flush=True)
 byrank={}
 for x in outs:
  r=len(x['shape']);
  if r not in byrank or x['energy']<byrank[r]['energy']:byrank[r]=x
 print('BESTBYRANK',json.dumps(byrank),flush=True)
 print('BEST',json.dumps(min(outs,key=lambda x:x['energy'])),'elapsed',time.time()-t,flush=True)
 open(f'results/cayley_scan_N{N}.json','w').write(json.dumps(dict(N=N,all=outs,best_by_rank=byrank),indent=2))
if __name__=='__main__':main(int(sys.argv[1]),int(sys.argv[2]) if len(sys.argv)>2 else 30000)
