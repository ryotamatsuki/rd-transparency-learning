#!/usr/bin/env python3
"""Independent general-parameter high-learning-cost Stage 4A checks.

This file intentionally does not import the project's old proof scripts.
It validates algebraic identities from primitive two-period payoff functions,
finds an exact counterexample to unconditional globality on unbounded quality
strategy spaces, and runs independent numerical finite-deviation regressions
for several non-normalized interior strategy boxes.

MATHEMATICAL SCOPE: generalized *compact-domain* sufficient theorem, subject
 to analytical existence of an L>0 small enough for all pricing continuations.
COMPUTATION DOES NOT REPLACE: the proof of uniform regularity and strong
 monotonicity given in audits/GENERAL_HIGH_COST_STAGE4A_2026-11-10.md.
"""
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
import sympy as S
from scipy.optimize import brentq, minimize_scalar

R=S.Rational
t,delta,d,L,pA,pB,Svar,Bvar=S.symbols('t delta d L pA pB s b', real=True)
ks,kb=S.symbols('ks kb', positive=True)
K=S.symbols('K', positive=True)
D_prim=(t-d+pA-pB)/(2*t)
q_prim=-d+L*D_prim
A_prim=S.factor(pA*(1-D_prim)+delta*(3*t-q_prim)**2/(18*t))
B_prim=S.factor(pB*D_prim+delta*(3*t+q_prim)**2/(18*t))
FOC_a=S.diff(A_prim,pA)
FOC_b=S.diff(B_prim,pB)
sol=S.solve((FOC_a,FOC_b),(pA,pB), dict=True)
assert len(sol)==1
pA_e=S.cancel(sol[0][pA]);pB_e=S.cancel(sol[0][pB])
De=S.factor(D_prim.subs({pA:pA_e,pB:pB_e}, simultaneous=True))
qe=-d+L*De
D_expected=(27*t*t-9*d*t-2*delta*d*L)/(2*(27*t*t-delta*L**2))
assert S.factor(De-D_expected)==0
Ae=S.cancel(A_prim.subs({pA:pA_e,pB:pB_e},simultaneous=True))
Be=S.cancel(B_prim.subs({pA:pA_e,pB:pB_e},simultaneous=True))

gA=S.factor(S.diff(Ae,L).subs(L,0))
gB=S.factor(S.diff(Be,L).subs(L,0))
h=delta*(3*t-d)**2/(54*t**2)
assert S.factor(gA+delta*(9*t-2*d)*(3*t+d)/(81*t**2))==0
assert S.factor(gB+2*delta*d*(3*t-d)/(81*t**2))==0
assert S.factor(S.diff(pA_e,L).subs(L,0)+delta*(9*t+d)/(27*t))==0

# Hidden B chooses price with A's period-1 price z fixed, and can change L.
z,Le=S.symbols('z Le',real=True)
B_br=S.solve([S.diff(B_prim.subs(pA,z),pB)],[pB])[pB]
Ddev=S.factor(D_prim.subs({pA:z,pB:B_br},simultaneous=True))
assert S.factor(Ddev-(9*t*(t-d+z)+delta*L*(3*t-d))/(36*t*t-delta*L**2))==0
Vdev=S.cancel(B_prim.subs({pA:z,pB:B_br}, simultaneous=True))
# Envelope evaluated with competitor's equilibrium first price and same investment
Vdev_equil_der=S.factor(S.diff(Vdev,L).subs(z,pA_e))
H_marg=delta*De*(3*t-d+L*De)/(9*t)
assert S.factor(Vdev_equil_der-H_marg)==0
assert S.factor(Vdev_equil_der.subs(L,0)-h)==0

c=(1+delta)/(9*t)
Delta=ks*kb-c*(ks+kb)
uA=S.factor(gA*h)
uB=S.factor(gB*h-h*h/2)
ua_prime=S.factor(S.diff(uA,d)); ub_prime=S.factor(S.diff(uB,d))
assert S.factor(ua_prime-delta**2*(3*t-d)*(-8*d*d+21*d*t+45*t*t)/(4374*t**4))==0
assert S.factor(ub_prime-delta**2*(3*t-d)**2*(5*d+3*t)/(4374*t**4))==0
S1=S.factor(((kb-c)*ua_prime+c*ub_prime)/Delta)
B1=S.factor(-(c*ua_prime+(ks-c)*ub_prime)/Delta)
FAprime=(1+delta)*(3*t+d)/(9*t)
FBprime=-(1+delta)*(3*t-d)/(9*t)
phiA=S.factor(uA-FAprime*B1)
phiB=S.factor(uB+FBprime*S1)
profitA_condition=S.factor(delta*(9*t-2*d)*h/(9*t*(1+delta))+B1)
assert S.factor(phiA+(1+delta)*(3*t+d)*profitA_condition/(9*t))==0
# Welfare independently from primitive consumer quality and transport costs
D2=(3*t+qe)/(6*t)
Wop=((1+delta)*Svar-d*(De+delta*D2)+delta*L*De*D2
     -t/2*((1-De)**2+De**2+delta*((1-D2)**2+D2**2)))
