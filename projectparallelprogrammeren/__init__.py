# -*- coding: utf-8 -*-
"""
Package projectparallelprogrammeren
=======================================

Een Monte Carlo simulatie van een aantal conformaties van een aantal atomen waarvan de Lennard Jones potentiaal berekend wordt.
"""
__version__ = "0.3.3"

try:
    import projectparallelprogrammeren.atomenfv2
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'atomenfv2')
    if not msg:
        import projectparallelprogrammeren.atomenfv2
    else:
        click.secho(msg, fg='bright_red')

try:
    import projectparallelprogrammeren.atomenf
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'atomenf')
    if not msg:
        import projectparallelprogrammeren.atomenf
    else:
        click.secho(msg, fg='bright_red')

try:
    import projectparallelprogrammeren.rng
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'rng')
    if not msg:
        import projectparallelprogrammeren.rng
    else:
        click.secho(msg, fg='bright_red')


from time import time_ns
import numpy as np
f90 = projectparallelprogrammeren.rng.my_f90_module
f901 = projectparallelprogrammeren.atomenf.f90_module
from projectparallelprogrammeren import atomen
from et_stopwatch import Stopwatch
import math
from statistics import stdev
from projectparallelprogrammeren import montecarlo_v0 as mc

class LCG:
	"""
	Linear congruential generator (LCG), gebaseerd op ET-rng.
	
	:param seed: Gebruikt standaard de huidige tijd om verschillende sequenties te berekenen.
	:param a: Parameter voor de LCG.
	:param b: Parameter voor de LCG.
	:param m: Parameter voor de LCG.
	"""
	#De parameters zijn grote getallen. Dit zorgt ervoor dat ze als het juiste type opgeslagen worden.
	UINT = np.uint64
	
	def __init__(self, seed=None, a=2147483629, b=2147483629, m=2**31-1):
		#seed instellen
		if seed is None:
			self.seed = LCG.UINT(time_ns())
		else:
			self.seed = LCG.UINT(seed)
		
		#parameters opslaan
		self.a = LCG.UINT(a)
		self.b = LCG.UINT(b)
		self.m = LCG.UINT(m)
		
		#sequentie initialiseren
		self.x = self.seed
	
	def __call__(self):
		"""
		:return: een willekeurig getal
		"""
		self.x = (self.a * self.x + self.b) % self.m
		return self.x
			
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
    
if __name__=="__main__":
	#voorlopig testcode
	"""print("Hello World!")
	test = LCG()
	c = test()
	print("Python rng:", c)
	print("Fortran rng:",f90.lcg1())"""
	#test geheel
	"""test = atomen.Atomen(5)
	with Stopwatch(message="Fortran"):
		pot = f901.ljpotalleatomen(test.getCoordinaten(), 5)
	with Stopwatch(message="Python"):
		pot2 = test.berekenLJPot()
	
	with Stopwatch(message="10x Fortran"):
		for i in range(10):
			test = atomen.Atomen(5)
			pot = f901.ljpotalleatomen(test.getCoordinaten(), 5)
			
	with Stopwatch(message="10x Python"):
		for i in range(10):
			test = atomen.Atomen(5)
			pot = test.berekenLJPot()"""
	"""with Stopwatch(message="10 atomen"):
		mc.simulatie(10,10)
	with Stopwatch(message="100 atomen"):
		mc.simulatie(100,10)
	with Stopwatch(message="1000 atomen"):
		mc.simulatie(1000,10)
	with Stopwatch(message="10000 atomen"):
		simulatie(10000,10)"""

	from importlib import import_module
	for i in range(4):
		#alle versies van de simulatie importeren en achtereenvolgens uitvoeren.
		version = f"montecarlo_v{i}"
		montecarlo = import_module(version)
		montecarlo.simulatie(100,100)


# eof
