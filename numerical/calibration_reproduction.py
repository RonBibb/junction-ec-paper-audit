#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parent
OUT = ROOT / "outputs"
SOURCE = PROJECT / "parent-child-s1-calibration" / "symbolic" / "generated" / "thermal_calibration.json"


def derive():
    gstar = sp.Rational(427, 4)
    gf = sp.Integer(90)
    w = sp.Rational(1, 3)
    x = sp.Integer(2)
    a = sp.pi**2 * gstar / 30
    b = 3 * sp.zeta(3) * gf / (4 * sp.pi**2)
    q = sp.simplify(4 * a / (sp.pi * b**2))
    rho_ratio = sp.simplify(a * q**2)
    x_coefficient = sp.simplify(8 * sp.pi * (1 - w) * rho_ratio)
    mass_ratio = sp.simplify(sp.sqrt(x / x_coefficient))
    return {
        "identities": [
            "natural units: hbar=c=k_B=1",
            "unreduced l_Pl=sqrt(G), T_Pl=1/sqrt(G), rho_Pl=G^-2",
            "kappa=8 pi G",
            "alpha=kappa/32=pi G/4",
            "rho=(pi^2/30)g_* T^4",
            "n_f=[3 zeta(3)/(4 pi^2)]g_f T^3",
            "critical rho=alpha n_f^2",
        ],
        "exact": {
            "Tc_over_TPlanck": str(sp.sqrt(q)),
            "rho_c_over_rhoPlanck": str(rho_ratio),
            "x_coefficient": str(x_coefficient),
            "M_over_lPlanck_for_x2": str(mass_ratio),
        },
        "numeric": {
            "Tc_over_TPlanck": float(sp.N(sp.sqrt(q))),
            "rho_c_over_rhoPlanck": float(sp.N(rho_ratio)),
            "x_coefficient": float(sp.N(x_coefficient)),
            "M_over_lPlanck": float(sp.N(mass_ratio)),
        },
        "physical_ruling": "P3: standard thermal SM-like sharp Weyssenhoff realization is outside the declared conservative controlled regime.",
        "scope": "Does not exclude nonthermal, different-spin, finite-thickness, large-species, or quantum-completed successors.",
    }


def main():
    result = derive()
    original = json.loads(SOURCE.read_text())
    result["source"] = str(SOURCE.relative_to(PROJECT))
    result["comparison"] = {
        key: abs(result["numeric"][key] - original["numeric"][key])
        for key in result["numeric"]
    }
    result["exact_reproduction"] = all(value < 1e-14 for value in result["comparison"].values())
    (OUT / "calibration_status.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["numeric"], indent=2))


if __name__ == "__main__":
    main()