Wlam=S.factor(S.diff(Wop,L).subs(L,0))
assert S.factor(Wlam-delta*(23*d*d-72*d*t+81*t*t)/(324*t*t))==0
W_learning=S.factor(h*Wlam-h*h/2)
assert S.factor(W_learning-h*delta*(10*d*d-27*d*t+27*t*t)/(162*t*t))==0
# Independent welfare investment derivatives (at zero learning)
Wfull=Wop-ks*Svar**2/2-kb*Bvar**2/2-K*L**2/2
W_s=S.factor(S.diff(Wfull,Svar)+S.diff(Wfull,d))
W_b=S.factor(S.diff(Wfull,Bvar)-S.diff(Wfull,d))
sstar=FAprime/ks
bstar=-FBprime/kb
assert S.factor(W_s.subs({L:0,Svar:sstar})-(1+delta)*(t+d)/(6*t))==0
assert S.factor(W_b.subs({L:0,Bvar:bstar})-(1+delta)*(t-d)/(6*t))==0
Wcoeff=S.factor(W_learning+(1+delta)/(6*t)*((t+d)*S1+(t-d)*B1))

# EXACT counterexample satisfying *all posted algebraic sufficient conditions*,
# where an unbounded s deviation enters the corner-price monopoly regime.
example={t:R(1),delta:R(1),ks:R(4,5),kb:R(4),}
cc=c.subs(example)
d_star=S.factor((1+3*cc*(1/example[ks]-1/example[kb]))/
                 (1-cc*(1/example[ks]+1/example[kb])))
s_star=S.factor((cc*(3+d_star)/example[ks]))
b_star=S.factor((cc*(3-d_star)/example[kb]))
assert (d_star,s_star,b_star)==(R(5,2),R(55,36),R(1,36))
condVal=S.factor(profitA_condition.subs({**example,d:d_star}))
assert condVal==R(125,559872)>0
assert Delta.subs(example)>0
p_static=S.factor(2*(3+d_star)**2/18-example[ks]*s_star**2/2)
s_dev=S.factor(2/example[ks])
d_dev=S.factor(1+s_dev-b_star)
assert d_dev>3
p_corner=S.factor(2*(d_dev-1)-example[ks]*s_dev**2/2)
gain=S.factor(p_corner-p_static)
assert p_static==R(1573,648) and p_corner==R(22,9) and gain==R(11,648)
print('EXACT GENERAL THEOREM CORNER COUNTEREXAMPLE:',dict(
    delta='1',t='1',d0='1',ks='4/5',kb='4',dstar=str(d_star),
    sstar=str(s_star),bstar=str(b_star),AconditionMargin=str(condVal),
    A_monopoly_deviation_s=str(s_dev),A_monopoly_deviation_gap=str(d_dev),
    original_A_profit=str(p_static),deviation_A_profit=str(p_corner),
    gain=str(gain)))
print('SYMBOLIC GENERAL MODEL IDENTITIES: PASS')

# Fresh direct-payoff numerical tests of multiple NON-NORMALIZED parameter sets.
# All games use compact s,b domains which keep 0<d<3t; learning cap small.
def D1(dv,lam,tv,delv):
    return (27*tv*tv-9*dv*tv-2*delv*dv*lam)/(2*(27*tv*tv-delv*lam*lam))

def prices(dv,lam,tv,delv):
    x=D1(dv,lam,tv,delv)
    q=-dv+lam*x
    return (2*tv*(1-x)-delv*lam*(3*tv-q)/(9*tv),
            2*tv*x-delv*lam*(3*tv+q)/(9*tv))

def hidden_lambda(dv, kv,tv,delv,lcap):
    def ff(lam):
        x=D1(dv,lam,tv,delv)
        return kv*lam-delv*x*(3*tv-dv+lam*x)/(9*tv)
    assert ff(0)<0 and ff(lcap)>0, (dv,kv,tv,delv)
    return brentq(ff,0,lcap,xtol=1e-14)

