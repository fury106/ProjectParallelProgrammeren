"""
Dit is dezelfde code montecarlo_v3, maar door problemen met de vindbaarheid van de modules op de cluster, werd deze code naar dit bestand gekopieerd, zodat het wel werkt.

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
	optimaleCoordinaten = comm.gather(coordinatenLaagsteE, root = 0)
	laagsteE = comm.gather(laagsteE, root = 0)
	totalePot = comm.gather(totalePot, root = 0)
	potentialen = comm.gather(potentialenlijst, root = 0)
	potkwadraat = comm.gather(potkwadraat, root = 0)
	stopwatch.stop()
	
	if rank == 0:
		#dictionary = {laagsteE[i]: optimaleCoordinaten[i] for i in range(len(laagsteE))}
		#laagsteEnergie = str(min(dictionary))
		#laagsteEnergie = str(dictionary)
		#optimaleCoordinaten = dictionary[laagsteEnergie]
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
		


if __name__ == "__main__":
	"""
	Dit script runt de code parallel.
	"""
	print("100 atomen, 100 simulaties")
	simulatie(100, 100)

	print("500 atomen, 100 simulaties")
	simulatie(500, 100)

	print("1000 atomen, 100 simulaties")
	simulatie(1000, 100)

	print("2000 atomen, 100 simulaties")
	simulatie(2000, 100)

	print("5000 atomen, 100 simulaties")
	simulatie(5000, 100)

	print("10000 atomen, 100 simulaties")
	simulatie(10000, 100)

	print("50000 atomen, 100 simulaties")
	simulatie(50000, 100)

	print("100000 atomen, 100 simulaties")
	simulatie(100000, 100)






	print("100 atomen, 30 simulaties")
	simulatie(100, 30)

	print("100 atomen, 50 simulaties")
	simulatie(100, 50)

	print("100 atomen, 100 simulaties")
	simulatie(100, 100)

	print("100 atomen, 250 simulaties")
	simulatie(100, 250)

	print("100 atomen, 500 simulaties")
	simulatie(100, 500)

	print("100 atomen, 1000 simulaties")
	simulatie(100, 1000)

	print("100 atomen, 10000 simulaties")
	simulatie(100, 10000)

#eof

