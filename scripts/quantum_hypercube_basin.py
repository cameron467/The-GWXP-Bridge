import numpy as np, sys, time, json
from scipy.linalg import eigh
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh
GPAR=2.;U=.1;KAP=.3;EPS=.025;TAU=5.;D=6;RHO=.1

def tri(A): return int(np.trace(A.astype(np.int16)@A.astype(np.int16)@A.astype(np.int16))//6)
def c4(A):
 B=A.astype(np.int16)@A.astype(np.int16);x=B[np.triu_indices(len(A),1)].astype(np.int64);return int(np.sum(x*(x-1)//2)//2)
def eper(A):
 n=len(A);w,v=eigh(A.astype(float)/D,check_finite=False);ex=np.exp(GPAR*w);ed=np.argwhere(np.triu(A,1));kij=np.einsum('ij,ij,j->i',v[ed[:,0]],v[ed[:,1]],ex,optimize=True)
 return float(-ex.mean()+U*np.dot(kij,kij)/n-KAP*np.log(EPS+1-w).mean()+TAU*tri(A)/n)
def metrics(A):
 w=eigh(np.eye(len(A))-A.astype(float)/D,eigvals_only=True,check_finite=False);z=np.exp(-5*w);return c4(A)/len(A),float(w[1]),float(10*np.dot(w,z)/z.sum())
def candidates(A,rng,limit=300000):
 ed=np.argwhere(np.triu(A,1))
 for _ in range(limit):
  i,j=rng.integers(len(ed),size=2)
  if i==j:continue
  a,b=map(int,ed[i]);c,d=map(int,ed[j])
  if len({a,b,c,d})<4:continue
  adds=((a,c),(b,d)) if rng.integers(2)==0 else ((a,d),(b,c))
  if any(A[x,y] for x,y in adds):continue
  B=A.copy();B[a,b]=B[b,a]=0;B[c,d]=B[d,c]=0
  if any(np.dot(B[x],B[y]) for x,y in adds):continue
  for x,y in adds:B[x,y]=B[y,x]=1
  yield a,b,c,d,adds,B

def select(A,m,seed):
 rng=np.random.default_rng(seed);used=set();out=[]
 for a,b,c,d,adds,B in candidates(A,rng):
  vs={a,b,c,d}
  if vs&used:continue
  out.append((a,b,c,d,adds));used|=vs
  if len(out)>=m:return out
 raise RuntimeError(len(out))
def apply(A0,sw,bits):
 A=A0.copy()
 for k,(a,b,c,d,adds) in enumerate(sw):
  if (bits>>k)&1:
   A[a,b]=A[b,a]=0;A[c,d]=A[d,c]=0
   for x,y in adds:A[x,y]=A[y,x]=1
 return A

def main(path,m=9,seed=991):
 A0=np.load(path)['A'].astype(np.int8);n=len(A0);sw=select(A0,m,seed);S=1<<m;t0=time.time()
 Es=np.empty(S);C=np.empty(S);gaps=np.empty(S);d5=np.empty(S);Ts=np.empty(S);Rs=[]
 print('ROOT',n,'eper',eper(A0),'metrics',metrics(A0),'tri',tri(A0),flush=True)
 for b in range(S):
  A=apply(A0,sw,b);Es[b]=n*eper(A);C[b],gaps[b],d5[b]=metrics(A);Ts[b]=tri(A);Rs.append(np.linalg.inv(np.eye(n)-RHO*A.astype(float)))
  if (b+1)%(max(1,S//8))==0:print('states',b+1,'elapsed',time.time()-t0,flush=True)
 rows=[];cols=[];fv=[]
 for i in range(S):
  R=Rs[i]
  for k,(a,b,c,d,adds) in enumerate(sw):
   if (i>>k)&1:continue
   j=i|(1<<k);Rp=Rs[j];(x1,y1),(x2,y2)=adds
   f=.5*(float(R[x1,y1]*R[x2,y2])+float(Rp[a,b]*Rp[c,d]))
   rows += [i,j];cols += [j,i];fv += [f,f]
 F=coo_matrix((fv,(rows,cols)),shape=(S,S)).tocsr();fmean=np.mean(np.array(fv)[::2]);Escale=np.std(Es);bits=np.array([i.bit_count() for i in range(S)],float)
 print('range pervertex',Es.min()/n,Es.max()/n,'C4 range',C.min(),C.max(),'fmean',fmean,'corr E,C4',np.corrcoef(Es,C)[0,1],flush=True)
 for z in [0,.03,.1,.3,1,3,10]:
  eta=0 if z==0 else z*(Escale/np.sqrt(m))/fmean;H=diags(Es)-eta*F;val,vec=eigsh(H,k=1,which='SA',tol=1e-10,maxiter=200000);p=vec[:,0]**2;p/=p.sum()
  o=dict(zeta=z,eta=float(eta),ground=float(val[0]),parent=float(p@Es)/n,c4=float(p@C),gap=float(p@gaps),ds5=float(p@d5),tri=float(p@Ts),bits=float(p@bits),rootweight=float(p[0]),highC4=float(p[C>=np.quantile(C,.75)].sum()),lowE=float(p[Es<=np.quantile(Es,.1)].sum()),ipr=float(p@p))
  print('RESULT',json.dumps(o),flush=True)
 np.savez_compressed(f'results/quantum_basin_N{n}_m{m}.npz',Es=Es,C4=C,gaps=gaps,ds5=d5,T=Ts,bits=bits,sw=np.array([(a,b,c,d,*adds[0],*adds[1]) for a,b,c,d,adds in sw]))
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 9,int(sys.argv[3]) if len(sys.argv)>3 else 991)