def direct_profit(sv,bv,tv,delv,d0v,kav,kbv,klv,lcap,regime):
    dv=d0v+sv-bv
    lam=0 if regime=='public' else hidden_lambda(dv,klv,tv,delv,lcap)
    x=D1(dv,lam,tv,delv)
    q=-dv+lam*x
    pa,pb=prices(dv,lam,tv,delv)
    return (pa*(1-x)+delv*(3*tv-q)**2/(18*tv)-kav*sv**2/2,
            pb*x+delv*(3*tv+q)**2/(18*tv)-kbv*bv**2/2-klv*lam**2/2,
            lam,x,q,pa,pb)

def hidden_dev_b_value(dv, lam, z, tv, delv, klv):
    x=(9*tv*(tv-dv+z)+delv*lam*(3*tv-dv))/(36*tv*tv-delv*lam**2)
    pb=tv-dv+z-2*tv*x
    q=-dv+lam*x
    return pb*x+delv*(3*tv+q)**2/(18*tv)-klv*lam**2/2

# The first four entries deliberately perturb delta, d0, ks/kb and t.
CASES=[
 dict(t=1.0,delta=1.0,d0=1.0,ks=4.0,kb=4.0,S=0.5,B=0.5,L=0.2,K=20.),
 dict(t=1.0,delta=0.5,d0=1.0,ks=4.0,kb=4.0,S=0.5,B=0.5,L=0.2,K=20.),
 dict(t=1.0,delta=0.75,d0=1.2,ks=4.0,kb=5.0,S=0.5,B=0.5,L=0.2,K=20.),
 dict(t=2.0,delta=1.0,d0=2.0,ks=2.0,kb=2.0,S=1.,B=1.,L=0.4,K=20.),
 dict(t=1.0,delta=0.8,d0=1.05,ks=3.0,kb=5.0,S=0.5,B=0.5,L=0.2,K=20.),
 dict(t=1.0,delta=0.6,d0=1.2,ks=8.0,kb=7.0,S=0.5,B=0.5,L=0.2,K=20.)
]

def max1d(f,lo,hi):
    grid=np.linspace(lo,hi,240)
    vals=np.array([f(float(x)) for x in grid])
    bestj=int(np.argmax(vals))
    cands=[(float(vals[bestj]),float(grid[bestj])), (float(vals[0]),float(lo)),(float(vals[-1]),float(hi))]
    for j in range(1,len(grid)-1):
        if vals[j]>=vals[j-1] and vals[j]>=vals[j+1]:
            m=minimize_scalar(lambda x:-f(x),bounds=(grid[j-1],grid[j+1]),method='bounded',options={'xatol':1e-13})
            cands.append((-float(m.fun),float(m.x)))
    return max(cands)

