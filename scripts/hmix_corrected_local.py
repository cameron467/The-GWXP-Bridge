import numpy as np, sys, json, time
from scipy.linalg import eigh, null_space
from scipy.optimize import linprog, minimize
from scipy.special import logsumexp
D=6;RHO=.1
# trace+traceless transform in symvec coordinates
tr=np.array([1,1,1,0,0,0.],float)/np.sqrt(3);T5=null_space(tr.reshape(1,-1)).T;R6=np.vstack([tr,T5])
def symvec(M):return np.array([M[0,0],M[1,1],M[2,2],np.sqrt(2)*M[0,1],np.sqrt(2)*M[0,2],np.sqrt(2)*M[1,2]])
def ball(A,c,r):
 seen={int(c)};fr={int(c)}
 for _ in range(r):
  nx=set()
  for u in fr:nx.update(map(int,np.flatnonzero(A[u])))
  nx-=seen;seen|=nx;fr=nx
 return sorted(seen)
def local_frame(A,vs):
 Ab=A[np.ix_(vs,vs)].astype(float);Lc=np.diag(Ab.sum(1))-Ab;w,V=eigh(Lc,check_finite=False);X0=V[:,1:4]
 Q=X0.T@Lc@X0;q,U=eigh(Q);q=np.maximum(q,1e-10);X=X0@U@np.diag(1/np.sqrt(q))@U.T
 return X,w,X.T@Lc@X
def tval(R,o,adds):
 a,b,c,d=o;(x1,y1),(x2,y2)=adds;fwd=max(float(R[x1,y1]*R[x2,y2]),0.)
 pairs=[(a,b,+RHO),(b,a,+RHO),(c,d,+RHO),(d,c,+RHO),(x1,y1,-RHO),(y1,x1,-RHO),(x2,y2,-RHO),(y2,x2,-RHO)]
 us=[x[0] for x in pairs];vs=[x[1] for x in pairs];coef=np.array([x[2] for x in pairs]);verts=[a,b,c,d]
 RU=R[np.ix_(verts,us)]*coef[None,:];K=np.eye(8)+R[np.ix_(vs,us)]*coef[None,:];VTR=R[np.ix_(vs,verts)]
 Rp=R[np.ix_(verts,verts)]-RU@np.linalg.solve(K,VTR);pos={v:i for i,v in enumerate(verts)}
 rev=max(float(Rp[pos[a],pos[b]]*Rp[pos[c],pos[d]]),0.)
 return .5*(fwd+rev)
def channels_in_ball(A,vs,Rglob):
 sset=set(vs);edges=[tuple(map(int,x)) for x in np.argwhere(np.triu(A,1)) if int(x[0]) in sset and int(x[1]) in sset];out=[]
 for ii in range(len(edges)):
  a,b=edges[ii]
  for jj in range(ii+1,len(edges)):
   c,d=edges[jj]
   if len({a,b,c,d})<4:continue
   for adds in [((a,c),(b,d)),((a,d),(b,c))]:
    if any(A[x,y] for x,y in adds):continue
    # triangle-free in full graph after old edges removed
    ok=True
    for x,y in adds:
     rx=A[x].copy();ry=A[y].copy()
     for u,v in ((a,b),(c,d)):
      if x==u:rx[v]=0
      elif x==v:rx[u]=0
      if y==u:ry[v]=0
      elif y==v:ry[u]=0
     if np.dot(rx,ry):ok=False;break
    if not ok:continue
    out.append(((a,b,c,d),adds,tval(Rglob,(a,b,c,d),adds)))
 return out
def zmove(Xmap,o,adds):
 a,b,c,d=o;M=np.zeros((3,3))
 for x,y in adds:
  v=Xmap[x]-Xmap[y];M+=np.outer(v,v)
 for x,y in ((a,b),(c,d)):
  v=Xmap[x]-Xmap[y];M-=np.outer(v,v)
 return symvec(M)
def feat(z):
 y=R6@z;K=np.outer(y,y);S=K[1:,1:];Dm=S-np.trace(S)/5*np.eye(5);f=list(K[0,1:])+[Dm[i,i] for i in range(4)]
 for i in range(5):
  for j in range(i+1,5):f.append(np.sqrt(2)*Dm[i,j])
 return np.array(f)
def shear_power(z):
 y=R6@z;return float(np.dot(y[1:],y[1:]))
