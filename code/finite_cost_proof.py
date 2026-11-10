"""Exact algebraic verification of the finite-cost R&D-disclosure theorem.

SymPy proves all stated polynomial inequalities using rational Bernstein
coefficients, rather than floating-point parameter-grid checks.
Run: python rd_disclosure_finite_threshold_proof.py
Requires: sympy, scipy (only for equilibrium display).
"""
from itertools import product
from math import comb
import sympy as sp
from scipy.optimize import root

Q = sp.Rational
d, ell, z, u, v, w = sp.symbols('d ell z u v w', real=True)

# Base model: t=delta=d0=1, k_s=k_b=4.
D = sp.cancel((27-(9+2*ell)*d)/(2*(27-ell**2)))
q = -d + ell*D
pa = 2*(1-D)-ell*(3-q)/9
pb = 2*D-ell*(3+q)/9
Va = sp.cancel(pa*(1-D)+(3-q)**2/18)
Vb = sp.cancel(pb*D+(3+q)**2/18)
R = sp.cancel(D*(3+q)/(9*ell)) # k_lambda implied by hidden FOC
ell_d = sp.cancel(-sp.diff(R,d)/sp.diff(R,ell))
TA = sp.factor(sp.diff(Va,d)+sp.diff(Va,ell)*ell_d)
TB = sp.factor(sp.diff(Vb,d)+(sp.diff(Vb,ell)-R*ell)*ell_d)
s = sp.cancel(TA/4)
b = sp.cancel(-TB/4)
P = sp.cancel(4*(d-1)-TA-TB)
Pnum,Pden = P.as_numer_denom()

# Closed-form payoff and welfare functions (R as equilibrium cost coefficient).
Afull = sp.cancel(Va-2*s**2)
Bfull = sp.cancel(Vb-2*b**2-R*ell**2/2)
AP = sp.factor(Afull.subs({d:Q(9,8), ell:0}))
BP = sp.factor(Bfull.subs({d:Q(9,8),ell:0}))
D2 = sp.cancel((3+q)/6)
W = sp.cancel(2*s-d*(D+D2)+ell*D*D2
              -((1-D)**2+D**2+(1-D2)**2+D2**2)/2
              -2*s**2-2*b**2-R*ell**2/2)
WP = sp.factor(W.subs({d:Q(9,8),ell:0}))


def bernstein_min(poly, subst, variables):
    """Exact minimum Bernstein coefficient on a unit hypercube."""
    poly = sp.Poly(sp.expand(poly.subs(subst, simultaneous=True)),
                   *variables, domain=sp.QQ)
    # Remove common nonnegative powers of unit-cube coordinates.
    terms = poly.terms()
    powers = tuple(min(exp[j] for exp, _ in terms) for j in range(len(variables)))
    if any(powers):
        divisor = sp.prod(var**power for var,power in zip(variables,powers))
        poly = sp.Poly(sp.cancel(poly.as_expr()/divisor),*variables,domain=sp.QQ)
    degrees = [poly.degree(t) for t in variables]
    terms = poly.terms()
    vals=[]
    for ij in product(*[range(k+1) for k in degrees]):
        val = sum(c*sp.prod(Q(comb(i,h),comb(k,h)) for i,h,k in
                            zip(ij,exps,degrees))
                  for exps,c in terms if all(h<=i for h,i in zip(exps,ij)))
        vals.append(val)
    return min(vals)


def prove_positive(label,expr,subst,variables,point):
    """Certified positivity of a rational expression on the open cube."""
    n,den = sp.cancel(expr).as_numer_denom()
    sig_n = sp.sign(n.subs(point)); sig_d=sp.sign(den.subs(point))
    assert sig_n in (-1,1) and sig_n==sig_d, (label,'incorrect reference sign')
    low_n=bernstein_min(sig_n*n,subst,variables)
    low_d=bernstein_min(sig_d*den,subst,variables)
    assert low_n>0 and low_d>0, (label,'nonpositive Bernstein bound',low_n,low_d)
    print(f'CERTIFIED {label:40s} min numerator={float(low_n):.4g}; denominator={float(low_d):.4g}')


