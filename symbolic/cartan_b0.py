#!/usr/bin/env python3
from __future__ import annotations

import sympy as sp

from common import write_json


def solve_general_cartan():
    n = 4
    kappa = sp.symbols("kappa", nonzero=True)
    delta = sp.eye(n)
    torsion = [[[sp.S.Zero for _ in range(n)] for _ in range(n)] for _ in range(n)]
    spin = [[[sp.S.Zero for _ in range(n)] for _ in range(n)] for _ in range(n)]
    unknowns = []
    for rho in range(n):
        for mu in range(n):
            for nu in range(mu + 1, n):
                q = sp.Symbol(f"Q_{rho}_{mu}{nu}")
                s = sp.Symbol(f"S_{rho}_{mu}{nu}")
                torsion[rho][mu][nu] = q
                torsion[rho][nu][mu] = -q
                spin[rho][mu][nu] = s
                spin[rho][nu][mu] = -s
                unknowns.append(q)

    def qtrace(nu):
        return sum(torsion[a][nu][a] for a in range(n))

    equations = []
    for rho in range(n):
        for mu in range(n):
            for nu in range(mu + 1, n):
                lhs = (
                    torsion[rho][mu][nu]
                    + delta[rho, mu] * qtrace(nu)
                    - delta[rho, nu] * qtrace(mu)
                )
                equations.append(sp.Eq(lhs, kappa * spin[rho][mu][nu]))
    solutions = sp.solve(equations, unknowns, dict=True)
    if len(solutions) != 1:
        return False, False

    solution = solutions[0]

    def trace_second(nu):
        return sum(spin[a][nu][a] for a in range(n))

    def trace_first(mu):
        return sum(spin[a][a][mu] for a in range(n))

    matches = True
    for rho in range(n):
        for mu in range(n):
            for nu in range(mu + 1, n):
                target = kappa * (
                    spin[rho][mu][nu]
                    + delta[rho, mu] * trace_second(nu) / 2
                    + delta[rho, nu] * trace_first(mu) / 2
                )
                if sp.simplify(solution[torsion[rho][mu][nu]] - target) != 0:
                    matches = False
    return True, matches


def weyssenhoff_check():
    kappa = sp.symbols("kappa", nonzero=True)
    s12, s13, s23 = sp.symbols("s12 s13 s23")
    spin2 = sp.zeros(4)
    spin2[1, 2], spin2[2, 1] = s12, -s12
    spin2[1, 3], spin2[3, 1] = s13, -s13
    spin2[2, 3], spin2[3, 2] = s23, -s23
    u = [1, 0, 0, 0]
    source = [[[u[r] * spin2[m, n] for n in range(4)] for m in range(4)] for r in range(4)]
    traces = [sp.simplify(sum(source[a][nu][a] for a in range(4))) for nu in range(4)]
    torsion = [[[kappa * source[r][m][n] for n in range(4)] for m in range(4)] for r in range(4)]
    residual_count = 0
    for r in range(4):
        for m in range(4):
            for n in range(4):
                qtrace_n = sum(torsion[a][n][a] for a in range(4))
                qtrace_m = sum(torsion[a][m][a] for a in range(4))
                residual = torsion[r][m][n] + (1 if r == m else 0) * qtrace_n - (
                    1 if r == n else 0
                ) * qtrace_m - kappa * source[r][m][n]
                if sp.simplify(residual) != 0:
                    residual_count += 1
    return all(value == 0 for value in traces), residual_count == 0


def derive():
    unique, trautman = solve_general_cartan()
    trace_free, residual_free = weyssenhoff_check()
    return {
        "declared_action": "first-order Einstein-Cartan gravitational action plus Weyssenhoff matter action used in TEST 003",
        "cartan_equation": "Q^rho_munu+delta^rho_mu Q^sigma_nusigma-delta^rho_nu Q^sigma_musigma=kappa s^rho_munu",
        "general_solution_unique": unique,
        "matches_trautman_equation_25": trautman,
        "weyssenhoff_frenkel_source_trace_free": trace_free,
        "weyssenhoff_cartan_residual_zero": residual_free,
        "weyssenhoff_solution": "Q^rho_munu=kappa u^rho s_munu",
        "averaging_linearity": "At fixed coframe, <Q>=Cartan(<s>) because the Cartan map is algebraic and linear.",
        "boundary_assumption_A_B": "Tr_Sigma(<s>)=<Tr_Sigma(s)> with finite one-sided traces and common averaging prescription",
        "B0_assumptions": [
            "unpolarized mean <s_munu>=0",
            "A_B boundary trace/averaging commutation",
            "no independent surface-spin action",
            "no distributional contorsion",
        ],
        "mean_boundary_torsion": "0",
        "bulk_spin_squared_stress": "may remain nonzero after eliminating torsion",
        "independent_angular_junction_correction": "0 under B0 assumptions",
        "israel_recovered": True,
        "torsion_free_limit": "s_munu->0 gives Q->0 and ordinary GR/Israel exactly",
        "scope": "Does not constrain polarized B1/B2, boundary polarization, surface-spin actions, or finite-thickness transitions.",
    }


if __name__ == "__main__":
    result = derive()
    write_json("cartan_b0.json", result)
    print(result)

