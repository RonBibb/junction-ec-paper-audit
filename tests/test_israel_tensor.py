import unittest

from helpers import load


class IsraelTensorTest(unittest.TestCase):
    def test_full_mixed_residual(self):
        data = load("energy_conditions.json")
        self.assertTrue(data["tensor_residual_zero"])
        self.assertEqual(data["mixed_tensor_residual"], [["0", "0", "0"]] * 3)

    def test_energy_condition_scope(self):
        data = load("energy_conditions.json")
        ordinary = [row for row in data["orientation_branches"] if row["ordinary_parent_exterior"]]
        self.assertEqual(len(ordinary), 2)
        self.assertTrue(all(row["WEC"] == "violated" for row in ordinary))
        self.assertTrue(all(row["DEC"] == "violated" for row in ordinary))


if __name__ == "__main__":
    unittest.main()

