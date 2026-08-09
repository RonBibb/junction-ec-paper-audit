#!/usr/bin/env python3
from __future__ import annotations

from common import OUT, read_json, write_json


def gate(name, passed, result):
    return {"gate": name, "status": "pass" if passed else "fail", "result": result}


def main():
    manifest = read_json(OUT / "equation_manifest.json")
    shear = read_json(OUT / "shear_identity.json")
    c1 = read_json(OUT / "c1_extrinsic.json")
    israel = read_json(OUT / "energy_conditions.json")
    conservation = read_json(OUT / "conservation_status.json")
    chart = read_json(OUT / "chart_comparison.json")
    interior = read_json(OUT / "interior_sector.json")
    cartan = read_json(OUT / "cartan_b0.json")
    s1 = read_json(OUT / "s1_status.json")
    events = read_json(OUT / "event_status.json")
    calibration = read_json(OUT / "calibration_status.json")
    claims = read_json(OUT / "claim_matrix.json")

    jec0 = not manifest["missing_sources"] and manifest["source_count"] == 18
    jec1 = (
        shear["isotropic_identity_verified"]
        and shear["integrated_residual"] == "0"
        and shear["constraint_propagation_verified"]
    )
    jec2 = (
        c1["child_C1"]["Ktau_methods_agree"]
        and c1["child_C1"]["Ktheta_methods_agree"]
        and c1["child_C1"]["Ktau_target_verified"]
        and c1["child_C1"]["Ktheta_target_verified"]
        and c1["parent"]["Ktau_methods_agree_away_from_turn"]
        and c1["flat_space_control"]["verified"]
        and israel["tensor_residual_zero"]
    )
    ordinary = [row for row in israel["orientation_branches"] if row["ordinary_parent_exterior"]]
    jec3 = (
        conservation["Q_tau_zero"]
        and chart["Ktau_chart_agreement"]
        and chart["Ktheta_chart_agreement"]
        and interior["interval_derivation_verified"]
        and interior["both_density_signs_verified"]
        and interior["witness"]["EF_future"]
        and interior["witness"]["EF_proper_time_residual"] == "0"
        and interior["witness"]["EF_normal_target_residual"] == "0"
        and len(ordinary) == 2
        and israel["convention_reversal_verified"]
        and all(row["WEC"] == "violated" and row["DEC"] == "violated" for row in ordinary)
    )
    jec4 = (
        cartan["general_solution_unique"]
        and cartan["matches_trautman_equation_25"]
        and cartan["weyssenhoff_cartan_residual_zero"]
        and cartan["israel_recovered"]
    )
    jec5 = s1["all_required_local_checks"] and s1["data_count"]["hidden_surface_functions"] == 0
    comparison = events["comparison"]
    jec6 = (
        events["classification"] == "N2"
        and comparison["event_equal"]
        and comparison["event_time_abs"] <= 1e-8
        and comparison["endpoint_B_abs"] <= 1e-8
        and comparison["endpoint_Theta_abs"] <= 1e-8
        and all(comparison["grid_counts_equal"])
        and events["baseline"]["max_constraint"] <= 1e-8
        and events["tight_baseline"]["max_constraint"] <= 1e-8
    )
    jec7 = calibration["exact_reproduction"]
    required_claim_fields = {
        "id",
        "type",
        "claim",
        "artifact",
        "assumptions_domain",
        "epistemic_status",
        "independent_control",
        "strongest_limitation",
        "permitted_wording",
        "prohibited_wording",
    }
    jec8 = len(claims) == 8 and all(required_claim_fields <= set(row) for row in claims)

    gates = [
        gate("JEC0", jec0, "18 hashed read-only sources and one convention map"),
        gate("JEC1", jec1, "shear equation and integrated identity close exactly"),
        gate("JEC2", jec2, "full parent/C1 extrinsic curvature closes by two methods and Israel residual is zero"),
        gate("JEC3", jec3, "C1 conservation, orientation, turning, exterior EF, and paired interior-sector sign checks pass"),
        gate("JEC4", jec4, "B0 Cartan reduction and torsion-free/Israel limit pass within declared scope"),
        gate("JEC5", jec5, "S1 local Darmois, constraint, and data ledger reproduced"),
        gate("JEC6", jec6, "N2 baseline, tight repeat, and both perturbation grids reproduced"),
        gate("JEC7", jec7, "TEST 008 exact unit and numerical calibration reproduced"),
        gate("JEC8", jec8, "eight load-bearing claim rows contain scope, controls, limitations, and wording bounds"),
    ]
    all_pass = all(item["status"] == "pass" for item in gates)
    outcome = "JEC-A" if all_pass else "JEC-D"
    result = {
        "test": "TEST_022_JUNCTION_EC_PAPER_DERIVATIONAL_CLOSURE",
        "highest_completed_gate": "JEC8" if all_pass else next(item["gate"] for item in gates if item["status"] == "fail"),
        "outcome": outcome,
        "gates": gates,
        "paper_eligibility": "eligible for novelty review and scoped drafting" if all_pass else "not eligible under current six-result architecture",
        "scope": "Paper closure only; not evidence for a child universe or physical transition.",
    }
    write_json("gate_status.json", result)
    print(result)


if __name__ == "__main__":
    main()
