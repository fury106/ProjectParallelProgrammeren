This file documents a python module built from Fortran code with f2py.
You should document the Python interfaces, *NOT* the Fortran interfaces.

Module projectparallelprogrammeren.atomenfv2
*********************************************************************

Module :py:mod:`atomenfv2` built from fortran code in :file:`f2py_atomenfv2/atomenfv2.f90`.

Deze extensie is gelijkaardig met de extensie atomenf, maar hier is de berekening van de LJ potentiaal geoptimaliseerd.

.. function:: add(x,y,z)
   :module: projectparallelprogrammeren.atomenfv2
   
   Compute the sum of *x* and *y* and store the result in *z* (overwrite).

   :param x: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param y: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param z: 1D Numpy array with ``dtype=numpy.float64`` (output)
