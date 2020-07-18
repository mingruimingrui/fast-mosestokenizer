#!/bin/sh
set -e

# Set up environment and work directory
export CC=clang
export CXX=clang++
export DEBIAN_FRONTEND=noninteractive

cd /opt/fast-mosestokenizer

# Download dependencies
apt update
apt upgrade -y
apt install -y clang make cmake git curl pkg-config

# Download and init conda
MINICONDA_FILENAME=Miniconda3-latest-Linux-x86_64.sh
curl -L -o $MINICONDA_FILENAME \
    "https://repo.continuum.io/miniconda/$MINICONDA_FILENAME"
bash ${MINICONDA_FILENAME} -b -f -p $HOME/miniconda3
export PATH=$HOME/miniconda3/bin:$PATH
eval "$(conda shell.bash hook)"

# Build dependencies as static libraries
conda create -n meson -y python=3.8
conda activate meson
conda install -y meson
make download-build-static-deps
conda deactivate

# Build and upload packages
for VERSION in 3.6 3.7 3.8; do
    conda create -n py$VERSION -y python=$VERSION
    conda activate py$VERSION
    python setup.py build_ext bdist_wheel \
        --plat-name manylinux1_x86_64
    conda deactivate
done

# Upload to PyPI
conda activate py3.8
python -m pip install setuptools wheel twine
python -m twine upload dist/*
