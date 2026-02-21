#!/usr/bin/env bash
set -euo pipefail

HOST=${HOST:-http://localhost:8080}
REPORT_DIR=${REPORT_DIR:-docs/results}
STAMP=$(date +%Y%m%d-%H%M%S)
mkdir -p "$REPORT_DIR"

run_case() {
  name=$1
  users=$2
  spawn=$3
  runtime=$4
  echo "[experiment] $name"
  USERS=$users SPAWN=$spawn RUNTIME=$runtime HOST=$HOST ./scripts/run_load_test.sh | tee "$REPORT_DIR/$STAMP-$name.log"
}

run_case scalability-100-500 500 50 15m
run_case write-heavy 800 80 10m
run_case mixed-latency 400 40 12m
