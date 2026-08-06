# Complete C1 extrinsic curvature

## Parent exterior

For

\[
X_P^\mu=(T(\tau),R(\tau),\theta,\phi),
\]

proper-time normalization gives

\[
F\dot T^2-\frac{\dot R^2}{F}=1,
\qquad
\beta=\sqrt{F+\dot R^2},
\qquad
\dot T=\frac{\beta}{F}.
\]

The oriented normal covector is

\[
n_{\mu,P}=\epsilon_P\left(-\dot R,\frac{\beta}{F},0,0\right).
\]

Direct embedding acceleration and the derivative identity for \(\beta\) independently give

\[
\boxed{
K^\tau{}_{\tau,P}
=\epsilon_P\frac{\ddot R+m/R^2}{\beta}
},
\qquad
\boxed{
K^\theta{}_{\theta,P}=\epsilon_P\frac{\beta}{R}
}.
\]

The acceleration expression, not \(\dot\beta/\dot R\), defines the turning-point limit.

## Moving child boundary

For

\[
X_C^\mu=(t_C(\tau),\chi(\tau),\theta,\phi),
\qquad R(\tau)=B(t_C(\tau)),
\]

proper-time normalization in \(N=1\) gauge is

\[
\dot t_C^2-A^2\dot\chi^2=1.
\]

Define

\[
X=A\dot\chi,
\qquad
\gamma=\dot t_C=\sqrt{1+X^2}.
\]

Then

\[
n_{\mu,C}=\epsilon_C(-A\dot\chi,A\dot t_C,0,0).
\]

The full result is

\[
\boxed{
K^\tau{}_{\tau,C1}
=\epsilon_C\left(\frac{\dot X}{\gamma}+H_AX\right)
},
\]

\[
\boxed{
K^\theta{}_{\theta,C1}
=\epsilon_CXH_B
=\epsilon_C\frac{X\dot R}{\gamma R}
}.
\]

The calculation is performed twice:

1. coordinate embedding acceleration with the KS Christoffel symbols; and
2. an orthonormal rapidity frame with
   \(u^{\hat a}=(\gamma,X)\) and \(n^{\hat a}=\epsilon_C(X,\gamma)\).

Both components simplify identically. Setting \(X=\dot X=0\) recovers the totally geodesic
C0 result.

## Exterior angular obstruction

For finite real \(X\),

\[
\frac{|X|}{\sqrt{1+X^2}}<1.
\]

For \(F>0\),

\[
|\dot R|<\sqrt{F+\dot R^2}=\beta.
\]

Consequently,

\[
|K^\theta{}_{\theta,C1}|
<\frac{|\dot R|}{R}
<\frac{\beta}{R}.
\]

The child term cannot cancel the parent angular term for the ordinary exterior orientation.
Squaring the cancellation equation gives

\[
X^2=-\frac{\beta^2}{F}<0,
\]

so no real shell rapidity cancels it in \(F>0\).

The executable derivation is `symbolic/c1_extrinsic.py`; the exact output is
`outputs/c1_extrinsic.json`.