if __name__=='__main__':
    rows=[]
    for C in CASES:
        tv=C['t'];dv=C['delta'];d0v=C['d0'];kav=C['ks'];kbv=C['kb'];klev=C['K'];lcap=C['L']
        cval=(1+dv)/(9*tv)
        dstar=(d0v+3*tv*cval*(1/kav-1/kbv))/(1-cval*(1/kav+1/kbv))
        sv=cval*(3*tv+dstar)/kav;bv=cval*(3*tv-dstar)/kbv
        assert 0<sv<C['S'] and 0<bv<C['B']
        assert 0<d0v-C['B']<d0v+C['S']<3*tv
        assert dstar>=tv
        # independent B stage 1, and A/B stage0 Nash solve via scipy root
        from scipy.optimize import root
        def grad(si,bi):
            eps=2e-5
            return [
              (direct_profit(si+eps,bi,tv,dv,d0v,kav,kbv,klev,lcap,'hidden')[0]
               -direct_profit(si-eps,bi,tv,dv,d0v,kav,kbv,klev,lcap,'hidden')[0])/(2*eps),
              (direct_profit(si,bi+eps,tv,dv,d0v,kav,kbv,klev,lcap,'hidden')[1]
               -direct_profit(si,bi-eps,tv,dv,d0v,kav,kbv,klev,lcap,'hidden')[1])/(2*eps)
            ]
        solN=root(lambda x:grad(*x),[sv,bv],tol=1e-11)
        assert np.linalg.norm(solN.fun)<1e-7,(C,solN.message)
        sh,bh=map(float,solN.x)
        assert 0<sh<C['S'] and 0<bh<C['B']
        a,b,lh,x,q,pA0,pB0=direct_profit(sh,bh,tv,dv,d0v,kav,kbv,klev,lcap,'hidden')
        gA=max1d(lambda si:direct_profit(si,bh,tv,dv,d0v,kav,kbv,klev,lcap,'hidden')[0],0,C['S'])
        gB=max1d(lambda bi:direct_profit(sh,bi,tv,dv,d0v,kav,kbv,klev,lcap,'hidden')[1],0,C['B'])
        gL=max1d(lambda lam:hidden_dev_b_value(d0v+sh-bh,lam,pA0,tv,dv,klev),0,lcap)
        gainA=gA[0]-a
        gainB=gB[0]-b
        bbase=hidden_dev_b_value(d0v+sh-bh,lh,pA0,tv,dv,klev)
        gainL=gL[0]-bbase
        assert max(gainA,gainB,gainL)<2e-7,(C,gainA,gainB,gainL)
        baseA,baseB,*_=direct_profit(sv,bv,tv,dv,d0v,kav,kbv,klev,lcap,'public')
        assert baseA>a and baseB>b
        assert sh>sv and bh<bv and lh>0
        # Independent public-learning global comparison at all lambda in [0,L].
        def public_b_operating(lam):
            gap=d0v+sv-bv
            x=D1(gap,lam,tv,dv)
            q=-gap+lam*x
            pa,pb=prices(gap,lam,tv,dv)
            return pb*x+dv*(3*tv+q)**2/(18*tv)-klev*lam**2/2
        pubopt=max1d(public_b_operating,0,lcap)
        public_margin=pubopt[0]-public_b_operating(0.0)
        assert abs(pubopt[1])<1e-10 and public_margin<2e-7
        pub_a=max1d(lambda si:direct_profit(si,bv,tv,dv,d0v,kav,kbv,klev,lcap,'public')[0],0,C['S'])
        pub_b=max1d(lambda bi:direct_profit(sv,bi,tv,dv,d0v,kav,kbv,klev,lcap,'public')[1],0,C['B'])
        assert abs(pub_a[1]-sv)<1e-6 and abs(pub_b[1]-bv)<1e-6
        # Search for alternative interior pure Nash roots from dispersed starts.
        roots=[]
        for start_s in np.linspace(.02*C['S'],.98*C['S'],5):
            for start_b in np.linspace(.02*C['B'],.98*C['B'],5):
                cand=root(lambda x:grad(*x),[start_s,start_b],tol=1e-10)
                if np.linalg.norm(cand.fun)<1e-6 and np.all(np.isfinite(cand.x)):
                    if 0<=cand.x[0]<=C['S'] and 0<=cand.x[1]<=C['B']:
                        if not any(np.linalg.norm(cand.x-prev)<1e-6 for prev in roots):
                            roots.append(cand.x.copy())
        assert len(roots)==1 and np.linalg.norm(roots[0]-np.array([sh,bh]))<1e-6
        # welfare recomputed from primitive consumer-integral formula
        def welfare(sv,bv,lam,x,q):
            x2=(3*tv+q)/(6*tv)
            return ((1+dv)*sv-(d0v+sv-bv)*(x+dv*x2)+dv*lam*x*x2-
                    tv/2*((1-x)**2+x*x+dv*((1-x2)**2+x2*x2))-
                    kav*sv*sv/2-kbv*bv*bv/2-klev*lam*lam/2)
        xP=(3*tv-dstar)/(6*tv)
        Wh=welfare(sh,bh,lh,x,q);Wp=welfare(sv,bv,0,xP,-dstar)
        assert Wh>Wp,(C,Wh,Wp)
        rows.append(dict(parameters=C,public=[sv,bv,0.0,baseA,baseB,Wp],
                         hidden=[sh,bh,lh,a,b,Wh],
                         best_response_gains=dict(A=gainA,B=gainB,hidden_learning=gainL,public_learning=public_margin),
                         alternative_interior_pure_roots=len(roots),
                         best_response_actions=dict(A=gA[1],B=gB[1],hidden_learning=gL[1])))
        print('NUMERIC PURE-STRATEGY FINITE-DEVIATION PASS:',C,'gains:',gainA,gainB,gainL)
    path=Path('general_high_cost_numeric_results.json')
    path.write_text(json.dumps(rows,indent=2))
    print('WROTE',path)
    print('PASS: all checked symbolic identities, exact boundary counterexample and numerical regressions')