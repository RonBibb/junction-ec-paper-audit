import unittest

from helpers import load


class TurningPointTest(unittest.TestCase):
    def test_unsolved_exterior_limit(self):
        data = load("chart_comparison.json")["turning_point_exterior"]
        self.assertIn("sqrt(F)", data["Ktheta_P"])
        self.assertEqual(data["Ktheta_C1"], "0 because H_B=0")
        self.assertIn("finite", data["pressure"])

    def test_horizon_is_not_turning_point(self):
        data = load("chart_comparison.json")["horizon_infall_limit"]
        self.assertIn("forbids Rdot=0", data["turning_at_horizon"])


if __name__ == "__main__":
    unittest.main()

