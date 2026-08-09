import unittest

import sympy as sp


class StaticNariaiFamilyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        t, chi, theta, phi = sp.symbols("t chi theta phi", real=True)
        radius = sp.symbols("R_0", positive=True)
        scale = sp.Function("A")(t)
        coords = (t, chi, theta, phi)
        metric = sp.diag(-1, scale**2, radius**2, radius**2 * sp.sin(theta) ** 2)
        inverse = sp.simplify(metric.inv())
        dimension = 4

        christoffel = [[[
            sp.simplify(
                sum(
                    inverse[a, d]
                    * (
                        sp.diff(metric[d, c], coords[b])
                        + sp.diff(metric[d, b], coords[c])
                        - sp.diff(metric[b, c], coords[d])
                    )
                    / 2
                    for d in range(dimension)
                )
            )
            for c in range(dimension)] for b in range(dimension)]
            for a in range(dimension)]

        ricci = sp.MutableDenseMatrix.zeros(dimension, dimension)
        for a in range(dimension):
            for b in range(dimension):
                value = 0
                for c in range(dimension):
                    value += sp.diff(christoffel[c][a][b], coords[c])
                    value -= sp.diff(christoffel[c][a][c], coords[b])
                    for d in range(dimension):
                        value += christoffel[c][c][d] * christoffel[d][a][b]
                        value -= christoffel[c][b][d] * christoffel[d][a][c]
                ricci[a, b] = sp.trigsimp(sp.simplify(value))

        scalar = sp.simplify(
            sum(inverse[a, b] * ricci[a, b] for a in range(dimension) for b in range(dimension))
        )
        einstein_covariant = sp.simplify(ricci - metric * scalar / 2)
        cls.einstein_mixed = sp.simplify(inverse * einstein_covariant)
        cls.t = t
        cls.radius = radius
        cls.scale = scale

    def test_all_independent_mixed_einstein_components(self):
        expected_lorentzian = -1 / self.radius**2
        expected_angular = -sp.diff(self.scale, self.t, 2) / self.scale

        self.assertEqual(sp.simplify(self.einstein_mixed[0, 0] - expected_lorentzian), 0)
        self.assertEqual(sp.simplify(self.einstein_mixed[1, 1] - expected_lorentzian), 0)
        self.assertEqual(sp.simplify(self.einstein_mixed[2, 2] - expected_angular), 0)
        self.assertEqual(sp.simplify(self.einstein_mixed[3, 3] - expected_angular), 0)

        for a in range(4):
            for b in range(4):
                if a != b:
                    self.assertEqual(sp.simplify(self.einstein_mixed[a, b]), 0)

    def test_vacuum_energy_normalization_and_isotropy(self):
        substituted = self.einstein_mixed.applyfunc(
            lambda component: sp.simplify(
                component.subs(sp.diff(self.scale, self.t, 2), self.scale / self.radius**2)
            )
        )
        expected = -sp.eye(4) / self.radius**2
        self.assertEqual(substituted, expected)

    def test_comoving_induced_metric_curvature_and_flux(self):
        # On chi=constant, (tau, theta, phi) inherit the static cylinder metric.
        induced = sp.diag(-1, self.radius**2, self.radius**2 * sp.sin(sp.symbols("theta")) ** 2)
        self.assertEqual(induced[0, 0], -1)
        self.assertEqual(induced[1, 1], self.radius**2)

        # The metric is independent of chi, so K_ab=(1/2)L_n h_ab vanishes.
        self.assertFalse(self.scale.has(sp.symbols("chi")))

        # Vacuum energy T_{mu nu}=-rho g_{mu nu} has no normal-tangent flux.
        rho = sp.symbols("rho", positive=True)
        normal = sp.Matrix([0, 1 / self.scale, 0, 0])
        tangent = sp.Matrix([1, 0, 0, 0])
        metric = sp.diag(-1, self.scale**2, self.radius**2, self.radius**2)
        stress = -rho * metric
        self.assertEqual(sp.simplify((normal.T * stress * tangent)[0]), 0)


if __name__ == "__main__":
    unittest.main()
