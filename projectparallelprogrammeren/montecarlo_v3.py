# -*- coding: utf-8 -*-

"""
Module projectparallelprogrammeren.montecarlo_v3 
=================================================================

Gelijkaardig aan v2, maar dan geparallelliseerd.

"""
import numpy as np
from statistics import stdev
import projectparallelprogrammeren
from projectparallelprogrammeren import atomen
#f90 = projectparallelprogrammeren.rng.my_f90_module
f901 = projectparallelprogrammeren.atomenfv2.f90_module2
from et_stopwatch import Stopwatch
from mpi4py import MPI


def simulatie(n=20, m=10):
	"""
	Deze functie doet een simulatie van een gegeven hoeveelheid conformaties van het gegeven aantal atomen. Dit is ook de eerste versie die parallel kan lopen over meerdere cores.
	
	:param int n: Het aantal atomen dat gebruikt wordt.
	:param int m: Het aantal conformaties dat gesimuleerd moet worden.
	"""
	stopwatch = Stopwatch()
	stopwatch.start()
		
	comm = MPI.COMM_WORLD
	size = comm.Get_size()	#aantal cores
	rank = comm.Get_rank()	#huidige core
	
	perrank = m // size	#het aanstal stappen per core (moet geheel getal zijn)
	comm.Barrier()
	
	coordinatenLaagsteE = 0
	nummerRunLaagsteE = 0
	laagsteE = float("inf")
	totalePot = 0
	gemiddelde = 0
	potentialenlijst = list()
	
	for i in range(1+rank*perrank, 1+(rank+1)*perrank):	#de lus itereren
		run = atomen.Atomen(n)	#nieuwe lijst atomen genereren
		pot = f901.ljpotalleatomen(run.getCoordinaten(), n)	#berekeningen uitvoeren
		
		totalePot = totalePot + pot
		potentialenlijst.append(pot)
		if pot < laagsteE:
			coordinatenLaagsteE = run.getCoordinaten()
			nummerRunLaagsteE = i
			laagsteE = pot
			
	comm.Barrier()
	
	#vanaf nu zoeken naar de optimale configuratie:
	optimaleCoordinaten = comm.gather(coordinatenLaagsteE, root = 0)
	laagsteE = comm.gather(str(laagsteE), root = 0)
	totalePot = comm.gather(totalePot, root = 0)
	potentialen = comm.gather(potentialenlijst, root = 0)
	
	stopwatch.stop()
	
	if rank == 0:
		#dictionary = {laagsteE[i]: optimaleCoordinaten[i] for i in range(len(laagsteE))}
		#laagsteEnergie = str(min(dictionary))
		#laagsteEnergie = str(dictionary)
		#optimaleCoordinaten = dictionary[laagsteEnergie]
		laagsteEnergie = str(min(laagsteE))
		
		print(" ")
		print("----------RESULTATEN----------")
		print("v3: parallellisatie:", stopwatch)
		print("De laagste energie bedraagt:", laagsteEnergie)
		gemiddelde = sum(totalePot) / m
		print("De gemiddelde energie bedraagt:", gemiddelde)
		print("De standaardafwijking bedraagt:", stdev(potentialen[0]))
		
		
		
			
		"""for i in range(m):
			#print("Bezig met het simuleren van run", i+1, "van", m)
			run = atomen.Atomen(n)
			pot = f901.ljpotalleatomen(run.getCoordinaten(), n)
			if pot >= 1.7976931348623157e+300:
				#als afstand = 0, geeft Fortran een heel hoog getal terug. Dit wordt beschouwd als oneindig.
				pot = float("inf")
			totalePot = totalePot + pot
			gemiddelde = totalePot / (i + 1)
			potentialenlijst.append(pot)
			if pot < LaagsteE:
				coordinatenLaagsteE = run.getCoordinaten()
				nummerRunLaagsteE = i
				LaagsteE = pot
		print(" ")
		print("----------RESULTATEN----------")
		print("Run", nummerRunLaagsteE + 1,"van", m, "had de laagste totale Lennard Jones Potentiaal, namelijk:", LaagsteE)
		#print("De Coordinaten van de atomen van deze run zijn:", coordinatenLaagsteE)
		print("De gemiddelde potentiaal:", gemiddelde)
		print("De standaardafwijking is:", stdev(potentialenlijst))"""
		
if __name__ == "__main__":
	test = simulatie(50,100)
		
#eof
