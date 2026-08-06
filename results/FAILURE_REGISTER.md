# TEST 022 Failure and correction register

## Corrections preserved from the source tests

1. **TEST 001 shear ansatz:** \(s\propto V^{-1}\) omitted the curvature-sourced particular
   solution. It remains retracted.
2. **TEST 002 V1 moving shell:** the angular curvature omitted the child time factor. J0-C
   remains retracted.
3. **TEST 002 V2 paper gap:** C1 temporal curvature, pressure, conservation, and the complete
   regular-chart tensor were claimed more broadly than implemented. TEST 022 closes all four.
4. **TEST 006 event prediction:** the cubic root was not a controlled exact event prediction.
   TEST 007/022 reproduce N2 instead.

## TEST 022 implementation correction

During the pre-gate independent C1 calculation, the coordinate-form angular-curvature code
temporarily retained an extra factor (A^{-1}\). The orthonormal-frame comparison returned a
nonzero mismatch immediately. The expression was corrected to

\[
K^\theta{}_{\theta,C1}=\epsilon_C A\dot\chi\frac{\partial_tB}{B}
=\epsilon_CXH_B
\]

before any gate or scientific outcome was evaluated. The failed intermediate expression was
never used in an output classification. This correction is recorded to preserve the audit
trail.

## Surviving limitations, not implementation failures

- The exterior theorem does not cover (F<0\), arbitrary embeddings, spacelike junctions,
  or smooth transitions.
- B0 does not classify polarized B1/B2 or independent surface-spin theories.
- S1 supplies local compatible data and bounded evolution, not a global transition.
- N2 is not a bounce.
- TEST 008 excludes only the declared standard thermal calibration.
- No mass-transfer, time-compression, CMB, halo, or empirical mechanism is derived.

