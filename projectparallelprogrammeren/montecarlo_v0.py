# -*- coding: utf-8 -*-

"""
Module projectparallelprogrammeren.montecarlo_v0 
=================================================================

simulatie v0

"""
import math
import numpy as np
from statistics import stdev
import projectparallelprogrammeren
from projectparallelprogrammeren import atomen
f90 = projectparallelprogrammeren.rng.my_f90_module
f901 = projectparallelprogrammeren.atomenf.f90_module
from et_stopwatch import Stopwatch


def simulatie(n=5, m=10):
	"""
	Deze functie doet een simulatie van een gegeven hoeveelheid conformaties van het gegeven aantal atomen.
	
	:param int n: Het aantal atomen dat gebruikt wordt. (default 5)
	:param int m: Het aantal conformaties dat gesimuleerd moet worden. (default 10)
	"""
	coordinatenLaagsteE = 0
	nummerRunLaagsteE = 0
	LaagsteE = math.inf
	totalePot = 0
	gemiddelde = 0
	potentialenlijst = list()
	for i in range(m):
		print("Bezig met het simuleren van run", i+1, "van", m)
		run = atomen.Atomen(n)
		pot = f901.ljpotalleatomen(run.getCoordinaten(), n)
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
