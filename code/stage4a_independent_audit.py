#!/usr/bin/env python3
"""Minimal Stage 4A independent algebraic audit (2026-11-10).

Rebuild payoffs from demand/utility and solve price FOCs WITHOUT importing
code/finite_cost_proof.py or copying its symbolic payoff formula. Then certify
selected global sign/curvature properties via an independent Bernstein
implementation and attack Stage-0/1 by multistart finite deviations.

Scope strictly: t=delta=d0=1, ks=kb=4, s,b in [0,1/2], lambda in [0,1],
learning cost k > 4343/32448, pure strategies. No claim of theorem novelty,
formal proof-assistant verification or exclusion of mixed PBE.
"""
from __future__ import annotations
import json
import os
from itertools import product
from math import comb
import numpy as np
import sympy as S
from scipy.optimize import minimize_scalar, root_scalar

r=S.Rational
a,bp,d,L,Z,X,Y=S.symbols('pa pb d L Z X Y', real=True)
D=S.expand((1-d+a-bp)/2)
q=-d+L*D
future_A=(3-q)**2/18
future_B=(3+q)**2/18
payo_A=S.expand(a*(1-D)+future_A)
payo_B=S.expand(bp*D+future_B)
FOC_A=S.factor(S.diff(payo_A,a))
FOC_B=S.factor(S.diff(payo_B,bp))
sol=S.solve([FOC_A,FOC_B],[a,bp], dict=True)
assert len(sol)==1
pp=sol[0]
AA=S.cancel(pp[a]); BB=S.cancel(pp[bp]); DD=S.cancel(D.subs(pp, simultaneous=True)); QQ=S.cancel(q.subs(pp, simultaneous=True))
print('Price FOCs derived independently:',FOC_A,FOC_B)
print('D:', S.factor(DD))
assert S.factor(DD-(27-(9+2*L)*d)/(2*(27-L*L)))==0
assert S.factor(AA-(2*(1-DD)-L*(3-QQ)/9))==0
assert S.factor(BB-(2*DD-L*(3+QQ)/9))==0

# Stage-1 hidden B chooses price (equiv. share) and privately chooses lambda.
# Reconstruct directly from price constraint pB=(1-d+Z)-2D to avoid original V_B.
Dchoice=S.symbols('Dchoice', real=True)
P_B_choice=1-d+Z-2*Dchoice
Vb_choice=S.expand(P_B_choice*Dchoice+(3-d+L*Dchoice)**2/18)
FOC_share=S.factor(S.diff(Vb_choice,Dchoice))
Dchoice_opt=S.solve(FOC_share,Dchoice)[0]
P_B_dev=S.cancel(P_B_choice.subs(Dchoice,Dchoice_opt));
Gdev=S.cancel(Vb_choice.subs(Dchoice,Dchoice_opt))
assert S.factor(S.diff(Vb_choice,Dchoice,2)+4-L*L/9)==0
print('Hidden deviator reoptimized D:', S.factor(Dchoice_opt))

# All numeric global checks are confined to pure-strategy normal form.
# Certify rational signs using an independent power-basis->Bernstein converter.
def bmin(pol, subst, variables):
    expr=S.together(S.expand(pol.subs(subst, simultaneous=True)))
    p=S.Poly(expr,*variables,domain=S.QQ)
    # Strip factors such as Y**2: positive on the strict interior, zero
    # only at the excluded L=0 boundary. Certify remaining polynomial.
    exponents=[m for m,c in p.terms()]
    common=tuple(min(ex[j] for ex in exponents) for j in range(len(variables)))
    if any(common):
        divisor=S.prod(variables[j]**common[j] for j in range(len(variables)))
        p=S.Poly(S.cancel(p.as_expr()/divisor),*variables,domain=S.QQ)
    deg=p.degree_list()
    lo=None
    # degree-elevated Bernstein coefficients for tensor-product cube [0,1]^n.
    dic=dict(p.terms())
    for ids in product(*[range(k+1) for k in deg]):
        s=S.Integer(0)
        for exps,c in dic.items():
            if all(exps[j]<=ids[j] for j in range(len(ids))):
                s+=c*S.prod(r(comb(ids[j],exps[j]),comb(deg[j],exps[j])) for j in range(len(ids)))
        lo=s if lo is None or s<lo else lo
    return lo

