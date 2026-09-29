import numpy as np, sys, json, time
from scipy.linalg import eigh
D=6;RHO=.1
# Sym(3) orthonormal coordinates [xx,yy,zz,sqrt2xy,sqrt2xz,sqrt2yz]
B=[]
for i,j in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]:
 M=np.zeros((3,3));
 if i==j:M[i,j]=1
 else:M[i,j]=M[j,i]=1/np.sqrt(2)
 B.append(M)
B=np.array(B)
trace=np.array([1.,1.,1.,0,0,0.]);_,_,vh=np.linalg.svd(trace.reshape(1,-1));Z5=vh[1:].T

def symvec(M):return np.array([M[0,0],M[1,1],M[2,2],np.sqrt(2)*M[0,1],np.sqrt(2)*M[0,2],np.sqrt(2)*M[1,2]])
def loadA(p):return np.load(p,allow_pickle=True)['A'].astype(np.int8)
def spectral_frame(A):
 N=len(A);L=np.eye(N)-A.astype(float)/D;w,V=eigh(L,check_finite=False)
 X0=V[:,1:4]
 Q=X0.T@L@X0
 q,U=eigh(Q);X=X0@U@np.diag(1/np.sqrt(q))@U.T
 return X,w,Q,X.T@L@X

def masks(A):
 out=[]
 for i in range(len(A)):
  z=0
  for j in np.flatnonzero(A[i]):z|=1<<int(j)
  out.append(z)
 return out

def sample_moves(A,M,seed):
 rng=np.random.default_rng(seed);ed=np.argwhere(np.triu(A,1));m=len(ed);ms=masks(A);out=[];raw=0
 while len(out)<M:
  raw+=1;i,j=rng.integers(m,size=2)
  if i==j:continue
  a,b=map(int,ed[i]);c,d=map(int,ed[j])
  if len({a,b,c,d})<4:continue
  adds=((a,c),(b,d)) if rng.integers(2)==0 else ((a,d),(b,c))
  if any(A[x,y] for x,y in adds):continue
  mm={a:ms[a]&~(1<<b),b:ms[b]&~(1<<a),c:ms[c]&~(1<<d),d:ms[d]&~(1<<c)}
  if any(mm.get(x,ms[x])&mm.get(y,ms[y]) for x,y in adds):continue
  out.append(((a,b,c,d),adds))
 return out,raw

def tval(R,o,adds):
 a,b,c,d=o;(x1,y1),(x2,y2)=adds
 fwd=max(float(R[x1,y1]*R[x2,y2]),0.0)
 # exact R' endpoint block via Woodbury for M'=I-rho A'
 pairs=[(a,b,+RHO),(b,a,+RHO),(c,d,+RHO),(d,c,+RHO),(x1,y1,-RHO),(y1,x1,-RHO),(x2,y2,-RHO),(y2,x2,-RHO)]
 us=[p[0] for p in pairs];vs=[p[1] for p in pairs];coef=np.array([p[2] for p in pairs])
 verts=[a,b,c,d]
 RU=R[np.ix_(verts,us)]*coef[None,:]
 K=np.eye(8)+R[np.ix_(vs,us)]*coef[None,:]
 VTR=R[np.ix_(vs,verts)]
 Rp=R[np.ix_(verts,verts)]-RU@np.linalg.solve(K,VTR)
 pos={v:i for i,v in enumerate(verts)}
 rev=max(float(Rp[pos[a],pos[b]]*Rp[pos[c],pos[d]]),0.0)
 return .5*(fwd+rev)

def tt_basis(k):
 k=np.array(k,float);k/=np.linalg.norm(k);s=np.array([1.,0,0])
 if abs(s@k)>.85:s=np.array([0.,1,0])
 e1=s-(s@k)*k;e1/=np.linalg.norm(e1);e2=np.cross(k,e1)
 P=(np.outer(e1,e1)-np.outer(e2,e2))/np.sqrt(2);X=(np.outer(e1,e2)+np.outer(e2,e1))/np.sqrt(2)
 return np.column_stack([symvec(P),symvec(X)])
def analyze(path,M=12000,seed=1):
 A=loadA(path);N=len(A);X,w,Q,Qw=spectral_frame(A);R=np.linalg.inv(np.eye(N)-RHO*A.astype(float));moves,raw=sample_moves(A,M,seed)
 K_eq=np.zeros((6,6));K_med=np.zeros((6,6));ws=[];zs=[]
 for o,adds in moves:
  a,b,c,d=o
  Dh=np.zeros((3,3))
  for x,y in adds:
   v=X[x]-X[y];Dh+=np.outer(v,v)
  for x,y in ((a,b),(c,d)):
   v=X[x]-X[y];Dh-=np.outer(v,v)
  z=symvec(Dh);t=tval(R,o,adds);ws.append(t);zs.append(z);K_eq+=np.outer(z,z);K_med+=t*np.outer(z,z)
 K_eq/=M;K_med/=sum(ws)
 rng=np.random.default_rng(seed+999);dirs=rng.normal(size=(500,3));dirs/=np.linalg.norm(dirs,axis=1)[:,None]
 def met(K):
  K5=Z5.T@K@Z5;alpha=np.trace(K5)/5;res=np.linalg.norm(K5-alpha*np.eye(5))/np.linalg.norm(alpha*np.eye(5));ev=np.linalg.eigvalsh(K5)
  splits=[];means=[]
  for k in dirs:
   T=tt_basis(k);Kt=T.T@K@T;e=np.linalg.eigvalsh(Kt);splits.append((e[-1]-e[0])/e.mean());means.append(e.mean())
  return dict(spin4_rms=float(res),eig5=[float(x) for x in ev/alpha],eig_ratio=float(ev[-1]/ev[0]),tt_split_mean=float(np.mean(splits)),tt_split_p95=float(np.quantile(splits,.95)),tt_split_max=float(np.max(splits)),tt_mean_cv=float(np.std(means)/np.mean(means)))
 out=dict(path=path,N=N,moves=M,raw_proposals=raw,legal_fraction=M/raw,lap_gap=float(w[1]),frame_Q_raw=Q.tolist(),frame_Q_whitened=Qw.tolist(),weight_mean=float(np.mean(ws)),weight_cv=float(np.std(ws)/np.mean(ws)),equal=met(K_eq),mediator=met(K_med))
 print(json.dumps(out),flush=True)
 return out
if __name__=='__main__':
 p=sys.argv[1];M=int(sys.argv[2]) if len(sys.argv)>2 else 12000;seed=int(sys.argv[3]) if len(sys.argv)>3 else 1
 o=analyze(p,M,seed);open(f'results/rank4_N{o["N"]}.json','w').write(json.dumps(o,indent=2))
