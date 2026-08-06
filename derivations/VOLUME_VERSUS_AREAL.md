# Volume versus areal turning

In anisotropic Kantowski–Sachs evolution, the following are distinct events:

\[
\Theta=0,qquad \dot\Theta>0
\]

for total-volume turning, and

\[
H_B=0,qquad \dot H_B>0,qquad B>0
\]

for areal-radius turning.

TEST 022 independently reruns the TEST 007 ODE system, baseline, ten-times-tighter baseline,
and all 54 constraint-preserving perturbation trajectories.

For the baseline \(M=\kappa=\alpha=1\), \(w=1/3\), and \(x=2\), the trajectory reaches
\(t=M\) with

\[
A=1.505474578235734,
\qquad
B=1.25147252663268M,
\]

\[
H_A=0.9333421567227373/M,
\qquad
H_B=-0.11054831358970746/M,
\]

\[
\Theta=0.7122455295433224/M.
\]

Thus total volume is expanding while the angular two-spheres continue contracting. The
maximum normalized Hamiltonian residual is below \(4\times10^{-15}\) in the baseline. The
tight repeat gives the same event classification and agrees well inside the TEST 022
tolerances.

The perturbation results reproduce:

- \(\pm1\%\): 0/27 areal turns;
- \(\pm10\%\): 3/27 positive-radius areal turns.

All 54 individual event records, times, endpoint diagnostics, maximum constraint residuals,
and maximum Kretschmann values are retained in `outputs/event_status.json`.

The 3/27 exploratory turns do not establish an open areal-bounce region, and the finite
baseline interval does not establish later behavior. The correct outcome remains N2:
bounded volume expansion without baseline areal turning.

