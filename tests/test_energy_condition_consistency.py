import unittest
from pathlib import Path
import sys

import sympy as sp

from helpers import load

SYMBOLIC = Path(__file__).resolve().parents[1] / "symbolic"
sys.path.insert(0, str(SYMBOLIC))
from energy_condition_criteria import CRITERION_VERSION, DECLARATIONS, evaluate


class EnergyConditionConsistencyTest(unittest.TestCase):
    def test_declared_criteria_drive_generated_outputs(self):
        declared = load("energy_conditions.json")
        witness = load("interior_sector.json")["ordinary_matter_witness"]
        self.assertEqual(declared["energy_condition_criterion_version"], CRITERION_VERSION)
        self.assertEqual(witness["energy_condition_criterion_version"], CRITERION_VERSION)
        for key, value in DECLARATIONS.items():
            self.assertEqual(declared["energy_condition_identities"][key], value)
        recomputed = evaluate(
            sp.sympify(witness["sigma_scaled_by_c4_over_8piG"]),
            sp.sympify(witness["pressure_scaled_by_c4_over_8piG"]),
            strict=True,
        )
        self.assertEqual({key: witness[key] for key in recomputed}, recomputed)

    def test_no_symbolic_module_defines_local_condition_booleans(self):
        offenders = []
        for path in SYMBOLIC.glob("*.py"):
            if path.name == "energy_condition_criteria.py":
                continue
            text = path.read_text()
            for key in ("NEC", "WEC", "DEC", "SEC"):
                if f'"{key}": bool(' in text:
                    offenders.append(f"{path.name}:{key}")
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
