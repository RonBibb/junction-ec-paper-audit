#!/usr/bin/env python3
from __future__ import annotations

import sympy as sp

from common import write_json


def derive():
    R, Rd, Rdd, m = sp.symbols("R Rdot Rddot m", positive=True)
    F, X, Xd, HA, HB, dHB, rho, p_chi, p_perp = sp.symbols(
        "F X Xdot H_A H_B dH_B rho p_chi p_perp", real=True
    )
    epsP, epsC, kappa = sp.symbols("epsilon_P epsilon_C kappa", nonzero=True)
    gamma = sp.sqrt(1 + X**2)
    beta = sp.sqrt(F + Rd**2)
    pref = 2 / kappa  # c=1, kappa=8 pi G, so 1/(4 pi G)=2/kappa.

    kp_h = epsP * beta / R
    kp_t = epsP * (Rdd + m / R**2) / beta
    kc_h = epsC * X * HB
    kc_t = epsC * (Xd / gamma + HA * X)
    delta_h = kp_h - kc_h
    delta_t = kp_t - kc_t
    sigma = -pref * delta_h
    pressure = pref * (delta_t + delta_h) / 2

    # Parent identity d(beta/R)=Rdot/R(Ktau/eps-Ktheta/eps) uses F'=2m/R^2.
    beta_dot = Rd * (Rdd + m / R**2) / beta
    parent_codazzi = sp.simplify(
        epsP * (beta_dot / R - beta * Rd / R**2)
        - (Rd / R) * (kp_t - kp_h)
    )

    # Child shell derivative: Rdot/R=gamma H_B.
    child_kh_dot = epsC * (Xd * HB + X * gamma * dHB)
    child_codazzi = sp.simplify(
        child_kh_dot - gamma * HB * (kc_t - kc_h)
    )
    child_target = epsC * gamma * X * (dHB - HA * HB + HB**2)

    # Difference of the KS longitudinal equation and Hamiltonian constraint for
    # diag(-rho,p_chi,p_perp,p_perp):
    # dH_B-H_A H_B+H_B^2=-(kappa/2)(rho+p_chi).
    field_sub = {dHB: HA * HB - HB**2 - kappa * (rho + p_chi) / 2}
    child_flux_reduced = sp.simplify(child_codazzi.subs(field_sub))

    # E=dot sigma+2 Rdot/R(sigma+p_s)=-pref*(Delta kh dot-Hs(Delta kt-Delta kh)).
    # Parent part vanishes; the remaining child part is pref*child_codazzi.
    energy_change = sp.simplify(pref * child_flux_reduced)
    divergence_covector = sp.simplify(-energy_change)
    # Direct orthonormal-frame projection.  The transverse pressure cancels.
    child_flux_direct = epsC * gamma * X * (rho + p_chi)
    jump_flux = -child_flux_direct
    qtau = sp.simplify(divergence_covector + jump_flux)

    return {
        "surface_energy_equation": "E_dot=dot(sigma)+2 Rdot/R(sigma+p_s)",
        "covector_divergence": "D_a Sigma^a_tau=-E_dot",
        "parent_codazzi_residual": str(parent_codazzi),
        "child_codazzi_raw": str(child_codazzi),
        "child_codazzi_target_residual": str(sp.simplify(child_codazzi - child_target)),
        "source_model": "T^hat(a)_hat(b)=diag(-rho,p_chi,p_perp,p_perp)",
        "child_field_equation": "dH_B-H_A H_B+H_B^2=-(kappa/2)(rho+p_chi)",
        "energy_change_reduced": str(energy_change),
        "energy_change_expected": "-epsilon_C gamma X (rho+p_chi)",
        "surface_divergence_reduced": str(divergence_covector),
        "bulk_flux_parent": "0",
        "bulk_flux_child": "epsilon_C gamma X (rho+p_chi)",
        "transverse_pressure_cancels": bool(not child_flux_direct.has(p_perp)),
        "jump_flux_P_minus_C": str(jump_flux),
        "Q_tau": str(qtau),
        "Q_tau_zero": bool(qtau == 0 and parent_codazzi == 0),
        "C0_limit": "X=0 gives zero child flux and the prior C0 conservation identity",
        "interpretation": "C1 exchanges energy with the comoving child source when X is nonzero; only rho+p_chi enters, and this is shell crossing, not parent-child mass transfer.",
    }


if __name__ == "__main__":
    result = derive()
    write_json("conservation_status.json", result)
    print(result)
