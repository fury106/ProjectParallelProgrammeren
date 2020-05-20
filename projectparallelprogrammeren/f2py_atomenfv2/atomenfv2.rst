This file documents a python module built from Fortran code with f2py.
You should document the Python interfaces, *NOT* the Fortran interfaces.

Module projectparallelprogrammeren.atomenfv2
*********************************************************************

Module :py:mod:`atomenfv2` built from fortran code in :file:`f2py_atomenfv2/atomenfv2.f90`.

Deze extensie is gelijkaardig met de extensie atomenf, maar hier is de berekening van de LJ potentiaal geoptimaliseerd.

.. function:: ljpot2atomen(afstand)
   :module: projectparallelprogrammeren.atomenf
   
   Deze functie berekent de Lennard Jones Potentiaal tussen twee atomen.

   :param afstand: De afstand tussen de twee atomen. (input)
   :param ljpot2atomen: De Lennard Jones potentiaal van twee atomen die op deze afstand van elkaar liggen. (output)
   
.. function:: ljpotalleatomen(lijstCoordinaten,aantal)
   :module: projectparallelprogrammeren.atomenf
   
   Deze functie berekent de Lennard Jones potentialen van alle atomen.
   
   :param lijstCoordinaten: De lijst met de coordinaten van alle atomen. (input)
   :param aantal: Het aantal atomen in de simulatie. (input)
   :param ljpotalleatomen: De som van alle Lennard Jones potentialen. (output)

