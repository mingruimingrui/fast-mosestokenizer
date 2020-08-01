.PHONY = help build install clean

help:
	@echo "Subcommands"
	@echo "==========="
	@echo "- build"
	@echo "	Build the mosestokenizer c library"
	@echo "- clean"
	@echo "	Remove all build files"
	@echo "- download-build-static-deps"
	@echo "	Download and build static dependencies"

build:
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
	cd build/rel && make install

clean:
	rm -rf build bindings/python/mosestokenizer/lib

download-build-static-deps:
	@mkdir -p deps

	@echo "Downloading pybind"
	curl -L -o deps/pybind-v2.5.0.tar.gz \
		https://github.com/pybind/pybind11/archive/v2.5.0.tar.gz
	tar -C deps -xf deps/pybind-v2.5.0.tar.gz

	@echo "Downloading and building re2"
	curl -L -o deps/re2-2020-06-01.tar.gz \
		https://github.com/google/re2/archive/2020-06-01.tar.gz
	tar -C deps -xf deps/re2-2020-06-01.tar.gz
	cd deps/re2-2020-06-01; CXXFLAGS="-fPIC" make

	@echo "Downloading and building glib2"
	curl -L -o deps/glib-2.63.6.tar.gz \
		https://github.com/GNOME/glib/archive/2.63.6.tar.gz
	tar -C deps -xf deps/glib-2.63.6.tar.gz
	( \
		cd deps/glib-2.63.6; \
		meson build --default-library static; \
		ninja -C build; \
	)

	@echo "Downloading and building boost"
	curl -L -o deps/boost_1_73_0.tar.gz \
		https://dl.bintray.com/boostorg/release/1.73.0/source/boost_1_73_0.tar.gz
	tar -C deps -xf deps/boost_1_73_0.tar.gz
	( \
		cd deps/boost_1_73_0; \
		./bootstrap.sh \
			--with-libraries=thread,program_options \
			--without-icu \
			--with-toolset=clang; \
		./b2 -j8 toolset=clang link=static cxxflags=-fPIC; \
	)
