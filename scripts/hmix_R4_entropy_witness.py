import numpy as np, sys, json, time
from scipy.optimize import linprog, minimize
from scipy.special import logsumexp
import hmix_corrected_local as H
from hmix_R4_fast import enumerate_Z

def main(path,c,rad,outfile,nsub=8000,seed=1):
 t0=time.time();A=np.load(path,allow_pickle=True)['A'].astype(np.int8);N=len(A);Rglob=np.linalg.inv(np.eye(N)-H.RHO*A.astype(float))
 vs=H.ball(A,c,rad);X,w,Qw=H.local_frame(A,vs);Xmap={v:X[i] for i,v in enumerate(vs)};Zall,meta=enumerate_Z(A,vs,Xmap)
 rng=np.random.default_rng(seed);ids=rng.choice(len(Zall),min(nsub,len(Zall)),replace=False);Z=Zall[ids];met=[meta[i] for i in ids]
 tv=np.array([H.tval(Rglob,*m) for m in met]);p=np.maximum(tv,1e-300);p/=p.sum()
 F=np.array([H.feat(z) for z in Z]).T;sc=np.sqrt((F*F)@p);sc[sc<1e-14]=1;Fs=F/sc[:,None]
 sp=np.array([H.shear_power(z) for z in Z]);sp0=float(sp@p);sps=sp/sp0
 Aeq=np.vstack([Fs,np.ones(len(p))]);beq=np.r_[np.zeros(19),1.]
 lp=linprog(-sps,A_eq=Aeq,b_eq=beq,bounds=(0,None),method='highs');rmax=float(sps@lp.x) if lp.success else 0.
 logp=np.log(p); trials={}
 for rt in [0.25,0.5,0.75,1.0]:
  if rt>rmax+1e-8:trials[str(rt)]={'feasible':False};continue
  C=np.vstack([Fs,sps[None,:]]);target=np.r_[np.zeros(19),rt]; chk=linprog(np.zeros(len(p)),A_eq=np.vstack([C,np.ones(len(p))]),b_eq=np.r_[target,1.],bounds=(0,None),method='highs')
  if not chk.success:trials[str(rt)]={'feasible':False};continue
  def fun(lam):return logsumexp(logp-lam@C)+lam@target
  def jac(lam):
   xx=logp-lam@C;xx-=xx.max();q=np.exp(xx);q/=q.sum();return target-C@q
  res=minimize(fun,np.zeros(20),jac=jac,method='BFGS',options={'gtol':1e-9,'maxiter':2500})
  xx=logp-res.x@C;xx-=xx.max();q=np.exp(xx);q/=q.sum();err=float(np.linalg.norm(C@q-target));kl=float(np.sum(q*np.log(np.maximum(q,1e-300)/p)))
  trials[str(rt)]={'feasible':True,'KL':kl,'err':err,'maxmult':float((q/p).max()),'p95mult':float(np.quantile(q/p,.95)),'metrics':H.km_metrics(Z,q)}
 out={'N':N,'center':c,'radius':rad,'ball':len(vs),'moves_total':len(Zall),'subset':len(Z),'prior_metrics':H.km_metrics(Z,p),'prior_shear':sp0,'iso_max_ratio_subset':rmax,'trials':trials,'elapsed':time.time()-t0}
 print(json.dumps(out),flush=True);open(outfile,'w').write(json.dumps(out,indent=2))
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5]),int(sys.argv[6]))
