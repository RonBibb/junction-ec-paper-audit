import unittest

from helpers import load


class SurfaceConservationTest(unittest.TestCase):
    def test_c1_flux_closure(self):
        data = load("conservation_status.json")
        self.assertEqual(data["parent_codazzi_residual"], "0")
        self.assertEqual(data["child_codazzi_target_residual"], "0")
        self.assertEqual(data["Q_tau"], "0")
        self.assertTrue(data["Q_tau_zero"])
        self.assertIn("not parent-child mass transfer", data["interpretation"])


if __name__ == "__main__":
    unittest.main()

