#!/usr/bin/env bash

# Benchmark info
echo "TIMING - Starting main script at: $(date)"

# Set working directory to home directory
#cd "${HOME}"

#
# Start Jupyter Notebook Server
#

echo "Environment Setting"
. /etc/profile.d/00-modulepath.sh
. /etc/profile.d/rci.sh
. /etc/profile.d/modules.sh

# Purge the module environment to avoid conflicts
module purge

# Load the require modules
module load jupyterlab/.3.6.3-py3.11

# List loaded modules
module list

# List available kernels for debugging purposes
set -x
#jupyter kernelspec list
{ set +x; } 2>/dev/null
echo "TTT - $(date)"

# Benchmark info
echo "TIMING - Starting jupyter at: $(date)"

# Launch the Jupyter Notebook Server
set -x
export XDG_RUNTIME_DIR=""
jupyter lab --config="${CONFIG_FILE}" --notebook-dir=/home/${USER}

