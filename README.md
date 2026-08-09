# TEST 022 — Junction–Einstein–Cartan Paper Audit

This package executes the bounded analytic and reproduction test defined by
`Arbiter/tests/TEST_022_JUNCTION_EC_PAPER_DERIVATIONAL_CLOSURE.md`.

Run:

```sh
./verify.sh
```

By default the entry point uses `.venv/bin/python`. A parent paper repository may instead provide
an existing compatible interpreter explicitly:

```sh
JUNCTION_AUDIT_PYTHON=/path/to/python ./verify.sh
```

The package treats `parent-child-phase0/`, `parent-child-j0/`, `parent-child-j1/`, and the
five `parent-child-s1*` packages as read-only provenance inputs. It does not alter their
outputs.

The central new calculation is the complete C1 timelike shell, including temporal and
angular extrinsic curvature, the full Israel tensor, moving-fluid flux, conservation,
turning-point limits, and an ingoing Eddington–Finkelstein comparison.

## Repository identity

- **Result:** `JEC-A` — six scoped junction/Einstein–Cartan derivations close
  through JEC8 with 20 checks, making the bounded technical paper eligible for
  novelty review and drafting.
- **Scope:** The result does not establish a bounce, nonsingular child universe,
  transfer mechanism, or universal junction no-go theorem.
- **Contents:** Frozen conventions, nine derivation ledgers, analytic and
  numerical reproductions, claim matrix, tests, citations, and Arbiter packet.
