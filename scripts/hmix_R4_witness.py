import numpy as np, sys, json, time
from scipy.optimize import linprog
import hmix_corrected_local as H
from hmix_R4_fast import enumerate_Z

def main(path,c,rad,outfile,nsub=16000,nsamp=3000,seed=1):
 t0=time.time();A=np.load(path,allow_pickle=True)['A'].astype(np.int8);N=len(A);Rglob=np.linalg.inv(np.eye(N)-H.RHO*A.astype(float))
 vs=H.ball(A,c,rad);X,w,Qw=H.local_frame(A,vs);Xmap={v:X[i] for i,v in enumerate(vs)};Z,meta=enumerate_Z(A,vs,Xmap)
 F=np.array([H.feat(z) for z in Z]).T;sp=np.array([H.shear_power(z) for z in Z]);sc=np.sqrt(np.mean(F*F,axis=1));sc[sc<1e-14]=1;Fs=F/sc[:,None]
 rng=np.random.default_rng(seed); ids=rng.choice(len(Z),min(nsub,len(Z)),replace=False);Fq=Fs[:,ids];spq=sp[ids];Aeq=np.vstack([Fq,np.ones(len(ids))]);beq=np.r_[np.zeros(19),1.]
 lp=linprog(-spq,A_eq=Aeq,b_eq=beq,bounds=(0,None),method='highs')
 print('subsetLP',lp.success,'n',len(ids),'sec',time.time()-t0,flush=True)
 sp_iso=float(spq@lp.x) if lp.success else None
 # exact physical-prior shear estimate via sample t weights
 ids2=rng.choice(len(meta),min(nsamp,len(meta)),replace=False);tv=np.empty(len(ids2));sv=sp[ids2]
 for k,idx in enumerate(ids2):tv[k]=H.tval(Rglob,*meta[idx])
 sp0=float(np.sum(tv*sv)/np.sum(tv))
 out={'N':N,'center':c,'radius':rad,'ball':len(vs),'moves_total':len(Z),'subset':len(ids),'subset_iso_feasible':bool(lp.success),'subset_iso_shear':sp_iso,
 'physical_prior_shear_est':sp0,'witness_ratio_to_prior':(sp_iso/sp0 if lp.success else None),'prior_sample_n':len(ids2),'uniform_shear':float(sp.mean()),'elapsed':time.time()-t0}
 print(json.dumps(out),flush=True);open(outfile,'w').write(json.dumps(out,indent=2))
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]))
