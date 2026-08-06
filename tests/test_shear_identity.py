import unittest

from helpers import load


class ShearIdentityTest(unittest.TestCase):
    def test_exact_subtraction_and_integral(self):
        data = load("shear_identity.json")
        self.assertTrue(data["isotropic_identity_verified"])
        self.assertEqual(data["isotropic_subtraction_residual"], "0")
        self.assertEqual(data["integrated_residual"], "0")
        self.assertTrue(data["constraint_propagation_verified"])
        self.assertEqual(data["constraint_propagation_residual"], "0")
        self.assertIn("p_A - p_B", data["anisotropic_pressure_equation"])


if __name__ == "__main__":
    unittest.main()
