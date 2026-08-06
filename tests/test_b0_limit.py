import unittest

from helpers import load


class B0LimitTest(unittest.TestCase):
    def test_cartan_and_israel_limit(self):
        data = load("cartan_b0.json")
        self.assertTrue(data["general_solution_unique"])
        self.assertTrue(data["matches_trautman_equation_25"])
        self.assertTrue(data["weyssenhoff_cartan_residual_zero"])
        self.assertTrue(data["israel_recovered"])
        self.assertEqual(data["mean_boundary_torsion"], "0")

    def test_scope_is_limited(self):
        data = load("cartan_b0.json")
        self.assertIn("polarized B1/B2", data["scope"])


if __name__ == "__main__":
    unittest.main()

