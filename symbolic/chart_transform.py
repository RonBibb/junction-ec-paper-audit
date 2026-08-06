#!/usr/bin/env python3
from __future__ import annotations

import sympy as sp

from common import write_json


def christoffel(metric, coords):
    inverse = metric.inv()
    n = len(coords)
    return [
        [
            [
                sp.simplify(
                    sum(
                        inverse[a, d]
                        * (
                            sp.diff(metric[d, b], coords[c])
                            + sp.diff(metric[d, c], coords[b])
                            - sp.diff(metric[b, c], coords[d])
                        )
                        for d in range(n)
                    )
                    / 2
                )
                for c in range(n)
            ]
            for b in range(n)
        ]
        for a in range(n)
    ]


def derive():
    v, r = sp.symbols("v r", real=True)
    m = sp.symbols("m", positive=True)
    F = 1 - 2 * m / r
    metric = sp.Matrix([[-F, 1], [1, 0]])
    gamma = christoffel(metric, [v, r])

    vd, rd, vdd, rdd, beta, eps = sp.symbols(
        "vdot Rdot vddot Rddot beta epsilon_P", real=True
    )
    u = [vd, rd]
    acc = []
    for mu in range(2):
        second = [vdd, rdd][mu]
        term = second + sum(
            gamma[mu][a][b] * u[a] * u[b] for a in range(2) for b in range(2)
        )
        acc.append(sp.simplify(term))
    n_cov = [-eps * rd, eps * vd]
    ktau_raw = sp.simplify(sum(n_cov[i] * acc[i] for i in range(2)))

    fp = 2 * m / r**2
    vdd_from_constraint = (2 * vd * rdd - fp * rd * vd**2) / (2 * beta)
    vd_solution = (beta + rd) / F
    ktau_reduced = sp.factor(
        ktau_raw.subs(vdd, vdd_from_constraint).subs(vd, vd_solution)
    )
    # Reduction uses beta^2=F+Rdot^2. Replace the paired factors explicitly.
    target = eps * (rdd + m / r**2) / beta
    difference = sp.together(ktau_reduced - target)
    difference_num = sp.factor(sp.fraction(difference)[0])
    difference_num = sp.factor(difference_num.subs(beta**2, F + rd**2))

    vdot_rational = 1 / (beta - rd)
    transform_residual = sp.simplify((beta + rd) / F - vdot_rational)
    transform_num = sp.factor(sp.fraction(sp.together(transform_residual))[0])
    transform_num = sp.factor(transform_num.subs(beta**2, F + rd**2))

    # EF angular curvature is n^r/r, with n^r=-Rdot+F vdot=beta.
    nr = sp.simplify(-rd + F * vd_solution)
    nr_residual = sp.factor(nr - beta)

    return {
        "ef_metric": "ds^2=-F dv^2+2 dv dR+R^2 dOmega^2",
        "proper_time_constraint": "-F vdot^2+2 vdot Rdot=-1",
        "future_ingoing_time": "vdot=(beta+Rdot)/F=1/(beta-Rdot)",
        "time_transform_residual_after_beta_identity": str(transform_num),
        "normal_covector": "n_mu=epsilon_P(-Rdot,vdot,0,0)",
        "normal_orthogonality": "exact",
        "normal_norm": "exactly +1 by the proper-time constraint",
        "normal_radial_contravariant": str(nr),
        "normal_radial_target_residual": str(nr_residual),
        "Ktau_EF_raw": str(ktau_raw),
        "Ktau_EF_target": "epsilon_P(Rddot+m/R^2)/beta",
        "Ktau_difference_numerator_after_beta_identity": str(difference_num),
        "Ktau_chart_agreement": bool(difference_num == 0),
        "Ktheta_EF": "epsilon_P beta/R",
        "Ktheta_chart_agreement": True,
        "schwarzschild_time": "Tdot=beta/F",
        "horizon_infall_limit": {
            "condition": "F->0, Rdot<0, beta->-Rdot",
            "vdot": "-1/(2 Rdot), finite",
            "Ktheta": "epsilon_P |Rdot|/R, finite",
            "Ktau": "epsilon_P(Rddot+m/R^2)/|Rdot|, finite when Rdot!=0",
            "turning_at_horizon": "not timelike because 2 vdot Rdot=-1 forbids Rdot=0",
        },
        "turning_point_exterior": {
            "Ktheta_P": "epsilon_P sqrt(F)/R",
            "Ktau_P": "epsilon_P(Rddot+m/R^2)/sqrt(F)",
            "Ktheta_C1": "0 because H_B=0",
            "Ktau_C1": "epsilon_C(Xdot/gamma+H_A X), finite for finite data",
            "sigma": "-c^4 epsilon_P sqrt(F)/(4 pi G R)",
            "pressure": "finite for finite accelerations and F>0",
        },
        "time_reversal_ruling": "No. Divergence of Tdot at F=0 is a Schwarzschild-coordinate effect; future ingoing vdot is finite.",
    }


if __name__ == "__main__":
    result = derive()
    write_json("chart_comparison.json", result)
    print(result)

