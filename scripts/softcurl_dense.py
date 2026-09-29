import numpy as np, sys, json, time
from scipy import sparse
from scipy.linalg import eigh
from softcurl_autonomous import cycles_upto

def main(path,label,Lmax):
 t0=time.time();A=np.load(path,allow_pickle=True)['A'].astype(np.int8);N=len(A);edges=[tuple(map(int,x)) for x in np.argwhere(np.triu(A,1))];E=len(edges);ei={e:i for i,e in enumerate(edges)}
 cyc=cycles_upto(A,Lmax);lens=np.array([len(c) for c in cyc]);rr=[];cc=[];dd=[]
 for f,c in enumerate(cyc):
  z=list(c)+[c[0]]
  for u,v in zip(z[:-1],z[1:]):
   e=tuple(sorted((u,v)));rr.append(ei[e]);cc.append(f);dd.append(1. if e==(u,v) else -1.)
 C=sparse.csc_matrix((dd,(rr,cc)),shape=(E,len(cyc)))
 br=[];bc=[];bd=[]
 for j,(u,v) in enumerate(edges):br += [u,v];bc += [j,j];bd += [1.,-1.]
 B=sparse.csr_matrix((bd,(br,bc)),shape=(N,E));BtB=(B.T@B).toarray()*100.0
 vals={}
 for rho in [.05,.1,.2,.3,.5,.7]:
  w=rho**(lens-4);H=(C@sparse.diags(w)@C.T).toarray();H+=BtB
  ev=float(eigh(H,subset_by_index=[0,0],check_finite=False,overwrite_a=True,driver='evr')[0][0]);vals[str(rho)]=ev;print(label,rho,ev,'sec',time.time()-t0,flush=True)
 out={'label':label,'N':N,'E':E,'F':len(cyc),'Lmax':Lmax,'gaps':vals,'elapsed':time.time()-t0};open(f'results/softcurl_dense_{label}.json','w').write(json.dumps(out,indent=2));print(json.dumps(out))
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]))
