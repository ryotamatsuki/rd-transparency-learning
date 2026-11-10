#!/usr/bin/env python3
"""Stage 6: canonical-form absorption sanity check (2026-11-10).

Reconstructs primitive differentiated Bertrand payoffs, obtains the
public-minus-hidden derivative wedge as a generic strategic-commitment
chain rule, and checks a diagnostic without customer-experience feedback.

This proves only the encoded algebraic statements, NOT publication
priority or a theorem-level audit of any cited paper.
"""
import sympy as S

t, delta, d, lam, p_A, p_B = S.symbols(
    "t delta d lam p_A p_B", positive=True)
D = (t-d+p_A-p_B)/(2*t)
q = -d + lam*D
VA = p_A*(1-D) + delta*(3*t-q)**2/(18*t)
VB = p_B*D + delta*(3*t+q)**2/(18*t)
FOC = [S.diff(VA, p_A), S.diff(VB, p_B)]
equilibria = S.solve(FOC, [p_A, p_B], dict=True)
assert len(equilibria) == 1
eq = equilibria[0]
pA0 = S.factor(eq[p_A].subs(lam, 0))
pB0 = S.factor(eq[p_B].subs(lam, 0))
public_value = S.factor(VB.subs(eq, simultaneous=True))
public_marginal = S.factor(S.diff(public_value, lam).subs(lam, 0))
hidden_marginal = S.factor(S.diff(VB, lam).subs({
    lam: 0, p_A: pA0, p_B: pB0}))
incumbent_reaction = S.factor(S.diff(eq[p_A], lam).subs(lam, 0))
cross_price_effect = S.factor(S.diff(VB, p_A).subs({
    lam: 0, p_A: pA0, p_B: pB0}))
wedge = S.factor(public_marginal - hidden_marginal)
generic = S.factor(cross_price_effect*incumbent_reaction)

expected = -delta*(3*t-d)*(9*t+d)/(162*t**2)
assert S.simplify(wedge-expected)==0
assert S.simplify(generic-expected)==0
assert S.simplify(hidden_marginal-delta*(3*t-d)**2/(54*t**2))==0
assert S.simplify(public_marginal+2*delta*d*(3*t-d)/(81*t**2))==0

# Ablation: replace market-share-mediated learning by a direct period-2
# quality increment, q2=-d+lambda. Both first-period price FOCs now
# contain no lambda, and the public/hidden incentive wedge disappears.
q_control=-d+lam
VA_control=p_A*(1-D)+delta*(3*t-q_control)**2/(18*t)
VB_control=p_B*D+delta*(3*t+q_control)**2/(18*t)
control=S.solve([S.diff(VA_control,p_A),S.diff(VB_control,p_B)],
    [p_A,p_B],dict=True)
assert len(control)==1
assert S.diff(control[0][p_A],lam)==0
assert S.diff(control[0][p_B],lam)==0
vB_control=S.factor(VB_control.subs(control[0],simultaneous=True))
ctrl_public=S.diff(vB_control,lam)
ctrl_hidden=S.diff(VB_control,lam).subs(control[0], simultaneous=True)
assert S.simplify(ctrl_public-ctrl_hidden)==0

print("PUBLIC marginal:",public_marginal)
print("HIDDEN marginal:",hidden_marginal)
print("PUBLIC-minus-HIDDEN:",wedge)
print("generic (payoff-pA slope)*(A reaction):",generic)
print("No-feedback control: public-hidden wedge = 0")
print("PASS: structural chain-rule / feedback-ablation identities")
