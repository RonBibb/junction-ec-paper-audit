import unittest

from helpers import load


class InteriorSectorTest(unittest.TestCase):
    def test_exact_positive_density_interval(self):
        data = load("interior_sector.json")
        self.assertTrue(data["interval_derivation_verified"])
        self.assertEqual(
            data["positive_density_interval"],
            "f<Rdot^2<(1+X^2)f with epsilon_C X Rdot>0",
        )

    def test_regular_future_infalling_witness(self):
        witness = load("interior_sector.json")["witness"]
        self.assertTrue(witness["EF_future"])
        self.assertEqual(witness["EF_proper_time_residual"], "0")
        self.assertEqual(witness["EF_normal_target_residual"], "0")
        self.assertTrue(witness["same_bulk_invariants"])
        self.assertTrue(witness["misner_sharp_order_reversed"])
        self.assertEqual(witness["misner_sharp_ratio_child"], "7/5")
        self.assertEqual(witness["misner_sharp_ratio_parent"], "3/2")

    def test_same_bulk_pair_realizes_both_density_signs(self):
        data = load("interior_sector.json")
        self.assertTrue(data["both_density_signs_verified"])
        signs = {row["sigma_sign"] for row in data["witness"]["paired_signs"]}
        self.assertEqual(signs, {"positive", "negative"})
        self.assertTrue(data["witness"]["reflection_preserves_epsilon_X"])
        self.assertTrue(data["witness"]["fixed_retained_side_reversal_changes_epsilon_X"])

    def test_compatible_witness_satisfies_all_shell_energy_conditions(self):
        witness = load("interior_sector.json")["ordinary_matter_witness"]
        self.assertEqual(witness["compatibility_residual"], "0")
        self.assertEqual(witness["DeltaKtau_target_residual"], "0")
        self.assertEqual(witness["equation_of_state_residual"], "0")
        self.assertTrue(witness["NEC"])
        self.assertTrue(witness["WEC"])
        self.assertTrue(witness["DEC"])
        self.assertTrue(witness["SEC"])

    def test_compatible_bulk_density_and_longitudinal_nec(self):
        witness = load("interior_sector.json")["ordinary_matter_witness"]
        self.assertEqual(witness["bulk_kappa_rho"], "7/5")
        self.assertEqual(
            witness["bulk_kappa_rho_plus_p_chi"],
            "31/20 - 6*sqrt(35)/25",
        )
        self.assertTrue(witness["bulk_density_positive"])
        self.assertTrue(witness["bulk_longitudinal_NEC"])
        self.assertEqual(
            witness["bulk_transverse_NEC"],
            "undetermined without dH_A/dt_C",
        )


if __name__ == "__main__":
    unittest.main()
