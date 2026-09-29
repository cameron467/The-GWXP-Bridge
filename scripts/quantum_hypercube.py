import numpy as np, itertools, sys, time, json
from scipy.linalg import eigh
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh

# GWXP corrected graph point
GPAR=2.0; U=.1; KAP=.3; EPS=.025; TAU=5.; D=6; RHO=.10

def make_initial(n,seed):
    rng=np.random.default_rng(seed); A=np.zeros((n,n),dtype=np.int8); m=n//2
    for _ in range(D):
        for __ in range(100000):
            p=rng.permutation(m)
            if not np.any(A[np.arange(m),m+p]): break
        else: raise RuntimeError('matching failure')
        A[np.arange(m),m+p]=1; A[m+p,np.arange(m)]=1
    return A

def triangle_count(A):
    # trace A^3/6
    return int(np.trace(A.astype(np.int16)@A.astype(np.int16)@A.astype(np.int16))//6)

def c4(A):
    B=A.astype(np.int16)@A.astype(np.int16)
    x=B[np.triu_indices(len(A),1)].astype(np.int64)
    return int(np.sum(x*(x-1)//2)//2)

def energy_per_vertex(A):
    n=len(A); w,v=eigh(A.astype(float)/D,check_finite=False)
    ex=np.exp(GPAR*w); ed=np.argwhere(np.triu(A,1))
    kij=np.einsum('ij,ij,j->i',v[ed[:,0]],v[ed[:,1]],ex,optimize=True)
    gp=float(-ex.mean()+U*np.dot(kij,kij)/n-KAP*np.log(EPS+1-w).mean())
    return gp + TAU*triangle_count(A)/n

def gap(A):
    w=eigh(np.eye(len(A))-A.astype(float)/D,eigvals_only=True,check_finite=False)
    return float(w[1])

def ds(A,t=5):
    w=eigh(np.eye(len(A))-A.astype(float)/D,eigvals_only=True,check_finite=False)
    z=np.exp(-t*w); return float(2*t*np.dot(w,z)/z.sum())

def legal_switch_candidates(A,rng,limit=20000):
    ed=np.argwhere(np.triu(A,1)); n=len(A)
    for _ in range(limit):
        i,j=rng.integers(len(ed),size=2)
        if i==j: continue
        a,b=map(int,ed[i]); c,d=map(int,ed[j])
        if len({a,b,c,d})<4: continue
        adds=((a,c),(b,d)) if rng.integers(2)==0 else ((a,d),(b,c))
        if any(A[x,y] for x,y in adds): continue
        B=A.copy(); B[a,b]=B[b,a]=0; B[c,d]=B[d,c]=0
        # require each individual move triangle-free at selection stage
        if any(np.dot(B[x],B[y]) for x,y in adds): continue
        B[adds[0]]=1; B[adds[0][::-1]]=1; B[adds[1]]=1; B[adds[1][::-1]]=1
        yield (a,b,c,d,adds,B)

def select_disjoint_downhill(A,m,seed):
    rng=np.random.default_rng(seed); E0=energy_per_vertex(A); used=set(); out=[]
    # repeatedly sample; exact energy filter
    for a,b,c,d,adds,B in legal_switch_candidates(A,rng,limit=200000):
        verts={a,b,c,d}
        if verts & used: continue
        e=energy_per_vertex(B)
        if e < E0-1e-12:
            out.append((a,b,c,d,adds,e-E0,c4(B)-c4(A)))
            used |= verts
            if len(out)>=m: break
    if len(out)<m: raise RuntimeError(f'only found {len(out)} switches')
    return out

def apply_bits(A0,switches,bits):
    A=A0.copy()
    for k,s in enumerate(switches):
        if (bits>>k)&1:
            a,b,c,d,adds,*_=s
            A[a,b]=A[b,a]=0;A[c,d]=A[d,c]=0
            for x,y in adds:A[x,y]=A[y,x]=1
    return A

def run(n=64,m=10,seed=64001):
    t0=time.time(); A0=make_initial(n,seed)
    sw=select_disjoint_downhill(A0,m,seed+1)
    print('selected',len(sw),'switches',[(round(x[-2],8),x[-1]) for x in sw],flush=True)
    S=1<<m
    Es=np.empty(S); C=np.empty(S); T=np.empty(S,dtype=int); gaps=np.empty(S); d5=np.empty(S)
    Rs=[]; As=[]
    for bits in range(S):
        A=apply_bits(A0,sw,bits); As.append(A)
        Es[bits]=n*energy_per_vertex(A); C[bits]=c4(A)/n; T[bits]=triangle_count(A)
        gaps[bits]=gap(A); d5[bits]=ds(A,5)
        Rs.append(np.linalg.inv(np.eye(n)-RHO*A.astype(float)))
        if (bits+1)%max(1,S//8)==0: print('states',bits+1,'/',S,'elapsed',time.time()-t0,flush=True)
    rows=[];cols=[];fvals=[]
    for sidx in range(S):
        R=Rs[sidx]
        for k,s in enumerate(sw):
            if (sidx>>k)&1: continue
            j=sidx|(1<<k); Rp=Rs[j]
            a,b,c,d,adds,*_=s; (x1,y1),(x2,y2)=adds
            fwd=float(R[x1,y1]*R[x2,y2]); rev=float(Rp[a,b]*Rp[c,d]); f=.5*(fwd+rev)
            rows.extend([sidx,j]);cols.extend([j,sidx]);fvals.extend([f,f])
    F=coo_matrix((fvals,(rows,cols)),shape=(S,S)).tocsr()
    pos=np.array([int(i).bit_count() for i in range(S)],float)
    # energy and kinetic scales
    Eshift=Es-Es.min(); medgap=float(np.median(np.abs(np.diff(np.sort(np.unique(np.round(Es,12))))))) if len(np.unique(np.round(Es,12)))>1 else 1
    fmed=float(np.median(np.array(fvals)[::2])); fmean=float(np.mean(np.array(fvals)[::2]))
    Escale=float(np.std(Es));
    print('diag range',Es.min(),Es.max(),'std',Escale,'f median',fmed,'mean',fmean,flush=True)
    # choose eta so typical offdiag = zeta*std(E)/sqrt(m) (rough extensive-normalized scale)
    zetas=[0,0.03,0.1,0.3,1.0,3.0,10.0]
    outs=[]
    for z in zetas:
        eta=0. if z==0 else z*(Escale/np.sqrt(m))/fmean
        H=diags(Es,0,format='csr') - eta*F
        if S<=3:
            vals,vecs=np.linalg.eigh(H.toarray()); val=vals[0]; psi=vecs[:,0]
        else:
            vals,vecs=eigsh(H,k=1,which='SA',tol=1e-10,maxiter=200000);val=float(vals[0]);psi=vecs[:,0]
        p=psi*psi; p/=p.sum()
        out=dict(zeta=z,eta=float(eta),E0=float(val),mean_parent_E=float(np.dot(p,Es)),
                 mean_bits=float(np.dot(p,pos)),mean_c4=float(np.dot(p,C)),mean_tri=float(np.dot(p,T)),
                 mean_gap=float(np.dot(p,gaps)),mean_ds5=float(np.dot(p,d5)),
                 weight_lowest10pct=float(p[Es<=np.quantile(Es,.1)].sum()),
                 weight_highC4_25pct=float(p[C>=np.quantile(C,.75)].sum()),
                 ipr=float(np.sum(p*p)))
        outs.append(out); print('RESULT',json.dumps(out),flush=True)
    # classical correlations
    print('CORR E,C4',float(np.corrcoef(Es,C)[0,1]),'E,bits',float(np.corrcoef(Es,pos)[0,1]),flush=True)
    np.savez_compressed(f'results/quantum_hypercube_N{n}_m{m}.npz',Es=Es,C4=C,T=T,gaps=gaps,ds5=d5,bits=pos,
                        fdata=F.data,findices=F.indices,findptr=F.indptr,sw=np.array([(x[0],x[1],x[2],x[3],x[4][0][0],x[4][0][1],x[4][1][0],x[4][1][1]) for x in sw]),
                        zetas=np.array(zetas),results_json=np.array([json.dumps(x) for x in outs]))
    return outs

if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 64
    m=int(sys.argv[2]) if len(sys.argv)>2 else 10
    seed=int(sys.argv[3]) if len(sys.argv)>3 else 64001
    run(n,m,seed)
