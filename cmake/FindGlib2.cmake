#[=======================================================================[.rst:
FindGlib2
--------

Find the glib-2.0 headers and libraries from the deps folder.

General variables::

  Glib2_FOUND - true if the libglib-2.0 headers and libraries were found
  Glib2_INCLUDE_DIRS - the directory containing the libglib-2.0 headers
  Glib2_LIBRARIES - libglib-2.0 libraries to be linked

The following variables may also be set to alter behavior::

  BUILD_SHARED_LIBS - used to determine which of static or shared library
    should be sourced

.. note::
  This script is pretty hard coded.
#]=======================================================================]

if (BUILD_SHARED_LIBS)

# Search for shared library on system level
find_package(PkgConfig REQUIRED)
pkg_search_module(Glib2 REQUIRED glib-2.0)

else()  # BUILD_SHARED_LIBS

# Search for static library from deps
set(
  Glib2_INCLUDE_DIRS
  ${CMAKE_SOURCE_DIR}/deps/glib-2.63.6
  ${CMAKE_SOURCE_DIR}/deps/glib-2.63.6/glib
  ${CMAKE_SOURCE_DIR}/deps/glib-2.63.6/build/glib
)
set(Glib2_LIBRARIES ${CMAKE_SOURCE_DIR}/deps/glib-2.63.6/build/glib/libglib-2.0.a)
add_library(glib-2.0::glib-2.0 STATIC IMPORTED)
set(Glib2_FOUND ON)

endif()  # BUILD_SHARED_LIBS
