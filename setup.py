from setuptools import setup, find_packages
from setuptools.extension import Extension
import subprocess
import sys

def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
  from Cython.Build import cythonize
except:
  install('cython')
  from Cython.Build import cythonize

extensions = [
  Extension(
    "alc.*",
    ["alc/*.py"],
  ),
]

setup(
  name = 'alc',
  version = '0.1.0',
  license='GPL-3.0',
  description = 'Code developed for the COC473 (Computational Linear Algebra) course @ UFRJ',
  packages=find_packages(),
  author = 'Gabriel Gazola Milan',
  author_email = 'gabriel.gazola@poli.ufrj.br',
  url = 'https://github.com/gabriel-milan/linear-algebra',
  install_requires=[
    'Cython>=0.29.17',
    'sympy==1.6.2',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  # ext_modules = cythonize(extensions, language_level = "3")
)
