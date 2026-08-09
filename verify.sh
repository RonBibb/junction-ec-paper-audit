#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PY="${JUNCTION_AUDIT_PYTHON:-$ROOT/.venv/bin/python}"
cd "$ROOT"

if [ ! -x "$PY" ]; then
  echo "Python environment not found. Bootstrap .venv or set JUNCTION_AUDIT_PYTHON." >&2
  exit 2
fi

mkdir -p "$ROOT/logs" "$ROOT/outputs"

"$PY" "$ROOT/symbolic/shear_identity.py" > "$ROOT/logs/shear.log"
"$PY" "$ROOT/symbolic/c1_extrinsic.py" > "$ROOT/logs/c1.log"
"$PY" "$ROOT/symbolic/israel_residual.py" > "$ROOT/logs/israel.log"
"$PY" "$ROOT/symbolic/surface_conservation.py" > "$ROOT/logs/conservation.log"
"$PY" "$ROOT/symbolic/chart_transform.py" > "$ROOT/logs/chart.log"
"$PY" "$ROOT/symbolic/interior_sector.py" > "$ROOT/logs/interior_sector.log"
"$PY" "$ROOT/symbolic/cartan_b0.py" > "$ROOT/logs/cartan.log"
"$PY" "$ROOT/symbolic/s1_constraints.py" > "$ROOT/logs/s1.log"
"$PY" "$ROOT/numerical/event_reproduction.py" > "$ROOT/logs/events.log"
"$PY" "$ROOT/numerical/calibration_reproduction.py" > "$ROOT/logs/calibration.log"
"$PY" "$ROOT/symbolic/provenance_and_claims.py" > "$ROOT/logs/provenance.log"
"$PY" "$ROOT/symbolic/run_gates.py" > "$ROOT/logs/gates.log"
"$PY" -m unittest discover -s "$ROOT/tests" -p 'test_*.py' -v > "$ROOT/logs/tests.log" 2>&1

echo "TEST 022 verification complete"
"$PY" - <<'PY'
import json
from pathlib import Path
root = Path(__file__).resolve().parent if '__file__' in globals() else Path.cwd()
path = root / 'outputs' / 'gate_status.json'
if not path.exists():
    path = Path.cwd() / 'outputs' / 'gate_status.json'
data = json.loads(path.read_text())
print(data['outcome'])
for gate in data['gates']:
    print(gate['gate'], gate['status'])
PY
