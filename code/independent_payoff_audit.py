"""Partial independent numerical audit of hidden benchmark best responses.

Reconstructs payoffs directly, rather than differentiating the production
symbolic payoff expressions. This is a NUMERICAL deviation test, not a proof
of global uniqueness or a complete Stage-4A certification.
"""
from scipy.optimize import brentq, minimize_scalar
import numpy as np

K_LEARNING = 0.3
S_EQ = 0.2524920153987139
B_EQ = 0.09674587868653284
DOMAIN = (0.0, 0.5)

def share(d, lam):
    return (27.0 - (9.0 + 2.0 * lam) * d) / (2.0 * (27.0 - lam ** 2))

def price_pair(d, lam):
    D = share(d, lam)
    q = -d + lam * D
    p_A = 2.0 * (1.0 - D) - lam * (3.0 - q) / 9.0
    p_B = 2.0 * D - lam * (3.0 + q) / 9.0
    return p_A, p_B

def learning_foc(d, lam):
    D = share(d, lam)
    q = -d + lam * D
    return D * (3.0 + q) / (9.0 * lam) - K_LEARNING

def hidden_learning(d):
    return brentq(lambda lam: learning_foc(d, lam),
                  1.0e-9, 1.0 - 1.0e-9, xtol=1e-13)

def net_profits(s, b):
    d = 1.0 + s - b
    lam = hidden_learning(d)
    D = share(d, lam)
    q = -d + lam * D
    p_A, p_B = price_pair(d, lam)
    profit_A = p_A * (1.0 - D) + (3.0 - q)**2 / 18.0 - 2.0 * s**2
    profit_B = p_B * D + (3.0 + q)**2 / 18.0 - 2.0 * b**2 - K_LEARNING * lam**2 / 2.0
    return profit_A, profit_B

def b_deviation_value(lam, gap, incumbent_price):
    # Incumbent's period-1 price cannot react to an unobserved deviation.
    # Entrant optimizes its own period-1 price against that fixed price.
    D = (1.0 - gap + incumbent_price + lam*(3.0-gap)/9.0)/(4.0-lam**2/9.0)
    p_B = 1.0-gap+incumbent_price-2.0*D
    q = -gap+lam*D
    return p_B*D + (3.0+q)**2/18.0 - K_LEARNING*lam**2/2.0

def main():
    d_eq = 1.0 + S_EQ - B_EQ
    lam_eq = hidden_learning(d_eq)
    profit_A, profit_B = net_profits(S_EQ, B_EQ)
    best_A = minimize_scalar(lambda s: -net_profits(s,B_EQ)[0],
                             bounds=DOMAIN,method='bounded',
                             options={'xatol':1e-13})
    best_B = minimize_scalar(lambda b: -net_profits(S_EQ,b)[1],
                             bounds=DOMAIN,method='bounded',
                             options={'xatol':1e-13})
    p_A, _ = price_pair(d_eq, lam_eq)
    best_L = minimize_scalar(lambda lam: -b_deviation_value(lam,d_eq,p_A),
                             bounds=(0.0,1.0),method='bounded',
                             options={'xatol':1e-13})
    gain_A = -best_A.fun-profit_A
    gain_B = -best_B.fun-profit_B
    gain_L = -best_L.fun-b_deviation_value(lam_eq,d_eq,p_A)
    print(f"Hidden benchmark: s={S_EQ:.12f}, b={B_EQ:.12f}, lambda={lam_eq:.12f}")
    print(f"Direct net profit A={profit_A:.12f}; B={profit_B:.12f}")
    print(f"Stage0 A best response: s={best_A.x:.12f}; gain={gain_A:.3g}")
    print(f"Stage0 B best response: b={best_B.x:.12f}; gain={gain_B:.3g}")
    print(f"Stage1 B best hidden deviation: lambda={best_L.x:.12f}; gain={gain_L:.3g}")
    assert abs(best_A.x-S_EQ) < 1e-6 and gain_A < 1e-8
    assert abs(best_B.x-B_EQ) < 1e-6 and gain_B < 1e-8
    assert abs(best_L.x-lam_eq) < 1e-6 and gain_L < 1e-8
    ds = np.linspace(0.5,1.5,101)
    ls = [hidden_learning(d) for d in ds]
    assert all(0.0 < l < 1.0 for l in ls)
    assert min(price_pair(d,l)[0] for d,l in zip(ds,ls)) > 0.0
    assert min(price_pair(d,l)[1] for d,l in zip(ds,ls)) > 0.0
    print("101-point off-path quality-gap sweep: finite interior learning and positive prices")
    print("PASS — partial numerical candidate-deviation check (not a global proof)")

if __name__ == "__main__":
    main()
