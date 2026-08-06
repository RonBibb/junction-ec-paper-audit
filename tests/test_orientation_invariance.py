import unittest

from helpers import load


class OrientationInvarianceTest(unittest.TestCase):
    def test_explicit_branch_table(self):
        data = load("energy_conditions.json")
        self.assertEqual(len(data["orientation_branches"]), 4)
        signs = {(row["epsilon_P"], row["epsilon_C"]): row["sigma_sign_from_exterior_bound"] for row in data["orientation_branches"]}
        self.assertEqual(signs[(1, 1)], "negative")
        self.assertEqual(signs[(1, -1)], "negative")
        self.assertEqual(signs[(-1, 1)], "positive")
        self.assertEqual(signs[(-1, -1)], "positive")

    def test_convention_and_topology_not_confused(self):
        data = load("energy_conditions.json")
        self.assertIn("exchange jump order", data["convention_reversal"])
        self.assertTrue(data["convention_reversal_verified"])
        self.assertIn("different throat/back-to-back", data["nonordinary_warning"])


if __name__ == "__main__":
    unittest.main()
