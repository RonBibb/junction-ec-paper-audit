import unittest

from helpers import load


class RegularChartTest(unittest.TestCase):
    def test_complete_parent_tensor_agrees(self):
        data = load("chart_comparison.json")
        self.assertTrue(data["Ktau_chart_agreement"])
        self.assertTrue(data["Ktheta_chart_agreement"])
        self.assertEqual(data["Ktau_difference_numerator_after_beta_identity"], "0")
        self.assertEqual(data["time_transform_residual_after_beta_identity"], "0")

    def test_no_time_reversal_inference(self):
        data = load("chart_comparison.json")
        self.assertTrue(data["time_reversal_ruling"].startswith("No."))


if __name__ == "__main__":
    unittest.main()