# Wedge for the physical, unique equilibrium branch: ell in (0,1/2].
subst_wedge={ell:u/2,d:Q(9,8)+(u/2)*(Q(1,8)+Q(3,40)*v)}
point_wedge={d:Q(23,20),ell:Q(1,5)}
# Existence and uniqueness of d(ell), with bounds on its slope.
prove_positive('P(d=9/8+ell/8,ell) < 0',
  -Pnum.subs(d,Q(9,8)+ell/8),{ell:u/2},[u],{ell:Q(1,5)})
prove_positive('P(d=9/8+ell/5,ell) > 0',
   Pnum.subs(d,Q(9,8)+ell/5),{ell:u/2},[u],{ell:Q(1,5)})
prove_positive('P_d > 0',sp.diff(Pnum,d),subst_wedge,[u,v],point_wedge)
prove_positive('-P_ell > 0',-sp.diff(Pnum,ell),subst_wedge,[u,v],point_wedge)
prove_positive('P denominator > 0',Pden,subst_wedge,[u,v],point_wedge)

# Five equilibrium comparisons on the entire wedge, not sampled values.
for label,expression in [
    ('s_H > s_P',s-Q(11,48)),
    ('b_H < b_P',Q(5,48)-b),
    ('profit A_P > A_H',AP-Afull),
    ('profit B_P > B_H',BP-Bfull),
    ('W_H > W_P',W-WP),
]:
    prove_positive(label,expression,subst_wedge,[u,v],point_wedge)

# Stronger corollaries: market-share reversal and period-wise gross surplus.
T1 = sp.cancel(s-d*D-((1-D)**2+D**2)/2)
T2 = sp.cancel(s+q*D2-((1-D2)**2+D2**2)/2)
for label, expression in [
    ('B first-period share lower under secrecy',Q(5,16)-D),
    ('B second-period share higher under secrecy',D2-Q(5,16)),
    ('B second-period relative quality higher',q+Q(9,8)),
    ('first-period market surplus higher under secrecy',T1-T1.subs({d:Q(9,8),ell:0})),
    ('second-period market surplus higher under secrecy',T2-T2.subs({d:Q(9,8),ell:0})),
]:
    prove_positive(label,expression,subst_wedge,[u,v],point_wedge)

# Extended algebraic equilibrium branch down to k_lambda >= 1/10.
subst_wedge01={ell:Q(3,5)*u, d:Q(9,8)+Q(3,5)*u*(Q(1,8)+Q(3,40)*v)}
prove_positive('extended P lower boundary < 0',
    -Pnum.subs(d,Q(9,8)+ell/8),{ell:Q(3,5)*u},[u],{ell:Q(1,5)})
prove_positive('extended P upper boundary > 0',
    Pnum.subs(d,Q(9,8)+ell/5),{ell:Q(3,5)*u},[u],{ell:Q(1,5)})
prove_positive('extended P_d > 0',sp.diff(Pnum,d),subst_wedge01,[u,v],point_wedge)
prove_positive('extended -P_ell > 0',-sp.diff(Pnum,ell),subst_wedge01,[u,v],point_wedge)
for label,expression in [
    ('extended s_H > s_P',s-Q(11,48)),
    ('extended b_H < b_P',Q(5,48)-b),
    ('extended profit A_P > A_H',AP-Afull),
    ('extended profit B_P > B_H',BP-Bfull),
    ('extended W_H > W_P',W-WP),
]:
    prove_positive(label,expression,subst_wedge01,[u,v],point_wedge)
assert Pnum.subs({d:Q(61,50),ell:Q(3,5)})<0
assert R.subs({d:Q(61,50),ell:Q(3,5)})==Q(1163267,11828160)
assert R.subs({d:Q(61,50),ell:Q(3,5)})<Q(1,10)
print('CERTIFIED algebraic equilibrium-branch threshold k_lambda >= 1/10')

