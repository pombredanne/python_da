from setuptools import setup, Extension

module = Extension('python_da', ['ext/python_da.cpp'], include_dirs=["libda/include"])

setup(name='python_da',
      version='1.0',
      ext_modules=[module],
     )
