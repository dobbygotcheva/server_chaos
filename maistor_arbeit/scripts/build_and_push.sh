#!/usr/bin/env bash
set -euo pipefail

REGISTRY=${REGISTRY:-ghcr.io/example}
IMAGE_NAME=${IMAGE_NAME:-cloud-native-api}
TAG=${TAG:-$(git rev-parse --short HEAD)}

full_image="$REGISTRY/$IMAGE_NAME:$TAG"

echo "[build] Building $full_image"
docker build -t "$full_image" -f Dockerfile.api .

echo "[push] Pushing $full_image"
docker push "$full_image"

echo "Image available at $full_image"