def certify(label, rational_expr, substitution, variables):
    top,bot=map(S.factor,S.cancel(rational_expr).as_numer_denom())
    # SymPy may canonicalize an entire rational expression with both
    # numerator and denominator negative. Normalize by denominator sign at
    # an interior reference point, and independently certify both signs.
    middle={v:S.Rational(1,2) for v in variables}
    denominator_sign=S.sign(S.factor(bot.subs(substitution,simultaneous=True).subs(middle)))
    assert denominator_sign in (-1,1)
    nt=bmin(denominator_sign*top,substitution,variables)
    dt=bmin(denominator_sign*bot,substitution,variables)
    if nt<=0 or dt<=0:
        print('UNRESOLVED exact Bernstein positivity',label,'bounds',nt,dt)
        return False
    print('EXACT POSITIVE',label,'lower numerator',str(nt)[:50], 'lower denominator',str(dt)[:50])
    return True

# Full rectangle for all possible stage-0 s,b and all learning choices.
subst={d:r(1,2)+X,L:Y}
# B's hidden price optimization must remain interior over the full
# incumbent price range given by the on-path price equilibrium.
subst_hidden={d:r(1,2)+X,L:Y,Z:r(4,5)+r(4,5)*S.symbols('Zscaled',real=True)}
Zscaled=list(subst_hidden[Z].free_symbols)[0]
checks=[]
for name,expr,subs,vars in [
    ('D_onpath>0',DD,subst,[X,Y]),
    ('D_onpath<1',1-DD,subst,[X,Y]),
    ('pA_onpath>4/5',AA-r(4,5),subst,[X,Y]),
    ('pA_onpath<8/5',r(8,5)-AA,subst,[X,Y]),
    ('pB_onpath>0',BB,subst,[X,Y]),
    ('hidden Ddev>0',Dchoice_opt,subst_hidden,[X,Y,Zscaled]),
    ('hidden Ddev<1',1-Dchoice_opt,subst_hidden,[X,Y,Zscaled]),
    ('hidden pBdev>0',P_B_dev,subst_hidden,[X,Y,Zscaled]),
    ('hidden gross payoff concavity bound Gll<1/10',r(1,10)-S.diff(Gdev,L,2),subst_hidden,[X,Y,Zscaled]),
]:
    checks.append(certify(name,expr,subs,vars))
assert all(checks),'Exact certificate failed; not authorized to claim global price/interiority.'

# Fresh derivation for public stage-1 values after A reprices to public lambda.
VA=S.cancel(payo_A.subs(pp,simultaneous=True))
VB=S.cancel(payo_B.subs(pp,simultaneous=True))
assert certify('public V_B(d,0)-V_B(d,L)>0 for L>0',
                S.cancel((VB.subs(L,0)-VB)/L),subst,[X,Y])

# Stage-1 optimal lambda when pA believes its equilibrium value.
# At symmetric period-1 price equilibrium z=AA(d,l), B's dG/dlambda
# (holding z fixed) divided by l must equal k when l>0.
Gdiff=S.factor(S.diff(Gdev,L))
K=S.cancel(Gdiff.subs(Z,AA)/(L))
assert S.factor(Gdiff.subs(Z,AA)-L*K)==0
# Three multiplicative factors are verified as positive after cancellation.
assert certify('-K_d>0',-S.diff(K,d),subst,[X,Y])
assert certify('-K_l>0',-S.diff(K,L),subst,[X,Y])
Kthreshold=S.factor(K.subs({d:r(1,2),L:1}))
assert Kthreshold==r(4343,32448)
assert S.simplify(Kthreshold-K.subs({d:r(19,16),L:r(1,2)}))>0
print('THRESHOLD', Kthreshold, 'K(19/16,1/2)',S.factor(K.subs({d:r(19,16),L:r(1,2)})))

