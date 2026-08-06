# Curvature-sourced shear

For isotropic effective pressure, the independent spatial Einstein equations may be written

\[
2\dot H_B+3H_B^2+\frac1{B^2}=-\kappa p,
\]

\[
\dot H_A+\dot H_B+H_A^2+H_B^2+H_AH_B=-\kappa p.
\]

Subtracting the first from the second gives

\[
\dot H_A-\dot H_B+H_A^2+H_AH_B-2H_B^2-\frac1{B^2}=0.
\]

Since \(s=H_A-H_B\) and \(\Theta=H_A+2H_B\),

\[
\boxed{\dot s+\Theta s=\frac1{B^2}}.
\]

With \(V=AB^2\), \(\dot V=\Theta V\), so

\[
\frac{d}{dt}(Vs)=\frac{V}{B^2}=A.
\]

Therefore

\[
\boxed{
s(t)=\frac{C+\int^t A(t')\,dt'}{A(t)B^2(t)}
}.
\]

The discarded \(C/V\) relation is only the homogeneous part.

If longitudinal and angular pressures differ, with \(p_A\) and \(p_B\) respectively, the
same subtraction gives

\[
\dot s+\Theta s=\frac1{B^2}+\kappa(p_A-p_B).
\]

The exact symbolic subtraction and integrated derivative are in
`symbolic/shear_identity.py` and `outputs/shear_identity.json`. Constraint preservation is
separately imported from TEST 005, where \(\dot C=-\Theta C\).

