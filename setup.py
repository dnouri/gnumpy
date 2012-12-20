try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='gnumpy',
      version='0.2',
      description="Gnumpy is a simple Python module that interfaces in a way "
      "almost identical to numpy, but does its computations on your "
      "computer's  GPU, using Cudamat.",
      long_description=README,
      author='Tijmen Tieleman',
      license='BSD-derived (see LICENSE.txt)',
      url='http://www.cs.toronto.edu/~tijmen/gnumpy.html',
      py_modules=['gnumpy', 'npmat'],
      )
