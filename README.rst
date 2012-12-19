[This document is a copy of the original.  `The latest version is
available on Tijmen Tieleman's
homepage. <http://www.cs.toronto.edu/~tijmen/gnumpy.html>`_]

Gnumpy is free software, but if you use it in scientific work that
gets published, you should cite `this tech report
<http://www.cs.toronto.edu/~tijmen/gnumpyTr.pdf>`_ in your
publication.

Documentation: `here
<http://www.cs.toronto.edu/~tijmen/gnumpyDoc.html>`_.

Do you want to have both the compute power of GPU's and the
programming convenience of Python numpy? Gnumpy + Cudamat will bring
you that.

Gnumpy is a simple Python module that interfaces in a way almost
identical to numpy, but does its computations on your computer's
GPU. See `this example
<http://www.cs.toronto.edu/~tijmen/gnumpy_example.py>`_, training an
RBM using Gnumpy.

Gnumpy runs on top of, and therefore requires, the excellent `cudamat
<http://code.google.com/p/cudamat/>`_ library, written by `Vlad Mnih
<http://www.cs.toronto.edu/~vmnih/>`_.

Gnumpy can run in simulation mode: everything happens on the CPU, but
the interface is the same. This can be helpful if you like to write
your programs on your GPU-less laptop before running them on a
GPU-equipped machine. It also allows you to easily test what
performance gain you get from using a GPU. The simulation mode
requires `npmat <http://www.cs.toronto.edu/~ilya/npmat.py>`_, written
by `Ilya Sutskever <http://www.cs.toronto.edu/~ilya>`_.  [npmat is
included in this distribution.]

Gnumpy is licensed with a BSD-style license (i.e. it's completely free
to use for everyone, also as a component in commercial software), with
one added note: if you use it for scientific work that gets published,
you must include reference to the Gnumpy tech report in your
publication. For details of the license, see the top of gnumpy.py.

Recent changes:

- 2012-07-25: Bugfix. gnumpy.dot(x, x), when x is a 1-dimensional array, didn't work but now works.
- 2011-06-06: gnumpy.dot() now takes arrays of ndim>2.
- 2011-04-19: Bugfix: several bugs involving zero size arrays were fixed.
- 2011-04-15: Bugfix. "x=gnumpy.zeros(10); x[array([])] = garray([])" didn't work as it should. Now it does.
- 2011-03-24: Added gnumpy.outer().
- 2011-03-15: The ability to check for infs and nans automatically has been added to Gnumpy.
- 2010-07-19: Cudamat now enables fast indexing with arrays of indices. Download the newest Cudamat to have fast indexing with arrays in Gnumpy.
- 2010-07-08: Renamed the project to Gnumpy. It used to be called Gpunnumpy.
