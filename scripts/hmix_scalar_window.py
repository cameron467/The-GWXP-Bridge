import numpy as np, json, sys
from scipy.optimize import linprog, minimize
from scipy.special import logsumexp
import hmix_corrected_local as H

def analyze(A,Rglob,c,rad):
    vs=H.ball(A,c,rad); X,w,Qw=H.local_frame(A,vs); Xmap={v:X[i] for i,v in enumerate(vs)}
    chs=H.channels_in_ball(A,vs,Rglob)
    if len(chs)<25:
        return {'center':int(c),'radius':rad,'ball':len(vs),'moves':len(chs),'status':'too_few'}
    Z=np.array([H.zmove(Xmap,o,a) for o,a,t in chs])
    p=np.maximum(np.array([t for o,a,t in chs],float),1e-300); p/=p.sum()
    F=np.array([H.feat(z) for z in Z]).T
    sc=np.sqrt((F*F)@p); sc[sc<1e-14]=1.; Fs=F/sc[:,None]
    sp=np.array([H.shear_power(z) for z in Z]); sp0=float(sp@p); sps=sp/max(sp0,1e-300)
    Aeq=np.vstack([Fs,np.ones(len(p))]); beq=np.r_[np.zeros(Fs.shape[0]),1.]
    # min/max scalar shear amplitude under exact isotropy
    lpmax=linprog(-sps,A_eq=Aeq,b_eq=beq,bounds=(0,None),method='highs')
    lpmin=linprog(sps,A_eq=Aeq,b_eq=beq,bounds=(0,None),method='highs')
    out={'center':int(c),'radius':rad,'ball':len(vs),'moves':len(chs),'prior_shear_power':sp0,
         'prior':H.km_metrics(Z,p),'iso_feasible':bool(lpmax.success)}
    if not lpmax.success: return out
    rmax=float(sps@lpmax.x); rmin=float(sps@lpmin.x) if lpmin.success else None
    out['shear_ratio_min']=rmin; out['shear_ratio_max']=rmax
    # KL projection at target ratios if within feasible interval.
    logp=np.log(p)
    trials={}
    for rt in [0.1,0.25,0.5,0.75,1.0,1.5,2.0]:
        if rt < rmin-1e-8 or rt > rmax+1e-8:
            trials[str(rt)]={'feasible':False}; continue
        C=np.vstack([Fs,sps[None,:]]); target=np.r_[np.zeros(Fs.shape[0]),rt]
        Ae2=np.vstack([C,np.ones(len(p))]); be2=np.r_[target,1.]
        chk=linprog(np.zeros(len(p)),A_eq=Ae2,b_eq=be2,bounds=(0,None),method='highs')
        if not chk.success:
            trials[str(rt)]={'feasible':False}; continue
        def fun(lam): return logsumexp(logp-lam@C)+lam@target
        def jac(lam):
            xx=logp-lam@C; xx-=xx.max(); q=np.exp(xx); q/=q.sum(); return target-C@q
        res=minimize(fun,np.zeros(C.shape[0]),jac=jac,method='BFGS',options={'gtol':1e-9,'maxiter':2000})
        xx=logp-res.x@C; xx-=xx.max(); q=np.exp(xx); q/=q.sum()
        err=float(np.linalg.norm(C@q-target)); kl=float(np.sum(q*np.log(np.maximum(q,1e-300)/p)))
        trials[str(rt)]={'feasible':True,'opt_success':bool(res.success),'constraint_err':err,'KL':kl,
                         'final':H.km_metrics(Z,q),'maxmult':float((q/p).max())}
    out['targets']=trials
    return out

def main(path,centers,rad,outfile):
    A=np.load(path,allow_pickle=True)['A'].astype(np.int8);N=len(A);Rglob=np.linalg.inv(np.eye(N)-H.RHO*A.astype(float))
    arr=[]
    for c in centers:
        o=analyze(A,Rglob,int(c),rad);arr.append(o);print(json.dumps(o),flush=True)
    with open(outfile,'w') as f: json.dump(arr,f,indent=2)
    ok=[x for x in arr if x.get('iso_feasible')]
    print('SUMMARY',N,'R',rad,'iso',len(ok),'/',len(arr),'rmax',[round(x['shear_ratio_max'],3) for x in ok], 'rmin',[round(x['shear_ratio_min'],6) for x in ok])

if __name__=='__main__':
    path=sys.argv[1]; rad=int(sys.argv[2]); centers=list(map(int,sys.argv[3].split(','))); outfile=sys.argv[4]
    main(path,centers,rad,outfile)
