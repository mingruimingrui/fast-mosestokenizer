.PHONY = help build clean

help:
	@echo "- build"
	@echo "	Build the mosestokenizer c library"
	@echo "- clean"
	@echo "	Remove all build files"
	@echo "- download-pybind11"
	@echo "	Download and decompress pybind11"
	@echo "- apt-install-deps"
	@echo "	Use APT to install dependencies (convenience during CI/CD)"

build:
	mkdir -p build/rel
	cmake . \
		--build ./build/rel \
		-DCMAKE_BUILD_TYPE=Release \
		-DBUILD_SHARED_LIBS:BOOL=ON \
		-DBUILD_CLI:BOOL=ON; \
	cmake --build ./build/rel --config Release
	# ( \
	# 	cd build; \
	# 	cmake . \
	# 		-DCMAKE_BUILD_TYPE=Release \
	# 		-DBUILD_SHARED_LIBS:BOOL=ON \
	# 		-DBUILD_CLI:BOOL=ON; \
	# 	make -j; \
	# )

clean:
	rm -rf build
	rm -rf *.so bindings/python/mosestokenizer/lib

download-pybind11:
	mkdir -p deps
	curl -L -o deps/pybind-v2.5.0.tar.gz \
		https://github.com/pybind/pybind11/archive/v2.5.0.tar.gz
	tar -C deps -xvf deps/pybind-v2.5.0.tar.gz

apt-install-deps:
	apt update
	apt install -y \
		g++ cmake \
		libboost-thread-dev \
		libboost-program-options-dev \
		libglib2.0-dev \
		libre2-dev
