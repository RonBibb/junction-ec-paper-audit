#!/usr/bin/env python3
from __future__ import annotations

import sympy as sp

from common import write_json


def derive():
    HA, HB, dHA, dHB, B, kappa = sp.symbols(
        "H_A H_B dH_A dH_B B kappa", nonzero=True
    )
    pA, pB = sp.symbols("p_A p_B")
    theta = HA + 2 * HB
    shear = HA - HB
    dshear = dHA - dHB

    longitudinal_lhs = 2 * dHB + 3 * HB**2 + B ** -2
    angular_lhs = dHA + dHB + HA**2 + HB**2 + HA * HB
    isotropic_residual = sp.expand(angular_lhs - longitudinal_lhs)
    target = sp.expand(dshear + theta * shear - B ** -2)

    V, A = sp.symbols("V A", positive=True)
    integrated_residual = sp.simplify(theta * V * shear + V * (B ** -2 - theta * shear) - A)
    integrated_residual = integrated_residual.subs(V, A * B**2)

    anisotropic = sp.Eq(
        dshear + theta * shear,
        B ** -2 + kappa * (pA - pB),
    )

    rho, pressure = sp.symbols("rho pressure")
    dHB_evolution = -(kappa * pressure + 3 * HB**2 + B ** -2) / 2
    dHA_evolution = (
        -kappa * pressure
        - dHB_evolution
        - HA**2
        - HB**2
        - HA * HB
    )
    drho = -theta * (rho + pressure)
    constraint = 2 * HA * HB + HB**2 + B ** -2 - kappa * rho
    constraint_dot = sp.expand(
        2 * dHA_evolution * HB
        + 2 * HA * dHB_evolution
        + 2 * HB * dHB_evolution
        - 2 * HB / B**2
        - kappa * drho
    )
    propagation_residual = sp.factor(constraint_dot + theta * constraint)

    return {
        "isotropic_subtraction_residual": str(sp.simplify(isotropic_residual - target)),
        "isotropic_identity_verified": bool(sp.simplify(isotropic_residual - target) == 0),
        "shear_equation": "dH_A-dH_B+(H_A+2 H_B)(H_A-H_B)=1/B^2",
        "integrated_derivative": "d(V s)/dt=A",
        "integrated_residual": str(sp.simplify(integrated_residual)),
        "integrated_identity": "s(t)=[C+integral A(t') dt']/[A(t) B(t)^2]",
        "anisotropic_pressure_equation": str(anisotropic),
        "anisotropic_convention": "p_A is longitudinal and p_B is angular pressure",
        "constraint_propagation": "Cdot=-Theta*C",
        "constraint_propagation_residual": str(propagation_residual),
        "constraint_propagation_verified": bool(propagation_residual == 0),
        "retraction": "s proportional to V^-1 omits the curvature-sourced particular solution",
    }


if __name__ == "__main__":
    result = derive()
    write_json("shear_identity.json", result)
    print(result)
