#!/usr/bin/env bash
set -euo pipefail

USERS=${USERS:-500}
SPAWN=${SPAWN:-50}
RUNTIME=${RUNTIME:-10m}
HOST=${HOST:-http://localhost:8080}

locust -f tests/load/locustfile.py --headless -u "$USERS" -r "$SPAWN" -t "$RUNTIME" -H "$HOST"
