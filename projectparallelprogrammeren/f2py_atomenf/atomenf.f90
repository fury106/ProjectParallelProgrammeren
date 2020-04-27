!-------------------------------------------------------------------------------------------------
! Fortran source code for module projectparallelprogrammeren.atomenf
!-------------------------------------------------------------------------------------------------
! Remarks:
!   . Enter Python documentation for this module in ``./atomenf.rst``.
!     You might want to check the f2py output for the interfaces of the C-wrapper functions.
!     It will be autmatically included in the projectparallelprogrammeren documentation.
!   . Documument the Fortran routines in this file. This documentation will not be included
!     in the projectparallelprogrammeren documentation (because there is no recent sphinx
!     extension for modern fortran.

module f90_module
	implicit none
	contains
		function ljpot2atomen(afstand)
			!Deze functie berekent de Lennard Jones Potentiaal tussen twee atomen
			implicit none
			!variabelen definieren:
			real*8		:: afstand
			real*8		:: ljPot2Atomen
			!LJ potentiaal berekenen
			ljPot2Atomen = 4*((1/afstand)**12-(1/afstand)**6)
		end function ljpot2atomen


	
end module f90_module
