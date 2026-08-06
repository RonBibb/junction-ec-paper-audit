import unittest

from helpers import load


class EventReproductionTest(unittest.TestCase):
    def test_n2_and_original_outputs(self):
        data = load("event_status.json")
        comparison = data["comparison"]
        self.assertEqual(data["classification"], "N2")
        self.assertTrue(comparison["event_equal"])
        self.assertLessEqual(comparison["event_time_abs"], 1e-8)
        self.assertLessEqual(comparison["endpoint_B_abs"], 1e-8)
        self.assertLessEqual(comparison["endpoint_Theta_abs"], 1e-8)
        self.assertTrue(all(comparison["grid_counts_equal"]))

    def test_numerical_controls(self):
        data = load("event_status.json")
        self.assertLessEqual(data["baseline"]["max_constraint"], 1e-8)
        self.assertLessEqual(data["tight_baseline"]["max_constraint"], 1e-8)
        self.assertEqual(data["grids"][0]["counts"]["areal_turn"], 0)
        self.assertEqual(data["grids"][1]["counts"]["areal_turn"], 3)


if __name__ == "__main__":
    unittest.main()

