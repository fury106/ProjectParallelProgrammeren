# -*- coding: utf-8 -*-

"""
Module projectparallelprogrammeren.montecarlo_v0 
=================================================================

simulatie v0: alles in Python (op genereren van de getallen na)

"""
import math
import numpy as np
from statistics import stdev
import projectparallelprogrammeren
from projectparallelprogrammeren import montecarlo_v1
from projectparallelprogrammeren import montecarlo_v2
from projectparallelprogrammeren import montecarlo_v3
from projectparallelprogrammeren import atomen
from et_stopwatch import Stopwatch


def simulatie(n=20, m=10):
	"""
	Deze functie doet een simulatie van een gegeven hoeveelheid conformaties van het gegeven aantal atomen.
	
	:param int n: Het aantal atomen dat gebruikt wordt.
	:param int m: Het aantal conformaties dat gesimuleerd moet worden.
	"""
	with Stopwatch(message="v0: Python"):
		coordinatenLaagsteE = 0
		nummerRunLaagsteE = 0
		LaagsteE = math.inf
		totalePot = 0
		gemiddelde = 0
		potentialenlijst = list()
		for i in range(m):
			#print("Bezig met het simuleren van run", i+1, "van", m)
			run = atomen.Atomen(n)
			pot = run.berekenLJPot()
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
	print("De standaardafwijking is:", stdev(potentialenlijst))
	
	"""montecarlo_v1.simulatie(n, m)
	montecarlo_v2.simulatie(n, m)
	montecarlo_v3.simulatie(n, m)"""
	
#eof