# Stage 0: FOCs along implicit level set K(d,L)=k.
# Symbolically differentiate l(d;k) via implicit-function theorem.
lprime=S.cancel(-S.diff(K,d)/S.diff(K,L))
first_A=S.cancel(S.diff(VA,d)+S.diff(VA,L)*lprime)
first_B=S.cancel(S.diff(VB,d)+(S.diff(VB,L)-K*L)*lprime)
second_A=S.cancel(S.diff(first_A,d)+S.diff(first_A,L)*lprime)
second_B=S.cancel(S.diff(first_B,d)+S.diff(first_B,L)*lprime)
for name,expr in [('TA_prime>0',first_A),('TA_prime<2',2-first_A),
                  ('TB_prime<0',-first_B),('TB_prime>-2',2+first_B),
                  ('TA_second<2',2-second_A),('TB_second<2',2-second_B)]:
    assert certify(name,expr,subst,[X,Y])
print('ANALYTIC CONSEQUENCE: Since 0<TA_prime<2 and -2<TB_prime<0, all stage-0 candidates lie in the action interior.')
print('ANALYTIC CONSEQUENCE: Stage-0 net own-action curvature is TA_second-4 or TB_second-4, both <-2.')
print('ANALYTIC CONSEQUENCE: Scalar F(d)=d-1-(TA_prime+TB_prime)/4 has F_prime>0 over [1/2,3/2]; F endpoints have opposite signs; hence exactly one pure Stage-0 profile.')

# A second implementation-independent route to the main sign comparisons:
# form original consumer utility integral and firm profits from the newly
# derived equilibrium, then certify signs across a rectangular wedge that
# contains the unique hidden stage-0 root for every k > k_threshold.
ss=S.cancel(first_A/4)
bb=S.cancel(-first_B/4)
FP=S.cancel(4*(d-1)-first_A-first_B)
FN,FD=S.cancel(FP).as_numer_denom()
# Symbolic root boundaries, checked using F itself (not the old polynomial).
low=r(9,8)+L/8
high=r(9,8)+L/5
subsb={L:X/2,d:r(9,8)+(X/2)*(r(1,8)+r(3,40)*Y)}
subsl={L:X/2}
assert certify('F(lower)<0', -FP.subs(d,low), subsl,[X])
assert certify('F(upper)>0', FP.subs(d,high), subsl,[X])
# CAUTION: partial_d at fixed L is NOT total_d along a fixed-k level set.
# Explicitly certify the partial derivative here for wedge uniqueness.
assert certify('partial_d F(d,L)>0 at fixed L',S.diff(FP,d),subsb,[X,Y])
assert certify('partial_L F(d,L)<0 at fixed d',-S.diff(FP,L),subsb,[X,Y])
# Together with boundary signs and fixed-L monotonicity, this proves
# exactly one d root in the wedge for each L.
assert certify('ss > 11/48',ss-r(11,48),subsb,[X,Y])
assert certify('bb < 5/48',r(5,48)-bb,subsb,[X,Y])
G_A=S.cancel(VA-2*ss**2)
G_B=S.cancel(VB-2*bb**2-K*L**2/2)
A_P=r(2057,1152); B_P=r(425,1152)
assert certify('public A profit > hidden',A_P-G_A,subsb,[X,Y])
assert certify('public B profit > hidden',B_P-G_B,subsb,[X,Y])
D2=S.cancel((3+QQ)/6)
transport=lambda z: ((1-z)**2+z*z)/2
W=S.cancel(2*ss-d*(DD+D2)+L*DD*D2-transport(DD)-transport(D2)-2*ss**2-2*bb**2-K*L**2/2)
assert certify('hidden W > public W',W+r(1085,1152),subsb,[X,Y])
assert certify('hidden D1 < public D1',r(5,16)-DD,subsb,[X,Y])
assert certify('hidden D2 > public D2',D2-r(5,16),subsb,[X,Y])
print('ANALYTIC CONSEQUENCE: a single monotonic scalar root lies in the exact wedge and all substantive payoff/share signs hold throughout the wedge.')


# Independently sample global deviation gains using direct cashflows, not the
# just-derived closed-form stage0 gradient; root solve lambda by G'(d,L,z)-kL.
num_pA=S.lambdify((d,L),AA,'numpy')
num_pB=S.lambdify((d,L),BB,'numpy')
num_D=S.lambdify((d,L),DD,'numpy')
num_K=S.lambdify((d,L),K,'numpy')
num_G=S.lambdify((d,L,Z),Gdev,'numpy')
num_lfirst=S.lambdify((d,L),first_A,'numpy')
num_bfirst=S.lambdify((d,L),first_B,'numpy')
num_Bdev=S.lambdify((d,L,Z),P_B_dev,'numpy')


