#!/bin/sh
# ---
# help-text: Build the docker images
# ---
set -eu

docker build \
    --tag "dna/axs-audit:$VG_DOCKER_UID" \
    --build-arg "UID=$VG_DOCKER_UID" \
    --build-arg "GID=$(id -g)" \
    --file "$VG_APP_DIR/Dockerfile" \
    "$VG_APP_DIR"
