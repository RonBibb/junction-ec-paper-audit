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

    def test_one_common_normal_and_retained_side_map(self):
        data = load("energy_conditions.json")
        self.assertIn("eta<0", data["common_normal"])
        self.assertIn("eta>0", data["common_normal"])
        self.assertIn("not independently outward", data["one_sided_limits"])
        self.assertEqual(data["parent_retained_side_map"]["ordinary exterior containing spatial infinity"], 1)
        self.assertEqual(data["child_retained_side_map"]["chi<=chi_Sigma"], 1)
        self.assertEqual(data["child_retained_side_map"]["chi>=chi_Sigma"], -1)

    def test_intrinsic_three_dimensional_sec(self):
        data = load("energy_conditions.json")
        self.assertEqual(data["energy_condition_identities"]["SEC_2plus1"], "NEC and p_s>=0")
        for branch in data["orientation_branches"]:
            self.assertIn("DeltaKtau+DeltaKtheta>=0", branch["SEC"])


if __name__ == "__main__":
    unittest.main()
