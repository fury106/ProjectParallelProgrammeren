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
			integer*8, optional :: s
			integer :: values(8)
			real	:: rTime
			!seed instellen (vergelijkbaar met time_ns() van python, maar nu is seed de tijd van de dag in ms.)
			if (present(s)) then
				seed = s
				x = s
			else 
				call date_and_time(values=values)
				rTime = (values(5))*60.
				rTime = (rTime + values(6))*60.
				rTime = (rTime + values(7))*1e3
				rTime = rTime + values(8) - x
				seed = rTime !orgineel seed = s
				x = rTime !s
			end if
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
		
 		
 		function coordinaten(hoeveel)
			! Deze functie berekent het volgende willekeurig getal
			implicit none
			integer*8, dimension(3, hoeveel)	:: coordinaten ! result type
			integer*8, intent(in)				:: hoeveel
			integer*4							:: teller, teller1
			
			call set_seed()
			do teller = 1, hoeveel
				do teller1 = 1, 3
					coordinaten(teller1, teller) = lcg1()/500000 !delen door 500000 om getal kleiner te maken, omdat anders atomen veel te ver van elkaar verwijderd zijn.
				end do
			end do
			!f2py depend (hoeveel) , coordinaten
		end function coordinaten
 		
end module my_f90_module
