#!/usr/bin/env python3
"""Single executable definition of the isotropic 2+1 shell energy conditions."""
from __future__ import annotations

import sympy as sp

CRITERION_VERSION = "isotropic-shell-2plus1-v1"
DECLARATIONS = {
    "NEC": "sigma+p_s>=0",
    "WEC": "sigma>=0 and NEC",
    "DEC": "sigma>=|p_s|",
    "SEC_2plus1": "NEC and p_s>=0",
}


def evaluate(sigma: sp.Expr, pressure: sp.Expr, *, strict: bool = False) -> dict[str, bool]:
    """Evaluate all declared conditions without module-local restatements."""
    sigma = sp.simplify(sigma)
    pressure = sp.simplify(pressure)
    sigma_plus_pressure = sp.simplify(sigma + pressure)
    sigma_minus_abs_pressure = sp.simplify(sigma - sp.Abs(pressure))
    if strict:
        nec = bool(sigma_plus_pressure.is_positive)
        sigma_nonnegative = bool(sigma.is_positive)
        dec = bool(sigma_minus_abs_pressure.is_positive)
        pressure_nonnegative = bool(pressure.is_positive)
    else:
        nec = bool(sigma_plus_pressure.is_nonnegative)
        sigma_nonnegative = bool(sigma.is_nonnegative)
        dec = bool(sigma_minus_abs_pressure.is_nonnegative)
        pressure_nonnegative = bool(pressure.is_nonnegative)
    return {
        "NEC": nec,
        "WEC": sigma_nonnegative and nec,
        "DEC": sigma_nonnegative and dec,
        "SEC": nec and pressure_nonnegative,
    }
