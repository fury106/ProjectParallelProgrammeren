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
	potkwadraat = 0 #nodig voor berekening stdev
	
	for i in range(1+rank*perrank, 1+(rank+1)*perrank):	#de lus itereren
		run = atomen.Atomen(n)	#nieuwe lijst atomen genereren
		pot = f901.ljpotalleatomen(run.getCoordinaten(), n)	#berekeningen uitvoeren
		
		totalePot = totalePot + pot
		potentialenlijst.append(pot)
		potkwadraat = potkwadraat + pot * pot
		if pot < laagsteE:
			coordinatenLaagsteE = run.getCoordinaten()
			nummerRunLaagsteE = i
			laagsteE = pot
			
	comm.Barrier()
	
	#vanaf nu zoeken naar de optimale configuratie:
	#resultaten bundelen
	optimaleCoordinaten = comm.gather(coordinatenLaagsteE, root = 0)
	laagsteE = comm.gather(laagsteE, root = 0)
	totalePot = comm.gather(totalePot, root = 0)
	potentialen = comm.gather(potentialenlijst, root = 0)
	potkwadraat = comm.gather(potkwadraat, root = 0)
	stopwatch.stop()
	
	if rank == 0:
		laagsteEnergie = min(laagsteE)
		
		print(" ")
		print("----------RESULTATEN----------")
		print("v3: parallellisatie:", stopwatch)
		#print(laagsteE)
		#print(potentialen)
		print("De laagste energie bedraagt:", laagsteEnergie)
		gemiddelde = sum(totalePot) / (size * (m // size))
		print("De gemiddelde energie bedraagt:", gemiddelde)
		standaardafwijking = np.sqrt(sum(potkwadraat) / (size * (m // size) - 1) - (gemiddelde * gemiddelde))
		print("De standaardafwijking bedraagt:", standaardafwijking)
		print(size)
	

#test code		
if __name__ == "__main__":
	test = simulatie(100,50)
		
#eof
