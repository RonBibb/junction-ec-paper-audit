# Israel tensor, energy conditions, and C1 conservation

Let

\[
\Delta K_\tau=K^\tau{}_{\tau,P}-K^\tau{}_{\tau,C},
\qquad
\Delta K_\theta=K^\theta{}_{\theta,P}-K^\theta{}_{\theta,C}.
\]

Substitution of

\[
\Sigma^a{}_b=\operatorname{diag}(-\sigma,p_s,p_s)
\]

into the complete mixed Israel equation gives

\[
\boxed{
\sigma=-\frac{c^4}{4\pi G}\Delta K_\theta
},
\]

\[
\boxed{
p_s=\frac{c^4}{8\pi G}(\Delta K_\tau+\Delta K_\theta)
}.
\]

All three independent mixed residual components simplify exactly to zero.

## Energy conditions

Useful identities are

\[
\sigma+p_s
=\frac{c^4}{8\pi G}(\Delta K_\tau-\Delta K_\theta),
\]

\[
\sigma+2p_s
=\frac{c^4}{4\pi G}\Delta K_\tau.
\]

For the ordinary child-interior/parent-exterior orientation \(\epsilon_P=+1\), the exterior
angular bound makes \(\Delta K_\theta>0\) for either child-side orientation. Hence

\[
\sigma<0,
\]

and WEC and DEC fail independently of the pressure. NEC and the (2+1)-dimensional SEC
remain conditional on the acceleration-dependent \(\Delta K_\tau\).

Algebraic branches with \(\epsilon_P=-1\) are recorded but correspond to a different
throat/back-to-back global gluing; they are not reclassified as viable ordinary exterior
branches. A simultaneous normal reversal accompanied by exchange of the jump order leaves
the physical surface tensor unchanged.

## Surface conservation

For the covector component \(b=\tau\),

\[
D_a\Sigma^a{}_{\tau}
=-\left[\dot\sigma+2\frac{\dot R}{R}(\sigma+p_s)\right].
\]

The parent Schwarzschild contribution obeys its vacuum Codazzi identity exactly. On the
child side,

\[
K^\theta{}_{\theta,C}=\epsilon_CXH_B,
\qquad
K^\tau{}_{\tau,C}=\epsilon_C
\left(\frac{\dot X}{\gamma}+H_AX\right),
\qquad
\frac{\dot R}{R}=\gamma H_B.
\]

Their Codazzi combination is

\[
\epsilon_C\gamma X
(\dot H_B-H_AH_B+H_B^2).
\]

The child Hamiltonian and longitudinal Einstein equation imply

\[
\dot H_B-H_AH_B+H_B^2
=-\frac{\kappa}{2}(\rho+p).
\]

Therefore

\[
\dot\sigma+2\frac{\dot R}{R}(\sigma+p_s)
=-\epsilon_C\gamma X(\rho+p)
\]

in (c=1) units. Meanwhile

\[
[T_{\mu\nu}n^\mu e^\nu{}_{\tau}]^P_C
=-\epsilon_C\gamma X(\rho+p).
\]

Because (D_a\Sigma^a{}_{\tau}) is the negative of the surface-energy expression,

\[
\boxed{
D_a\Sigma^a{}_{\tau}
+[T_{\mu\nu}n^\mu e^\nu{}_{\tau}]^P_C=0
}.
\]

The nonzero C1 child flux describes a moving shell crossing the comoving child fluid. It is
not a parent-to-child transfer law. The C0 limit \(X=0\) recovers zero flux.

