cmake_minimum_required(VERSION 3.1)

file(STRINGS "VERSION" MOSESTOKENIZER_VERSION)
project(mosestokenizer VERSION ${SPM_VERSION} LANGUAGES CXX)

######## Options
option(BUILD_SHARED_LIBS "Build mosestokenizer as shared library" ON)
option(BUILD_CLI "Build mosestokenizer commandline tool" ON)
option(BUILD_PYTHON "Build mosestokneizer python library" OFF)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

######## Compiler flags
add_definitions(
    -DVERSION_INFO="${MOSESTOKENIZER_VERSION}"
)

if (NOT BUILD_SHARED_LIBS)
    add_definitions(-static -fPIC)
    SET(CMAKE_FIND_LIBRARY_SUFFIXES ".a")
    SET(CMAKE_EXE_LINKER_FLAGS "-static")
endif (NOT BUILD_SHARED_LIBS)

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
find_package(PkgConfig REQUIRED)

if(NOT BUILD_SHARED_LIBS)
    set(Boost_USE_STATIC_LIBS ON)
endif(NOT BUILD_SHARED_LIBS)
find_package(Boost COMPONENTS program_options thread REQUIRED)
include_directories(${Boost_INCLUDE_DIRS})

pkg_search_module(GLIB REQUIRED glib-2.0)
include_directories(${GLIB_INCLUDE_DIRS})
link_directories(${GLIB_LIBRARY_DIRS})
add_definitions(${GLIB_CFLAGS_OTHER})

pkg_search_module(RE2 REQUIRED re2)
include_directories(${RE2_INCLUDE_DIRS})
link_directories(${RE2_LIBRARY_DIRS})
add_definitions(${RE2_CFLAGS_OTHER})


######## Linking
include_directories(${CMAKE_SOURCE_DIR}/include)

add_library(
    mosestokenizer-dev
    src/tokenizer.cpp
    src/Parameters.cpp
)
set_target_properties(mosestokenizer-dev PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_link_libraries(mosestokenizer-dev PRIVATE
    ${Boost_LIBRARIES}
    ${GLIB_LIBRARIES}
    ${RE2_LIBRARIES}
)

# TODO: Figure out how to link dependencies only to libmosestokenizer
if (BUILD_CLI)
add_executable(
    mosestokenizer
    src/tools/tokenizer_main.cpp
)
set_target_properties(mosestokenizer PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_link_libraries(mosestokenizer PRIVATE mosestokenizer-dev)
target_link_libraries(mosestokenizer PRIVATE
    ${Boost_LIBRARIES}
    ${GLIB_LIBRARIES}
    ${RE2_LIBRARIES}
)
endif (BUILD_CLI)

if (BUILD_PYTHON)
add_subdirectory(deps/pybind11-2.5.0)
pybind11_add_module(_mosestokenizer src/python/mosestokenizer.cpp)
set_target_properties(_mosestokenizer PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_link_libraries(_mosestokenizer PRIVATE mosestokenizer-dev)
endif (BUILD_PYTHON)
