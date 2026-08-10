#!/usr/bin/env python3
from __future__ import annotations

import itertools
import sympy as sp

from common import write_json
from energy_condition_criteria import CRITERION_VERSION, DECLARATIONS


def derive():
    dkt, dkh, G, c = sp.symbols("DeltaKtau DeltaKtheta G c", nonzero=True)
    pref = c**4 / (4 * sp.pi * G)
    sigma = -pref * dkh
    pressure = pref * (dkt + dkh) / 2
    jump = sp.diag(dkt, dkh, dkh)
    trace = dkt + 2 * dkh
    surface = sp.diag(-sigma, pressure, pressure)
    residual = sp.simplify(jump - sp.eye(3) * trace + (8 * sp.pi * G / c**4) * surface)
    kp_t, kp_h, kc_t, kc_h = sp.symbols("Kp_tau Kp_theta Kc_tau Kc_theta")
    original_jump = sp.Matrix([kp_t - kc_t, kp_h - kc_h])
    reversed_with_order_exchange = sp.Matrix([(-kc_t) - (-kp_t), (-kc_h) - (-kp_h)])
    reversal_verified = bool(
        sp.simplify(original_jump - reversed_with_order_exchange) == sp.zeros(2, 1)
    )

    R, Rd, Rdd, m, X, Xd, HA = sp.symbols(
        "R Rdot Rddot m X Xdot H_A", real=True
    )
    F = sp.symbols("F", positive=True)
    beta = sp.sqrt(F + Rd**2)
    gamma = sp.sqrt(1 + X**2)

    branches = []
    for eps_p, eps_c in itertools.product((1, -1), repeat=2):
        kp_h = eps_p * beta / R
        kc_h = eps_c * X * Rd / (gamma * R)
        delta_h = kp_h - kc_h
        sign_result = "negative" if eps_p == 1 else "positive"
        ordinary = eps_p == 1
        branches.append(
            {
                "epsilon_P": eps_p,
                "epsilon_C": eps_c,
                "angular_jump": str(delta_h),
                "sigma_sign_from_exterior_bound": sign_result,
                "ordinary_parent_exterior": ordinary,
                "WEC": "violated" if ordinary else "conditional; different global gluing",
                "DEC": "violated" if ordinary else "conditional; different global gluing",
                "NEC": "DeltaKtau>=DeltaKtheta",
                "SEC": "DeltaKtau>=DeltaKtheta and DeltaKtau+DeltaKtheta>=0",
            }
        )

    return {
        "common_normal": "n=deta points from retained KS region (eta<0) to retained Schwarzschild region (eta>0)",
        "one_sided_limits": "n_C and n_P are limits of one normal, not independently outward normals",
        "child_retained_side_map": {
            "chi<=chi_Sigma": 1,
            "chi>=chi_Sigma": -1,
        },
        "parent_retained_side_map": {
            "ordinary exterior containing spatial infinity": 1,
        },
        "jump_convention": "DeltaK=K_P-K_C",
        "surface_tensor": "Sigma^a_b=diag(-sigma,p_s,p_s)",
        "sigma": str(sigma),
        "pressure": str(pressure),
        "mixed_tensor_residual": [[str(residual[i, j]) for j in range(3)] for i in range(3)],
        "tensor_residual_zero": bool(residual == sp.zeros(3)),
        "energy_condition_identities": {
            "sigma_plus_p": "c^4/(8 pi G)(DeltaKtau-DeltaKtheta)",
            "sigma_plus_2p": "c^4/(4 pi G) DeltaKtau",
            **DECLARATIONS,
        },
        "energy_condition_criterion_version": CRITERION_VERSION,
        "orientation_branches": branches,
        "ordinary_exterior_ruling": "For epsilon_P=+1 the parent angular term dominates for either explicitly retained KS interval, so sigma<0 and WEC/DEC fail.",
        "convention_reversal": "Reverse the single common normal and exchange jump order; DeltaK and physical Sigma are unchanged.",
        "convention_reversal_verified": reversal_verified,
        "nonordinary_warning": "epsilon_P=-1 requires a different throat/back-to-back global gluing and is not admitted as the declared child-interior/parent-exterior branch.",
    }


if __name__ == "__main__":
    result = derive()
    write_json("junction_branch_table.json", result["orientation_branches"])
    write_json("energy_conditions.json", result)
    print(result)
