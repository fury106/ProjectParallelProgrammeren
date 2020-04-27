# -*- coding: utf-8 -*-
"""
Package projectparallelprogrammeren
=======================================

A 'hello world' example.
"""
__version__ = "0.0.4"

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
	print("Hello World!")

# eof
