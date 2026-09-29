import numpy as np, json, sys
from scipy.linalg import eigh
from scipy.sparse.csgraph import shortest_path, connected_components
D=6

def c4(A):
 B=A.astype(np.int16)@A.astype(np.int16);x=B[np.triu_indices(len(A),1)].astype(np.int64);return int(np.sum(x*(x-1)//2)//2)
def tri(A):return int(np.trace(A.astype(np.int16)@A.astype(np.int16)@A.astype(np.int16))//6)
def metrics(path):
 z=np.load(path,allow_pickle=True);A=z['A'].astype(np.int8);N=len(A)
 E=float(z['E']) if 'E' in z.files else float(z['energy'])
 L=np.eye(N)-A.astype(float)/D;w=eigh(L,eigvals_only=True,check_finite=False)
 ds={}
 for t in (2,3,4,5,6,8,10,12,16):
  zz=np.exp(-t*w);ds[str(t)]=float(2*t*np.dot(w,zz)/zz.sum())
 dist=shortest_path(A,directed=False,unweighted=True)
 balls=[]
 for r in range(1,8):balls.append(float(np.mean(np.sum(dist<=r,axis=1))))
 finite=dist[np.isfinite(dist)&(dist>0)]
 nc,_=connected_components(A,directed=False)
 return dict(path=path,N=N,E=E,degree_min=int(A.sum(1).min()),degree_max=int(A.sum(1).max()),triangles=tri(A),C4N=c4(A)/N,gap=float(w[1]),ds=ds,balls=balls,mean_pair_distance=float(finite.mean()),diameter=int(finite.max()),components=int(nc))
paths=sys.argv[1:]
out=[metrics(p) for p in paths]
for x in out:print(json.dumps(x),flush=True)
open('results/three_size_metrics.json','w').write(json.dumps(out,indent=2))
