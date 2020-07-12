# Install

This is a guide for compiling and building the package from source.

## Requirements

- `g++` or `clang`
- `cmake>=3.1`
- `pkg-config` (to source `glib-2.0` and `re2`)
- `Boost`
  - `program_options`
  - `thread`
- `glib-2.0`
- `re2` (Be warned that early versions do not contain `re2.pc`)

## Optional Requirements

- `make` (This way you can just use the handy `Makefile` provided)
- Python headers (For building python package)

## Installation (Library and command-line tool)

```sh
# Script to build the CLI is provided in the Makefile
make build-cli

# Installation comming soon
```

## Installation (Python)

### From PyPI (Recommended for users)

```sh
pip install fast-mosestokenizer
```

### From source

```sh
# Download and decompress pybind11
make download-pybind11

# Build and install python package
python setup.py build_ext install
```
