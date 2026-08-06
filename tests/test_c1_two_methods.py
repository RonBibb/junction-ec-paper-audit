import unittest

from helpers import load


class C1TwoMethodsTest(unittest.TestCase):
    def test_child_components(self):
        child = load("c1_extrinsic.json")["child_C1"]
        self.assertTrue(child["Ktau_methods_agree"])
        self.assertTrue(child["Ktau_target_verified"])
        self.assertTrue(child["Ktheta_methods_agree"])
        self.assertTrue(child["Ktheta_target_verified"])

    def test_parent_components(self):
        parent = load("c1_extrinsic.json")["parent"]
        self.assertTrue(parent["Ktau_methods_agree_away_from_turn"])
        self.assertIn("Rddot", parent["Ktau_acceleration"])
        self.assertTrue(load("c1_extrinsic.json")["flat_space_control"]["verified"])


if __name__ == "__main__":
    unittest.main()