def km_metrics(Z,q):
 K=(Z.T*q)@Z;Kp=R6@K@R6.T;S=Kp[1:,1:];ev=np.linalg.eigvalsh(S);mu=ev.mean();spread=(ev[-1]-ev[0])/mu;rms=np.sqrt(np.mean((ev/mu-1)**2));mix=np.linalg.norm(Kp[0,1:])/mu
 return dict(rms=float(rms),spread=float(spread),mix=float(mix),eig=[float(x/mu) for x in ev])
def solve_ball(A,Rglob,c,rad):
 vs=ball(A,c,rad);X,w,Qw=local_frame(A,vs);Xmap={v:X[i] for i,v in enumerate(vs)};chs=channels_in_ball(A,vs,Rglob)
 if len(chs)<25:return dict(center=int(c),radius=rad,ball=len(vs),moves=len(chs),status='too_few')
 Z=np.array([zmove(Xmap,o,a) for o,a,t in chs]);p=np.array([t for o,a,t in chs],float);p=np.maximum(p,1e-300);p/=p.sum();F=np.array([feat(z) for z in Z]).T
 # row scaling with physical prior RMS
 sc=np.sqrt((F*F)@p);sc[sc<1e-14]=1;Fs=F/sc[:,None]
 # preserve the total shear kinetic strength; otherwise a fake solution can
 # satisfy anisotropy constraints by selecting almost-zero-shear channels.
 sp=np.array([shear_power(z) for z in Z]);sp0=float(sp@p);sps=sp/max(sp0,1e-300)
 # feasibility: 19 bad components =0, shear power/prior=1, probability=1
 Ae=np.vstack([Fs,sps,np.ones(len(p))]);be=np.r_[np.zeros(19),1.,1.]
 lp=linprog(np.zeros(len(p)),A_eq=Ae,b_eq=be,bounds=(0,None),method='highs')
 raw=np.linalg.norm(Fs@p);out=dict(center=int(c),radius=rad,ball=len(vs),moves=len(chs),feasible=bool(lp.success),raw_feature=float(raw),prior_shear_power=sp0,prior=km_metrics(Z,p),local_eigs=[float(x) for x in w[1:4]],Qwhite=Qw.tolist())
 if not lp.success:return out
 # max entropy projection of physical prior with exact bad-feature cancellation
 # and fixed shear-power constraint. Dual uses constraints C q = target.
 C=np.vstack([Fs,sps[None,:]]);target=np.r_[np.zeros(19),1.]
 logp=np.log(p)
 def fun(lam):return logsumexp(logp-lam@C)+lam@target
 def jac(lam):
  x=logp-lam@C;x-=x.max();q=np.exp(x);q/=q.sum();return target-C@q
 res=minimize(fun,np.zeros(20),jac=jac,method='BFGS',options={'gtol':1e-10,'maxiter':3000})
 x=logp-res.x@C;x-=x.max();q=np.exp(x);q/=q.sum();fin=np.linalg.norm(Fs@q);kl=float(np.sum(q*np.log(np.maximum(q,1e-300)/p)));mult=q/p
 out.update(opt_success=bool(res.success),final_feature=float(fin),final_shear_power_ratio=float((sp@q)/sp0),KL=kl,p95mult=float(np.quantile(mult,.95)),maxmult=float(mult.max()),final=km_metrics(Z,q))
 return out
def main(path,ncent=6,seed=1):
 A=np.load(path,allow_pickle=True)['A'].astype(np.int8);N=len(A);Rglob=np.linalg.inv(np.eye(N)-RHO*A.astype(float));rng=np.random.default_rng(seed);centers=rng.choice(N,ncent,replace=False);all=[]
 for rad in [2,3]:
  for c in centers:
   o=solve_ball(A,Rglob,int(c),rad);all.append(o);print(json.dumps(o),flush=True)
 for rad in [2,3]:
  vv=[x for x in all if x['radius']==rad and x.get('feasible')]
  if vv:
   print('SUMMARY',N,rad,'feasible',len(vv),'/',ncent,'medianKL',np.median([x.get('KL',np.nan) for x in vv]),'median raw rms',np.median([x['prior']['rms'] for x in vv]),'median final rms',np.median([x.get('final',{}).get('rms',np.nan) for x in vv]),flush=True)
 open(f'results/hmix_local_N{N}.json','w').write(json.dumps(all,indent=2))
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 6,int(sys.argv[3]) if len(sys.argv)>3 else 1)
