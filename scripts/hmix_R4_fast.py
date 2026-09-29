import numpy as np, sys, json, time
from scipy.optimize import linprog
import hmix_corrected_local as H

def enumerate_Z(A,vs,Xmap):
    sset=set(vs)
    edges=[tuple(map(int,x)) for x in np.argwhere(np.triu(A,1)) if int(x[0]) in sset and int(x[1]) in sset]
    Z=[]; meta=[]
    for ii,(a,b) in enumerate(edges):
      for jj in range(ii+1,len(edges)):
        c,d=edges[jj]
        if len({a,b,c,d})<4: continue
        for adds in (((a,c),(b,d)),((a,d),(b,c))):
          if any(A[x,y] for x,y in adds): continue
          ok=True
          for x,y in adds:
            # common neighbor excluding the two removed edges
            nx=np.flatnonzero(A[x]); ny=set(map(int,np.flatnonzero(A[y])))
            for z in nx:
              z=int(z)
              if (x==a and z==b) or (x==b and z==a) or (x==c and z==d) or (x==d and z==c): continue
              if z in ny:
                if (y==a and z==b) or (y==b and z==a) or (y==c and z==d) or (y==d and z==c): continue
                ok=False; break
            if not ok: break
          if not ok: continue
          Z.append(H.zmove(Xmap,(a,b,c,d),adds)); meta.append(((a,b,c,d),adds))
    return np.array(Z),meta

def main(path,c,rad,outfile,nsamp=12000,seed=1):
    t0=time.time(); A=np.load(path,allow_pickle=True)['A'].astype(np.int8);N=len(A); Rglob=np.linalg.inv(np.eye(N)-H.RHO*A.astype(float))
    vs=H.ball(A,c,rad); X,w,Qw=H.local_frame(A,vs); Xmap={v:X[i] for i,v in enumerate(vs)}
    Z,meta=enumerate_Z(A,vs,Xmap); print('enumerated',len(Z),'moves ball',len(vs),'sec',time.time()-t0,flush=True)
    F=np.array([H.feat(z) for z in Z]).T
    sc=np.sqrt(np.mean(F*F,axis=1));sc[sc<1e-14]=1;Fs=F/sc[:,None]
    sp=np.array([H.shear_power(z) for z in Z])
    Aeq=np.vstack([Fs,np.ones(len(Z))]);beq=np.r_[np.zeros(19),1.]
    lp=linprog(-sp,A_eq=Aeq,b_eq=beq,bounds=(0,None),method='highs')
    print('LP',lp.success,'sec',time.time()-t0,flush=True)
    sp_iso_max=float(sp@lp.x) if lp.success else None
    # sample exact physical mediator weights to estimate prior shear power
    rng=np.random.default_rng(seed); ids=rng.choice(len(meta),min(nsamp,len(meta)),replace=False)
    tv=[]; sps=[]
    for k,idx in enumerate(ids):
      o,adds=meta[idx]; tv.append(H.tval(Rglob,o,adds));sps.append(sp[idx])
      if (k+1)%2000==0: print('tvals',k+1,'sec',time.time()-t0,flush=True)
    tv=np.maximum(np.array(tv),1e-300);sps=np.array(sps); sp0=float(np.sum(tv*sps)/np.sum(tv));
    out={'N':N,'center':c,'radius':rad,'ball':len(vs),'moves':len(Z),'iso_feasible':bool(lp.success),'iso_shear_max':sp_iso_max,
         'physical_prior_shear_est':sp0,'iso_max_over_prior_est':(sp_iso_max/sp0 if lp.success else None),'prior_sample_n':len(ids),
         'uniform_prior_shear':float(sp.mean()),'iso_max_over_uniform':(sp_iso_max/sp.mean() if lp.success else None),'elapsed':time.time()-t0}
    print(json.dumps(out),flush=True);open(outfile,'w').write(json.dumps(out,indent=2))
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5]) if len(sys.argv)>5 else 12000,int(sys.argv[6]) if len(sys.argv)>6 else 1)
