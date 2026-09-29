import numpy as np, sys, json, time
from scipy import sparse
from scipy.sparse.linalg import eigsh, LinearOperator
from scipy.linalg import null_space

def cycles_upto(A,Lmax):
 N=len(A);neigh=[list(map(int,np.flatnonzero(A[i]))) for i in range(N)];out=[]
 for s in range(N):
  def dfs(path,seen):
   u=path[-1]
   for v in neigh[u]:
    if v==s:
     if 4<=len(path)<=Lmax and path[1]<path[-1]:out.append(tuple(path))
     continue
    if v<=s or v in seen or len(path)>=Lmax:continue
    seen.add(v);path.append(v);dfs(path,seen);path.pop();seen.remove(v)
  for v in neigh[s]:
   if v>s:dfs([s,v],{s,v})
 return out

def analyze(path,label,Lmax):
 t0=time.time();A=np.load(path,allow_pickle=True)['A'].astype(np.int8);N=len(A);edges=[tuple(map(int,x)) for x in np.argwhere(np.triu(A,1))];E=len(edges);ei={e:i for i,e in enumerate(edges)}
 cyc=cycles_upto(A,Lmax);lens=np.array([len(c) for c in cyc]);rr=[];cc=[];dd=[]
 for f,c in enumerate(cyc):
  z=list(c)+[c[0]]
  for u,v in zip(z[:-1],z[1:]):
   e=tuple(sorted((u,v)));rr.append(ei[e]);cc.append(f);dd.append(1. if e==(u,v) else -1.)
 C=sparse.csc_matrix((dd,(rr,cc)),shape=(E,len(cyc)))
 br=[];bc=[];bd=[]
 for j,(u,v) in enumerate(edges):br += [u,v];bc += [j,j];bd += [1.,-1.]
 B=sparse.csr_matrix((bd,(br,bc)),shape=(N,E)).toarray();Z=null_space(B);cd=Z.shape[1]
 print(label,'built N,E,F,cd',N,E,len(cyc),cd,'sec',time.time()-t0,flush=True)
 vals={}
 for rho in [.05,.1,.2,.3,.5,.7]:
  w=rho**(lens-4)
  def mv(v):
   z=Z@v;u=C.T@z;return Z.T@(C@(w*u))
  R=LinearOperator((cd,cd),matvec=mv,dtype=float)
  ev=float(eigsh(R,k=1,which='SA',return_eigenvectors=False,tol=2e-8,maxiter=40000)[0])
  vals[str(rho)]=ev;print(label,'rho',rho,'gap',ev,'sec',time.time()-t0,flush=True)
 out={'label':label,'N':N,'E':E,'F':len(cyc),'cycle_dim':cd,'Lmax':Lmax,'counts':{str(int(x)):int(np.sum(lens==x)) for x in np.unique(lens)},'gaps':vals,'elapsed':time.time()-t0}
 open(f'results/softcurl_{label}.json','w').write(json.dumps(out,indent=2));return out
if __name__=='__main__':
 label,path,L=sys.argv[1],sys.argv[2],int(sys.argv[3]);print(json.dumps(analyze(path,label,L)))
