.PHONY = help build clean

help:
	@echo "Subcommands"
	@echo "==========="
	@echo "- build"
	@echo "	Build the mosestokenizer c library"
	@echo "- clean"
	@echo "	Remove all build files"
	@echo "- download-pybind11"
	@echo "	Download and decompress pybind11"
	@echo "- apt-install-deps"
	@echo "	Use APT to install dependencies (for convenience during CI/CD)"
	@echo "- brew-install-deps"
	@echo "	Use Homebrew to install dependencies (for convenience during CI/CD)"

build-cli:
	mkdir -p build/rel
	( \
		cd build/rel; \
		cmake ../.. \
			-DCMAKE_BUILD_TYPE=Release \
			-DBUILD_SHARED_LIBS:BOOL=ON \
			-DBUILD_CLI:BOOL=ON; \
		cmake --build . --config Release; \
	)

install:
	@echo "Not yet implemented"
	exit 1

clean:
	pip uninstall -y fast-mosestokenizer
	rm -rf build bindings/python/mosestokenizer/lib

download-pybind11:
	mkdir -p deps
	curl -L -o deps/pybind-v2.5.0.tar.gz \
		https://github.com/pybind/pybind11/archive/v2.5.0.tar.gz
	tar -C deps -xvf deps/pybind-v2.5.0.tar.gz

apt-install-deps:
	apt update
	DEBIAN_FRONTEND=noninteractive apt install -y \
		libboost-thread-dev \
		libboost-program-options-dev \
		libglib2.0-dev \
		libre2-dev

brew-install-deps:
	brew install pkg-config boost glib re2
