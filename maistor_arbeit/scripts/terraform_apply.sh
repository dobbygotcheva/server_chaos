#!/usr/bin/env bash
set -euo pipefail

WORKDIR=${WORKDIR:-infra/terraform}
ACTION=${ACTION:-apply}

pushd "$WORKDIR" >/dev/null
terraform init
terraform "$ACTION" -auto-approve
popd >/dev/null
