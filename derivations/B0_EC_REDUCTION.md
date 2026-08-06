# B0 Einstein–Cartan reduction

The declared first-order Einstein–Cartan model gives the algebraic Cartan equation

\[
Q^\rho{}_{\mu\nu}
+\delta^\rho_\mu Q^\sigma{}_{\nu\sigma}
-\delta^\rho_\nu Q^\sigma{}_{\mu\sigma}
=\kappa s^\rho{}_{\mu\nu}.
\]

TEST 022 solves all 24 independent torsion components for a general source antisymmetric in
\(\mu,\nu\). The solution is unique and reproduces the declared Trautman convention,

\[
Q^\rho{}_{\mu\nu}
=\kappa\left(
s^\rho{}_{\mu\nu}
+\frac12\delta^\rho_\mu s^\sigma{}_{\nu\sigma}
+\frac12\delta^\rho_\nu s^\sigma{}_{\sigma\mu}
\right).
\]

For a Weyssenhoff source

\[
s^\rho{}_{\mu\nu}=u^\rho s_{\mu\nu}
\]

with the Frenkel condition \(s_{\mu\nu}u^\nu=0\), the trace terms vanish and

\[
Q^\rho{}_{\mu\nu}=\kappa u^\rho s_{\mu\nu}.
\]

Every component of the original Cartan equation then has zero residual.

At fixed coframe, the Cartan map is algebraic and linear, so

\[
\langle Q\rangle=Q[\langle s\rangle].
\]

The B0 result additionally requires the separately declared boundary regularity assumption

\[
\operatorname{Tr}_\Sigma\langle s\rangle
=\left\langle\operatorname{Tr}_\Sigma s\right\rangle
\qquad\text{(A_B)}.
\]

Under

- unpolarized mean spin \(\langle s_{\mu\nu}\rangle=0\);
- finite one-sided traces and A_B;
- no independent surface-spin action; and
- no distributional contorsion,

the mean boundary torsion vanishes. The mean connection at the surface is Levi–Civita and
there is no independent B0 torsion term in the angular junction equation. Ordinary Israel
matching is recovered.

This does not remove the spin-squared contribution from the bulk effective stress after
torsion elimination. Nor does it classify polarized B1/B2 matter, boundary polarization,
surface-spin actions, correlated geometry–spin fluctuations, or finite-thickness
transitions.

The exact general solve, Weyssenhoff residual, and torsion-free limit are implemented in
`symbolic/cartan_b0.py`.

