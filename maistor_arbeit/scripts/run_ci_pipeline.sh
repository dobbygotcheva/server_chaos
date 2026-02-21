#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q

docker build -t cloud-native-api-ci -f Dockerfile.api .
