import os
import platform
import re
import shutil
import subprocess
import sys
from distutils.version import LooseVersion
from glob import glob

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    """CMake python extension class.

    Adapted from https://github.com/pybind/cmake_example.
    """

    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    """CMake build_ext command class.

    Adapted from https://github.com/pybind/cmake_example.
    """

    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])

        except OSError:
            _msg = (
                "CMake must be installed to build the "
                "following extensions: {}"
            ).format(', '.join(e.name for e in self.extensions))
            raise RuntimeError(_msg)

        if platform.system() == "Windows":
            cmake_version = re.search(r'version\s*([\d.]+)', out.decode())
            cmake_version = cmake_version.group(1)
            cmake_version = LooseVersion(cmake_version)
            if cmake_version < '3.1.0':
                raise RuntimeError("CMake >= 3.1.0 is required on Windows")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.dirname(self.get_ext_fullpath(ext.name))
        extdir = os.path.abspath(extdir)
        # required for auto-detection of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        cfg = 'Debug' if self.debug else 'Release'

        cmake_args = [
            'cmake', ext.sourcedir,
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
            '-DPYTHON_EXECUTABLE=' + sys.executable,
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DBUILD_CLI:BOOL=OFF',
            '-DBUILD_PYTHON:BOOL=ON',
        ]
        build_args = [
            'cmake', '--build', '.',
            '--config', cfg
        ]

        if platform.system() == "Windows":
            cmake_args.append('-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(
                cfg.upper(), extdir))
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]

        env = os.environ.copy()
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp, exist_ok=True)
        subprocess.check_call(cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(build_args, cwd=self.build_temp)


TOKENIZER_DIR = os.path.join('bindings', 'python', 'mosestokenizer')
TOKENIZER_LIB_DIR = os.path.join(TOKENIZER_DIR, 'lib')


with open('VERSION', 'r') as f:
    VERSION_INFO = f.read().strip()


with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


# Copy dynamically linked libraries
os.makedirs(os.path.join(TOKENIZER_DIR, 'lib'), exist_ok=True)
for lib in [
    'glib-2.0',
    'stdc++',
    're2',
    'boost_atomic',
    'boost_system',
    'boost_date_time',
    'boost_chrono',
    'boost_thread',
    'boost_program_options',
]:
    if platform.system() == 'Darwin':
        libpaths = glob('/usr/local/lib/lib{}*.dylib'.format(lib))
        if lib == 'stdc++':
            libpaths = glob('/usr/lib/lib{}*.dylib'.format(lib))
    else:
        libpaths = glob('/usr/lib/x86_64-linux-gnu/lib{}.so*'.format(lib))

    for fp in libpaths:
        shutil.copy(fp, TOKENIZER_LIB_DIR)


setup(
    name='mosestokenizer',
    version=VERSION_INFO,
    author='Wang Ming Rui',
    author_email='mingruimingrui@hotmail.com',
    description='c++ mosestokenizer',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/mingruimingrui/fast-mosestokenizer',

    packages=['mosestokenizer', 'mosestokenizer.lib'],
    package_dir={'mosestokenizer': 'bindings/python/mosestokenizer'},
    package_data={'mosestokenizer': [
        'share/*/*',
        'lib/*.so*'
    ]},
    ext_modules=[CMakeExtension(
        'mosestokenizer.lib._mosestokenizer'
    )],

    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
)
