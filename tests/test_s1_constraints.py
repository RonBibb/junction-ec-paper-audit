import unittest

from helpers import load


class S1ConstraintsTest(unittest.TestCase):
    def test_local_data_and_constraint(self):
        data = load("s1_status.json")
        self.assertEqual(data["parent_hamiltonian_residual"], "0")
        self.assertEqual(data["child_minus_parent_constraint"], "-kappa*rho_eff")
        self.assertEqual(data["data_count"]["hidden_surface_functions"], 0)
        self.assertTrue(data["all_required_local_checks"])

    def test_no_global_promotion(self):
        status = load("s1_status.json")["classification"]
        self.assertEqual(status["global_nonsingular_extension"], "not proven")
        self.assertIn("not established", status["areal_turning"])


if __name__ == "__main__":
    unittest.main()

