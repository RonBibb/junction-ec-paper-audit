#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path

from scipy.integrate import solve_ivp

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parent
OUT = ROOT / "outputs"
SOURCE = PROJECT / "parent-child-s1-numerical" / "outputs" / "continuation.json"


def matter(y, config):
    _, _, _, _, rho, number = y
    return rho - config["alpha"] * number**2, config["w"] * rho - config["alpha"] * number**2


def rhs(_, y, config):
    A, B, HA, HB, rho, number = y
    _, p_eff = matter(y, config)
    theta = HA + 2 * HB
    bdd_over_b = -(config["kappa"] * p_eff + B ** -2 + HB**2) / 2
    add_over_a = -config["kappa"] * p_eff - bdd_over_b - HA * HB
    return [
        HA * A,
        HB * B,
        add_over_a - HA**2,
        bdd_over_b - HB**2,
        -(1 + config["w"]) * theta * rho,
        -theta * number,
    ]


def diagnostics(y, config):
    A, B, HA, HB, rho, number = y
    rho_eff, p_eff = matter(y, config)
    theta = HA + 2 * HB
    shear = HA - HB
    derivatives = rhs(0, y, config)
    add_over_a = derivatives[2] + HA**2
    bdd_over_b = derivatives[3] + HB**2
    constraint = 2 * HA * HB + HB**2 + B ** -2 - config["kappa"] * rho_eff
    scale = abs(2 * HA * HB) + HB**2 + B ** -2 + abs(config["kappa"] * rho_eff) + 1e-30
    ricci = 2 * add_over_a + 4 * bdd_over_b + 4 * HA * HB + 2 * HB**2 + 2 * B ** -2
    ricci2 = config["kappa"] ** 2 * (rho_eff**2 + 3 * p_eff**2)
    kretschmann = 4 * (
        add_over_a**2
        + 2 * bdd_over_b**2
        + 2 * (HA * HB) ** 2
        + ((1 + (HB * B) ** 2) / B**2) ** 2
    )
    finite_scale = HA**2 + 2 * HB**2 + B ** -2 + config["kappa"] * abs(rho) + 1e-30
    return {
        "A": A,
        "B": B,
        "HA": HA,
        "HB": HB,
        "Theta": theta,
        "s": shear,
        "rho_eff": rho_eff,
        "p_eff": p_eff,
        "constraint_normalized": abs(constraint) / scale,
        "Ricci": ricci,
        "Ricci2": ricci2,
        "Kretschmann": kretschmann,
        "finite_shear_ratio": shear**2 / finite_scale,
        "spin_interaction": config["alpha"] * number**2,
    }


def initial(config, deltas=(0.0, 0.0, 0.0)):
    mass = config["M"]
    w = config["w"]
    B = 1.5 * mass * (1 + deltas[0])
    HB = (-2 * math.sqrt(3) / (9 * mass)) * (1 + deltas[1])
    mu = config["x"] / (config["kappa"] * (1 - w) * mass**2) * (1 + deltas[2])
    rho = mu
    number = math.sqrt(mu / config["alpha"])
    HA = (-HB**2 - B ** -2) / (2 * HB)
    return [1 / math.sqrt(3), B, HA, HB, rho, number]


def run_one(config, deltas=(0.0, 0.0, 0.0), tight=False):
    y0 = initial(config, deltas)
    initial_diag = diagnostics(y0, config)
    curvature_stop = config["curvature_factor_stop"] * initial_diag["Kretschmann"]

    def areal_turn(_, y):
        return y[3]

    areal_turn.direction = 1
    areal_turn.terminal = True

    def b_floor(_, y):
        return y[1] - config["B_floor"] * config["M"]

    b_floor.direction = -1
    b_floor.terminal = True

    def curvature(_, y):
        return curvature_stop - diagnostics(y, config)["Kretschmann"]

    curvature.direction = -1
    curvature.terminal = True

    def constraint(_, y):
        return config["constraint_tolerance"] - diagnostics(y, config)["constraint_normalized"]

    constraint.direction = -1
    constraint.terminal = True

    factor = 0.1 if tight else 1.0
    solution = solve_ivp(
        lambda t, y: rhs(t, y, config),
        (0, config["t_max"] * config["M"]),
        y0,
        method="DOP853",
        rtol=config["rtol"] * factor,
        atol=config["atol"] * factor,
        max_step=config["max_step"] * config["M"] * factor,
        events=(areal_turn, b_floor, curvature, constraint),
    )
    names = ("areal_turn", "B_floor", "curvature_stop", "constraint_stop")
    event = "t_max"
    event_time = float(solution.t[-1])
    event_state = solution.y[:, -1]
    for name, times, states in zip(names, solution.t_events, solution.y_events):
        if len(times):
            event = name
            event_time = float(times[0])
            event_state = states[0]
            break
    all_diag = [diagnostics(solution.y[:, idx], config) for idx in range(solution.y.shape[1])]
    return {
        "deltas": list(deltas),
        "event": event,
        "time": event_time,
        "diagnostics": diagnostics(event_state, config),
        "max_constraint": max(item["constraint_normalized"] for item in all_diag),
        "max_Kretschmann": max(item["Kretschmann"] for item in all_diag),
        "steps": len(solution.t),
        "solver_success": bool(solution.success),
    }


def main():
    original = json.loads(SOURCE.read_text())
    config = original["config"]
    baseline = run_one(config)
    tight = run_one(config, tight=True)
    grids = []
    for level in (0.01, 0.10):
        cases = [run_one(config, delta) for delta in itertools.product((-level, 0, level), repeat=3)]
        counts = {
            event: sum(case["event"] == event for case in cases)
            for event in ("areal_turn", "B_floor", "curvature_stop", "constraint_stop", "t_max")
        }
        grids.append(
            {
                "level": level,
                "cases": len(cases),
                "counts": counts,
                "turn_fraction": counts["areal_turn"] / len(cases),
                "min_turn_B": min(
                    (case["diagnostics"]["B"] for case in cases if case["event"] == "areal_turn"),
                    default=None,
                ),
                "max_constraint": max(case["max_constraint"] for case in cases),
                "max_Kretschmann": max(case["max_Kretschmann"] for case in cases),
                "runs": cases,
            }
        )

    reproduced = {
        "source": str(SOURCE.relative_to(PROJECT)),
        "config": config,
        "baseline": baseline,
        "tight_baseline": tight,
        "grids": grids,
        "comparison": {
            "event_equal": baseline["event"] == original["baseline"]["event"],
            "event_time_abs": abs(baseline["time"] - original["baseline"]["time"]),
            "endpoint_B_abs": abs(baseline["diagnostics"]["B"] - original["baseline"]["diagnostics"]["B"]),
            "endpoint_Theta_abs": abs(baseline["diagnostics"]["Theta"] - original["baseline"]["diagnostics"]["Theta"]),
            "grid_counts_equal": [
                grids[index]["counts"] == original["grids"][index]["counts"] for index in range(2)
            ],
        },
        "classification": "N2",
        "interpretation": "Volume expands while B remains contracting through t=M; 3/27 ten-percent cases turn, not an open bounce region.",
    }
    (OUT / "event_status.json").write_text(json.dumps(reproduced, indent=2, sort_keys=True) + "\n")
    print(json.dumps(reproduced["comparison"], indent=2))


if __name__ == "__main__":
    main()
