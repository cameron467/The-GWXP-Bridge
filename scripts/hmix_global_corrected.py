import importlib.util,numpy as np,sys,json
from scipy.linalg import eigh,null_space
from scipy.optimize import linprog,minimize
from scipy.special import logsumexp
# reuse move sampling/tval/symvec from rank4 script
spec=importlib.util.spec_from_file_location('rk',str(__import__('pathlib').Path(__file__).with_name('rank4_keff_autonomous.py')));rk=importlib.util.module_from_spec(spec);spec.loader.exec_module(rk)
tr=np.array([1,1,1,0,0,0.],float)/np.sqrt(3);T5=null_space(tr.reshape(1,-1)).T;R6=np.vstack([tr,T5])
def feat(z):
 y=R6@z;K=np.outer(y,y);S=K[1:,1:];D=S-np.trace(S)/5*np.eye(5);f=list(K[0,1:])+[D[i,i] for i in range(4)]
 for i in range(5):
  for j in range(i+1,5):f.append(np.sqrt(2)*D[i,j])
 return np.array(f)
def shear(z):
 y=R6@z;return y[1:]@y[1:]
def km(Z,q):
 K=(Z.T*q)@Z;Kp=R6@K@R6.T;S=Kp[1:,1:];ev=np.linalg.eigvalsh(S);mu=ev.mean();return dict(rms=float(np.sqrt(np.mean((ev/mu-1)**2))),spread=float((ev[-1]-ev[0])/mu),mix=float(np.linalg.norm(Kp[0,1:])/mu),eig=[float(x/mu) for x in ev])
def main(path,M,seed):
 A=rk.loadA(path);N=len(A);X,w,Q,Qw=rk.spectral_frame(A);R=np.linalg.inv(np.eye(N)-rk.RHO*A.astype(float));moves,raw=rk.sample_moves(A,M,seed);Z=[];p=[]
 for o,adds in moves:
  a,b,c,d=o;Dh=np.zeros((3,3))
  for x,y in adds:v=X[x]-X[y];Dh+=np.outer(v,v)
  for x,y in ((a,b),(c,d)):v=X[x]-X[y];Dh-=np.outer(v,v)
  Z.append(rk.symvec(Dh));p.append(rk.tval(R,o,adds))
 Z=np.array(Z);p=np.maximum(np.array(p),1e-300);p/=p.sum();F=np.array([feat(z) for z in Z]).T;sc=np.sqrt((F*F)@p);sc[sc<1e-14]=1;Fs=F/sc[:,None];sp=np.array([shear(z) for z in Z]);sp0=sp@p;sps=sp/sp0
 Ae=np.vstack([Fs,sps,np.ones(M)]);be=np.r_[np.zeros(19),1.,1.];lp=linprog(np.zeros(M),A_eq=Ae,b_eq=be,bounds=(0,None),method='highs')
 out=dict(N=N,moves=M,feasible=bool(lp.success),prior=km(Z,p),rawfeat=float(np.linalg.norm(Fs@p)),shear0=float(sp0))
 if lp.success:
  C=np.vstack([Fs,sps[None,:]]);target=np.r_[np.zeros(19),1.];logp=np.log(p)
  def fun(lam):return logsumexp(logp-lam@C)+lam@target
  def jac(lam):
   x=logp-lam@C;x-=x.max();q=np.exp(x);q/=q.sum();return target-C@q
  res=minimize(fun,np.zeros(20),jac=jac,method='BFGS',options={'gtol':1e-10,'maxiter':4000});x=logp-res.x@C;x-=x.max();q=np.exp(x);q/=q.sum();mult=q/p
  out.update(opt_success=bool(res.success),finalfeat=float(np.linalg.norm(Fs@q)),shearratio=float((sp@q)/sp0),KL=float(np.sum(q*np.log(np.maximum(q,1e-300)/p))),p95mult=float(np.quantile(mult,.95)),maxmult=float(mult.max()),final=km(Z,q))
 print(json.dumps(out),flush=True);open(f'results/hmix_global_N{N}.json','w').write(json.dumps(out,indent=2))
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
