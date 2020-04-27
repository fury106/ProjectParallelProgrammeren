!-------------------------------------------------------------------------------------------------
! Fortran source code for module projectparallelprogrammeren.rng
!-------------------------------------------------------------------------------------------------
! Remarks:
!   . Enter Python documentation for this module in ``./rng.rst``.
!     You might want to check the f2py output for the interfaces of the C-wrapper functions.
!     It will be autmatically included in the projectparallelprogrammeren documentation.
!   . Documument the Fortran routines in this file. This documentation will not be included
!     in the projectparallelprogrammeren documentation (because there is no recent sphinx
!     extension for modern fortran.

module my_f90_module
	implicit none
	
	! definieren van de parameters en andere variabelen
	integer*8, parameter :: a=2147483629_8
	integer*8, parameter :: b=2147483629_8
	integer*8, parameter :: m=2_8**31-1
	integer*8			 :: seed = 0_8
	integer*8			 :: x	 = 0_8
	
	contains
		subroutine set_seed(s)
			integer*8, intent(in) :: s
			seed = s
			x = s
		end subroutine set_seed
		
		function lcg1()
			! Deze functie berekent het volgende willekeurig getal
			implicit none
			integer*8 :: lcg1 ! result type
			! nieuw getal berekenen:
			x = modulo(a*x+b, m)
			! nieuw getal toewijzen:
			lcg1 = x
		end function lcg1
end module my_f90_module
