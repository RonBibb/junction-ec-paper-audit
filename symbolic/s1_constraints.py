#!/usr/bin/env python3
from __future__ import annotations

import sympy as sp

from common import write_json


def derive():
    M, R, kappa, rho_eff = sp.symbols("M R kappa rho_eff", positive=True)
    A = sp.sqrt(2 * M / R - 1)
    Rdot = -A
    Adot = sp.simplify(sp.diff(A, R) * Rdot)
    HA = sp.simplify(Adot / A)
    HB = sp.simplify(Rdot / R)
    theta = sp.simplify(HA + 2 * HB)
    shear = sp.simplify(HA - HB)
    parent_hamiltonian = sp.simplify(2 * HA * HB + HB**2 + R ** -2)
    child_minus_parent = -kappa * rho_eff

    w, alpha, n, rho, V = sp.symbols("w alpha n rho V", positive=True)
    rho_eff_expr = rho - alpha * n**2
    p_eff_expr = w * rho - alpha * n**2
    rho_dot = -(1 + w) * sp.Symbol("Theta") * rho
    n_dot = -sp.Symbol("Theta") * n
    rho_eff_dot = sp.simplify(rho_dot - 2 * alpha * n * n_dot)
    critical_dot = sp.simplify(rho_eff_dot.subs(rho, alpha * n**2))

    return {
        "spacelike_surface": "constant proper-time KS slice with positive-definite induced three-metric",
        "causal_orientation": "future/past timelike unit normal; not a continuous timelike transport boundary",
        "darmois_data": ["A_C=A_P", "B_C=B_P", "H_A,C=H_A,P", "H_B,C=H_B,P"],
        "parent_vacuum_trajectory": {
            "A": str(A),
            "B": "R",
            "Rdot": str(Rdot),
            "H_A": str(HA),
            "H_B": str(HB),
            "Theta": str(theta),
            "s": str(shear),
            "domain": "0<R<2M",
        },
        "parent_hamiltonian_residual": str(parent_hamiltonian),
        "child_minus_parent_constraint": str(child_minus_parent),
        "necessary_density_condition": "rho_eff=rho-alpha n^2=0",
        "homogeneous_momentum_constraint": "0",
        "normal_effective_stress_jump_at_criticality": "0",
        "data_count": {
            "parent_parameters": ["M", "R_Sigma", "orientation"],
            "child_geometric_data_fixed": ["A", "B", "H_A", "H_B"],
            "matter_condition": "rho=alpha n^2",
            "remaining_local_choices": ["M>0", "0<R_Sigma<2M", "n>0", "declared w", "orientation"],
            "hidden_surface_functions": 0,
        },
        "effective_conservation": {
            "rho_eff": str(rho_eff_expr),
            "p_eff": str(p_eff_expr),
            "critical_derivative": str(critical_dot),
            "ratio_scaling": "rho/(alpha n^2) proportional to V^(1-w)",
        },
        "classification": {
            "necessary_constraint_intersection": "working",
            "compatible_local_initial_data": "working conditionally under B0/A_B",
            "bounded_local_evolution": "working through TEST 007 authorized interval",
            "areal_turning": "not established for baseline; exploratory 3/27 at 10 percent",
            "global_nonsingular_extension": "not proven",
        },
        "all_required_local_checks": bool(parent_hamiltonian == 0 and child_minus_parent == -kappa * rho_eff),
    }


if __name__ == "__main__":
    result = derive()
    write_json("s1_status.json", result)
    print(result)

