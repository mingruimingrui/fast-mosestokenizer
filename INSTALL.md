# Install

This page contains a general guide on compiling and building the package
from source.

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

Coming soon.

## Installation (Python)

Pybind11 is used to create a python interface.
The `Makefile` contains a script to download and to decompress a release of
Pybind11.
Installation can be done using the `setup.py` script.

```sh
# Download and decompress pybind11
make download-pybind11

# Build and install python package
python setup.py build_ext install
```
