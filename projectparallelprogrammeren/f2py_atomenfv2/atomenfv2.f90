!-------------------------------------------------------------------------------------------------
! Fortran source code for module projectparallelprogrammeren.atomenfv2
!-------------------------------------------------------------------------------------------------
! Remarks:
!   . Enter Python documentation for this module in ``./atomenfv2.rst``.
!     You might want to check the f2py output for the interfaces of the C-wrapper functions.
!     It will be autmatically included in the projectparallelprogrammeren documentation.
!   . Documument the Fortran routines in this file. This documentation will not be included
!     in the projectparallelprogrammeren documentation (because there is no recent sphinx
!     extension for modern fortran.

module f90_module2
	implicit none
	contains
		function ljpot2atomen(afstand)
			!Deze functie berekent de Lennard Jones Potentiaal tussen twee atomen
			implicit none
			!variabelen definieren:
			real*8		:: afstand
			real*8		:: ljpot2atomen
			real*8		:: rr, rr6
			!LJ potentiaal berekenen
			if (afstand .EQ. 0) then !Als afstand = 0, ongeldige invoer
				!write(*,*) 'afstand =', afstand
				ljpot2atomen = HUGE(ljpot2atomen) !als afstand = 0, potentiaal = grootst mogelijke getal
			else
				rr = 1/afstand
				rr = rr * rr
				rr6 = rr * rr * rr
				ljpot2atomen = 4*(rr6 * (rr6 - 1))
			end if
		end function ljpot2atomen
		
		function ljpotalleatomen(lijstCoordinaten,aantal)
			!Deze functie loopt over de lijst van alle atomen en berekent alle LJ potentialen.
			implicit none
		
			!variabelen definieren:
			real*8, dimension(3, aantal)	:: lijstCoordinaten	!de lijst met alle coordinaten
			integer*4						:: aantal			!het aantal atomen
			integer*4						:: atoom1, atoom2	!nummer van atoom 1 en 2
			real*8							:: x1, y1, z1		!coordinaten atoom 1
			real*8							:: x2, y2, z2		!coordinaten atoom 2
			real*8							:: r				!afstand tussen twee atomen
			real*8							:: ljpot			!lj pot tussen 2 atomen
			real*8							:: ljpotalleatomen	!totale lj pot van alle atomen
			ljpotalleatomen = 0
		
			!de eigenlijke berekening:
			!do atoom1 = 1, aantal
			do atoom1 = 1, (aantal - 1)
				x1 = lijstCoordinaten(1, atoom1)
				y1 = lijstCoordinaten(2, atoom1)
				z1 = lijstCoordinaten(3, atoom1)
				!do atoom2 = 1, aantal
				do atoom2 = (atoom1 + 1), aantal
					x2 = lijstCoordinaten(1, atoom2)
					y2 = lijstCoordinaten(2, atoom2)
					z2 = lijstCoordinaten(3, atoom2)
					
					if (atoom1 .NE. atoom2) then
						r = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
						ljpot = ljpot2atomen(r)
						ljpotalleatomen = ljpotalleatomen + ljpot
						!print*, atoom1, " - ", atoom2, ": ", ljpot
					end if
				end do
			end do
			!ljpotalleatomen = ljpotalleatomen / 2 !delen door 2 want alles wordt 2x berekend
			!print*, "Totale potentiaal = ", ljpotalleatomen
		end function ljpotalleatomen
	


	
end module f90_module2
