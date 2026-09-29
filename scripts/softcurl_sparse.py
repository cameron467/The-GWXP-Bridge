import numpy as np, sys, json, time
from scipy import sparse
from scipy.sparse.linalg import eigsh
from softcurl_autonomous import cycles_upto

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
 B=sparse.csr_matrix((bd,(br,bc)),shape=(N,E)); BtB=(B.T@B).tocsc()
 out={}
 for rho in [.05,.1,.2,.3,.5,.7]:
  sw=np.sqrt(rho**(lens-4));CW=C@sparse.diags(sw);H=(CW@CW.T + 100.0*BtB).tocsc()
  ev=float(eigsh(H,k=1,which='SA',return_eigenvectors=False,tol=1e-8,maxiter=30000)[0]);out[str(rho)]=ev;print(label,rho,ev,'sec',time.time()-t0,flush=True)
 res={'label':label,'N':N,'E':E,'F':len(cyc),'Lmax':Lmax,'gaps':out,'elapsed':time.time()-t0};open(f'results/softcurl_sparse_{label}.json','w').write(json.dumps(res,indent=2));print(json.dumps(res))
if __name__=='__main__':analyze(sys.argv[2],sys.argv[1],int(sys.argv[3]))
