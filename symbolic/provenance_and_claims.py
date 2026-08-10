#!/usr/bin/env python3
from __future__ import annotations

from common import PROJECT, OUT, read_json, sha256, write_json


SOURCES = [
    ("Arbiter/tests/TEST_001_PARENT_CHILD_PHASE0_EQUATION_CLOSURE.md", "equation manifest and gates", "historical specification"),
    ("Arbiter/reviews/REVIEW_TEST_001_V2_2026-07-25.md", "corrected shear and closure ruling", "accepted review"),
    ("Arbiter/tests/TEST_002_J0_KS_SCHWARZSCHILD_MATCHING.md", "C0/C1 junction specification", "historical specification"),
    ("Arbiter/reviews/REVIEW_TEST_002_V2_2026-07-25.md", "accepted angular theorem and missing closeout", "accepted scoped review"),
    ("Arbiter/tests/TEST_003_J1_EINSTEIN_CARTAN_BOUNDARY_CLOSURE.md", "B0/B1/B2 and S1 gates", "historical specification"),
    ("Arbiter/reviews/REVIEW_TEST_003_V2_2026-07-25.md", "B0 and S1 ruling", "accepted conditional review"),
    ("Arbiter/tests/TEST_004_S1_INITIAL_DATA_COMPATIBILITY.md", "S1 data test", "historical specification"),
    ("Arbiter/reviews/REVIEW_TEST_004_2026-07-25.md", "local S1 compatibility", "accepted conditional review"),
    ("Arbiter/tests/TEST_005_S1_SHORT_TIME_EVOLUTION.md", "local acceleration test", "historical specification"),
    ("Arbiter/reviews/REVIEW_TEST_005_2026-07-25.md", "volume-turning tendency", "accepted review"),
    ("Arbiter/tests/TEST_006_S1_SHORT_TIME_REGULARITY_ROBUSTNESS.md", "series and robustness test", "historical specification"),
    ("Arbiter/reviews/REVIEW_TEST_006_2026-07-25.md", "R4 analytic indeterminacy", "accepted review"),
    ("Arbiter/tests/TEST_007_BOUNDED_S1_EVENT_CONTINUATION.md", "event test", "historical specification"),
    ("Arbiter/reviews/REVIEW_TEST_007_2026-07-25.md", "N2 volume/areal result", "accepted review"),
    ("Arbiter/tests/TEST_008_S1_PHYSICAL_CALIBRATION_VALIDITY.md", "physical calibration test", "historical specification"),
    ("Arbiter/reviews/REVIEW_TEST_008_2026-07-25.md", "P3 thermal ruling", "accepted scoped review"),
    ("parent-child-s1-numerical/outputs/continuation.json", "complete TEST 007 numerical output", "read-only reproduced data"),
    ("parent-child-s1-calibration/symbolic/generated/thermal_calibration.json", "TEST 008 exact calibration", "read-only reproduced data"),
]


def manifest():
    entries = []
    missing = []
    for relative, locator, status in SOURCES:
        path = PROJECT / relative
        if not path.is_file():
            missing.append(relative)
            continue
        entries.append(
            {
                "path": relative,
                "locator": locator,
                "epistemic_status": status,
                "sha256": sha256(path),
            }
        )
    equations = {
        "P1": "dot(s)+Theta s=1/B^2",
        "P2_parent": "Ktau_P=epsilon_P(Rddot+m/R^2)/beta; Ktheta_P=epsilon_P beta/R",
        "P2_child_C1": "Ktau_C=epsilon_C(Xdot/gamma+H_A X); Ktheta_C=epsilon_C X H_B",
        "P2_israel": "sigma=-c^4 DeltaKtheta/(4 pi G); p_s=c^4(DeltaKtau+DeltaKtheta)/(8 pi G)",
        "P2_interior": "For F=-f<0 and aligned angular curvatures, sigma>0 iff f<Rdot^2<(1+X^2)f",
        "P2_conservation": "D_a Sigma^a_tau+[T_mn n^m e^n_tau]^P_C=0",
        "P3": "<s>=0 plus A_B implies <Q>=0 and no independent B0 torsion junction term",
        "P4": "rho_eff=0 is necessary for impulse-free S1 matching to vacuum",
        "P5": "Theta turning and H_B turning are distinct",
        "P6": "Tc/TPl=0.8133906806; rho_c/rho_Pl=15.3724519; x=2 maps M/l_Pl=0.0881189",
    }
    return {
        "test": "TEST_022",
        "active_convention": "config/conventions.yaml",
        "sources": entries,
        "missing_sources": missing,
        "source_count": len(entries),
        "equations": equations,
        "retractions": [
            "s proportional to V^-1 as a complete solution",
            "TEST 002 V1 J0-C moving shell viability",
            "TEST 006 cubic root as an exact event prediction",
        ],
    }


