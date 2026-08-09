import unittest

import sympy as sp


class NecCriterionTest(unittest.TestCase):
    def setUp(self):
        self.R, self.m = sp.symbols("R m", positive=True)
        self.Rdot, self.Rddot = sp.symbols("Rdot Rddot", real=True)
        self.X, self.Xdot, self.HA = sp.symbols("X Xdot H_A", real=True)
        self.epsilon_c = sp.symbols("epsilon_C", real=True)
        self.F = 1 - 2 * self.m / self.R
        self.beta = sp.sqrt(self.F + self.Rdot**2)
        self.gamma = sp.sqrt(1 + self.X**2)

    def test_parent_nec_combination_simplifies(self):
        direct = (
            (self.Rddot + self.m / self.R**2) / self.beta
            - self.beta / self.R
        )
        reduced = (
            self.R * self.Rddot
            - self.Rdot**2
            - 1
            + 3 * self.m / self.R
        ) / (self.beta * self.R)
        self.assertEqual(sp.simplify(direct - reduced), 0)

    def test_full_nec_combination_matches_curvature_jump(self):
        Ktau_p = (self.Rddot + self.m / self.R**2) / self.beta
        Ktheta_p = self.beta / self.R
        Ktau_c = self.epsilon_c * (
            self.Xdot / self.gamma + self.HA * self.X
        )
        Ktheta_c = (
            self.epsilon_c * self.X * self.Rdot / (self.gamma * self.R)
        )
        jump_difference = (Ktau_p - Ktau_c) - (Ktheta_p - Ktheta_c)
        criterion = (
            self.R * self.Rddot
            - self.Rdot**2
            - 1
            + 3 * self.m / self.R
        ) / (self.beta * self.R) - self.epsilon_c * (
            self.Xdot / self.gamma
            + self.HA * self.X
            - self.X * self.Rdot / (self.gamma * self.R)
        )
        self.assertEqual(sp.simplify(jump_difference - criterion), 0)

    def test_static_comoving_threshold(self):
        static_value = sp.simplify(
            (
                (self.Rddot + self.m / self.R**2) / self.beta
                - self.beta / self.R
            ).subs({self.Rdot: 0, self.Rddot: 0})
        )
        expected = (3 * self.m - self.R) / (
            self.R**2 * sp.sqrt(1 - 2 * self.m / self.R)
        )
        self.assertEqual(sp.simplify(static_value - expected), 0)
        self.assertLess(float(expected.subs({self.m: 1, self.R: 4})), 0)
        self.assertEqual(sp.simplify(expected.subs(self.R, 3 * self.m)), 0)

    def test_static_comoving_surface_tensor(self):
        prefactor = sp.symbols("A", positive=True)
        root_f = sp.sqrt(self.F)
        sigma = -prefactor * root_f / self.R
        pressure = prefactor * (self.R - self.m) / (
            2 * self.R**2 * root_f
        )
        equation_of_state = -(self.R - self.m) / (
            2 * (self.R - 2 * self.m)
        )
        nec = prefactor * (3 * self.m - self.R) / (
            2 * self.R**2 * root_f
        )
        sec_second = prefactor * self.m / (self.R**2 * root_f)

        self.assertEqual(sp.simplify(pressure / sigma - equation_of_state), 0)
        self.assertEqual(sp.simplify(sigma + pressure - nec), 0)
        self.assertEqual(sp.simplify(sigma + 2 * pressure - sec_second), 0)
        self.assertLess(float(nec.subs({prefactor: 1, self.m: 1, self.R: 4})), 0)
        self.assertGreater(
            float(sec_second.subs({prefactor: 1, self.m: 1, self.R: 4})), 0
        )

    def test_static_isotropic_bulk_witness(self):
        t, R0 = sp.symbols("t R_0", real=True, positive=True)
        A_plus, A_minus = sp.symbols("A_plus A_minus", real=True)
        scale = A_plus * sp.exp(t / R0) + A_minus * sp.exp(-t / R0)

        self.assertEqual(sp.simplify(sp.diff(scale, t, 2) - scale / R0**2), 0)

        kappa = sp.symbols("kappa", positive=True)
        density = 1 / (kappa * R0**2)
        pressure = -1 / (kappa * R0**2)
        self.assertEqual(sp.simplify(density + pressure), 0)


if __name__ == "__main__":
    unittest.main()
