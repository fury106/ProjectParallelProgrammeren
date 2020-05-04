# -*- coding: utf-8 -*-
"""
Package projectparallelprogrammeren
=======================================

A 'hello world' example.
"""
__version__ = "0.0.9"

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
			
	
    
if __name__=="__main__":
	#voorlopig testcode
	"""print("Hello World!")
	test = LCG()
	c = test()
	print("Python rng:", c)
	print("Fortran rng:",f90.lcg1())"""
	#test geheel
	test = atomen.Atomen(5)
	with Stopwatch(message="Fortran"):
		pot = f901.ljpotalleatomen(test.getCoordinaten(), 5)
	with Stopwatch(message="Python"):
		pot2 = test.berekenLJPot()

# eof
