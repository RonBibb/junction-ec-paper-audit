# TEST 022 — Final Arbiter Packet

**File manifest:** `README.md`, `CITATIONS.md`, `requirements.txt`, `verify.sh`, two frozen
configuration files, nine derivation ledgers, ten symbolic/audit modules, two numerical
reproduction programs, eleven test files containing 20 checks, thirteen JSON outputs,
execution logs, `RESULTS.md`, `FAILURE_REGISTER.md`, and this packet.  
**Highest completed gate:** **JEC8**  
**Outcome:** **JEC-A — six-result derivational closure**

## Gate ledger

| Gate | Status | Result |
|---|---|---|
| JEC0 | Pass | Eighteen read-only sources are located, scoped, and SHA-256 hashed; notation is translated. |
| JEC1 | Pass | The shear equation and integrated identity close exactly. |
| JEC2 | Pass | Full parent/C1 temporal and angular extrinsic curvature agrees by two methods; the complete Israel residual is zero. |
| JEC3 | Pass | C1 surface conservation, orientation table, turning limit, and complete ingoing-EF parent tensor pass. |
| JEC4 | Pass | The B0 Cartan reduction and torsion-free/Israel limit pass within the declared unpolarized scope. |
| JEC5 | Pass | S1 local Darmois data, constraints, causal classification, and data count reproduce. |
| JEC6 | Pass | N2, the tight repeat, and all 54 perturbation runs reproduce with residuals inside tolerance. |
| JEC7 | Pass | TEST 008's exact unit chain and numerical calibration reproduce. |
| JEC8 | Pass | Every abstract, theorem, figure, and conclusion claim has artifacts, domain, status, control, limitation, and permitted/prohibited wording. |

## Working results

### 1. Curvature-sourced shear

\[
\dot s+\Theta s=\frac1{B^2},
\qquad
s(t)=\frac{C+\int^t A(t')dt'}{A(t)B^2(t)}.
\]

Anisotropic pressure adds \(\kappa(p_A-p_B)\).

### 2. Complete scoped exterior timelike obstruction

For the moving child boundary,

\[
K^\tau{}_{\tau,C1}
=\epsilon_C\left(\frac{\dot X}{\gamma}+H_AX\right),
\qquad
K^\theta{}_{\theta,C1}=\epsilon_CXH_B,
\qquad
\gamma=\sqrt{1+X^2}.
\]

The parent components are

\[
K^\tau{}_{\tau,P}
=\epsilon_P\frac{\ddot R+m/R^2}{\beta},
\qquad
K^\theta{}_{\theta,P}=\epsilon_P\frac{\beta}{R},
\qquad
\beta=\sqrt{F+\dot R^2}.
\]

The complete Israel solution is

\[
\sigma=-\frac{c^4}{4\pi G}\Delta K_\theta,
\qquad
p_s=\frac{c^4}{8\pi G}(\Delta K_\tau+\Delta K_\theta).
\]

For the ordinary exterior orientation, the angular bound forces \(\sigma<0\) for C0 and C1,
so WEC and DEC fail. The full C1 conservation residual is exactly zero after including the
moving child-fluid flux. Schwarzschild and ingoing Eddington–Finkelstein components agree.

### 3. Limited B0 Einstein–Cartan non-repair

For the declared Weyssenhoff/Frenkel mean field, Cartan torsion is algebraic. Under zero mean
boundary spin, A_B, no surface-spin action, and no distributional contorsion, mean boundary
torsion vanishes and ordinary Israel matching returns. Bulk spin-squared stress can remain.
No result is claimed for polarized B1/B2 or finite-thickness theories.

### 4. Conditional S1 route

The local impulse-free S1 data require equality of \(A,B,H_A,H_B\) and
\(\rho_{\rm eff}=0\). The family is nonempty under the accepted assumptions and has no hidden
surface functions. It is compatible initial data, not continuous transport or a global
junction.

### 5. Volume and areal turning are distinct

The N2 baseline, tight repeat, and all 54 perturbation runs reproduce. At \(t=M\), the
baseline has \(\Theta>0\) and \(H_B<0\): volume expands while areal radius contracts. The
3/27 coarse turns do not establish an open bounce region.

### 6. Scoped thermal exclusion

TEST 022 reproduces

\[
T_c=0.8133906806414589T_{\rm Pl},
\quad
\rho_c=15.372451912542129\rho_{\rm Pl},
\quad
M(x=2)=0.08811891192485782\ell_{\rm Pl}.
\]

The standard thermal SM-like sharp Weyssenhoff realization remains outside TEST 008's
conservative controlled regime. Successor matter models remain open.

## Correction made during TEST 022

The first coordinate-form implementation of (K^\theta{}_{\theta,C1}\) retained an extra
factor (A^{-1}\). The independent orthonormal derivation caught it before gate evaluation.
It was corrected and is recorded in `results/FAILURE_REGISTER.md`.

## Scoped failures and unresolved work

- Ordinary exterior C0/C1 matching requires exotic surface density under the tested
  embeddings.
- The baseline N2 solution is not an areal bounce.
- The standard thermal SM-like sharp Weyssenhoff realization fails its declared physical
  control.
- Polarized torsion boundaries, smooth layers, global S1 extension, successor microphysics,
  transport, CMB production, and halo projection are unresolved or belong to other tests.

## Prohibited claims

Do not claim a universal moving-shell no-go theorem, failure of all Einstein–Cartan
junctions, a bounce, nonsingularity, a global child universe, mass transfer, time reversal,
time compression, halo projection, CMB production, or empirical validation.

## Paper-eligibility decision

The preferred six-result technical paper is **eligible for novelty review and scoped
drafting**. JEC-A is not publication acceptance. The paper must retain the claim matrix and
must not broaden beyond the tested action, embeddings, domains, and physical calibration.

## Reproduction

From `junction-ec-paper-audit/` run:

```sh
./verify.sh
```

The command regenerates every output and runs 20 checks. The accepted run returned JEC-A and
JEC0–JEC8 pass.

> Derivational paper closure is not evidence for a bounce, nonsingular child universe,
> parent–child transition, mass transfer, time reversal, or empirical validity.