# All off-path R&D choices: 0<=s,b<=1/2 imply 1/2<=d<=3/2.
subst_global={d:Q(1,2)+u,ell:v}
point_global={d:1,ell:Q(1,4)}
prove_positive('R_d < 0',-sp.diff(R,d),subst_global,[u,v],point_global)
prove_positive('R_ell < 0',-sp.diff(R,ell),subst_global,[u,v],point_global)
for label,expression in [
    ('0 < T_A prime',TA),('T_A prime < 2',2-TA),
    ('-2 < T_B prime',2+TB),('T_B prime < 0',-TB),
]:
    prove_positive(label,expression,subst_global,[u,v],point_global)
TA2 = sp.factor(sp.diff(TA,d)+sp.diff(TA,ell)*ell_d)
TB2 = sp.factor(sp.diff(TB,d)+sp.diff(TB,ell)*ell_d)
for label,expr in [
    ('T_A second < 2',2-TA2),
    ('T_B second < 2',2-TB2),
]:
    prove_positive(label,expr,subst_global,[u,v],point_global)

# Stage 1 public B: L=0 beats every L in (0,1] at each feasible d.
prove_positive('public B: V_B(d,0) > V_B(d,ell)',
  Va*0+Vb.subs(ell,0)-Vb,subst_global,[u,v],point_global)
# On-equilibrium p_A is between 0.8 and 1.6.
prove_positive('price A > 0.8',pa-Q(4,5),subst_global,[u,v],point_global)
prove_positive('price A < 1.6',Q(8,5)-pa,subst_global,[u,v],point_global)

# For hidden Stage 1 deviations, A's expected price z is fixed.
D_dev=sp.cancel((1-d+z+ell*(3-d)/9)/(4-ell**2/9))
q_dev=-d+ell*D_dev
pb_dev=2*D_dev-ell*(3+q_dev)/9
V_dev=sp.cancel(pb_dev*D_dev+(3+q_dev)**2/18)
prove_positive('hidden B: d^2 V_dev/dell^2 < 0.1',
 Q(1,10)-sp.diff(V_dev,ell,2),
 {d:Q(1,2)+u,z:Q(4,5)+Q(4,5)*v,ell:w},
 [u,v,w],{d:1,z:Q(6,5),ell:Q(1,2)})

# Nonasymptotic, exact sufficient threshold for globally unique equilibrium.
threshold=sp.factor(R.subs({d:Q(1,2),ell:1}))
assert threshold==Q(4343,32448)
assert sp.simplify(threshold-R.subs({d:Q(19,16),ell:Q(1,2)}))>0
print('EXACT THRESHOLD k_lambda >',threshold,'=',float(threshold))

# Numerical equilibrium is only for displaying magnitudes, not sign certification.
import numpy as np
Pfun=sp.lambdify((d,ell),P,'numpy')
Rfun=sp.lambdify((d,ell),R,'numpy')
sol=root(lambda x:[Pfun(*x),Rfun(*x)-0.3],[1.156,0.211],tol=1e-12)
assert np.max(np.abs(sol.fun))<1e-10
DD,LL=sol.x
res={'d':DD,'ell':LL}
for name,expr in [('s',s),('b',b),('profit_A',Afull),
                  ('profit_B',Bfull),('welfare',W)]:
    res[name]=float(sp.lambdify((d,ell),expr,'numpy')(DD,LL))
print('PUBLIC',{'s':str(Q(11,48)),'b':str(Q(5,48)),
                'profit_A':str(AP),'profit_B':str(BP),'welfare':str(WP)})
print('HIDDEN k=0.3',res)
# Degree of the exact algebraic equation for ell when k=3/10.
Gnum=sp.cancel(R-Q(3,10)).as_numer_denom()[0]
resultant=sp.resultant(Pnum,Gnum,d)
factors=sp.factor_list(resultant)[1]
print('RESULTANT FACTOR DEGREES',[(sp.degree(f,ell),e) for f,e in factors])
print('All exact-rational certificates succeeded.')