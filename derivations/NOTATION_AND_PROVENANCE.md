# Notation and provenance

## Active convention

The metric signature is ((-+++)). The child metric is

\[
ds_C^2=-N^2dt^2+A^2(t)d\chi^2+B^2(t)d\Omega_2^2,
\]

with

\[
H_A=\frac{\dot A}{NA},\qquad H_B=\frac{\dot B}{NB},\qquad
\Theta=H_A+2H_B,\qquad s=H_A-H_B.
\]

After deriving the C1 normalization equation, the child calculation uses proper time
\(N=1\). A dot on a shell variable is \(d/d\tau\); a time derivative appearing in
\(H_A,H_B\) is with respect to child proper time. The distinction is made explicit through
\(\gamma=dt_C/d\tau\).

The parent exterior is

\[
ds_P^2=-F(R)dT^2+F(R)^{-1}dR^2+R^2d\Omega_2^2,
\qquad F=1-\frac{2m}{R},
\]

in geometrized units, with \(m=GM/c^2\). Physical factors are restored in surface
quantities.

The jump is

\[
[K^a{}_b]=K^a{}_{b,P}-K^a{}_{b,C},
\]

and

\[
\Sigma^a{}_b=\operatorname{diag}(-\sigma,p_s,p_s).
\]

The Israel equation is

\[
[K_{ab}]-h_{ab}[K]=-
\frac{8\pi G}{c^4}\Sigma_{ab}.
\]

The extrinsic-curvature convention is

\[
K_{ab}=e_a{}^\mu e_b{}^\nu\nabla_\mu n_\nu
=-n_\mu\left(\partial_a\partial_bX^\mu
+\Gamma^\mu{}_{\nu\lambda}\partial_aX^\nu\partial_bX^\lambda\right).
\]

It is anchored by an outward normal on a round sphere in flat space, for which
\(K^\theta{}_{\theta}=+1/R\).

## Translation table

| Active symbol | Earlier package notation | Meaning |
|---|---|---|
| \(A\) | `a_par`, \(a_\parallel\) | longitudinal KS scale |
| \(B\) | `a_perp`, \(a_\perp\) | angular/areal KS scale |
| \(H_A\) | `Hpar` | longitudinal Hubble rate |
| \(H_B\) | `Hperp` | angular Hubble rate |
| \(s\) | `Hpar-Hperp` | signed shear variable |
| \(V=AB^2\) | `V` | volume per fiducial longitudinal length |
| \(m\) | `M` in geometrized test code | Schwarzschild mass length \(GM/c^2\) |
| \(\Sigma^a{}_b\) | `S^a_b` | surface stress tensor |
| \(\sigma\) | `sigma` | surface energy density |
| \(X=A\dot\chi\) | `a_par*chidot` | shell rapidity variable relative to the child fluid |
| \(\gamma=\sqrt{1+X^2}\) | `N*tdot_C` | child-fluid Lorentz factor |

## Retractions preserved

1. The homogeneous relation \(s\propto V^{-1}\) is not the complete KS shear solution; it
   omits the curvature-sourced particular integral.
2. TEST 002 V1 outcome J0-C is retracted. Its moving angular curvature omitted
   \(dt_C/d\tau\).
3. The TEST 006 cubic candidate time is not an exact event prediction; TEST 007 did not
   reproduce it for the baseline within \(t\le M\).

## Provenance control

`outputs/equation_manifest.json` contains the exact path, locator, epistemic status, and
SHA-256 hash for all 18 imported files. Earlier packages are read-only. TEST 022 generates
new files only under `junction-ec-paper-audit/`.

