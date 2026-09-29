import numpy as np, scipy.linalg as la, sys, time
G=2.;U=.1;KAP=.3;EPS=.025;D=6;TAU=5.
def make_initial(N,seed):
 rng=np.random.default_rng(seed);A=np.zeros((N,N),np.int8);m=N//2
 for _ in range(D):
  while True:
   p=rng.permutation(m)
   if not np.any(A[np.arange(m),m+p]):break
  A[np.arange(m),m+p]=A[m+p,np.arange(m)]=1
 return A
def energy(A):
 N=len(A);ed=np.argwhere(np.triu(A,1)>0);w,V=la.eigh(A.astype(float)/D,check_finite=False,driver='evr');ew=np.exp(G*w);eij=np.sum((V[ed[:,0]]*V[ed[:,1]])*ew[None,:],axis=1)
 return float(-ew.mean()+U*np.sum(eij*eij)/N-KAP*np.log(EPS+1-w).mean())
def c4(A):
 C=A.astype(np.int16)@A.astype(np.int16);x=C[np.triu_indices(len(A),1)].astype(np.int64);return int(np.sum(x*(x-1)//2)//2)
def diag(A):
 N=len(A);w=la.eigh(np.eye(N)-A.astype(float)/D,eigvals_only=True,check_finite=False);ds={}
 for t in (3,5,8,10):z=np.exp(-t*w);ds[t]=float(2*t*np.dot(w,z)/z.sum())
 return float(w[1]),ds
def balls(A,R=5):
 N=len(A);ne=[np.flatnonzero(A[i]).tolist() for i in range(N)];vv=[]
 for s in range(N):
  seen={s};fr={s};row=[]
  for _ in range(R):
   nf=set()
   for u in fr:nf.update(ne[u])
   nf-=seen;seen|=nf;fr=nf;row.append(len(seen))
  vv.append(row)
 return np.mean(vv,0)
def main(N,attempts,seed,start=None):
 rng=np.random.default_rng(seed)
 if start:
  z=np.load(start);A=z['A'].astype(np.int8);E=energy(A);acc=0
 else:
  A=make_initial(N,seed);E=energy(A);acc=0
 valid=0;ed=[tuple(map(int,x)) for x in np.argwhere(np.triu(A,1)>0)];t0=time.time()
 print('START',E,c4(A)/N,diag(A),balls(A),flush=True)
 for it in range(1,attempts+1):
  prop=None
  for _ in range(100):
   i,j=rng.integers(len(ed),size=2)
   if i==j:continue
   e1,e2=ed[i],ed[j];a,b=e1;c,d=e2
   if len({a,b,c,d})<4:continue
   adds=((a,c),(b,d)) if rng.integers(2)==0 else ((a,d),(b,c))
   if any(A[x,y] for x,y in adds):continue
   B=A.copy();B[a,b]=B[b,a]=0;B[c,d]=B[d,c]=0
   if any(np.dot(B[x],B[y]) for x,y in adds):continue
   for x,y in adds:B[x,y]=B[y,x]=1
   prop=B;break
  if prop is None:continue
  valid+=1;Eb=energy(prop)
  if Eb<E-1e-14:A=prop;E=Eb;acc+=1;ed=[tuple(map(int,x)) for x in np.argwhere(np.triu(A,1)>0)]
  if it%2000==0:
   ck=f'results/blind_N{N}_seed{seed}_step{it}.npz';np.savez_compressed(ck,A=A,E=E,attempts=it,accepted=acc,seed=seed)
   print('STEP',it,'E',E,'acc',acc,'C4N',c4(A)/N,'diag',diag(A),'CK',ck,flush=True)
 out=f'results/blind_N{N}_{attempts}.npz';np.savez_compressed(out,A=A,E=E,attempts=attempts,accepted=acc,seed=seed)
 print('FINAL',out,E,c4(A)/N,diag(A),balls(A),'acc',acc,'time',time.time()-t0,flush=True)
if __name__=='__main__':main(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4] if len(sys.argv)>4 else None)
