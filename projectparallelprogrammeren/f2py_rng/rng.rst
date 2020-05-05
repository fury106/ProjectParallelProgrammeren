This file documents a python module built from Fortran code with f2py.
You should document the Python interfaces, *NOT* the Fortran interfaces.

Module projectparallelprogrammeren.rng
*********************************************************************

Module :py:mod:`rng` built from fortran code in :file:`f2py_rng/rng.f90`.

.. function:: lcg1()
   :module: projectparallelprogrammeren.rng
   
   Deze functie retourneert een willekeurig getal.

   :param x: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param y: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param z: 1D Numpy array with ``dtype=numpy.float64`` (output)
   
.. function:: coordinaten(hoeveel)
   :module: projectparallelprogrammeren.rng
   
   Deze functie genereert de coordinaten van de atomen van een run, gebruikmakend van de functie lcg1().
   
   :param hoeveel: het aantal atomen waarvoor coordinaten berekend moeten worden. (input)
   :param coordinaten: Een lijst met de coordinaten van alle atomen ([x1,...],[y],[z]) (output)