def claims():
    return [
        {
            "id": "R1",
            "type": "theorem/abstract",
            "claim": "Kantowski-Sachs curvature sources shear: dot(s)+Theta s=1/B^2 for isotropic effective pressure.",
            "artifact": "symbolic/shear_identity.py; outputs/shear_identity.json",
            "assumptions_domain": "homogeneous KS, proper time, isotropic effective pressure",
            "epistemic_status": "working derived result",
            "independent_control": "Einstein-equation subtraction and integrated derivative",
            "strongest_limitation": "anisotropic stress adds kappa(p_A-p_B)",
            "permitted_wording": "curvature-sourced shear law",
            "prohibited_wording": "shear necessarily diverges or necessarily isotropizes",
        },
        {
            "id": "R2",
            "type": "theorem/abstract",
            "claim": "The declared ordinary exterior C0/C1 timelike gluing requires negative surface density.",
            "artifact": "symbolic/c1_extrinsic.py; symbolic/israel_residual.py; symbolic/surface_conservation.py; symbolic/chart_transform.py",
            "assumptions_domain": "Schwarzschild F>0, homogeneous KS, declared C0/C1 embeddings and ordinary orientation",
            "epistemic_status": "working scoped result if JEC2-JEC3 pass",
            "independent_control": "coordinate/frame derivations and Schwarzschild/EF chart comparison",
            "strongest_limitation": "not an F<0, spacelike, smooth, or arbitrary-embedding theorem",
            "permitted_wording": "scoped exterior timelike obstruction with full surface ledger",
            "prohibited_wording": "all moving shells or all parent-child junctions fail",
        },
        {
            "id": "R3",
            "type": "theorem/abstract",
            "claim": "For F<0 the KS/Schwarzschild surface-density sign is indefinite; a same-bulk paired witness realizes both signs and compatible acceleration data satisfy NEC, WEC, DEC, and shell SEC.",
            "artifact": "symbolic/interior_sector.py; outputs/interior_sector.json; tests/test_interior_sector.py",
            "assumptions_domain": "local future-infalling timelike segment, Schwarzschild F<0, retained increasing-R parent side, fixed KS retained interval",
            "epistemic_status": "exact local sign classification if JEC3 passes",
            "independent_control": "invariant inequality and mass ordering, retained-region reflection check, exact paired witness, matching compatibility, energy conditions, and ingoing-EF normalization",
            "strongest_limitation": "not a shell equation of motion, stability result, global completion, or spacelike-transition result",
            "permitted_wording": "interior timelike sign indeterminacy with an explicit fully energy-condition-satisfying local surface witness",
            "prohibited_wording": "positive-energy child universe or validation of interior transition models",
        },
        {
            "id": "R4",
            "type": "theorem/abstract",
            "claim": "Unpolarized algebraic torsion supplies no independent B0 angular repair under the declared boundary assumptions.",
            "artifact": "symbolic/cartan_b0.py; outputs/cartan_b0.json",
            "assumptions_domain": "Weyssenhoff/Frenkel, zero mean boundary spin, A_B, no surface-spin action or distributional contorsion",
            "epistemic_status": "working conditional result",
            "independent_control": "general Cartan solve and exact torsion-free limit",
            "strongest_limitation": "polarized B1/B2 and finite-thickness models remain open",
            "permitted_wording": "limited unpolarized B0 non-repair",
            "prohibited_wording": "Einstein-Cartan torsion cannot repair any junction",
        },
        {
            "id": "R5",
            "type": "conclusion",
            "claim": "A nonempty S1 family satisfies the necessary local impulse-free data and admits bounded local evolution.",
            "artifact": "symbolic/s1_constraints.py; outputs/s1_status.json",
            "assumptions_domain": "interior Schwarzschild KS control and B0/A_B boundary assumptions",
            "epistemic_status": "conditional local result",
            "independent_control": "Hamiltonian, momentum, data count, and original TEST 004–007 checks",
            "strongest_limitation": "not a sufficient global junction or transport law",
            "permitted_wording": "conditional local spacelike route",
            "prohibited_wording": "global child spacetime or mass transfer",
        },
        {
            "id": "R6",
            "type": "figure/conclusion",
            "claim": "The N2 baseline expands in total volume while its areal radius remains contracting through t=M.",
            "artifact": "numerical/event_reproduction.py; outputs/event_status.json",
            "assumptions_domain": "TEST 007 homogeneous ODE, x=2, w=1/3, t<=M",
            "epistemic_status": "working bounded numerical result",
            "independent_control": "tight repeat and 54 constraint-preserving perturbations",
            "strongest_limitation": "3/27 coarse cases turn; no open areal-bounce region established",
            "permitted_wording": "volume/areal distinction and N2 counterexample",
            "prohibited_wording": "bounce, nonsingularity, or long-time behavior",
        },
        {
            "id": "R7",
            "type": "conclusion",
            "claim": "The standard thermal SM-like sharp Weyssenhoff calibration fails the conservative TEST 008 control regime.",
            "artifact": "numerical/calibration_reproduction.py; outputs/calibration_status.json",
            "assumptions_domain": "zero chemical potential thermal reference, g*=106.75, gf=90, conservative EFT threshold",
            "epistemic_status": "disproven under stated assumptions",
            "independent_control": "exact unit-chain reproduction",
            "strongest_limitation": "does not cover nonthermal or successor matter",
            "permitted_wording": "scoped physical calibration exclusion",
            "prohibited_wording": "all spin matter or all Einstein-Cartan cosmology fails",
        },
        {
            "id": "ABSTRACT",
            "type": "abstract",
            "claim": "Seven scoped control results form a coherent junction-and-controls record if JEC0-JEC9 pass.",
            "artifact": "all TEST 022 outputs and results/ARBITER_PACKET.md",
            "assumptions_domain": "union of explicitly printed R1-R7 domains",
            "epistemic_status": "paper eligibility only; not empirical validation",
            "independent_control": "claim matrix and gate runner",
            "strongest_limitation": "no child-universe transition, bounce, transfer, time reversal, or empirical result",
            "permitted_wording": "technical controls and scoped obstructions",
            "prohibited_wording": "proof of the framework",
        },
    ]


def main():
    equation_manifest = manifest()
    claim_matrix = claims()
    write_json("equation_manifest.json", equation_manifest)
    write_json("claim_matrix.json", claim_matrix)
    print({"sources": equation_manifest["source_count"], "missing": equation_manifest["missing_sources"], "claims": len(claim_matrix)})


if __name__ == "__main__":
    main()
