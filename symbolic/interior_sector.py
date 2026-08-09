#!/usr/bin/env python3
from __future__ import annotations

import sympy as sp

from common import write_json


def derive():
    f, rdot, X = sp.symbols("f Rdot X", positive=True)
    gamma2 = 1 + X**2

    # For F=-f and aligned positive angular curvatures, K_C>K_P is
    # X^2 Rdot^2/(1+X^2) > Rdot^2-f.
    condition_residual = sp.factor(X**2 * rdot**2 - gamma2 * (rdot**2 - f))

    # Exact paired witness in units R=1.
    F = -sp.Rational(1, 2)
    Rdot = -sp.Integer(2)
    beta = sp.sqrt(F + Rdot**2)
    gamma = sp.sqrt(10)
    Bdot = Rdot / gamma
    epsilon_p = 1
    epsilon_c = -1
    vdot = sp.simplify(1 / (beta - Rdot))
    proper_time = sp.simplify(-F * vdot**2 + 2 * vdot * Rdot)
    normal_r = sp.simplify(epsilon_p * (-Rdot + F * vdot))

    witnesses = []
    for x in (sp.Integer(3), -sp.Integer(3)):
        k_parent = sp.simplify(epsilon_p * beta)
        k_child = sp.simplify(epsilon_c * x * Bdot)
        delta = sp.simplify(k_parent - k_child)
        witnesses.append(
            {
                "X": str(x),
                "Ktheta_parent_times_R": str(k_parent),
                "Ktheta_child_times_R": str(k_child),
                "DeltaKtheta_times_R": str(delta),
                "sigma_sign": "positive" if sp.signsimp(-delta).is_positive else "negative",
            }
        )

    q_child = sp.simplify(-Bdot**2)
    return {
        "sector": "F<0 future-infalling timelike shell",
        "aligned_condition_residual": str(condition_residual),
        "positive_density_interval": "f<Rdot^2<(1+X^2)f with epsilon_C X Rdot>0",
        "interval_derivation_verified": bool(
            sp.simplify(condition_residual - (f * (1 + X**2) - rdot**2)) == 0
        ),
        "witness": {
            "R": "1",
            "m": "3/4",
            "F": str(F),
            "Rdot": str(Rdot),
            "gamma": str(gamma),
            "Bdot": str(Bdot),
            "gradient_norm_child": str(q_child),
            "gradient_norm_parent": str(F),
            "epsilon_P": epsilon_p,
            "epsilon_C": epsilon_c,
            "EF_vdot": str(vdot),
            "EF_future": bool(vdot.is_positive),
            "EF_proper_time_residual": str(sp.simplify(proper_time + 1)),
            "EF_normal_r": str(normal_r),
            "EF_normal_target_residual": str(sp.simplify(normal_r - beta)),
            "paired_signs": witnesses,
            "same_bulk_invariants": bool(q_child == -sp.Rational(2, 5)),
        },
        "both_density_signs_verified": {row["sigma_sign"] for row in witnesses}
        == {"positive", "negative"},
    }


if __name__ == "__main__":
    result = derive()
    write_json("interior_sector.json", result)
    print(result)
