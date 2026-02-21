#!/usr/bin/env bash
set -euo pipefail

NAMESPACE=${NAMESPACE:-default}
OBS_NS=${OBS_NS:-observability}

helm upgrade --install api infra/helm/api -n "$NAMESPACE" --create-namespace
helm upgrade --install mongodb infra/helm/mongodb -n "$NAMESPACE"
helm upgrade --install monitoring infra/helm/monitoring -n "$OBS_NS" --create-namespace
