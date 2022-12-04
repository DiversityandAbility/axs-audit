#!/bin/sh
# ---
# image:
#   tag: dna/axs-audit:$VG_DOCKER_UID
#   ipc: host
#   security-opt: seccomp=seccomp_profile.json
#   volume:
#     - $VG_APP_DIR:/workdir
#     - $VG_APP_DIR/results:/results
# help-text: Run a command inside an AXS Audit docker container
# ---
"${@:-bash}"
