import unittest

from helpers import load


class PhysicalUnitsTest(unittest.TestCase):
    def test_exact_calibration_reproduction(self):
        data = load("calibration_status.json")
        self.assertTrue(data["exact_reproduction"])
        self.assertAlmostEqual(data["numeric"]["Tc_over_TPlanck"], 0.8133906806414589, places=14)
        self.assertAlmostEqual(data["numeric"]["rho_c_over_rhoPlanck"], 15.372451912542129, places=13)
        self.assertAlmostEqual(data["numeric"]["M_over_lPlanck"], 0.08811891192485782, places=14)

    def test_scope(self):
        data = load("calibration_status.json")
        self.assertIn("Does not exclude", data["scope"])


if __name__ == "__main__":
    unittest.main()