def learning(dval,k):
    assert k>float(Kthreshold)
    return root_scalar(lambda l:num_K(dval,l)-k,bracket=[1e-12,1.0],xtol=1e-13).root

def netprofits(s,b,k):
    dv=1+s-b
    lam=learning(dv,k)
    Dv=num_D(dv,lam)
    qv=-dv+lam*Dv
    Ap=num_pA(dv,lam); Bp=num_pB(dv,lam)
    return (Ap*(1-Dv)+(3-qv)**2/18-2*s*s,
            Bp*Dv+(3+qv)**2/18-2*b*b-k*lam*lam/2)

def bracket_all(f,lo=0,hi=0.5,N=251):
    """Numerical stress test: dense mesh + local optimizations per basin."""
    # Include logarithmic near-boundary probes; at k=100 the true learning
    # optimum is below a uniform 251-point mesh spacing.
    xs=np.unique(np.r_[np.linspace(lo,hi,N), lo+np.geomspace(1e-10,hi-lo,150)])
    ys=np.array([f(x) for x in xs]); cand=[(ys[0],xs[0]),(ys[-1],xs[-1])]
    for j in range(1,len(xs)-1):
        if ys[j]<=min(ys[j-1],ys[j+1]):
            r0=minimize_scalar(f,method='bounded',bounds=(xs[j-1],xs[j+1]),options={'xatol':1e-12})
            cand.append((r0.fun,r0.x))
    return min(cand,key=lambda z:z[0]), len(cand)-2

metrics=[]
for k in (0.134,0.15,0.3,1.0,3.0,20.0,100.0):
    def F(dv):
        ll=learning(dv,k)
        return dv-1-(num_lfirst(dv,ll)+num_bfirst(dv,ll))/4
    # Sample sign monotonicity and search ALL root brackets on 251 grid pts.
    xgrid=np.linspace(.5,1.5,251)
    Fvals=[F(float(x)) for x in xgrid]
    root_intervals=[(float(xgrid[i]),float(xgrid[i+1])) for i in range(len(xgrid)-1)
          if Fvals[i]*Fvals[i+1]<0]
    assert len(root_intervals)==1,(k,root_intervals)
    dsol=root_scalar(F,bracket=root_intervals[0],xtol=1e-13).root
    lsol=learning(dsol,k)
    seq=num_lfirst(dsol,lsol)/4;beq=-num_bfirst(dsol,lsol)/4
    assert abs(1+seq-beq-dsol)<1e-9
    paeq=num_pA(dsol,lsol)
    payoff=netprofits(seq,beq,k)
    BRa,na=bracket_all(lambda sval:-netprofits(sval,beq,k)[0])
    BRb,nb=bracket_all(lambda bval:-netprofits(seq,bval,k)[1])
    BRlambda,nl=bracket_all(lambda lv:-num_G(dsol,lv,paeq)+k*lv*lv/2,0,1,251)
    gainA=-BRa[0]-payoff[0]; gainB=-BRb[0]-payoff[1]
    gainL=(-BRlambda[0]-(num_G(dsol,lsol,paeq)-k*lsol*lsol/2))
    assert abs(BRa[1]-seq)<1e-5 and abs(BRb[1]-beq)<1e-5 and abs(BRlambda[1]-lsol)<1e-5,(k,BRa,BRb,BRlambda)
    assert max(gainA,gainB,gainL)<1e-8
    metrics.append(dict(k=k,d=dsol,lam=lsol,s=seq,b=beq,stage0A_gain=gainA,stage0B_gain=gainB,hiddenLambda_gain=gainL,number_F_brackets=len(root_intervals),local_minima=[na,nb,nl]))
    print('MULTISTART',json.dumps(metrics[-1]))

with open(os.environ.get('RD_STAGE4A_OUTPUT','stage4a_independent_numerical_results.json'),'w',encoding='utf-8') as f:
    json.dump(metrics,f,indent=2)
print('PASS exact algebraic sign and independent multistart numerical pure-strategy checks within stated domains.')
print('LIMITATIONS no pure-strategy theorem outside compact action or cost bound; no mixed PBE exclusion; no formal proof assistant; independent symbolic certificates require human audit.')