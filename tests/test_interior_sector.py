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

    def test_same_bulk_pair_realizes_both_density_signs(self):
        data = load("interior_sector.json")
        self.assertTrue(data["both_density_signs_verified"])
        signs = {row["sigma_sign"] for row in data["witness"]["paired_signs"]}
        self.assertEqual(signs, {"positive", "negative"})


if __name__ == "__main__":
    unittest.main()
