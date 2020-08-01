cmake_minimum_required(VERSION 3.2)

file(STRINGS "VERSION" MOSESTOKENIZER_VERSION)
project(mosestokenizer VERSION ${MOSESTOKENIZER_VERSION} LANGUAGES CXX)
add_definitions(-DVERSION_INFO="${MOSESTOKENIZER_VERSION}")
add_definitions(-DTOKENIZER_NAMESPACE=mosestokenizer)


######## Options
option(BUILD_SHARED_LIBS "Build mosestokenizer as shared library" ON)
option(BUILD_CLI "Build mosestokenizer commandline tool" ON)
option(BUILD_PYTHON "Build mosestokneizer python library" OFF)


######## CMake settings
if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  set(CMAKE_MACOSX_RPATH 1)
  find_library(COREFOUNDATION_LIBRARY CoreFoundation)
  find_library(FOUNDATION_LIBRARY Foundation)
  set(
    DEP_LIBRARIES ${DEP_LIBRARIES}
    ${COREFOUNDATION_LIBRARY} ${FOUNDATION_LIBRARY}
  )
endif()
set(CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if (NOT BUILD_SHARED_LIBS)
  set(CMAKE_FIND_LIBRARY_SUFFIXES ".a")
  set(CMAKE_EXE_LINKER_FLAGS "-static")
  set(CMAKE_POSITION_INDEPENDENT_CODE ON)
else()
  if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(CMAKE_FIND_LIBRARY_SUFFIXES ".dylib")
  else()
    set(CMAKE_FIND_LIBRARY_SUFFIXES ".so")
  endif()
endif ()

set(
  CMAKE_MODULE_PATH
  ${CMAKE_MODULE_PATH}
  ${CMAKE_SOURCE_DIR}/cmake
  ${CMAKE_SOURCE_DIR}/cmake
)


######## Compiler flags
if ("${CMAKE_CXX_COMPILER_ID}" MATCHES "Clang")
  add_definitions(-std=c++11 -Wall)
  if (CMAKE_BUILD_TYPE MATCHES Debug)
    add_definitions(-O0 -g3)
  endif ()
elseif ("${CMAKE_CXX_COMPILER_ID}" MATCHES "GNU")
  add_definitions(-std=c++0x -Wall)
  if (CMAKE_BUILD_TYPE MATCHES Debug)
    add_definitions(-O0 -g3)
  endif ()
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
  add_definitions(/W4 /D "_CRT_SECURE_NO_WARNINGS")
endif()


######## Dependencies
# Boost
if (BUILD_SHARED_LIBS)

find_package(Boost COMPONENTS program_options thread REQUIRED)
include_directories(${Boost_INCLUDE_DIRS})
set(DEP_LIBRARIES ${DEP_LIBRARIES} ${Boost_LIBRARIES})

else()

include_directories(${CMAKE_SOURCE_DIR}/deps/boost_1_73_0)
set(
  DEP_LIBRARIES
  ${DEP_LIBRARIES}
  ${CMAKE_SOURCE_DIR}/deps/boost_1_73_0/stage/lib/libboost_thread.a
  ${CMAKE_SOURCE_DIR}/deps/boost_1_73_0/stage/lib/libboost_program_options.a
)

endif()

# Intl
find_package(Intl REQUIRED)
include_directories(${Intl_INCLUDE_DIRS})
set(DEP_LIBRARIES ${DEP_LIBRARIES} ${Intl_LIBRARIES})

find_package(Glib2 REQUIRED)
include_directories(${Glib2_INCLUDE_DIRS})
link_directories(${Glib2_LIBRARY_DIRS})
set(DEP_LIBRARIES ${DEP_LIBRARIES} ${Glib2_LIBRARIES})

find_package(RE2 REQUIRED)
include_directories(${RE2_INCLUDE_DIRS})
link_directories(${RE2_LIBRARY_DIRS})
set(DEP_LIBRARIES ${DEP_LIBRARIES} ${RE2_LIBRARIES})

include_directories(${CMAKE_SOURCE_DIR}/include)
add_definitions(-std=c++11 -pthread)


######## Targets
add_library(mosestokenizer-dev src/Tokenizer.cpp src/Parameters.cpp)
target_link_libraries(mosestokenizer-dev PRIVATE ${DEP_LIBRARIES})

configure_file(
  mosestokenizer.pc.in
  mosestokenizer.pc
  @ONLY
)

install(
  FILES ${CMAKE_BINARY_DIR}/mosestokenizer.pc
  DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/pkgconfig
)

install(
  DIRECTORY ${CMAKE_SOURCE_DIR}/share/nonbreaking_prefixes
  DESTINATION ${CMAKE_INSTALL_PREFIX}/share/mosestokenizer
)

install(
  TARGETS mosestokenizer-dev
  LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
  ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
)


######## CLI
if (BUILD_CLI)

add_executable(mosestokenizer src/tools/tokenizer_main.cpp)
target_link_libraries(
  mosestokenizer PRIVATE
  mosestokenizer-dev
  ${DEP_LIBRARIES}
)

install(
  TARGETS mosestokenizer
  RUNTIME DESTINATION bin
)

endif()


######## Python
if (BUILD_PYTHON)

add_subdirectory(deps/pybind11-2.5.0)
pybind11_add_module(_mosestokenizer src/python/mosestokenizer.cpp)
target_link_libraries(
  _mosestokenizer PRIVATE
  mosestokenizer-dev
  ${DEP_LIBRARIES}
)

endif()


######## Installation
