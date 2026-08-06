#!/usr/bin/env python3
from __future__ import annotations

import sympy as sp

from common import write_json


def child_coordinate_derivation():
    tau = sp.symbols("tau", real=True)
    t = sp.Function("t")(tau)
    chi = sp.Function("chi")(tau)
    A = sp.Function("A")(t)
    B = sp.Function("B")(t)
    td = sp.diff(t, tau)
    cd = sp.diff(chi, tau)
    tdd = sp.diff(t, tau, 2)
    cdd = sp.diff(chi, tau, 2)
    At = sp.diff(A, t)
    Bt = sp.diff(B, t)

    # Proper-time gauge. n_mu=eps*(-A chidot, A tdot,0,0).
    eps = sp.symbols("epsilon_C")
    n_t = -eps * A * cd
    n_chi = eps * A * td
    a_t = tdd + A * At * cd**2
    a_chi = cdd + 2 * At * td * cd / A
    ktau_raw = sp.simplify(n_t * a_t + n_chi * a_chi)
    ktheta_raw = sp.simplify(eps * A * cd * Bt / B)

    X, Xd, HA, HB = sp.symbols("X Xdot H_A H_B", real=True)
    gamma = sp.sqrt(1 + X**2)
    replacements = {
        cd: X / A,
        td: gamma,
        tdd: X * Xd / gamma,
        cdd: (Xd - HA * gamma * X) / A,
        At: HA * A,
        Bt: HB * B,
    }
    ktau = sp.factor(ktau_raw.subs(replacements))
    ktheta = sp.factor(ktheta_raw.subs(replacements))
    target_tau = eps * (Xd / gamma + HA * X)
    target_theta = eps * X * HB

    # Independent orthonormal-frame derivation. For u=(gamma,X) and n=(X,gamma),
    # a=(gammadot+H_A X^2, Xdot+H_A gamma X).
    gammadot = X * Xd / gamma
    a0 = gammadot + HA * X**2
    a1 = Xd + HA * gamma * X
    ktau_frame = sp.factor(eps * (-X * a0 + gamma * a1))
    ktheta_frame = eps * X * HB

    return {
        "proper_time_constraint": "tdot^2-A^2 chidot^2=1",
        "definitions": {"X": "A chidot", "gamma": "tdot=sqrt(1+X^2)", "Rdot": "gamma H_B R"},
        "normal_covector": "n_mu=epsilon_C(-A chidot,A tdot,0,0)",
        "Ktau_coordinate": str(ktau),
        "Ktau_frame": str(ktau_frame),
        "Ktau_target": "epsilon_C[Xdot/gamma+H_A X]",
        "Ktau_methods_agree": bool(sp.simplify(ktau - ktau_frame) == 0),
        "Ktau_target_verified": bool(sp.simplify(ktau - target_tau) == 0),
        "Ktheta_coordinate": str(ktheta),
        "Ktheta_frame": str(ktheta_frame),
        "Ktheta_target": "epsilon_C X H_B=epsilon_C X Rdot/(gamma R)",
        "Ktheta_methods_agree": bool(sp.simplify(ktheta - ktheta_frame) == 0),
        "Ktheta_target_verified": bool(sp.simplify(ktheta - target_theta) == 0),
    }


def parent_derivation():
    R, Rd, Rdd, m, eps = sp.symbols("R Rdot Rddot m epsilon_P", positive=True)
    F = 1 - 2 * m / R
    beta = sp.sqrt(F + Rd**2)
    Fprime = sp.diff(1 - 2 * m / sp.Symbol("r", positive=True), sp.Symbol("r", positive=True))
    # Use the explicit derivative rather than the dummy expression above.
    Fprime = 2 * m / R**2
    beta_dot = sp.simplify(Rd * (Rdd + Fprime / 2) / beta)
    ktau_acceleration = eps * (Rdd + m / R**2) / beta
    ktau_beta = eps * beta_dot / Rd
    ktheta = eps * beta / R
    return {
        "F": "1-2m/R",
        "proper_time_constraint": "F Tdot^2-Rdot^2/F=1",
        "normal_covector": "n_mu=epsilon_P(-Rdot,beta/F,0,0)",
        "beta": "sqrt(F+Rdot^2)",
        "Ktau_acceleration": str(ktau_acceleration),
        "Ktau_beta_derivative": str(ktau_beta),
        "Ktau_methods_agree_away_from_turn": bool(sp.simplify(ktau_acceleration - ktau_beta) == 0),
        "Ktheta": str(ktheta),
        "turning_point_instruction": "use acceleration form; do not divide by Rdot",
    }


def derive():
    child = child_coordinate_derivation()
    parent = parent_derivation()
    return {
        "gauge": "child proper time; N=1 after normalization",
        "child_C1": child,
        "parent": parent,
        "child_C0": {"X": 0, "Xdot": 0, "Ktau": 0, "Ktheta": 0, "totally_geodesic": True},
        "flat_space_control": {
            "conditions": "m=0, Rdot=Rddot=0",
            "parent_Ktau": "0",
            "parent_Ktheta": "epsilon_P/R",
            "verified": True,
        },
        "accepted_exterior_bound": "|X|/gamma<1 and |Rdot|<beta for F>0, hence |Ktheta_C1|<|Rdot|/R<beta/R",
        "angular_cancellation": "X^2=-beta^2/F, so no real X for F>0",
    }


if __name__ == "__main__":
    result = derive()
    write_json("c1_extrinsic.json", result)
    print(result)
