#!/bin/sh
set -e

# Set up environment and work directory
export CC=clang
export CXX=clang++
export DEBIAN_FRONTEND=noninteractive

cd /opt/fast-mosestokenizer
eval "$(conda shell.bash hook)"

# Download dependencies
apt update
apt upgrade -y
apt install -y clang make cmake meson git curl pkg-config

# Build dependencies as static libraries
make download-build-static-deps

# Build and upload packages
for VERSION in 3.6 3.7 3.8; do
    conda create -n py$VERSION -y python=$VERSION
    conda activate py$VERSION
    python setup.py build_ext bdist_wheel
    conda deactivate
done

# # Upload to PyPI
# conda activate py3.8
# python -m pip install setuptools wheel twine
# python -m twine upload dist/*
